#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S01 · 抓取课程官网并结构化为 JSON。

挑战要求"定位一手来源"。课程官网 themodernsoftware.dev 是**纯客户端渲染**的
Next.js 应用：HTML 里只有外壳，真正的课程大纲 / FAQ / 评分标准内联在
`/_next/static/chunks/*.js` 里。

本步骤做的事
------------
1. 抓 `/`（当前学期）与 `/fall2025`（往期学期）两个页面，存原始 HTML；
2. 解析出两页引用的全部 JS chunk 并抓取存档（原文证据）；
3. 从 chunk 中提取：weeks / grading / team / FAQ；
4. **不硬编码压缩变量名**：先从 bundle 里解析出
   `activeTerm === "<术语>" ? <A> : <B>` 的映射关系，再按映射取值，
   这样站点重新构建后脚本依然能自证是否取对了学期；
5. 从 SSR 出来的 HTML 里提取 Overview 正文（这部分服务端渲染了，不必解析 React）；
6. 全部结果写入 sources/site/，并在 sources/manifest.json 记录 URL、字节数、SHA-256。

产出
----
sources/raw/site/index.html, fall2025.html, js/*.js
sources/site/course.json          —— 两个学期的完整结构化数据
sources/site/overview_<term>.md   —— 官网 Overview 的英文 Markdown
sources/manifest.json             —— 素材账本（累积写入）
"""

from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402
import jslit  # noqa: E402
from htmlmd import html_to_markdown  # noqa: E402

BASE = "https://themodernsoftware.dev"
PAGES = [
    ("fall2026", BASE + "/"),
    ("fall2025", BASE + "/fall2025"),
]


def gather_chunks(html: str) -> list[str]:
    """从页面 HTML 里取出所有 JS chunk 的路径。"""
    srcs = re.findall(r'src="(/_next/static/[^"]+\.js[^"]*)"', html)
    out, seen = [], set()
    for s in srcs:
        clean = s.split("?")[0]
        if clean not in seen:
            seen.add(clean)
            out.append(s)
    return out


def derive_term_mapping(chunk: str, terms: list[str]) -> dict:
    """从压缩产物里解析"学期 → 变量"的映射，而不是硬编码变量名。

    目标片段形如：
        CourseSite",0,function({activeTerm:e}){let o="fall2026"===e, ...
        "syllabus"===n&&(0,t.jsx)(ej,{weeks:o?eP:eA,grading:o?eT:e_})
        "overview"===n&&(0,t.jsx)(ev,{team:o?eC:eS})
    """
    m = re.search(
        r'CourseSite",\s*\d+\s*,\s*function\s*\(\s*\{\s*activeTerm\s*:\s*(\w+)\s*\}'
        r"\s*\)\s*\{\s*let\s+(\w+)\s*=\s*\"([^\"]+)\"\s*===",
        chunk,
    )
    if not m:
        raise RuntimeError("无法从 bundle 中解析 CourseSite 的学期判断，站点结构可能已变")
    _prop, flag, active_literal = m.group(1), m.group(2), m.group(3)

    def pick(pattern: str, what: str):
        mm = re.search(pattern, chunk)
        if not mm:
            raise RuntimeError(f"无法解析 {what} 的学期映射")
        groups = mm.groups()
        cond = groups[0]
        if cond != flag:
            raise RuntimeError(f"{what} 的分支变量 {cond} 与学期判断变量 {flag} 不一致")
        return groups[1], groups[2]  # (active, other)

    weeks_a, weeks_o = pick(
        r"weeks:\s*(\w+)\s*\?\s*(\w+)\s*:\s*(\w+)\s*,\s*grading", "weeks"
    )
    grade_a, grade_o = pick(r"grading:\s*(\w+)\s*\?\s*(\w+)\s*:\s*(\w+)", "grading")
    team_a, team_o = pick(r"team:\s*(\w+)\s*\?\s*(\w+)\s*:\s*(\w+)", "team")

    others = [t for t in terms if t != active_literal]
    other_literal = others[0] if others else "other"
    return {
        "flag_var": flag,
        "active_literal": active_literal,
        "other_literal": other_literal,
        "weeks": {active_literal: weeks_a, other_literal: weeks_o},
        "grading": {active_literal: grade_a, other_literal: grade_o},
        "team": {active_literal: team_a, other_literal: team_o},
    }


def extract_faq(chunk: str) -> list[dict]:
    """FAQ 数组的元素形如 {q:"...",a:"..."}，按内容特征定位。"""
    items = jslit.extract_by_anchor(chunk, '{q:"')
    return [{"q": i["q"], "a": i["a"]} for i in items]


def normalise_weeks(weeks: list[dict]) -> list[dict]:
    out = []
    for w in weeks:
        out.append(
            {
                "title": w.get("title", ""),
                "topics": w.get("topics", []),
                "readings": w.get("reading", []),
                "assignments": w.get("assignment", []),
                "sessions": [
                    {
                        "date": s.get("date", ""),
                        "lead": s.get("lead", ""),
                        "profile": s.get("profile", ""),
                        "links": s.get("links", []),
                    }
                    for s in w.get("sessions", [])
                ],
            }
        )
    return out


def main() -> int:
    C.ensure_dirs(C.RAW, os.path.join(C.RAW, "site", "js"), C.SITE, C.WORK)
    ledger = C.Ledger("s01_fetch_site")
    manifest = C.read_json(C.MANIFEST, {}) or {}
    manifest.setdefault("sources", {})

    # ---------- 1. 页面 HTML ----------
    htmls: dict[str, str] = {}
    for term, url in PAGES:
        cache = os.path.join(C.RAW, "site", f"{term}.html")
        text = C.fetch_text(url, cache)
        htmls[term] = text
        digest = C.sha256_text(text)
        ledger.add(kind="page", term=term, url=url, bytes=len(text.encode()),
                   sha256=digest, cache=os.path.relpath(cache, C.ROOT))
        manifest["sources"][url] = {
            "kind": "site_page", "term": term, "bytes": len(text.encode()),
            "sha256": digest, "cached_at": C.now_iso(),
            "cache": os.path.relpath(cache, C.ROOT),
        }
        C.log(f"[页面] {term:<9} {url}  {len(text):>7} 字符  sha256={digest[:12]}")

    # ---------- 2. JS chunk ----------
    chunk_paths: dict[str, str] = {}
    for _term, url in PAGES:
        for src in gather_chunks(htmls[_term]):
            clean = src.split("?")[0]
            if clean in chunk_paths:
                continue
            cache = os.path.join(C.RAW, "site", "js", os.path.basename(clean))
            res = C.fetch(BASE + src, cache)
            if res.error and not res.data:
                C.log(f"[JS ] 失败 {src}: {res.error}")
                continue
            chunk_paths[clean] = cache
    C.log(f"[JS ] 共 {len(chunk_paths)} 个 chunk 已归档")

    # ---------- 3. 找到承载课程内容的那个 chunk ----------
    carrier = None
    for clean, path in chunk_paths.items():
        body = C.read_text(path, "")
        if "CourseSite" in body and 'title:"Week 1' in body:
            carrier = (clean, body)
            break
    if not carrier:
        C.log("!! 没有找到承载课程内容的 chunk，站点结构可能变了")
        return 2
    chunk_name, chunk = carrier
    manifest["sources"][BASE + "/_next/static/chunks/" + chunk_name] = {
        "kind": "site_bundle", "bytes": len(chunk.encode()),
        "sha256": C.sha256_text(chunk), "cached_at": C.now_iso(),
        "cache": os.path.relpath(chunk_paths[chunk_name], C.ROOT),
    }
    ledger.add(kind="bundle", chunk=chunk_name, bytes=len(chunk.encode()),
               sha256=C.sha256_text(chunk))
    C.log(f"[JS ] 课程内容位于 {chunk_name}（{len(chunk)} 字符）")

    # ---------- 4. 学期映射 + 结构化提取 ----------
    terms = [t for t, _ in PAGES]
    mapping = derive_term_mapping(chunk, terms)
    C.log(f"[映射] activeTerm === \"{mapping['active_literal']}\" → "
          f"weeks={mapping['weeks']}  grading={mapping['grading']}  team={mapping['team']}")

    faq_raw = extract_faq(chunk)
    C.log(f"[FAQ ] {len(faq_raw)} 条")

    course: dict = {
        "source": BASE,
        "fetched_at": C.now_iso(),
        "bundle": chunk_name,
        "term_mapping": mapping,
        "terms": {},
    }
    for term, url in PAGES:
        weeks = jslit.extract_assignment(chunk, mapping["weeks"][term])
        grading = jslit.extract_assignment(chunk, mapping["grading"][term])
        team = jslit.extract_assignment(chunk, mapping["team"][term])
        overview_md = html_to_markdown(htmls[term])
        course["terms"][term] = {
            "url": url,
            "weeks": normalise_weeks(weeks),
            "grading": grading,
            "team": team,
            "faq": faq_raw,
            "overview_markdown": overview_md,
        }
        readings = sum(len(w["readings"]) for w in course["terms"][term]["weeks"])
        slides = sum(
            len([l for l in s["links"] if "presentation" in l.get("href", "")])
            for w in course["terms"][term]["weeks"] for s in w["sessions"]
        )
        C.log(f"[学期] {term}: {len(weeks)} 周 / {readings} 条阅读 / "
              f"{slides} 份讲义链接 / {len(overview_md)} 字符 Overview")
        ledger.add(kind="term", term=term, weeks=len(weeks), readings=readings,
                   slides=slides, overview_chars=len(overview_md))

        C.write_text(os.path.join(C.SITE, f"overview_{term}.md"), overview_md)
        C.write_json(
            os.path.join(C.SITE, f"syllabus_{term}.json"),
            course["terms"][term]["weeks"],
        )

    C.write_json(os.path.join(C.SITE, "course.json"), course)
    C.write_json(C.MANIFEST, manifest)

    rec = ledger.finish({
        "terms": len(course["terms"]),
        "faq": len(faq_raw),
        "bundle": chunk_name,
        "chunks_archived": len(chunk_paths),
    })
    C.append_ledger(rec)
    C.log(f"\n完成 · 输出 {os.path.relpath(os.path.join(C.SITE,'course.json'), C.ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
