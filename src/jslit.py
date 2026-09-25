#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从压缩过的 JS 产物里安全取出对象/数组字面量。

为什么需要它
------------
CS146S 官网是纯客户端渲染的 Next.js 应用：课程大纲（syllabus）、FAQ、评分标准
**都不在 HTML 里**，而是内联在 `/_next/static/chunks/*.js` 的压缩代码中，
形如 `eP=[{title:"Week 1: ...",topics:[...]},...]`。

常规做法是起一个无头浏览器去点页面，但那会引入 200MB 级的运行时依赖，
与"任何人 clone 下来就能复跑"的目标冲突。

这里改用**手写词法扫描**：只识别字符串 / 模板串 / 注释 / 括号，遇到
`{` 或 `,` 之后紧跟的裸标识符就给它加引号，最后交给 json 解析。
整个过程**不 eval、不 exec**，压缩包里的任何代码都不会被执行。

公开接口
--------
find_literal(text, anchor)  -> 从 anchor 处的 `[`/`{` 开始取平衡的字面量
js_to_json(js)              -> 把 JS 字面量转成合法 JSON 文本
parse_literal(js)           -> 直接得到 Python 对象
extract_assignment(text, name) -> 取出 `name=<字面量>` 的值
"""

from __future__ import annotations

import json
import re

_OPEN = {"[": "]", "{": "}"}
_CLOSE = {"]": "[", "}": "{"}
_IDENT_START = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$")
_IDENT_CHARS = _IDENT_START | set("0123456789")


def find_literal(text: str, start: int) -> str:
    """返回 text[start] 处那个 `[`/`{` 对应的完整平衡字面量（含首尾括号）。

    会正确跳过字符串、模板串、转义符与注释中的括号。
    """
    if start >= len(text) or text[start] not in _OPEN:
        raise ValueError(f"位置 {start} 不是 [ 或 {{ ，而是 {text[start:start+20]!r}")

    stack: list[str] = []
    i = start
    n = len(text)
    while i < n:
        ch = text[i]
        if ch in "\"'`":
            quote = ch
            i += 1
            while i < n:
                c = text[i]
                if c == "\\":
                    i += 2
                    continue
                if c == quote:
                    break
                i += 1
            i += 1
            continue
        if ch == "/" and i + 1 < n and text[i + 1] == "/":
            j = text.find("\n", i)
            i = n if j < 0 else j + 1
            continue
        if ch == "/" and i + 1 < n and text[i + 1] == "*":
            j = text.find("*/", i)
            i = n if j < 0 else j + 2
            continue
        if ch in _OPEN:
            stack.append(ch)
        elif ch in _CLOSE:
            if not stack or stack[-1] != _CLOSE[ch]:
                raise ValueError(f"括号不匹配，位置 {i}")
            stack.pop()
            if not stack:
                return text[start : i + 1]
        i += 1
    raise ValueError("字面量未闭合")


def js_to_json(js: str) -> str:
    """把 JS 对象/数组字面量转成合法 JSON 文本。

    支持：裸键名加引号、单引号字符串、模板串（无插值）、尾随逗号、
    `undefined` → `null`。含 `${}` 插值的模板串会直接报错，避免悄悄产出错误数据。
    """
    out: list[str] = []
    i = 0
    n = len(js)
    # 上一个"有意义的"字符，用来判断当前位置是否处于"期待键名"的位置
    prev_sig = ""
    while i < n:
        ch = js[i]

        # --- 注释：直接丢弃
        if ch == "/" and i + 1 < n and js[i + 1] == "/":
            j = js.find("\n", i)
            i = n if j < 0 else j
            continue
        if ch == "/" and i + 1 < n and js[i + 1] == "*":
            j = js.find("*/", i)
            i = n if j < 0 else j + 2
            continue

        # --- 字符串
        if ch in "\"'`":
            quote = ch
            j = i + 1
            buf = []
            while j < n:
                c = js[j]
                if c == "\\":
                    nxt = js[j + 1] if j + 1 < n else ""
                    mapping = {"n": "\n", "t": "\t", "r": "\r", "b": "\b", "f": "\f"}
                    if nxt in mapping:
                        buf.append(mapping[nxt])
                        j += 2
                        continue
                    if nxt == "u":
                        try:
                            buf.append(chr(int(js[j + 2 : j + 6], 16)))
                            j += 6
                            continue
                        except ValueError:
                            pass
                    buf.append(nxt)
                    j += 2
                    continue
                if c == quote:
                    break
                buf.append(c)
                j += 1
            if quote == "`":
                raw = js[i + 1 : j]
                if "${" in raw:
                    raise ValueError("模板串含 ${} 插值，无法静态解析")
            out.append(json.dumps("".join(buf), ensure_ascii=False))
            prev_sig = quote
            i = j + 1
            continue

        # --- 标识符 / 键名
        if ch in _IDENT_START:
            j = i
            while j < n and js[j] in _IDENT_CHARS:
                j += 1
            word = js[i:j]
            k = j
            while k < n and js[k] in " \t\r\n":
                k += 1
            is_key = prev_sig in ("{", ",") and k < n and js[k] == ":"
            if is_key:
                out.append(json.dumps(word, ensure_ascii=False))
            elif word == "undefined":
                out.append("null")
            elif word in ("true", "false", "null"):
                out.append(word)
            else:
                raise ValueError(f"无法解析的裸标识符 {word!r}（位置 {i}）")
            prev_sig = word[-1]
            i = j
            continue

        # --- 尾随逗号：`]` / `}` 前多余的逗号在 JSON 里非法
        if ch == ",":
            k = i + 1
            while k < n and js[k] in " \t\r\n":
                k += 1
            if k < n and js[k] in "]}":
                i += 1  # 丢弃这个逗号
                continue

        if not ch.isspace():
            prev_sig = ch
        out.append(ch)
        i += 1

    return "".join(out)


def parse_literal(js: str):
    """JS 字面量 → Python 对象。"""
    return json.loads(js_to_json(js))


def find_assignment_start(text: str, name: str) -> int:
    """定位 `name=` 右侧字面量的起始下标（可能是 `[` 或 `{`）。

    用词边界匹配，避免把 `xeA=` 误当成 `eA=`。
    """
    m = re.search(r"(?<![A-Za-z0-9_$])" + re.escape(name) + r"\s*=\s*(?=[\[{])", text)
    if not m:
        raise KeyError(f"未找到赋值 {name}=<字面量>")
    idx = m.end()
    j = idx
    while j < len(text) and text[j] in " \t\r\n":
        j += 1
    if text[j] not in _OPEN:
        raise ValueError(f"{name}= 右侧不是字面量，而是 {text[j:j+30]!r}")
    return j


def extract_assignment(text: str, name: str):
    """取出 `name=<字面量>` 并解析成 Python 对象。"""
    return parse_literal(find_literal(text, find_assignment_start(text, name)))


def extract_by_anchor(text: str, anchor: str, *, window: int = 400_000):
    """以内容特征定位数组字面量，不依赖压缩后的变量名。

    压缩产物的变量名每次构建都会变，所以这里给出不依赖变量名的退路：
    从 anchor 出现的位置向左扫描，找到最近的一个**处于括号深度 0** 的 `[`，
    解析它并**校验结果里确实含有 anchor**（校验不过就继续往左找）。

    这样即使站点重新构建，只要内容还在，脚本就能把数据取出来。
    """
    idx = text.find(anchor)
    if idx < 0:
        raise KeyError(f"未找到锚点 {anchor!r}")

    j = idx - 1
    depth = 0
    limit = max(0, idx - window)
    tried = []
    while j >= limit:
        ch = text[j]
        if ch in "}]":
            depth += 1
        elif ch in "[{":
            if depth > 0:
                depth -= 1
            elif ch == "[":
                try:
                    lit = find_literal(text, j)
                    if anchor in lit:
                        return parse_literal(lit)
                    tried.append(j)
                except ValueError:
                    pass
        j -= 1
    raise ValueError(f"锚点 {anchor!r} 向左 {window} 字符内没找到含它的数组字面量")


def split_top_level_arrays(text: str, anchor: str) -> list:
    """找出文中所有包含 anchor 的顶层数组字面量（按出现顺序）。"""
    results = []
    pos = 0
    while True:
        idx = text.find(anchor, pos)
        if idx < 0:
            return results
        j = idx
        while j >= 0 and text[j] != "[" and text[j] != "{":
            j -= 1
        if j < 0:
            return results
        try:
            results.append((j, parse_literal(find_literal(text, j))))
        except ValueError:
            return results
        pos = idx + len(anchor)
