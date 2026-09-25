# MCP Server SDK

# MCP TypeScript SDK

Important

**This is the `main` branch — v2 of the SDK** (`@modelcontextprotocol/server`, `@modelcontextprotocol/client`), implementing the [2026-07-28 MCP spec](https://modelcontextprotocol.io/specification/2026-07-28).

**Have feedback? Please [open a v2 issue](https://github.com/modelcontextprotocol/typescript-sdk/issues/new?template=v2-feedback.yml)** — it is the most useful thing you can do for the SDK right now. The [v2 documentation](https://ts.sdk.modelcontextprotocol.io/v2/) starts with a ten-minute server tutorial.

**v2 is the stable release line**, released alongside the 2026-07-28 spec. v1.x continues to receive bug fixes and security updates for at least 6 months after v2's release. v1 documentation: [ts.sdk.modelcontextprotocol.io](https://ts.sdk.modelcontextprotocol.io/) · v2: [`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/).

Warning

**We're limiting pull requests to 1 per new contributor while v2 settles after the [2026-07-28 spec](https://modelcontextprotocol.io/specification/2026-07-28) release.**

[Issues](https://github.com/modelcontextprotocol/typescript-sdk/issues/new?template=v2-feedback.yml) are the most useful feedback right now — we'll reopen PRs as v2 stabilizes.

[![NPM Version - Server](https://camo.githubusercontent.com/e7e672f8592e73357a364b99bbf21764d170d99af35c18ffadc881cd76274c7f/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f2534306d6f64656c636f6e7465787470726f746f636f6c2532467365727665723f6c6162656c3d2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)](https://www.npmjs.com/package/@modelcontextprotocol/server)[![NPM Version - Client](https://camo.githubusercontent.com/3bad587253ac498a80616c99c29bb5712c10acdf590f738793e225ac6ab07d23/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f2534306d6f64656c636f6e7465787470726f746f636f6c253246636c69656e743f6c6162656c3d2534306d6f64656c636f6e7465787470726f746f636f6c253246636c69656e74)](https://www.npmjs.com/package/@modelcontextprotocol/client)[![MIT licensed](https://camo.githubusercontent.com/d7d1d5c096046c443ea4d1c5ed7b3e446d4eb333ce9c1305e186746e454a0eab/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)](https://camo.githubusercontent.com/d7d1d5c096046c443ea4d1c5ed7b3e446d4eb333ce9c1305e186746e454a0eab/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)

Table of Contents

- Overview
- Packages
- Installation
- Getting Started
- Documentation
- Contributing
- License

## Overview

The Model Context Protocol (MCP) allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction.

This repository contains the TypeScript SDK implementation of the MCP specification. It runs on **Node.js**, **Bun**, and **Deno**, and ships:

- MCP **server** libraries (tools/resources/prompts, Streamable HTTP, stdio, auth helpers)
- MCP **client** libraries (transports, high-level helpers, OAuth helpers)
- Optional **middleware packages** for specific runtimes/frameworks (Express, Fastify, Hono, Node.js HTTP)
- Runnable **examples** (under [`examples/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples))

## Packages

This monorepo publishes split packages:

- **`@modelcontextprotocol/server`**: build MCP servers
- **`@modelcontextprotocol/client`**: build MCP clients

Tool and prompt schemas use [Standard Schema](https://standardschema.dev/) — bring Zod v4, Valibot, ArkType, or any compatible library.

### Middleware packages (optional)

The SDK also publishes small "middleware" packages under [`packages/middleware/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/packages/middleware) that help you **wire MCP into a specific runtime or web framework**.

They are intentionally thin adapters: they should not introduce new MCP functionality or business logic. See [`packages/middleware/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/README.md) for details.

- **`@modelcontextprotocol/node`**: Node.js Streamable HTTP transport wrapper for `IncomingMessage` / `ServerResponse`
- **`@modelcontextprotocol/express`**: Express helpers (app defaults + Host header validation)
- **`@modelcontextprotocol/fastify`**: Fastify helpers (app defaults + Host header validation)
- **`@modelcontextprotocol/hono`**: Hono helpers (app defaults + JSON body parsing hook + Host header validation)

## Installation

### Server

```
npm install @modelcontextprotocol/server
# or
bun add @modelcontextprotocol/server
# or
deno add npm:@modelcontextprotocol/server
```

### Client

```
npm install @modelcontextprotocol/client
# or
bun add @modelcontextprotocol/client
# or
deno add npm:@modelcontextprotocol/client
```

### Optional middleware packages

The SDK also publishes optional “middleware” packages that help you **wire MCP into a specific runtime or web framework** (for example Express, Fastify, Hono, or Node.js `http`).

These packages are intentionally thin adapters and should not introduce additional MCP features or business logic. See [`packages/middleware/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/README.md) for details.

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

Here is what an MCP server looks like. This minimal example exposes a single `greet` tool over stdio:

```
import{McpServer}from'@modelcontextprotocol/server';import{StdioServerTransport}from'@modelcontextprotocol/server/stdio';import*aszfrom'zod/v4';constserver=newMcpServer({name: 'greeting-server',version: '1.0.0'});server.registerTool('greet',{description: 'Greet someone by name',inputSchema: z.object({name: z.string()})},async({ name })=>({content: [{type: 'text',text: `Hello, ${name}!`}]}));asyncfunctionmain(){consttransport=newStdioServerTransport();awaitserver.connect(transport);}main();
```

Ready to build something real? Follow the step-by-step tutorials:

- [Build your first server](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-server.md) — a stdio weather-alert server, from `npm init` to a tool call
- [Build your first client](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-client.md) — connect to that server, list its tools, and call them

For runnable, end-to-end examples beyond the tutorials, see:

- [`examples/README.md`](/modelcontextprotocol/typescript-sdk/blob/main/examples/README.md) — runnable, self-verifying client/server example pairs (one story per directory)

## Documentation

- [Build a server](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-server.md) — your first MCP server, step by step
- [Build a client](/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-client.md) — your first MCP client, step by step
- [Documentation site](https://ts.sdk.modelcontextprotocol.io/v2/) — the full guides: tools, resources, prompts, serving over HTTP and stdio, clients, OAuth, and migration
- [Troubleshooting](/modelcontextprotocol/typescript-sdk/blob/main/docs/troubleshooting.md) — common errors and their fixes
- [API reference](https://ts.sdk.modelcontextprotocol.io/v2/api/)
- [MCP documentation](https://modelcontextprotocol.io/docs)
- [MCP specification](https://modelcontextprotocol.io/specification/latest)

### Building docs locally

To work on the documentation site locally:

```
pnpm docs:api      # Generate the API reference markdown (output: docs/api/)
pnpm docs:dev      # Start the VitePress dev server for the V2 site
pnpm docs:build    # Build the V2 site (output: docs/.vitepress/dist/)
pnpm docs:multi    # Build the combined V1 + V2 site (output: tmp/docs-combined/)
```

The `docs:multi` script builds the V2 site from the current checkout, checks out the `v1.x` branch via a git worktree to build the V1 site, and produces a combined site with V1 docs at the root and V2 docs under `/v2/`.

## v1 (legacy) documentation and fixes

If you are using the **v1** generation of the SDK, the **v1 API documentation** is available at [`https://ts.sdk.modelcontextprotocol.io/`](https://ts.sdk.modelcontextprotocol.io/). The v1 source code and any v1-specific fixes live on the long-lived [`v1.x` branch](https://github.com/modelcontextprotocol/typescript-sdk/tree/v1.x). V2 API docs are at [`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/).

## Contributing

Issues and pull requests are welcome on GitHub at [https://github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk).

## License

This project is licensed under the Apache License 2.0 for new contributions, with existing code under MIT. See the [LICENSE](/modelcontextprotocol/typescript-sdk/blob/main/LICENSE) file for details.
