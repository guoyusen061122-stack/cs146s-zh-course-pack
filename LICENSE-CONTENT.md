# 译文与原文素材 · 版权声明

> 本文件**不是**开源许可。它说明本仓库里**非代码部分**的版权归属与使用边界。
> 流水线代码的许可见 [`LICENSE`](LICENSE)（MIT）。

---

## 一、版权归属

本仓库的英文原文与中文译文，**版权均不属于本仓库作者**。逐项归属如下：

| 内容 | 位置 | 版权归属 |
|---|---|---|
| 课程官网正文（总览 / 大纲 / FAQ / 评分构成） | `corpus/en/site-*`、`corpus/zh/site-*` | **Stanford University CS146S 课程组**（讲师 Mihail Eric） |
| 官方作业仓库文档 | `corpus/*/repo-*` | **Mihail Eric / Stanford CS146S** |
| 课程讲义（Google Slides / Drive 导出） | `corpus/*/fall2025-w*`、`media_*` | **Stanford CS146S 课程组**及各场嘉宾所属公司：**Cognition、Anthropic、Graphite、Vercel、Resolve AI、Warp** |
| 课程指定阅读文章（第三方博客 / 论文 / 官方文档） | `corpus/en/<域名>-*` | **各原文作者与发布机构**（Anthropic、Google、OWASP、Palo Alto Networks、Semgrep、Snyk/Graphite、GitHub、Splunk、Stytch、Chroma、SRE Google、last9、resolve.ai、blakesmith.me、codinghorror、dbreunig、ravi-mehta、stytch、reillywood、unit42、embracethered、tldraw 等） |
| 中文译文 | `corpus/zh/`、`translated/` | **译文由本仓库作者产出，但属原作品的演绎作品**，其使用不得超出原文的授权范围 |

---

## 二、使用边界（请务必遵守）

**允许**：

- 个人学习、教学参考、研究用途；
- 在注明来源的前提下引用与链接；
- 基于本仓库的**流水线代码**（`src/`、`scripts/`、`tests/`，MIT 授权）做二次开发。

**不允许**：

- **商业用途**（原文与译文均不得用于商业目的）；
- 把译文**冒充为原创作品**或声称拥有其版权；
- 把原文或译文**整体再分发**到其他公开仓库而不注明来源与版权归属；
- 移除或修改本文件与各原文中的版权声明。

**关于本仓库是否公开的说明**：
本包为非官方学习译本，仅提供学习用途的中文译本。原始英文素材（`sources/`，约 40MB）
已通过 `.gitignore` 排除，**不再分发**；任何人 clone 后可用仓库内的抓取脚本重新获取。
译文保留在仓库中，是学分要求（"以可复用的方式发布成果"）与学习交流所必需；
如权利人有异议，请联系仓库作者，将立即移除相应内容。

---

## 三、第三方组件的 License 状况（逐项声明）

本项目的设计目标之一是**不引入任何 copyleft 依赖**。实际状况如下：

| 类别 | 组件 | License | 状态 |
|---|---|---|---|
| 运行依赖 | 无 —— **全部使用 Python 标准库** | — | ✅ 无第三方依赖 |
| 曾考虑但**未采用** | PyMuPDF | **AGPL-3.0** | ❌ 主动拒绝。AGPL 装进 MIT 仓库是明确的授权冲突 |
| 曾考虑但**未采用** | trafilatura / readability-lxml | Apache-2.0 / Apache-2.0 | ⚪ 未采用（自研 `htmlmd.py` 替代），非 License 原因 |
| 曾考虑但**未采用** | Playwright / Selenium | Apache-2.0 | ⚪ 未采用（自研 `jslit.py` 替代），体积原因 |
| 曾考虑但**未采用** | Argos Translate（离线 MT） | MIT | ⚪ 未采用，环境装不上（见 AI 日志决策 1） |
| 素材来源（非依赖） | `dair-ai/Prompt-Engineering-Guide` | **MIT** | ✅ 仅取用 1 篇 Markdown 原文，已注明 |
| 素材来源（非依赖） | Wayback Machine（archive.org） | 存档服务条款 | ✅ 仅取用 2 篇已下线文章的存档，已注明 |
| 兜底服务（未实际使用） | `r.jina.ai` | 第三方服务 | ⚪ 配置保留但本次未触发 |

**结论**：本仓库**不含任何 AGPL / GPL / LGPL 代码**，代码部分的 MIT 声明干净成立。
（对照：常见的 PDF 处理选型 PyMuPDF 是 AGPL-3.0，若直接采用会与 MIT 声明冲突 ——
这正是本项目选择自研 `src/pdftext.py` 的主要原因。）

---

## 四、本包不包含什么

- **不包含**原始英文素材的分发（`sources/` 被 `.gitignore` 排除）；
- **不包含**任何付费墙后的内容：遇到付费墙时只取公开可得的部分，并在
  `reports/_inventory.md` 中如实标注（如 `Specs Are the New Source Code` 仅有预览）；
- **不包含**需登录态才能获取的内容（1 份 401 讲义、3 份 Drive 文件、1 份 Figma 讲稿），
  已记入「已知缺口」，**没有用任何方式绕过权限**。

---

## 五、致谢

感谢 **Stanford CS146S 课程组（Mihail Eric）** 把这门课的讲义、作业与阅读清单公开出来；
感谢 **Cognition / Anthropic / Graphite / Vercel / Resolve AI / Warp** 的嘉宾同意课程公开其分享；
感谢所有被课程引用的文章作者。本包只是把它们译成中文，版权与功劳都归于他们。
