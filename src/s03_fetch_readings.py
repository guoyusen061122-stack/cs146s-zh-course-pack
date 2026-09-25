#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S03 · 批量抓取课程指定的阅读素材（文章 / PDF / 仓库文件）。

挑战原话是"定位一手来源……批量抓取并归档"。这一步就是"批量"两个字的兑现：
从 syllabus 里把两个学期**所有** readings 链接拉出来，去重、分类、逐个抓取。

多级兜底（本步的核心工程）
--------------------------
真实世界里"抓不到"有一堆不同的原因，一刀切地记 FAILED 会丢掉信息。
本步为每条素材准备了一条**按侵入性递增排列**的兜底链，并记录**最终是哪一级救回来的**：

  1. direct        直连（默认，校验证书）
  2. insecure-tls  仅在对端证书链异常时降级关闭校验（本机网络经透明代理，见 README 已知缺口）
  3. alt-host      改用同一内容的官方替代端点（如 arxiv.org → export.arxiv.org）
  4. wayback       Wayback Machine 存档快照（原站已下线时的最后手段，属第三方存档）
  5. reader-proxy  文本代理读取（第三方；仅在前述全部失败后使用，并如实标注）

抓不到的**不伪造**：状态记 FAILED/GONE，原因记下来，最终进 README 的「已知缺口」。
"""

from __future__ import annotations

import json
import os
import re
import sys
from urllib.parse import urlparse, urlunparse, urljoin, quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402

COURSE = os.path.join(C.SITE, "course.json")

# 页面已消失的特征（作者删稿 / 站点下线）
GONE_MARKERS = (
    "PAGE NOT FOUND",
    "page not found",
    "This page could not be found",
    "404 Not Found",
    "The page you are looking for",
)

FETCHABLE = {"html", "pdf", "github_file"}

# 一篇文章的正文至少该有多少字符？低于这个量级基本可以断定拿到的是空壳/付费墙预览。
# 400 太宽松：Substack 的登录壳也能产出 1400 字符的导航文字，会被误判为成功。
MIN_HTML_YIELD = 1500


def normalise_url(url: str) -> str:
    """归一化：去 fragment、去跟踪参数，让同一篇文章只抓一次。"""
    p = urlparse(url.strip())
    query = p.query
    if p.netloc.endswith("youtube.com"):
        # 注意：urlparse 已经把 "?" 剥掉了，所以这里不能用 [?&] 打头匹配，
        # 否则会匹配不到、把 query 清空，导致不同视频被归一化成同一个 key。
        m = re.search(r"(?:^|[?&])v=([^&]+)", query)
        query = "v=" + m.group(1) if m else query
    else:
        query = "&".join(
            kv for kv in query.split("&")
            if kv and not kv.lower().startswith(("utm_", "ref=", "tab=", "si="))
        )
    return urlunparse((p.scheme, p.netloc, p.path.rstrip("/") or "/", "", query, ""))


def classify(url: str) -> str:
    p = urlparse(url)
    host = p.netloc.lower()
    path = p.path.lower()
    if "youtube.com" in host or "youtu.be" in host:
        return "video"
    if host == "docs.google.com" and "/presentation/" in path:
        return "slides"
    if (host == "docs.google.com" and "/file/" in path) or host == "drive.google.com":
        return "drive_file"
    if "figma.com" in host:
        return "figma_slides"
    if path.endswith(".pdf") or host in ("arxiv.org", "www.arxiv.org"):
        return "pdf"
    if host in ("github.com", "www.github.com"):
        segs = [s for s in p.path.split("/") if s]
        if len(segs) >= 4 and segs[2] in ("blob", "tree", "raw"):
            return "github_file"
        return "github_repo"
    if host in ("x.com", "twitter.com"):
        return "social_post"
    return "html"


SKIP_NOTE = {
    "video": "视频：由 s04 抓取字幕后纳入翻译",
    "slides": "Google Slides 讲义：由 s04 统一导出（避免重复抓取）",
    "drive_file": "Google Drive 文件：需登录态，脚本不代抓",
    "figma_slides": "Figma 讲稿：需登录态，脚本不代抓",
    "github_repo": "GitHub 仓库主页：属代码素材，登记不翻译（README 类文档另行处理）",
    "social_post": "社交平台帖子：需登录态，脚本不代抓",
}


def url_slug(url: str) -> str:
    return C.url_slug(url)


# ---------------------------------------------------------------- 兜底链
def wayback_snapshots(url: str, limit: int = 3) -> list[tuple[str, str]]:
    """列出 Wayback 的可用快照，按**由旧到新**返回。

    为什么要多个：站点的内容会随时间变化。真实例子——Substack 上那篇
    《Specs Are the New Source Code》后来改成了付费订阅，最新快照只剩预览；
    早年的快照才留着全文。所以别只取最新一条，把几个都拿来比一比。
    """
    cdx = ("http://web.archive.org/cdx/search/cdx?url="
           + quote(url, safe="")
           + "&output=json&limit=40&filter=statuscode:200&collapse=digest")
    res = C.fetch(cdx, None, retries=2, timeout=40, insecure=True)
    if not res.data:
        return []
    try:
        rows = json.loads(res.data.decode("utf-8", "replace"))
    except Exception:  # noqa: BLE001
        return []
    stamps = [r[1] for r in rows[1:] if len(r) > 1]
    if not stamps:
        return []
    stamps = stamps[:1] + stamps[len(stamps) // 2 : len(stamps) // 2 + 1] + stamps[-1:]
    seen, out = set(), []
    for ts in stamps:
        if ts in seen:
            continue
        seen.add(ts)
        out.append((ts, f"https://web.archive.org/web/{ts}id_/{url}"))
    return out[:limit]


def alt_hosts(url: str, kind: str) -> list[tuple[str, str]]:
    """同一内容的官方替代端点。"""
    p = urlparse(url)
    out = []
    if "arxiv.org" in p.netloc.lower():
        out.append((urlunparse(p._replace(netloc="export.arxiv.org")), "alt-host:export.arxiv.org"))
    if p.scheme == "https":
        out.append((urlunparse(p._replace(scheme="http")), "alt-host:http"))
    return out


def looks_gone(body: bytes) -> bool:
    if not body or len(body) > 200_000:
        return False
    text = body.decode("utf-8", "replace")
    return sum(1 for m in GONE_MARKERS if m in text) >= 1


def find_markdown_alternate(body: bytes, base_url: str) -> str | None:
    """找出页面声明的 Markdown 原文地址。

    不少文档站（Mintlify / Docusaurus 等）会在 <head> 里声明：

        <link rel="alternate" type="text/markdown" href="/docs/en/best-practices.md"/>

    对"把资料译成中文"这件事来说，这是**比抓 HTML 更干净的一手来源**：
    没有导航、没有脚本、没有 CSS 汤，段落边界就是作者写的段落。
    本项目在 Anthropic 的 Claude Code 文档页上踩过坑 —— 该页正文全靠客户端渲染，
    抓 HTML 一个字都提不出来，改用它声明的 Markdown 原文后一次拿到干净全文。
    """
    head = body[:600_000].decode("utf-8", "replace")
    base = base_url
    # 相对 href 必须相对**页面声明的 canonical** 解析，而不是相对抓取时的 URL。
    # 例如 anthropic.com/engineering/claude-code-best-practices 实际返回的是
    # code.claude.com 的文档页，其 markdown 链接是 /docs/en/best-practices.md，
    # 用抓取 URL 拼会 404。
    cm = re.search(r'<link\b[^>]*rel=["\']canonical["\'][^>]*>', head, re.I)
    if cm:
        hm = re.search(r'href=["\']([^"\']+)["\']', cm.group(0), re.I)
        if hm:
            base = urljoin(base_url, hm.group(1))
    for tag in re.findall(r"<link\b[^>]*>", head, re.I):
        if "markdown" not in tag.lower() or "alternate" not in tag.lower():
            continue
        m = re.search(r'href=["\']([^"\']+)["\']', tag, re.I)
        if m:
            return urljoin(base, m.group(1))
    return None


def _html_yield(data: bytes) -> int:
    """估算 HTML 能产出多少正文字符（用于识别"抓到了空壳"）。"""
    from htmlmd import html_to_blocks, page_text

    text = data.decode("utf-8", "replace")
    blocks = html_to_blocks(text)
    chars = sum(
        len(b.get("text", "") or "") + sum(len(i) for i in b.get("items", []))
        for b in blocks
    )
    return max(chars, len(page_text(text)))


def _acceptable(data: bytes, kind: str) -> tuple[bool, str]:
    if not data:
        return False, "空响应"
    if kind in ("html", "github_file") and b"<html" in data[:4000].lower():
        try:
            chars = _html_yield(data)
        except Exception as exc:  # noqa: BLE001
            return True, f"体检异常({type(exc).__name__})，按可用处理"
        if chars < MIN_HTML_YIELD:
            return False, f"正文仅 {chars} 字符，疑为 JS 渲染空壳或付费墙预览"
        return True, ""
    if kind == "pdf" and not data.startswith(b"%PDF"):
        return False, "返回的不是 PDF"
    if len(data) < 400:
        return False, f"内容过短（{len(data)} 字节）"
    return True, ""


def fetch_with_fallback(url: str, cache: str, kind: str) -> tuple[C.FetchResult, str, str]:
    """按侵入性递增的顺序尝试，返回 (结果, 策略, 说明)。

    关键点：**"HTTP 200 但正文为空壳"必须继续兜底**。

    这是抓取类管线最隐蔽的失败：请求成功、状态码漂亮、字节数也不小，但正文由 JS 渲染，
    HTML 里其实什么都没有。只看状态码的管线会把空壳当成成功收下，
    到翻译环节才发现"没东西可译" —— 挑战里把这类现象叫「环境静默退化」。
    所以这里对每次结果做一次**正文产出量体检**，不达标就换下一条路。

    兜底链（侵入性递增）：
      direct → insecure-tls → alt-host → site-fallback(config) → wayback → reader-proxy
    """
    attempts: list[str] = []
    best: tuple[C.FetchResult, str, str] | None = None

    def cache_for(strategy: str, fb_kind: str = "") -> str | None:
        """每条兜底路线用**独立的缓存文件**。

        踩过的坑：所有候选共用同一个 cache 路径时，第二次尝试会命中第一次写下的缓存，
        于是"兜底"其实什么都没抓 —— 表现就是明明配了备用来源，结果还是拿到原来的空壳。
        """
        if not cache:
            return None
        base, ext = os.path.splitext(cache)
        if fb_kind == "markdown":
            return base + ".md"
        if strategy == "direct":
            return cache
        safe = re.sub(r"[^a-zA-Z0-9]+", "-", strategy).strip("-")
        return f"{base}.{safe}{ext}"

    def attempt(candidate: str, strategy: str, note: str, fb_kind: str = "") -> bool:
        nonlocal best
        res = C.fetch(candidate, cache_for(strategy, fb_kind), retries=2, timeout=60,
                      insecure=True)
        if not res.data or res.error:
            attempts.append(f"{strategy}→{res.error}")
            return False
        if fb_kind == "substack_json":
            res = rewrite_as_html(res)
        ok, why = _acceptable(res.data, kind)
        if ok:
            best = (res, strategy, note)
            return True
        attempts.append(f"{strategy}→{why}")
        if best is None or len(res.data) > len(best[0].data):
            best = (res, strategy + "·空壳", ((note + "；") if note else "") + why)
        return False

    # 1) 直连（默认校验证书）
    res = C.fetch(url, cache, retries=2, timeout=40)
    if res.data and not res.error:
        ok, why = _acceptable(res.data, kind)
        if ok:
            return res, "direct", ""
        best = (res, "direct·空壳", why)
        attempts.append(f"direct→{why}")
    else:
        attempts.append(f"direct→{res.error}")
        # 2) 只在证书链异常时才值得降级关闭校验
        if res.error and ("SSL" in res.error or "CERTIFICATE" in res.error.upper()):
            r2 = C.fetch(url, cache, retries=1, timeout=40, insecure=True)
            if r2.data:
                ok, why = _acceptable(r2.data, kind)
                if ok:
                    return r2, "insecure-tls", "对端证书链在本网络下校验失败，降级跳过校验取回"
                attempts.append(f"insecure→{why}")

    # 3) 官方替代端点（如 arxiv.org → export.arxiv.org）
    for alt, label in alt_hosts(url, kind):
        if attempt(alt, label, f"改用替代端点 {alt}"):
            return best

    # 4) 站点专用一手来源（config/fallbacks.json，逐条写明理由）
    for fb in site_fallbacks(url):
        if attempt(fb["url"], "site-fallback", fb.get("note", ""), fb.get("kind", "")):
            return best

    # 5) Wayback Machine 存档：多个快照全取，挑正文最多的那个
    snaps = wayback_snapshots(url)
    if snaps:
        cands: list[tuple[int, C.FetchResult, str]] = []
        for ts, snap_url in snaps:
            res_w = C.fetch(snap_url, cache_for("wayback", "") or None,
                            retries=2, timeout=60, insecure=True, use_cache=False)
            if not res_w.data:
                attempts.append(f"wayback@{ts}→{res_w.error}")
                continue
            ok, why = _acceptable(res_w.data, kind)
            if ok:
                cands.append((_html_yield(res_w.data) if kind == "html" else len(res_w.data),
                              res_w, ts))
            else:
                attempts.append(f"wayback@{ts}→{why}")
        if cands:
            cands.sort(key=lambda x: -x[0])
            best = (cands[0][1], "wayback",
                    f"原站正文不可得，在 {len(snaps)} 个存档快照中取正文最多的 {cands[0][2]}")
            return best
    else:
        attempts.append("wayback→无存档")

    # 6) 文本代理（第三方，最后手段）
    if attempt("https://r.jina.ai/" + url, "reader-proxy",
               "原站反爬，经第三方文本代理取回（内容可能与原文有出入）"):
        return best

    if best is not None:
        return best
    return C.FetchResult(url, 0, b"", error=" | ".join(attempts[-4:])), "failed", ""


def rewrite_as_html(res: C.FetchResult) -> C.FetchResult:
    """Substack 的 API 返回 JSON，取出 body_html 当 HTML 用，后续流程无需特判。"""
    try:
        payload = json.loads(res.data.decode("utf-8", "replace"))
        body = payload.get("body_html") or ""
        if not body:
            return res
        wrapped = f"<html><body><article>{body}</article></body></html>"
        return C.FetchResult(res.url, res.status, wrapped.encode("utf-8"))
    except Exception:  # noqa: BLE001
        return res


def _fallback_kind(original_url: str, candidate: str) -> str:
    for fb in site_fallbacks(original_url):
        if fb["url"] == candidate:
            return fb.get("kind", "")
    return ""


def site_fallbacks(url: str) -> list[dict]:
    cfg = C.read_json(os.path.join(C.CONFIG, "fallbacks.json"), {}) or {}
    return [x for x in cfg.get(url, []) if isinstance(x, dict) and x.get("url")]


def collect() -> list[dict]:
    course = C.read_json(COURSE)
    if not course:
        raise SystemExit("缺少 sources/site/course.json，请先跑 s01_fetch_site.py")
    seen: dict[str, dict] = {}
    for term, t in course["terms"].items():
        for wi, w in enumerate(t["weeks"], 1):
            for r in w["readings"]:
                url = r.get("href", "")
                if not url:
                    continue
                key = normalise_url(url)
                item = seen.setdefault(key, {
                    "url": url, "key": key, "label": r.get("label", ""),
                    "kind": classify(url), "years": [], "weeks": [],
                })
                if term not in item["years"]:
                    item["years"].append(term)
                tag = f"{term}/W{wi}"
                if tag not in item["weeks"]:
                    item["weeks"].append(tag)
                if not item["label"] and r.get("label"):
                    item["label"] = r["label"]
    return sorted(seen.values(), key=lambda x: (x["kind"], x["url"]))


def main() -> int:
    C.ensure_dirs(C.READINGS, C.WORK)
    ledger = C.Ledger("s03_fetch_readings")
    manifest = C.read_json(C.MANIFEST, {}) or {}
    manifest.setdefault("sources", {})

    items = collect()
    by_kind: dict[str, int] = {}
    for it in items:
        by_kind[it["kind"]] = by_kind.get(it["kind"], 0) + 1
    C.log(f"[清单] 去重后 {len(items)} 条：" +
          "  ".join(f"{k}={v}" for k, v in sorted(by_kind.items())))

    out_dir = os.path.join(C.READINGS, "raw")
    C.ensure_dirs(out_dir)
    results = []

    for it in items:
        slug, kind = url_slug(it["url"]), it["kind"]
        entry = dict(it, slug=slug, status="SKIPPED", strategy="",
                     bytes=0, sha256="", cache="", error="", note="")

        if kind not in FETCHABLE:
            entry["note"] = SKIP_NOTE.get(kind, "")
            results.append(entry)
            continue

        ext = ".pdf" if kind == "pdf" else ".html"
        cache = os.path.join(out_dir, slug + ext)
        url = it["url"]
        if kind == "github_file":
            p = urlparse(url)
            segs = [s for s in p.path.split("/") if s]
            if len(segs) >= 5 and segs[2] == "blob":
                url = (f"https://raw.githubusercontent.com/{segs[0]}/{segs[1]}/"
                       f"{segs[3]}/{'/'.join(segs[4:])}")
                cache = os.path.join(out_dir, slug + ".txt")

        res, strategy, note = fetch_with_fallback(url, cache, kind)
        if res.data and strategy != "failed":
            gone = looks_gone(res.data) and strategy in ("direct", "insecure-tls")
            shell = strategy.endswith("·空壳")
            entry.update(
                status="GONE" if gone else ("SHELL" if shell else "OK"),
                strategy=strategy, note=note,
                bytes=len(res.data), sha256=C.sha256_bytes(res.data),
                cache=os.path.relpath(cache, C.ROOT), final_url=url,
            )
            if gone:
                entry["error"] = "页面已不存在（原文被删除或下线）"
            elif shell:
                entry["error"] = note or "所有已知取法都只能拿到空壳"
            # 页面若声明了 Markdown 原文，优先取它（文本更干净）
            if entry["status"] == "OK" and kind == "html":
                alt = find_markdown_alternate(res.data, url)
                if alt:
                    md_cache = os.path.join(out_dir, slug + ".md")
                    md_res, md_strategy, _ = fetch_with_fallback(alt, md_cache, "html")
                    if md_res.data and md_strategy != "failed":
                        entry["md_alternate"] = alt
                        entry["md_cache"] = os.path.relpath(md_cache, C.ROOT)
                        entry["md_bytes"] = len(md_res.data)
                        entry["md_sha256"] = C.sha256_bytes(md_res.data)
                        if not note:
                            entry["note"] = "该站声明了 Markdown 原文，已改用原文而非 HTML"
        else:
            entry.update(status="FAILED", strategy="failed",
                         error=res.error or "空响应", final_url=url)

        manifest["sources"][it["key"]] = {
            "kind": "reading_" + kind, "status": entry["status"],
            "strategy": entry["strategy"], "bytes": entry["bytes"],
            "sha256": entry["sha256"], "cached_at": C.now_iso(),
            "cache": entry.get("cache", ""), "error": entry["error"],
        }
        ledger.add(slug=entry["slug"], kind=kind, status=entry["status"],
                   strategy=entry["strategy"], bytes=entry["bytes"], url=it["url"])
        mark = {"OK": "OK  ", "GONE": "GONE", "FAILED": "FAIL", "SHELL": "SHLL"}[entry["status"]]
        C.log(f"  {mark} {kind:<12} {strategy:<14} {entry['bytes']:>8}B  "
              f"{it['label'][:32]:<34} {it['url'][:58]}")
        results.append(entry)

    ok = sum(1 for r in results if r["status"] == "OK")
    gone = [r for r in results if r["status"] == "GONE"]
    shells = [r for r in results if r["status"] == "SHELL"]
    failed = [r for r in results if r["status"] == "FAILED"]
    skipped = [r for r in results if r["status"] == "SKIPPED"]
    by_strategy: dict[str, int] = {}
    for r in results:
        by_strategy[r["strategy"]] = by_strategy.get(r["strategy"], 0) + 1

    C.log(f"\n[结果] 成功 {ok} / 空壳 {len(shells)} / 已消失 {len(gone)} / "
          f"失败 {len(failed)} / 分类跳过 {len(skipped)} / 共 {len(results)}")
    C.log(f"[策略] " + "  ".join(f"{k}={v}" for k, v in sorted(by_strategy.items())))
    for r in shells + gone + failed:
        C.log(f"   {r['status']:<6} {r['url'][:70]}  → {r['error']}")

    C.write_json(os.path.join(C.READINGS, "index.json"), {
        "collected_at": C.now_iso(), "total": len(results), "ok": ok,
        "shell": len(shells), "gone": len(gone), "failed": len(failed),
        "skipped": len(skipped), "by_kind": by_kind,
        "by_strategy": by_strategy, "items": results,
    })
    C.write_json(C.MANIFEST, manifest)
    C.append_ledger(ledger.finish({
        "total": len(results), "ok": ok, "shell": len(shells), "gone": len(gone),
        "failed": len(failed), "skipped": len(skipped), "by_strategy": by_strategy,
    }))
    C.log("完成 · 输出 sources/readings/index.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
