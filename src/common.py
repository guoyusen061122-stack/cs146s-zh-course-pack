#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C1 课程资料管线 · 公共基础设施。

只依赖 Python 标准库，保证任何装了 Python 3.9+ 的机器上都能跑，
不需要虚拟环境、不需要联网装包（除抓取那几步本身需要联网）。
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

# ---------------------------------------------------------------- 控制台编码
# Windows 默认 GBK 控制台会把中文和 • 之类的字符直接打崩，这里统一强制 UTF-8。
for _stream in ("stdout", "stderr"):
    try:
        getattr(sys, _stream).reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # pragma: no cover - 老版本 Python 没有 reconfigure
        pass

# ---------------------------------------------------------------- 路径
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC_DIR)

SOURCES = os.path.join(ROOT, "sources")
RAW = os.path.join(SOURCES, "raw")
SITE = os.path.join(SOURCES, "site")
REPO = os.path.join(SOURCES, "repo")
READINGS = os.path.join(SOURCES, "readings")
DOCS_SRC = os.path.join(SOURCES, "docs")

WORK = os.path.join(ROOT, "work")
REPORTS = os.path.join(ROOT, "reports")
GLOSSARY_DIR = os.path.join(ROOT, "glossary")
CONFIG = os.path.join(ROOT, "config")
LOGS = os.path.join(SRC_DIR, "logs")

# 原始素材不进版本库（版权 + 体积），但保留在本地供复跑。
MANIFEST = os.path.join(SOURCES, "manifest.json")

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 CS146S-zh-pipeline/1.0"
)


def ensure_dirs(*paths: str) -> None:
    for p in paths:
        os.makedirs(p, exist_ok=True)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


# 网页里出现 `&#xD83D;` 这类数字引用时，html.parser 会产出**孤立代理字符**，
# 它既不是合法 UTF-8 也不是合法 JSON，写盘时直接抛 UnicodeEncodeError。
# 这是抓取类管线的通病，统一在出口处清理，避免每个抽取器各写一遍。
_SURROGATE_RE = re.compile(r"[\ud800-\udfff]")


def sanitize(text: str) -> str:
    """去掉孤立代理字符等无法落盘的字符。"""
    if not text:
        return text
    return _SURROGATE_RE.sub("", text)


def write_json(path: str, obj, *, indent: int = 2) -> None:
    ensure_dirs(os.path.dirname(path))
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=indent, sort_keys=False)
        fh.write("\n")


def read_json(path: str, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write_text(path: str, text: str) -> None:
    ensure_dirs(os.path.dirname(path))
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(sanitize(text))


def read_text(path: str, default=None) -> str:
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def read_any_text(path: str, default: str = "") -> str:
    """读文本文件，自动处理 BOM 与 gzip。

    存在的意义：缓存里可能躺着**改代码之前**写下的旧字节（例如未解压的 Wayback 快照），
    直接 `open(encoding="utf-8")` 会抛 UnicodeDecodeError。读入口统一做一次净化，
    比要求调用方记得先清缓存可靠得多。
    """
    if not os.path.exists(path):
        return default
    with open(path, "rb") as fh:
        data = _maybe_gunzip(fh.read())
    if data[:3] == b"\xef\xbb\xbf":
        data = data[3:]
    return data.decode("utf-8", "replace")


def log(msg: str) -> None:
    print(msg, flush=True)


# ---------------------------------------------------------------- HTTP
def _maybe_gunzip(data: bytes) -> bytes:
    """透明解压 gzip。

    Wayback Machine 的 `id_` 原始快照会把**当年服务器返回的 gzip 字节**原样给你，
    不做解压就是一堆二进制乱码（本项目在 Medium 的存档上踩到：3.5 万"字符"全是乱码）。
    """
    if data[:2] != b"\x1f\x8b":
        return data
    import gzip

    try:
        return gzip.decompress(data)
    except Exception:  # noqa: BLE001
        try:
            import zlib

            return zlib.decompress(data, 16 + zlib.MAX_WBITS)
        except Exception:  # noqa: BLE001
            return data


class FetchResult:
    __slots__ = ("url", "status", "data", "from_cache", "error")

    def __init__(self, url, status, data, from_cache=False, error=None):
        self.url = url
        self.status = status
        self.data = data
        self.from_cache = from_cache
        self.error = error


def fetch(
    url: str,
    cache_path: str | None = None,
    *,
    use_cache: bool = True,
    retries: int = 3,
    timeout: int = 45,
    headers: dict | None = None,
    binary: bool = True,
    insecure: bool = False,
) -> FetchResult:
    """带磁盘缓存的 GET。

    设计要点：
    - 命中缓存直接返回，保证**重复运行不重复打服务器**，也让离线复跑可行；
    - 失败**重试后抛异常**，不静默返回空 —— 静默退化是本项目明确要避免的失败模式；
    - `insecure=True` 关闭证书校验，**只在对端证书链异常的兜底路径上使用**（见 s03）。
    """
    if cache_path and use_cache and os.path.exists(cache_path):
        with open(cache_path, "rb") as fh:
            return FetchResult(url, 200, _maybe_gunzip(fh.read()), from_cache=True)

    ctx = None
    if insecure:
        import ssl

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

    last_err = None
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                data = resp.read()
                status = resp.status
            data = _maybe_gunzip(data)
            if cache_path:
                ensure_dirs(os.path.dirname(cache_path))
                with open(cache_path, "wb") as fh:
                    fh.write(data)
            return FetchResult(url, status, data)
        except urllib.error.HTTPError as exc:  # 4xx/5xx：有些是预期内的（坏链）
            last_err = f"HTTP {exc.code} {exc.reason}"
            if exc.code in (400, 401, 403, 404, 410, 422):
                break  # 重试没有意义
        except Exception as exc:  # noqa: BLE001 - 网络异常种类多，统一收口
            last_err = f"{type(exc).__name__}: {exc}"
        if attempt < retries:
            time.sleep(1.5 * attempt)

    return FetchResult(url, 0, b"", error=last_err)


def fetch_text(url: str, cache_path: str | None = None, **kw) -> str:
    res = fetch(url, cache_path, **kw)
    if res.error and not res.data:
        raise RuntimeError(f"抓取失败 {url}: {res.error}")
    return res.data.decode("utf-8", "replace")


# ---------------------------------------------------------------- 运行账本
class Ledger:
    """记录每一步的输入 / 输出 / 哈希 / 结论，供 AI 日志与质检报告引用。

    这是"可追溯"的基础设施：任何数字都能追到是哪一次运行、哪一份输入产生的。
    """

    def __init__(self, step: str):
        self.step = step
        self.started = now_iso()
        self.t0 = time.time()
        self.items: list[dict] = []
        self.notes: list[str] = []

    def add(self, **kw) -> None:
        self.items.append(kw)

    def note(self, text: str) -> None:
        self.notes.append(text)
        log(f"  · {text}")

    def finish(self, summary: dict | None = None) -> dict:
        return {
            "step": self.step,
            "started_at": self.started,
            "finished_at": now_iso(),
            "elapsed_sec": round(time.time() - self.t0, 2),
            "items": self.items,
            "notes": self.notes,
            "summary": summary or {},
        }


def append_ledger(record: dict) -> None:
    """把本次运行追加到 work/ledger.jsonl（只追加，永不覆盖）。"""
    ensure_dirs(WORK)
    path = os.path.join(WORK, "ledger.jsonl")
    with open(path, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def slugify(text: str, max_len: int = 80) -> str:
    out = []
    for ch in text:
        if ch.isalnum() and ord(ch) < 128:
            out.append(ch.lower())
        elif ch in " -_/":
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")[:max_len] or "item"


def url_slug(url: str, max_len: int = 90) -> str:
    """URL → 干净的本地文件名主干（不含扩展名）。

    `host.tld/a/b.html` → `host-tld-a-b`
    点号转连字符、扩展名去掉，避免出现 `...teamshtml.html` 这种重复后缀。
    """
    from urllib.parse import urlparse

    p = urlparse(url.strip())
    host = re.sub(r"[^A-Za-z0-9]+", "-", p.netloc.lower()).strip("-")
    if "youtube.com" in p.netloc.lower() or "youtu.be" in p.netloc.lower():
        m = re.search(r"(?:^|[?&])v=([A-Za-z0-9_-]+)", p.query)
        if m:
            return f"youtube-{m.group(1)}"
    path = re.sub(r"\.(pdf|html?|txt|md|json|xml)$", "", p.path, flags=re.I)
    tail = re.sub(r"[^A-Za-z0-9]+", "-", path).strip("-")
    full = f"{host}-{tail}" if tail else host
    full = re.sub(r"-{2,}", "-", full).strip("-")
    return full[:max_len].strip("-") or "item"
