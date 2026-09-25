#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""冒烟测试：确认流水线的每个环节都还在正常工作。

不是单元测试的替代品，而是"一条命令看清整条管线有没有断"的体检。
覆盖：自研抽取器的核心能力、语料完整性、术语表合法性、译文结构对齐、成品与文档站存在性。

    python tests/test_smoke.py

退出码 0 = 全部通过；非 0 = 有失败项（并逐条打印失败原因）。
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

for _s in ("stdout", "stderr"):
    try:
        getattr(sys, _s).reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass

PASS, FAIL = [], []


def check(name: str, fn) -> None:
    try:
        fn()
        PASS.append(name)
        print(f"  \u2705 {name}")
    except AssertionError as exc:
        FAIL.append((name, str(exc)))
        print(f"  \u274c {name}  → {exc}")
    except Exception as exc:  # noqa: BLE001
        FAIL.append((name, f"{type(exc).__name__}: {exc}"))
        print(f"  \u274c {name}  → {type(exc).__name__}: {exc}")


def section(title: str) -> None:
    print(f"\n=== {title} ===")


# ---------------------------------------------------------------- 1. 自研 JS 解析
section("1. src/jslit.py —— 从压缩 JS 里取结构化数据")

import jslit  # noqa: E402


def t_jslit_basic():
    js = '[{title:"Week 1",topics:["a","b"],n:3,ok:true,x:undefined,},]'
    obj = jslit.parse_literal(js)
    assert obj[0]["title"] == "Week 1", obj
    assert obj[0]["topics"] == ["a", "b"], obj
    assert obj[0]["n"] == 3 and obj[0]["ok"] is True, obj
    assert obj[0]["x"] is None, "undefined 应转成 null"


def t_jslit_strings():
    js = '[{a:"he said \\"hi\\"",b:\'single\',c:"tab\\there"}]'
    obj = jslit.parse_literal(js)
    assert obj[0]["a"] == 'he said "hi"', obj
    assert obj[0]["b"] == "single", obj
    assert obj[0]["c"] == "tab\there", obj


def t_jslit_brackets_in_strings():
    js = '[{a:"[not an array]",b:"{not an object}",c:"(x)"}]'
    obj = jslit.parse_literal(js)
    assert obj[0]["a"] == "[not an array]", obj
    assert obj[0]["b"] == "{not an object}", obj


def t_jslit_no_eval():
    """确认解析器不会执行代码：带函数调用的字面量必须报错，而不是被求值。"""
    js = '[{a:alert("pwned")}]'
    try:
        jslit.parse_literal(js)
    except Exception:  # noqa: BLE001
        return
    raise AssertionError("含函数调用的字面量本应解析失败，却被接受了（危险）")


def t_jslit_no_boundary_confusion():
    js = "xeA=1;eA=[{title:\"Week 1\"}];"
    got = jslit.extract_assignment(js, "eA")
    assert got == [{"title": "Week 1"}], got


def t_jslit_anchor():
    js = 'xxx=[{y:1}];eI=[{q:"Q1",a:"A1"},{q:"Q2",a:"A2"}];yyy=1;'
    got = jslit.extract_by_anchor(js, '{q:"')
    assert len(got) == 2 and got[0]["q"] == "Q1", got


check("基本字面量 + undefined→null + 尾随逗号", t_jslit_basic)
check("单双引号与转义", t_jslit_strings)
check("字符串里的括号不干扰平衡匹配", t_jslit_brackets_in_strings)
check("不执行代码（含函数调用必须报错）", t_jslit_no_eval)
check("词边界匹配不误取 xeA 为 eA", t_jslit_no_boundary_confusion)
check("按内容锚点定位数组", t_jslit_anchor)

# ---------------------------------------------------------------- 2. HTML → Markdown
section("2. src/htmlmd.py —— HTML 抽取")

import htmlmd  # noqa: E402


def t_html_basic():
    html = """<html><body><nav>菜单 菜单</nav>
    <article><h1>标题</h1><p>第一段正文，足够长以便通过长度判断。</p>
    <h2>小节</h2><ul><li>甲</li><li>乙</li></ul>
    <pre><code class="language-python">print(1)</code></pre>
    <table><tr><th>H</th></tr><tr><td>V</td></tr></table></article>
    <footer>页脚</footer></body></html>"""
    blocks = htmlmd.html_to_blocks(html)
    types = [b["type"] for b in blocks]
    assert "heading" in types and "para" in types, types
    assert "list" in types and "code" in types, types
    text = htmlmd.blocks_to_markdown(blocks)
    assert "菜单" not in text, "导航区应被剪掉"
    assert "页脚" not in text, "页脚应被剪掉"
    assert "print(1)" in text, "代码应保留"


def t_html_no_css_js_soup():
    """script/style 的内容绝不能出现在结果里（本项目真实踩过的坑）。"""
    html = """<html><head><style>.a{color:red}</style>
    <script>var x=[1,2,3];function f(){return 1}</script></head>
    <body><article><p>这是正文，长度足够通过判据所以不会被丢弃掉。</p></article></body></html>"""
    text = htmlmd.blocks_to_markdown(htmlmd.html_to_blocks(html))
    assert "color:red" not in text, text[:200]
    assert "function f" not in text, text[:200]


def t_html_prune_safety_valve():
    """命中样板特征但含大段正文的容器不能被剪掉（GitHub Blog 19700→86 的坑）。

    安全阀是"文字量阈值"，所以测试用的正文必须真的超过阈值（1200 字符）。
    """
    body = "".join(
        f"<p>正文段落 {i}，这里写得足够长，以便被识别为真正的文章正文而不是导航样板，"
        f"长度必须超过安全阀的阈值才能真正验证到这条防线。</p>"
        for i in range(30))
    html = f'<html><body><div class="post-header-body">{body}</div></body></html>'
    text = htmlmd.blocks_to_markdown(htmlmd.html_to_blocks(html))
    assert len(text) > 1000, f"正文被误删，只剩 {len(text)} 字符"


def t_html_prune_removes_short_nav():
    """反过来：短的导航块（含样板特征）必须被剪掉。"""
    links = "".join(f'<a href="/p{i}">栏目{i}</a>' for i in range(12))
    html = (f'<html><body><div class="site-nav">{links}</div>'
            f'<article><p>这是唯一的正文段落，长度足够通过判据所以不会被丢掉。</p>'
            f'</article></body></html>')
    text = htmlmd.blocks_to_markdown(htmlmd.html_to_blocks(html))
    assert "栏目" not in text, "导航菜单未被剪掉"


def t_html_surrogate_sanitised():
    """网页里的孤立代理字符不能让写盘崩溃。"""
    html = "<html><body><p>正文&#xD83D;内容足够长以便通过长度判据不会丢。</p></body></html>"
    text = htmlmd.blocks_to_markdown(htmlmd.html_to_blocks(html))
    text.encode("utf-8")  # 不抛 UnicodeEncodeError 即通过


def t_html_div_layout():
    """div 版式（无 p 标签）也要能抽出来。"""
    inner = "".join(
        f'<div>这是第 {i} 段正文，写长一点以便被识别为段落内容而不是被长度判据丢掉，'
        f'再补一些字确保超过最小长度阈值。</div>'
        for i in range(8))
    html = f"<html><body><div class='wrapper'>{inner}</div></body></html>"
    text = htmlmd.page_text(html)
    assert len(text) > 300, f"div 版式抽取失败，只得到 {len(text)} 字符"


check("基本块切分 + 剪掉导航页脚 + 保留代码", t_html_basic)
check("不产出 CSS/JS 汤", t_html_no_css_js_soup)
check("样板剪枝的安全阀（不误删正文）", t_html_prune_safety_valve)
check("样板剪枝确实剪掉短导航块", t_html_prune_removes_short_nav)
check("孤立代理字符被净化", t_html_surrogate_sanitised)
check("div 版式兜底抽取", t_html_div_layout)

# ---------------------------------------------------------------- 3. PDF 抽取
section("3. src/pdftext.py —— 自研 PDF 文本提取")

import pdftext  # noqa: E402


def t_pdf_lexer():
    lx = pdftext.Lexer(rb'(a \(nested\) b) /Name 42 <414243> [1 2]')
    assert lx.read_token() == b"a (nested) b", lx.read_token()
    assert lx.read_token() == b"/Name"
    assert lx.read_token() == b"42"
    assert lx.read_token() == b"ABC", "十六进制字符串应被解码"
    assert lx.read_token() == b"["


def t_pdf_tounicode():
    cmap = (b"beginbfchar\n<0041> <4E2D>\n<0042> <6587>\nendbfchar\n"
            b"beginbfrange\n<0050> <0052> <0041>\nendbfrange\n")
    table = pdftext.FontMap._parse_tounicode(cmap)
    assert table[0x41] == "中" and table[0x42] == "文", table
    assert table[0x50] == "A" and table[0x52] == "C", table


def t_pdf_winansi():
    info = {"table": dict(pdftext.WIN_ANSI_HIGH), "two_byte": False}
    got = pdftext.FontMap.decode(b"\x93hi\x94", info)
    assert got == "\u201chi\u201d", repr(got)


def t_pdf_real_files_if_present():
    """若本地已抓取素材，对真实 PDF 做一次抽取验证（不存在则跳过）。"""
    pdfs = glob.glob(os.path.join(ROOT, "sources", "docs", "slides", "*.pdf"))
    if not pdfs:
        return
    st = pdftext.pdf_stats(pdfs[0])
    assert st["pages"] > 0, f"{pdfs[0]} 解析出 0 页"
    assert st["chars"] > 200, f"{pdfs[0]} 只抽出 {st['chars']} 字符"


check("PDF 词法分析（转义/十六进制串）", t_pdf_lexer)
check("ToUnicode CMap 解析（bfchar + bfrange）", t_pdf_tounicode)
check("WinAnsi 高位字符解码", t_pdf_winansi)
check("真实讲义 PDF 抽取（有素材时）", t_pdf_real_files_if_present)

# ---------------------------------------------------------------- 4. Markdown 块
section("4. src/mdblocks.py —— Markdown 结构化块")

import mdblocks  # noqa: E402


def t_md_blocks():
    md = ("# T\n\n段落一。\n\n## 小节\n\n- a\n- b\n\n1. x\n\n```py\ncode\n```\n\n"
          "| A | B |\n| --- | --- |\n| 1 | 2 |\n\n> 引用\n\n---\n")
    blocks = mdblocks.parse_markdown(md)
    types = [b["type"] for b in blocks]
    for want in ("heading", "para", "list", "code", "table", "quote", "rule"):
        assert want in types, (want, types)


def t_md_fullwidth_ordered_list():
    """中文全角 `）` 也要被认成有序列表（否则中英结构会假性不一致）。"""
    blocks = mdblocks.parse_markdown("2） （可选）安装提交前钩子\n")
    assert blocks and blocks[0]["type"] == "list", blocks


def t_md_links_and_plain():
    text = "见 [文档](https://example.com/a?b=1) 与 `code` 与 **粗**。"
    assert mdblocks.links(text) == ["https://example.com/a?b=1"]
    plain = mdblocks.plain(text)
    assert "https://" not in plain and "code" in plain, plain


def t_md_iter_segments():
    blocks = mdblocks.parse_markdown("- a\n- b\n\n段落\n")
    segs = list(mdblocks.iter_segments(blocks))
    assert len(segs) == 3, segs
    assert all("id" in s for s in segs)


check("块类型识别（标题/段/列表/代码/表格/引用/分隔线）", t_md_blocks)
check("中文全角 ） 的有序列表", t_md_fullwidth_ordered_list)
check("链接提取与纯文本剥离", t_md_links_and_plain)
check("切段与稳定 ID", t_md_iter_segments)

# ---------------------------------------------------------------- 5. 术语表
section("5. glossary/glossary.json —— 术语表健康度")

GLOSSARY = os.path.join(ROOT, "glossary", "glossary.json")


def t_glossary_valid():
    data = json.load(open(GLOSSARY, encoding="utf-8"))
    terms = data["terms"]
    assert len(terms) >= 50, f"术语表只有 {len(terms)} 条，低于验收线 50"


def t_glossary_no_dup():
    terms = json.load(open(GLOSSARY, encoding="utf-8"))["terms"]
    seen = set()
    for t in terms:
        assert t["en"] not in seen, f"重复词条 {t['en']}"
        seen.add(t["en"])


def t_glossary_no_conflict():
    """定译之间不打架；禁用写法不与别人的定译冲突（否则照规范译也会违规）。"""
    terms = json.load(open(GLOSSARY, encoding="utf-8"))["terms"]
    owner = {}
    for t in terms:
        if t.get("keep") or t.get("alias_of"):
            continue
        base = re.sub(r"（.*?）", "", t.get("zh", "")).strip()
        if base:
            owner.setdefault(base, t["en"])
    for t in terms:
        for bad in t.get("forbid", []):
            if bad in owner and owner[bad] != t["en"]:
                raise AssertionError(f"「{bad}」是 {owner[bad]} 的定译，却被 {t['en']} 列为禁用")


def t_glossary_generated_md():
    p = os.path.join(ROOT, "glossary", "术语表.md")
    assert os.path.exists(p), "缺少生成的人读版术语表，跑 src/s08_glossary.py"
    assert len(open(p, encoding="utf-8").read()) > 1000


check("术语表条数 ≥50", t_glossary_valid)
check("无重复词条", t_glossary_no_dup)
check("无定译冲突 / 禁用写法与定译打架", t_glossary_no_conflict)
check("人读版术语表已生成", t_glossary_generated_md)

# ---------------------------------------------------------------- 6. 语料
section("6. corpus/ —— 语料完整性")

CORPUS_EN = os.path.join(ROOT, "corpus", "en")


def t_corpus_index():
    idx = json.load(open(os.path.join(ROOT, "corpus", "index.json"), encoding="utf-8"))
    assert idx["count"] > 0, "语料为空"
    files = glob.glob(os.path.join(CORPUS_EN, "*.md"))
    assert len(files) >= idx["count"] - 5, f"索引 {idx['count']} 份但实际只有 {len(files)} 个文件"


def t_corpus_has_h1():
    """绝大多数语料都应带标题。

    注意两点，避免把测试写成脆的：
    · `__pN` 是超长素材的拆分部分，标题只在第 1 部分里（这是拆分的设计，不是缺陷）；
    · 少数从 Google Docs / PDF 抽出的文档自带多个 H1（原文就是这样）。
    所以判据是"至少 90% 的**完整文档**带 H1"，而不是"恰好一个"。
    """
    total, with_h1 = 0, 0
    for p in glob.glob(os.path.join(CORPUS_EN, "*.md")):
        name = os.path.basename(p)
        if "__p" in name and name.endswith(".md"):
            stem = name[:-3]
            if re.search(r"__p\d+$", stem):
                continue
        total += 1
        md = open(p, encoding="utf-8").read()
        if any(ln.startswith("# ") for ln in md.split("\n")):
            with_h1 += 1
    assert total > 0, "语料目录为空"
    ratio = with_h1 / total
    assert ratio >= 0.90, f"只有 {ratio:.0%}（{with_h1}/{total}）的完整文档带 H1，偏低"


def t_corpus_all_parse():
    import mdblocks as mb

    empty = []
    for p in glob.glob(os.path.join(CORPUS_EN, "*.md")):
        blocks = mb.parse_markdown(open(p, encoding="utf-8").read())
        if not blocks:
            empty.append(os.path.basename(p))
    assert not empty, f"以下语料解析出 0 个块：{empty[:5]}"


check("语料索引与文件数一致", t_corpus_index)
check("≥90% 的完整文档带 H1 标题", t_corpus_has_h1)
check("每份语料至少解析出 1 个块", t_corpus_all_parse)

# ---------------------------------------------------------------- 7. 译文结构对齐
section("7. corpus/zh/ —— 译文结构对齐")

import s10_qa  # noqa: E402

CORPUS_ZH = os.path.join(ROOT, "corpus", "zh")


def t_translation_structure():
    terms = s10_qa.load_glossary()
    zh_files = glob.glob(os.path.join(CORPUS_ZH, "*.md"))
    if not zh_files:
        return  # 尚未开始翻译时跳过
    bad = []
    for p in zh_files:
        slug = os.path.splitext(os.path.basename(p))[0]
        en = os.path.join(CORPUS_EN, slug + ".md")
        if not os.path.exists(en):
            continue
        res = s10_qa.check_pair(open(en, encoding="utf-8").read(),
                                open(p, encoding="utf-8").read(), terms)
        st = res["stats"]
        if st["code_changed"] or st["link_lost"] or st["empty"]:
            bad.append((slug, st["code_changed"], st["link_lost"], st["empty"]))
    assert not bad, f"译文存在代码改动/链接丢失/空译：{bad[:5]}"


check("已译文件无代码改动 / 链接丢失 / 空译", t_translation_structure)


# ------------------------------------------------------------ 7b. 质检器自测
section("7b. src/s10_qa.py —— 质检器本身有效吗（不能是空转的）")

import mdblocks as _mb  # noqa: E402


def _qa(zh: str, en: str):
    return s10_qa.check_pair(en, zh, s10_qa.load_glossary())["stats"]


def t_qa_catches_missing_block():
    """删掉一段译文，必须报结构不一致或截断。"""
    en = "# T\n\n第一段原文内容。\n\n第二段原文内容。\n\n第三段原文内容。\n"
    zh = "# T\n\n第一段译文内容。\n\n第三段译文内容。\n"
    st = _qa(zh, en)
    assert st["structure"] or st["truncated"], f"漏掉一整段却没报错：{st}"


def t_qa_catches_changed_code():
    """改动代码块，必须报 code_changed。"""
    en = "# T\n\n```py\nx = 1\n```\n"
    zh = "# T\n\n```py\nx = 2\n```\n"
    assert _qa(zh, en)["code_changed"] == 1, "代码被改动却没报错"


def t_qa_catches_lost_link():
    """丢掉链接，必须报 link_lost。"""
    en = "# T\n\n见 [文档](https://example.com/a)。\n"
    zh = "# T\n\n见 文档。\n"
    assert _qa(zh, en)["link_lost"] >= 1, "链接丢失却没报错"


def t_qa_catches_empty():
    """空译文必须报 empty。"""
    en = "# T\n\n" + "这是一段足够长的原文，用来触发长度判据。" * 3 + "\n"
    zh = "# T\n\n\n"
    assert _qa(zh, en)["empty"] >= 1 or _qa(zh, en)["truncated"] >= 1, "空译却没报错"


def t_qa_catches_term_violation():
    """使用禁用写法，必须被术语检查抓到。"""
    en = "# T\n\nThe coding agent writes code.\n"
    zh = "# T\n\n这个编程代理会写代码。\n"       # 编程代理 是 coding agent 的禁用写法
    assert _qa(zh, en)["term_violations"] >= 1, "禁用写法却没被术语检查抓到"


def t_qa_catches_spacing():
    """中英文之间漏空格，必须被排版检查抓到。"""
    en = "# T\n\nUse Claude Code here.\n"
    zh = "# T\n\n在这里使用Claude Code。\n"
    assert _qa(zh, en)["spacing"] >= 1, "漏空格却没报错"


def t_qa_allows_kept_english():
    """原文里本来就有的英文引用，不该被当成漏译。"""
    en = '# T\n\n一段正文。\n\n“Now critique your answer. Was it correct?”\n'
    zh = '# T\n\n一段正文。\n\n“Now critique your answer. Was it correct?”\n'
    st = _qa(zh, en)
    assert st["untranslated"] == 0, f"原文自带的英文引用被误判为漏译：{st}"


def t_qa_clean_pair_passes():
    """一份规规矩矩的译文必须零问题（防止质检器过度敏感）。"""
    en = "# 标题\n\n第一段正文，长度够长以便通过判据。\n\n- 甲\n- 乙\n\n```py\nx = 1\n```\n"
    zh = "# 标题\n\n第一段译文，长度也够长以便通过判据。\n\n- 甲项\n- 乙项\n\n```py\nx = 1\n```\n"
    st = _qa(zh, en)
    assert st["issues"] == 0, f"正常译文被误报：{st}"


check("删掉一段译文会被抓到", t_qa_catches_missing_block)
check("改动代码块会被抓到", t_qa_catches_changed_code)
check("链接丢失会被抓到", t_qa_catches_lost_link)
check("空译会被抓到", t_qa_catches_empty)
check("禁用写法会被术语检查抓到", t_qa_catches_term_violation)
check("中英文漏空格会被抓到", t_qa_catches_spacing)
check("原文自带的英文引用不被误判", t_qa_allows_kept_english)
check("正常译文零误报", t_qa_clean_pair_passes)

# ---------------------------------------------------------------- 8. 成品与文档站
section("8. 交付物存在性")


def t_deliverables():
    for f in ("README.md", "AI日志.md", "AAR.md", "拿来说明.md",
              "TRANSLATION_SPEC.md", "LICENSE", "LICENSE-CONTENT.md"):
        assert os.path.exists(os.path.join(ROOT, f)), f"缺少交付物 {f}"


def t_reports():
    for f in ("_inventory.md", "_qa_report.md"):
        assert os.path.exists(os.path.join(ROOT, "reports", f)), f"缺少报告 reports/{f}"


def t_scripts():
    for f in ("scripts/reproduce.ps1", "scripts/reproduce.sh"):
        assert os.path.exists(os.path.join(ROOT, f)), f"缺少复现脚本 {f}"


def t_site_if_built():
    idx = os.path.join(ROOT, "docs", "index.html")
    if not os.path.isdir(os.path.join(ROOT, "docs")):
        return  # 尚未建站时跳过
    assert os.path.exists(idx), "docs/ 存在但缺少 index.html"
    html = open(idx, encoding="utf-8").read()
    assert "CS146S" in html, "文档站首页内容异常"
    assert "http://" not in html.replace("http://www.w3.org", ""), \
        "文档站不应引用外部 http 资源（必须离线可用）"


def t_translated_if_assembled():
    d = os.path.join(ROOT, "translated")
    if not os.path.isdir(d):
        return
    assert glob.glob(os.path.join(d, "*.zh.md")), "translated/ 里没有纯中文版"
    assert glob.glob(os.path.join(d, "*.bilingual.md")), "translated/ 里没有中英对照版"


check("四份交付物 + 规范 + License 齐备", t_deliverables)
check("清点与质检报告存在", t_reports)
check("一键复现脚本存在", t_scripts)
check("文档站可离线打开", t_site_if_built)
check("成品含纯中文版与中英对照版", t_translated_if_assembled)

# ---------------------------------------------------------------- 汇总
print("\n" + "=" * 62)
print(f"  冒烟测试：通过 {len(PASS)} 项 / 失败 {len(FAIL)} 项")
print("=" * 62)
if FAIL:
    for name, why in FAIL:
        print(f"  ❌ {name}\n      {why}")
    sys.exit(1)
print("  ✅ 全部通过")
sys.exit(0)
