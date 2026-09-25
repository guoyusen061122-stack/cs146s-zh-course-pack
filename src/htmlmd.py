#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HTML → 结构化块（blocks）→ Markdown。

为什么自己写而不是用 trafilatura / readability
---------------------------------------------
1. **可复现**：零第三方依赖，评审方 `git clone` 后不用装任何东西就能重跑；
2. **可审计**：正文抽取的每一步（去样板、找正文根、块切分）都是本项目自己的代码，
   出问题能定位到行，而不是"某个库的黑盒行为"；
3. **够用**：我们面对的是课程官网和几十篇技术博客，结构相对规整。

产出统一为 block 列表，Markdown 与翻译切段都从这里派生 —— 单一事实来源。

block 形态
----------
{"type":"heading","level":1..6,"text":str}
{"type":"para","text":str}                    text 为行内 Markdown
{"type":"code","lang":str,"text":str}
{"type":"list","ordered":bool,"items":[str]}
{"type":"quote","text":str}
{"type":"table","header":[str],"rows":[[str]]}
{"type":"image","src":str,"alt":str}
{"type":"hr"}
"""

from __future__ import annotations

import re
from html.parser import HTMLParser

VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

DROP_TAGS = {
    "script", "style", "noscript", "template", "svg", "canvas", "iframe",
    "form", "button", "select", "option", "textarea", "nav", "footer",
    "header", "aside", "video", "audio", "figure_caption",
}

# 样板区域的 class / id 特征。命中即整棵子树丢弃。
BOILERPLATE_RE = re.compile(
    r"(^|[-_ ])("
    r"nav|navbar|navigation|menu|breadcrumb|sidebar|side-bar|footer|header|"
    r"masthead|site-header|site-footer|topbar|toolbar|"
    r"cookie|consent|gdpr|banner|promo|advert|ad-|ads|sponsor|"
    r"share|sharing|social|subscribe|newsletter|signup|sign-up|"
    r"comment|comments|disqus|related|recommend|more-from|read-next|"
    r"pagination|pager|tags|tag-list|meta-bar|post-meta|byline|author-box|"
    r"search|modal|popup|overlay|skip-link|sr-only|visually-hidden|"
    r"toc|table-of-contents|progress|back-to-top"
    r")($|[-_ ])",
    re.I,
)

# 明确是正文容器的特征，优先选它。
CONTENT_RE = re.compile(
    r"(^|[-_ ])(article|post|content|entry|main|markdown|prose|body|story|"
    r"blog-post|post-content|article-body|entry-content)([-_ ]|$)",
    re.I,
)


class Node:
    __slots__ = ("tag", "attrs", "children", "parent")

    def __init__(self, tag, attrs=None, parent=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children: list = []
        self.parent = parent

    # -- 便捷访问 -------------------------------------------------
    def get(self, name, default=""):
        return self.attrs.get(name, default)

    @property
    def classes(self) -> str:
        return (self.attrs.get("class", "") or "") + " " + (self.attrs.get("id", "") or "")

    def text(self) -> str:
        out = []
        stack = [self]
        while stack:
            cur = stack.pop()
            if isinstance(cur, str):
                out.append(cur)
            else:
                if cur.tag in DROP_TAGS:
                    continue
                stack.extend(reversed(cur.children))
        return re.sub(r"\s+", " ", "".join(out)).strip()

    def walk(self):
        yield self
        for child in self.children:
            if not isinstance(child, str):
                yield from child.walk()

    def __repr__(self):  # pragma: no cover
        return f"<Node {self.tag} {len(self.children)}>"


class _TreeBuilder(HTMLParser):
    AUTO_CLOSE = {"p", "li", "dt", "dd", "option", "tr", "td", "th"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.stack = [self.root]

    def _open(self, tag, attrs):
        while len(self.stack) > 1 and self.stack[-1].tag in self.AUTO_CLOSE and tag not in VOID:
            # 简单启发式：块级标签开启时，自动闭合尚未闭合的 p / li
            if tag in ("p", "li", "dt", "dd", "tr", "td", "th", "ul", "ol", "table", "div", "section"):
                self.stack.pop()
            else:
                break
        node = Node(tag, {k: (v or "") for k, v in attrs}, self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_starttag(self, tag, attrs):
        self._open(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        node = Node(tag, {k: (v or "") for k, v in attrs}, self.stack[-1])
        self.stack[-1].children.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if data.strip():
            self.stack[-1].children.append(data)


def parse_html(html: str) -> Node:
    builder = _TreeBuilder()
    builder.feed(html)
    builder.close()
    return builder.root


# ---------------------------------------------------------------- 正文定位
def _is_boilerplate(node: Node) -> bool:
    return bool(BOILERPLATE_RE.search(node.classes))


def _prune(node: Node) -> None:
    """移除脚本/样式与样板区域。

    关键的安全阀：**样板区本身一定是小的**。如果一个节点的 class 命中了样板特征，
    但它包含上千字符的正文，那多半是"post-header-body 这类把正文也包进来的外层壳"
    —— 直接删掉会连正文一起删。本项目在 GitHub Blog 上真实踩到：
    整页 19,700 字符，剪完只剩 86 字符。阈值 1200 就是照这个案例定的。

    ⚠️ 这个函数**不能事后随意调整**：它决定 corpus/en 的内容，而译文已经与语料逐块对齐。
    改一次阈值，重跑 s05 就会产出不同的语料，既有的译文会全部错位。
    真要改，必须重跑 s05 → s05b → s07 → 重新翻译，代价极大。
    （本项目真的动过一次念头并改了代码，靠冒烟测试发现行为不一致才回滚 —— 见 AI日志。）
    """
    kept = []
    for child in node.children:
        if isinstance(child, str):
            kept.append(child)
            continue
        if child.tag in DROP_TAGS:
            continue
        if _is_boilerplate(child) and len(child.text()) < 1200:
            continue
        if child.tag == "div" and child.get("hidden") == "true":
            continue
        _prune(child)
        kept.append(child)
    node.children = kept


def _score(node: Node) -> float:
    """正文密度打分：段落文字越多分越高，链接占比越高分越低。"""
    text_len = 0
    link_len = 0
    paras = 0
    for sub in node.walk():
        if sub.tag == "p":
            t = sub.text()
            if len(t) > 40:
                paras += 1
                text_len += len(t)
        elif sub.tag == "a":
            link_len += len(sub.text())
    if paras == 0:
        return 0.0
    return text_len * (1.0 - min(link_len / max(text_len, 1), 0.9)) + paras * 25


def find_content_root(root: Node) -> Node:
    """选出正文根节点。

    优先 `<article>` / `<main>` / 语义化 class；否则在所有 div/section 里挑分最高的。
    """
    candidates: list[tuple[float, int, Node]] = []

    for node in root.walk():
        if node.tag in ("article", "main"):
            score = _score(node) + 500  # 语义标签直接加权
            candidates.append((score, _depth(node), node))
        elif node.tag in ("div", "section", "td") and CONTENT_RE.search(node.classes):
            candidates.append((_score(node) + 200, _depth(node), node))

    if not candidates:
        for node in root.walk():
            if node.tag in ("div", "section", "body", "article", "main"):
                s = _score(node)
                if s > 0:
                    candidates.append((s, _depth(node), node))

    if not candidates:
        return root

    # 分高者胜；同分时选更深的（更贴近正文，避免选到最外层容器）
    candidates.sort(key=lambda item: (item[0], item[1]))
    return candidates[-1][2]


def _depth(node: Node) -> int:
    d = 0
    cur = node
    while cur.parent is not None:
        d += 1
        cur = cur.parent
    return d


# ---------------------------------------------------------------- 行内 Markdown
INLINE_SKIP = {"script", "style", "svg", "noscript", "iframe", "button", "form"}


def _inline(node: Node) -> str:
    parts: list[str] = []
    for child in node.children:
        if isinstance(child, str):
            parts.append(re.sub(r"\s+", " ", child))
            continue
        tag = child.tag
        if tag in INLINE_SKIP:
            continue
        inner = _inline(child)
        if tag in ("strong", "b"):
            parts.append(f"**{inner}**" if inner.strip() else inner)
        elif tag in ("em", "i"):
            parts.append(f"*{inner}*" if inner.strip() else inner)
        elif tag in ("code", "kbd", "samp", "tt"):
            parts.append(f"`{inner.strip()}`" if inner.strip() else inner)
        elif tag == "a":
            href = child.get("href")
            label = inner.strip()
            if not href or href.startswith("#"):
                parts.append(label)
            elif not label:
                parts.append(f"<{href}>")
            else:
                parts.append(f"[{label}]({href})")
        elif tag == "br":
            parts.append("  \n")
        elif tag == "img":
            alt = child.get("alt", "").strip()
            src = child.get("src", "")
            if alt:
                parts.append(f"![{alt}]({src})")
        elif tag in ("sup", "sub", "span", "abbr", "mark", "small", "time", "u", "s"):
            parts.append(inner)
        elif tag in ("ul", "ol"):
            parts.append(" " + _list_inline(child) + " ")
        elif tag == "pre":
            parts.append(_code_text(child))
        else:
            parts.append(inner)
    text = "".join(parts)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s+([,.!?;:)\]])", r"\1", text)
    # 网页中的 &#xD83D; 之类数字引用会让解析器产出孤立代理字符，直接丢弃
    text = re.sub(r"[\ud800-\udfff]", "", text)
    return text.strip()


def _code_text(node: Node) -> str:
    lines: list[str] = []
    stack = [node]
    buf: list[str] = []
    while stack:
        cur = stack.pop()
        if isinstance(cur, str):
            buf.append(cur)
        else:
            if cur.tag == "br":
                buf.append("\n")
                continue
            stack.extend(reversed(cur.children))
    return "".join(buf)


def _list_inline(node: Node) -> str:
    items = [_inline(li) for li in node.children if not isinstance(li, str) and li.tag == "li"]
    return " / ".join(i for i in items if i)


# ---------------------------------------------------------------- 块切分
BLOCK_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "pre", "ul", "ol",
              "blockquote", "table", "hr", "figure", "div", "section", "article", "main"}


def _code_lang(node: Node) -> str:
    for sub in node.walk():
        cls = sub.get("class", "")
        m = re.search(r"(?:language|lang|highlight)[- ]([a-zA-Z0-9+#]+)", cls)
        if m:
            return m.group(1).lower()
    return ""


def _table_block(node: Node) -> dict | None:
    rows: list[list[str]] = []
    for tr in node.walk():
        if tr.tag != "tr":
            continue
        cells = [
            _inline(c)
            for c in tr.children
            if not isinstance(c, str) and c.tag in ("td", "th")
        ]
        if cells:
            rows.append(cells)
    if not rows:
        return None
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    header, body = rows[0], rows[1:]
    if not body:
        header, body = [""] * width, rows
    return {"type": "table", "header": header, "rows": body}


def _blocks_from(node: Node, out: list[dict], depth: int = 0) -> None:
    if node.tag in ("pre",):
        code = _code_text(node).strip("\n")
        if code.strip():
            out.append({"type": "code", "lang": _code_lang(node), "text": code})
        return

    if node.tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        text = _inline(node)
        if text:
            out.append({"type": "heading", "level": int(node.tag[1]), "text": text})
        return

    if node.tag == "p":
        text = _inline(node)
        if text:
            out.append({"type": "para", "text": text})
        return

    if node.tag in ("ul", "ol"):
        items = [
            _inline(li)
            for li in node.children
            if not isinstance(li, str) and li.tag == "li"
        ]
        items = [i for i in items if i]
        if items:
            out.append({"type": "list", "ordered": node.tag == "ol", "items": items})
        # 列表项里可能嵌了代码块，单独捞出来
        for li in node.children:
            if isinstance(li, str):
                continue
            for sub in li.walk():
                if sub.tag == "pre":
                    code = _code_text(sub).strip("\n")
                    if code.strip():
                        out.append({"type": "code", "lang": _code_lang(sub), "text": code})
        return

    if node.tag == "blockquote":
        text = _inline(node)
        if text:
            out.append({"type": "quote", "text": text})
        return

    if node.tag == "table":
        blk = _table_block(node)
        if blk:
            out.append(blk)
        return

    if node.tag == "hr":
        out.append({"type": "hr"})
        return

    if node.tag == "img":
        alt = node.get("alt", "").strip()
        if alt:
            out.append({"type": "image", "src": node.get("src", ""), "alt": alt})
        return

    if node.tag in ("div", "section", "article", "main", "body", "#root", "figure",
                    "span", "a", "strong", "em", "code", "dl", "dd", "dt", "details",
                    "summary", "label", "center", "font", "small", "time"):
        # 容器：先看它自己是不是"纯文本叶子"，是就直接出段落
        if not any(isinstance(c, Node) for c in node.children):
            text = _inline(node)
            if text and depth > 0:
                out.append({"type": "para", "text": text})
            return
        # 若容器内没有块级子节点，整段当一段
        has_block = any(
            isinstance(c, Node) and c.tag in BLOCK_TAGS for c in node.children
        )
        if not has_block and node.tag not in ("div", "section", "article", "main", "body", "#root"):
            text = _inline(node)
            if text:
                out.append({"type": "para", "text": text})
            return
        if not has_block and depth > 0 and node.tag in ("div", "span"):
            text = _inline(node)
            if len(text) > 30:
                out.append({"type": "para", "text": text})
            return
        for child in node.children:
            if isinstance(child, str):
                text = re.sub(r"\s+", " ", child).strip()
                if len(text) > 60:
                    out.append({"type": "para", "text": text})
                continue
            _blocks_from(child, out, depth + 1)
        return

    # 兜底：其它标签按容器递归
    for child in node.children:
        if isinstance(child, (str, Node)):
            if isinstance(child, str):
                text = re.sub(r"\s+", " ", child).strip()
                if len(text) > 60:
                    out.append({"type": "para", "text": text})
            else:
                _blocks_from(child, out, depth + 1)


def html_to_blocks(html: str, *, content_root_only: bool = True) -> list[dict]:
    """HTML → block 列表。"""
    root = parse_html(html)
    _prune(root)
    target = find_content_root(root) if content_root_only else root
    blocks: list[dict] = []
    _blocks_from(target, blocks)
    return _dedupe(blocks)


def _dedupe(blocks: list[dict]) -> list[dict]:
    """去掉重复块（有些站点会在正文里再放一份标题/摘要）。"""
    out: list[dict] = []
    seen_recent: list[str] = []
    for b in blocks:
        key = ""
        if b["type"] in ("para", "heading", "quote"):
            key = b["text"].strip()
        if key:
            if key in seen_recent:
                continue
            seen_recent.append(key)
            if len(seen_recent) > 400:
                seen_recent.pop(0)
        out.append(b)
    return out


# ---------------------------------------------------------------- Markdown 输出
def _escape_list_item(text: str) -> str:
    return re.sub(r"\n+", " ", text).strip()


def blocks_to_markdown(blocks: list[dict], *, title: str | None = None) -> str:
    lines: list[str] = []
    if title:
        # 正文里常已带一个同名 H1（网页标题），避免出现两行一样的标题
        if blocks and blocks[0].get("type") == "heading" and blocks[0].get("level") == 1:
            if blocks[0]["text"].strip().lower() == title.strip().lower():
                blocks = blocks[1:]
        lines.append(f"# {title}")
        lines.append("")
    prev_type = None
    for b in blocks:
        t = b["type"]
        if t == "heading":
            if lines and lines[-1] != "":
                lines.append("")
            lines.append("#" * max(1, min(6, b["level"])) + " " + b["text"])
            lines.append("")
        elif t == "para":
            lines.append(b["text"])
            lines.append("")
        elif t == "code":
            lines.append(f"```{b.get('lang','')}".rstrip())
            lines.append(b["text"])
            lines.append("```")
            lines.append("")
        elif t == "list":
            for item in b["items"]:
                lines.append(("- " if not b.get("ordered") else "1. ") + _escape_list_item(item))
            lines.append("")
        elif t == "quote":
            for ln in b["text"].split("\n"):
                lines.append("> " + ln)
            lines.append("")
        elif t == "table":
            header = b["header"]
            lines.append("| " + " | ".join(h.replace("|", "\\|") for h in header) + " |")
            lines.append("|" + "|".join([" --- "] * len(header)) + "|")
            for row in b["rows"]:
                lines.append("| " + " | ".join(str(c).replace("|", "\\|") for c in row) + " |")
            lines.append("")
        elif t == "image":
            lines.append(f"![{b['alt']}]({b['src']})")
            lines.append("")
        elif t == "hr":
            lines.append("---")
            lines.append("")
        prev_type = t
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def html_to_markdown(html: str, *, title: str | None = None,
                     content_root_only: bool = True) -> str:
    return blocks_to_markdown(
        html_to_blocks(html, content_root_only=content_root_only), title=title
    )


def _text_leaves(node: Node, out: list, *, min_len: int) -> None:
    """按文档顺序收集"段落级"节点。

    判据：节点自己不再是纯容器。若它某个子元素本身就含有成篇文字，就继续往下钻；
    否则把整个节点的文字作为一段收下。这样 `<div>` 包裹的排版（Substack、
    Docusaurus、Notion 导出等）也能正确切段，而不是整页一个字都拿不到。
    """
    if node.tag in ("p", "li", "blockquote", "td", "h1", "h2", "h3", "h4", "h5", "h6"):
        out.append(node)
        return
    if node.tag == "pre":
        out.append(node)
        return
    el_children = [c for c in node.children if isinstance(c, Node)]
    if not el_children:
        # 叶子节点：自己有文字就收下。早期版本在这里直接 return，
        # 导致「整个 div 版式的页面一个字都抽不出来」—— 因为最外层有子元素，
        # 递归到叶子又因为"没有子元素"被丢弃。
        if len(node.text()) >= min_len:
            out.append(node)
        return
    rich = [c for c in el_children if len(c.text()) >= min_len]
    if not rich:
        out.append(node)
        return
    for child in el_children:
        _text_leaves(child, out, min_len=min_len)


def page_text(html: str, *, min_len: int = 40, limit: int = 400_000) -> str:
    """兜底抽取：不去猜"正文根"，直接把整页里像正文的段落捞出来。

    前提是**必须先 `_prune`** —— 否则 `<script>` / `<style>` 的内容会被当成正文，
    产出满屏 CSS/JS（本项目在 Anthropic 的文档页上真实踩到过这个坑）。
    """
    root = parse_html(html)
    _prune(root)
    leaves: list = []
    _text_leaves(root, leaves, min_len=min_len)

    out: list[str] = []
    seen: set[str] = set()
    total = 0
    for node in leaves:
        if node.tag == "pre":
            continue
        text = re.sub(r"\s+", " ", node.text()).strip()
        if len(text) < min_len or text in seen:
            continue
        if any(text in prev for prev in out):
            continue
        seen.add(text)
        out.append(text)
        total += len(text)
        if total > limit:
            break
    return "\n\n".join(out)


def plain_text(md: str) -> str:
    """把行内 Markdown 剥成纯文本，用于术语检查与字数统计。"""
    t = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", md)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = t.replace("**", "").replace("*", "").replace("__", "_")
    return re.sub(r"\s+", " ", t).strip()
