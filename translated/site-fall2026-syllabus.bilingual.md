# CS146S 课程大纲 · fall2026

# CS146S 课程大纲 · fall2026

## Week 1: The Internals of Coding Agents

## 第 1 周：编码智能体的内部机制

### Topics

### 主题

- What an LLM actually is, and what the agent loop looks like under the hood
- The core tool set (read, write, edit, bash) and how tasks flow through it
- How production coding agents structure their system prompts and tool definitions

- 大语言模型（LLM）到底是什么，智能体循环在底层是什么样子
- 核心工具集（read、write、edit、bash）以及任务如何流经它
- 生产级编码智能体如何组织其系统提示词与工具定义

### Readings

### 阅读材料

- [Building a Coding Agent](https://youtube.com/watch?v=s7ZzkdvCMDY)

- [构建一个编码智能体](https://youtube.com/watch?v=s7ZzkdvCMDY)

### Sessions

### 课程安排

- Tue 9/22: Course intro + build Claude Code in 200 lines
- [Slides](https://docs.google.com/presentation/d/1uztIhjHAG6O_9QOD1N_3wdhwhABml1fANXEN2dGwdbg/edit?usp=drive_link)
- [Completed code](https://drive.google.com/file/d/1DxKa_autBOu9s8DvItodgUAwH_pBg7aR/view?usp=drive_link)
- Thu 9/24: How state-of-the-art coding agents are designed: deep dive into the system prompts that define the agent

- 周二 9/22：课程介绍 + 用 200 行代码构建 Claude Code
- [幻灯片](https://docs.google.com/presentation/d/1uztIhjHAG6O_9QOD1N_3wdhwhABml1fANXEN2dGwdbg/edit?usp=drive_link)
- [完整代码](https://drive.google.com/file/d/1DxKa_autBOu9s8DvItodgUAwH_pBg7aR/view?usp=drive_link)
- 周四 9/24：最先进的编码智能体是如何设计的：深入剖析定义智能体的系统提示词

## Week 2: Advanced Context Engineering

## 第 2 周：进阶上下文工程

### Topics

### 主题

- Advanced prompting techniques and when each applies
- RePPIT (Research, Propose, Plan, Implement, Test) and spec-driven development
- MCP fundamentals: servers, clients, tools, and transport
- Designing tools for agent ergonomics

- 进阶提示词技巧，以及每种技巧的适用场景
- RePPIT（研究、提议、规划、实现、测试）与规格驱动开发
- MCP 基础：服务器、客户端、工具与传输
- 为智能体易用性设计工具

### Sessions

### 课程安排

- Tue 9/29: Advanced prompting + agentic dev frameworks (RePPIT, spec-driven development)
- Thu 10/1: Full introduction to MCP and tool-calling (theory, setup, and advanced tool design)

- 周二 9/29：进阶提示词 + 智能体开发框架（RePPIT、规格驱动开发）
- 周四 10/1：MCP 与工具调用完整入门（理论、配置与进阶工具设计）

## Week 3: Agent Skills and CLI

## 第 3 周：智能体技能与 CLI

### Topics

### 主题

- What skills are and how SKILL.md + scripts encode a workflow
- Web skills and extending agent capability beyond the repo
- Working effectively from the CLI

- 技能是什么，以及 SKILL.md 与脚本如何编码一个工作流
- Web 技能，以及把智能体能力扩展到仓库之外
- 在 CLI 中高效工作

### Sessions

### 课程安排

- Tue 10/6: All about agent skills (including web skills)
- Thu 10/8: Guest: Lee Robinson (VP of Developer Relations @ Cursor) ([profile](https://leerob.com))

- 周二 10/6：智能体技能全解（含 Web 技能）
- 周四 10/8：嘉宾：Lee Robinson（Cursor 开发者关系副总裁）（[主页](https://leerob.com)）

## Week 4: Customizing Your Agent and Repository

## 第 4 周：定制你的智能体与仓库

### Topics

### 主题

- CLAUDE.md and AGENTS.md: what to put where
- Hooks for lint gates, test runs, and guardrails
- Subagent patterns (planner / implementer / reviewer)

- CLAUDE.md 与 AGENTS.md：哪些内容放在哪里
- 用于静态检查门禁、测试运行与护栏的钩子
- 子智能体模式（规划者 / 实现者 / 评审者）

### Sessions

### 课程安排

- Tue 10/13: Customizing your agentic setup (CLAUDE.md, AGENTS.md, hooks)
- Thu 10/15: Guest: Boris Cherny (Creator of Claude Code @ Anthropic) ([profile](https://borischerny.com))

- 周二 10/13：定制你的智能体化配置（CLAUDE.md、AGENTS.md、钩子）
- 周四 10/15：嘉宾：Boris Cherny（Anthropic 的 Claude Code 创建者）（[主页](https://borischerny.com)）

## Week 5: Agent-Ready Codebases

## 第 5 周：面向智能体的代码仓库

### Topics

### 主题

- What makes a repo agent-ready: structure, docs, tests, and checks
- Scoring and auditing readiness
- Common gaps that block agents in real repos

- 什么让仓库对智能体友好：结构、文档、测试与检查
- 就绪度评分与审计
- 真实仓库中阻碍智能体的常见缺口

### Sessions

### 课程安排

- Tue 10/20: Agent readiness in your repos (structure, docs, and checks that make repos agent-friendly)
- Thu 10/22: Guest: Eno Reyes (CTO @ Factory) ([profile](https://www.linkedin.com/in/enoreyes))

- 周二 10/20：让你的仓库对智能体就绪（使仓库对智能体友好的结构、文档与检查）
- 周四 10/22：嘉宾：Eno Reyes（Factory 首席技术官）（[主页](https://www.linkedin.com/in/enoreyes)）

## Week 6: Agentic Code Review

## 第 6 周：智能体化代码评审

### Topics

### 主题

- What AI review catches well, and what it misses
- Review architectures and custom rules
- Fitting AI review into a team's PR workflow

- AI 评审擅长发现什么，又会漏掉什么
- 评审架构与自定义规则
- 把 AI 评审融入团队的 PR 工作流

### Sessions

### 课程安排

- Tue 10/27: Agentic code review: best practices and architectures
- Thu 10/29: Guest: Silas Alberti (SVP Research @ Cognition) ([profile](https://sil.as))

- 周二 10/27：智能体化代码评审：最佳实践与架构
- 周四 10/29：嘉宾：Silas Alberti（Cognition 研究高级副总裁）（[主页](https://sil.as)）

## Week 7: Security

## 第 7 周：安全

### Topics

### 主题

- SAST / SCA, dependency and secret-leak vulnerabilities
- Prompt injection and agent-specific attack surfaces
- Agent-assisted triage and remediation

- SAST / SCA，依赖漏洞与密钥泄露漏洞
- 提示注入与智能体特有的攻击面
- 智能体辅助的分诊与修复

### Sessions

### 课程安排

- Tue 11/3: Security in AI codebases
- Thu 11/5: Guest: Isaac Evans (CEO @ Semgrep) ([profile](https://www.linkedin.com/in/isaacevans))

- 周二 11/3：AI 代码仓库中的安全
- 周四 11/5：嘉宾：Isaac Evans（Semgrep 首席执行官）（[主页](https://www.linkedin.com/in/isaacevans)）

## Week 8: Background Agents

## 第 8 周：后台智能体

### Topics

### 主题

- Async, cloud-delegated agents
- Managing fleets of parallel agents
- Issue-to-PR pipelines and triggers (Slack, Linear, GitHub)

- 异步、云端托管的智能体
- 管理并行智能体集群
- 从 issue 到 PR 的流水线与触发器（Slack、Linear、GitHub）

### Sessions

### 课程安排

- Tue 11/10: Background agents: launching tasks asynchronously
- Thu 11/12: Guest: Rajesh Bhatia (Senior Director @ Cloudflare) ([profile](https://www.linkedin.com/in/rajeshbh))

- 周二 11/10：后台智能体：以异步方式启动任务
- 周四 11/12：嘉宾：Rajesh Bhatia（Cloudflare 高级总监）（[主页](https://www.linkedin.com/in/rajeshbh)）

## Week 9: Building an AI-Native Team

## 第 9 周：打造 AI 原生团队

### Topics

### 主题

- MCP portals and centralized, permissioned tool access
- LLM gateways, model routing, and cost optimization
- Org-wide adoption patterns

- MCP 门户与集中式、带权限的工具访问
- LLM 网关、模型路由与成本优化
- 组织范围内的采纳模式

### Sessions

### 课程安排

- Tue 11/17: Guest: Elad Gil (Investor @ Gil Capital) ([profile](https://eladgil.com))
- Thu 11/19: Guest: Amjad Masad (CEO @ Replit) ([profile](https://amasad.me))

- 周二 11/17：嘉宾：Elad Gil（Gil Capital 投资人）（[主页](https://eladgil.com)）
- 周四 11/19：嘉宾：Amjad Masad（Replit 首席执行官）（[主页](https://amasad.me)）

## Week 10: The Software Factory + The Future

## 第 10 周：软件工厂 + 未来

### Topics

### 主题

- Self-running, self-improving software systems
- Running and securing agents post-deployment
- Where AI software engineering goes next

- 自运行、自改进的软件系统
- 部署后智能体的运行与安全防护
- AI 软件工程下一步走向何方

### Sessions

### 课程安排

- Tue 12/1: Coding agents in big teams (MCP portals, LLM gateways, org patterns, cost optimization, and model routing)
- Thu 12/3: The Software Factory: self-running, self-improving software systems

- 周二 12/1：大团队中的编码智能体（MCP 门户、LLM 网关、组织模式、成本优化与模型路由）
- 周四 12/3：软件工厂：自运行、自改进的软件系统
