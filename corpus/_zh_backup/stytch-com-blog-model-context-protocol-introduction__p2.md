**5. 把结果返回给 LLM** —— MCP 客户端收到工具的输出。此时宿主应用可以把结果整合回 AI 的回复中。在许多智能体配置中，做法是把结果注入对话，并让模型继续。例如，助手随后可能这样呈现：「AAPL 当前股价为 $173.22（USD）。」如果使用自动化循环，可以把结果交给模型（也许作为一条系统消息追加到对话中，例如「Result of get_current_stock_price:...」），模型便可以带着这条信息继续回答用户的提问。

下面是一个简化的示例，演示如何在对话中调用工具并使用结果，这里用的是 Anthropic 的 Claude（它原生支持工具调用）：

```javascript
// 1. Send user prompt to LLM with available tools context
const response = await anthropicClient.complete({
  prompt: "User: Can you list my projects?\nAssistant: ",
  model: "claude-3.5",
  tools: tools // list of tools from MCP server
});
for (const msg of response.messages) {
  if (msg.type === 'tool_use') {
    // 2. LLM decided to use a tool
    const { name, args } = msg;
    // 3. Call the tool via MCP
    const toolRes = await mcpClient.request({ method: 'tools/call', params: { name, arguments: args } });
    // 4. Inject tool result and resume LLM
    await anthropicClient.send({ role: 'system', content: `Tool result: ${toolRes.result}` });
  } else {
    // 5. Handle normal LLM reply (tool result likely integrated)
    console.log("Assistant:", msg.content);
  }
}
```

实际上，框架会替你处理其中大量工作，但上面的伪代码勾勒出 MCP 如何嵌入这个循环。关键点是：**MCP 提供了标准化的调用/响应层**用于执行工具，AI 智能体代码可以挂接进去。无论你用的是 OpenAI、Anthropic 还是其他大语言模型，MCP 都保持不变 —— 它是模型意图与外部动作之间的黏合剂。

借助 MCP，开发者能够获得一条清晰、结构化的流水线来扩展 AI 能力。代码变得更易维护（因为你在各处调用的是通用的 mcpClient.request，而不是针对每个服务写专门的代码），AI 也变得更强（因为它可以接入任何与 MCP 相连的服务）。调试同样更容易 —— 你可以监控 JSON-RPC 消息，精确看到请求和返回了什么，而不必从模型生成的文本里去猜线索。

## 早期局限（没有内置认证）

MCP 在 2024 年末刚出现时，提供了用于工具与数据交换的核心协议，但缺少连接远程服务器所需的标准化认证机制。在实践中，早期的 MCP 演示和实现往往要求把 MCP 服务器运行在**本地**或可信环境中，在那里认证并不算大问题（因为 AI 和服务器跑在同一台机器上）。例如，开发者可以在自己的 [localhost](http://localhost) 上运行一个访问 Google Drive 的 MCP 服务器，并预先拿到 token，然后让 AI 应用指向它。但如果没有正式的认证流程，要通过互联网或与第三方服务一起使用 MCP 就很棘手。

许多早期的 MCP 服务器都假定用户会在启动时手工向服务器提供凭据或 API key。举个例子，Anthropic 的快速入门建议通过配置或命令行提供你自己的凭据（API key、token），来运行预构建的服务器。这意味着服务器本身能拿到你的密钥，而 MCP 客户端只是信任那台服务器。这对个人或单用户场景可行，但对多用户应用或云端托管的智能体来说扩展性很差。当时并没有一个**标准握手**，让 AI 智能体能够说：「嘿，我获准代表用户 X 访问这项服务，这是我的凭据。」

本质上，早期的 MCP 客户端除了带外方式（比如预先共享一个 token，或者干脆在无认证的情况下运行）之外，没有办法向 MCP 服务器认证。这是一个明显的局限 —— **MCP 的设计初衷是开放、基于互联网的，但缺少认证标准，使安全的远程使用受到了限制**。

缺少认证标准意味着 **MCP 客户端无法自行安全地连接任意服务器**。你要么把客户端 ID/API key 硬编码进客户端（在分布式应用中并不理想），要么在无认证的情况下运行，并假定只有获授权的用户才能访问到服务器（通常靠把它保持在本地）。显然，要让 MCP 发挥全部潜力（例如以安全的方式把 AI 智能体连接到云端托管的数据源），需要更好的方案。好消息是社区认识到了这一点，并投入工作把基于 OAuth 的认证内建到 MCP 中。

### **OAuth 2.0 认证流程**

为了解决最初的认证局限并增强安全连接能力，MCP 采用了 OAuth 2.0 —— 一个被广泛认可且稳健的认证标准。OAuth 2.0 提供了安全、可扩展的框架，使 MCP 客户端能够安全地与远程服务器、云端托管资源以及多用户环境交互。把 OAuth 2.0 集成到 MCP 中的关键组成部分与收益包括：

1. **动态客户端注册（DCR）**：模型上下文协议支持动态客户端注册，允许客户端自动向 OAuth 服务器注册。这省去了手工配置客户端或硬编码凭据的需要，显著简化了开发者的部署工作。
1. **自动端点发现**：MCP 利用标准化元数据 URL（遵循 OAuth 的发现协议），让客户端能够自动发现 OAuth 端点。这降低了配置开销，使 MCP 部署更容易、更灵活。
1. **安全的授权与 token 管理**：客户端能够安全地获取精确匹配用户权限和访问范围的 OAuth token。这确保客户端只访问用户明确许可的资源，提升了安全性与合规性，在多用户和云环境中尤其如此。
1. **可扩展且安全的多用户支持**：OAuth 2.0 的设计本身就支持多个并发用户与服务，解决了 MCP 早期的一大显著局限。应用现在可以同时无缝处理大量用户的授权流程，这对云端的广泛采用至关重要。

## 调试与故障排查

调试与故障排查是使用 MCP 服务器和客户端时的关键环节。MCP 提供了多种调试与故障排查的工具和技术，确保开发者能够高效地定位并解决问题。这一过程中的关键工具之一是 MCP Inspector，一个面向 MCP 服务器的交互式调试工具。

MCP Inspector 让开发者可以测试和检查 MCP 服务器，定位并解决 MCP 服务器集成中的问题。该工具提供 MCP 客户端与服务器之间交互的详细视图，使定位问题、理解根本原因变得更容易。此外，MCP 还提供一份全面的调试指南，列出常见问题与解决方案，帮助开发者快速排查并解决问题。

调试 MCP 服务器时，考虑系统的架构与设计至关重要。开发者应当找出引发问题的具体组件或模块，并使用 MCP Inspector 这类工具来诊断和解决问题。专注于系统化的调试方法并善用现有工具，开发者就能确保自己的 MCP 集成稳健可靠。

## MCP 的实际应用

模型上下文协议（MCP）在各行各业和各个领域都有多种实际应用。MCP 的主要用例之一是 AI 集成，MCP 在其中实现 AI 模型与外部数据源或工具之间无缝的通信与数据交换。

MCP 可用于多种应用，例如：

- **构建 AI 驱动的聊天机器人**：这类聊天机器人可以访问外部数据源或工具，为用户提供准确且最新的信息。
- **创建 AI 驱动的工作流**：MCP 使 AI 模型能够与外部系统或数据源集成，自动完成复杂的工作流并提升效率。
- **开发 AI 模型**：这些模型可以与外部工具或数据源交互，增强自身能力，并给出更准确、更相关的输出。
- **实现 AI 驱动的自动化**：在金融、医疗或制造等行业，MCP 可以自动完成任务和流程，提升生产力并减少错误。

MCP 的灵活性与适应性，使它成为希望在自己的应用中利用 AI 与机器学习的开发者和组织的一个有吸引力的方案。通过为 AI 模型与数据源、工具的交互提供标准化接口，MCP 促成了 AI 生态中的创新与试验。这种标准化做法不仅简化了集成过程，也确保 AI 模型能够获取为发挥最佳表现所需的那些数据和工具。

总之，MCP 为 AI 应用打开了一片可能性的天地，让开发者能够构建更集成、更自主、更易扩展的方案。无论是用 AI 驱动的聊天机器人提升客户服务，还是在工业场景中自动完成复杂工作流，MCP 都提供了把这些创新落到实处所需的工具与框架。

## 结论

模型上下文协议（MCP）是 AI 开发中一个令人兴奋的进展，因为它让开发者能够安全、高效地把日益智能的语言模型连接到以往难以连接的广阔软件与数据世界。通过引入一套通用协议，MCP 让我们能够构建**更集成、更自主、更易扩展的 AI 系统**。我们不必为每个新工具编写一次性插件或给模型下脆弱的指令，而是有了一个连贯的框架：AI 智能体可以即席发现并使用工具，同时具备恰当的监督与安全保障。

虽然该协议仍在演进（认证是最近才加入的，而标准化服务器发现等更多特性也即将到来），但可以明确的是，MCP 或类似的东西将在下一代 AI 应用中扮演关键角色。对开发者而言，现在是熟悉 MCP 概念的大好时机。无论你是在用公司专属知识增强聊天机器人，还是在构建自动完成工作流的 AI 智能体，MCP 都能替你处理工具集成的「底层连接」工作，省下时间与麻烦。而且由于它是一个开放标准，背后有不断壮大的社区（以及 Anthropic 这样的公司）支持，它很可能会成为未来 AI 基础设施的一块基石。

总之，模型上下文协议让我们能够想象这样一个世界：AI 助手不再是孤立的天才，而是装备齐全的工程师和助手 —— 能够与众多系统对接、遵循流程、按需获取或创建信息，而这一切都通过一个统一、安全的接口完成。这是一个强大的愿景，而随着 MCP 的出现，它正在迅速成为现实。

在 Stytch，我们专注于为[解决远程 MCP 服务器认证问题](https://stytch.com/docs/guides/connected-apps/mcp-servers)提供便捷方案，让客户能够轻松为自己的应用搭建 MCP 服务器，从而让最终用户向 MCP 客户端授予有权限的访问。

### 用 Stytch 做 MCP 认证

使用 Stytch Connected Apps 为 MCP 服务器构建认证

阅读文档

分享这篇文章

[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fstytch.com%2Fblog%2Fmodel-context-protocol-introduction%2F)[X](https://x.com/intent/post?url=https%3A%2F%2Fstytch.com%2Fblog%2Fmodel-context-protocol-introduction%2F)[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fstytch.com%2Fblog%2Fmodel-context-protocol-introduction%2F)

# 相关文章

[![Stytch Connected Apps：让任何应用成为集成与 AI 智能体的 OAuth 提供方](https://cdn.sanity.io/images/3jwyzebk/production/e508e790c2042da91864ad821bfa2e329b91d4fe-1150x884.png?auto=format&fit=max&w=3840&q=75)](/blog/stytch-connected-apps/)[产品 2025 年 2 月 20 日 Stytch Connected Apps：让任何应用成为集成与 AI 智能体的 OAuth 提供方](/blog/stytch-connected-apps/)[![智能体体验的时代](https://cdn.sanity.io/images/3jwyzebk/production/debae5121d138d6b3358e3289e070b223092689e-1584x988.png?auto=format&fit=max&w=3840&q=75)](/blog/the-age-of-agent-experience/)[认证与身份 2025 年 2 月 8 日智能体体验的时代](/blog/the-age-of-agent-experience/)[![检测 AI 智能体的使用与滥用](https://cdn.sanity.io/images/3jwyzebk/production/4124b124a6f5ddebe133043163ce820536175e97-1088x902.png?auto=format&fit=max&w=3840&q=75)](/blog/detecting-ai-agent-use-abuse/)[认证与身份 2025 年 2 月 15 日检测 AI 智能体的使用与滥用](/blog/detecting-ai-agent-use-abuse/)

开始使用
Stytch

[免费开始构建](/start-now)[浏览我们的文档](/docs)

#### 认证与授权

[面向消费者应用](/b2c)[面向 B2B SaaS 应用](/b2b)[管理门户](/admin-portal)[Connected Apps](/connected-apps)[单点登录](/lp/sso)

#### 欺诈与风险防范

[设备指纹](/fraud)[主动风险评估](/docs/fraud/guides/device-fingerprinting/verdicts)[细粒度管控](/docs/fraud/guides/device-fingerprinting/traffic-shaping/intelligent-rate-limiting)

#### 为什么选择 Stytch

[Stytch 与 Auth0 对比](/stytch-vs-auth0)[Stytch 与 Firebase 对比](/stytch-vs-firebase)[Stytch 与 Cognito 对比](/stytch-vs-cognito)[Stytch 与 Fingerprint 对比](/stytch-vs-fingerprint)

#### 公司

[关于我们](/about)[招贤纳士](/careers)[联系我们](/contact)

#### 资源

[定价](/pricing)[文档](/docs)[更新日志](https://stytch.com/docs/resources/changelog)[API 状态](https://status.stytch.com/)[博客](/blog)

#### 社区

[Slack 社区](https://stytch.slack.com/join/shared_invite/zt-3aqo03e10-afWXyLzRIAlzGWJyF_~zHw)[客户案例](/customer-stories)

© 2020-2026 Stytch. 保留所有权利。

[使用条款](https://www.twilio.com/en-us/legal/tos)[隐私政策](https://www.twilio.com/en-us/legal/privacy)
