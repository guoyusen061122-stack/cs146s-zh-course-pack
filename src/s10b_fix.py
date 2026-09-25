#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S10b · 术语回正与排版修复（数据驱动、留痕、幂等）。

为什么单独一步、而不是让译者重译
--------------------------------
译文由多路并行产出，个别术语会漂移（同一个概念出现两种写法）。
回炉重译整篇成本高，还可能把本来对的地方改错。定向回正只动该动的字符串，
其余一个字符不碰 —— 风险最小、效果最直接。

三条设计约束
------------
1. **规则是数据不是代码**（`config/term_fix_rules.json` + `glossary.json` 的 forbid 字段），
   换一门课只改表，不改脚本。
2. **留痕永不覆盖**：每次回正把逐条 before/after 写进 `src/logs/term_fix_<时间戳>.md`，
   摘要追加到 `reports/_term_fix_log.md`。改了什么、为什么改，全程可追。
3. **幂等自检**：同一份文本上跑第二遍必须零改动；否则报错退出。
   （"规则不幂等"是真实踩过的坑：把 `记录` 替换成 `日志记录`，第二遍又把
   `日志记录` 里的 `记录` 换成 `日志记录`，得到 `日志日志记录`，越跑越烂。）

用法：
    python src/s10b_fix.py              # 试运行（dry-run），只报告不改文件
    python src/s10b_fix.py --apply      # 真正写入
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

CORPUS_ZH = os.path.join(C.ROOT, "corpus", "zh")
RULES = os.path.join(C.CONFIG, "term_fix_rules.json")
GLOSSARY_JSON = os.path.join(C.GLOSSARY_DIR, "glossary.json")

HAN = r"\u4e00-\u9fff\u3400-\u4dbf"
SPACE_LEFT = re.compile(rf"([{HAN}])([A-Za-z0-9])")
SPACE_RIGHT = re.compile(rf"([A-Za-z0-9])([{HAN}])")

FENCE_RE = re.compile(r"(^```.*?^```)", re.S | re.M)


def base_form(t: dict) -> str:
    return re.sub(r"（.*?）", "", t.get("zh", "")).strip()


def build_rules() -> list[dict]:
    """显式规则表 + 术语表 forbid 自动派生的回正规则。"""
    cfg = C.read_json(RULES, {}) or {}
    rules: list[dict] = []
    for r in cfg.get("rules", []):
        if r.get("from") and r.get("to") and r["from"] != r["to"]:
            rules.append({"from": r["from"], "to": r["to"],
                          "reason": r.get("reason", "规则表")})
    terms = (C.read_json(GLOSSARY_JSON, {}) or {}).get("terms", [])
    correct = [base_form(t) for t in terms if not t.get("keep") and base_form(t)]
    for t in terms:
        target = base_form(t)
        if not target:
            continue
        for bad in t.get("forbid", []):
            if bad == target or bad not in correct:
                pass
            # 只有当"禁用写法"没有被别的正确写法包含时，才敢做无脑替换；
            # 否则会改坏（例：把「提示」换成「提示词」，会把「提示工程」变成
            # 「提示词工程」—— 正好制造出新的违规）。
            if any(bad in c and c != target for c in correct):
                continue
            if bad != target:
                rules.append({"from": bad, "to": target,
                              "reason": f"glossary: {t['en']}"})
    # 长规则优先，避免短串先命中把长串切碎
    rules.sort(key=lambda r: -len(r["from"]))
    return rules


def protect(text: str, keep_forms: list[str]) -> tuple[str, list[str]]:
    """把不能改动的片段替换成占位符。

    三类要保护的东西：
    1. 围栏代码块、行内代码 —— 改了就破坏原文；
    2. 链接 URL —— 改了就断链；
    3. **所有"正确写法"** —— 不保护它们会踩非幂等的坑：
       规则「系统提示 → 系统提示词」在第一遍里正确命中，第二遍又会命中
       刚生成的「系统提示词」里的「系统提示」，产出「系统提示词词」。
       这正是本项目在别处已经记录过的"规则不幂等"事故，必须在机制上堵死。
    """
    vault: list[str] = []

    def stash_str(s: str) -> str:
        vault.append(s)
        return f"\x01{len(vault) - 1}\x02"

    text = FENCE_RE.sub(lambda m: stash_str(m.group(0)), text)
    text = re.sub(r"`[^`\n]*`", lambda m: stash_str(m.group(0)), text)
    # 只保护 URL 本身，不要连 `](` `)` 一起塞进占位符（第一版就是这么把链接写坏的）
    text = re.sub(r"\]\(([^)\s]+)\)", lambda m: "](" + stash_str(m.group(1)) + ")", text)
    text = re.sub(r"<(https?://[^>\s]+)>", lambda m: "<" + stash_str(m.group(1)) + ">", text)
    for cf in sorted({c for c in keep_forms if c}, key=len, reverse=True):
        if cf in text:
            text = text.replace(cf, stash_str(cf))
    return text, vault


def restore(text: str, vault: list[str]) -> str:
    def pop(m):
        return vault[int(m.group(1))]

    return re.sub(r"\x01(\d+)\x02", pop, text)


def apply_rules(text: str, rules: list[dict], keep_forms: list[str]) -> tuple[str, list[tuple]]:
    body, vault = protect(text, keep_forms)
    changes: list[tuple] = []
    for r in rules:
        if r["from"] in body:
            n = body.count(r["from"])
            body = body.replace(r["from"], r["to"])
            changes.append((r["from"], r["to"], n, r["reason"]))
    # 排版：只在**汉字与拉丁字母/数字之间补一个空格**。
    #
    # ⚠️ 这里曾经还有一句 `body = re.sub(r" {2,}", " ", body)`（折叠连续空格），
    # 后果是把 9 份译文改坏：unit42 系列的正文是「PDF 抽取后压平的表格」，
    # 靠成百上千个填充空格维持几何，折叠空格直接摧毁了它的块结构与全部链接。
    # 教训：回正步骤只该做**定向的替换**，任何"顺手清理空白"都是危险的 ——
    # 在靠空格排版的内容里，空白就是数据。
    before = body
    body = SPACE_LEFT.sub(r"\1 \2", body)
    body = SPACE_RIGHT.sub(r"\1 \2", body)
    if body != before:
        changes.append(("(中英文之间)", "(补一个空格)", max(len(body) - len(before), 1),
                        "排版规范 R5"))
    return restore(body, vault), changes


def main() -> int:
    ap = argparse.ArgumentParser(description="S10b 术语回正与排版修复")
    ap.add_argument("--apply", action="store_true", help="真正写入（默认试运行）")
    args = ap.parse_args()

    C.ensure_dirs(C.LOGS, C.REPORTS)
    rules = build_rules()
    # "正确写法"先入库保护，避免"禁止→正确"的规则二次命中（非幂等的根源）
    keep_forms = sorted({r["to"] for r in rules}, key=len, reverse=True)
    C.log(f"[规则] {len(rules)} 条（显式表 + glossary 派生），保护写法 {len(keep_forms)} 个")
    for r in rules[:40]:
        C.log(f"   「{r['from']}」→「{r['to']}」  （{r['reason']}）")

    files = sorted(glob.glob(os.path.join(CORPUS_ZH, "*.md")))
    if not files:
        C.log("corpus/zh/ 还是空的，先完成翻译再来回正。")
        return 0

    ts = C.now_iso().replace(":", "").replace("-", "")[:15]
    log_lines = [f"# 术语回正明细 · {C.now_iso()}", "",
                 f"- 规则条数：{len(rules)}", f"- 处理文件：{len(files)}",
                 f"- 模式：{'写入' if args.apply else '试运行（未改动文件）'}", ""]
    total_changes = 0
    touched_files = 0
    idempotent_violations: list[str] = []
    guard_hits: list[str] = []

    for path in files:
        slug = os.path.splitext(os.path.basename(path))[0]
        original = C.read_any_text(path)
        fixed, changes = apply_rules(original, rules, keep_forms)

        # ---------- 防回归护栏：回正不得改变 Markdown 块结构 ----------
        # 这是本项目最惨痛的一次教训换来的：回正步骤曾经"顺手"折叠了连续空格，
        # 结果把 9 份靠空格定宽的译文改坏（块结构错乱、172 处链接丢失）。
        # 现在起，只要块结构发生变化，**直接拒绝写入**并记为护栏拦截。
        if changes:
            import mdblocks

            before_types = [b["type"] for b in mdblocks.parse_markdown(original)]
            after_types = [b["type"] for b in mdblocks.parse_markdown(fixed)]
            if before_types != after_types:
                guard_hits.append(
                    f"{slug}：块结构发生变化（{len(before_types)} → {len(after_types)} 块），已拒绝写入")
                continue

        # 幂等自检：把结果再跑一遍，必须零改动
        again, changes2 = apply_rules(fixed, rules, keep_forms)
        if again != fixed:
            idempotent_violations.append(
                f"{slug}: 第二遍仍产生改动 {[c[:3] for c in changes2]}")

        if not changes:
            continue
        touched_files += 1
        total_changes += sum(c[2] for c in changes)
        log_lines.append(f"## `{slug}`")
        log_lines.append("")
        for frm, to, n, why in changes:
            log_lines.append(f"- `{frm}` → `{to}`（{n} 处；依据：{why}）")
        log_lines.append("")
        if args.apply:
            C.write_text(path, fixed)

    violation_note = ""
    if idempotent_violations:
        violation_note += ("\n## ⚠️ 幂等自检未通过\n\n"
                           + "\n".join(f"- {v}" for v in idempotent_violations) + "\n")
    if guard_hits:
        violation_note += ("\n## 🛡️ 防回归护栏拦截（未写入）\n\n"
                           + "\n".join(f"- {v}" for v in guard_hits) + "\n")

    C.write_text(os.path.join(C.LOGS, f"term_fix_{ts}.md"),
                 "\n".join(log_lines) + violation_note)
    with open(os.path.join(C.REPORTS, "_term_fix_log.md"), "a", encoding="utf-8",
              newline="\n") as fh:
        fh.write(f"\n## {C.now_iso()} · {'写入' if args.apply else '试运行'}\n\n"
                 f"- 涉及文件 {touched_files} / {len(files)}，改动合计 {total_changes} 处\n"
                 f"- 明细：`src/logs/term_fix_{ts}.md`\n")

    C.log(f"\n[回正] 涉及 {touched_files}/{len(files)} 份，改动 {total_changes} 处"
          f"（{'已写入' if args.apply else '试运行，未改文件'}）")
    if guard_hits:
        C.log(f"[护栏] 🛡️ 拦截 {len(guard_hits)} 份（块结构会变，已拒绝写入）：")
        for v in guard_hits[:10]:
            C.log("   " + v)
    if idempotent_violations:
        C.log("[幂等] ❌ 未通过：")
        for v in idempotent_violations:
            C.log("   " + v)
        return 2
    C.log("[幂等] ✅ 通过（同一输入跑第二遍零改动）")
    if not args.apply:
        C.log("       加 --apply 才会真正写入。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
