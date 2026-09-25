# MCP Server Authentication

# MCP 服务器认证

---

---

description: Deploy a remote MCP server on Cloudflare with optional authentication using Streamable HTTP transport. title: Build a Remote MCP server image: https://developers.cloudflare.com/og-docs.png

description: 使用 Streamable HTTP 传输在 Cloudflare 上部署远程 MCP 服务器，认证可选。 title: 构建远程 MCP 服务器 image: https://developers.cloudflare.com/og-docs.png

---

---

[Skip to content](#main-content)

[跳到正文](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/agents/llms.txt  
> Use this file to discover all available pages before exploring further.

> 文档索引  
> 在此获取完整文档索引：https://developers.cloudflare.com/agents/llms.txt  
> 在进一步浏览之前，可先用该文件发现所有可用页面。

# Build a Remote MCP server

# 构建远程 MCP 服务器

Last updated Jul 27, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

最后更新 Jul 27, 2026|复制为 Markdown| [以 Markdown 查看](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/index.md)| [智能体设置](https://developers.cloudflare.com/agent-setup/)

This guide shows how to deploy a remote MCP server on Cloudflare using [Streamable HTTP transport](https://developers.cloudflare.com/agents/model-context-protocol/protocol/transport/). You have two options:

本指南介绍如何用 [Streamable HTTP 传输](https://developers.cloudflare.com/agents/model-context-protocol/protocol/transport/)在 Cloudflare 上部署远程 MCP 服务器。你有两个选择：

- **Without authentication** — anyone can connect and use the server (no login required).
- **With [authentication and authorization](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/#add-authentication)** — users sign in before accessing tools, and you can control which tools an agent can call based on the user's permissions.

- **不带认证** —— 任何人都能连接并使用该服务器（无需登录）。
- **带[认证与授权](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/#add-authentication)** —— 用户先登录再访问工具，你可以根据用户权限控制智能体能调用哪些工具。

## Choosing an approach

## 选择一种方案

The Agents SDK provides multiple ways to create MCP servers. Choose the approach that fits your use case:

Agents SDK 提供多种创建 MCP 服务器的方式。请选择适合你用例的方案：

| Approach | Stateful? | Protocol path | Best for |
| --- | --- | --- | --- |
| [`createMcpHandler()`](https://developers.cloudflare.com/agents/model-context-protocol/apis/handler-api/) | No | stateless with legacy compatibility | New stateless tools |
| [`createLegacyMcpHandler()`](https://developers.cloudflare.com/agents/model-context-protocol/apis/handler-api/#createlegacymcphandler) | Optional | legacy | Temporary existing `WorkerTransport` routes |
| [`McpAgent`](https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/) | Yes | legacy | Deprecated Durable Object and RPC servers |
| Raw SDK transport | Depends on transport | Depends on SDK package | Custom transport ownership |

| 方案 | 有状态？ | 协议路径 | 最适合 |
| --- | --- | --- | --- |
| [`createMcpHandler()`](https://developers.cloudflare.com/agents/model-context-protocol/apis/handler-api/) | 否 | 无状态，兼容旧版 | 新的无状态工具 |
| [`createLegacyMcpHandler()`](https://developers.cloudflare.com/agents/model-context-protocol/apis/handler-api/#createlegacymcphandler) | 可选 | 旧版 | 临时沿用现有的 `WorkerTransport` 路由 |
| [`McpAgent`](https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/) | 是 | 旧版 | 已弃用的 Durable Object 与 RPC 服务器 |
| 原生 SDK 传输 | 取决于传输方式 | 取决于 SDK 包 | 自行掌控传输 |

Use `createMcpHandler` for a new stateless server. An existing `McpAgent` without legacy stateful dependencies can migrate directly. If it uses MCP session state, RPC, pushed requests, streams, or replay, plan the stateless equivalents and serve stateless and legacy lanes during the transition. Refer to [Migrate to MCP SDK v2](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/) for the staged rollout.

新服务器请用 `createMcpHandler` 构建无状态实现。若现有 `McpAgent` 不依赖旧版有状态能力，可直接迁移。若它用到了 MCP 会话状态、RPC、推送请求、流或重放，请先规划好对应的无状态实现，并在过渡期内同时提供无状态通道与旧版通道。分阶段上线的做法参见[迁移到 MCP SDK v2](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/)。

## Deploy your first MCP server

## 部署你的第一个 MCP 服务器

Template protocol path

模板协议路径

The quick-deploy templates in this section still use the deprecated `McpAgent` path. Do not use that path for a new server. Start with the [`mcp-worker` example ↗](https://github.com/cloudflare/agents/tree/main/examples/mcp-worker). If an existing template deployment needs sessionful behavior, add a stateless route and follow the [migration guide](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/).

本节的快速部署模板仍在使用已弃用的 `McpAgent` 路径。新服务器不要走这条路。请从 [`mcp-worker` 示例 ↗](https://github.com/cloudflare/agents/tree/main/examples/mcp-worker)开始。如果现有模板部署需要会话化行为，请新增一条无状态路由并遵循[迁移指南](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/)。

You can start by deploying a [public MCP server ↗](https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-authless) without authentication, then add user authentication and scoped authorization later. If you already know your server will require authentication, you can skip ahead to the [next section](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/#add-authentication).

你可以先部署一个不带认证的[公开 MCP 服务器 ↗](https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-authless)，之后再补上用户认证与范围化授权。如果你已经确定该服务器需要认证，可以跳到[下一节](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/#add-authentication)。

### Via the dashboard

### 通过仪表盘

The button below will guide you through everything you need to do to deploy an [example MCP server ↗](https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-authless) to your Cloudflare account:

下面的按钮会引导你完成把一个[示例 MCP 服务器 ↗](https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-authless)部署到 Cloudflare 账户所需的全部操作：

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-authless)

[![部署到 Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-authless)

Once deployed, this server will be live at your `workers.dev` subdomain (for example, `remote-mcp-server-authless.your-account.workers.dev/mcp`). You can connect to it immediately using the [AI Playground ↗](https://playground.ai.cloudflare.com/) (a remote MCP client), [MCP inspector ↗](https://github.com/modelcontextprotocol/inspector) or [other MCP clients](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/#connect-from-an-mcp-client-via-a-local-proxy).

部署完成后，该服务器会运行在你的 `workers.dev` 子域上（例如 `remote-mcp-server-authless.your-account.workers.dev/mcp`）。你可以立刻用 [AI Playground ↗](https://playground.ai.cloudflare.com/)（一个远程 MCP 客户端）、[MCP inspector ↗](https://github.com/modelcontextprotocol/inspector)或[其他 MCP 客户端](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/#connect-from-an-mcp-client-via-a-local-proxy)连接它。

A new git repository will be set up on your GitHub or GitLab account for your MCP server, configured to automatically deploy to Cloudflare each time you push a change or merge a pull request to the main branch of the repository. You can clone this repository, [develop locally](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/#via-the-cli), and start customizing the MCP server with your own [tools](https://developers.cloudflare.com/agents/model-context-protocol/protocol/tools/).

系统会在你的 GitHub 或 GitLab 账户上为该 MCP 服务器新建一个 git 仓库，并配置为每次推送改动或把拉取请求合并到仓库主分支时自动部署到 Cloudflare。你可以克隆这个仓库，[在本地开发](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/#via-the-cli)，并开始用自己的[工具](https://developers.cloudflare.com/agents/model-context-protocol/protocol/tools/)定制该 MCP 服务器。

### Via the CLI

### 通过 CLI

You can use the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler) to create a new MCP Server on your local machine and deploy it to Cloudflare.

你可以用 [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler)在本机创建新的 MCP 服务器，再把它部署到 Cloudflare。

1. Open a terminal and run the following command:npmyarnpnpm

1. 打开终端并运行以下命令：npmyarnpnpm

```
   npm create cloudflare@latest -- remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
```

```
   yarn create cloudflare remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
```

```
   pnpm create cloudflare@latest remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
```

During setup, select the following options: - For *Do you want to add an AGENTS.md file to help AI coding tools understand Cloudflare APIs?*, choose `No`. - For *Do you want to use git for version control?*, choose `No`. - For *Do you want to deploy your application?*, choose `No` (we will be testing the server before deploying).

安装过程中请选择以下选项： - 对于 *Do you want to add an AGENTS.md file to help AI coding tools understand Cloudflare APIs?*，选择 `No`。 - 对于 *Do you want to use git for version control?*，选择 `No`。 - 对于 *Do you want to deploy your application?*，选择 `No`（我们会先测试服务器再部署）。

Now, you have the MCP server setup, with dependencies installed.

现在 MCP 服务器已经搭好，依赖也已安装。

1. Move into the project folder:

1. 进入项目文件夹：

```sh
   cd remote-mcp-server-authless
```

1. In the directory of your new project, run the following command to start the development server:

1. 在新项目所在目录中运行以下命令，启动开发服务器：

```sh
   npm start
```

```sh
   ⎔ Starting local server...
   [wrangler:info] Ready on http://localhost:8788
```

Check the command output for the local port. In this example, the MCP server runs on port `8788`, and the MCP endpoint URL is `http://localhost:8788/mcp`.

请查看命令输出中的本地端口。在本例中，MCP 服务器运行在端口 `8788` 上，MCP 端点 URL 为 `http://localhost:8788/mcp`。

Note

注意

You cannot interact with the MCP server by opening the `/mcp` URL directly in a web browser. The `/mcp` endpoint expects an MCP client to send MCP protocol messages, which a browser does not do by default. In the next step, we will demonstrate how to connect to the server using an MCP client.

你无法通过在 Web 浏览器中直接打开 `/mcp` URL 来与 MCP 服务器交互。`/mcp` 端点期待 MCP 客户端发送 MCP 协议消息，而浏览器默认不会这么做。下一步我们将演示如何用 MCP 客户端连接该服务器。

1. To test the server locally:
1. In a new terminal, run the [MCP inspector ↗](https://github.com/modelcontextprotocol/inspector). The MCP inspector is an interactive MCP client that allows you to connect to your MCP server and invoke tools from a web browser.

1. 在本地测试该服务器：
1. 在一个新终端中运行 [MCP inspector ↗](https://github.com/modelcontextprotocol/inspector)。MCP inspector 是一个交互式 MCP 客户端，让你可以从 Web 浏览器连接自己的 MCP 服务器并调用工具。

```sh
      npx @modelcontextprotocol/inspector@latest
```

```sh
      🚀 MCP Inspector is up and running at:
      	http://localhost:5173/?MCP_PROXY_AUTH_TOKEN=46ab..cd3

      🌐 Opening browser...
```

The MCP Inspector will launch in your web browser. You can also launch it manually by opening a browser and going to `http://localhost:<PORT>`. Check the command output for the local port where MCP Inspector is running. In this example, MCP Inspector is served on port `5173`.

MCP Inspector 会在你的 Web 浏览器中启动。你也可以手动启动它：打开浏览器并访问 `http://localhost:<PORT>`。请查看命令输出中 MCP Inspector 运行的本地端口。在本例中，MCP Inspector 服务于端口 `5173`。

1. In the MCP inspector, enter the URL of your MCP server ( `http://localhost:8788/mcp`), and select **Connect**. Select **List Tools** to show the tools that your MCP server exposes.
1. You can now deploy your MCP server to Cloudflare. From your project directory, run:

1. 在 MCP inspector 中输入你的 MCP 服务器 URL（`http://localhost:8788/mcp`），然后选择 **Connect**。选择 **List Tools** 即可看到你的 MCP 服务器对外暴露的工具。
1. 现在你可以把 MCP 服务器部署到 Cloudflare。在项目目录中运行：

```sh
   npx wrangler@latest deploy
```

If you have already [connected a git repository](https://developers.cloudflare.com/workers/ci-cd/builds/) to the Worker with your MCP server, you can deploy your MCP server by pushing a change or merging a pull request to the main branch of the repository.

如果你已经把 [git 仓库](https://developers.cloudflare.com/workers/ci-cd/builds/)连接到承载 MCP 服务器的 Worker，那么只要推送改动或把拉取请求合并到仓库主分支，就能完成部署。

The MCP server will be deployed to your `*.workers.dev` subdomain at `https://remote-mcp-server-authless.your-account.workers.dev/mcp`.

MCP 服务器会被部署到你的 `*.workers.dev` 子域，地址为 `https://remote-mcp-server-authless.your-account.workers.dev/mcp`。

1. To test the remote MCP server, take the URL of your deployed MCP server ( `https://remote-mcp-server-authless.your-account.workers.dev/mcp`) and enter it in the MCP inspector running on `http://localhost:5173`.

1. 要测试这个远程 MCP 服务器，请取已部署服务器的 URL（`https://remote-mcp-server-authless.your-account.workers.dev/mcp`），填入运行在 `http://localhost:5173` 的 MCP inspector。

You now have a remote MCP server that MCP clients can connect to.

现在你有了一个可供 MCP 客户端连接的远程 MCP 服务器。

## Connect from an MCP client via a local proxy

## 通过本地代理从 MCP 客户端连接

Now that your remote MCP server is running, you can use the [`mcp-remote` local proxy ↗](https://www.npmjs.com/package/mcp-remote) to connect Claude Desktop or other MCP clients to it — even if your MCP client does not support remote transport or authorization on the client side. This lets you test what an interaction with your remote MCP server will be like with a real MCP client.

远程 MCP 服务器已经跑起来了，你可以用 [`mcp-remote` 本地代理 ↗](https://www.npmjs.com/package/mcp-remote)把 Claude Desktop 或其他 MCP 客户端连上去 —— 即便你的 MCP 客户端本身不支持远程传输或客户端侧授权也没关系。这样你就能用真实的 MCP 客户端试出与该远程 MCP 服务器交互的效果。

For example, to connect from Claude Desktop:

例如，要从 Claude Desktop 连接：

1. Update your Claude Desktop configuration to point to the URL of your MCP server:

1. 更新 Claude Desktop 配置，指向你的 MCP 服务器 URL：

```json
   {
   	"mcpServers": {
   		"math": {
   			"command": "npx",
   			"args": [
   				"mcp-remote",
   				"https://remote-mcp-server-authless.your-account.workers.dev/mcp"
   			]
   		}
   	}
   }
```

1. Restart Claude Desktop to load the MCP Server. Once this is done, Claude will be able to make calls to your remote MCP server.
1. To test, ask Claude to use one of your tools. For example:

1. 重启 Claude Desktop 以加载该 MCP 服务器。完成后，Claude 就能调用你的远程 MCP 服务器了。
1. 要测试，请让 Claude 使用你的某个工具。例如：

```txt
   Could you use the math tool to add 23 and 19?
```

Claude should invoke the tool and show the result generated by the remote MCP server.

Claude 应当调用该工具，并显示远程 MCP 服务器生成的结果。

To learn how to use remote MCP servers with other MCP clients, refer to [Test a Remote MCP Server](https://developers.cloudflare.com/agents/model-context-protocol/guides/test-remote-mcp-server/).

要了解如何配合其他 MCP 客户端使用远程 MCP 服务器，请参阅[测试远程 MCP 服务器](https://developers.cloudflare.com/agents/model-context-protocol/guides/test-remote-mcp-server/)。

## Add Authentication

## 添加认证

The public MCP server example you deployed earlier allows any client to connect and invoke tools without logging in. To add user authentication to your MCP server, you can integrate Cloudflare Access or a third-party service as the OAuth provider. Your MCP server handles secure login flows and issues access tokens that MCP clients can use to make authenticated tool calls. Users sign in with the OAuth provider and grant their AI agent permission to interact with the tools exposed by your MCP server, using scoped permissions.

你之前部署的公开 MCP 服务器示例允许任何客户端在未登录的情况下连接并调用工具。要为 MCP 服务器添加用户认证，可以接入 Cloudflare Access 或第三方服务作为 OAuth 提供方。你的 MCP 服务器负责处理安全登录流程，并签发访问令牌，供 MCP 客户端发起经过认证的工具调用。用户通过 OAuth 提供方登录，并授予其 AI 智能体以范围化权限与你的 MCP 服务器所暴露工具交互的许可。

### Cloudflare Access OAuth

### Cloudflare Access OAuth

You can configure your MCP server to require user authentication through Cloudflare Access. Cloudflare Access acts as an identity aggregator and verifies user emails, signals from your existing [identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) (such as GitHub or Google), and other attributes such as IP address or device certificates. When users connect to the MCP server, they will be prompted to log in to the configured identity provider and are only granted access if they pass your [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#selectors).

你可以把 MCP 服务器配置为要求通过 Cloudflare Access 进行用户认证。Cloudflare Access 充当身份聚合器，校验用户邮箱、来自你现有[身份提供方](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)（例如 GitHub 或 Google）的信号，以及 IP 地址、设备证书等其他属性。用户连接 MCP 服务器时，会被提示登录所配置的身份提供方，且只有通过你的 [Access 策略](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#selectors)才会获得访问权限。

For a step-by-step deployment guide, refer to [Secure MCP servers with Access for SaaS](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/).

分步部署指南请参阅[用 Access for SaaS 保护 MCP 服务器](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/)。

### Third-party OAuth

### 第三方 OAuth

You can connect your MCP server with any [OAuth provider](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/#2-third-party-oauth-provider) that supports the OAuth 2.0 specification, including GitHub, Google, Slack, [Stytch](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/#stytch), [Auth0](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/#auth0), [WorkOS](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/#workos), and more.

你可以让 MCP 服务器接入任何支持 OAuth 2.0 规格的 [OAuth 提供方](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/#2-third-party-oauth-provider)，包括 GitHub、Google、Slack、[Stytch](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/#stytch)、[Auth0](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/#auth0)、[WorkOS](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/#workos) 等。

The following example demonstrates how to use GitHub as an OAuth provider.

下面的示例演示如何把 GitHub 用作 OAuth 提供方。

#### Step 1 — Create a new MCP server

#### 第 1 步 —— 创建新的 MCP 服务器

Run the following command to create a new MCP server with GitHub OAuth:

运行以下命令，创建一个使用 GitHub OAuth 的 MCP 服务器：

npmyarnpnpm

npmyarnpnpm

```
npm create cloudflare@latest -- my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
```

```
yarn create cloudflare my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
```

```
pnpm create cloudflare@latest my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
```

Now, you have the MCP server setup, with dependencies installed. Move into that project folder:

现在 MCP 服务器已经搭好，依赖也已安装。进入该项目文件夹：

```sh
cd my-mcp-server-github-auth
```

You'll notice that in the example MCP server, if you open `src/index.ts`, the primary difference is that the `defaultHandler` is set to the `GitHubHandler`:

你会注意到，在这个示例 MCP 服务器中，如果打开 `src/index.ts`，最主要的区别是 `defaultHandler` 被设置为 `GitHubHandler`：

```ts
import GitHubHandler from "./github-handler";

export default new OAuthProvider({
	apiRoute: "/mcp",
	apiHandler: MyMCP.serve("/mcp"),
	defaultHandler: GitHubHandler,
	authorizeEndpoint: "/authorize",
	tokenEndpoint: "/token",
	clientRegistrationEndpoint: "/register",
});
```

This ensures that your users are redirected to GitHub to authenticate. To get this working though, you need to create OAuth client apps in the steps below.

这确保你的用户会被重定向到 GitHub 完成认证。不过要让它跑起来，你还需要按下面的步骤创建 OAuth 客户端应用。

#### Step 2 — Create an OAuth App

#### 第 2 步 —— 创建一个 OAuth 应用

You'll need to create two [GitHub OAuth Apps ↗](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) to use GitHub as an authentication provider for your MCP server — one for local development, and one for production.

你需要创建两个 [GitHub OAuth 应用 ↗](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)，才能把 GitHub 用作 MCP 服务器的认证提供方 —— 一个用于本地开发，一个用于生产环境。

#### Step 2.1 — Create a new OAuth App for local development

#### 第 2.1 步 —— 为本地开发创建一个新的 OAuth 应用

1. Navigate to [github.com/settings/developers ↗](https://github.com/settings/developers) to create a new OAuth App with the following settings:
1. **Application name**: `My MCP Server (local)`
1. **Homepage URL**: `http://localhost:8788`
1. **Authorization callback URL**: `http://localhost:8788/callback`
1. For the OAuth app you just created, add the client ID of the OAuth app as `GITHUB_CLIENT_ID` and generate a client secret, adding it as `GITHUB_CLIENT_SECRET` to a `.env` file in the root of your project, which [will be used to set secrets in local development](https://developers.cloudflare.com/workers/configuration/secrets/).

1. 前往 [github.com/settings/developers ↗](https://github.com/settings/developers)，用以下设置创建一个新的 OAuth 应用：
1. **应用名称**：`My MCP Server (local)`
1. **主页 URL**：`http://localhost:8788`
1. **授权回调 URL**：`http://localhost:8788/callback`
1. 对你刚创建的 OAuth 应用，把该应用的客户端 ID 添加为 `GITHUB_CLIENT_ID`，并生成客户端密钥，把它作为 `GITHUB_CLIENT_SECRET` 添加到项目根目录的 `.env` 文件中；该文件[会用于在本地开发中设置密钥](https://developers.cloudflare.com/workers/configuration/secrets/)。

```sh
   touch .env
   echo 'GITHUB_CLIENT_ID="your-client-id"' >> .env
   echo 'GITHUB_CLIENT_SECRET="your-client-secret"' >> .env
   cat .env
```

1. Run the following command to start the development server:

1. 运行以下命令启动开发服务器：

```sh
   npm start
```

Your MCP server is now running on `http://localhost:8788/mcp`.

你的 MCP 服务器现在运行在 `http://localhost:8788/mcp`。

1. In a new terminal, run the [MCP inspector ↗](https://github.com/modelcontextprotocol/inspector). The MCP inspector is an interactive MCP client that allows you to connect to your MCP server and invoke tools from a web browser.

1. 在一个新终端中运行 [MCP inspector ↗](https://github.com/modelcontextprotocol/inspector)。MCP inspector 是一个交互式 MCP 客户端，让你可以从 Web 浏览器连接自己的 MCP 服务器并调用工具。

```sh
   npx @modelcontextprotocol/inspector@latest
```

1. Open the MCP inspector in your web browser:

1. 在 Web 浏览器中打开 MCP inspector：

```sh
   open http://localhost:5173
```

1. In the inspector, enter the URL of your MCP server, `http://localhost:8788/mcp`
1. In the main panel on the right, click the **OAuth Settings** button and then click **Quick OAuth Flow**.

1. 在 inspector 中输入你的 MCP 服务器 URL，即 `http://localhost:8788/mcp`
1. 在右侧主面板中，点击 **OAuth Settings** 按钮，然后点击 **Quick OAuth Flow**。

You should be redirected to a GitHub login or authorization page. After authorizing the MCP Client (the inspector) access to your GitHub account, you will be redirected back to the inspector.

你应当会被重定向到 GitHub 的登录或授权页面。在授权 MCP 客户端（即 inspector）访问你的 GitHub 账户后，你会被重定向回 inspector。

1. Click **Connect** in the sidebar and you should see the "List Tools" button, which will list the tools that your MCP server exposes.

1. 点击侧边栏中的 **Connect**，你应该会看到 "List Tools" 按钮，它会列出你的 MCP 服务器暴露的工具。

#### Step 2.2 — Create a new OAuth App for production

#### 第 2.2 步 —— 为生产环境创建一个新的 OAuth 应用

You'll need to repeat [Step 2.1](#step-21--create-a-new-oauth-app-for-local-development) to create a new OAuth App for production.

你需要重复[第 2.1 步](#step-21--create-a-new-oauth-app-for-local-development)来创建一个用于生产环境的 OAuth 应用。

1. Navigate to [github.com/settings/developers ↗](https://github.com/settings/developers) to create a new OAuth App with the following settings:

1. 前往 [github.com/settings/developers ↗](https://github.com/settings/developers)，用以下设置创建一个新的 OAuth 应用：

- **Application name**: `My MCP Server (production)`
- **Homepage URL**: Enter the workers.dev URL of your deployed MCP server (ex: `worker-name.account-name.workers.dev`)
- **Authorization callback URL**: Enter the `/callback` path of the workers.dev URL of your deployed MCP server (ex: `worker-name.account-name.workers.dev/callback`)

- **应用名称**：`My MCP Server (production)`
- **主页 URL**：填入已部署 MCP 服务器的 workers.dev URL（例如 `worker-name.account-name.workers.dev`）
- **授权回调 URL**：填入已部署 MCP 服务器的 workers.dev URL 的 `/callback` 路径（例如 `worker-name.account-name.workers.dev/callback`）

1. For the OAuth app you just created, add the client ID and client secret, using Wrangler CLI:

1. 对你刚创建的 OAuth 应用，用 Wrangler CLI 添加客户端 ID 与客户端密钥：

```sh
npx wrangler secret put GITHUB_CLIENT_ID
```

```sh
npx wrangler secret put GITHUB_CLIENT_SECRET
```

```sh
npx wrangler secret put COOKIE_ENCRYPTION_KEY
```

Use any random string for `COOKIE_ENCRYPTION_KEY`, for example the output of `openssl rand -hex 32`.

`COOKIE_ENCRYPTION_KEY` 可用任意随机字符串，例如 `openssl rand -hex 32` 的输出。

Caution

注意

When you create the first secret, Wrangler will ask if you want to create a new Worker. Submit "Y" to create a new Worker and save the secret.

创建第一个密钥时，Wrangler 会询问你是否要新建一个 Worker。提交 "Y" 以新建 Worker 并保存该密钥。

1. Set up a KV namespace

1. 设置 KV 命名空间

a. Create the KV namespace:

a. 创建 KV 命名空间：

```bash
   npx wrangler kv namespace create "OAUTH_KV"
```

b. Update the `wrangler.jsonc` file with the resulting KV ID:

b. 用得到的 KV ID 更新 `wrangler.jsonc` 文件：

```json
   {
   	"kvNamespaces": [
   		{
   			"binding": "OAUTH_KV",
   			"id": "<YOUR_KV_NAMESPACE_ID>"
   		}
   	]
   }
```

1. Deploy the MCP server to your Cloudflare `workers.dev` domain:

1. 把 MCP 服务器部署到你的 Cloudflare `workers.dev` 域：

```bash
   npm run deploy
```

1. Connect to your server running at `worker-name.account-name.workers.dev/mcp` using the [AI Playground ↗](https://playground.ai.cloudflare.com/), MCP Inspector, or [other MCP clients](https://developers.cloudflare.com/agents/model-context-protocol/guides/test-remote-mcp-server/), and authenticate with GitHub.

1. 用 [AI Playground ↗](https://playground.ai.cloudflare.com/)、MCP Inspector 或[其他 MCP 客户端](https://developers.cloudflare.com/agents/model-context-protocol/guides/test-remote-mcp-server/)连接运行在 `worker-name.account-name.workers.dev/mcp` 的服务器，并用 GitHub 完成认证。

## Next steps

## 后续步骤

### [MCP Tools](https://developers.cloudflare.com/agents/model-context-protocol/protocol/tools/)

### [MCP 工具](https://developers.cloudflare.com/agents/model-context-protocol/protocol/tools/)

Add tools to your MCP server.

为你的 MCP 服务器添加工具。

### [Authorization](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/)

### [授权](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/)

Customize authentication and authorization.

自定义认证与授权。

Was this helpful?

这个页面有帮助吗？

YesNo

YesNo

## On this page

## 本页内容

[![](https://developers.cloudflare.com/_astro/logo.te5VL_aD.svg)Docs](https://developers.cloudflare.com/)

[![](https://developers.cloudflare.com/_astro/logo.te5VL_aD.svg)文档](https://developers.cloudflare.com/)

```json
{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/#page","headline":"Build a Remote MCP server","description":"Deploy a remote MCP server on Cloudflare with optional authentication using Streamable HTTP transport.","url":"https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","dateModified":"2026-07-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MCP"]}
```
