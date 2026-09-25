#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S11 · 构建离线双语文档站。

目标：产出一个**双击 index.html 就能看、断网也能看、不需要任何服务器**的中英对照站。
挑战里写"以可复用的方式发布成果（GitHub 仓库 / 文档站），让下一批同学零成本复用"——
所以这里刻意不用 MkDocs / Docusaurus：那些要装依赖、要跑构建服务，
而"零成本"对下一位同学来说就是"打开就能读"。

实现要点
--------
- 每篇文档渲染为**逐块对照**（中文块 + 对应英文块），顶栏一键切换「中文 / 中英对照」；
- 全文检索索引以 `assets/search-index.js` 形式内联（`window.SEARCH_INDEX = [...]`），
  这样在 `file://` 协议下也能检索 —— 用 fetch 读 JSON 会被浏览器 CORS 拦掉；
- 不引用任何 CDN，样式与脚本全部内联，保证离线可用。

产出：site/index.html ｜ site/doc/<slug>.html ｜ site/glossary.html
      site/assets/style.css ｜ site/assets/app.js ｜ site/assets/search-index.js
"""

from __future__ import annotations

import html as htmllib
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402
from mdblocks import block_plain, block_text, parse_markdown  # noqa: E402

CORPUS_EN = os.path.join(C.ROOT, "corpus", "en")
CORPUS_ZH = os.path.join(C.ROOT, "corpus", "zh")
SITE = os.path.join(C.ROOT, "site")
GROUP_LABEL = {
    "site": "课程官网",
    "media": "课程讲义",
    "repo": "作业仓库",
    "reading": "指定阅读",
    "other": "其他",
}
GROUP_ORDER = ["site", "media", "repo", "reading", "other"]


# ---------------------------------------------------------------- 行内 Markdown
def inline(text: str) -> str:
    out = htmllib.escape(text, quote=False)
    out = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)",
                 lambda m: f'<img src="{htmllib.escape(m.group(2))}" alt="{htmllib.escape(m.group(1))}">',
                 out)
    out = re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)",
                 lambda m: f'<a href="{htmllib.escape(m.group(2))}" target="_blank" rel="noopener">{m.group(1)}</a>',
                 out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    return out


def render_block(b: dict, lang: str) -> str:
    t = b["type"]
    if t == "heading":
        lv = min(max(b["level"], 1), 6)
        return f"<h{lv}>{inline(b['text'])}</h{lv}>"
    if t == "para":
        return f"<p>{inline(b['text'])}</p>"
    if t == "list":
        tag = "ol" if b.get("ordered") else "ul"
        items = "".join(f"<li>{inline(i)}</li>" for i in b["items"])
        return f"<{tag}>{items}</{tag}>"
    if t == "code":
        cls = f' class="language-{b["lang"]}"' if b.get("lang") else ""
        return f"<pre><code{cls}>{htmllib.escape(b['text'])}</code></pre>"
    if t == "quote":
        return "<blockquote>" + inline(b["text"]).replace("\n", "<br>") + "</blockquote>"
    if t == "table":
        head = "".join(f"<th>{inline(c)}</th>" for c in b["header"])
        rows = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                       for r in b["rows"])
        return f"<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>"
    if t == "rule":
        return "<hr>"
    return ""


def render_pairs(en_md: str, zh_md: str | None) -> tuple[str, int]:
    en_blocks = parse_markdown(en_md)
    zh_blocks = parse_markdown(zh_md) if zh_md else []
    out: list[str] = []
    for i, eb in enumerate(en_blocks):
        zb = zh_blocks[i] if i < len(zh_blocks) else None
        same = zb is not None and zb["type"] == eb["type"]
        if eb["type"] == "code":
            out.append(f'<div class="pair code">{render_block(eb, "en")}</div>')
            continue
        zh_html = render_block(zb, "zh") if same else ""
        en_html = render_block(eb, "en")
        if zh_html:
            out.append(f'<div class="pair"><div class="zh">{zh_html}</div>'
                       f'<div class="en">{en_html}</div></div>')
        else:
            out.append(f'<div class="pair untranslated"><div class="en">{en_html}</div></div>')
    return "\n".join(out), len(en_blocks)


CSS = """
:root{--bg:#fbfaf7;--fg:#1f2328;--muted:#6b7280;--card:#fff;--line:#e5e7eb;
--accent:#0b6b3a;--accent-soft:#e8f3ec;--code-bg:#f4f5f7;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font-family:-apple-system,"Segoe UI","Microsoft YaHei",system-ui,sans-serif;
line-height:1.75;font-size:16px}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
header.top{position:sticky;top:0;z-index:10;background:rgba(251,250,247,.94);
border-bottom:1px solid var(--line);backdrop-filter:blur(6px)}
.top-inner{max-width:1180px;margin:0 auto;padding:10px 20px;display:flex;
gap:14px;align-items:center;flex-wrap:wrap}
.brand{font-weight:700;color:var(--accent)}
.top-inner .spacer{flex:1}
button,input[type=search],select{font:inherit;padding:6px 10px;border:1px solid var(--line);
border-radius:8px;background:var(--card);color:var(--fg)}
button{cursor:pointer}
button:hover{border-color:var(--accent);color:var(--accent)}
.layout{max-width:1180px;margin:0 auto;display:grid;grid-template-columns:280px 1fr;gap:28px;padding:22px 20px 80px}
nav.side{position:sticky;top:64px;align-self:start;max-height:calc(100vh - 90px);overflow:auto;
font-size:14px}
nav.side h4{margin:16px 0 6px;color:var(--muted);font-size:12px;letter-spacing:.06em;
text-transform:uppercase}
nav.side a{display:block;padding:3px 8px;border-radius:6px;color:var(--fg)}
nav.side a:hover{background:var(--accent-soft);text-decoration:none}
nav.side a.active{background:var(--accent-soft);color:var(--accent);font-weight:600}
main{min-width:0}
h1{font-size:1.75rem;line-height:1.3;margin:.2em 0 .6em}
h2{font-size:1.28rem;margin:1.6em 0 .5em;padding-top:.3em;border-top:1px solid var(--line)}
h3{font-size:1.08rem;margin:1.3em 0 .4em}
.pair{display:grid;grid-template-columns:1fr;gap:0;margin:0 0 .2em}
.pair .zh>*:first-child,.pair .en>*:first-child{margin-top:0}
.pair .en{display:none;color:#374151}
body.mode-bi .pair{grid-template-columns:1fr 1fr;gap:20px;border-bottom:1px dashed var(--line);
padding-bottom:.5em}
body.mode-bi .pair .en{display:block;font-size:.94em}
body.mode-bi .pair.code{grid-template-columns:1fr}
body.mode-bi .pair.untranslated{grid-template-columns:1fr}
pre{background:var(--code-bg);padding:12px 14px;border-radius:8px;overflow:auto;
border:1px solid var(--line)}
code{background:var(--code-bg);padding:.1em .35em;border-radius:4px;
font-family:"Cascadia Mono",Consolas,"Courier New",monospace;font-size:.92em}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:.8em 0;font-size:.95em}
th,td{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}
th{background:var(--accent-soft)}
blockquote{margin:.8em 0;padding:.2em 0 .2em 14px;border-left:3px solid var(--accent);
color:#374151}
img{max-width:100%}
.meta{color:var(--muted);font-size:13px;margin-bottom:18px}
.badge{display:inline-block;background:var(--accent-soft);color:var(--accent);
border-radius:6px;padding:1px 8px;font-size:12px;margin-right:6px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.card h3{margin:0 0 6px;font-size:1rem}
.card p{margin:0;color:var(--muted);font-size:13px}
.kpi{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:14px;margin:20px 0}
.kpi div{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 16px}
.kpi b{display:block;font-size:1.5rem;color:var(--accent)}
.kpi span{color:var(--muted);font-size:13px}
#results a{display:block;padding:8px 0;border-bottom:1px solid var(--line)}
.miss{color:#b45309}
@media (max-width:900px){.layout{grid-template-columns:1fr}nav.side{position:static;max-height:none}
body.mode-bi .pair{grid-template-columns:1fr}}
"""

APP_JS = """
(function(){
  var body=document.body;
  var saved=localStorage.getItem('cs146s-mode')||'zh';
  if(saved==='bi') body.classList.add('mode-bi');
  var btn=document.getElementById('mode-btn');
  function label(){btn.textContent = body.classList.contains('mode-bi')?'切换：仅中文':'切换：中英对照';}
  label();
  if(btn) btn.addEventListener('click',function(){
    body.classList.toggle('mode-bi');
    localStorage.setItem('cs146s-mode', body.classList.contains('mode-bi')?'bi':'zh');
    label();
  });
  var box=document.getElementById('q');
  var out=document.getElementById('results');
  var idx=(window.SEARCH_INDEX||[]);
  function esc(s){return s.replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  function run(){
    var q=box.value.trim().toLowerCase();
    if(!q){out.innerHTML='';return;}
    var hits=[];
    for(var i=0;i<idx.length;i++){
      var it=idx[i];
      var pos=it.text.toLowerCase().indexOf(q);
      if(pos<0) continue;
      hits.push({it:it,pos:pos});
      if(hits.length>=60) break;
    }
    if(!hits.length){out.innerHTML='<p class="meta">没有匹配结果。</p>';return;}
    var html='<p class="meta">命中 '+hits.length+' 处</p>';
    for(var j=0;j<hits.length;j++){
      var h=hits[j], t=h.it.text, p=h.pos;
      var s=Math.max(0,p-60), e=Math.min(t.length,p+q.length+90);
      html+='<a href="'+h.it.url+'"><span class="badge">'+esc(h.it.group)+'</span>'
        +esc(h.it.title)+'<br><span class="meta">…'+esc(t.slice(s,e))+'…</span></a>';
    }
    out.innerHTML=html;
  }
  if(box){box.addEventListener('input',run);}
})();
"""

NAV_JS = """
(function(){
  var links=document.querySelectorAll('nav.side a');
  for(var i=0;i<links.length;i++){
    if(links[i].pathname===location.pathname) links[i].classList.add('active');
  }
})();
"""


def write_page(path: str, title: str, nav: str, body: str, depth: int,
               search_ui: bool = True) -> None:
    prefix = "../" * depth
    head = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{htmllib.escape(title)}</title>
<link rel="stylesheet" href="{prefix}assets/style.css">
</head><body>
<header class="top"><div class="top-inner">
  <span class="brand">CS146S 中文资料包</span>
  <span class="badge">Stanford The Modern Software Developer</span>
  <span class="spacer"></span>
  <input type="search" id="q" placeholder="全文检索（中/英）" style="min-width:220px">
  <button id="mode-btn" type="button">切换</button>
  <a href="{prefix}index.html">目录</a>
</div></header>
<div class="layout">
<nav class="side">{nav}</nav>
<main id="results-main">
{('<div id="results"></div>' if search_ui else '')}
{body}
</main>
</div>
<script src="{prefix}assets/search-index.js"></script>
<script src="{prefix}assets/app.js"></script>
</body></html>"""
    C.write_text(path, head)


def build_nav(items: list[dict], prefix: str, current: str = "") -> str:
    by_group: dict[str, list[dict]] = {}
    for it in items:
        by_group.setdefault(it.get("group", "other"), []).append(it)
    out = ['<h4>导航</h4>',
           f'<a href="{prefix}index.html">首页 / 项目说明</a>',
           f'<a href="{prefix}glossary.html">术语表</a>']
    for g in GROUP_ORDER:
        xs = by_group.get(g)
        if not xs:
            continue
        out.append(f"<h4>{GROUP_LABEL.get(g, g)}（{len(xs)}）</h4>")
        for it in sorted(xs, key=lambda x: x.get("sortkey", x["slug"])):
            title = it["title"][:38]
            cls = ' class="active"' if it["slug"] == current else ""
            out.append(f'<a href="{prefix}doc/{it["slug"]}.html"{cls}>{htmllib.escape(title)}</a>')
    return "\n".join(out)


def main() -> int:
    index = C.read_json(os.path.join(C.ROOT, "corpus", "index.json"), {}) or {}
    items = index.get("items", [])
    if not items:
        raise SystemExit("缺少 corpus/index.json")

    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    C.ensure_dirs(os.path.join(SITE, "doc"), os.path.join(SITE, "assets"))
    C.write_text(os.path.join(SITE, "assets", "style.css"), CSS)
    C.write_text(os.path.join(SITE, "assets", "app.js"), APP_JS + NAV_JS)

    parent_of = {i["slug"]: i.get("parent") for i in items if i.get("parent")}
    plan = C.read_json(os.path.join(C.WORK, "translation_plan.json"), {}) or {}
    order = {}
    for b in plan.get("plan", []):
        for n, f in enumerate(b["files"]):
            order.setdefault(f["slug"], (b["id"], n))
    for it in items:
        p = it.get("parent") or it["slug"]
        it["sortkey"] = (order.get(p, ("zz", 0))[0], order.get(p, ("zz", 0))[1],
                         it.get("part", 0), it["slug"])

    nav_cache: dict[str, str] = {}
    search: list[dict] = []
    translated = 0

    for it in items:
        slug = it["slug"]
        en_md = C.read_any_text(os.path.join(CORPUS_EN, slug + ".md"))
        zh_path = os.path.join(CORPUS_ZH, slug + ".md")
        zh_md = C.read_any_text(zh_path) if os.path.exists(zh_path) else None
        if zh_md:
            translated += 1
        depth = 1  # doc 页在 site/doc/ 下
        nav = nav_cache.get("nav")
        if nav is None:
            nav = build_nav(items, "../")
            nav_cache["nav"] = nav
        pairs, nblocks = render_pairs(en_md, zh_md)
        meta = (f'<div class="meta"><span class="badge">{GROUP_LABEL.get(it.get("group"), "")}</span>'
                f'{htmllib.escape(it.get("term") or "")} ｜ 原文 {it["chars"]:,} 字符 ｜ '
                f'{nblocks} 个内容块 ｜ '
                + (f'<a href="{htmllib.escape(it.get("source_url") or "#")}" target="_blank" rel="noopener">查看一手来源</a>'
                   if it.get("source_url") else "本地素材")
                + ("（英译中：已译）" if zh_md else ' <span class="miss">（尚未翻译，仅显示英文）</span>')
                + "</div>")
        body = f'<h1>{htmllib.escape(it["title"])}</h1>{meta}{pairs}'
        write_page(os.path.join(SITE, "doc", slug + ".html"), it["title"], nav, body, depth)

        text = " ".join([it["title"], block_plain({"type": "para", "text": ""}) or ""])
        chunks = [it["title"]]
        for b in parse_markdown(en_md)[:400]:
            txt = block_text(b)
            if txt:
                chunks.append(txt[:400])
        if zh_md:
            for b in parse_markdown(zh_md)[:400]:
                txt = block_text(b)
                if txt:
                    chunks.append(txt[:400])
        search.append({
            "title": it["title"], "url": f"doc/{slug}.html",
            "group": GROUP_LABEL.get(it.get("group"), ""),
            "text": re.sub(r"\s+", " ", " ".join(chunks))[:12000],
        })

    C.write_text(os.path.join(SITE, "assets", "search-index.js"),
                 "window.SEARCH_INDEX=" + json.dumps(search, ensure_ascii=False) + ";")

    # ---------- 术语表页 ----------
    terms = (C.read_json(os.path.join(C.GLOSSARY_DIR, "glossary.json"), {}) or {}).get("terms", [])
    rows = "".join(
        f"<tr><td><code>{htmllib.escape(t['en'])}</code></td><td>{htmllib.escape(t['zh'])}</td>"
        f"<td>{htmllib.escape('、'.join(t.get('forbid', [])) or '—')}</td>"
        f"<td>{htmllib.escape(t.get('note') or '')}</td></tr>"
        for t in sorted(terms, key=lambda x: x["en"].lower()))
    gnav = nav_cache.get("nav") or build_nav(items, "")
    gloss_body = (f"<h1>术语表</h1><div class='meta'>共 {len(terms)} 条，"
                  f"{sum(1 for t in terms if t.get('keep'))} 条保留英文，"
                  f"{sum(len(t.get('forbid', [])) for t in terms)} 条声明禁用写法。"
                  f"本表是全项目译名的唯一事实来源。</div>"
                  "<table><thead><tr><th>英文</th><th>中文定译</th><th>禁用写法</th>"
                  f"<th>说明</th></tr></thead><tbody>{rows}</tbody></table>")
    write_page(os.path.join(SITE, "glossary.html"), "术语表", gnav, gloss_body, 0)

    # ---------- 首页 ----------
    inv = C.read_json(os.path.join(C.REPORTS, "_inventory.json"), {}) or {}
    qa = C.read_json(os.path.join(C.REPORTS, "_qa.json"), {}) or {}
    agg = qa.get("aggregate", {})
    seg = C.read_json(os.path.join(C.WORK, "segments_index.json"), {}) or {}
    missing = inv.get("missing", [])

    def card(it):
        return (f'<a class="card" href="doc/{it["slug"]}.html"><h3>{htmllib.escape(it["title"][:60])}</h3>'
                f'<p>{GROUP_LABEL.get(it.get("group"), "")} · {it["chars"]:,} 字符</p></a>')

    top_site = [i for i in items if i.get("group") == "site"]
    html_body = f"""<h1>CS146S 中文课程资料包</h1>
<div class="meta">Stanford《The Modern Software Developer》(CS146S) 公开课程资料的中文译本
 ｜ 离线可读 ｜ 中英逐块对照 ｜ 由可复现流水线产出</div>
<div class="kpi">
  <div><b>{index.get('count', 0)}</b><span>语料份数</span></div>
  <div><b>{index.get('total_chars', 0):,}</b><span>英文字符数</span></div>
  <div><b>{seg.get('translatable_segments', 0):,}</b><span>翻译片段数</span></div>
  <div><b>{len(terms)}</b><span>术语条目</span></div>
  <div><b>{agg.get('term_consistency', 0):.1%}</b><span>术语一致率</span></div>
  <div><b>{len(missing)}</b><span>未纳入素材</span></div>
</div>
<h2>怎么用这个站</h2>
<p>左侧目录选一篇；右上角「切换」按钮在中英对照与仅中文之间切换（选择会记住）。
顶部搜索框可同时检索中文译文与英文原文，完全离线运行，不依赖网络。</p>
<h2>课程官网（建议从这里开始）</h2>
<div class="cards">{''.join(card(i) for i in sorted(top_site, key=lambda x: x['slug']))}</div>
<h2>全部语料</h2>
<div class="cards">{''.join(card(i) for i in sorted(items, key=lambda x: x.get('sortkey', ())))}</div>
<h2>已知缺口（如实披露）</h2>
<p>以下 {len(missing)} 项素材未能纳入，原因逐条列出，未做任何美化：</p>
<table><thead><tr><th>分组</th><th>素材</th><th>状态</th><th>原因</th></tr></thead><tbody>
{''.join(f"<tr><td>{htmllib.escape(m['group'])}</td><td>{htmllib.escape((m['title'] or m['url'])[:70])}</td><td>{htmllib.escape(m['status'])}</td><td>{htmllib.escape((m['reason'] or '')[:120])}</td></tr>" for m in missing)}
</tbody></table>
"""
    write_page(os.path.join(SITE, "index.html"), "CS146S 中文课程资料包", gnav, html_body, 0)

    C.log(f"[建站] {len(items)} 篇文档（已译 {translated}）→ site/")
    C.log(f"       打开 {os.path.join(SITE, 'index.html')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
