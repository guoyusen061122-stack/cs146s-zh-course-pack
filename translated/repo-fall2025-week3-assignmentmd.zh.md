# 第 3 周 — 构建自定义 MCP 服务器

设计并实现一个包装真实外部 API 的模型上下文协议（MCP）服务器。你可以：
- 在**本地**运行它（STDIO 传输），并与一个 MCP 客户端（如 Claude Desktop）集成。
- 或在**远程**运行它（HTTP 传输），并从某个模型智能体或客户端调用它。后者更难，但可获得额外加分。

按照 MCP Authorization 规范添加认证（API 密钥或 OAuth2）可获得额外加分。

## 学习目标
- 理解 MCP 的核心能力：工具、资源、提示词。
- 用带类型的参数和健壮的错误处理实现工具定义。
- 遵循日志与传输的最佳实践（STDIO 服务器不得使用 stdout）。
- 可选地，为 HTTP 传输实现授权流程。

## 要求
1. 选择一个外部 API，并记录你将使用哪些端点。示例：天气、GitHub issues、Notion 页面、影视数据库、日历、任务管理器、金融/加密货币、旅行、体育统计。
2. 至少暴露两个 MCP 工具
3. 实现基本的韧性：
 - 对 HTTP 失败、超时和空结果给出优雅的错误。
 - 遵守 API 速率限制（例如简单的退避，或向用户提示）。
4. 打包与文档：
 - 提供清晰的搭建说明、环境变量和运行命令。
 - 包含一个调用流程示例（在客户端中输入什么或点击什么来触发这些工具）。
5. 选择一种部署模式：
 - 本地：STDIO 服务器，可在你的机器上运行，并能被 Claude Desktop 或 Cursor 这类 AI IDE 发现。
 - 远程：可通过网络访问的 HTTP 服务器，能被感知 MCP 的客户端或智能体运行时调用。若能部署并可访问，可获得额外加分。
6. （可选）加分项：认证
 - 通过环境变量与客户端配置支持 API 密钥；或
 - 为 HTTP 传输支持 OAuth2 风格的持有者令牌（bearer token），校验令牌受众，绝不把令牌透传给上游 API。

## 交付物
- `week3/` 下的源代码（建议放在 `week3/server/`，并有清晰的入口，如 `main.py` 或 `app.py`）。
- `week3/README.md`，其中包含：
 - 前置条件、环境搭建与运行说明（本地和/或远程）。
 - 如何配置 MCP 客户端（本地场景以 Claude Desktop 为例）或远程场景下的智能体运行时。
 - 工具参考：名称、参数、示例输入/输出以及预期行为。

## 评分标准（总分 90 分）
- 功能（35）：实现 2 个以上工具、正确的 API 集成、有意义的输出。
- 可靠性（20）：输入校验、错误处理、日志、对速率限制的考虑。
- 开发者体验（20）：清晰的搭建/文档，易于在本地运行；合理的目录结构。
- 代码质量（15）：代码可读、命名有描述性、复杂度最小、在适用处使用类型标注。
- 额外加分（10）：
 - +5 远程 HTTP MCP 服务器，可被 OpenAI/Claude SDK 这类智能体/客户端调用。
 - +5 正确实现认证（API 密钥，或带受众校验的 OAuth2）。

## 有用参考
- MCP 服务器快速上手：[modelcontextprotocol.io/quickstart/server](https://modelcontextprotocol.io/quickstart/server)。 
*注意：你不能直接提交这个示例。*
- MCP 授权（HTTP）：[modelcontextprotocol.io/specification/2025-06-18/basic/authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- Cloudflare 上的远程 MCP（Agents）：[developers.cloudflare.com/agents/guides/remote-mcp-server/](https://developers.cloudflare.com/agents/guides/remote-mcp-server/)。部署前请使用 modelcontextprotocol inspector 工具在本地调试你的服务器。
- https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel 如果你选择做远程 MCP 部署，Vercel 是个不错的选择，还提供免费套餐。 