#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S05b · 大文件切分：把超长语料按块边界拆成若干部分。

为什么需要
----------
一次翻译能稳定产出的译文长度是有限的。9.6 万字符的英文（约合 6 万中文字）不可能
在一轮里译完又不掉质量。与其指望"一口气译完"，不如**在翻译之前就把输入切成能译完的大小**。

切分点只在**块边界**（标题之间 / 空行之间），绝不在段落中间切 —— 否则译文会从半句话开始，
中英对照也就对不齐了。切分后每部分都是独立的一等语料项，清点、切段、质检、装配全流程照常工作；
装配阶段再按 `__pN` 后缀合并回完整文档。

产出：corpus/en/<slug>__pN.md ｜ corpus/_full/<slug>.md ｜ 更新 corpus/index.json
"""

from __future__ import annotations

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402

CORPUS_EN = os.path.join(C.ROOT, "corpus", "en")
CORPUS_FULL = os.path.join(C.ROOT, "corpus", "_full")
SPLIT_THRESHOLD = 28000   # 超过这个字符数就切
PART_TARGET = 20000       # 每部分的目标大小


def split_markdown(md: str, target: int) -> list[str]:
    """把长文档切成若干部分，每部分尽量不超过 target 字符。

    切分单元是**标题行或空行分隔的段落**，绝不从段落中间切。
    第一版只在 `## ` 标题处切，结果遇到"某个二级标题下有 5 万字"的文档时，
    仍然产出了一个 5.6 万字的部分 —— 等于没切。所以这里改成累积"最小可切单元"，
    只要超预算就断开，无论当前处在几级标题下。
    """
    lines = md.split("\n")
    head: list[str] = []
    i = 0
    while i < len(lines) and not lines[i].startswith("#"):
        head.append(lines[i])
        i += 1
    head_text = "\n".join(head).strip()

    # 累积最小单元：标题行自成单元；空行结束当前段落
    units: list[str] = []
    cur: list[str] = []
    for line in lines[i:]:
        if line.startswith("#"):
            if cur:
                units.append("\n".join(cur))
                cur = []
            units.append(line)
        elif not line.strip():
            if cur:
                units.append("\n".join(cur))
                cur = []
        else:
            cur.append(line)
    if cur:
        units.append("\n".join(cur))

    parts: list[str] = []
    buf: list[str] = []
    size = len(head_text)
    for u in units:
        if buf and size + len(u) > target:
            parts.append((head_text + "\n\n" + "\n\n".join(buf)).strip())
            buf, size = [], len(head_text)
        buf.append(u)
        size += len(u) + 2
    if buf:
        parts.append((head_text + "\n\n" + "\n\n".join(buf)).strip())
    return [p + "\n" for p in parts if p.strip()]


def main() -> int:
    index = C.read_json(os.path.join(C.ROOT, "corpus", "index.json"), {}) or {}
    items = index.get("items", [])
    if not items:
        raise SystemExit("缺少 corpus/index.json，请先跑 s05_extract_corpus.py")

    C.ensure_dirs(CORPUS_FULL)
    new_items: list[dict] = []
    split_count = 0
    part_count = 0

    for it in items:
        path = os.path.join(C.ROOT, it["path"])
        if it["chars"] <= SPLIT_THRESHOLD:
            new_items.append(it)
            continue
        md = C.read_any_text(path)
        parts = split_markdown(md, PART_TARGET)
        if len(parts) < 2:
            new_items.append(it)
            continue

        C.write_text(os.path.join(CORPUS_FULL, it["slug"] + ".md"), md)
        os.remove(path)
        for n, part in enumerate(parts, 1):
            slug = f"{it['slug']}__p{n}"
            p = os.path.join(CORPUS_EN, slug + ".md")
            C.write_text(p, part)
            entry = dict(it)
            entry.update({
                "slug": slug,
                "title": f"{it['title']}（第 {n}/{len(parts)} 部分）",
                "chars": len(re.sub(r"\s+", "", part)),
                "lines": part.count("\n") + 1,
                "path": os.path.relpath(p, C.ROOT).replace("\\", "/"),
                "parent": it["slug"], "part": n, "parts": len(parts),
            })
            new_items.append(entry)
            part_count += 1
        split_count += 1
        C.log(f"  切分 {it['slug'][:52]}  {it['chars']:,} → {len(parts)} 部分")

    new_items.sort(key=lambda x: (x["group"], x["slug"]))
    index["items"] = new_items
    index["count"] = len(new_items)
    index["total_chars"] = sum(i["chars"] for i in new_items)
    index["split"] = {"files_split": split_count, "parts": part_count,
                      "threshold": SPLIT_THRESHOLD, "target": PART_TARGET}
    index["generated_at"] = C.now_iso()
    C.write_json(os.path.join(C.ROOT, "corpus", "index.json"), index)

    C.log(f"[切分] {split_count} 份超长语料拆成 {part_count} 部分；"
          f"语料项 {len(new_items)} 份 / {index['total_chars']:,} 字符")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
