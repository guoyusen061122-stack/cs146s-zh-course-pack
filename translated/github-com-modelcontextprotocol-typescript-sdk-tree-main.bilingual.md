# MCP Server SDK

# MCP 服务器 SDK

# MCP TypeScript SDK

# MCP TypeScript SDK

Important

重要提示

**This is the `main` branch — v2 of the SDK** (`@modelcontextprotocol/server`, `@modelcontextprotocol/client`), implementing the [2026-07-28 MCP spec](https://modelcontextprotocol.io/specification/2026-07-28).

**这是 `main` 分支 —— SDK 的 v2 版本**（`@modelcontextprotocol/server`、`@modelcontextprotocol/client`），实现 [2026-07-28 MCP 规格](https://modelcontextprotocol.io/specification/2026-07-28)。

**Have feedback? Please [open a v2 issue](https://github.com/modelcontextprotocol/typescript-sdk/issues/new?template=v2-feedback.yml)** — it is the most useful thing you can do for the SDK right now. The [v2 documentation](https://ts.sdk.modelcontextprotocol.io/v2/) starts with a ten-minute server tutorial.

**有反馈意见？请[提交 v2 issue](https://github.com/modelcontextprotocol/typescript-sdk/issues/new?template=v2-feedback.yml)** —— 这是目前你能为 SDK 做的最有用的事。[v2 文档](https://ts.sdk.modelcontextprotocol.io/v2/) 从一份十分钟的服务端教程讲起。

**v2 is the stable release line**, released alongside the 2026-07-28 spec. v1.x continues to receive bug fixes and security updates for at least 6 months after v2's release. v1 documentation: [ts.sdk.modelcontextprotocol.io](https://ts.sdk.modelcontextprotocol.io/) · v2: [`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/).

**v2 是稳定发布线**，与 2026-07-28 规格一同发布。在 v2 发布后至少 6 个月内，v1.x 仍会继续收到缺陷修复与安全更新。v1 文档：[ts.sdk.modelcontextprotocol.io](https://ts.sdk.modelcontextprotocol.io/) · v2：[`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/)。

Warning

警告

**We're limiting pull requests to 1 per new contributor while v2 settles after the [2026-07-28 spec](https://modelcontextprotocol.io/specification/2026-07-28) release.**

**在 [2026-07-28 规格](https://modelcontextprotocol.io/specification/2026-07-28) 发布后 v2 逐步稳定期间，我们把每位新贡献者的拉取请求（PR）限制为 1 个。**

[Issues](https://github.com/modelcontextprotocol/typescript-sdk/issues/new?template=v2-feedback.yml) are the most useful feedback right now — we'll reopen PRs as v2 stabilizes.

[Issues](https://github.com/modelcontextprotocol/typescript-sdk/issues/new?template=v2-feedback.yml) 是目前最有用的反馈 —— 等 v2 稳定下来，我们会重新开放 PR。

[![NPM Version - Server](https://camo.githubusercontent.com/e7e672f8592e73357a364b99bbf21764d170d99af35c18ffadc881cd76274c7f/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f2534306d6f64656c636f6e7465787470726f746f636f6c2532467365727665723f6c6162656c3d2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)](https://www.npmjs.com/package/@modelcontextprotocol/server)[![NPM Version - Client](https://camo.githubusercontent.com/3bad587253ac498a80616c99c29bb5712c10acdf590f738793e225ac6ab07d23/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f2534306d6f64656c636f6e7465787470726f746f636f6c253246636c69656e743f6c6162656c3d2534306d6f64656c636f6e7465787470726f746f636f6c253246636c69656e74)](https://www.npmjs.com/package/@modelcontextprotocol/client)[![MIT licensed](https://camo.githubusercontent.com/d7d1d5c096046c443ea4d1c5ed7b3e446d4eb333ce9c1305e186746e454a0eab/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)](https://camo.githubusercontent.com/d7d1d5c096046c443ea4d1c5ed7b3e446d4eb333ce9c1305e186746e454a0eab/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)

[![NPM 版本 - 服务端](https://camo.githubusercontent.com/e7e672f8592e73357a364b99bbf21764d170d99af35c18ffadc881cd76274c7f/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f2534306d6f64656c636f6e7465787470726f746f636f6c2532467365727665723f6c6162656c3d2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)](https://www.npmjs.com/package/@modelcontextprotocol/server)[![NPM 版本 - 客户端](https://camo.githubusercontent.com/3bad587253ac498a80616c99c29bb5712c10acdf590f738793e225ac6ab07d23/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f2534306d6f64656c636f6e7465787470726f746f636f6c253246636c69656e743f6c6162656c3d2534306d6f64656c636f6e7465787470726f746f636f6c253246636c69656e74)](https://www.npmjs.com/package/@modelcontextprotocol/client)[![MIT 许可](https://camo.githubusercontent.com/d7d1d5c096046c443ea4d1c5ed7b3e446d4eb333ce9c1305e186746e454a0eab/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)](https://camo.githubusercontent.com/d7d1d5c096046c443ea4d1c5ed7b3e446d4eb333ce9c1305e186746e454a0eab/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)

Table of Contents

目录

- Overview
- Packages
- Installation
- Getting Started
- Documentation
- Contributing
- License

- 总览
- 包
- 安装
- 快速开始
- 文档
- 贡献
- 许可

## Overview

## 总览

The Model Context Protocol (MCP) allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction.

模型上下文协议（MCP）让应用能够以标准化的方式为大语言模型（LLM）提供上下文，从而把提供上下文这件事与实际的大语言模型交互分离开来。

This repository contains the TypeScript SDK implementation of the MCP specification. It runs on **Node.js**, **Bun**, and **Deno**, and ships:

本仓库包含 MCP 规格的 TypeScript SDK 实现。它可运行在 **Node.js**、**Bun** 和 **Deno** 上，并提供：

- MCP **server** libraries (tools/resources/prompts, Streamable HTTP, stdio, auth helpers)
- MCP **client** libraries (transports, high-level helpers, OAuth helpers)
- Optional **middleware packages** for specific runtimes/frameworks (Express, Fastify, Hono, Node.js HTTP)
- Runnable **examples** (under [`examples/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples))

- MCP **服务端**库（工具/资源/提示词、Streamable HTTP、stdio、认证辅助工具）
- MCP **客户端**库（传输层、高层辅助工具、OAuth 辅助工具）
- 面向特定运行时/框架的可选 **中间件包**（Express、Fastify、Hono、Node.js HTTP）
- 可运行的 **示例**（位于 [`examples/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples)）

## Packages

## 包

This monorepo publishes split packages:

这个 monorepo 以拆分后的包对外发布：

- **`@modelcontextprotocol/server`**: build MCP servers
- **`@modelcontextprotocol/client`**: build MCP clients

- **`@modelcontextprotocol/server`**：用于构建 MCP 服务器
- **`@modelcontextprotocol/client`**：用于构建 MCP 客户端

Tool and prompt schemas use [Standard Schema](https://standardschema.dev/) — bring Zod v4, Valibot, ArkType, or any compatible library.

工具与提示词的模式使用 [Standard Schema](https://standardschema.dev/) —— 你可以带上 Zod v4、Valibot、ArkType 或任何兼容的库。

### Middleware packages (optional)

### 中间件包（可选）

The SDK also publishes small "middleware" packages under [`packages/middleware/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/packages/middleware) that help you **wire MCP into a specific runtime or web framework**.

SDK 还会在 [`packages/middleware/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/packages/middleware) 下发布一些小型的「中间件」包，帮助你 **把 MCP 接入特定的运行时或 Web 框架**。

They are intentionally thin adapters: they should not introduce new MCP functionality or business logic. See [`packages/middleware/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/README.md) for details.

它们刻意做成很薄的适配器：不应引入新的 MCP 功能或业务逻辑。详情见 [`packages/middleware/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/README.md)。

- **`@modelcontextprotocol/node`**: Node.js Streamable HTTP transport wrapper for `IncomingMessage` / `ServerResponse`
- **`@modelcontextprotocol/express`**: Express helpers (app defaults + Host header validation)
- **`@modelcontextprotocol/fastify`**: Fastify helpers (app defaults + Host header validation)
- **`@modelcontextprotocol/hono`**: Hono helpers (app defaults + JSON body parsing hook + Host header validation)

- **`@modelcontextprotocol/node`**：面向 `IncomingMessage` / `ServerResponse` 的 Node.js Streamable HTTP 传输封装
- **`@modelcontextprotocol/express`**：Express 辅助工具（应用默认配置 + Host 头校验）
- **`@modelcontextprotocol/fastify`**：Fastify 辅助工具（应用默认配置 + Host 头校验）
- **`@modelcontextprotocol/hono`**：Hono 辅助工具（应用默认配置 + JSON 请求体解析钩子 + Host 头校验）

## Installation

## 安装

### Server

### 服务端

```
npm install @modelcontextprotocol/server
# or
bun add @modelcontextprotocol/server
# or
deno add npm:@modelcontextprotocol/server
```

### Client

### 客户端

```
npm install @modelcontextprotocol/client
# or
bun add @modelcontextprotocol/client
# or
deno add npm:@modelcontextprotocol/client
```

### Optional middleware packages

### 可选的中间件包

The SDK also publishes optional “middleware” packages that help you **wire MCP into a specific runtime or web framework** (for example Express, Fastify, Hono, or Node.js `http`).

SDK 还会发布可选的「中间件」包，帮助你 **把 MCP 接入特定的运行时或 Web 框架**（例如 Express、Fastify、Hono 或 Node.js `http`）。

These packages are intentionally thin adapters and should not introduce additional MCP features or business logic. See [`packages/middleware/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/README.md) for details.

这些包刻意做成很薄的适配器，不应引入额外的 MCP 特性或业务逻辑。详情见 [`packages/middleware/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/README.md)。

```
# Node.js HTTP (IncomingMessage/ServerResponse) Streamable HTTP transport:
npm install @modelcontextprotocol/node

# Express integration:
npm install @modelcontextprotocol/express express

# Fastify integration:
npm install @modelcontextprotocol/fastify fastify

# Hono integration:
npm install @modelcontextprotocol/hono hono
```

## Getting Started

## 快速开始

Here is what an MCP server looks like. This minimal example exposes a single `greet` tool over stdio:

下面是一个 MCP 服务器的样子。这个最小示例通过 stdio 暴露一个 `greet` 工具：

```
import{McpServer}from'@modelcontextprotocol/server';import{StdioServerTransport}from'@modelcontextprotocol/server/stdio';import*aszfrom'zod/v4';constserver=newMcpServer({name: 'greeting-server',version: '1.0.0'});server.registerTool('greet',{description: 'Greet someone by name',inputSchema: z.object({name: z.string()})},async({ name })=>({content: [{type: 'text',text: `Hello, ${name}!`}]}));asyncfunctionmain(){consttransport=newStdioServerTransport();awaitserver.connect(transport);}main();
```

Ready to build something real? Follow the step-by-step tutorials:

准备好构建真正有用的东西了吗？请跟着分步教程操作：

- [Build your first server](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-server.md) — a stdio weather-alert server, from `npm init` to a tool call
- [Build your first client](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-client.md) — connect to that server, list its tools, and call them

- [构建你的第一个服务端](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-server.md) —— 一个基于 stdio 的天气预警服务器，从 `npm init` 到一次工具调用
- [构建你的第一个客户端](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-client.md) —— 连接到那个服务器，列出它的工具并调用它们

For runnable, end-to-end examples beyond the tutorials, see:

除教程之外，还想看可运行的端到端示例，请见：

- [`examples/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/examples/README.md) — runnable, self-verifying client/server example pairs (one story per directory)

- [`examples/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/examples/README.md) —— 可运行且可自校验的客户端/服务端示例对（每个目录一个故事）

## Documentation

## 文档

- [Build a server](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-server.md) — your first MCP server, step by step
- [Build a client](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-client.md) — your first MCP client, step by step
- [Documentation site](https://ts.sdk.modelcontextprotocol.io/v2/) — the full guides: tools, resources, prompts, serving over HTTP and stdio, clients, OAuth, and migration
- [Troubleshooting](/modelcontextprotocol/typescript-sdk/blob/main/docs/troubleshooting.md) — common errors and their fixes
- [API reference](https://ts.sdk.modelcontextprotocol.io/v2/api/)
- [MCP documentation](https://modelcontextprotocol.io/docs)
- [MCP specification](https://modelcontextprotocol.io/specification/latest)

- [构建服务端](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-server.md) —— 你的第一个 MCP 服务器，分步讲解
- [构建客户端](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-client.md) —— 你的第一个 MCP 客户端，分步讲解
- [文档站点](https://ts.sdk.modelcontextprotocol.io/v2/) —— 完整指南：工具、资源、提示词、通过 HTTP 与 stdio 提供服务、客户端、OAuth 以及迁移
- [疑难解答](/modelcontextprotocol/typescript-sdk/blob/main/docs/troubleshooting.md) —— 常见错误及其修复方法
- [API 参考](https://ts.sdk.modelcontextprotocol.io/v2/api/)
- [MCP 文档](https://modelcontextprotocol.io/docs)
- [MCP 规格](https://modelcontextprotocol.io/specification/latest)

### Building docs locally

### 在本地构建文档

To work on the documentation site locally:

要在本地开发文档站点：

```
pnpm docs:api      # Generate the API reference markdown (output: docs/api/)
pnpm docs:dev      # Start the VitePress dev server for the V2 site
pnpm docs:build    # Build the V2 site (output: docs/.vitepress/dist/)
pnpm docs:multi    # Build the combined V1 + V2 site (output: tmp/docs-combined/)
```

The `docs:multi` script builds the V2 site from the current checkout, checks out the `v1.x` branch via a git worktree to build the V1 site, and produces a combined site with V1 docs at the root and V2 docs under `/v2/`.

`docs:multi` 脚本会基于当前检出内容构建 V2 站点，通过 git worktree 检出 `v1.x` 分支来构建 V1 站点，最终生成一个合并站点：V1 文档位于根路径，V2 文档位于 `/v2/` 下。

## v1 (legacy) documentation and fixes

## v1（旧版）文档与修复

If you are using the **v1** generation of the SDK, the **v1 API documentation** is available at [`https://ts.sdk.modelcontextprotocol.io/`](https://ts.sdk.modelcontextprotocol.io/). The v1 source code and any v1-specific fixes live on the long-lived [`v1.x` branch](https://github.com/modelcontextprotocol/typescript-sdk/tree/v1.x). V2 API docs are at [`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/).

如果你使用的是 **v1** 这一代 SDK，**v1 API 文档**位于 [`https://ts.sdk.modelcontextprotocol.io/`](https://ts.sdk.modelcontextprotocol.io/)。v1 源代码以及任何 v1 专属修复都放在长期维护的 [`v1.x` 分支](https://github.com/modelcontextprotocol/typescript-sdk/tree/v1.x) 上。V2 API 文档位于 [`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/)。

## Contributing

## 贡献

Issues and pull requests are welcome on GitHub at [https://github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk).

欢迎在 GitHub 上通过 [https://github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) 提交 issue 和拉取请求。

## License

## 许可

This project is licensed under the Apache License 2.0 for new contributions, with existing code under MIT. See the [LICENSE](/modelcontextprotocol/typescript-sdk/blob/main/LICENSE) file for details.

本项目的新贡献采用 Apache License 2.0 许可，既有代码采用 MIT 许可。详情见 [LICENSE](/modelcontextprotocol/typescript-sdk/blob/main/LICENSE) 文件。
