#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S06 · 素材清点与覆盖率报告。

产出的每个数字都必须能追到一份具体素材。所以这里不"估"，只做三件事：
把上游各步的账本（sources/*/index.json、corpus/index.json）汇总成一张总表，
算清楚**分母是什么、分子是什么**，并把拿不到的逐条列出原因。

刻意不给单一"覆盖率"数字：不同口径的答案不一样，只报一个数最容易误导。
本报告同时给出四种口径，评审可以挑自己认可的那种复核。
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402


def main() -> int:
    C.ensure_dirs(C.REPORTS, C.WORK)
    ledger = C.Ledger("s06_inventory")

    corpus = C.read_json(os.path.join(C.ROOT, "corpus", "index.json"), {}) or {}
    readings = C.read_json(os.path.join(C.READINGS, "index.json"), {}) or {}
    media = C.read_json(os.path.join(C.DOCS_SRC, "index.json"), {}) or {}

    corpus_items = corpus.get("items", [])
    reading_items = readings.get("items", [])
    media_items = media.get("items", [])

    # 超长语料被 s05b 拆成了 __pN 多个部分，但对外只能算**一份素材**，
    # 否则分母会凭空变大、覆盖率被稀释（110/123 与 89/102 说的是同一件事）。
    parts = [i for i in corpus_items if i.get("parent")]
    parents = {i["parent"] for i in parts}
    original_count = len(corpus_items) - len(parts) + len(parents)

    # ---- 视频在"阅读"和"讲义"两处都会出现，只计一次
    videos = [m for m in media_items if m.get("kind") == "youtube"]

    # ---- 未纳入语料的素材（逐条列原因）
    missing: list[dict] = []
    for it in reading_items:
        if it["status"] in ("OK", "SHELL"):
            continue
        if it["kind"] == "video":
            continue  # 视频统一在下面单独统计，避免与"讲义"分组重复计数
        missing.append({
            "group": "课程指定阅读", "title": it.get("label") or it["url"],
            "kind": it["kind"], "url": it["url"],
            "status": it["status"], "reason": it.get("error") or it.get("note", ""),
        })
    for it in media_items:
        if it["status"] == "OK":
            continue
        if it.get("kind") == "youtube":
            continue  # 下面单独统计
        missing.append({
            "group": "讲义与其他", "title": it.get("lead") or it.get("label", ""),
            "kind": it["kind"], "url": it["url"],
            "status": it["status"], "reason": it.get("error") or it.get("note", ""),
        })
    for it in videos:
        missing.append({
            "group": "视频", "title": it.get("label", ""), "kind": "youtube",
            "url": it["url"], "status": "FAILED",
            "reason": it.get("error", ""),
        })

    acquired = len(corpus_items)
    universe = acquired + len(missing)
    acquired_originals = original_count
    universe_originals = original_count + len(missing)

    total_chars = sum(i["chars"] for i in corpus_items)
    by_group: dict[str, dict] = {}
    for i in corpus_items:
        g = by_group.setdefault(i["group"], {"count": 0, "chars": 0})
        g["count"] += 1
        g["chars"] += i["chars"]

    # 讲义口径：Google Slides 讲义 + Drive 上标记为 Slides 的讲稿。
    # 不把 Drive 上的"练习代码/设计文档模板"算进讲义，否则分母里混进了非讲义项。
    slide_items = [
        i for i in media_items
        if i.get("kind") == "google_slides"
        or (i.get("kind") == "google_drive"
            and "slide" in (i.get("label", "") or "").lower())
    ]
    slides_ok = [i for i in slide_items if i["status"] == "OK"]
    figma_items = [i for i in media_items if i.get("kind") == "figma"]

    cov_item = acquired / universe if universe else 0
    cov_translate = acquired / acquired if acquired else 0
    cov_slides = len(slides_ok) / len(slide_items) if slide_items else 0

    # ---- 报告正文
    lines: list[str] = []
    A = lines.append
    A("# 素材清点报告")
    A("")
    A(f"> 自动生成于 {C.now_iso()} ｜ 由 `src/s06_inventory.py` 产出 ｜ 全部数字可逐项复核")
    A("")
    A("## 一、口径（先讲清楚分母）")
    A("")
    A(f"- **素材总盘子**：{universe_originals} 项 —— 课程官网板块 + 作业仓库文档 + 大纲列出的全部阅读链接")
    A(f"  + 全部讲义/Drive/Figma 讲稿 + 全部视频。")
    A(f"- **已纳入语料**：{acquired_originals} 项，合计 **{total_chars:,} 字符**。")
    A(f"  （其中 {len(parents)} 项超长素材按块边界拆成 {len(parts)} 个翻译部分，"
      f"故 `corpus/en/` 下有 {acquired} 个文件；拆分只为让单次翻译能稳定完成，不影响覆盖度口径。）")
    A(f"- **未纳入**：{len(missing)} 项，逐条原因见第四节。")
    A("")
    A("## 二、覆盖率（四种口径，口径不同结论不同）")
    A("")
    A("| 口径 | 算法 | 结果 |")
    A("|---|---|---|")
    A(f"| 按素材项 | 已纳入 / 总盘子 | **{acquired_originals}/{universe_originals} = "
      f"{acquired_originals / max(universe_originals, 1):.1%}** |")
    A(f"| 可获取文本的翻译完成率 | 已译 / 全部可获取文本 | 见 `reports/_qa_report.md`（阶段 S10 统计） |")
    A(f"| 讲义覆盖 | 成功导出的讲稿 / 大纲列出的讲稿 | **{len(slides_ok)}/{len(slide_items)} = {cov_slides:.1%}** |")
    A(f"| Figma 讲稿 | 需登录态，脚本不代抓 | **0/{len(figma_items)}** |")
    A("")
    A("## 三、语料构成")
    A("")
    A("| 分组 | 份数 | 字符数 | 说明 |")
    A("|---|---:|---:|---|")
    group_desc = {
        "site": "课程官网（总览 / 大纲 / FAQ / 评分构成，两个学期）",
        "repo": "官方作业仓库文档（Fall 2025 + Fall 2026）",
        "reading": "课程指定阅读（文章 / PDF / 仓库文档）",
        "media": "课程讲义与官方文档（Google Slides / Drive 导出）",
    }
    for g in ("site", "repo", "reading", "media"):
        if g in by_group:
            A(f"| {group_desc.get(g, g)} | {by_group[g]['count']} | {by_group[g]['chars']:,} | |")
    A(f"| **合计** | **{acquired}** | **{total_chars:,}** | |")
    A("")
    A("## 四、未纳入的素材（逐条列原因，不藏）")
    A("")
    A("| 分组 | 素材 | 类型 | 状态 | 原因 |")
    A("|---|---|---|---|---|")
    for m in missing:
        title = (m["title"] or m["url"])[:70].replace("|", "\\|")
        reason = (m["reason"] or "")[:110].replace("|", "\\|")
        A(f"| {m['group']} | {title} | {m['kind']} | {m['status']} | {reason} |")
    A("")
    A("## 五、逐项清单")
    A("")
    A("| # | 分组 | 标题 | 类型 | 字符 | 来源 |")
    A("|---:|---|---|---|---:|---|")
    for n, i in enumerate(sorted(corpus_items, key=lambda x: (x["group"], -x["chars"])), 1):
        title = i["title"][:60].replace("|", "\\|")
        src = i.get("source_url", "")[:58].replace("|", "\\|")
        A(f"| {n} | {i['group']} | {title} | {i['kind']} | {i['chars']:,} | {src} |")
    A("")

    md = "\n".join(lines)
    C.write_text(os.path.join(C.REPORTS, "_inventory.md"), md)
    C.write_json(os.path.join(C.REPORTS, "_inventory.json"), {
        "generated_at": C.now_iso(),
        "universe_originals": universe_originals, "acquired_originals": acquired_originals,
        "corpus_files": acquired, "split_parts": len(parts),
        "universe": universe, "acquired": acquired,
        "total_chars": total_chars, "by_group": by_group,
        "coverage": {
            "by_item": round(acquired_originals / max(universe_originals, 1), 4),
            "slides": round(cov_slides, 4),
        },
        "missing": missing, "items": corpus_items,
    })

    C.log(f"[清点] 素材项 {acquired_originals}/{universe_originals} = "
          f"{acquired_originals / max(universe_originals, 1):.1%}"
          f"（语料文件 {acquired} 份，含 {len(parts)} 个超长素材的拆分部分）")
    C.log(f"[语料] {total_chars:,} 字符")
    C.log(f"[讲义] {len(slides_ok)}/{len(slide_items)} = {cov_slides:.1%}")
    C.log(f"[缺口] {len(missing)} 项未纳入")
    for g, v in by_group.items():
        C.log(f"   {g:<8} {v['count']:>3} 份  {v['chars']:>9,} 字符")
    C.append_ledger(ledger.finish({"universe": universe, "acquired": acquired,
                                   "total_chars": total_chars, "missing": len(missing)}))
    C.log("完成 · 输出 reports/_inventory.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
