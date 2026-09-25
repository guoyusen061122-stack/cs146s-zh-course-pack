#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""纯标准库 PDF 文本层提取器。

为什么自己写
------------
课程 16 份 PDF（13 份讲义 + 3 份官方文档）是语料的大头，必须有 PDF 文本提取。
但本项目有两条硬约束：

1. **可复现**：希望 `clone` 下来零依赖就能跑；
2. **License 干净**：业界常用的 PyMuPDF 是 **AGPL-3.0**，装进 MIT 仓库是明确的
   授权冲突（"把 AGPL 作品装进 MIT 仓库"正是挑战三条红线之一）。

外加本机沙箱禁止 pip 写临时目录，第三方包根本装不上。
于是只剩一条路：用标准库把文本层抠出来。好在需要的只是：
对象扫描 → FlateDecode（zlib 是标准库）→ 内容流里识别文本算子 → 用 ToUnicode CMap 解码。

能力边界（如实说明，不夸大）
--------------------------
- 支持：FlateDecode 内容流、Type0/TrueType/Type1 字体的 ToUnicode 映射、
  WinAnsi/MacRoman 简单编码、Form XObject 递归、TJ 字距断词。
- **不支持**：纯图片扫描件（无文字层，需 OCR）、LZW/JPEG2000 等少见滤镜、
  竖排与复杂 CMap 的高级特性。遇到不支持的会**抛出或明确标记**，不会静默给空文本。
"""

from __future__ import annotations

import re
import zlib

# ---------------------------------------------------------------- 编码表
WIN_ANSI_HIGH = {
    0x80: "\u20ac", 0x82: "\u201a", 0x83: "\u0192", 0x84: "\u201e", 0x85: "\u2026",
    0x86: "\u2020", 0x87: "\u2021", 0x88: "\u02c6", 0x89: "\u2030", 0x8A: "\u0160",
    0x8B: "\u2039", 0x8C: "\u0152", 0x8E: "\u017d", 0x91: "\u2018", 0x92: "\u2019",
    0x93: "\u201c", 0x94: "\u201d", 0x95: "\u2022", 0x96: "\u2013", 0x97: "\u2014",
    0x98: "\u02dc", 0x99: "\u2122", 0x9A: "\u0161", 0x9B: "\u203a", 0x9C: "\u0153",
    0x9E: "\u017e", 0x9F: "\u0178",
}
MAC_ROMAN_HIGH = {
    0x80: "\u00c4", 0x81: "\u00c5", 0x82: "\u00c7", 0x83: "\u00c9", 0x84: "\u00d1",
    0x85: "\u00d6", 0x86: "\u00dc", 0x87: "\u00e1", 0x88: "\u00e0", 0x89: "\u00e2",
    0x8a: "\u00e4", 0x8b: "\u00e3", 0x8c: "\u00e5", 0x8d: "\u00e7", 0x8e: "\u00e9",
    0x8f: "\u00e8", 0x90: "\u00ea", 0x91: "\u00eb", 0x92: "\u00ed", 0x93: "\u00ec",
    0x94: "\u00ee", 0x95: "\u00ef", 0x96: "\u00f1", 0x97: "\u00f3", 0x98: "\u00f2",
    0x99: "\u00f4", 0x9a: "\u00f6", 0x9b: "\u00f5", 0x9c: "\u00fa", 0x9d: "\u00f9",
    0x9e: "\u00fb", 0x9f: "\u00fc", 0xa0: "\u2020", 0xa1: "\u00b0", 0xa2: "\u00a2",
    0xa3: "\u00a3", 0xa4: "\u00a7", 0xa5: "\u2022", 0xa6: "\u00b6", 0xa7: "\u00df",
    0xa8: "\u00ae", 0xa9: "\u00a9", 0xaa: "\u2122", 0xab: "\u00b4", 0xac: "\u00a8",
    0xad: "\u2260", 0xae: "\u00c6", 0xaf: "\u00d8", 0xb0: "\u221e", 0xb1: "\u00b1",
    0xb2: "\u2264", 0xb3: "\u2265", 0xb4: "\u00a5", 0xb5: "\u00b5", 0xb6: "\u2202",
    0xb7: "\u2211", 0xb8: "\u220f", 0xb9: "\u03c0", 0xba: "\u222b", 0xbb: "\u00aa",
    0xbc: "\u00ba", 0xbd: "\u03a9", 0xbe: "\u00e6", 0xbf: "\u00f8", 0xc0: "\u00bf",
    0xc1: "\u00a1", 0xc2: "\u00ac", 0xc3: "\u221a", 0xc4: "\u0192", 0xc5: "\u2248",
    0xc6: "\u2206", 0xc7: "\u00ab", 0xc8: "\u00bb", 0xc9: "\u2026", 0xca: "\u00a0",
    0xcb: "\u00c0", 0xcc: "\u00c3", 0xcd: "\u00d5", 0xce: "\u0152", 0xcf: "\u0153",
    0xd0: "\u2013", 0xd1: "\u2014", 0xd2: "\u201c", 0xd3: "\u201d", 0xd4: "\u2018",
    0xd5: "\u2019", 0xd6: "\u00f7", 0xd7: "\u25ca", 0xd8: "\u00ff", 0xd9: "\u0178",
    0xda: "\u2044", 0xdb: "\u20ac", 0xdc: "\u2039", 0xdd: "\u203a", 0xde: "\ufb01",
    0xdf: "\ufb02",
}


def _std_decode(data: bytes, table: dict | None = None) -> str:
    out = []
    for b in data:
        if table and b in table:
            out.append(table[b])
        else:
            out.append(chr(b))
    return "".join(out)


# ---------------------------------------------------------------- 词法
PDF_WS = b"\x00\t\n\x0c\r "
PDF_DELIM = b"()<>[]{}/%"


class Lexer:
    """PDF 词法分析（够用即可：数字 / 名字 / 字符串 / 数组 / 字典 / 关键字）。"""

    def __init__(self, data: bytes, pos: int = 0):
        self.d = data
        self.i = pos

    def skip_ws(self):
        while self.i < len(self.d):
            c = self.d[self.i]
            if c in PDF_WS:
                self.i += 1
            elif c == 0x25:  # %
                while self.i < len(self.d) and self.d[self.i] not in b"\r\n":
                    self.i += 1
            else:
                return

    def peek(self) -> bytes:
        self.skip_ws()
        return self.d[self.i : self.i + 1]

    def read_token(self) -> bytes:
        self.skip_ws()
        if self.i >= len(self.d):
            return b""
        c = self.d[self.i]
        if c == 0x2F:  # /
            j = self.i + 1
            while j < len(self.d) and self.d[j] not in PDF_WS and self.d[j] not in PDF_DELIM:
                j += 1
            tok = self.d[self.i : j]
            self.i = j
            return tok
        if c == 0x28:  # (
            return self.read_literal_string()
        if c == 0x3C:  # <
            if self.d[self.i : self.i + 2] == b"<<":
                self.i += 2
                return b"<<"
            return self.read_hex_string()
        if c == 0x3E and self.d[self.i : self.i + 2] == b">>":
            self.i += 2
            return b">>"
        if c in b"[]{}":
            self.i += 1
            return bytes([c])
        j = self.i
        while j < len(self.d) and self.d[j] not in PDF_WS and self.d[j] not in PDF_DELIM:
            j += 1
        if j == self.i:
            j += 1
        tok = self.d[self.i : j]
        self.i = j
        return tok

    def read_literal_string(self) -> bytes:
        """读 ( ... )，处理转义与嵌套括号。返回原始字节（不含括号）。"""
        assert self.d[self.i] == 0x28
        self.i += 1
        depth = 1
        out = bytearray()
        while self.i < len(self.d):
            c = self.d[self.i]
            if c == 0x5C:  # backslash
                nxt = self.d[self.i + 1] if self.i + 1 < len(self.d) else None
                if nxt is None:
                    break
                mapping = {0x6E: 0x0A, 0x72: 0x0D, 0x74: 0x09, 0x62: 0x08, 0x66: 0x0C,
                           0x28: 0x28, 0x29: 0x29, 0x5C: 0x5C}
                if nxt in mapping:
                    out.append(mapping[nxt])
                    self.i += 2
                elif 0x30 <= nxt <= 0x37:  # 八进制
                    k = self.i + 1
                    oct_digits = b""
                    while k < len(self.d) and len(oct_digits) < 3 and 0x30 <= self.d[k] <= 0x37:
                        oct_digits += bytes([self.d[k]])
                        k += 1
                    out.append(int(oct_digits, 8) & 0xFF)
                    self.i = k
                elif nxt in (0x0A, 0x0D):  # 续行
                    self.i += 2
                    if nxt == 0x0D and self.i < len(self.d) and self.d[self.i] == 0x0A:
                        self.i += 1
                else:
                    out.append(nxt)
                    self.i += 2
                continue
            if c == 0x28:
                depth += 1
                out.append(c)
            elif c == 0x29:
                depth -= 1
                if depth == 0:
                    self.i += 1
                    return bytes(out)
                out.append(c)
            else:
                out.append(c)
            self.i += 1
        return bytes(out)

    def read_hex_string(self) -> bytes:
        assert self.d[self.i] == 0x3C
        j = self.d.find(b">", self.i)
        if j < 0:
            j = len(self.d)
        raw = re.sub(rb"[^0-9A-Fa-f]", b"", self.d[self.i + 1 : j])
        self.i = j + 1
        if len(raw) % 2:
            raw += b"0"
        try:
            return bytes.fromhex(raw.decode("ascii"))
        except ValueError:
            return b""


# ---------------------------------------------------------------- 对象层
class PdfDoc:
    def __init__(self, path: str):
        with open(path, "rb") as fh:
            self.raw = fh.read()
        self.objects: dict[int, tuple[int, int, bytes, bytes | None]] = {}
        self._scan_objects()

    def _scan_objects(self) -> None:
        """扫描 `N G obj ... endobj`。不走 xref 表 —— 对文本提取而言更鲁棒，
        能容忍 xref 损坏或线性化 PDF。

        注意：这里**不能用 `^` 行首锚定**。部分生成器（如 Anthropic 的导出工具）
        用单独的 `\\r` 作换行，而 Python 的 `re.M` 只在 `\\n` 之后认行首，
        加了 `^` 会让 4011 个对象只匹配到 1 个，整份 PDF 一个字都提不出来。
        """
        for m in re.finditer(rb"(?<![\d])(\d+)\s+(\d+)\s+obj\b", self.raw):
            num = int(m.group(1))
            start = m.end()
            end = self.raw.find(b"endobj", start)
            if end < 0:
                continue
            body = self.raw[start:end]
            stream = None
            sm = re.search(rb"\bstream\r?\n", body)
            if sm:
                s_start = sm.end()
                s_end = body.rfind(b"endstream")
                if s_end > s_start:
                    stream = body[s_start:s_end]
                    if stream.endswith(b"\r\n"):
                        stream = stream[:-2]
                    elif stream.endswith(b"\n") or stream.endswith(b"\r"):
                        stream = stream[:-1]
                    dict_part = body[: sm.start()]
                else:
                    dict_part = body
            else:
                dict_part = body
            self.objects[num] = (start, end, dict_part, stream)
        self._expand_object_streams()

    def _decode_stream(self, dict_part: bytes, stream: bytes) -> bytes | None:
        """按 /Filter 链解码流数据；遇到图片类滤镜直接放弃（不是文本源）。"""
        filters = re.findall(rb"/(FlateDecode|LZWDecode|ASCIIHexDecode|ASCII85Decode|"
                             rb"DCTDecode|JPXDecode|RunLengthDecode|CCITTFaxDecode)",
                             dict_part)
        data = stream
        for f in filters:
            name = f.decode()
            if name == "FlateDecode":
                try:
                    data = zlib.decompress(data)
                except zlib.error:
                    try:
                        data = zlib.decompressobj().decompress(data)
                    except zlib.error:
                        return None
            elif name == "ASCIIHexDecode":
                data = Lexer(b"<" + data + b">").read_hex_string()
            else:
                return None
        return data

    def _expand_object_streams(self) -> None:
        """展开对象流（/ObjStm）。

        PDF 1.5 之后，页面字典、字体字典经常被**压缩进对象流**里，
        用 `N G obj` 扫全文件根本扫不到它们 —— 直接后果是整份 PDF "一个字都提不出来"
        （本项目在 Anthropic 那份 23 页 PDF 上真实踩到）。

        对象流的真实布局（踩过坑才写对）：
          - **对象个数 N 与正文起始偏移 First 在流的字典里**（`/N 23 /First 214`），
            不在解压后的数据开头；
          - 解压后的数据 = 先 214 字节的「对象号 相对偏移」成对数字，再是各对象正文，
            每个对象的绝对位置是 `First + 相对偏移`。
        最初把 N/First 当成数据的前两个数字去解析，结果整份文档只解出 0 页。
        """
        for _num, (_s, _e, dpart, stream) in list(self.objects.items()):
            if stream is None or b"/ObjStm" not in dpart:
                continue
            n_match = re.search(rb"/N\s+(\d+)", dpart)
            f_match = re.search(rb"/First\s+(\d+)", dpart)
            if not n_match or not f_match:
                continue
            count, first = int(n_match.group(1)), int(f_match.group(1))
            data = self._decode_stream(dpart, stream)
            if not data or first > len(data):
                continue
            pairs = re.findall(rb"(\d+)\s+(\d+)", data[:first])
            if len(pairs) < count:
                continue
            for i, (onum, off) in enumerate(pairs[:count]):
                onum, off = int(onum), int(off)
                begin = first + off
                end = (first + int(pairs[i + 1][1])) if i + 1 < count else len(data)
                if begin >= len(data):
                    continue
                self.objects.setdefault(onum, (0, 0, data[begin:end], None))

    def stream_data(self, num: int) -> bytes | None:
        obj = self.objects.get(num)
        if not obj:
            return None
        _s, _e, dict_part, stream = obj
        if stream is None:
            return None
        return self._decode_stream(dict_part, stream)

    # -- 字典辅助 -------------------------------------------------
    @staticmethod
    def dict_get(dict_bytes: bytes, key: str) -> bytes | None:
        m = re.search(rb"/" + key.encode() + rb"(?![A-Za-z0-9])", dict_bytes)
        if not m:
            return None
        lx = Lexer(dict_bytes, m.end())
        return lx.read_token()

    @staticmethod
    def dict_get_ref(dict_bytes: bytes, key: str) -> int | None:
        m = re.search(rb"/" + key.encode() + rb"(?![A-Za-z0-9])\s+(\d+)\s+\d+\s+R",
                      dict_bytes)
        return int(m.group(1)) if m else None

    def resolve_dict(self, token: bytes | None) -> bytes | None:
        """`/Font 12 0 R` 这类间接引用解开成对象体。"""
        if token is None:
            return None
        if re.fullmatch(rb"\d+", token):
            return self.objects.get(int(token), (0, 0, b"", None))[2]
        m = re.fullmatch(rb"(\d+)\s+\d+\s+R", token)
        if m:
            return self.objects.get(int(m.group(1)), (0, 0, b"", None))[2]
        return token

    def get_object_body(self, num: int) -> bytes:
        obj = self.objects.get(num)
        return obj[2] if obj else b""


# ---------------------------------------------------------------- 字体解码
class FontMap:
    """把一个字体资源名映射成"字节 → Unicode"的解码函数。"""

    def __init__(self, doc: PdfDoc):
        self.doc = doc
        self.cache: dict[int, dict] = {}

    def build(self, font_obj_num: int) -> dict:
        if font_obj_num in self.cache:
            return self.cache[font_obj_num]
        body = self.doc.get_object_body(font_obj_num)
        table: dict[int, str] = {}
        two_byte = False

        subtype = self.doc.dict_get(body, "Subtype") or b""
        if subtype == b"/Type0":
            two_byte = True

        # 1) ToUnicode CMap（最可靠）
        tu = self.doc.dict_get_ref(body, "ToUnicode")
        if tu is not None:
            cmap = self.doc.stream_data(tu)
            if cmap:
                table = self._parse_tounicode(cmap)

        # 2) 简单字体的 Encoding
        if not table:
            enc = self.doc.dict_get(body, "Encoding") or b""
            enc_body = self.doc.resolve_dict(enc) or b""
            name = enc_body if enc_body.startswith(b"/") else (self.doc.dict_get(enc_body, "BaseEncoding") or b"")
            if b"MacRomanEncoding" in name:
                table = dict(MAC_ROMAN_HIGH)
            elif b"WinAnsiEncoding" in name or b"StandardEncoding" in name or not name:
                table = dict(WIN_ANSI_HIGH)

        info = {"table": table, "two_byte": two_byte}
        self.cache[font_obj_num] = info
        return info

    @staticmethod
    def _parse_tounicode(cmap: bytes) -> dict[int, str]:
        table: dict[int, str] = {}

        def hexval(b: bytes) -> str:
            b = re.sub(rb"[^0-9A-Fa-f]", b"", b)
            if len(b) % 4:
                b = b + b"0" * (4 - len(b) % 4)
            out = []
            for i in range(0, len(b), 4):
                try:
                    out.append(chr(int(b[i : i + 4], 16)))
                except ValueError:
                    pass
            return "".join(out)

        for block in re.findall(rb"beginbfchar(.*?)endbfchar", cmap, re.S):
            for src, dst in re.findall(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]*)>", block):
                try:
                    table[int(src, 16)] = hexval(dst)
                except ValueError:
                    continue
        for block in re.findall(rb"beginbfrange(.*?)endbfrange", cmap, re.S):
            for m in re.finditer(
                rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*(<([0-9A-Fa-f]*)>|\[(.*?)\])",
                block, re.S,
            ):
                lo, hi = int(m.group(1), 16), int(m.group(2), 16)
                if hi - lo > 65535:
                    continue
                if m.group(4) is not None:
                    base = m.group(4)
                    start = hexval(base)
                    if len(start) != 1:
                        for off in range(hi - lo + 1):
                            table[lo + off] = start
                        continue
                    for off in range(hi - lo + 1):
                        table[lo + off] = chr(ord(start) + off)
                else:
                    items = re.findall(rb"<([0-9A-Fa-f]*)>", m.group(5) or b"")
                    for off, it in enumerate(items):
                        if lo + off <= hi:
                            table[lo + off] = hexval(it)
        return table

    @staticmethod
    def decode(raw: bytes, info: dict) -> str:
        table = info.get("table") or {}
        if info.get("two_byte"):
            out = []
            for i in range(0, len(raw) - 1, 2):
                code = (raw[i] << 8) | raw[i + 1]
                out.append(table.get(code, ""))
            return "".join(out)
        return "".join(table.get(b, chr(b)) for b in raw)


# ---------------------------------------------------------------- 内容流
NUM_RE = re.compile(rb"^[+-]?(\d+\.?\d*|\.\d+)$")


def _content_tokens(data: bytes):
    """产出内容流的 token。

    与裸 Lexer 的差别：`[ ... ]` 数组会被**整体**产出（内容流里只有 TJ 会用到数组，
    拆开会让操作数栈拿不到完整数组）。
    """
    lx = Lexer(data)
    d = data
    while True:
        lx.skip_ws()
        if lx.i >= len(d):
            return
        if d[lx.i] == 0x5B:  # [
            start = lx.i
            depth = 0
            j = lx.i
            while j < len(d):
                ch = d[j]
                if ch == 0x5B:
                    depth += 1
                    j += 1
                elif ch == 0x5D:
                    depth -= 1
                    j += 1
                    if depth == 0:
                        break
                elif ch == 0x28:  # 跳过 ( ... )，避免串里的括号干扰
                    sub = Lexer(d, j)
                    sub.read_literal_string()
                    j = sub.i
                elif ch == 0x3C and d[j : j + 2] != b"<<":
                    k = d.find(b">", j)
                    j = (k + 1) if k >= 0 else j + 1
                else:
                    j += 1
            lx.i = j
            yield d[start:j]
            continue
        yield lx.read_token()


def _page_content(doc: PdfDoc, page_body: bytes, depth: int = 0) -> bytes:
    """取出页面的内容流；递归展开 Form XObject。"""
    if depth > 6:
        return b""
    out = bytearray()

    contents = doc.dict_get(page_body, "Contents")
    refs = []
    if contents is not None:
        refs.append(contents)
    else:
        m = re.search(rb"/Contents\s*\[(.*?)\]", page_body, re.S)
        if m:
            refs.extend(re.findall(rb"(\d+)\s+\d+\s+R", m.group(1)))
    for r in refs:
        m = re.fullmatch(rb"(\d+)\s+\d+\s+R", r) or re.fullmatch(rb"(\d+)", r)
        if m:
            sd = doc.stream_data(int(m.group(1)))
            if sd:
                out += sd + b"\n"

    # Form XObject
    xref = doc.dict_get_ref(page_body, "XObject")
    if xref:
        xbody = doc.get_object_body(xref)
        for name, num in re.findall(rb"/([A-Za-z0-9_.+-]+)\s+(\d+)\s+\d+\s+R", xbody):
            sub_body = doc.get_object_body(int(num))
            if b"/Form" in sub_body:
                sd = doc.stream_data(int(num))
                if sd:
                    out += sd + b"\n"
    return bytes(out)


def extract_text_from_content(doc: PdfDoc, content: bytes, font_maps: dict) -> str:
    """把内容流里的文本算子还原成文本（按行）。"""
    lines: list[str] = []
    cur: list[str] = []
    cur_font = None
    pending: list[bytes] = []  # 操作数栈

    def flush():
        nonlocal cur
        text = "".join(cur)
        text = re.sub(r"[ \t]+", " ", text).strip()
        if text:
            lines.append(text)
        cur = []

    def show(raw: bytes):
        nonlocal cur
        info = font_maps.get(cur_font, {"table": {}, "two_byte": False})
        cur.append(FontMap.decode(raw, info))

    for tok in _content_tokens(content):
        if tok in (b"BT", b"ET"):
            flush()
            pending.clear()
            continue
        if tok == b"Tf":
            # 栈形如 [/F1 12 Tf]：取倒数第二个名字
            name = None
            for t in reversed(pending):
                if t.startswith(b"/"):
                    name = t[1:].decode("latin-1")
                    break
            cur_font = name
            pending.clear()
            continue
        if tok in (b"Td", b"TD", b"T*", b"Tm"):
            flush()
            pending.clear()
            continue
        if tok in (b"Tj", b"'", b'"'):
            if pending:
                show(pending[-1])
            if tok in (b"'", b'"'):
                lines.append("".join(cur).strip())
                cur = []
            pending.clear()
            continue
        if tok == b"TJ":
            if pending:
                arr = pending[-1]
                if arr.startswith(b"["):
                    # 数组内部再用一次词法分析，正确还原转义字符串
                    inner = Lexer(arr, 1)
                    while inner.i < len(arr) - 1:
                        item = inner.read_token()
                        if not item:
                            break
                        if item in (b"]", b""):
                            break
                        if NUM_RE.match(item):
                            try:
                                if float(item) < -180:
                                    cur.append(" ")
                            except ValueError:
                                pass
                        else:
                            show(item)
            pending.clear()
            continue

        pending.append(tok)
        if len(pending) > 64:
            pending.pop(0)

    flush()
    # 合并被逐字拆散的片段（很多导出器一个字一个 Tj）
    return "\n".join(lines)


def extract_pdf_text(path: str) -> str:
    """提取整份 PDF 的文本，页间用分页符隔开。"""
    doc = PdfDoc(path)
    pages = []
    fonts_cache = FontMap(doc)

    page_nums = [
        num for num, (_s, _e, dpart, _st) in doc.objects.items()
        if re.search(rb"/Type\s*/Page(?![sA-Za-z])", dpart)
    ]
    if not page_nums:
        return ""
    page_nums.sort()

    for pnum in page_nums:
        body = doc.get_object_body(pnum)
        # 字体资源表
        res_ref = doc.dict_get_ref(body, "Resources")
        res_body = doc.get_object_body(res_ref) if res_ref else body
        font_maps: dict[str, dict] = {}
        fm = re.search(rb"/Font\s*<<(.*?)>>", res_body, re.S)
        font_dict = fm.group(1) if fm else b""
        if not font_dict:
            fref = doc.dict_get_ref(res_body, "Font")
            if fref:
                font_dict = doc.get_object_body(fref)
        for name, objnum in re.findall(rb"/([A-Za-z0-9_.+-]+)\s+(\d+)\s+\d+\s+R", font_dict):
            font_maps[name.decode("latin-1")] = fonts_cache.build(int(objnum))

        content = _page_content(doc, body)
        text = extract_text_from_content(doc, content, font_maps) if content else ""
        pages.append(text)

    return "\n\n\f\n\n".join(pages)


def pdf_stats(path: str) -> dict:
    """给清点步骤用的统计。"""
    doc = PdfDoc(path)
    page_nums = [
        num for num, (_s, _e, dpart, _st) in doc.objects.items()
        if re.search(rb"/Type\s*/Page(?![sA-Za-z])", dpart)
    ]
    text = extract_pdf_text(path)
    chars = len(re.sub(r"\s+", "", text))
    return {"pages": len(page_nums), "chars": chars, "text": text}
