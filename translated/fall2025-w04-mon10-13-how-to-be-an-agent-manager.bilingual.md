# How to be an agent manager（fall2025 W4）

# 如何做一名智能体管理者（fall2025 W4）

## Slide 1

## Slide 1

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

## Slide 2

## Slide 2

themodernsoftware.dev Guest Lecture - 10/17/25 Anthropic Creator of Claude Code , Boris Cherny

themodernsoftware.dev 嘉宾讲座 - 10/17/25 Anthropic Claude Code 的创造者 Boris Cherny

## Slide 3

## Slide 3

How to be an Agent Manager themodernsoftware.dev

如何做一名智能体管理者 themodernsoftware.dev

## Slide 4

## Slide 4

Why

为什么

- 

- 

Development evolution

开发的演进

- 

- 

Single developer managing single developer’s output

单个开发者管理单个开发者的产出

- 

- 

Lead managing many developers worth of output

主管管理许多开发者的产出

- 

- 

Lead managing many developers worth of output (assisted by an AI system)

主管管理许多开发者的产出（由 AI 系统辅助）

- 

- 

Single developer managing many AI agents worth of work themodernsoftware.dev

单个开发者管理许多 AI 智能体的工作量 themodernsoftware.dev

## Slide 5

## Slide 5

A brief history of software teams themodernsoftware.dev Mainstream adoption of software teams, specialization emerges First software teams emerge driven by requirements of NASA, DoD projects 1940 2030 2025 Teams with developers managing groups of diverse agents 2023 Software teams with developers assisted by AI coding systems 1960 Solo developers handling full projects 1970 1990

软件团队的简史 themodernsoftware.dev 软件团队成为主流，专业化分工出现 第一批软件团队出现，由 NASA、DoD 项目的需求驱动 1940 2030 2025 由开发者管理多类智能体团队的团队 2023 由 AI 编码系统辅助开发者的软件团队 1960 独立开发者独自承担完整项目 1970 1990

## Slide 6

## Slide 6

Goals themodernsoftware.dev ….

目标 themodernsoftware.dev ….

## Slide 7

## Slide 7

Software task steps themodernsoftware.dev

软件任务步骤 themodernsoftware.dev

- 

- 

Provide high level requirements

给出高层需求

- 

- 

Convert requirements into a design doc

把需求转化为设计文档

/

/

- 

- 

Implement solution from doc

依据文档实现方案

- 

- 

Add tests

添加测试

- 

- 

Ensure CI (continuous integration) passes

确保 CI（持续集成）通过

- 

- 

Code review

代码评审

- 

- 

Update docs

更新文档

## Slide 8

## Slide 8

Techniques for directing agents themodernsoftware.dev

指挥智能体的技巧 themodernsoftware.dev

- 

- 

Agent behavior ﬁles (Claude.md/Cursorrules/agents.md)

智能体行为文件（Claude.md/Cursorrules/agents.md）

- 

- 

Hooks

Hooks

- 

- 

Commands

Commands

- 

- 

Subagents

子智能体

## Slide 9

## Slide 9

Hooks

Hooks

- 

- 

Deterministic scripts that run on predeﬁned event types

在预定义事件类型上运行的确定性脚本

- 

- 

PreToolUse

PreToolUse

- 

- 

PostToolUse

PostToolUse

- 

- 

UserPromptSubmit

UserPromptSubmit

- 

- 

PreCompact

PreCompact

- 

- 

…and more themodernsoftware.dev

……以及更多 themodernsoftware.dev

## Slide 10

## Slide 10

Commands

Commands

- 

- 

Provide frequently-used prompts as ﬁles that the agent can execute

把常用提示词做成文件，供智能体执行

- 

- 

Use cases

用例

- 

- 

Running tests

运行测试

- 

- 

Reviewing code

评审代码

- 

- 

Form a git commit, push themodernsoftware.dev

形成一次 git 提交并推送 themodernsoftware.dev

## Slide 11

## Slide 11

Subagents

子智能体

- 

- 

Runtime delegation

运行时委派

- 

- 

Purposes of a subagent is to

子智能体的用途是

- 

- 

Create distinct developer personas for different types of work (frontend, backend, etc)

为不同类型的工作（前端、后端等）创建不同的开发者角色

- 

- 

Cleanly separate contexts for different work streams

为不同工作流干净地隔离上下文

- 

- 

Offer

提供

- 

- 

Customized system prompts, tools, and a separate context window

定制化的系统提示词、工具，以及独立的上下文窗口

- 

- 

A move toward agents managing other agents

向着智能体管理其他智能体迈进

- 

- 

Use cases

用例

- 

- 

https://github.com/vijaythecoder/awesome-claude-agents/blob/main/CLAUDE.md

https://github.com/vijaythecoder/awesome-claude-agents/blob/main/CLAUDE.md

- 

- 

https://github.com/SuperClaude-Org/SuperClaude_Framework themodernsoftware.dev

https://github.com/SuperClaude-Org/SuperClaude_Framework themodernsoftware.dev

## Slide 12

## Slide 12

- 

- 

You need careful backstops

你需要仔细设置兜底机制

- 

- 

Tests in codebase

代码库中的测试

- 

- 

CI/CD best practices

CI/CD 最佳实践

- 

- 

Auditability of each agent

每个智能体的可审计性

- 

- 

Label every diff made by an agent

给智能体产生的每一处差异（diff）打标签

- 

- 

Different models for different classes of tasks

不同类型任务使用不同模型

- 

- 

More complex tasks you may need to handhold a bit more upfront vs fully async ones

越复杂的任务，越可能需要在前期多扶一把，而不像完全异步的任务那样

- 

- 

Checkpoint (commit) regularly themodernsoftware.dev Best practices

定期设置检查点（提交） themodernsoftware.dev 最佳实践

## Slide 13

## Slide 13

Workﬂow walkthrough themodernsoftware.dev

工作流走查 themodernsoftware.dev

## Slide 14

## Slide 14

- 

- 

How can we automate the ﬁrst 10-20% research phase of any task?

如何把任何任务最初 10-20% 的研究阶段自动化？

- 

- 

How to maintain a queue of pending tasks (easier for 1-off changes)? themodernsoftware.dev Open questions

如何维护一个待办任务队列（对一次性改动更方便）？ themodernsoftware.dev 开放问题
