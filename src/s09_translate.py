#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S09 · 翻译装配：分批计划、进度、成品输出。

子命令
------
plan      把语料切成分批计划（work/translation_plan.json），供并行翻译使用
status    报告翻译完成度（按份、按段、按字符）
assemble  把 corpus/zh/*.md 装配成成品：纯中文版 + 中英对照版
api       可选后端：调用 OpenAI 兼容接口自动翻译（需要环境变量提供 key）

设计说明：翻译这一步是**可插拔**的。
无论译文是人写的、AI 逐段译的，还是调 API 跑出来的，只要落在 `corpus/zh/<slug>.md`
并且通过 `s10_qa.py` 的结构校验，下游装配与建站完全一视同仁。
换源（换一门课）时只需重跑 plan，其余环节不动。
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402
from mdblocks import parse_markdown  # noqa: E402

CORPUS_EN = os.path.join(C.ROOT, "corpus", "en")
CORPUS_ZH = os.path.join(C.ROOT, "corpus", "zh")
TRANSLATED = os.path.join(C.ROOT, "translated")
PLAN = os.path.join(C.WORK, "translation_plan.json")

# 优先级：课程自有材料先译，第三方阅读最后。这样即便中途停下，
# 交付出去的核心内容也是完整的。
PRIORITY = {"site": 0, "media": 1, "repo": 2, "reading": 3}
BATCH_BUDGET = 26000  # 每批的英文字符上限（约合 8–10k 中文输出，单次翻译能稳定完成）


def load_corpus_index() -> dict:
    idx = C.read_json(os.path.join(C.ROOT, "corpus", "index.json"), {}) or {}
    return {i["slug"]: i for i in idx.get("items", [])}


def cmd_plan(_args) -> int:
    index = load_corpus_index()
    entries = []
    for path in sorted(glob.glob(os.path.join(CORPUS_EN, "*.md"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        meta = index.get(slug, {})
        entries.append({
            "slug": slug,
            "group": meta.get("group", "reading"),
            "title": meta.get("title", slug),
            "chars": meta.get("chars", len(C.read_any_text(path))),
        })

    entries.sort(key=lambda e: (PRIORITY.get(e["group"], 9), e["chars"]))
    batches: list[dict] = []
    cur: list[dict] = []
    cur_chars = 0
    for e in entries:
        if cur and cur_chars + e["chars"] > BATCH_BUDGET:
            batches.append({"files": cur, "chars": cur_chars})
            cur, cur_chars = [], 0
        cur.append(e)
        cur_chars += e["chars"]
    if cur:
        batches.append({"files": cur, "chars": cur_chars})

    for n, b in enumerate(batches, 1):
        b["id"] = f"t{n:02d}"
        b["slugs"] = [f["slug"] for f in b["files"]]

    C.write_json(PLAN, {
        "generated_at": C.now_iso(),
        "batch_budget": BATCH_BUDGET,
        "files": len(entries), "batches": len(batches),
        "total_chars": sum(e["chars"] for e in entries),
        "plan": batches,
    })
    C.log(f"[计划] {len(entries)} 份 / {len(batches)} 批 / "
          f"{sum(e['chars'] for e in entries):,} 字符（预算 {BATCH_BUDGET}/批）")
    for b in batches:
        names = "、".join(f["slug"][:38] for f in b["files"][:3])
        more = f" 等 {len(b['files'])} 份" if len(b["files"]) > 3 else ""
        C.log(f"   {b['id']}  {b['chars']:>7,} 字符  {names}{more}")
    return 0


def cmd_status(_args) -> int:
    index = load_corpus_index()
    seg_index = C.read_json(os.path.join(C.WORK, "segments_index.json"), {}) or {}
    seg_by_slug = {i["slug"]: i for i in seg_index.get("items", [])}

    done, pending = [], []
    for slug in sorted(index):
        zh = os.path.join(CORPUS_ZH, slug + ".md")
        (done if os.path.exists(zh) and os.path.getsize(zh) > 0 else pending).append(slug)

    def chars(slugs):
        return sum(index[s]["chars"] for s in slugs)

    total = len(index)
    C.log(f"[进度] {len(done)}/{total} 份完成（{len(done)/max(total,1):.1%}）")
    C.log(f"        字符 {chars(done):,}/{chars(list(index)):,}"
          f"（{chars(done)/max(chars(list(index)),1):.1%}）")
    by_group: dict[str, list[int]] = {}
    for slug in index:
        g = index[slug].get("group", "?")
        st = by_group.setdefault(g, [0, 0])
        st[1] += 1
        if slug in done:
            st[0] += 1
    for g, (d, t) in sorted(by_group.items(), key=lambda x: PRIORITY.get(x[0], 9)):
        seg = sum(seg_by_slug.get(s, {}).get("translatable", 0) for s in index
                  if index[s].get("group") == g)
        C.log(f"   {g:<8} {d:>3}/{t:<3}  待译段 {seg:,}")
    if pending:
        C.log("   未完成：" + "、".join(s[:44] for s in pending[:12])
              + (f" 等 {len(pending)} 份" if len(pending) > 12 else ""))
    return 0


def _bilingual(en_md: str, zh_md: str) -> str:
    """逐块交错的中英对照版。"""
    en_blocks = parse_markdown(en_md)
    zh_blocks = parse_markdown(zh_md)
    out: list[str] = []
    for i, eb in enumerate(en_blocks):
        zb = zh_blocks[i] if i < len(zh_blocks) else None
        if eb["type"] == "code":
            out.append("```" + eb.get("lang", ""))
            out.append(eb["text"])
            out.append("```")
            out.append("")
            continue
        if zb is not None and zb["type"] == eb["type"]:
            out.append(_render(eb))
            out.append("")
            out.append(_render(zb))
            out.append("")
        else:
            out.append(_render(eb))
            out.append("")
    text = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def _render(b: dict) -> str:
    t = b["type"]
    if t == "heading":
        return "#" * b["level"] + " " + b["text"]
    if t == "para":
        return b["text"]
    if t == "list":
        return "\n".join(("- " if not b.get("ordered") else "1. ") + i for i in b["items"])
    if t == "quote":
        return "\n".join("> " + ln for ln in b["text"].split("\n"))
    if t == "code":
        return "```" + b.get("lang", "") + "\n" + b["text"] + "\n```"
    if t == "table":
        rows = ["| " + " | ".join(b["header"]) + " |",
                "|" + "|".join([" --- "] * len(b["header"])) + "|"]
        rows += ["| " + " | ".join(r) + " |" for r in b["rows"]]
        return "\n".join(rows)
    if t == "rule":
        return "---"
    return ""


def cmd_assemble(args) -> int:
    C.ensure_dirs(TRANSLATED)
    index = load_corpus_index()
    made = 0

    # ① 先装配被切分的超长语料：把 __pN 各部分按序拼回完整文档
    groups: dict[str, list[str]] = {}
    for slug, meta in index.items():
        parent = meta.get("parent")
        if parent:
            groups.setdefault(parent, []).append(slug)
    for parent, parts in groups.items():
        parts.sort(key=lambda s: index[s].get("part", 0))
        zh_parts = [os.path.join(CORPUS_ZH, s + ".md") for s in parts]
        if not all(os.path.exists(p) and os.path.getsize(p) > 0 for p in zh_parts):
            continue
        en_full = os.path.join(C.ROOT, "corpus", "_full", parent + ".md")
        zh_md = "\n\n".join(C.read_any_text(p).strip() for p in zh_parts) + "\n"
        en_md = C.read_any_text(en_full)
        C.write_text(os.path.join(TRANSLATED, parent + ".zh.md"), zh_md)
        C.write_text(os.path.join(TRANSLATED, parent + ".bilingual.md"),
                     _bilingual(en_md, zh_md))
        made += 1
        C.log(f"  合并 {parent} ← {len(parts)} 部分")

    # ② 其余语料逐份装配
    for slug, meta in sorted(index.items()):
        if meta.get("parent"):
            continue
        en_path = os.path.join(CORPUS_EN, slug + ".md")
        zh_path = os.path.join(CORPUS_ZH, slug + ".md")
        if not os.path.exists(zh_path) or os.path.getsize(zh_path) == 0:
            continue
        en_md, zh_md = C.read_any_text(en_path), C.read_any_text(zh_path)
        C.write_text(os.path.join(TRANSLATED, slug + ".zh.md"), zh_md)
        C.write_text(os.path.join(TRANSLATED, slug + ".bilingual.md"),
                     _bilingual(en_md, zh_md))
        made += 1
    C.log(f"[装配] 输出 {made} 份纯中文版 + {made} 份中英对照版 → translated/")
    return 0


def cmd_api(args) -> int:
    """可选后端：OpenAI 兼容接口。

    本项目实际交付的译文由 AI 逐段产出并固化进 `corpus/zh/`，
    这个子命令是为了**换源复用**：下一门课只要提供 key 就能全自动跑完。
    需要环境变量 `CS146S_LLM_BASE`、`CS146S_LLM_KEY`、`CS146S_LLM_MODEL`。
    """
    import urllib.request

    base = os.environ.get("CS146S_LLM_BASE", "").rstrip("/")
    key = os.environ.get("CS146S_LLM_KEY", "")
    model = os.environ.get("CS146S_LLM_MODEL", "gpt-4o-mini")
    if not base or not key:
        C.log("未配置 CS146S_LLM_BASE / CS146S_LLM_KEY，api 后端不可用。")
        C.log("（本仓库交付的译文已固化在 corpus/zh/，无需重跑此步。详见 拿来说明.md）")
        return 2

    spec = C.read_any_text(os.path.join(C.ROOT, "TRANSLATION_SPEC.md"))
    plan = C.read_json(PLAN) or {"plan": [{"files": [{"slug": s} for s in load_corpus_index()]}]}
    todo = [f for b in plan["plan"] for f in b["files"]
            if not os.path.exists(os.path.join(CORPUS_ZH, f["slug"] + ".md"))]
    C.log(f"[api] 待译 {len(todo)} 份")

    for i, f in enumerate(todo, 1):
        slug = f["slug"]
        src = C.read_any_text(os.path.join(CORPUS_EN, slug + ".md"))
        prompt = (spec + "\n\n---\n\n以下是待翻译的 Markdown 原文，"
                  "请直接输出译文 Markdown，不要任何解释：\n\n" + src)
        payload = json.dumps({
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
        }).encode()
        req = urllib.request.Request(
            base + "/chat/completions", data=payload,
            headers={"Content-Type": "application/json",
                     "Authorization": "Bearer " + key})
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read().decode())
            out = data["choices"][0]["message"]["content"]
            C.write_text(os.path.join(CORPUS_ZH, slug + ".md"), out)
            C.log(f"  [{i}/{len(todo)}] {slug} ✓")
        except Exception as exc:  # noqa: BLE001
            C.log(f"  [{i}/{len(todo)}] {slug} ✗ {type(exc).__name__}: {exc}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="S09 翻译装配")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("plan").set_defaults(func=cmd_plan)
    sub.add_parser("status").set_defaults(func=cmd_status)
    sub.add_parser("assemble").set_defaults(func=cmd_assemble)
    sub.add_parser("api").set_defaults(func=cmd_api)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
