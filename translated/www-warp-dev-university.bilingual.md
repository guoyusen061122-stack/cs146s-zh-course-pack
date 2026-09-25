# Warp University

# Warp University

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

> 完整的文档索引见 [llms.txt](https://docs.warp.dev/llms.txt)。
> 每个页面的 Markdown 版本都可以在任何 URL 后追加 .md 获得。

# Getting started with Warp

# Warp 入门

Get started with Warp, the Agentic Development Environment, and the Automation Platform, which orchestrates cloud agents at scale.

从 Warp 开始：它是智能体化开发环境（Agentic Development Environment），以及自动化平台（Automation Platform），后者可大规模编排云端智能体。

Warp is an [open source](https://github.com/warpdotdev/warp) **Agentic Development Environment** that combines a modern, high-performance terminal with powerful agents to help you build, test, deploy, and debug code. Agents in Warp are powered by the **Automation Platform**, which orchestrates agents locally or in the cloud at scale.

Warp 是一个[开源](https://github.com/warpdotdev/warp)的**智能体化开发环境**，把现代高性能终端与强大的智能体结合起来，帮助你构建、测试、部署和调试代码。Warp 中的智能体由**自动化平台**驱动，该平台可在本地或云端大规模编排智能体。

![Two panels side by side: Warp, a modern terminal built for coding with agents, and Warp Factories, open infrastructure for building cloud software factories](https://docs.warp.dev/_astro/warp-factories-welcome.rhXaWld0_2f30gX.webp?dpl=dpl_F7D8J5JuYJnLjprxdi483kF2EyKz)

![左右并排的两个面板：Warp，一个为智能体编码而构建的现代终端；以及 Warp Factories，用于构建云端软件工厂的开放基础设施](https://docs.warp.dev/_astro/warp-factories-welcome.rhXaWld0_2f30gX.webp?dpl=dpl_F7D8J5JuYJnLjprxdi483kF2EyKz)

Warp and Warp Factories in the Agentic Development Environment.

智能体化开发环境中的 Warp 与 Warp Factories。

---

---

## Warp

## Warp

Warp is where you work — a fast, modern terminal built for coding with agents.

Warp 是你工作的地方——一个快速、现代的终端，为与智能体协作编码而构建。

**Key capabilities:**

**核心能力：**

- [**Terminal and Agent modes**](https://docs.warp.dev/agents/local-agents/interacting-with-agents/terminal-and-agent-modes/): Switch between a clean terminal for commands and a dedicated conversation view for multi-turn agent workflows.
- [**Modern terminal UX**](https://docs.warp.dev/terminal/editor/): Cursor movement, block-based navigation, multi-line editing, syntax highlighting, and rich completions. Built with Rust for high performance.
- [**Code editor**](https://docs.warp.dev/code/overview/): File tree, code editor with LSP support, and interactive code review experience.
- [**Third-party CLI agents**](https://docs.warp.dev/agents/cli-agents/overview/): Run third-party CLI agents like Claude Code, Codex, and OpenCode with the agent toolbelt — rich input, code review, notifications, and more.

- [**终端模式与智能体模式**](https://docs.warp.dev/agents/local-agents/interacting-with-agents/terminal-and-agent-modes/)：在用于执行命令的干净终端与用于多轮智能体工作流的专用对话视图之间切换。
- [**现代终端体验**](https://docs.warp.dev/terminal/editor/)：光标移动、基于块的导航、多行编辑、语法高亮和丰富补全。用 Rust 构建，性能出色。
- [**代码编辑器**](https://docs.warp.dev/code/overview/)：文件树、支持 LSP 的代码编辑器，以及可交互的代码评审体验。
- [**第三方 CLI 智能体**](https://docs.warp.dev/agents/cli-agents/overview/)：借助智能体工具带运行 Claude Code、Codex、OpenCode 等第三方 CLI 智能体——丰富的输入、代码评审、通知等等。

![Deep dive into Warp's core features](https://i.ytimg.com/vi/xhkoXsE9Wqc/sddefault.jpg)

![深入剖析 Warp 的核心功能](https://i.ytimg.com/vi/xhkoXsE9Wqc/sddefault.jpg)

---

---

## Three ways to use the Warp Agent

## 使用 Warp 智能体的三种方式

The **Warp Agent** writes and edits code, debugs issues, runs commands, and works through multi-step tasks. You reach the same agent three ways, and your account, rules, skills, and model access carry across all of them.

**Warp 智能体**会编写和修改代码、调试问题、运行命令，并推进多步骤任务。你可以通过三种方式使用同一个智能体，你的账号、规则、技能和模型访问权限在三种方式之间通用。

### In the Warp app

### 在 Warp 应用里

Real-time, interactive coding assistance alongside your terminal.

与终端并行的实时交互式编码辅助。

- Write and refactor code across your codebase
- Debug issues and fix errors
- Run commands and interpret results
- Plan and execute multi-step tasks

- 在你的代码库中编写和重构代码
- 调试问题并修复错误
- 运行命令并解读结果
- 规划并执行多步骤任务

You stay in control. Review changes, steer the agent mid-task, and approve actions before they execute.

控制权始终在你手上。审查改动、在任务进行中引导智能体，并在动作执行前批准。

→ [Get started with agents in Warp](https://docs.warp.dev/agents/)

→ [在 Warp 中开始使用智能体](https://docs.warp.dev/agents/)

### In any terminal, with the Warp Agent CLI

### 在任何终端里，使用 Warp Agent CLI

The Warp Agent CLI is a standalone terminal program that runs the same agent without the Warp app. Run the `warp` command to start a conversation in whichever terminal you already use, over SSH, or on a machine where Warp isn’t installed.

Warp Agent CLI 是一个独立的终端程序，无需 Warp 应用即可运行同一个智能体。在你已使用的任何终端中、通过 SSH，或在一台没有安装 Warp 的机器上，运行 `warp` 命令即可开始对话。

→ [Get started with the Warp Agent CLI](https://docs.warp.dev/agents/cli/quickstart/)

→ [开始使用 Warp Agent CLI](https://docs.warp.dev/agents/cli/quickstart/)

### In the cloud, as a cloud agent

### 在云端，作为云智能体

Cloud agents run in the background on Warp’s infrastructure (or your own) for automation at scale.

云智能体在 Warp 的基础设施（或你自己的基础设施）上后台运行，用于大规模自动化。

- **Triggers**: React to events from Slack, Linear, GitHub, or custom webhooks
- **Schedules**: Run recurring tasks like dependency updates or dead code removal
- **Parallelism**: Run many agents concurrently across repos or tasks
- **Observability**: Every run is tracked, auditable, and shareable with your team

- **触发器**：响应来自 Slack、Linear、GitHub 或自定义 webhook 的事件
- **定时调度**：运行依赖更新、死代码清理等周期性任务
- **并行**：跨多个仓库或任务并发运行大量智能体
- **可观测性**：每一次运行都可追踪、可审计，并可与团队共享

Cloud agents are ideal for work that doesn’t need your immediate attention, like PR reviews, issue triage, routine maintenance, and integration-driven workflows.

云智能体适合那些不需要你立即关注的工作，例如 PR 评审、issue 分类、例行维护，以及由集成驱动的工作流。

→ [Learn about cloud agents](https://docs.warp.dev/platform/)

→ [了解云智能体](https://docs.warp.dev/platform/)

### The platform behind them

### 它们背后的平台

The **Automation Platform** is Warp’s programmable system for running and coordinating agents at scale. It provides the environments, triggers, integrations, orchestration, and observability that cloud agents run on, plus a CLI, API, and SDK.

**自动化平台**是 Warp 用于大规模运行和协调智能体的可编程系统。它提供云智能体运行所依赖的环境、触发器、集成、编排和可观测性，此外还有 CLI、API 和 SDK。

→ [Learn about the Automation Platform](https://docs.warp.dev/platform/overview/)

→ [了解自动化平台](https://docs.warp.dev/platform/overview/)

---

---

## Repeatable development workflows with Warp Factories

## 用 Warp Factories 实现可重复的开发工作流

A single cloud agent handles one task. **Warp Factories**, now in Early Access, lets your team run a software factory: a repeatable process where cloud agents triage, spec, implement, review, and verify work, and humans approve key decisions.

单个云智能体只处理一个任务。**Warp Factories** 目前处于早期访问阶段，它让你的团队运行一个软件工厂：云智能体对工作进行分类、编写规格、实现、评审和验证，人类则批准关键决策，整个过程可重复。

→ [Learn about Warp Factories](https://docs.warp.dev/factories/) or [request access](https://www.warp.dev/factories/request-access)

→ [了解 Warp Factories](https://docs.warp.dev/factories/) 或[申请访问](https://www.warp.dev/factories/request-access)

---

---

## How they work together

## 它们如何协同工作

Warp and the Automation Platform provide a unified experience across local and cloud development:

Warp 与自动化平台在本地开发和云端开发之间提供统一体验：

- **Same agent, anywhere**: Whether you’re working in the Warp app, in another terminal through the Warp Agent CLI, or running agents in the cloud, you’re using the same underlying agent capabilities.
- **Seamless handoff**: Start a task in the cloud and take over locally in Warp when you want hands-on control, without losing progress or context.
- **Shared context**: [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/), [Rules](https://docs.warp.dev/agents/capabilities/rules/), and [MCP servers](https://docs.warp.dev/agents/capabilities/mcp/) work across both local and cloud agents, so your team’s knowledge and tools are always available.
- **Team collaboration**: Share agent sessions, review agents’ actions, and steer running tasks, regardless of who started them.

- **同一个智能体，随处可用**：无论你是在 Warp 应用中工作、通过 Warp Agent CLI 在另一个终端里工作，还是在云端运行智能体，用的都是同一套底层智能体能力。
- **无缝交接**：在云端启动任务，想亲自动手时就在本地 Warp 中接管，进度和上下文都不会丢失。
- **共享上下文**：[Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/)、[Rules](https://docs.warp.dev/agents/capabilities/rules/) 和 [MCP 服务器](https://docs.warp.dev/agents/capabilities/mcp/)在本地和云端智能体之间通用，团队的知识和工具始终可用。
- **团队协作**：共享智能体会话、审查智能体的动作，并引导正在运行的任务，无论任务是谁启动的。

---

---

## Multi-model support

## 多模型支持

The Automation Platform is multi-model by design. You can [choose your preferred LLM](https://docs.warp.dev/agents/inference/model-choice/) from a curated set of top models.

自动化平台在设计上支持多模型。你可以从一组精选的顶尖模型中[选择偏好的 LLM](https://docs.warp.dev/agents/inference/model-choice/)。

---

---

## Open source

## 开源

Warp’s client is open source under [AGPL v3](https://github.com/warpdotdev/warp/blob/master/LICENSE-AGPL). The source lives at [`warpdotdev/warp`](https://github.com/warpdotdev/warp), where you can read the code, file issues, and contribute alongside the Warp team. Development happens in the open with an agent-first workflow managed by the Automation Platform.

Warp 客户端在 [AGPL v3](https://github.com/warpdotdev/warp/blob/master/LICENSE-AGPL) 下开源。源代码位于 [`warpdotdev/warp`](https://github.com/warpdotdev/warp)，你可以阅读代码、提交 issue，并与 Warp 团队一起贡献。开发以开放的、智能体优先的工作流进行，由自动化平台管理。

→ [Contributing to Warp](https://docs.warp.dev/support-and-community/community/contributing/) explains how to file issues, claim work, and ship code or themes.

→ [为 Warp 做贡献](https://docs.warp.dev/support-and-community/community/contributing/)说明了如何提交 issue、认领工作，以及提交代码或主题。

---

---

## Privacy and security

## 隐私与安全

Warp is **SOC 2 compliant** and has **Zero Data Retention** policies with all contracted LLM providers. No customer AI data is retained, stored, or used for training.

Warp 符合 **SOC 2** 标准，并对所有签约的 LLM 提供商执行**零数据保留**政策。不会保留、存储客户 AI 数据，也不会将其用于训练。

Warp’s AI features can be globally disabled in **Settings** > **Agents** > **Warp Agent**.

Warp 的 AI 功能可在**设置** > **Agents** > **Warp Agent** 中全局禁用。

→ [Read more about data privacy](https://www.warp.dev/privacy)

→ [进一步了解数据隐私](https://www.warp.dev/privacy)

---

---

## Next steps

## 后续步骤

- [**Quickstart**](https://docs.warp.dev/quickstart/): Get Warp installed and start coding
- [**Agents overview**](https://docs.warp.dev/agents/): What the Warp Agent does, how to control it, and where to run it
- [**Warp Agent CLI**](https://docs.warp.dev/agents/cli/): Run the Warp Agent in any terminal
- [**Cloud Agents overview**](https://docs.warp.dev/platform/): Set up background automation
- [**Automation Platform**](https://docs.warp.dev/platform/overview/): Learn about the CLI, API, SDK, and infrastructure

- [**快速开始**](https://docs.warp.dev/quickstart/)：安装 Warp 并开始编码
- [**智能体总览**](https://docs.warp.dev/agents/)：Warp 智能体能做什么、如何控制它、在哪里运行它
- [**Warp Agent CLI**](https://docs.warp.dev/agents/cli/)：在任何终端中运行 Warp 智能体
- [**云智能体总览**](https://docs.warp.dev/platform/)：搭建后台自动化
- [**自动化平台**](https://docs.warp.dev/platform/overview/)：了解 CLI、API、SDK 和基础设施
