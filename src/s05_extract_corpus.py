#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S05 · 把全部素材统一抽取成规范化的英文 Markdown（语料层）。

这一步是"信息处理管线"的中枢：上游是形态各异的一手素材（HTML 文章、PDF 讲义、
GitHub 仓库文档、客户端渲染的官网数据），下游要的是**结构一致、可切段、可对照翻译**
的语料。

统一后的形态（`corpus/en/<slug>.md`）
------------------------------------
- 只有一个 H1 标题，层级从 H2 开始，保证中英对照时结构能逐块对齐；
- 代码块原样保留（不翻译），链接原样保留（译者只动文字）；
- PDF 按页/按幻灯片切分为 `## Slide N` / `## Page N`，方便定位与抽检；
- 每份语料在 `corpus/index.json` 里都有出处（URL / 仓库路径 / commit）、
  字符数、块数，后续覆盖率与质检全部引用这份账本。

产出：corpus/en/*.md ｜ corpus/index.json
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402
from htmlmd import html_to_blocks, blocks_to_markdown, page_text  # noqa: E402
from pdftext import pdf_stats  # noqa: E402

CORPUS_EN = os.path.join(C.ROOT, "corpus", "en")


# ---------------------------------------------------------------- PDF → Markdown
BULLET_RE = re.compile(r"^\s*[●○•·▪◦*]\s*")
SENT_END = tuple(".!?:;\"')]”’")


def pdf_text_to_markdown(text: str, *, label: str, slide_like: bool) -> str:
    """把 PDF 文本层还原成 Markdown。

    讲义导出的文本通常是"一行一个文本块"，需要两步整理：
    1. 归一化项目符号（● / ○ / • → `- `）；
    2. 把被硬换行拆断的句子接回去（上一行没有句末标点、下一行以小写字母开头）。
    """
    pages = text.split("\f")
    out: list[str] = []
    for idx, page in enumerate(pages, 1):
        raw_lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in page.split("\n")]
        lines = [ln for ln in raw_lines if ln]
        if not lines:
            continue
        out.append(f"## {'Slide' if slide_like else 'Page'} {idx}")
        out.append("")
        merged: list[str] = []
        for ln in lines:
            is_bullet = bool(BULLET_RE.match(ln))
            ln = BULLET_RE.sub("- ", ln)
            if merged and not is_bullet and not ln.startswith(("-", "#", "|")):
                prev = merged[-1]
                if prev and not prev.endswith(SENT_END) and prev.startswith("- ") is False \
                        and ln[:1].islower():
                    merged[-1] = prev + " " + ln
                    continue
            merged.append(ln)
        out.extend(merged)
        out.append("")
    body = "\n".join(out)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return f"# {label}\n\n{body.strip()}\n"


# ---------------------------------------------------------------- 语料构造
def site_items(course: dict) -> list[dict]:
    items = []
    for term, t in course["terms"].items():
        base = {"kind": "site", "term": term, "source_url": t["url"],
                "license": "Stanford CS146S 课程组"}
        # Overview：服务端渲染出来的官网正文
        items.append(dict(base, slug=f"site-{term}-overview",
                          title=f"CS146S 官网 · 总览（{term}）",
                          md=t["overview_markdown"]))
        # Syllabus
        lines = [f"# CS146S 课程大纲 · {term}", ""]
        for w in t["weeks"]:
            lines.append(f"## {w['title']}")
            lines.append("")
            if w["topics"]:
                lines.append("### Topics")
                lines.extend(f"- {x}" for x in w["topics"])
                lines.append("")
            if w["readings"]:
                lines.append("### Readings")
                lines.extend(f"- [{r['label']}]({r['href']})" for r in w["readings"])
                lines.append("")
            if w["assignments"]:
                lines.append("### Assignments")
                lines.extend(f"- [{a['label']}]({a['href']})" for a in w["assignments"])
                lines.append("")
            if w["sessions"]:
                lines.append("### Sessions")
                for s in w["sessions"]:
                    head = f"- {s['date']} {s['lead']}".rstrip()
                    if s["profile"]:
                        head += f" ([profile]({s['profile']}))"
                    lines.append(head)
                    for lk in s["links"]:
                        lines.append(f"  - [{lk['label']}]({lk['href']})")
                lines.append("")
        items.append(dict(base, slug=f"site-{term}-syllabus",
                          title=f"CS146S 课程大纲（{term}）",
                          md="\n".join(lines).strip() + "\n"))
        # FAQ
        lines = [f"# CS146S 常见问题（{term}）", ""]
        for f in t["faq"]:
            lines.append(f"## {f['q']}")
            lines.append("")
            lines.append(f["a"])
            lines.append("")
        items.append(dict(base, slug=f"site-{term}-faq",
                          title=f"CS146S 常见问题（{term}）",
                          md="\n".join(lines).strip() + "\n"))
        # Grading
        lines = [f"# CS146S 评分构成（{term}）", "", "| 项目 | 占比 |", "| --- | --- |"]
        lines += [f"| {g['label']} | {g['value']} |" for g in t["grading"]]
        items.append(dict(base, slug=f"site-{term}-grading",
                          title=f"CS146S 评分构成（{term}）",
                          md="\n".join(lines).strip() + "\n"))
    return items


def repo_items() -> list[dict]:
    items = []
    for branch_dir in sorted(glob.glob(os.path.join(C.REPO, "*"))):
        if not os.path.isdir(branch_dir):
            continue
        branch = os.path.basename(branch_dir)
        meta = C.read_json(os.path.join(C.REPO, f"{branch}_files.json"), {}) or {}
        sha = meta.get("sha", "")
        for path in sorted(glob.glob(os.path.join(branch_dir, "**", "*"), recursive=True)):
            if not os.path.isfile(path):
                continue
            if not path.lower().endswith((".md", ".txt", ".rst")):
                continue
            rel = os.path.relpath(path, branch_dir)
            # 去掉 tarball 顶层目录前缀
            parts = rel.split(os.sep)
            if len(parts) > 1 and parts[0].startswith("modern-software-dev"):
                rel = "/".join(parts[1:])
            body = C.read_text(path, "")
            if not body.strip():
                continue
            slug = C.slugify(f"repo-{branch}-{rel.replace('/', '-')}")
            title = f"CS146S 作业仓库 · {rel}（{branch}）"
            md = body if body.lstrip().startswith("#") else f"# {title}\n\n{body}"
            items.append({
                "slug": slug, "title": title, "md": md, "kind": "repo",
                "term": branch,
                "source_url": (f"https://github.com/{ 'mihail911' }/"
                               f"modern-software-dev-assignments/blob/{branch}/{rel}"),
                "source_path": rel, "commit": sha,
                "license": "仓库代码与文档版权归 Mihail Eric / Stanford CS146S",
            })
    return items


def reading_items() -> list[dict]:
    idx = C.read_json(os.path.join(C.READINGS, "index.json"), {}) or {}
    raw = os.path.join(C.READINGS, "raw")
    items = []
    for it in idx.get("items", []):
        # SHELL：所有取法都只拿回很短的正文（例如 OWASP 首页本身就是短目录页）。
        # 这类内容仍是有价值的原文，收进语料但在清单里如实标注，绝不冒充"完整抓取"。
        if it["status"] not in ("OK", "SHELL"):
            continue
        slug = it["slug"]
        src = None
        # 站点若声明了 Markdown 原文（<link rel="alternate" type="text/markdown">），
        # 它是比 HTML 更干净的一手来源，优先使用。
        for ext in (".md", ".html", ".pdf", ".txt"):
            p = os.path.join(raw, slug + ext)
            if os.path.exists(p) and os.path.getsize(p) > 0:
                src = p
                break
        if not src:
            continue
        title = it.get("label") or slug
        block_count = 0
        try:
            if src.endswith(".md") and it["kind"] == "html":
                body = C.read_any_text(src)
                md = body if body.lstrip().startswith("#") else f"# {title}\n\n{body}\n"
                block_count = md.count("\n## ")
            elif src.endswith(".html"):
                blocks = html_to_blocks(C.read_any_text(src))
                block_count = len(blocks)
                body_len = sum(
                    len(b.get("text", "") or "") + sum(len(x) for x in b.get("items", []))
                    for b in blocks
                )
                if body_len < 400:
                    # 正文抽取失败（JS 渲染空壳 / 结构太怪）：换整页兜底，
                    # 但兜底也必须先剥掉 script/style，否则会产出 CSS/JS 汤。
                    text = page_text(C.read_any_text(src))
                    md = f"# {title}\n\n{text}\n" if text else \
                         f"# {title}\n\n> [抽取失败] 页面无可提取正文\n"
                else:
                    md = blocks_to_markdown(blocks, title=title)
            elif src.endswith(".pdf"):
                st = pdf_stats(src)
                slide_like = st["pages"] > 0 and st["chars"] / max(st["pages"], 1) < 900
                md = pdf_text_to_markdown(st["text"], label=title, slide_like=slide_like)
                block_count = st["pages"]
            else:
                body = C.read_any_text(src)
                md = f"# {title}\n\n{body}\n"
                block_count = 1
        except Exception as exc:  # noqa: BLE001
            md = f"# {title}\n\n> [抽取失败] {type(exc).__name__}: {exc}\n"
        items.append({
            "slug": slug, "title": title, "md": md,
            "kind": "reading_" + it["kind"], "term": ",".join(it["years"]),
            "source_url": it["url"], "strategy": it["strategy"],
            "weeks": it["weeks"],
            "license": "第三方文章，版权归原作者；本包仅提供学习用途中文译本",
        })
    return items


def media_items() -> list[dict]:
    idx = C.read_json(os.path.join(C.DOCS_SRC, "index.json"), {}) or {}
    items = []
    for it in idx.get("items", []):
        if it["status"] != "OK":
            continue
        cache = os.path.join(C.ROOT, it.get("cache", ""))
        if not os.path.exists(cache):
            continue
        slug, title = it["slug"], it.get("lead") or it.get("label") or it["slug"]
        label = f"{title}（{it['term']} W{it['week']}）"
        try:
            if cache.lower().endswith(".pdf"):
                st = pdf_stats(cache)
                md = pdf_text_to_markdown(st["text"], label=label, slide_like=True)
            elif cache.lower().endswith(".md"):
                md = f"# {label}\n\n{C.read_any_text(cache)}\n"
            else:
                md = f"# {label}\n\n{C.read_any_text(cache)}\n"
        except Exception as exc:  # noqa: BLE001
            md = f"# {label}\n\n> [抽取失败] {type(exc).__name__}: {exc}\n"
        items.append({
            "slug": slug, "title": label, "md": md, "kind": "media_" + it["kind"],
            "term": it["term"], "source_url": it["url"],
            "license": "课程讲义，版权归 Stanford CS146S 课程组及各位嘉宾公司",
        })
    return items


# ---------------------------------------------------------------- 主流程
def main() -> int:
    C.ensure_dirs(CORPUS_EN, C.WORK, C.REPORTS)
    ledger = C.Ledger("s05_extract_corpus")

    course = C.read_json(os.path.join(C.SITE, "course.json"))
    if not course:
        raise SystemExit("缺少 sources/site/course.json，请先跑 s01_fetch_site.py")

    groups = {
        "site": site_items(course),
        "repo": repo_items(),
        "reading": reading_items(),
        "media": media_items(),
    }

    index = []
    # ---------- slug 唯一性兜底 ----------
    # 真实踩到的坑：同一节课的 Google Slides 讲义与 Drive 上的「设计文档模板」
    # 由 slide_slug() 生成了**完全相同的文件名**，后写的把先写的覆盖了 ——
    # 索引里两条都在，磁盘上却只有一个文件，**一份讲义就这么静默消失了**。
    # 这里做一次全局查重：撞名的一律追加内容特征后缀，并打日志（不静默处理）。
    seen_slugs: dict[str, int] = {}
    for group, items in groups.items():
        for it in items:
            slug = it["slug"]
            if slug in seen_slugs:
                tag = C.slugify(str(it.get("label") or it.get("source_path")
                                    or it.get("kind") or "dup"), 36)
                cand = f"{slug}-{tag}"
                n = 2
                while cand in seen_slugs:
                    cand = f"{slug}-{tag}-{n}"
                    n += 1
                C.log(f"  ⚠️ slug 冲突：{slug} → {cand}"
                      f"（{it['title'][:44]} · {it.get('kind','')}）")
                it["slug"] = cand
                slug = cand
            seen_slugs[slug] = 1

    for group, items in groups.items():
        C.log(f"[{group}] {len(items)} 份")
        for it in items:
            md = it["md"]
            path = os.path.join(CORPUS_EN, it["slug"] + ".md")
            C.write_text(path, md)
            chars = len(re.sub(r"\s+", "", md))
            index.append({
                "slug": it["slug"], "title": it["title"], "kind": it["kind"],
                "group": group, "term": it.get("term", ""),
                "source_url": it.get("source_url", ""),
                "source_path": it.get("source_path", ""),
                "commit": it.get("commit", ""),
                "strategy": it.get("strategy", ""),
                "license": it.get("license", ""),
                "chars": chars, "lines": md.count("\n") + 1,
                "path": os.path.relpath(path, C.ROOT).replace("\\", "/"),
            })
            ledger.add(slug=it["slug"], group=group, chars=chars)

    title_map = {i["slug"]: i["title"] for i in index}
    total_chars = sum(i["chars"] for i in index)
    C.write_json(os.path.join(C.ROOT, "corpus", "index.json"), {
        "generated_at": C.now_iso(),
        "count": len(index),
        "total_chars": total_chars,
        "groups": {g: sum(1 for i in index if i["group"] == g) for g in groups},
        "items": index,
    })
    C.write_json(os.path.join(C.WORK, "titles.json"), title_map)

    C.log(f"\n[语料] {len(index)} 份 · 合计 {total_chars:,} 字符")
    for g, items in groups.items():
        sub = [i for i in index if i["group"] == g]
        C.log(f"   {g:<8} {len(sub):>3} 份  {sum(i['chars'] for i in sub):>9,} 字符")

    C.append_ledger(ledger.finish({"count": len(index), "total_chars": total_chars}))
    C.log("完成 · 输出 corpus/en/ 与 corpus/index.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
