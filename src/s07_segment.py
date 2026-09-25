#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S07 · 切段：把语料切成稳定的"最小翻译单元"，产出 segments.jsonl。

这一步的意义是把"翻译"从一件含糊的事变成一件**可计量、可抽检、可续跑**的事：

- 每个片段有稳定 ID（`<slug>#b0012`），中英因此能逐段对齐；
- 每段记录类型、字符数、SHA-256，翻译进度可以按段统计；
- 代码块不进入翻译队列（明确标记 `translate: false`），避免"把代码也翻了"；
- 中文译文到位后，同一套 ID 用于逐段比对（见 s10_qa.py）。

产出：work/segments/<slug>.jsonl ｜ work/segments_index.json
"""

from __future__ import annotations

import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402
from mdblocks import iter_segments, parse_markdown  # noqa: E402

CORPUS_EN = os.path.join(C.ROOT, "corpus", "en")
SEG_DIR = os.path.join(C.WORK, "segments")


def main() -> int:
    C.ensure_dirs(SEG_DIR, C.WORK)
    ledger = C.Ledger("s07_segment")

    files = sorted(glob.glob(os.path.join(CORPUS_EN, "*.md")))
    index = []
    total_seg = 0
    total_translatable = 0
    total_chars = 0

    for path in files:
        slug = os.path.splitext(os.path.basename(path))[0]
        md = C.read_any_text(path)
        blocks = parse_markdown(md)
        segs = []
        for s in iter_segments(blocks):
            translatable = s["kind"] != "code"
            seg = {
                "slug": slug,
                "id": f"{slug}#{s['id']}",
                "block": s["block"],
                "kind": s["kind"],
                "translate": translatable,
                "chars": len(s["text"]),
                "sha256": C.sha256_text(s["text"])[:16],
                "text": s["text"],
            }
            segs.append(seg)

        out = os.path.join(SEG_DIR, slug + ".jsonl")
        with open(out, "w", encoding="utf-8", newline="\n") as fh:
            for seg in segs:
                fh.write(json.dumps(seg, ensure_ascii=False) + "\n")

        tr = [s for s in segs if s["translate"]]
        chars = sum(s["chars"] for s in tr)
        index.append({"slug": slug, "blocks": len(blocks), "segments": len(segs),
                      "translatable": len(tr), "translatable_chars": chars})
        total_seg += len(segs)
        total_translatable += len(tr)
        total_chars += chars

    C.write_json(os.path.join(C.WORK, "segments_index.json"), {
        "generated_at": C.now_iso(), "files": len(files), "segments": total_seg,
        "translatable_segments": total_translatable, "translatable_chars": total_chars,
        "items": index,
    })
    C.log(f"[切段] {len(files)} 份语料 → {total_seg} 段"
          f"（其中待译 {total_translatable} 段 / {total_chars:,} 字符）")
    C.append_ledger(ledger.finish({"files": len(files), "segments": total_seg,
                                   "translatable": total_translatable,
                                   "translatable_chars": total_chars}))
    C.log("完成 · 输出 work/segments/ 与 work/segments_index.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
