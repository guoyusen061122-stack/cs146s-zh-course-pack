#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Markdown → 结构化块。中英对照质检的基础设施。

为什么需要它
------------
译文质量不能只靠"看起来还行"。要能**机器核对**，就得把英文原文和中文译文
都解析成同一套块序列，再逐块比较：

  - 块的数量与类型是否一一对应（漏译/多译/结构被改会立刻暴露）
  - 代码块是否**逐字节相同**（代码不该被翻译）
  - 链接地址是否**全部保留**（译文字数变了，URL 不该变）
  - 表格行列数是否一致
  - 空块、残留英文、术语是否合规

块类型
------
{"type":"heading","level":2,"text":...}
{"type":"para","text":...}
{"type":"list","ordered":bool,"items":[...]}
{"type":"code","lang":...,"text":...}
{"type":"table","header":[...],"rows":[[...]]}
{"type":"quote","text":...}
{"type":"rule"}
"""

from __future__ import annotations

import re

FENCE_RE = re.compile(r"^\s*(```+|~~~+)\s*([A-Za-z0-9+#._-]*)\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)）])\s+(.*)$")
QUOTE_RE = re.compile(r"^\s*>\s?(.*)$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
RULE_RE = re.compile(r"^\s*([-*_])\s*(\1\s*){2,}$")


def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    out, buf, esc = [], [], False
    for ch in line:
        if esc:
            buf.append(ch)
            esc = False
        elif ch == "\\":
            esc = True
        elif ch == "|":
            out.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    out.append("".join(buf).strip())
    return out


def parse_markdown(md: str) -> list[dict]:
    lines = md.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    blocks: list[dict] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # --- 围栏代码块
        # 注意：信息串里可能带属性（Mintlify 的文档就写成
        # ```` ```txt title="claude (plan mode)" wrap theme={null} ````）。
        # 第一版正则要求信息串后面直接是行尾，认不出这种围栏，于是把**开围栏当成了闭围栏**，
        # 结果把大段正文散文判成了代码块 —— 而代码块在流水线里是"不翻译"的，
        # 于是这些正文**从未进入翻译队列**却没人发现。详见 AI日志。
        fence = FENCE_RE.match(line)
        if fence:
            # 闭围栏要用**完整的**围栏串去匹配（CommonMark 规定：4 个反引号开的块
            # 必须由 4 个反引号关闭，3 个反引号关不掉）。
            # 原来的写法 `fence.group(1)[0] * 3` 把任何长度的围栏都截成 3 个反引号，
            # 遇到块内含 3 反引号时可能提前闭合。实测在本项目语料上块数不变，
            # 但保留正确写法，免得注释与代码互相矛盾。
            marker = fence.group(1)
            lang = fence.group(2)
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith(marker):
                buf.append(lines[i])
                i += 1
            i += 1  # 跳过结束围栏
            blocks.append({"type": "code", "lang": lang, "text": "\n".join(buf)})
            continue

        if not line.strip():
            i += 1
            continue

        if RULE_RE.match(line):
            blocks.append({"type": "rule"})
            i += 1
            continue

        h = HEADING_RE.match(line)
        if h:
            blocks.append({"type": "heading", "level": len(h.group(1)),
                           "text": h.group(2).strip()})
            i += 1
            continue

        # --- 引用（连续 > 行为一块）
        if QUOTE_RE.match(line):
            buf = []
            while i < n and QUOTE_RE.match(lines[i]):
                buf.append(QUOTE_RE.match(lines[i]).group(1))
                i += 1
            blocks.append({"type": "quote", "text": "\n".join(buf).strip()})
            continue

        # --- 表格：含分隔行的连续 | 行
        if "|" in line and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1]):
            header = _split_row(line)
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(_split_row(lines[i]))
                i += 1
            width = len(header)
            rows = [(r + [""] * width)[:width] for r in rows]
            blocks.append({"type": "table", "header": header, "rows": rows})
            continue

        # --- 列表（连续列表行合成一块）
        if LIST_RE.match(line):
            items: list[str] = []
            ordered = False
            while i < n:
                m = LIST_RE.match(lines[i])
                if m:
                    if m.group(2)[0].isdigit():
                        ordered = True
                    items.append(m.group(3).strip())
                    i += 1
                elif lines[i].strip() and lines[i].startswith(("  ", "\t")) and items:
                    items[-1] = items[-1] + " " + lines[i].strip()
                    i += 1
                else:
                    break
            blocks.append({"type": "list", "ordered": ordered, "items": items})
            continue

        # --- 段落：连续非空行
        buf = []
        while i < n and lines[i].strip() and not (
            FENCE_RE.match(lines[i]) or HEADING_RE.match(lines[i])
            or QUOTE_RE.match(lines[i]) or LIST_RE.match(lines[i])
            or RULE_RE.match(lines[i])
        ):
            buf.append(lines[i].strip())
            i += 1
        if buf:
            blocks.append({"type": "para", "text": " ".join(buf)})

    return blocks


INLINE_LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)\s]+)")
CODE_SPAN_RE = re.compile(r"`([^`]*)`")
MD_MARKS_RE = re.compile(r"(\*\*|__|\*|_|~~)")


def plain(text: str) -> str:
    """剥掉行内标记，得到纯文本（术语检查与字数统计用）。"""
    t = INLINE_LINK_RE.sub(lambda m: m.group(1), text)
    t = CODE_SPAN_RE.sub(lambda m: m.group(1), t)
    t = MD_MARKS_RE.sub("", t)
    return re.sub(r"\s+", " ", t).strip()


def links(text: str) -> list[str]:
    return [m.group(2) for m in INLINE_LINK_RE.finditer(text)]


def block_text(b: dict) -> str:
    """把一个块拼成可检查的整段文本。"""
    t = b["type"]
    if t in ("heading", "para", "quote"):
        return b["text"]
    if t == "list":
        return "\n".join(b["items"])
    if t == "code":
        return b["text"]
    if t == "table":
        return "\n".join([" | ".join(b["header"])] + [" | ".join(r) for r in b["rows"]])
    return ""


def block_plain(b: dict) -> str:
    return plain(block_text(b))


def iter_segments(blocks: list[dict]):
    """把块展开成可切分的"最小翻译单元"，并给出稳定编号。

    段落/标题各算一段；列表的每一项各算一段；代码块与表格整体各算一段
    （代码不翻译，表格按行整体校验）。
    """
    idx = 0
    for bi, b in enumerate(blocks):
        if b["type"] == "list":
            for ii, item in enumerate(b["items"]):
                idx += 1
                yield {"id": f"b{bi:04d}-i{ii:02d}", "block": bi, "kind": "list_item",
                       "text": item}
        elif b["type"] == "rule":
            continue
        else:
            idx += 1
            yield {"id": f"b{bi:04d}", "block": bi, "kind": b["type"],
                   "text": block_text(b)}
