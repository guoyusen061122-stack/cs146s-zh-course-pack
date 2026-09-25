# 素材清点报告

> 自动生成于 2026-09-25T12:37:59+08:00 ｜ 由 `src/s06_inventory.py` 产出 ｜ 全部数字可逐项复核

## 一、口径（先讲清楚分母）

- **素材总盘子**：102 项 —— 课程官网板块 + 作业仓库文档 + 大纲列出的全部阅读链接
  + 全部讲义/Drive/Figma 讲稿 + 全部视频。
- **已纳入语料**：89 项，合计 **776,025 字符**。
  （其中 6 项超长素材按块边界拆成 27 个翻译部分，故 `corpus/en/` 下有 110 个文件；拆分只为让单次翻译能稳定完成，不影响覆盖度口径。）
- **未纳入**：13 项，逐条原因见第四节。

## 二、覆盖率（四种口径，口径不同结论不同）

| 口径 | 算法 | 结果 |
|---|---|---|
| 按素材项 | 已纳入 / 总盘子 | **89/102 = 87.3%** |
| 可获取文本的翻译完成率 | 已译 / 全部可获取文本 | 见 `reports/_qa_report.md`（阶段 S10 统计） |
| 讲义覆盖 | 成功导出的讲稿 / 大纲列出的讲稿 | **16/17 = 94.1%** |
| Figma 讲稿 | 需登录态，脚本不代抓 | **0/1** |

## 三、语料构成

| 分组 | 份数 | 字符数 | 说明 |
|---|---:|---:|---|
| 课程官网（总览 / 大纲 / FAQ / 评分构成，两个学期） | 8 | 24,334 | |
| 官方作业仓库文档（Fall 2025 + Fall 2026） | 26 | 55,601 | |
| 课程指定阅读（文章 / PDF / 仓库文档） | 59 | 637,256 | |
| 课程讲义与官方文档（Google Slides / Drive 导出） | 17 | 58,834 | |
| **合计** | **110** | **776,025** | |

## 四、未纳入的素材（逐条列原因，不藏）

| 分组 | 素材 | 类型 | 状态 | 原因 |
|---|---|---|---|---|
| 课程指定阅读 | Super Claude | github_repo | SKIPPED | GitHub 仓库主页：属代码素材，登记不翻译（README 类文档另行处理） |
| 课程指定阅读 | Sample MCP Server Implementations | github_repo | SKIPPED | GitHub 仓库主页：属代码素材，登记不翻译（README 类文档另行处理） |
| 课程指定阅读 | Awesome Claude Agents | github_repo | SKIPPED | GitHub 仓库主页：属代码素材，登记不翻译（README 类文档另行处理） |
| 课程指定阅读 | How FAANG Vibe Codes | social_post | SKIPPED | 社交平台帖子：需登录态，脚本不代抓 |
| 讲义与其他 | Gaspar Garcia, Head of AI Research Vercel | google_slides | FAILED | HTTP 401 Unauthorized |
| 讲义与其他 | Course intro + build Claude Code in 200 lines | google_drive | FAILED | 需登录态或已限制下载权限（Drive 返回登录页） |
| 讲义与其他 | Building a coding agent from scratch | google_drive | FAILED | 需登录态或已限制下载权限（Drive 返回登录页） |
| 讲义与其他 | Building a custom MCP server | google_drive | FAILED | 需登录态或已限制下载权限（Drive 返回登录页） |
| 讲义与其他 | Zach Lloyd, CEO Warp | figma | SKIPPED | Figma 讲稿需登录态才能导出，脚本不代抓；原始链接已在讲义索引中保留 |
| 视频 | Building a Coding Agent | youtube | FAILED | timedtext 返回空体：YouTube 现要求 pot(proof-of-origin) 令牌 |
| 视频 | Deep Dive into LLMs | youtube | FAILED | timedtext 返回空体：YouTube 现要求 pot(proof-of-origin) 令牌 |
| 视频 | AI Prompt Engineering: A Deep Dive | youtube | FAILED | timedtext 返回空体：YouTube 现要求 pot(proof-of-origin) 令牌 |
| 视频 | Lessons from millions of AI code reviews | youtube | FAILED | timedtext 返回空体：YouTube 现要求 pot(proof-of-origin) 令牌 |

## 五、逐项清单

| # | 分组 | 标题 | 类型 | 字符 | 来源 |
|---:|---|---|---|---:|---|
| 1 | media | Mayank Agarwal, CTO Resolve, and Milind Ganjoo, Technical St | media_google_drive | 7,118 | https://drive.google.com/file/d/11WnEbMGc9kny_WBpMN10I8oP8 |
| 2 | media | Power prompting for LLMs（fall2025 W1） | media_google_slides | 6,252 | https://docs.google.com/presentation/d/1MIhw8p6TLGdbQ9Tcxh |
| 3 | media | Boris Cherney, Creator of Claude Code（fall2025 W4） | media_google_slides | 5,123 | https://docs.google.com/presentation/d/1bv7Zozn6z45CAh-IyX |
| 4 | media | Tomas Reimers, CPO Graphite（fall2025 W7） | media_google_drive | 4,908 | https://drive.google.com/file/d/1hwF-RIkOJ_OFy17BKhzFyCtxS |
| 5 | media | Introduction and how an LLM is made（fall2025 W1） | media_google_slides | 4,129 | https://docs.google.com/presentation/d/1zT2Ofy88cajLTLkd7T |
| 6 | media | AI QA, SAST, DAST, and Beyond（fall2025 W6） | media_google_slides | 3,963 | https://docs.google.com/presentation/d/1C05bCLasMDigBbkwdW |
| 7 | media | Silas Alberti, Head of Research Cognition（fall2025 W3） | media_google_slides | 3,685 | https://docs.google.com/presentation/d/1i0pRttHf72lgz8C-n7 |
| 8 | media | From first prompt to optimal IDE setup（fall2025 W3） | media_google_slides | 3,366 | https://docs.google.com/presentation/d/11pQNCde_mmRnImBat0 |
| 9 | media | Incident response and DevOps（fall2025 W9） | media_google_slides | 3,238 | https://docs.google.com/presentation/d/1Mfe-auWAsg9URCujne |
| 10 | media | Course intro + build Claude Code in 200 lines（fall2026 W1） | media_google_slides | 2,680 | https://docs.google.com/presentation/d/1uztIhjHAG6O_9QOD1N |
| 11 | media | How to Build a Breakout AI Developer Product（fall2025 W5） | media_google_slides | 2,578 | https://docs.google.com/presentation/d/1Djd4eBLBbRkma8rFnJ |
| 12 | media | How to be an agent manager（fall2025 W4） | media_google_slides | 2,480 | https://docs.google.com/presentation/d/19mgkwAnJDc7JuJy0zh |
| 13 | media | AI code review（fall2025 W7） | media_google_slides | 2,396 | https://docs.google.com/presentation/d/1NkPzpuSQt6Esbnr2-E |
| 14 | media | Building a custom MCP server（fall2025 W2） | media_google_slides | 2,247 | https://docs.google.com/presentation/d/1zSC2ra77XOUrJeyS85 |
| 15 | media | From first prompt to optimal IDE setup（fall2025 W3） | media_google_drive | 2,148 | https://drive.google.com/file/d/1MZ0Qx68Vzw4x5x_XcV8XiPLp7 |
| 16 | media | End-to-end apps with a single prompt（fall2025 W8） | media_google_slides | 1,503 | https://docs.google.com/presentation/d/1GrVLsfMFIXMiGjIW9D |
| 17 | media | Building a coding agent from scratch（fall2025 W2） | media_google_slides | 1,020 | https://docs.google.com/presentation/d/11CP26VhsjnZOmi9YFg |
| 18 | reading | Getting AI to Work In Complex Codebases | reading_github_file | 23,567 | https://github.com/humanlayer/advanced-context-engineering |
| 19 | reading | Writing Effective Tools for Agents | reading_html | 21,754 | https://www.anthropic.com/engineering/writing-tools-for-ag |
| 20 | reading | Introduction to Site Reliability Engineering | reading_html | 21,143 | https://sre.google/sre-book/introduction/ |
| 21 | reading | SAST vs DAST | reading_html | 20,909 | https://www.splunk.com/en_us/blog/learn/sast-vs-dast.html |
| 22 | reading | How to Review Code Effectively | reading_html | 20,526 | https://github.blog/developer-skills/github/how-to-review- |
| 23 | reading | Peeking Under the Hood of Claude Code | reading_html | 20,415 | https://medium.com/@outsightai/peeking-under-the-hood-of-c |
| 24 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 17,818 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 25 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 17,418 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 26 | reading | Prompt Engineering Guide | reading_html | 17,297 | https://www.promptingguide.ai/techniques |
| 27 | reading | Context Rot: Understanding Degradation in AI Context Windows | reading_html | 16,875 | https://research.trychroma.com/context-rot |
| 28 | reading | MCP Introduction（第 1/2 部分） | reading_html | 16,858 | https://stytch.com/blog/model-context-protocol-introductio |
| 29 | reading | MCP Server Authentication | reading_html | 16,702 | https://developers.cloudflare.com/agents/guides/remote-mcp |
| 30 | reading | Context Rot: Understanding Degradation in AI Context Windows | reading_html | 16,685 | https://research.trychroma.com/context-rot |
| 31 | reading | AI-Assisted Assessment of Coding Practices in Modern Code Re | reading_pdf | 16,678 | https://arxiv.org/pdf/2405.13565 |
| 32 | reading | How Anthropic Uses Claude Code（第 1/4 部分） | reading_pdf | 16,111 | https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f13 |
| 33 | reading | Claude Best Practices（第 2/3 部分） | reading_html | 16,038 | https://www.anthropic.com/engineering/claude-code-best-pra |
| 34 | reading | How Anthropic Uses Claude Code（第 2/4 部分） | reading_pdf | 15,357 | https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f13 |
| 35 | reading | Devin: Coding Agents 101 | reading_html | 15,326 | https://devin.ai/agents101#introduction |
| 36 | reading | Claude Best Practices（第 1/3 部分） | reading_html | 15,184 | https://www.anthropic.com/engineering/claude-code-best-pra |
| 37 | reading | How Anthropic Uses Claude Code（第 3/4 部分） | reading_pdf | 14,224 | https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f13 |
| 38 | reading | Prompt Engineering Overview | reading_html | 13,812 | https://cloud.google.com/discover/what-is-prompt-engineeri |
| 39 | reading | AI Code Review Implementation Best Practices | reading_html | 12,967 | https://graphite.dev/guides/ai-code-review-implementation- |
| 40 | reading | Good Context Good Code | reading_html | 12,912 | https://blog.stockapp.com/good-context-good-code/ |
| 41 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 12,780 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 42 | reading | MCP Introduction（第 2/2 部分） | reading_html | 12,273 | https://stytch.com/blog/model-context-protocol-introductio |
| 43 | reading | AI-Assisted Assessment of Coding Practices in Modern Code Re | reading_pdf | 12,036 | https://arxiv.org/pdf/2405.13565 |
| 44 | reading | How Anthropic Uses Claude Code（第 4/4 部分） | reading_pdf | 11,693 | https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f13 |
| 45 | reading | AI-Assisted Assessment of Coding Practices in Modern Code Re | reading_pdf | 11,630 | https://arxiv.org/pdf/2405.13565 |
| 46 | reading | Observability Basics You Should Know | reading_html | 10,754 | https://last9.io/blog/traces-spans-observability-basics/ |
| 47 | reading | How Long Contexts Fail | reading_html | 10,127 | https://www.dbreunig.com/2025/06/22/how-contexts-fail-and- |
| 48 | reading | Code Review Essentials for Software Teams | reading_html | 9,980 | https://blakesmith.me/2015/02/09/code-review-essentials-fo |
| 49 | reading | Role of Multi Agent Systems in Making Software Engineers AI- | reading_html | 9,723 | https://resolve.ai/blog/role-of-multi-agent-systems-AI-nat |
| 50 | reading | How OpenAI Uses Codex | reading_pdf | 9,413 | https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd |
| 51 | reading | Kubernetes Troubleshooting with AI | reading_html | 9,392 | https://resolve.ai/blog/kubernetes-troubleshooting-in-reso |
| 52 | reading | MCP Server SDK | reading_github_file | 8,311 | https://github.com/modelcontextprotocol/typescript-sdk/tre |
| 53 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 7,843 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 54 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 7,826 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 55 | reading | Finding Vulnerabilities in Modern Web Apps Using Claude Code | reading_html | 7,780 | https://semgrep.dev/blog/2025/finding-vulnerabilities-in-m |
| 56 | reading | Copilot Remote Code Execution via Prompt Injection | reading_html | 7,517 | https://embracethered.com/blog/posts/2025/github-copilot-r |
| 57 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 6,959 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 58 | reading | Your New Autonomous Teammate | reading_html | 6,665 | https://resolve.ai/blog/product-deep-dive |
| 59 | reading | MCP Registry | reading_html | 6,328 | https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp- |
| 60 | reading | Benefits of Agentic AI in On-call Engineering | reading_html | 6,240 | https://resolve.ai/blog/Top-5-Benefits |
| 61 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 6,232 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 62 | reading | Warp vs Claude Code | reading_html | 6,173 | https://www.warp.dev/university/getting-started/warp-vs-cl |
| 63 | reading | Warp University | reading_html | 6,171 | https://www.warp.dev/university?slug=university |
| 64 | reading | Context Rot: Understanding Degradation in AI Context Windows | reading_html | 5,860 | https://research.trychroma.com/context-rot |
| 65 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 5,832 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 66 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 4,960 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 67 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 4,878 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 68 | reading | MCP Food-for-Thought | reading_html | 4,559 | https://www.reillywood.com/blog/apis-dont-make-good-mcp-to |
| 69 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 3,391 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 70 | reading | Code Reviews: Just Do It | reading_html | 3,089 | https://blog.codinghorror.com/code-reviews-just-do-it/ |
| 71 | reading | Vulnerability Prompt Analysis with O3 | reading_github_file | 1,658 | https://github.com/SeanHeelan/o3_finds_cve-2025-37899/blob |
| 72 | reading | Specs Are the New Source Code | reading_html | 1,331 | https://blog.ravi-mehta.com/p/specs-are-the-new-source-cod |
| 73 | reading | OWASP Top Ten: The Leading Web Application Security Risks | reading_html | 860 | https://owasp.org/www-project-top-ten/ |
| 74 | reading | Claude Best Practices（第 3/3 部分） | reading_html | 350 | https://www.anthropic.com/engineering/claude-code-best-pra |
| 75 | reading | How Warp Uses Warp to Build Warp | reading_html | 42 | https://notion.warp.dev/How-Warp-uses-Warp-to-build-Warp-2 |
| 76 | reading | Agentic AI Threats: Identity Spoofing and Impersonation Risk | reading_html | 24 | https://unit42.paloaltonetworks.com/agentic-ai-threats/ |
| 77 | repo | CS146S 作业仓库 · week1/assignment.md（master） | repo | 8,446 | https://github.com/mihail911/modern-software-dev-assignmen |
| 78 | repo | CS146S 作业仓库 · week4/assignment.md（fall2025） | repo | 5,887 | https://github.com/mihail911/modern-software-dev-assignmen |
| 79 | repo | CS146S 作业仓库 · week5/docs/TASKS.md（fall2025） | repo | 4,359 | https://github.com/mihail911/modern-software-dev-assignmen |
| 80 | repo | CS146S 作业仓库 · week5/assignment.md（fall2025） | repo | 3,817 | https://github.com/mihail911/modern-software-dev-assignmen |
| 81 | repo | CS146S 作业仓库 · week8/assignment.md（fall2025） | repo | 3,693 | https://github.com/mihail911/modern-software-dev-assignmen |
| 82 | repo | CS146S 作业仓库 · week2/assignment.md（fall2025） | repo | 3,517 | https://github.com/mihail911/modern-software-dev-assignmen |
| 83 | repo | CS146S 作业仓库 · week3/assignment.md（fall2025） | repo | 3,175 | https://github.com/mihail911/modern-software-dev-assignmen |
| 84 | repo | CS146S 作业仓库 · week1/writeup.md（master） | repo | 2,752 | https://github.com/mihail911/modern-software-dev-assignmen |
| 85 | repo | CS146S 作业仓库 · week7/assignment.md（fall2025） | repo | 2,401 | https://github.com/mihail911/modern-software-dev-assignmen |
| 86 | repo | CS146S 作业仓库 · week6/assignment.md（fall2025） | repo | 2,075 | https://github.com/mihail911/modern-software-dev-assignmen |
| 87 | repo | CS146S 作业仓库 · week8/writeup.md（fall2025） | repo | 1,675 | https://github.com/mihail911/modern-software-dev-assignmen |
| 88 | repo | CS146S 作业仓库 · week1/assignment.md（fall2025） | repo | 1,648 | https://github.com/mihail911/modern-software-dev-assignmen |
| 89 | repo | CS146S 作业仓库 · week5/writeup.md（fall2025） | repo | 1,573 | https://github.com/mihail911/modern-software-dev-assignmen |
| 90 | repo | CS146S 作业仓库 · week2/writeup.md（fall2025） | repo | 1,517 | https://github.com/mihail911/modern-software-dev-assignmen |
| 91 | repo | CS146S 作业仓库 · week4/writeup.md（fall2025） | repo | 1,395 | https://github.com/mihail911/modern-software-dev-assignmen |
| 92 | repo | CS146S 作业仓库 · week7/writeup.md（fall2025） | repo | 1,200 | https://github.com/mihail911/modern-software-dev-assignmen |
| 93 | repo | CS146S 作业仓库 · week4/docs/TASKS.md（fall2025） | repo | 1,176 | https://github.com/mihail911/modern-software-dev-assignmen |
| 94 | repo | CS146S 作业仓库 · week7/README.md（fall2025） | repo | 1,108 | https://github.com/mihail911/modern-software-dev-assignmen |
| 95 | repo | CS146S 作业仓库 · week5/README.md（fall2025） | repo | 944 | https://github.com/mihail911/modern-software-dev-assignmen |
| 96 | repo | CS146S 作业仓库 · week6/writeup.md（fall2025） | repo | 846 | https://github.com/mihail911/modern-software-dev-assignmen |
| 97 | repo | CS146S 作业仓库 · README.md（fall2025） | repo | 672 | https://github.com/mihail911/modern-software-dev-assignmen |
| 98 | repo | CS146S 作业仓库 · README.md（master） | repo | 672 | https://github.com/mihail911/modern-software-dev-assignmen |
| 99 | repo | CS146S 作业仓库 · week7/docs/TASKS.md（fall2025） | repo | 486 | https://github.com/mihail911/modern-software-dev-assignmen |
| 100 | repo | CS146S 作业仓库 · week1/data/api_docs.txt（fall2025） | repo | 213 | https://github.com/mihail911/modern-software-dev-assignmen |
| 101 | repo | CS146S 作业仓库 · week6/requirements.txt（fall2025） | repo | 181 | https://github.com/mihail911/modern-software-dev-assignmen |
| 102 | repo | CS146S 作业仓库 · week1/README.md（fall2025） | repo | 173 | https://github.com/mihail911/modern-software-dev-assignmen |
| 103 | site | CS146S 课程大纲（fall2025） | site | 9,992 | https://themodernsoftware.dev/fall2025 |
| 104 | site | CS146S 课程大纲（fall2026） | site | 3,665 | https://themodernsoftware.dev/ |
| 105 | site | CS146S 官网 · 总览（fall2025） | site | 3,473 | https://themodernsoftware.dev/fall2025 |
| 106 | site | CS146S 官网 · 总览（fall2026） | site | 3,367 | https://themodernsoftware.dev/ |
| 107 | site | CS146S 常见问题（fall2025） | site | 1,803 | https://themodernsoftware.dev/fall2025 |
| 108 | site | CS146S 常见问题（fall2026） | site | 1,803 | https://themodernsoftware.dev/ |
| 109 | site | CS146S 评分构成（fall2026） | site | 130 | https://themodernsoftware.dev/ |
| 110 | site | CS146S 评分构成（fall2025） | site | 101 | https://themodernsoftware.dev/fall2025 |
