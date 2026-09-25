#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S10 · 质检：把"译得好不好"拆成一堆机器能回答的问题。

质检思路
--------
不指望机器判断"文笔好不好"，那是人的事。机器负责回答**这些一定有确定答案的问题**：

  结构类：段/标题/列表项/表格行列 是否与原文一一对应（漏译、截断、合并段落）
  代码类：代码块是否逐字节未改（代码被翻译是硬伤）
  链接类：URL 是否全部保留（译文里最常见的静默损坏）
  空译类：有没有空段落、只留标点的段落、原文照抄未译的段落
  残留类：中文段落里有没有成串未译的英文
  术语类：定译是否统一、有没有出现明令禁止的写法（一致率 = 命中 / (命中 + 违规)）
  排版类：中英文之间是否漏空格

产出 reports/_qa_report.md（总览）、_qa_scan.md（逐条问题）、_qa.json（机器可读）。

用法：
    python src/s10_qa.py              # 全量质检
    python src/s10_qa.py --slug XXX   # 只查一份
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
from mdblocks import block_plain, block_text, links, parse_markdown  # noqa: E402

CORPUS_EN = os.path.join(C.ROOT, "corpus", "en")
CORPUS_ZH = os.path.join(C.ROOT, "corpus", "zh")
GLOSSARY_JSON = os.path.join(C.GLOSSARY_DIR, "glossary.json")

EN_RUN_RE = re.compile(r"(?:\b[A-Za-z][A-Za-z'\-]*\b[ ,]+){7,}\b[A-Za-z][A-Za-z'\-]*\b")
# 只把**汉字**算作"中文"。第一版把全角标点区（\u3000-\u303f、\uff00-\uffef）
# 也算了进去，结果「（fall2025 W3）」里的「3）」被判成"中英文之间缺空格"，
# 30 条报警里大半是这种假阳性。判据放宽到全角标点上，真问题就被淹没了。
HAN = r"\u4e00-\u9fff\u3400-\u4dbf"
SPACING_BAD_RE = re.compile(rf"([{HAN}])([A-Za-z0-9])|([A-Za-z0-9])([{HAN}])")

# 允许出现的"看起来像漏译"的情况
ALLOW_KEEP = re.compile(r"^(?:[A-Za-z0-9 ._/+#\-:（）()\[\]]{0,80})$")

# 判断一块英文"像不像正文散文"。
# 为什么要这个判据：讲义 PDF 抽出来的文本里混着大量**本来就不该翻译**的东西 ——
# 命令行（npm install -g ...）、图表坐标轴（1950 1960 1970 ...）、编程语言名、
# 纯 URL 块。把它们报成"漏译"，会让真正需要看的漏译淹没在噪音里。
FUNC_WORD_RE = re.compile(
    r"\b(the|is|are|was|were|of|to|and|in|for|with|that|this|you|we|it|on|as|be|"
    r"can|will|from|your|our|not|but|or|if|when|how|what|which|there|their)\b", re.I)
CODE_LIKE_RE = re.compile(r"https?://|\s--?\w|\$\s|\|\s*\w+\(|^\s*[\w.@/-]+\s*=\s*[\w.]")


def looks_like_prose(text: str) -> bool:
    if len(text.split()) < 6:
        return False
    if len(FUNC_WORD_RE.findall(text)) < 3:
        return False
    if CODE_LIKE_RE.search(text):
        return False
    return True


def load_glossary() -> list[dict]:
    data = C.read_json(GLOSSARY_JSON, {}) or {}
    return data.get("terms", [])


def base_form(t: dict) -> str:
    return re.sub(r"（.*?）", "", t.get("zh", "")).strip()


def count_forbidden(text: str, bad: str, all_correct: list[str]) -> int:
    """统计禁用写法出现次数，且**不把正确写法的一部分算成违规**。

    踩过的坑：术语表里 `prompt → 提示词`，同时把「提示」列为禁用写法。
    而「提示」正是「提示词」的前两个字 —— 直接 `text.count("提示")` 会把所有
    正确的「提示词」也数成违规，术语一致率被凭空压低。
    做法：先把所有正确写法从文本里"抠掉"（替换成占位符），再统计禁止形式。
    """
    masked = text
    for cf in sorted(all_correct, key=len, reverse=True):
        if bad in cf and len(cf) > len(bad):
            masked = masked.replace(cf, "\u0000")
    return masked.count(bad)


def count_forbidden_re(text: str, pattern: str, all_correct: list[str]) -> list[str]:
    """正则级禁用规则，返回命中的片段。

    为什么需要正则：有些"禁用写法"要带上下文条件才成立。
    例如 `prompt` 的名词义必须译「提示词」，但动名词义（prompting → 提示）用「提示」是对的 ——
    光列一个裸词「提示」当禁用项，会把 26 处正当用法全报成违规。
    与其把规则放宽到查不出东西，不如把条件写清楚。
    """
    masked = text
    for cf in sorted(all_correct, key=len, reverse=True):
        masked = masked.replace(cf, "\u0000")
    try:
        return [m.group(0) for m in re.finditer(pattern, masked)]
    except re.error:
        return []


def is_reference_or_quote(text: str) -> bool:
    """判断一块是否属于"按规范就该保留原文"的类型。

    两类：
      · **参考文献条目**（`[5] Meta AI, (2025). The Llama 4 herd...`）——
        `TRANSLATION_SPEC.md` §4 明确要求保留作者名与标题；
      · **逐字引用**（`“Now critique your answer. Was it correct? …”`）——
        课程讲义里要求模型复述的原始提示词，保留英文才是忠实。

    这两类被"整块照抄 = 漏译"的判据命中，属于规则与规范打架。
    与其让译者把它们硬译成中文（那才是真的不忠实），不如在这里放行。
    """
    t = text.strip()
    if re.match(r"^\[\d+\]", t):
        return True
    if len(t) >= 2 and ((t[0] == "“" and t[-1] == "”") or (t[0] == '"' and t[-1] == '"')):
        return True
    return False


def check_pair(en_md: str, zh_md: str, terms: list[dict]) -> dict:
    en_blocks = parse_markdown(en_md)
    zh_blocks = parse_markdown(zh_md)
    issues: list[dict] = []
    stats = {
        "blocks_en": len(en_blocks), "blocks_zh": len(zh_blocks),
        "empty": 0, "untranslated": 0, "truncated": 0,
        "code_changed": 0, "link_lost": 0, "structure": 0, "spacing": 0,
        "term_hits": 0, "term_violations": 0, "term_missing": 0, "kept_english": 0,
    }
    term_violation_detail: list[str] = []

    def add(kind, where, detail):
        issues.append({"kind": kind, "where": where, "detail": detail})

    if len(en_blocks) != len(zh_blocks):
        stats["structure"] += 1
        add("structure", "文档", f"块数不一致：原文 {len(en_blocks)} / 译文 {len(zh_blocks)}")

    for i in range(max(len(en_blocks), len(zh_blocks))):
        eb = en_blocks[i] if i < len(en_blocks) else None
        zb = zh_blocks[i] if i < len(zh_blocks) else None
        where = f"块#{i + 1}"
        if eb is None:
            add("extra", where, "译文多出块")
            stats["structure"] += 1
            continue
        if zb is None:
            stats["truncated"] += 1
            add("truncated", where, f"译文缺块（原文 {eb['type']}：{block_plain(eb)[:40]}）")
            continue
        if eb["type"] != zb["type"]:
            stats["structure"] += 1
            add("structure", where, f"块类型不一致：原文 {eb['type']} / 译文 {zb['type']}")
            continue

        # --- 代码块必须逐字节相同
        if eb["type"] == "code":
            if eb["text"] != zb["text"]:
                stats["code_changed"] += 1
                add("code_changed", where, "代码块被改动（代码不应翻译）")
            continue

        if eb["type"] == "table":
            if len(eb["header"]) != len(zb["header"]) or len(eb["rows"]) != len(zb["rows"]):
                stats["structure"] += 1
                add("structure", where,
                    f"表格尺寸不一致：{len(eb['rows'])}×{len(eb['header'])} "
                    f"vs {len(zb['rows'])}×{len(zb['header'])}")

        if eb["type"] == "list" and len(eb["items"]) != len(zb["items"]):
            stats["structure"] += 1
            add("structure", where,
                f"列表项数不一致：{len(eb['items'])} vs {len(zb['items'])}")

        # --- 链接必须全部保留
        en_links, zh_links = set(links(block_text(eb))), set(links(block_text(zb)))
        lost = en_links - zh_links
        if lost:
            stats["link_lost"] += len(lost)
            add("link_lost", where, "链接丢失：" + "、".join(sorted(lost)[:3]))

        # --- 空译 / 截断
        en_plain, zh_plain = block_plain(eb), block_plain(zb)
        if len(en_plain) >= 20:
            if not zh_plain:
                stats["empty"] += 1
                add("empty", where, f"译文为空（原文 {len(en_plain)} 字符）")
            elif zh_plain == en_plain and looks_like_prose(en_plain):
                if is_reference_or_quote(en_plain):
                    stats["kept_english"] += 1
                else:
                    stats["untranslated"] += 1
                    add("untranslated", where, "整块照抄原文未译")
            elif len(zh_plain) < len(en_plain) * 0.20 and len(en_plain) >= 60 \
                    and eb["type"] in ("para", "heading"):
                # 只对**足够长的**块做"过短"判定。英文短句译成中文本来就会短一大截
                # （"Course logistics" → "课程安排"），拿短块比长度只会制造假警报。
                stats["truncated"] += 1
                add("truncated", where,
                    f"译文明显过短（原文 {len(en_plain)} → 译文 {len(zh_plain)} 字符）")

        # --- 未译英文残留
        if zh_plain and eb["type"] in ("para", "heading", "quote"):
            m = EN_RUN_RE.search(zh_plain)
            # 光看"连续 8 个英文单词"会误伤图表标签与技术名词串
            # （fortran algol cobol basic c pascal prolog…）。加一条：这段英文里
            # 必须真的出现功能词，才算"像句子"。
            if m and len(FUNC_WORD_RE.findall(m.group(0))) >= 2 and not ALLOW_KEEP.match(zh_plain):
                # 再区分"漏译"与"有意保留"：如果这段英文**在原文里就一模一样地存在**，
                # 说明译者是有意照抄的（论文页眉、OCR 残留原文、要求模型复述的原始提示词），
                # 不是忘了翻译。这类记为提示性指标 kept_english，不计入违规 ——
                # 否则译者只能靠"删掉原文"来把指标做漂亮，那是用违规换指标。
                if m.group(0).strip() in en_plain:
                    stats["kept_english"] += 1
                else:
                    stats["untranslated"] += 1
                    add("untranslated", where, f"疑似未译英文：{m.group(0)[:60]}")

        # --- 排版：中英文之间漏空格
        for mm in SPACING_BAD_RE.finditer(zh_plain):
            stats["spacing"] += 1
            add("spacing", where, f"中英文之间缺空格：…{zh_plain[max(0, mm.start()-12):mm.end()+12]}…")
            break

    # --- 术语一致率
    zh_all = "\n".join(block_plain(b) for b in zh_blocks if b["type"] != "code")
    en_all = "\n".join(block_plain(b) for b in en_blocks if b["type"] != "code")
    all_correct = [base_form(t) for t in terms if not t.get("keep") and base_form(t)]
    for t in terms:
        if t.get("keep"):
            continue
        zh_form = base_form(t)
        if not zh_form:
            continue
        hits = zh_all.count(zh_form)
        for bad in t.get("forbid", []):
            n = count_forbidden(zh_all, bad, all_correct)
            if n:
                stats["term_violations"] += n
                term_violation_detail.append(f"{t['en']} 应作「{zh_form}」，出现禁用写法「{bad}」×{n}")
                add("term_violation", "全文", f"禁用写法「{bad}」出现 {n} 次（应为「{zh_form}」）")
        for pat in t.get("forbid_re", []):
            hits_list = count_forbidden_re(zh_all, pat, all_correct)
            if hits_list:
                stats["term_violations"] += len(hits_list)
                detail = "、".join(sorted(set(hits_list))[:4])
                term_violation_detail.append(
                    f"{t['en']} 应作「{zh_form}」，命中禁用式 /{pat}/：{detail}")
                add("term_violation", "全文",
                    f"命中禁用式 /{pat}/（应为「{zh_form}」），如：{detail}")
        # 英文原词出现在原文、中文定译却一次没出现 → 记为"术语缺失"（提示性指标），
        # 不计入违规数。它可能说明漏译，也可能只是这个词在译文里用了别的合理表达；
        # 把它算成违规会污染一致率这个核心指标。
        if re.search(rf"(?<![A-Za-z]){re.escape(t['en'])}(?![A-Za-z])", en_all, re.I):
            if hits == 0:
                stats["term_missing"] += 1
                term_violation_detail.append(
                    f"[术语缺失] {t['en']} 在原文出现但译文中未见定译「{zh_form}」")
        stats["term_hits"] += hits

    total_term = stats["term_hits"] + stats["term_violations"]
    stats["term_consistency"] = round(stats["term_hits"] / total_term, 4) if total_term else 1.0
    stats["issues"] = len(issues)
    stats["term_detail"] = term_violation_detail
    return {"stats": stats, "issues": issues}


def main() -> int:
    ap = argparse.ArgumentParser(description="S10 质检")
    ap.add_argument("--slug", help="只检查指定语料")
    args = ap.parse_args()

    C.ensure_dirs(C.REPORTS, C.WORK)
    terms = load_glossary()
    index = C.read_json(os.path.join(C.ROOT, "corpus", "index.json"), {}) or {}
    meta = {i["slug"]: i for i in index.get("items", [])}

    slugs = [args.slug] if args.slug else [
        os.path.splitext(os.path.basename(p))[0]
        for p in sorted(glob.glob(os.path.join(CORPUS_EN, "*.md")))
    ]

    results = []
    agg = {"empty": 0, "untranslated": 0, "truncated": 0, "code_changed": 0,
           "link_lost": 0, "structure": 0, "spacing": 0, "issues": 0,
           "term_hits": 0, "term_violations": 0, "term_missing": 0, "translated": 0,
           "segments": 0, "segments_translated": 0}
    missing: list[str] = []

    for slug in slugs:
        en_path = os.path.join(CORPUS_EN, slug + ".md")
        zh_path = os.path.join(CORPUS_ZH, slug + ".md")
        if not os.path.exists(zh_path) or os.path.getsize(zh_path) == 0:
            missing.append(slug)
            continue
        res = check_pair(C.read_any_text(en_path), C.read_any_text(zh_path), terms)
        res["slug"] = slug
        res["title"] = meta.get(slug, {}).get("title", slug)
        res["group"] = meta.get(slug, {}).get("group", "?")
        results.append(res)
        agg["translated"] += 1
        for k in ("empty", "untranslated", "truncated", "code_changed",
                  "link_lost", "structure", "spacing", "issues"):
            agg[k] += res["stats"][k]
        agg["term_hits"] += res["stats"]["term_hits"]
        agg["term_violations"] += res["stats"]["term_violations"]
        agg["term_missing"] += res["stats"].get("term_missing", 0)
        # 段级统计
        en_blocks = parse_markdown(C.read_any_text(en_path))
        zh_blocks = parse_markdown(C.read_any_text(zh_path))
        agg["segments"] += sum(1 for b in en_blocks if b["type"] != "code")
        agg["segments_translated"] += min(len(en_blocks), len(zh_blocks))

    total_term = agg["term_hits"] + agg["term_violations"]
    consistency = round(agg["term_hits"] / total_term, 4) if total_term else 1.0

    # ---------- 报告 ----------
    lines = ["# 质量抽检报告", "",
             f"> 自动生成于 {C.now_iso()} ｜ 由 `src/s10_qa.py` 产出 ｜ "
             f"检查项对应 `TRANSLATION_SPEC.md` 的 R1–R10", "",
             "## 一、总览", "",
             "| 指标 | 数值 | 判定 |", "|---|---:|---|"]
    rows = [
        ("已译份数", f"{agg['translated']}/{len(slugs)}", "—"),
        ("段级结构对齐", f"{agg['segments_translated']}/{agg['segments']}",
         "✅" if agg["structure"] == 0 else "⚠️"),
        ("空译", agg["empty"], "✅" if agg["empty"] == 0 else "❌"),
        ("漏译/截断", agg["truncated"], "✅" if agg["truncated"] == 0 else "❌"),
        ("疑似未译英文", agg["untranslated"], "✅" if agg["untranslated"] == 0 else "⚠️"),
        ("代码块被改动", agg["code_changed"], "✅" if agg["code_changed"] == 0 else "❌"),
        ("链接丢失", agg["link_lost"], "✅" if agg["link_lost"] == 0 else "❌"),
        ("结构不一致", agg["structure"], "✅" if agg["structure"] == 0 else "❌"),
        ("中英文缺空格", agg["spacing"], "✅" if agg["spacing"] == 0 else "⚠️"),
        ("术语一致率", f"{consistency:.1%}",
         "✅" if consistency >= 0.98 else "⚠️"),
    ]
    for r in rows:
        lines.append(f"| {r[0]} | {r[1]} | {r[2]} |")
    lines.append("")
    lines.append(f"- 术语命中 **{agg['term_hits']}** 次 / 违规 **{agg['term_violations']}** 次"
                 f" / 术语缺失（提示性）**{agg['term_missing']}** 处")
    lines.append("")
    lines.append("> **关于质检口径的一条取舍**：本报告刻意**不做**无法可靠判定的检查。")
    lines.append("> 例如 `prompt` 的名词义必须译「提示词」，但动名词义（prompting）在中文里正当译法就是「提示」")
    lines.append("> ——「零样本提示」「思维链提示」「角色提示」。曾用正则 `提示(?!词|工程|…)` 去拦，")
    lines.append("> 结果 26 条命中里没有一条是错的。**一条误报会让二十条真报一起被忽略**，")
    lines.append("> 所以该规则被撤掉，改为用「术语缺失」这一提示性指标间接观察。")
    if missing:
        lines.append(f"- 尚未翻译：**{len(missing)}** 份")
        lines.append("")
        for s in missing[:40]:
            lines.append(f"  - `{s}`")
    lines.append("")

    lines.append("## 二、逐份结果")
    lines.append("")
    lines.append("| 语料 | 分组 | 块数 | 问题数 | 术语一致率 |")
    lines.append("|---|---|---:|---:|---:|")
    for r in sorted(results, key=lambda x: -x["stats"]["issues"]):
        lines.append(f"| `{r['slug'][:52]}` | {r['group']} | "
                     f"{r['stats']['blocks_zh']}/{r['stats']['blocks_en']} | "
                     f"{r['stats']['issues']} | {r['stats']['term_consistency']:.1%} |")
    lines.append("")

    scan = ["# 问题逐条清单", "",
            f"> 共 {agg['issues']} 条。按严重程度排序：结构/代码/链接/空译 → 术语 → 排版。", ""]
    order = {"code_changed": 0, "structure": 1, "link_lost": 2, "empty": 3,
             "truncated": 4, "untranslated": 5, "term_violation": 6, "spacing": 7,
             "extra": 8}
    for r in sorted(results, key=lambda x: -x["stats"]["issues"]):
        if not r["issues"]:
            continue
        scan.append(f"## `{r['slug']}`（{len(r['issues'])} 条）")
        scan.append("")
        for it in sorted(r["issues"], key=lambda x: order.get(x["kind"], 9))[:60]:
            scan.append(f"- **{it['kind']}** · {it['where']} · {it['detail']}")
        if len(r["issues"]) > 60:
            scan.append(f"- … 其余 {len(r['issues']) - 60} 条从略")
        scan.append("")

    # 单文件模式（--slug）不得覆盖全局报告。
    # 踩过的坑：翻译批次按规范做自查时跑的是 `s10_qa.py --slug X`，
    # 而脚本把结果写进了 reports/_qa.json，于是全局汇总被最后一份文件的
    # "0 问题"报告覆盖 —— 汇总数字看起来完美，其实什么都没查。
    if args.slug:
        C.ensure_dirs(C.WORK)
        C.write_json(os.path.join(C.WORK, f"qa_{args.slug}.json"),
                     {"generated_at": C.now_iso(), "slug": args.slug,
                      "stats": results[0]["stats"] if results else None,
                      "issues": results[0]["issues"] if results else []})
        if not results:
            C.log(f"[质检] {args.slug}：尚无译文")
            return 1
        st = results[0]["stats"]
        C.log(f"[质检] {args.slug}")
        C.log(f"       块 {st['blocks_zh']}/{st['blocks_en']} ｜ 问题 {st['issues']} 条 "
              f"（空译 {st['empty']} / 截断 {st['truncated']} / 结构 {st['structure']} / "
              f"链接 {st['link_lost']} / 未译英文 {st['untranslated']} / 缺空格 {st['spacing']}）")
        C.log(f"       术语一致率 {st['term_consistency']:.1%}")
        for it in results[0]["issues"][:15]:
            C.log(f"       - {it['kind']} · {it['where']} · {it['detail']}")
        return 0

    C.write_text(os.path.join(C.REPORTS, "_qa_report.md"), "\n".join(lines))
    C.write_text(os.path.join(C.REPORTS, "_qa_scan.md"), "\n".join(scan))
    C.write_json(os.path.join(C.REPORTS, "_qa.json"), {
        "generated_at": C.now_iso(), "aggregate": {**agg, "term_consistency": consistency},
        "missing": missing,
        "items": [{"slug": r["slug"], "group": r["group"], "stats": r["stats"]} for r in results],
        "issues": [{"slug": r["slug"], **it} for r in results for it in r["issues"]],
    })

    C.log(f"[质检] 已译 {agg['translated']}/{len(slugs)} 份")
    C.log(f"       结构不一致 {agg['structure']} ｜ 代码改动 {agg['code_changed']} "
          f"｜ 链接丢失 {agg['link_lost']} ｜ 空译 {agg['empty']} ｜ 截断 {agg['truncated']}")
    C.log(f"       术语一致率 {consistency:.1%}（命中 {agg['term_hits']} / 违规 {agg['term_violations']}）")
    C.log(f"       未译英文段 {agg['untranslated']} ｜ 缺空格 {agg['spacing']} ｜ 问题合计 {agg['issues']}")
    if missing:
        C.log(f"       尚未翻译 {len(missing)} 份")
    C.log("完成 · 输出 reports/_qa_report.md / _qa_scan.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
