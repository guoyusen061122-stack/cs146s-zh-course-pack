# Silas Alberti, Head of Research Cognition（fall2025 W3）

# Silas Alberti，Cognition 研究负责人（fall2025 W3）

## Slide 1

## Slide 1

IDE ❤ Agents An opinionated guide to AI coding in 2025 CS146S: The Modern Software Developer – Oct 10, 2025

IDE ❤ Agents 2025 年 AI 编码的一份有主见指南 CS146S：The Modern Software Developer – Oct 10, 2025

## Slide 2

## Slide 2

Silas Alberti Founding Team @ Cognition Prev: Stanford PhD Student

Silas Alberti Founding Team @ Cognition 此前：Stanford 博士生

## Slide 3

## Slide 3

Agenda 1. Overview of the AI tooling landscape 2. Synchronous vs. asynchronous tools 3. The 2025 coding workflow

议程 1. AI 工具版图概览 2. 同步工具与异步工具 3. 2025 年的编码工作流

- 

- 

When to hand-off from sync to async?

什么时候该从同步交接给异步？

- 

- 

How to combine tools like Devin & Windsurf 4. Where are we headed?

如何组合 Devin 与 Windsurf 这类工具 4. 我们要走向哪里？

## Slide 4

## Slide 4

Three Eras of AI Coding Tools Local Development ⇒ Collaborative Cloud Agents GitHub Copilot: speed up coding Code Completion 1 AI IDEs: single-player task completion IDE Automation 2 Image 2 AI agents: scale workﬂows in parallel AI Software Engineer 3 Overview

AI 编码工具的三个时代 本地开发 ⇒ 云端协作智能体 GitHub Copilot：加速编码 代码补全 1 AI IDE：单人任务完成 IDE 自动化 2 Image 2 AI 智能体：并行扩展工作流 AI 软件工程师 3 概览

## Slide 5

## Slide 5

Three Eras of AI Coding Tools Local Development ⇒ Collaborative Cloud Agents GitHub Copilot: speed up coding Code Completion 1 AI IDEs: single-player task completion IDE Automation 2 Image 2 AI agents: scale workﬂows in parallel AI Software Engineer 3 Overview ~10% efﬁciency gain ~20% efﬁciency gain 6-12x efﬁciency gain Local, Synchronous Cloud, Asynchronous

AI 编码工具的三个时代 本地开发 ⇒ 云端协作智能体 GitHub Copilot：加速编码 代码补全 1 AI IDE：单人任务完成 IDE 自动化 2 Image 2 AI 智能体：并行扩展工作流 AI 软件工程师 3 概览 约 10% 效率提升 约 20% 效率提升 6-12 倍效率提升 本地、同步 云端、异步

## Slide 6

## Slide 6

Synchronous vs. Asynchronous sync: single-threaded, human-in-the-loop, your attention is focused on one task => AI agent works for 20 seconds - 1.5 minutes

同步与异步 sync： 单线程，人在回路，你的注意力集中在一个任务上 => AI 智能体工作 20 秒 - 1.5 分钟

## Slide 7

## Slide 7

Synchronous vs. Asynchronous sync: single-threaded, human-in-the-loop, your attention is focused on one task => AI agent works for 20 seconds - 1.5 minutes async: multi-threaded, human delegates to AI, switches attention between multiple tasks => AI agent works for 10 minutes - multiple hours

同步与异步 sync： 单线程，人在回路，你的注意力集中在一个任务上 => AI 智能体工作 20 秒 - 1.5 分钟 async： 多线程，人把任务委派给 AI，在多个任务之间切换注意力 => AI 智能体工作 10 分钟 - 数小时

## Slide 8

## Slide 8

Local Cloud Sync Async

本地 云端 同步 异步

## Slide 9

## Slide 9

Local Cloud Sync Async

本地 云端 同步 异步

## Slide 10

## Slide 10

Local Cloud Sync Async

本地 云端 同步 异步

## Slide 11

## Slide 11

Local Cloud Sync Async DeepWiki

本地 云端 同步 异步 DeepWiki

## Slide 12

## Slide 12

Overview Cloud + Async enables 10x parallelism Boost individual speed. Local IDE Local IDE Local IDE Users Laptops Env Users Devins Env In VPC Local AI IDEs Unlimited Devins for parallel capacity . Cloud AI Agents Local • Synchronous • 1-to-1 • Isolated Knowledge Cloud • Asynchronous • 1-to-Many • Organizational Knowledge

概览 云端 + 异步带来 10 倍并行度 提升个体速度。 本地 IDE 本地 IDE 本地 IDE 用户 笔记本电脑 环境 用户 Devins 环境 VPC 内 本地 AI IDE 无限个 Devin 提供并行容量 。 云端 AI 智能体 本地 • 同步 • 一对一 • 孤立知识 云端 • 异步 • 一对多 • 组织知识

## Slide 13

## Slide 13

Using async agents is a hard but learnable skill Managing async agents can unlock 10x gains… …but most people use sync agents.

使用异步智能体是一门难但可学的技能 管理异步智能体可以释放 10 倍收益…… ……但大多数人用的是同步智能体。

## Slide 14

## Slide 14

Using async agents is a hard but learnable skill Managing async agents can unlock 10x gains… …but most people use sync agents. Why?

使用异步智能体是一门难但可学的技能 管理异步智能体可以释放 10 倍收益…… ……但大多数人用的是同步智能体。 为什么？

- 

- 

Turns out management & delegation is a difficult skill to master – whether it’s humans or agents.

事实证明，管理委派是一门很难掌握的技能——无论对象是人还是智能体。

- 

- 

Requires ability to cycle between multiple tasks and quickly understanding new context

需要具备在多个任务之间轮转的能力，并能快速理解新上下文

## Slide 15

## Slide 15

Semi-Async: The awkward middle Sync Async “Semi-Async” 5s 10s 30s 1m 3m 5m 10m 1h 3h Flow Barrier

半异步：尴尬的中间地带 同步 异步 「半异步」 5s 10s 30s 1m 3m 5m 10m 1h 3h 心流屏障

## Slide 16

## Slide 16

Semi-Async: The awkward middle Sync Async “Semi-Async” 5s 10s 30s 1m 3m 5m 10m 1h 3h Avoid! Too slow for staying in flow. Too short for multi-tasking. Flow Barrier

半异步：尴尬的中间地带 同步 异步 「半异步」 5s 10s 30s 1m 3m 5m 10m 1h 3h 避免！ 慢得无法保持心流。 又短得无法多任务处理。 心流屏障

## Slide 17

## Slide 17

Semi-Async: The awkward middle Sync Async “Semi-Async” 5s 10s 30s 1m 3m 5m 10m 1h 3h Avoid! Too slow for staying in flow. Too short for multi-tasking. Make faster to preserve flow Trade time for higher intelligence Flow Barrier

半异步：尴尬的中间地带 同步 异步 「半异步」 5s 10s 30s 1m 3m 5m 10m 1h 3h 避免！ 慢得无法保持心流。 又短得无法多任务处理。 做得更快以保持心流 用时间换更高的智能 心流屏障

## Slide 18

## Slide 18

Planning Coding Testing

规划 编码 测试

## Slide 19

## Slide 19

Planning Coding Testing sync async sync

规划 编码 测试 同步 异步 同步

## Slide 20

## Slide 20

Planning with Windsurf & Devin 1. DeepWiki 2. Ask Devin 3. Codemaps 4. DeepWiki in Windsurf

用 Windsurf 与 Devin 做规划 1. DeepWiki 2. Ask Devin 3. Codemaps 4. Windsurf 中的 DeepWiki

## Slide 21

## Slide 21

Delegate the coding to the agent

把编码委派给智能体

## Slide 22

## Slide 22

Delegate the coding to the agent

把编码委派给智能体

## Slide 23

## Slide 23

Testing the agent’s changes Common workflow:

测试智能体的改动 常见工作流：

1. Delegate task to Devin (async)
1. Test & refine changes in Windsurf (sync)

1. 把任务委派给 Devin（异步）
1. 在 Windsurf 中测试并打磨改动（同步）

## Slide 24

## Slide 24

Testing the agent’s changes Common workflow:

测试智能体的改动 常见工作流：

1. Delegate task to Devin (async)
1. Test & refine changes in Windsurf (sync)

1. 把任务委派给 Devin（异步）
1. 在 Windsurf 中测试并打磨改动（同步）

Future outlook: If async agents could test autonomously, the leverage increases. This is slowly starting to become a reality.

未来展望： 如果异步智能体能自主测试，杠杆会更大。 这正在慢慢变成现实。

## Slide 25

## Slide 25

Planning Coding Testing Where are we headed? Today:

规划 编码 测试 我们要走向哪里？ 今天：

## Slide 26

## Slide 26

Planning Coding Testing Where are we headed? Planning Coding Testing Today: Future:

规划 编码 测试 我们要走向哪里？ 规划 编码 测试 今天： 未来：

## Slide 27

## Slide 27

Where are we headed? 1. The human engineer as the agent manager a. Leveraging sync tools to solve the most difficult problems b. Leveraging async tools to achieve 10x leverage

我们要走向哪里？ 1. 人类工程师作为智能体管理者 a. 利用同步工具解决最难的问题 b. 利用异步工具获得 10 倍杠杆

## Slide 28

## Slide 28

Where are we headed? 1. The human engineer as the agent manager a. Leveraging sync tools to solve the most difficult problems b. Leveraging async tools to achieve 10x leverage 2. Valuable skills for the future: a. Delegation & multi-threading b. Code reading c. Planning, scoping, architecting

我们要走向哪里？ 1. 人类工程师作为智能体管理者 a. 利用同步工具解决最难的问题 b. 利用异步工具获得 10 倍杠杆 2. 面向未来的宝贵技能： a. 委派与多线程 b. 代码阅读 c. 规划、划定范围、架构设计

## Slide 29

## Slide 29

Thank you!

谢谢！
