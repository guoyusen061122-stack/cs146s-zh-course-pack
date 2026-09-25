# MCP 服务器 SDK

# MCP TypeScript SDK

重要提示

**这是 `main` 分支 —— SDK 的 v2 版本**（`@modelcontextprotocol/server`、`@modelcontextprotocol/client`），实现 [2026-07-28 MCP 规格](https://modelcontextprotocol.io/specification/2026-07-28)。

**有反馈意见？请[提交 v2 issue](https://github.com/modelcontextprotocol/typescript-sdk/issues/new?template=v2-feedback.yml)** —— 这是目前你能为 SDK 做的最有用的事。[v2 文档](https://ts.sdk.modelcontextprotocol.io/v2/) 从一份十分钟的服务端教程讲起。

**v2 是稳定发布线**，与 2026-07-28 规格一同发布。在 v2 发布后至少 6 个月内，v1.x 仍会继续收到缺陷修复与安全更新。v1 文档：[ts.sdk.modelcontextprotocol.io](https://ts.sdk.modelcontextprotocol.io/) · v2：[`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/)。

警告

**在 [2026-07-28 规格](https://modelcontextprotocol.io/specification/2026-07-28) 发布后 v2 逐步稳定期间，我们把每位新贡献者的拉取请求（PR）限制为 1 个。**

[Issues](https://github.com/modelcontextprotocol/typescript-sdk/issues/new?template=v2-feedback.yml) 是目前最有用的反馈 —— 等 v2 稳定下来，我们会重新开放 PR。

[![NPM 版本 - 服务端](https://camo.githubusercontent.com/e7e672f8592e73357a364b99bbf21764d170d99af35c18ffadc881cd76274c7f/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f2534306d6f64656c636f6e7465787470726f746f636f6c2532467365727665723f6c6162656c3d2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)](https://www.npmjs.com/package/@modelcontextprotocol/server)[![NPM 版本 - 客户端](https://camo.githubusercontent.com/3bad587253ac498a80616c99c29bb5712c10acdf590f738793e225ac6ab07d23/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f2534306d6f64656c636f6e7465787470726f746f636f6c253246636c69656e743f6c6162656c3d2534306d6f64656c636f6e7465787470726f746f636f6c253246636c69656e74)](https://www.npmjs.com/package/@modelcontextprotocol/client)[![MIT 许可](https://camo.githubusercontent.com/d7d1d5c096046c443ea4d1c5ed7b3e446d4eb333ce9c1305e186746e454a0eab/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)](https://camo.githubusercontent.com/d7d1d5c096046c443ea4d1c5ed7b3e446d4eb333ce9c1305e186746e454a0eab/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)

目录

- 总览
- 包
- 安装
- 快速开始
- 文档
- 贡献
- 许可

## 总览

模型上下文协议（MCP）让应用能够以标准化的方式为大语言模型（LLM）提供上下文，从而把提供上下文这件事与实际的大语言模型交互分离开来。

本仓库包含 MCP 规格的 TypeScript SDK 实现。它可运行在 **Node.js**、**Bun** 和 **Deno** 上，并提供：

- MCP **服务端**库（工具/资源/提示词、Streamable HTTP、stdio、认证辅助工具）
- MCP **客户端**库（传输层、高层辅助工具、OAuth 辅助工具）
- 面向特定运行时/框架的可选 **中间件包**（Express、Fastify、Hono、Node.js HTTP）
- 可运行的 **示例**（位于 [`examples/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples)）

## 包

这个 monorepo 以拆分后的包对外发布：

- **`@modelcontextprotocol/server`**：用于构建 MCP 服务器
- **`@modelcontextprotocol/client`**：用于构建 MCP 客户端

工具与提示词的模式使用 [Standard Schema](https://standardschema.dev/) —— 你可以带上 Zod v4、Valibot、ArkType 或任何兼容的库。

### 中间件包（可选）

SDK 还会在 [`packages/middleware/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/packages/middleware) 下发布一些小型的「中间件」包，帮助你 **把 MCP 接入特定的运行时或 Web 框架**。

它们刻意做成很薄的适配器：不应引入新的 MCP 功能或业务逻辑。详情见 [`packages/middleware/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/README.md)。

- **`@modelcontextprotocol/node`**：面向 `IncomingMessage` / `ServerResponse` 的 Node.js Streamable HTTP 传输封装
- **`@modelcontextprotocol/express`**：Express 辅助工具（应用默认配置 + Host 头校验）
- **`@modelcontextprotocol/fastify`**：Fastify 辅助工具（应用默认配置 + Host 头校验）
- **`@modelcontextprotocol/hono`**：Hono 辅助工具（应用默认配置 + JSON 请求体解析钩子 + Host 头校验）

## 安装

### 服务端

```
npm install @modelcontextprotocol/server
# or
bun add @modelcontextprotocol/server
# or
deno add npm:@modelcontextprotocol/server
```

### 客户端

```
npm install @modelcontextprotocol/client
# or
bun add @modelcontextprotocol/client
# or
deno add npm:@modelcontextprotocol/client
```

### 可选的中间件包

SDK 还会发布可选的「中间件」包，帮助你 **把 MCP 接入特定的运行时或 Web 框架**（例如 Express、Fastify、Hono 或 Node.js `http`）。

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

## 快速开始

下面是一个 MCP 服务器的样子。这个最小示例通过 stdio 暴露一个 `greet` 工具：

```
import{McpServer}from'@modelcontextprotocol/server';import{StdioServerTransport}from'@modelcontextprotocol/server/stdio';import*aszfrom'zod/v4';constserver=newMcpServer({name: 'greeting-server',version: '1.0.0'});server.registerTool('greet',{description: 'Greet someone by name',inputSchema: z.object({name: z.string()})},async({ name })=>({content: [{type: 'text',text: `Hello, ${name}!`}]}));asyncfunctionmain(){consttransport=newStdioServerTransport();awaitserver.connect(transport);}main();
```

准备好构建真正有用的东西了吗？请跟着分步教程操作：

- [构建你的第一个服务端](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-server.md) —— 一个基于 stdio 的天气预警服务器，从 `npm init` 到一次工具调用
- [构建你的第一个客户端](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-client.md) —— 连接到那个服务器，列出它的工具并调用它们

除教程之外，还想看可运行的端到端示例，请见：

- [`examples/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/examples/README.md) —— 可运行且可自校验的客户端/服务端示例对（每个目录一个故事）

## 文档

- [构建服务端](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-server.md) —— 你的第一个 MCP 服务器，分步讲解
- [构建客户端](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-client.md) —— 你的第一个 MCP 客户端，分步讲解
- [文档站点](https://ts.sdk.modelcontextprotocol.io/v2/) —— 完整指南：工具、资源、提示词、通过 HTTP 与 stdio 提供服务、客户端、OAuth 以及迁移
- [疑难解答](/modelcontextprotocol/typescript-sdk/blob/main/docs/troubleshooting.md) —— 常见错误及其修复方法
- [API 参考](https://ts.sdk.modelcontextprotocol.io/v2/api/)
- [MCP 文档](https://modelcontextprotocol.io/docs)
- [MCP 规格](https://modelcontextprotocol.io/specification/latest)

### 在本地构建文档

要在本地开发文档站点：

```
pnpm docs:api      # Generate the API reference markdown (output: docs/api/)
pnpm docs:dev      # Start the VitePress dev server for the V2 site
pnpm docs:build    # Build the V2 site (output: docs/.vitepress/dist/)
pnpm docs:multi    # Build the combined V1 + V2 site (output: tmp/docs-combined/)
```

`docs:multi` 脚本会基于当前检出内容构建 V2 站点，通过 git worktree 检出 `v1.x` 分支来构建 V1 站点，最终生成一个合并站点：V1 文档位于根路径，V2 文档位于 `/v2/` 下。

## v1（旧版）文档与修复

如果你使用的是 **v1** 这一代 SDK，**v1 API 文档**位于 [`https://ts.sdk.modelcontextprotocol.io/`](https://ts.sdk.modelcontextprotocol.io/)。v1 源代码以及任何 v1 专属修复都放在长期维护的 [`v1.x` 分支](https://github.com/modelcontextprotocol/typescript-sdk/tree/v1.x) 上。V2 API 文档位于 [`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/)。

## 贡献

欢迎在 GitHub 上通过 [https://github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) 提交 issue 和拉取请求。

## 许可

本项目的新贡献采用 Apache License 2.0 许可，既有代码采用 MIT 许可。详情见 [LICENSE](/modelcontextprotocol/typescript-sdk/blob/main/LICENSE) 文件。
