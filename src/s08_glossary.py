#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S08 · 术语表：校验、生成人读版、并从语料里找漏掉的术语。

术语表是本项目**唯一的译名事实来源**。这一步做三件事：

1. **自检**：词条不重复、定译之间不打架、禁用写法不与别人的定译冲突；
2. **生成** `glossary/术语表.md`，给人读、给评审查；
3. **反向找漏**：统计语料里高频出现的英文技术词，标出"出现很多但术语表里没有"的，
   提示需要补进表里 —— 术语表不是一次写死的，是随着语料扫出来的。
"""

from __future__ import annotations

import glob
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402

GLOSSARY_JSON = os.path.join(C.GLOSSARY_DIR, "glossary.json")
OUT_MD = os.path.join(C.GLOSSARY_DIR, "术语表.md")
CORPUS_EN = os.path.join(C.ROOT, "corpus", "en")

# 停用词：这些词高频但没有术语价值，不进候选
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "than", "that", "this",
    "these", "those", "is", "are", "was", "were", "be", "been", "being", "to",
    "of", "in", "on", "at", "by", "for", "with", "from", "as", "it", "its",
    "you", "your", "we", "our", "they", "their", "he", "she", "his", "her",
    "can", "will", "would", "should", "could", "may", "might", "must", "do",
    "does", "did", "not", "no", "so", "such", "when", "where", "which", "who",
    "how", "what", "why", "all", "any", "more", "most", "other", "some", "only",
    "also", "into", "out", "up", "down", "over", "about", "after", "before",
    "here", "there", "one", "two", "first", "last", "new", "use", "used",
    "using", "make", "makes", "made", "get", "gets", "got", "see", "sees",
    "like", "well", "just", "now", "then", "them", "us", "my", "me", "i",
    "have", "has", "had", "very", "much", "many", "each", "both", "same",
    "because", "while", "during", "through", "between", "without", "within",
    "code", "file", "files", "example", "examples", "run", "runs", "running",
    "need", "needs", "want", "wants", "work", "works", "working", "one",
    "let", "lets", "add", "adds", "added", "say", "says", "said", "go",
    "goes", "going", "take", "takes", "took", "give", "gives", "gave",
    "know", "knows", "knew", "think", "thinks", "thought", "come", "comes",
    "keep", "keeps", "kept", "put", "puts", "set", "sets", "show", "shows",
    "call", "calls", "called", "build", "builds", "built", "write", "writes",
    "written", "read", "reads", "start", "starts", "started", "end", "ends",
    "ended", "way", "ways", "thing", "things", "time", "times", "part", "parts",
}


def main() -> int:
    C.ensure_dirs(C.GLOSSARY_DIR, C.REPORTS)
    ledger = C.Ledger("s08_glossary")

    data = C.read_json(GLOSSARY_JSON)
    if not data:
        raise SystemExit("缺少 glossary/glossary.json")
    terms = data["terms"]

    # ---------- 1. 自检 ----------
    problems: list[str] = []
    seen_en: dict[str, str] = {}
    zh_owner: dict[str, str] = {}
    for t in terms:
        en = t["en"]
        if en in seen_en:
            problems.append(f"词条重复：{en}")
        seen_en[en] = t["zh"]
        zh = t.get("zh", "")
        # alias_of 显式声明「这条是同义词/缩写」，共用定译不算冲突。
        # 与其把冲突检查放宽松（那样真冲突也漏了），不如要求显式声明。
        if zh and not t.get("keep") and not t.get("alias_of"):
            base = re.sub(r"（.*?）", "", zh).strip()
            if base in zh_owner and zh_owner[base] != en:
                problems.append(f"定译冲突：「{base}」同时属于 {zh_owner[base]} 与 {en}")
            zh_owner.setdefault(base, en)

    # 禁用写法与别人的定译是否打架（打架会造成"照规范译也违规"的死结）
    for t in terms:
        for bad in t.get("forbid", []):
            if bad in zh_owner and zh_owner[bad] != t["en"]:
                problems.append(
                    f"禁用写法冲突：「{bad}」是 {zh_owner[bad]} 的定译，却被 {t['en']} 列为禁用")
            if bad == t.get("zh"):
                problems.append(f"自相矛盾：{t['en']} 的定译与禁用写法相同")

    # ---------- 2. 生成人读版 ----------
    lines = ["# CS146S 中文译本术语表", ""]
    lines.append(f"> 共 **{len(terms)}** 条 ｜ 其中保留英文 **{sum(1 for t in terms if t.get('keep'))}** 条"
                 f" ｜ 声明禁用写法 **{sum(len(t.get('forbid', [])) for t in terms)}** 条")
    lines.append(">")
    lines.append("> 本表是全项目译名的唯一事实来源，由 `glossary/glossary.json` 生成（请勿手改本文件）。")
    lines.append("> 校验与生成：`python src/s08_glossary.py`")
    lines.append("")
    lines.append("## 术语对照")
    lines.append("")
    lines.append("| 英文 | 中文定译 | 禁用写法 | 说明 |")
    lines.append("|---|---|---|---|")
    for t in sorted(terms, key=lambda x: x["en"].lower()):
        forbid = "、".join(t.get("forbid", [])) or "—"
        note = (t.get("note") or "").replace("|", "\\|")
        zh = t["zh"] + ("（保留英文）" if t.get("keep") and t["zh"] != t["en"] else "")
        lines.append(f"| `{t['en']}` | {zh} | {forbid} | {note} |")
    lines.append("")
    lines.append("## 自检结果")
    lines.append("")
    if problems:
        lines.append("发现问题：")
        lines.append("")
        for p in problems:
            lines.append(f"- ⚠️ {p}")
    else:
        lines.append("✅ 无重复词条、无定译冲突、无禁用写法与定译打架。")
    lines.append("")
    C.write_text(OUT_MD, "\n".join(lines))

    # ---------- 3. 从语料里找漏掉的术语 ----------
    freq: Counter = Counter()
    files = sorted(glob.glob(os.path.join(CORPUS_EN, "*.md")))
    for p in files:
        text = C.read_any_text(p)
        text = re.sub(r"```.*?```", " ", text, flags=re.S)          # 去掉代码块
        text = re.sub(r"`[^`]*`", " ", text)
        for m in re.finditer(r"\b([A-Za-z][A-Za-z-]{2,})\b", text):
            w = m.group(1)
            if w.lower() in STOPWORDS:
                continue
            freq[w.lower()] += 1

    known = {t["en"].lower() for t in terms}
    for t in terms:
        for part in re.split(r"[\s/]+", t["en"].lower()):
            known.add(part)

    candidates = [(w, c) for w, c in freq.most_common(1200) if c >= 15 and w not in known]
    lines = ["# 术语候选（自动扫描，供补表用）", "",
             f"> 扫描 {len(files)} 份语料，列出**高频但术语表里没有**的英文技术词。",
             "> 不是所有候选都该进表（很多只是普通词汇），这一步是给人做判断用的。", "",
             "| 词 | 出现次数 |", "|---|---:|"]
    for w, c in candidates[:120]:
        lines.append(f"| `{w}` | {c} |")
    lines.append("")
    C.write_text(os.path.join(C.REPORTS, "_term_candidates.md"), "\n".join(lines))

    C.log(f"[术语] {len(terms)} 条 ｜ 保留英文 {sum(1 for t in terms if t.get('keep'))} 条"
          f" ｜ 禁用写法 {sum(len(t.get('forbid', [])) for t in terms)} 条")
    if problems:
        C.log("[自检] 发现问题：")
        for p in problems:
            C.log(f"   ⚠️ {p}")
    else:
        C.log("[自检] ✅ 无冲突")
    C.log(f"[候选] 高频未收录词 {len(candidates)} 个 → reports/_term_candidates.md")
    C.write_json(os.path.join(C.REPORTS, "_glossary_check.json"),
                 {"terms": len(terms), "problems": problems,
                  "candidates": candidates[:120]})
    C.append_ledger(ledger.finish({"terms": len(terms), "problems": len(problems),
                                   "candidates": len(candidates)}))
    C.log("完成 · 输出 glossary/术语表.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
