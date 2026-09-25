# From first prompt to optimal IDE setup（fall2025 W3）

# 从最初的提示词到最优 IDE 配置（fall2025 W3）

## Slide 1

## Slide 1

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

## Slide 2

## Slide 2

themodernsoftware.dev Guest Lecture - 10/10/25 (8:30am PT, 420-041) Cognition Head of Research, Silas Alberti

themodernsoftware.dev 嘉宾讲座 - 10/10/25 (8:30am PT, 420-041) Cognition 研究负责人 Silas Alberti

## Slide 3

## Slide 3

The AI IDE: Fundamentals to Power User themodernsoftware.dev

AI IDE：从基础到 高级用户 themodernsoftware.dev

## Slide 4

## Slide 4

Why

为什么

- 

- 

IDE (Integrated Development Environment)

IDE（集成开发环境）

- 

- 

All-in-one workspaces for software development containing editor, compiler, debugger, and more

一体化工作空间，用于软件开发，包含编辑器、编译器、调试器等

- 

- 

Most development work is done there so it’s a natural form factor for AI enhancement

大部分开发工作都在这里完成，所以它是 AI 增强的天然形态

- 

- 

In their evolution, there’s always a see-saw between functionality consolidation and developer customization themodernsoftware.dev

在 IDE 的演进过程中，功能整合与开发者自定义之间始终存在拉锯 themodernsoftware.dev

## Slide 5

## Slide 5

A brief history themodernsoftware.dev 2001 Intellij IDEA released with advanced contextual code navigation, refactoring, code completion 2015 Microsoft VSCode released offering lightweight editor with highly extensible ecosystem 1983 Release of Turbo Pascal, ﬁrst true IDE 1997 Microsoft Visual Studio released, offering advanced debugging capabilities for the C++/Visual Basic language 1980 2030 2023 Cursor released, one of the ﬁrst widely used AI native IDEs

简史 themodernsoftware.dev 2001 Intellij IDEA 发布，带来先进的上下文代码导航、重构、代码补全 2015 Microsoft VSCode 发布，提供轻量编辑器与高度可扩展的生态 1983 Turbo Pascal 发布，第一个真正的 IDE 1997 Microsoft Visual Studio 发布，为 C++/Visual Basic 语言提供先进的调试能力 1980 2030 2023 Cursor 发布，最早被广泛使用的 AI 原生 IDE 之一

## Slide 6

## Slide 6

Usage

用法

- 

- 

Bread-and-butter modes

日常主力模式

- 

- 

Inline

行内

- 

- 

Function

函数级

- 

- 

Single-ﬁle

单文件

- 

- 

Multi-ﬁle

多文件

- 

- 

True AI-native

真正的 AI 原生

- 

- 

Background agents

后台智能体

- 

- 

MCP

MCP

- 

- 

Learn memories

从记忆中学习

- 

- 

Bugbot (PR review) themodernsoftware.dev

Bugbot（PR 评审） themodernsoftware.dev

## Slide 7

## Slide 7

Let’s see some of this in action themodernsoftware.dev

来看看其中一些内容的实际效果 themodernsoftware.dev

## Slide 8

## Slide 8

How an AI IDE works under-the-hood themodernsoftware.dev Tab-complete

AI IDE 的内部工作原理 themodernsoftware.dev Tab 补全

- 

- 

Small context window around current code is encrypted

当前代码周围的小块上下文窗口会被加密

- 

- 

Server receives and runs inﬁlling LLM

服务器接收并运行填充用的 大语言模型（LLM）

- 

- 

Suggestion sent back and displayed Chat

建议被送回并显示 聊天

- 

- 

Store code chunks as embeddings in semantic index on server (obfuscated ﬁlename + code)

把代码块作为嵌入存储到服务器上的语义索引中 （文件名与代码均已混淆）

- 

- 

Any query retrieves most relevant chunks and feeds as context into LLM

任何查询都会检索最相关的代码块，并作为上下文送入 LLM

- 

- 

IDE regularly re-index code chunks and syncs embeddings

IDE 会定期重建代码块索引并同步嵌入

- 

- 

Chunk diffs are computed via Merkle trees for eﬃcient updates

代码块之间的差异（diff）通过 Merkle 树计算，以实现高效更新

## Slide 9

## Slide 9

- 

- 

For simple changes you don’t have to be too thoughtful about prompting

对于简单的改动，你不必在提示上过于费心

- 

- 

For more complex tasks, you’re going to become a product manager

对于更复杂的任务，你要变成一个产品经理

- 

- 

Carefully crafted specs doc themodernsoftware.dev Best practices

精心编写的规格文档 themodernsoftware.dev 最佳实践

## Slide 10

## Slide 10

- 

- 

Goal

目标

- 

- 

What is the purpose of the change

这次改动的目的是什么

- 

- 

Deﬁnitions

定义

- 

- 

What prereqs does the LLM need to know about the problem

LLM 需要了解这个问题的哪些前置条件

- 

- 

Plan

计划

- 

- 

High-level implementation breakdown

高层实现拆解

- 

- 

Source ﬁles being changed

涉及改动的源文件

- 

- 

What parts of the codebase are relevant and why

代码库中哪些部分是相关的，以及为什么

- 

- 

Test cases

测试用例

- 

- 

How will testing be done

测试将如何进行

- 

- 

Edge cases

边界情况

- 

- 

What special cases need to be accounted for

需要考虑哪些特殊情况

- 

- 

Out-of-scope

超出范围

- 

- 

What should *not* be changed

哪些内容*不*应该改动

- 

- 

Extensions

扩展

- 

- 

What changes will be relevant later so the LLM can future-proof its design and not take shortcuts themodernsoftware.dev Best practices

后续哪些改动会变得相关，从而让 LLM 做出前瞻性的设计而不走捷径 themodernsoftware.dev 最佳实践

## Slide 11

## Slide 11

Let’s see some of this in action themodernsoftware.dev

来看看其中一些内容的实际效果 themodernsoftware.dev

## Slide 12

## Slide 12

- 

- 

Optimize your codebase so that a human and an agent could understand what’s going on

优化你的代码库，让人类和智能体都能看懂正在发生什么

- 

- 

Much of LLM confusion comes from trying to ﬁnish a task with a messy repo as context

LLM 的许多困惑，都来自用凌乱的仓库作为上下文去完成任务

- 

- 

Provide optimal context for LLMs by describing

通过描述以下内容，为 LLM 提供最优上下文

- 

- 

Repo orientation

仓库导览

- 

- 

File structure

文件结构

- 

- 

Setup and environment

安装与环境

- 

- 

Best practices

最佳实践

- 

- 

Code style

代码风格

- 

- 

Access patterns

访问模式

- 

- 

APIs and contracts

API 与契约

- 

- 

All of this should be thoroughly documented

所有这些都应详尽记录成文档

- 

- 

Tip: a monorepo design in your repo is highly encouraged themodernsoftware.dev Best practices

提示： 强烈建议在仓库中采用 monorepo 设计 themodernsoftware.dev 最佳实践

## Slide 13

## Slide 13

- 

- 

Help LLM navigate your codebase with agent conﬁgurations

用智能体配置帮助 LLM 浏览你的代码库

- 

- 

claude.md ■ CLAUDE.md is a special file that Claude automatically pulls into context when starting a conversation. This makes it an ideal place for documenting: common bash commands, core files and utility functions, code style guidelines, testing instructions.

claude.md ■ CLAUDE.md 是一个特殊文件，Claude 在开始对话时会自动把它拉入上下文。因此它非常适合用来记录：常用的 bash 命令、核心文件与工具函数、代码风格指南以及测试说明。

- 

- 

c ursorrules

c ursorrules

- 

- 

AGENTS.md ■ Open format

AGENTS.md ■ 开放格式

- 

- 

llms.txt ■ Provide that navigation guidance for LLMs scraping the web

llms.txt ■ 为抓取网页的 LLM 提供这种导航指引

- 

- 

Note: The agents won’t always adhere to these descriptions/directives. They are intended as guidance. themodernsoftware.dev Best practices

注意： 智能体并不总会遵守这些描述与指令。这些内容只作指导之用。 themodernsoftware.dev 最佳实践

## Slide 14

## Slide 14

themodernsoftware.dev Samples

themodernsoftware.dev 示例

## Slide 15

## Slide 15

Let’s see some of this in action themodernsoftware.dev

来看看其中一些内容的实际效果 themodernsoftware.dev
