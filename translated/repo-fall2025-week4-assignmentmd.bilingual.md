# Week 4 — The Autonomous Coding Agent IRL

# 第 4 周 —— 真实世界中的自主编码智能体

> ***We recommend reading this entire document before getting started.***

> ***我们建议你在动手之前先通读整份文档。***

This week, your task is to build at least **2 automations** within the context of this repository using any combination of the following **Claude Code** features:

本周你的任务是在本仓库的上下文下，用以下 **Claude Code** 功能的任意组合，构建至少 **2 个自动化功能**：

- Custom slash commands (checked into  `.claude/commands/*.md`)

- 自定义斜杠命令（提交到 `.claude/commands/*.md` ）

- `CLAUDE.md` files for repository or context guidance

- 用于仓库或上下文指引的 `CLAUDE.md` 文件

- Claude SubAgents (role-specialized agents working together)

- Claude SubAgents （各司其职、协同工作的角色化智能体）

- MCP servers integrated into Claude Code

- 集成到 Claude Code 中的 MCP 服务器

Your automations should meaningfully improve a developer workflow – for example, by streamlining tests, documentation, refactors, or data-related tasks. You will then use the automations you create to expand upon the starter application found in `week4/`.

你的自动化功能应当切实改善某个开发者工作流 —— 例如，精简测试、文档、重构或与数据相关的任务。随后，你要用自己创建的自动化功能来扩展 `week4/` 中的起步应用。

## Learn about Claude Code

## 了解 Claude Code

To gain a deeper understanding of Claude Code and explore your automation options, please read through the following two resources:

为了更深入地理解 Claude Code 并探索可选的自动化方案，请通读以下两份资料：

1. **Claude Code best practices:** [anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)

1. **Claude Code 最佳实践：** [anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)

1. **SubAgents overview:** [docs.anthropic.com/en/docs/claude-code/sub-agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)

1. **SubAgents 概述：** [docs.anthropic.com/en/docs/claude-code/sub-agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)

## Explore the Starter Application

## 探索起步应用

Minimal full‑stack starter application designed to be a **"developer's command center"**.

一个极简的全栈起步应用，定位是 **“开发者的指挥中心”**。

- FastAPI backend with SQLite (SQLAlchemy)
- Static frontend (no Node toolchain needed)
- Minimal tests (pytest)
- Pre-commit (black + ruff)
- Tasks to practice agent-driven workflows

- 带 SQLite （ SQLAlchemy ）的 FastAPI 后端
- 静态前端（不需要 Node 工具链）
- 极简测试（ pytest ）
- 预提交钩子（ black + ruff ）
- 供你练手智能体驱动工作流的任务

Use this application as your playground to experiment with the Claude automations you build.

把这个应用当作试验场，去试用你构建的 Claude 自动化功能。

### Structure

### 结构

```
backend/                # FastAPI app
frontend/               # Static UI served by FastAPI
data/                   # SQLite DB + seed
docs/                   # TASKS for agent-driven workflows
```

### Quickstart

### 快速开始

1. Activate your conda environment.

1. 激活你的 conda 环境。

```bash
conda activate cs146s
```

1. (Optional) Install pre-commit hooks

1. （可选）安装预提交钩子

```bash
pre-commit install
```

1. Run the app (from `week4/` directory)

1. 运行应用（在 `week4/` 目录下）

```bash
make run
```

1. Open `http://localhost:8000` for the frontend and `http://localhost:8000/docs` for the API docs.

1. 打开 `http://localhost:8000` 访问前端，打开 `http://localhost:8000/docs` 访问 API 文档。

1. Play around with the starter application to get a feel for its current features and functionality.

1. 试用这个起步应用，感受它当前的功能与特性。

### Testing

### 测试

Run the tests (from `week4/` directory)

运行测试（在 `week4/` 目录下）

```bash
make test
```

### Formatting/Linting

### 格式化/静态检查

```bash
make format
make lint
```

## Part I: Build Your Automation (Choose 2 or more)

## 第一部分：构建你的自动化功能（选择 2 个或更多）

Now that you’re familiar with the starter application, your next step is to build automations to enhance or extend it. Below are several automation options you can choose from. You can mix and match across categories.

既然你已经熟悉了起步应用，下一步就是构建自动化功能来增强或扩展它。下面列出若干可选的自动化方案，你可以跨类别自由搭配。

As you build your automations, document your changes in the `writeup.md` file. Leave the *"How you used the automation to enhance the starter application"* section empty for now - you will be returning to this in Part II of the assignment.

在构建自动化功能的过程中，把你的改动记录到 `writeup.md` 文件里。*“你如何使用该自动化功能来增强起步应用”* 一节先留空 —— 你会在作业的第二部分回到这里。

### A) Claude custom slash commands

### A) Claude 自定义斜杠命令

Slash commands are a feature for repeated workflows, letting you create reusable workflows in Markdown files inside `.claude/commands/`. Claude exposes these via `/`.

斜杠命令是为重复性工作流准备的特性，让你可以把可复用的工作流写成 Markdown 文件，放在 `.claude/commands/` 里。 Claude 通过 `/` 暴露这些命令。

- Example 1: Test runner with coverage
- Name: `tests.md`
- Intent: Run `pytest -q backend/tests --maxfail=1 -x` and, if green, run coverage.
- Inputs: Optional marker or path.
- Output: Summarize failures and suggest next steps.
- Example 2: Docs sync
- Name: `docs-sync.md`
- Intent: Read `/openapi.json`, update `docs/API.md`, and list route deltas.
- Output: Diff-like summary and TODOs.
- Example 3: Refactor harness
- Name: `refactor-module.md`
- Intent: Rename a module (e.g., `services/extract.py` → `services/parser.py`), update imports, run lint/tests.
- Output: A checklist of modified files and verification steps.

- 示例 1 ：带覆盖率的测试运行器
- 名称： `tests.md`
- 意图：运行 `pytest -q backend/tests --maxfail=1 -x` ，如果通过，再运行覆盖率统计。
- 输入：可选的标记或路径。
- 输出：总结失败情况并给出下一步建议。
- 示例 2 ：文档同步
- 名称： `docs-sync.md`
- 意图：读取 `/openapi.json` ，更新 `docs/API.md` ，并列出路由差异。
- 输出：类似 diff 的摘要与待办事项。
- 示例 3 ：重构脚手架
- 名称： `refactor-module.md`
- 意图：重命名模块（例如 `services/extract.py` → `services/parser.py` ），更新导入，运行静态检查/测试。
- 输出：一份被修改文件的清单与验证步骤。

> *Tips: Keep commands focused, use `$ARGUMENTS`, and prefer idempotent steps. Consider allowlisting safe tools and using headless mode for repeatability.*

> *提示：让命令保持聚焦，使用 `$ARGUMENTS` ，并优先选择幂等的步骤。可以考虑把安全的工具加入允许列表，并用无头模式保证可重复性。*

### B) `CLAUDE.md` guidance files

### B) `CLAUDE.md` 指引文件

The `CLAUDE.md` file is automatically read when starting a conversation, allowing you to provide repository-specific instructions, context, or guidance that influence Claude's behavior. Create a `CLAUDE.md` in the repo root (and optionally in `week4/` subfolders) to guide Claude’s behavior.

开始对话时会自动读取 `CLAUDE.md` 文件，这使你可以提供仓库专属的指令、上下文或指引，从而影响 Claude 的行为。在仓库根目录（以及可选的 `week4/` 子目录）创建 `CLAUDE.md` 来引导 Claude 的行为。

- Example 1: Code navigation and entry points
- Include: How to run the app, where routers live (`backend/app/routers`), where tests live, how the DB is seeded.
- Example 2: Style and safety guardrails
- Include: Tooling expectations (black/ruff), safe commands to run, commands to avoid, and lint/test gates.
- Example 3: Workflow snippets
- Include: “When asked to add an endpoint, first write a failing test, then implement, then run pre-commit.”

- 示例 1 ：代码导航与入口点
- 内容：如何运行应用、路由文件在哪里（ `backend/app/routers` ）、测试在哪里、数据库如何填充种子数据。
- 示例 2 ：风格与安全护栏
- 内容：工具链要求（ black/ruff ）、可以安全运行的命令、应当避免的命令，以及静态检查/测试关卡。
- 示例 3 ：工作流片段
- 内容：“当被要求添加端点时，先写一个失败的测试，再实现，最后运行预提交钩子。”

> *Tips: Iterate on `CLAUDE.md` like a prompt, keep it concise and actionable, and document custom tools/scripts you expect Claude to use.*

> *提示：像对待提示词一样反复打磨 `CLAUDE.md` ，保持简洁且可执行，并写明你期望 Claude 使用的自定义工具/脚本。*

### C) SubAgents (role-specialized)

### C) SubAgents （角色化）

SubAgents are specialized AI assistants configured to handle specific tasks with their own system prompts, tools, and context. Design two or more cooperating agents, each responsible for a distinct step in a single workflow.

SubAgents 是专门化的 AI 助手，它们各自配有系统提示词、工具和上下文，用来处理特定任务。设计两个或更多协同工作的智能体，每个负责单一工作流中一个明确的步骤。

- Example 1: TestAgent + CodeAgent
- Flow: TestAgent writes/updates tests for a change → CodeAgent implements code to pass tests → TestAgent verifies.
- Example 2: DocsAgent + CodeAgent
- Flow: CodeAgent adds a new API route → DocsAgent updates `API.md` and `TASKS.md` and checks drift against `/openapi.json`.
- Example 3: DBAgent + RefactorAgent
- Flow: DBAgent proposes a schema change (adjust `data/seed.sql`) → RefactorAgent updates models/schemas/routers and fixes lints.

- 示例 1 ： TestAgent + CodeAgent
- 流程： TestAgent 为某处改动编写/更新测试 → CodeAgent 实现代码让测试通过 → TestAgent 验证。
- 示例 2 ： DocsAgent + CodeAgent
- 流程： CodeAgent 新增一条 API 路由 → DocsAgent 更新 `API.md` 与 `TASKS.md` ，并对照 `/openapi.json` 检查是否偏离。
- 示例 3 ： DBAgent + RefactorAgent
- 流程： DBAgent 提出模式变更（调整 `data/seed.sql` ）→ RefactorAgent 更新模型/模式/路由并修复静态检查问题。

> *Tips: Use checklists/scratchpads, reset context (`/clear`) between roles, and run agents in parallel for independent tasks.*

> *提示：使用清单/草稿板，在不同角色之间重置上下文（ `/clear` ），并对相互独立的任务并行运行智能体。*

## Part II: Put Your Automations to Work

## 第二部分：让你的自动化功能投入实战

Now that you’ve built 2+ automations, let's put them to use! In the `writeup.md` under section *"How you used the automation to enhance the starter application"*, describe how you leveraged each automation to improve or extend the app’s functionality.

既然你已经构建了 2 个以上的自动化功能，那就把它们用起来！在 `writeup.md` 的*“你如何使用该自动化功能来增强起步应用”*一节中，描述你如何借助每个自动化功能来改进或扩展应用的功能。

e.g. If you implemented the custom slash command `/generate-test-cases`, explain how you used it to interact with and test the starter application.

例如，如果你实现了自定义斜杠命令 `/generate-test-cases` ，就说明你如何使用它与起步应用交互并对其进行测试。

## Deliverables

## 交付物

1. Two or more automations, which may include:
1. Slash commands in `.claude/commands/*.md`
1. `CLAUDE.md` files
1. SubAgent prompts/configuration (documented clearly, files/scripts if any)

1. 两个或更多的自动化功能，其中可以包括：
1. `.claude/commands/*.md` 中的斜杠命令
1. `CLAUDE.md` 文件
1. SubAgent 的提示词/配置（需清晰记录，若有文件/脚本一并给出）

1. A write-up `writeup.md` under `week4/` that includes:
1. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
1. Design of each automation, including goals, inputs/outputs, steps
1. How to run it (exact commands), expected outputs, and rollback/safety notes
1. Before vs. after (i.e. manual workflow vs. automated workflow)
1. How you used the automation to enhance the starter application

1. 一份位于 `week4/` 下的书面说明 `writeup.md` ，内容包括：
1. 设计灵感（例如引用最佳实践文档和/或子智能体文档）
1. 每个自动化功能的设计，包括目标、输入/输出、步骤
1. 如何运行（确切命令）、预期输出，以及回滚/安全注意事项
1. 之前与之后（即手动工作流与自动化工作流的对比）
1. 你如何使用该自动化功能来增强起步应用

## SUBMISSION INSTRUCTIONS

## 提交说明

1. Make sure you have all changes pushed to your remote repository for grading.
1. **Make sure you've added both brentju and febielin as collaborators on your assignment repository.**
1. Submit via Gradescope.

1. 确保所有改动都已经推送到你的远程仓库以供评分。
1. **确保你已经把 brentju 和 febielin 都添加为作业仓库的协作者。**
1. 通过 Gradescope 提交。
