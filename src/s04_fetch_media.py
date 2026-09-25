#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S04 · 抓取讲义（Google Slides / Drive / Figma）与视频字幕。

课程讲义不是普通网页，而是 Google Slides / Figma 在线演示文稿。
本步用它们的**无鉴权导出端点**把讲义变成 PDF，从而进入统一的文本提取流程：

    Google Slides : https://docs.google.com/presentation/d/<ID>/export/pdf
    Google Drive  : https://drive.google.com/uc?export=download&id=<ID>

视频字幕：YouTube 的 timedtext 端点现在要求 `pot`（proof-of-origin token），
无该令牌一律返回空体；本环境又因沙箱限制装不了 yt-dlp（详见 README 已知缺口）。
本步仍然**完整地尝试并记录失败证据**，而不是假装视频不存在。
"""

from __future__ import annotations

import json
import os
import re
import sys
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402

COURSE = os.path.join(C.SITE, "course.json")


def slide_slug(term: str, week: int, sess_idx: int, lead: str, date: str) -> str:
    day = re.search(r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun)", date or "")
    md = re.search(r"(\d+)/(\d+)", date or "")
    stamp = f"{day.group(1).lower()}{md.group(1)}-{md.group(2)}" if day and md else f"s{sess_idx}"
    return C.slugify(f"{term}-w{week:02d}-{stamp}-{lead}", 80)


def gdrive_id(url: str) -> str | None:
    m = re.search(r"/(?:file|d)/([A-Za-z0-9_-]{20,})", url)
    return m.group(1) if m else None


def slides_id(url: str) -> str | None:
    m = re.search(r"/presentation/d/([A-Za-z0-9_-]+)", url)
    return m.group(1) if m else None


def collect(course: dict) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    slides, drive, figma, videos = [], [], [], []
    for term, t in course["terms"].items():
        for wi, w in enumerate(t["weeks"], 1):
            for si, s in enumerate(w["sessions"], 1):
                for link in s["links"]:
                    href, label = link.get("href", ""), link.get("label", "")
                    base = {
                        "term": term, "week": wi, "session_index": si,
                        "date": s["date"], "lead": s["lead"], "label": label,
                        "url": href,
                        "slug": slide_slug(term, wi, si, s["lead"], s["date"]),
                    }
                    if not href:
                        continue
                    if "docs.google.com/presentation" in href:
                        sid = slides_id(href)
                        if sid:
                            slides.append(dict(base, kind="google_slides", file_id=sid))
                    elif "drive.google.com" in href or "docs.google.com/file" in href:
                        did = gdrive_id(href)
                        if did:
                            drive.append(dict(base, kind="google_drive", file_id=did))
                    elif "figma.com" in href:
                        figma.append(dict(base, kind="figma"))
            for r in w["readings"]:
                if "youtu" in r.get("href", ""):
                    m = re.search(r"[?&]v=([A-Za-z0-9_-]{6,})", r["href"])
                    videos.append({
                        "kind": "youtube", "term": term, "week": wi,
                        "label": r.get("label", ""), "url": r["href"],
                        "video_id": m.group(1) if m else "",
                        "slug": C.slugify(f"yt-{m.group(1)}" if m else r.get("label", "video"), 60),
                    })
    # 去重（同一份讲义可能被两个学期引用）
    def dedup(items, keyfn):
        seen, out = set(), []
        for it in items:
            k = keyfn(it)
            if k in seen:
                continue
            seen.add(k)
            out.append(it)
        return out

    return (dedup(slides, lambda x: x["file_id"]), dedup(drive, lambda x: x["file_id"]),
            dedup(figma, lambda x: x["url"]), dedup(videos, lambda x: x["video_id"]))


def sniff_ext(data: bytes) -> str:
    """按内容判断扩展名。

    注意：Google Drive 的 `uc?export=download` 对 Google Docs 会**直接吐出 Markdown**，
    一开始只按 PDF/ZIP/JSON 三分支判断，会把一份正经文档误判成 .bin。
    """
    if data[:5] == b"%PDF-":
        return ".pdf"
    if data[:2] == b"PK":
        return ".zip"
    if data[:1] == b"{":
        return ".json"
    head = data[:600].decode("utf-8", "replace")
    if re.search(r"^\s*#{1,6}\s+\S", head, re.M):
        return ".md"
    printable = sum(1 for ch in head if ch.isprintable() or ch in "\r\n\t")
    if head and printable / max(len(head), 1) > 0.9:
        return ".txt"
    return ".bin"


def main() -> int:
    C.ensure_dirs(C.DOCS_SRC, C.WORK)
    ledger = C.Ledger("s04_fetch_media")
    manifest = C.read_json(C.MANIFEST, {}) or {}
    manifest.setdefault("sources", {})

    course = C.read_json(COURSE)
    if not course:
        raise SystemExit("缺少 sources/site/course.json，请先跑 s01_fetch_site.py")
    slides, drive, figma, videos = collect(course)
    C.log(f"[清单] 讲义 {len(slides)} 份 Google Slides ｜ {len(drive)} 份 Drive 文件 ｜ "
          f"{len(figma)} 份 Figma ｜ 视频 {len(videos)} 个")

    results: list[dict] = []

    # ---------- Google Slides ----------
    d = os.path.join(C.DOCS_SRC, "slides")
    C.ensure_dirs(d)
    for it in slides:
        cache = os.path.join(d, it["slug"] + ".pdf")
        url = f"https://docs.google.com/presentation/d/{it['file_id']}/export/pdf"
        res = C.fetch(url, cache, retries=2, timeout=90, insecure=True)
        entry = dict(it, status="FAILED", bytes=0, sha256="", cache="", error="",
                     note="")
        if res.data and len(res.data) > 1000:
            entry.update(status="OK", bytes=len(res.data),
                         sha256=C.sha256_bytes(res.data),
                         cache=os.path.relpath(cache, C.ROOT))
        else:
            entry["error"] = res.error or f"导出内容异常（{len(res.data)} 字节）"
        results.append(entry)
        C.log(f"  {'OK  ' if entry['status']=='OK' else 'FAIL'} slides  "
              f"{entry['bytes']:>9}B  {it['term']} w{it['week']:02d}  {it['lead'][:44]}")

    # ---------- Google Drive ----------
    d = os.path.join(C.DOCS_SRC, "drive")
    C.ensure_dirs(d)
    for it in drive:
        url = f"https://drive.google.com/uc?export=download&id={it['file_id']}"
        res = C.fetch(url, None, retries=2, timeout=90, insecure=True)
        entry = dict(it, status="FAILED", bytes=0, sha256="", cache="", error="", note="")
        if res.data and len(res.data) > 1000 and b"<html" not in res.data[:200].lower():
            ext = sniff_ext(res.data)
            cache = os.path.join(d, it["slug"] + ext)
            with open(cache, "wb") as fh:
                fh.write(res.data)
            entry.update(status="OK", bytes=len(res.data), sha256=C.sha256_bytes(res.data),
                         cache=os.path.relpath(cache, C.ROOT))
        else:
            entry["error"] = "需登录态或已限制下载权限（Drive 返回登录页）"
        results.append(entry)
        C.log(f"  {'OK  ' if entry['status']=='OK' else 'FAIL'} drive   "
              f"{entry['bytes']:>9}B  {it['label'][:22]:<24} {it['lead'][:38]}")

    # ---------- Figma ----------
    for it in figma:
        results.append(dict(it, status="SKIPPED", bytes=0, sha256="", cache="",
                            error="", note="Figma 讲稿需登录态才能导出，脚本不代抓；"
                                           "原始链接已在讲义索引中保留"))

    # ---------- YouTube ----------
    d = os.path.join(C.DOCS_SRC, "transcripts")
    C.ensure_dirs(d)
    for it in videos:
        note, error = "", ""
        watch = f"https://www.youtube.com/watch?v={it['video_id']}"
        res = C.fetch(watch, os.path.join(d, it["slug"] + ".watch.html"),
                      retries=1, timeout=60, insecure=True, use_cache=False)
        status = "FAILED"
        if res.data:
            m = re.search(rb'"captionTracks":(\[.*?\])', res.data)
            if m:
                try:
                    tracks = json.loads(m.group(1).decode("utf-8", "replace"))
                except Exception:  # noqa: BLE001
                    tracks = []
                note = f"页面含 {len(tracks)} 条字幕轨"
                for t in tracks:
                    if not t.get("languageCode", "").startswith("en"):
                        continue
                    sub = C.fetch(t["baseUrl"] + "&fmt=json3", None,
                                  retries=1, timeout=40, insecure=True, use_cache=False)
                    if sub.data:
                        path = os.path.join(d, it["slug"] + ".json3")
                        with open(path, "wb") as fh:
                            fh.write(sub.data)
                        status = "OK"
                        results.append(dict(it, status="OK", bytes=len(sub.data),
                                            sha256=C.sha256_bytes(sub.data),
                                            cache=os.path.relpath(path, C.ROOT),
                                            error="", note=note))
                        break
                    error = "timedtext 返回空体：YouTube 现要求 pot(proof-of-origin) 令牌"
            else:
                error = "页面未包含 captionTracks"
        else:
            error = res.error or "无法获取视频页面"
        if status != "OK":
            results.append(dict(it, status="FAILED", bytes=0, sha256="", cache="",
                                error=error, note=note))

    # ---------- 汇总 ----------
    it_index = {
        "collected_at": C.now_iso(),
        "total": len(results),
        "by_status": {},
        "items": results,
    }
    for r in results:
        it_index["by_status"][r["status"]] = it_index["by_status"].get(r["status"], 0) + 1
        manifest["sources"]["media:" + r.get("slug", r["url"])] = {
            "kind": r["kind"], "status": r["status"], "bytes": r["bytes"],
            "sha256": r.get("sha256", ""), "cached_at": C.now_iso(),
            "cache": r.get("cache", ""), "error": r.get("error", ""),
            "url": r["url"],
        }
        ledger.add(kind=r["kind"], slug=r.get("slug"), status=r["status"],
                   bytes=r["bytes"], url=r["url"], error=r.get("error", ""))

    ok = it_index["by_status"].get("OK", 0)
    skipped = it_index["by_status"].get("SKIPPED", 0)
    failed = it_index["by_status"].get("FAILED", 0)
    C.log(f"\n[结果] 成功 {ok} / 失败 {failed} / 跳过 {skipped} / 共 {len(results)}")
    for r in results:
        if r["status"] != "OK":
            C.log(f"   {r['status']:<8} {r['kind']:<14} {r.get('lead', r.get('label',''))[:40]:<42} "
                  f"→ {r.get('error') or r.get('note','')}")

    C.write_json(os.path.join(C.DOCS_SRC, "index.json"), it_index)
    C.write_json(C.MANIFEST, manifest)
    C.append_ledger(ledger.finish(it_index["by_status"]))
    C.log("完成 · 输出 sources/docs/index.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
