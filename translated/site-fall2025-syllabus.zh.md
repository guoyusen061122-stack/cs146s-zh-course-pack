# CS146S 课程大纲 · fall2025

## 第 1 周：编码 LLM 与 AI 开发入门

### 主题
- 课程安排说明
- 大语言模型（LLM）到底是什么
- 如何有效地写提示词

### 阅读材料
- [深入剖析 LLM](https://www.youtube.com/watch?v=7xTGNNLPyMI)
- [提示工程概览](https://cloud.google.com/discover/what-is-prompt-engineering)
- [提示工程指南](https://www.promptingguide.ai/techniques)
- [AI 提示工程：深入剖析](https://www.youtube.com/watch?v=T9aRN5JkmL8)
- [OpenAI 如何使用 Codex](https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf)

### 作业
- [LLM 提示词练习场](https://github.com/mihail911/modern-software-dev-assignments/tree/master/week1)

### 课程安排
- 周一 9/22：课程介绍与 LLM 是如何制造的
 - [幻灯片](https://docs.google.com/presentation/d/1zT2Ofy88cajLTLkd7TcuSM4BCELvF9qQdHmlz33i4t0/edit?usp=sharing)
- 周五 9/26：面向 LLM 的强力提示技巧
 - [幻灯片](https://docs.google.com/presentation/d/1MIhw8p6TLGdbQ9TcxhXSs5BaPf5d_h77QY70RHNfeGs/edit?usp=drive_link)

## 第 2 周：编码智能体的解剖

### 主题
- 智能体架构与组件
- 工具调用与函数调用
- MCP（模型上下文协议）

### 阅读材料
- [MCP 入门](https://stytch.com/blog/model-context-protocol-introduction/)
- [MCP 服务器示例实现](https://github.com/modelcontextprotocol/servers)
- [MCP 服务器认证](https://developers.cloudflare.com/agents/guides/remote-mcp-server/#add-authentication)
- [MCP 服务器 SDK](https://github.com/modelcontextprotocol/typescript-sdk/tree/main?tab=readme-ov-file#server)
- [MCP 注册表](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/)
- [MCP 的思考素材](https://www.reillywood.com/blog/apis-dont-make-good-mcp-tools/)

### 作业
- [AI IDE 中的第一步](https://github.com/mihail911/modern-software-dev-assignments/tree/master/week2)

### 课程安排
- 周一 9/29：从零构建一个编码智能体
 - [幻灯片](https://docs.google.com/presentation/d/11CP26VhsjnZOmi9YFgLlonzdib9BLyAlgc4cEvC5Fps/edit?usp=sharing)
 - [已完成练习](https://drive.google.com/file/d/1YtpKFVG13DHyQ2i3HOtwyVJOV90nWeL2/view?usp=drive_link)
- 周五 10/3：构建自定义 MCP 服务器
 - [幻灯片](https://docs.google.com/presentation/d/1zSC2ra77XOUrJeyS85houg1DU7z9hq5Y4ebagTch-5o/edit?usp=drive_link)
 - [已完成练习](https://drive.google.com/file/d/1J6lgZWcxPzpCpjujJSnW1aAkCYF6Yxv3/view?usp=drive_link)

## 第 3 周：AI IDE

### 主题
- 上下文管理与代码理解
- 面向智能体的 PRD
- IDE 集成与扩展

### 阅读材料
- [规格是新的源代码](https://blog.ravi-mehta.com/p/specs-are-the-new-source-code)
- [长上下文为何失败](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)
- [Devin：编码智能体 101](https://devin.ai/agents101#introduction)
- [让 AI 在复杂代码库中工作](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)
- [FAANG 如何 Vibe Coding](https://x.com/rohanpaul_ai/status/1959414096589422619)
- [为智能体编写有效的工具](https://www.anthropic.com/engineering/writing-tools-for-agents)

### 作业
- [构建自定义 MCP 服务器](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week3/assignment.md)

### 课程安排
- 周一 10/6：从第一次提示词到最优 IDE 配置
 - [幻灯片](https://docs.google.com/presentation/d/11pQNCde_mmRnImBat0Zymnp8TCS_cT_1up7zbcj6Sjg/edit?usp=sharing)
 - [设计文档模板](https://drive.google.com/file/d/1MZ0Qx68Vzw4x5x_XcV8XiPLp7fFDe1LJ/view?usp=drive_link)
- 周五 10/10：Silas Alberti，Cognition 研究负责人（[主页](https://sil.as)）
 - [幻灯片](https://docs.google.com/presentation/d/1i0pRttHf72lgz8C-n7DSegcLBgncYZe_ppU7dB9zhUA/edit?usp=sharing)

## 第 4 周：编码智能体模式

### 主题
- 管理智能体自主性级别
- 人类与智能体的协作模式

### 阅读材料
- [Anthropic 如何使用 Claude Code](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)
- [Claude 最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Awesome Claude Agents](https://github.com/vijaythecoder/awesome-claude-agents)
- [Super Claude](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- [好的上下文，好的代码](https://blog.stockapp.com/good-context-good-code/)
- [掀开 Claude Code 的引擎盖](https://medium.com/@outsightai/peeking-under-the-hood-of-claude-code-70f5a94a9a62)

### 作业
- [用 Claude Code 编码](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week4/assignment.md)

### 课程安排
- 周一 10/13：如何做一名智能体管理者
 - [幻灯片](https://docs.google.com/presentation/d/19mgkwAnJDc7JuJy0zhhoY0ZC15DiNpxL8kchPDnRkRQ/edit?usp=sharing)
- 周五 10/17：Boris Cherney，Claude Code 创建者（[主页](https://borischerny.com)）
 - [幻灯片](https://docs.google.com/presentation/d/1bv7Zozn6z45CAh-IyX99dMPMyXCHC7zj95UfwErBYQ8/edit?usp=sharing)

## 第 5 周：现代终端

### 主题
- AI 增强的命令行界面
- 终端自动化与脚本编写

### 阅读材料
- [Warp 大学](https://www.warp.dev/university?slug=university)
- [Warp 对比 Claude Code](https://www.warp.dev/university/getting-started/warp-vs-claude-code)
- [Warp 如何用 Warp 构建 Warp](https://notion.warp.dev/How-Warp-uses-Warp-to-build-Warp-21643263616d81a6b9e3e63fd8a7380c)

### 作业
- [用 Warp 进行智能体化开发](https://github.com/mihail911/modern-software-dev-assignments/tree/master/week5)

### 课程安排
- 周一 10/20：如何打造一款突破性的 AI 开发者产品
 - [幻灯片](https://docs.google.com/presentation/d/1Djd4eBLBbRkma8rFnJAWMT0ptct_UGB8hipmoqFVkxQ/edit?usp=sharing)
- 周五 10/24：Zach Lloyd，Warp 首席执行官（[主页](https://www.linkedin.com/in/zachlloyd)）
 - [幻灯片](https://www.figma.com/slides/kwbcmtqTFQMfUhiMH8BiEx/Warp---Stanford--Copy-?node-id=9-116&t=oBWBCk8mjg2l2NR5-1)

## 第 6 周：AI 测试与安全

### 主题
- 安全地 Vibe Coding
- 漏洞检测的历史
- AI 生成的测试套件

### 阅读材料
- [SAST 与 DAST 对比](https://www.splunk.com/en_us/blog/learn/sast-vs-dast.html)
- [通过提示注入实现的 Copilot 远程代码执行](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/)
- [用 Claude Code 和 OpenAI Codex 发现现代 Web 应用中的漏洞](https://semgrep.dev/blog/2025/finding-vulnerabilities-in-modern-web-apps-using-claude-code-and-openai-codex/)
- [智能体式 AI 威胁：身份冒用与伪装风险](https://unit42.paloaltonetworks.com/agentic-ai-threats/)
- [OWASP Top Ten：主要的 Web 应用安全风险](https://owasp.org/www-project-top-ten/)
- [上下文腐化：理解 AI 上下文窗口中的退化](https://research.trychroma.com/context-rot)
- [用 O3 进行漏洞提示词分析](https://github.com/SeanHeelan/o3_finds_cve-2025-37899/blob/master/system_prompt_uafs.prompt)

### 作业
- [编写安全的 AI 代码](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week6/assignment.md)

### 课程安排
- 周一 10/27：AI QA、SAST、DAST 及更多
 - [幻灯片](https://docs.google.com/presentation/d/1C05bCLasMDigBbkwdWbiz4WrXibzi6ua4hQQbTod_8c/edit?usp=sharing)
- 周五 10/31：Isaac Evans，Semgrep 首席执行官（[主页](https://www.linkedin.com/in/isaacevans)）

## 第 7 周：现代软件支持

### 主题
- 哪些 AI 代码系统值得我们信任
- 调试与诊断
- 智能文档生成

### 阅读材料
- [代码评审：去做就是了](https://blog.codinghorror.com/code-reviews-just-do-it/)
- [如何有效地评审代码](https://github.blog/developer-skills/github/how-to-review-code-effectively-a-github-staff-engineers-philosophy/)
- [现代代码评审中 AI 辅助的编码实践评测](https://arxiv.org/pdf/2405.13565)
- [AI 代码评审实施最佳实践](https://graphite.dev/guides/ai-code-review-implementation-best-practices)
- [软件团队的代码评审要点](https://blakesmith.me/2015/02/09/code-review-essentials-for-software-teams.html)
- [来自数百万次 AI 代码评审的经验](https://www.youtube.com/watch?v=TswQeKftnaw)

### 作业
- [代码评审练习](https://github.com/mihail911/modern-software-dev-assignments/tree/master/week7)

### 课程安排
- 周一 11/3：AI 代码评审
 - [幻灯片](https://docs.google.com/presentation/d/1NkPzpuSQt6Esbnr2-EnxM9007TL6ebSPFwITyVY-QxU/edit?usp=sharing)
- 周五 11/7：Tomas Reimers，Graphite 首席产品官（[主页](https://www.linkedin.com/in/tomasreimers)）
 - [幻灯片](https://drive.google.com/file/d/1hwF-RIkOJ_OFy17BKhzFyCtxSS7Pcf7p/view?usp=drive_link)

## 第 8 周：自动化 UI 与应用构建

### 主题
- 人人都能做设计与前端
- 快速 UI/UX 原型与迭代

### 作业
- [多技术栈 Web 应用构建](https://github.com/mihail911/modern-software-dev-assignments/tree/master/week8)

### 课程安排
- 周一 11/10：用一条提示词做端到端应用
 - [幻灯片](https://docs.google.com/presentation/d/1GrVLsfMFIXMiGjIW9D7EJIyLYh_-3ReHHNd_vRfZUoo/edit?usp=sharing)
- 周五 11/14：Gaspar Garcia，Vercel AI 研究负责人（[主页](https://www.linkedin.com/in/gaspargarcia)）
 - [幻灯片](https://docs.google.com/presentation/d/1Jf2aN5zIChd5tT86rZWWqY-iDWbxgR-uynKJxBR7E9E/edit?usp=sharing)

## 第 9 周：部署后的智能体

### 主题
- AI 系统的监控与可观测性
- 自动化事故响应
- 分诊与调试

### 阅读材料
- [站点可靠性工程导论](https://sre.google/sre-book/introduction/)
- [你应该了解的可观测性基础](https://last9.io/blog/traces-spans-observability-basics/)
- [用 AI 排查 Kubernetes 问题](https://resolve.ai/blog/kubernetes-troubleshooting-in-resolve-ai)
- [你的新自主队友](https://resolve.ai/blog/product-deep-dive)
- [多智能体系统在让软件工程师 AI 原生化中的作用](https://resolve.ai/blog/role-of-multi-agent-systems-AI-native-engineering)
- [智能体式 AI 在值班工程中的五大收益](https://resolve.ai/blog/Top-5-Benefits)

### 课程安排
- 周一 11/17：事故响应与 DevOps
 - [幻灯片](https://docs.google.com/presentation/d/1Mfe-auWAsg9URCujneKnHr0AbO8O-_U4QXBVOlO4qp0/edit?usp=sharing)
- 周五 11/21：Mayank Agarwal，Resolve 首席技术官，以及 Milind Ganjoo，Resolve 技术团队成员
 - [幻灯片](https://drive.google.com/file/d/11WnEbMGc9kny_WBpMN10I8oP8XsiQOnM/view?usp=sharing)

## 第 10 周：AI 软件工程的下一步

### 主题
- 软件开发角色的未来
- 新兴的 AI 编码范式
- 行业趋势与预测

### 课程安排
- 周一 12/1：10 年后的软件开发
- 周五 12/5：Martin Casado，a16z 普通合伙人（[主页](https://a16z.com/author/martin-casado/)）
