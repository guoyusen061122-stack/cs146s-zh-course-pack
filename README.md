# CS146S 中文课程资料包 · C1 提交（郭裕森）

> **一句话定位**：把 Stanford CS146S《The Modern Software Developer》(Fall 2025 / Fall 2026)
> 的公开课程资料，用一条**可复跑的抓取与翻译流水线**译成中文，让不懂英文的同学零成本读懂这门课。
>
> 这不是"翻译练习"，是**一条信息获取与处理管线**：资料在哪 → 怎么批量抓 → 怎么控制质量 → 怎么让别人复用。

---

## ✅ 交付物对照表（挑战要求 ↔ 实际文件）

| 挑战要求的交付物 | 本仓库对应文件 | 说明 |
|---|---|---|
| `README.md` | [`README.md`](README.md) | 本文件 |
| AI 日志 | [`AI日志.md`](AI日志.md) | 关键决策节点 + AI/人分工 + **真实失败记录（未美化）** |
| AAR | [`AAR.md`](AAR.md) | 七维事后复盘 |
| 拿来说明 | [`拿来说明.md`](拿来说明.md) | 复用声明 + License 合规 + 换源复用指南 |
| —（过程证据） | [`方案草案.md`](方案草案.md) ｜ [`方案设计.md`](方案设计.md) ｜ [`G1背书.md`](G1背书.md) ｜ [`Portfolio条目.md`](Portfolio条目.md) ｜ [`CHANGELOG.md`](CHANGELOG.md) | G1 送审与过程留痕 |
| —（质量证据） | [`reports/_qa_report.md`](reports/_qa_report.md) ｜ [`reports/_qa_scan.md`](reports/_qa_scan.md) ｜ [`reports/_inventory.md`](reports/_inventory.md) | 覆盖率与质检的原始输出 |

---

## ✅ Demo / 演示入口

| 入口 | 位置 |
|---|---|
| **离线双语文档站（推荐从这里开始）** | 双击打开 [`site/index.html`](site/index.html) |
| 译文总目录 | [`translated/`](translated/) |
| 纯中文版 | [`translated/<slug>.zh.md`](translated/) |
| 中英对照版 | [`translated/<slug>.bilingual.md`](translated/) |
| 术语表（105 条中英对照 + 禁用写法） | [`glossary/术语表.md`](glossary/术语表.md) |
| 素材清点与覆盖率 | [`reports/_inventory.md`](reports/_inventory.md) |
| 质量抽检报告 | [`reports/_qa_report.md`](reports/_qa_report.md) ｜ [`reports/_qa_scan.md`](reports/_qa_scan.md) |
| 术语回正明细留痕 | [`reports/_term_fix_log.md`](reports/_term_fix_log.md) ｜ `src/logs/term_fix_*.md` |
| 三条红线自测 | [`docs/红线自测.md`](docs/红线自测.md) |

> **文档站怎么用**：左侧目录选一篇；右上角「切换」在中英逐块对照与仅中文之间切换（选择会记住）；
> 顶部搜索框可同时检索中文译文与英文原文。
>
> **离线可用到什么程度（如实说明）**：样式、脚本、检索索引**全部本地内联**，
> 经检查 **0 处外部资源依赖**，双击 `index.html` 即可阅读，不需要服务器、不需要网络。
> 唯一例外是**译文里保留了原文的配图链接（218 张）**，离线时这些图片不会显示 ——
> 这是刻意的取舍：把两百多张原文配图下载进仓库会带来不必要的版权再分发风险，
> 而正文文字完整可读。想看配图时点文末的「查看一手来源」即可。

> **译文格式说明**：`translated/*.bilingual.md` 是**逐块中英对照**（每段中文紧跟对应英文），
> 便于随时回看原文与核对忠实度；`translated/*.zh.md` 是**纯中文版**，给只想顺畅阅读的同学。
> 两种都给，是因为读者需求不同（这是审阅意见里明确指出该补的一项）。

---

## ✅ Quick Start（≤5 行，复制即跑）

```powershell
# Windows PowerShell（仓库自带，逐字复制即可）
cd cs146s-zh-course-pack
python src/s01_fetch_site.py        # ① 抓课程官网 → 结构化 syllabus/FAQ/评分
python src/s03_fetch_readings.py    # ② 批量抓 46 条阅读素材（多级兜底）
python src/s06_inventory.py         # ③ 清点素材、算覆盖率
```

一键版本：`scripts/reproduce.ps1`（Windows）／`scripts/reproduce.sh`（macOS / Linux），
详见 [§复现与可重复性](#-复现与可重复性)。

> **零第三方依赖**：整条流水线只用 Python 标准库。不需要 `pip install`，
> 不需要虚拟环境，clone 下来就能跑。原因见 [§为什么零依赖](#-为什么坚持零依赖)。

---

## ✅ 效果数据

### 覆盖度

| 口径 | 数值 | 说明 |
|---|---|---|
| 素材总盘子 | **102 项** | 官网板块 + 仓库文档 + 全部阅读链接 + 全部讲义/讲稿 + 全部视频 |
| 已纳入语料 | **89 项 / 776,025 字符** | 超长素材按块边界拆分为 110 个翻译单元 |
| 素材项覆盖率 | **89/102 = 87.3%** | 未纳入的 13 项逐条列在「已知缺口」节，不藏不糊 |
| **教学讲义覆盖** | **16/17 = 94.1%** | 15 份 Google Slides 讲义 + Drive 上的 2 份嘉宾讲稿 |
| 术语表 | **105 条**（20 条保留英文，80 条声明禁用写法） | 验收线 ≥50 |
| 翻译完成率 | **110/110 份 · 100%** | `src/s09_translate.py status` |
| 结构不一致 / 空译 / 漏译 / 截断 | **0 / 0 / 0 / 0** | `reports/_qa_report.md`，逐块机器核对 |
| 代码块被改动 / 链接丢失 | **0 / 0** | 代码逐字节比对；URL 集合比对 |
| 未译英文残留 / 中英文缺空格 | **0 / 0** | 含"原文自带英文引用"豁免，见质检口径说明 |
| 术语一致率 | **100.0%**（命中 4,490 / 违规 0） | 105 条术语表 + 95 条数据驱动回正规则 |
| 语料可复现性 | **109/109 份逐字节相同** | `python tests/test_reproducible.py` |

### 声称达到 Level：**L3（组合优化 / 工程化）**

| 级别 | 判据 | 本包实际 |
|---|---|---|
| L1 跑通基线 | 能跑通全流程、产出中文 | ✅ |
| L2 单点改进 | 有可量化改进 | ✅ 覆盖率、术语一致率、空译/漏译均以脚本给出前后对比 |
| **L3 组合优化 / 工程化** | 产出可被他人直接使用 | ✅ 数据驱动规则表 + 一键复现 + 幂等自检 + 离线文档站 |
| L4 SOTA | 全球可见信号 | ❌ 未追求 |

---

## ✅ 流水线（13 步 · 换源可复用）

```
                            ┌─ s01 官网抓取（Next.js 客户端渲染 → 从 JS 产物安全取结构化数据）
                            ├─ s02 作业仓库抓取（tar.gz + commit SHA 锚定）
 一手素材 ──────────────────┼─ s03 阅读素材抓取（6 级兜底链 + 「空壳体检」）
                            ├─ s04 讲义抓取（Google Slides/Drive 无鉴权导出 → PDF）
                            └─ s05 语料抽取（HTML/PDF/仓库文档 → 统一 Markdown）
                                     │
                              s05b 超长素材按块边界拆分
                                     │
                              s06 清点与覆盖率  ──→ reports/_inventory.md
                                     │
                              s07 切段（稳定 ID，中英可逐段对齐）
                                     │
                              s08 术语表校验与生成 ──→ glossary/术语表.md
                                     │
                              s09 翻译装配（plan / status / assemble / api）
                                     │
                              s10 质检 ──→ reports/_qa_report.md
                                     │
                              s10b 术语回正（数据驱动 + 留痕 + 幂等自检）
                                     │
                              s11 构建离线双语文档站 ──→ site/index.html
```

**设计要点（为什么这么做）**

1. **翻译是可插拔的一步**——切分、续跑、合并、校验、建站全部脚本化。换一门课只改 `corpus/en/`
   的来源，其余环节原样复用（见 `拿来说明.md` §3）。
2. **术语表是单一事实来源**——译名一旦冻结，`s10b_fix.py` 按规则表强制回正，且**留痕永不覆盖**。
3. **规则表是数据不是代码**——`glossary/glossary.json` 与 `config/term_fix_rules.json` 都是 JSON，
   换源只改表不改脚本。
4. **失败必须响**——抓取任何一段按设计失败都会触发下一条兜底路线；全部失败则记 `FAILED` 并进「已知缺口」，
   **绝不用空内容或伪造内容充数**。
5. **幂等自检**——术语回正把规则作用到自己的产出上，若仍在变化就直接报错退出
   （防"每跑一次叠加一层"，这个坑真踩过，见 AI 日志决策 6）。
6. **质检宁可少报也不能错报**——凡是无法可靠判定的检查项一律不做，理由写在
   `reports/_qa_report.md`（一条误报会让二十条真报一起被忽略，这个坑也真踩过）。

---

## ⚠️ 已知缺口（如实列出，共 5 类 / 13 项）

> 按挑战要求，"已知缺口"写清原因是加分项。以下每一条都可在
> [`reports/_inventory.md`](reports/_inventory.md) 第四节复核。

### 一、视频未纳入（4 个）

| 视频 | 讲者 |
|---|---|
| Deep Dive into LLMs like ChatGPT | Andrej Karpathy |
| AI Prompt Engineering: A Deep Dive | Anthropic |
| Lessons from millions of AI code reviews | Graphite |
| Building a Coding Agent | — |

**原因**：YouTube 的 `timedtext` 端点现在要求 `pot`（proof-of-origin）令牌，无令牌一律返回空体；
InnerTube 各客户端（ANDROID / IOS / WEB / TVHTML5）实测均被拒；
本机沙箱禁止 pip 写临时目录、PyInstaller 打包的 yt-dlp 独立程序也无法解包运行（两处均实测并留了报错原文）。
**下一步**：装好 yt-dlp 后按同一流程转写字幕即可接入，无需改管线。

### 二、需登录态、脚本不代抓（6 项）

| 素材 | 症状 |
|---|---|
| Google Slides：Gaspar Garcia（Vercel） | 导出端点返回 **HTTP 401**，讲者未开放公开查看 |
| Drive：Completed Exercise ×2、Completed code ×1 | 需登录态，`uc?export=download` 返回登录页 |
| Figma：Zach Lloyd（Warp） | 需登录态 |

### 三、内容型缺口（2 项）

| 素材 | 症状与原因 |
|---|---|
| `Good Context Good Code` | 原文站已下线，**改用 Wayback Machine 存档取回**（已在语料中） |
| `Peeking Under the Hood of Claude Code` | Medium 原文已 404，**改用 Wayback 存档取回**（已在语料中） |
| `Specs Are the New Source Code` | 原文已改为付费订阅，公开可得的只有开头预览；已取回该预览并标注 |

> 另有 3 个 GitHub 仓库主页与 1 条 X（Twitter）帖子：它们是**代码素材与社交发言**，不是可翻译的课程文本，
> 已登记但未纳入翻译，不是"抓不到"。

### 四、本站点专用的正文兜底（已解决，留档说明）

`www.promptingguide.ai` 与 `notion.warp.dev` 的正文完全由客户端渲染，HTML 里只有空壳。
前者改用同一作者在 GitHub 上维护的**官方 Markdown 原文**（见 `config/fallbacks.json`）；
后者无公开替代端点，记为空壳（其内容与 Week 5 讲义高度重叠，实际信息损失很小）。

### 五、`themodernsoftware.dev` 的正文不在 HTML 里

官网是纯客户端渲染的 Next.js 应用：syllabus / FAQ / 评分标准**都不在 HTML 中**，
而是内联在 `/_next/static/chunks/*.js` 的压缩产物里。
本项目用**手写词法扫描**把它们安全取出来（不 `eval`、不执行任何代码），
并从 bundle 中解析出「学期 → 变量」的映射再取值，因此站点重新构建后脚本仍能自证取对了学期。

---

## 📁 目录结构

```
cs146s-zh-course-pack/
├── README.md                  ← 本文件
├── AI日志.md                   ← 关键决策节点（含 18 条真实失败）
├── AAR.md                      ← 七维复盘
├── 拿来说明.md                  ← 复用声明 + License 合规 + 换源指南
├── 方案草案.md / 方案设计.md / G1背书.md / Portfolio条目.md / CHANGELOG.md
├── TRANSLATION_SPEC.md         ← 翻译硬性规范 R1–R10（所有译者必读）
├── LICENSE                     ← 流水线代码：MIT
├── LICENSE-CONTENT.md          ← 译文与原文素材：版权声明
├── config/
│   ├── fallbacks.json          ← 站点专用一手替代来源（逐条写理由）
│   └── term_fix_rules.json     ← 术语回正规则表（数据，不是代码）
├── glossary/
│   ├── glossary.json           ← 术语表单一事实来源（105 条）
│   └── 术语表.md                ← 生成的人读版
├── src/                        ← 13 步流水线 + 自研 PDF/HTML 抽取器
│   ├── common.py  jslit.py  htmlmd.py  pdftext.py  mdblocks.py
│   ├── s01…s11, s05b, s10b
│   ├── logo/                   （无）
│   └── logs/                   ← 术语回正逐条明细（永不覆盖）
├── scripts/reproduce.ps1 / .sh ← 一键复现
├── tests/test_smoke.py         ← 冒烟测试
├── docs/红线自测.md / 文件对照表.md / 群消息留痕.md
├── corpus/en/                  ← 冻结的英文语料（110 份）
├── corpus/zh/                  ← 中文译文
├── translated/                 ← 成品：纯中文版 + 中英对照版
├── reports/                    ← 清点、质检、术语回正报告
├── site/                       ← 离线双语文档站（双击 index.html）
└── sources/                    ← 原始素材（默认不入版本库，见 .gitignore 与 拿来说明.md）
```

---

## 🔁 复现与可重复性

```powershell
# Windows
powershell -ExecutionPolicy Bypass -File scripts/reproduce.ps1
# macOS / Linux
bash scripts/reproduce.sh
```

**环境要求**：Python **3.9+**（实测 3.14）。**零第三方依赖** —— 不需要 pip install。
**无需联网**（除 s01–s04 抓取步骤本身；抓取结果已带磁盘缓存，重跑直接命中缓存）。
**随机性**：全流程确定性，无随机采样，无需固定 seed。

> 完整复现（含重新抓取）约 6–10 分钟；仅重跑处理与质检（命中缓存）约 1 分钟。
> 译文本身是 LLM 产出并已固化在 `corpus/zh/`，因此复现不会"重新翻译"，而是复现
> **从原文到成品的全部自动化环节**：抽取、切分、校验、回正、建站、报告。

---

## 🧱 为什么坚持零依赖

本项目在准备阶段就撞上一堵墙：**本机沙箱禁止 pip 写临时目录**，任何第三方包都装不上
（`OSError: [Errno 13] Permission denied: ...pip-unpack-...whl.metadata`，报错原文见 AI 日志决策 1）。

于是只剩两条路：要么放弃 PDF 文本提取（丢掉 16 份讲义与官方 PDF，覆盖度直接塌掉），
要么自己写。我选了后者，于是有了：

| 自研模块 | 替换了什么 | 为什么值得 |
|---|---|---|
| `src/pdftext.py` | PyMuPDF / pypdf | PyMuPDF 是 **AGPL-3.0**，装进 MIT 仓库是明确的授权冲突（正是挑战红线之一）；自研版还顺手解决了对象流（ObjStm）与 CR-only 换行两个真实坑 |
| `src/htmlmd.py` | trafilatura / readability | 正文抽取逻辑全部可控可审计，出问题能定位到行 |
| `src/jslit.py` | 无头浏览器 | 不引入 200MB 级运行时，且**不 eval**，压缩包里的代码一行都不会被执行 |

零依赖的副产物是：**评审方不需要装任何东西，clone 下来就能跑**——"可复现"这条硬要求因此真正成立。

---

## 🙏 致谢与拿来

**原文版权**：全部英文原文版权归 **Stanford University CS146S 课程组（讲师 Mihail Eric）
及各原文作者**所有；嘉宾讲义版权归 **Cognition、Anthropic、Graphite、Vercel、Warp、Resolve AI** 等
相应公司所有。本包为**非官方学习译本**，仅供学习交流，不得商用。

**复用了什么**（完整清单与逐项 License 见 [`拿来说明.md`](拿来说明.md) §1）：

| 来源 | 取用了什么 | License |
|---|---|---|
| Stanford CS146S 官网与官方作业仓库 | 全部英文原文与讲义 | 版权归原作者，学习用途 |
| Wayback Machine（archive.org） | 2 篇已下线文章的存档快照 | 存档服务条款 |
| dair-ai/Prompt-Engineering-Guide | 1 篇客户端渲染页面的官方 Markdown 原文 | MIT |
| r.jina.ai 文本代理 | 仅在全部一手途径失败时的最后兜底（本次**未实际使用**） | 第三方服务 |

> 本包**没有**复用任何第三方翻译引擎、没有使用商业 MT API、没有引入任何 copyleft 依赖。

## 📄 License

- **流水线代码**（`src/`、`scripts/`、`tests/`）：[MIT](LICENSE)
- **译文与原文素材**（`corpus/`、`translated/`、`glossary/`、`sources/`）：
  见 [LICENSE-CONTENT.md](LICENSE-CONTENT.md) —— 版权归原作者，仅供学习用途，不得商用。
