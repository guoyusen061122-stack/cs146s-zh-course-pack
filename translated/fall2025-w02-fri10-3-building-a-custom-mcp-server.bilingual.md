# Building a custom MCP server（fall2025 W2）

# 从零构建一个自定义 MCP 服务器（fall2025 W2）

## Slide 1

## Slide 1

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

## Slide 2

## Slide 2

To MCP and Beyond themodernsoftware.dev

走向 MCP 及更远处 themodernsoftware.dev

## Slide 3

## Slide 3

Why

为什么

- 

- 

LLMs have vast (but static) world knowledge that only updates when we retrain

大语言模型（LLM）拥有广博（但静态）的世界知识，只有重新训练时才会更新

- 

- 

To build fully autonomous systems we need robust ways to feed dynamic data in

要构建完全自主的系统，我们需要可靠的方式把动态数据喂进去

- 

- 

What’s the weather today

今天天气怎么样

- 

- 

Who’s president

谁是总统

- 

- 

What’s the price of Bitcoin

比特币价格多少

- 

- 

Who’s the narrator in Nike’s latest ad campaign

Nike 最新广告里的旁白是谁

- 

- 

RAG and tool-calling are the best answer we have today themodernsoftware.dev

RAG 和工具调用是我们目前最好的答案 themodernsoftware.dev

## Slide 4

## Slide 4

Basics

基础

- 

- 

M odel C ontext P rotocol

M odel C ontext P rotocol

- 

- 

Open protocol that allows systems to provide context to AI models in a manner generalizable across integrations ■ In English: standard format for exposing tools to LLMs

一种开放协议，让系统能够以可跨集成通用化的方式为 AI 模型提供上下文 ■ 用大白话讲：把工具暴露给 LLM 的标准格式

- 

- 

History: in the distant past pre-November 2024 when MCP was introduced… themodernsoftware.dev

历史：在遥远的过去，也就是 2024 年 11 月 MCP 被提出之前…… themodernsoftware.dev

## Slide 5

## Slide 5

themodernsoftware.dev ???? What APIs do you expose? Imagine integrating with a questionable 3rd party API

themodernsoftware.dev ???? 你暴露哪些 API？ 设想一下要集成一个不靠谱的第三方 API

## Slide 6

## Slide 6

themodernsoftware.dev ???? Now many APIs ???? ????

themodernsoftware.dev ???? 现在 API 很多 ???? ????

## Slide 7

## Slide 7

themodernsoftware.dev Now many LLM apps

themodernsoftware.dev 现在 LLM 应用很多

## Slide 8

## Slide 8

Basics

基础

- 

- 

MCP

MCP

- 

- 

Does away with the need to build M x N connectors from LLM host/agent to underlying tool ■ Don’t need to reimplement auth, error handling, rate-limiting, etc ■ Enforces consistent output format using JSON-RPC

免去了从 LLM 主机/智能体到底层工具构建 M x N 连接器的必要 ■ 不需要重新实现认证、错误处理、限流等 ■ 用 JSON-RPC 强制统一输出格式

- 

- 

Extends from Language Server Protocols ■ Allows for proactive agentic workﬂows rather than purely reactive ones as in LSP

从语言服务器协议扩展而来 ■ 支持主动的智能体化的工作流，而不是 LSP 那样纯粹被动的

- 

- 

Integrating with tools goes from M x N → M + N connectors themodernsoftware.dev

与工具集成从 M x N → M + N 个连接器 themodernsoftware.dev

## Slide 9

## Slide 9

MCP A Bit Deeper

MCP 再深入一点

- 

- 

Terminology

术语

- 

- 

Host : Cursor, Claude Desktop

Host ：Cursor、Claude Desktop

- 

- 

MCP Client : Library embedded on host (stateful session per server)

MCP Client ：嵌入主机中的库（每个服务器一个有状态会话）

- 

- 

MCP Server : Lightweight wrapper in front of a tool

MCP Server ：工具前方的一层轻量封装

- 

- 

Tool : Callable function (could be data source, API)

Tool ：可调用函数（可以是数据源、API）

- 

- 

Flow

流程

- 

- 

Client calls tools/list to MCP server (what can you do?)

客户端向 MCP 服务器调用 tools/list（你能做什么？）

- 

- 

Server returns JSON describing each tool (name, summary, JSON schema)

服务器返回描述每个工具的 JSON（名称、摘要、JSON schema）

- 

- 

Host injects that JSON into model’s context

主机把该 JSON 注入模型的上下文

- 

- 

User prompt triggers model, emitting a structured tool call

用户提示词触发模型，模型发出结构化的工具调用

- 

- 

MCP server executes and conversation resumes

MCP 服务器执行，对话继续

- 

- 

MCP provides stdio and SSE transport layer themodernsoftware.dev

MCP 提供 stdio 和 SSE 传输层 themodernsoftware.dev

## Slide 10

## Slide 10

themodernsoftware.dev MCP client Summarize my emails from Jack MCP server 1 Ask query 2 Get tools 3 Send query and pick tool with params 4 Call function for tool and get response Send response 5

themodernsoftware.dev MCP 客户端 帮我把 Jack 发来的邮件做个总结 MCP 服务器 1 发出查询 2 获取工具 3 发送查询并选定带参数的工具 4 调用工具对应函数并取得响应 发送响应 5

## Slide 11

## Slide 11

Let’s build a custom MCP server from scratch! themodernsoftware.dev

让我们从零构建一个自定义 MCP 服务器！ themodernsoftware.dev

## Slide 12

## Slide 12

Limitations

局限

- 

- 

Agents don’t handle many tools very well today

如今智能体处理大量工具的表现并不好

- 

- 

APIs eat up your context window quickly

API 会很快吃掉你的上下文窗口

- 

- 

Design APIs to be AI-native rather that rigid themodernsoftware.dev

把 API 设计成 AI 原生，而不是僵硬的形态 themodernsoftware.dev

## Slide 13

## Slide 13

themodernsoftware.dev Questions?

themodernsoftware.dev 有问题吗？
