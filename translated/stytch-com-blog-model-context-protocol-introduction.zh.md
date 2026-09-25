# MCP 简介

#### 返回博客

# 模型上下文协议（MCP）：面向开发者的全面介绍

认证与身份

Mar 28, 2025

作者：Reed McGinley-Stempel

![模型上下文协议（MCP）：面向开发者的全面介绍](https://cdn.sanity.io/images/3jwyzebk/production/e3f8d6ac0106744a859c305e903837fa0c68108c-877x621.png?auto=format&fit=max&w=1920&q=75)

## 内容摘要

**模型上下文协议（MCP）** 是一项开放标准，把 AI 模型与外部数据和服务连接起来，让大语言模型（LLM）能以一致、安全的方式发起结构化 API 调用。本文会介绍 MCP，说明它在连接 AI 系统方面的价值，把它与 ChatGPT 插件、手工 API 集成等既有做法做比较，并深入到它近期对基于 OAuth 的认证的支持。我们也会看一点代码，观察 MCP 的实际运行。

MCP 充当 AI 工具与外部服务之间的万能适配器，免去了为每个工具或 API 编写定制集成代码的需要。就像 USB-C 简化了各种设备之间的连接，MCP 为 AI 模型提供了一种统一方式去调用外部函数、获取数据或使用预定义的提示词。其核心在于：MCP 用一个接口连接众多不同系统。

## 什么是模型上下文协议 MCP？

MCP 本质上是 AI 应用与外部工具或数据源之间的**万能适配器**。它[定义了一套通用协议](https://www.anthropic.com/news/model-context-protocol#:~:text=MCP%20addresses%20this%20challenge,to%20the%20data%20they%20need)（构建在 JSON-RPC 2.0 之上），让 AI 助手能以结构化方式调用外部服务的函数、获取数据或使用预定义的提示词。有了它，就不必为每个 API 或数据库在每个 LLM 应用里写定制代码，[MCP 为所有交互提供了一门标准化的「语言」。](https://medium.com/data-and-beyond/the-model-context-protocol-mcp-the-ultimate-guide-c40539e2a8e7#:~:text=https%3A%2F%2Fmodelcontextprotocol)

MCP 这一层让 AI 应用能够安全地访问外部数据源与工具并与之交互。它充当大语言模型（LLM）与各种数据库、应用或 API 之间的桥梁，无需大量定制编码即可实现顺畅的集成与功能。

MCP 用**客户端-服务器架构**实现这一点。这个由 AI 驱动的应用（例如聊天机器人、IDE 助手或智能体）充当*宿主*，运行一个 MCP *客户端*组件，而每个外部集成都作为一个 MCP *服务器*运行。服务器通过 MCP 协议暴露能力（如函数、数据资源或提示词模板），客户端连接它来使用这些能力。这种分离意味着 AI 模型并不直接与 API 对话，而是经过 MCP 客户端/服务器的握手，由后者来组织结构化的交换。

![MCP 服务器连接](https://cdn.sanity.io/images/3jwyzebk/production/da5293781d0d860d74d785ac249597d9e39af044-1026x629.png?auto=format&fit=max&w=3840&q=75)

[Source](https://generativeai.pub/mcp-servers-explained-python-and-agentic-ai-tool-integration-aa2ddca6cbe5)

## MCP 为何有价值

在传统做法里，把 AI 模型接到外部数据或操作上既繁琐又零散。开发者往往得为模型要用的每个 API 或数据库各写一套一次性集成，还要分别处理各自的认证、数据格式与错误处理。MCP 通过**把这些交互标准化**改变了局面。主要好处[包括](https://huggingface.co/blog/Kseniase/mcp#:~:text=,the%20client%20will%20pick%20on)：

- **快速集成工具**：有了 MCP，你可以直接接入新能力，而不必为每个能力从零写定制代码。假如某个 MCP 服务器已经存在，比如用于 Google Drive 或某个 SQL 数据库，那么任何兼容 MCP 的 AI 应用都能连上它并立刻获得那项能力。这对自动化来说是*巨大*的胜利 —— AI 智能体只需加上合适的服务器，就能按需获取文档、查询数据库或调用 API。这就像拥有一个现成「插件」库，而且它们都说同一种语言。MCP 服务器是轻量程序，通过标准化协议暴露特定能力，充当 Cursor 与各种外部工具或数据源之间的中介。
- **自主智能体**：MCP 让 AI 行为更自主。智能体不再受限于内置知识，它们可以在多步工作流中主动检索信息或执行操作。例如，一个复杂的智能体可以用 MCP 从 CRM 取数据，再通过通信工具发一封邮件，然后在数据库里记一条记录 —— 全都在一条顺畅的链路里完成。通过支持流畅、具备上下文感知的多步交互，MCP 帮助 AI 智能体更接近真正的自主任务执行。正如一位观察者所说，MCP 让 AI 从孤立的「大脑」变成多才多艺的「行动者」，因为它获得了对现实世界工具与数据的标准化访问。
- **减少摩擦与配置**：由于 MCP 充当通用接口，开发者不必再维护一堆彼此割裂的集成。一个应用只要支持 MCP，就能通过单一机制连接到任意数量的服务。每当你想让 AI 使用新 API 时，所需的手工配置大幅减少。团队可以把精力放在更高层的逻辑上，而不必第十次重写连接代码。用 Anthropic 的话说，MCP 用一套更简单、更可靠的单一协议取代了碎片化的集成，用于访问数据。
- **一致性与互操作性**：MCP 在各工具之间强制统一的请求/响应格式。这意味着你的 AI 应用不必为服务 A 处理一种 HTTP 响应、为服务 B 处理另一种 XML，等等。模型的输出（函数调用）与工具结果都以[统一的 JSON 结构](https://dev.to/fotiecodes/function-calling-vs-model-context-protocol-mcp-what-you-need-to-know-4nbo#:~:text=Purpose%20Converts%20user%20prompts%20into,Ensures%20interoperability%20across%20multiple%20tools)传递。这种一致性让调试与扩展都更容易。它也让你的集成逻辑更经得起未来变化 —— 即使更换底层模型供应商，MCP 面向工具的接口依然不变。
- **双向上下文**：与简单的 API 调用不同，MCP 支持在模型与工具之间维持上下文与持续对话。除了工具，MCP 服务器还能提供 *提示词*（面向特定任务的预定义提示词模板）与 *资源*（文档之类的数据上下文）。这意味着 AI 不仅能「调用 API」，还能摄入参考数据，或沿着服务器引导的复杂工作流行事。该协议的设计初衷就是支持丰富的交互，而不只是一次性查询。这在编码助手这类应用中尤其有用（AI 可以通过 MCP 与开发环境反复迭代），也适用于需要与各种数据源来回沟通的复杂决策任务。

简而言之，MCP 为增强 LLM 带来了**可扩展、即插即用的方式**。它让 AI 系统安全地取用所需的「活」数据与操作，而不必每个开发者都重新造轮子。MCP 的早期采用者已经为 Google Drive、Slack、GitHub、数据库等工具构建了服务器 —— 展示了 AI 智能体如何借助 MCP 与企业内容仓库、dev ops 工具以及其他现实系统协作。

## MCP 架构 —— 一眼看懂它的工作原理

### 客户端-服务器结构

MCP 遵循清晰的客户端-服务器架构：

- **MCP 客户端**：嵌入在 AI 应用中（聊天机器人、IDE 助手、自动化智能体）。
- **MCP 服务器**：暴露外部能力，如函数（工具）、资源（数据）与提示词（模板）。

所有交互都通过标准化的 JSON-RPC 消息进行，保持安全、结构化的交换：

**JSON-RPC 请求示例：**

例如，要列出可用工具，MCP 客户端会发出这样的请求：

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

服务器会回复一段结构化的 JSON，列出各个工具（每个都带名称、描述与输入 schema）。比如，服务器可能公开一个 get_weather 工具，并说明它需要哪些输入。

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    { "name": "get_weather", "description": "Retrieves weather data.", "schema": { "location": "string" } }
  ]
}
```

之后，当 LLM 决定使用某个工具时，客户端会发起一次调用。MCP 服务器执行该函数，并以结构化的 JSON 响应返回结果。MCP 客户端（位于宿主应用内）随后可以把该结果送回模型的上下文或响应中。在实践中，宿主应用中介了这一过程：它把 LLM 的意图（通常来自模型的函数调用输出）翻译成 MCP 请求，再把服务器返回的结构化结果交回 LLM。这种双向交换是**安全且受控的** —— 模型只能调用服务器暴露的那些特定工具，所有进出数据都经过既定协议。

## 构建与部署 MCP 服务器

构建与部署 MCP 服务器是把模型上下文协议（MCP）用于 AI 集成的关键一步。MCP 服务器充当 AI 模型与外部数据源或工具之间的中介，实现顺畅的通信与数据交换。MCP 的一大突出特点是服务器开发的灵活性。开发者可以使用任何能向 stdout 打印或提供 HTTP 端点的编程语言，从而自由选择偏好的语言与技术栈。

构建 MCP 服务器时，必须考虑架构与设计。MCP 遵循客户端-服务器架构，一个宿主应用可以连接多个服务器。这种架构带来可扩展性与灵活性，让开发者能够设计处理各类任务与功能的 MCP 服务器，例如数据处理、工具集成或 AI 模型管理。

MCP 服务器可以部署在各种环境里，包括本地开发环境、云平台或本地基础设施。例如，Cloudflare 提供了用于构建与部署远程 MCP 服务器的稳健平台，让 MCP 部署的管理与扩展更容易。这种灵活性确保 MCP 服务器能够按不同应用与环境的具体需求量身定制，无论是用于开发的本地环境，还是用于生产的云端方案。

只要关注良好的架构设计并利用 MCP 的灵活性，开发者就能构建强大、可扩展的 MCP 服务器，增强 AI 模型的能力，使其与外部数据源和工具顺畅交互。

## MCP 客户端与工具

MCP 客户端与工具是模型上下文协议生态中的必要组成部分。MCP 客户端是连接 MCP 服务器以访问外部数据源或工具的应用。这些客户端可以用 Python、JavaScript 或 Java 等各种编程语言与框架构建，让开发者能灵活选择最适合自身需求的工具。

另一方面，MCP 工具是为 MCP 客户端提供特定能力或功能的软件组件。这些工具可以集成到 MCP 服务器中，以实现数据处理、AI 模型管理或工具集成等功能。MCP 工具的例子包括 Claude Desktop，它提供与 AI 模型交互的聊天界面；以及 Cursor，它提供扩展 AI 能力的插件系统。

开发者可以构建定制的 MCP 客户端与工具，以满足特定用例或需求。这种灵活性让 MCP 生态中的创新与试验成为可能，开发者可以创造出令人兴奋的新应用。无论是用于数据分析的专用工具，还是集成多个 MCP 服务器的客户端应用，可能性都非常广阔。

借助 MCP 客户端与工具，开发者可以构建稳健而多样的应用，充分发挥 AI 模型的潜力，使其与各类外部数据源和工具顺畅交互。

## 把 MCP 与其他做法做比较

我们来比较几种在 MCP 之前或与它同时存在的做法：

- **定制集成与 API 密钥管理**：最常见的传统做法是为每个服务编写定制代码，并把凭据（API 密钥或 token）交给 LLM 去使用这些集成。例如，你可能写一个 Python 函数来查询某个 API，让 LLM 拥有调用该函数的能力，并在后端手工管理 API 密钥。这种做法耗费人力且难以扩展 —— 每个新数据源都要写新代码，每个环境都必须安全管理 API 密钥。由于每个集成都各不相同，系统往往很脆弱。相比之下，MCP 把这些交互集中并标准化：AI 智能体只需处理 MCP 协议，*任何* MCP 服务器（面向任何服务）都能以即插即用的方式工作。新增服务器完全不需要改动客户端代码。此外，MCP 为认证提供了正式结构（后文讨论），因此把 API 密钥交给 AI 不再是零散操作，而是走安全协议。
- **ChatGPT 插件（OpenAI 插件）**：2023 年，OpenAI 为 ChatGPT 引入了插件系统，允许模型调用由 OpenAPI 规格定义的外部 API。这是迈向标准化工具调用的早期一步，但存在局限。每个插件本质上都是自己的小型集成（有自己的 API schema 与认证），需要逐一构建与托管。只有某些平台（如 ChatGPT 或 Bing Chat）能用这些插件，因为它是专有做法。插件大多也是一次性调用 —— 模型调用一个 API 拿到信息，没有持久连接或持续交换。MCP 的不同之处在于它**开放且通用**（不绑定某一家供应商或某个界面），并支持丰富的双向交互与持续的上下文。可以把 ChatGPT 插件想成封闭工具箱里的专用工具，而 MCP 是任何开发者或 AI 平台都能使用的开放标准工具箱。MCP 标准化的认证（尤其是 OAuth）也意味着，它能以比 ChatGPT 体系中逐插件 OAuth 流程更统一的方式处理对用户数据的安全访问。总的来说，ChatGPT 插件展示了为 LLM 标准化 API 访问的价值，而 MCP 更进一步，把它变成开放协议，并让 AI 与服务之间能够维持持续的「对话」。
- **LLM 工具框架（LangChain、各类智能体库）**：在 MCP 之前，许多开发者用 LangChain 这类框架给模型提供工具。在这些方案里，你定义一组工具函数（带描述）以及智能体的提示逻辑，让 LLM 能决定是否使用它们。这样可行，但每个工具背后仍需定制实现 —— LangChain 最终在其库中维护了数百个工具集成。本质上，LangChain 提供的是*面向开发者*的标准（一种 Python 类接口），用于把工具集成进智能体的代码库，但没有任何东西让模型在运行时动态发现新工具。MCP 与这些框架互补，它把标准化转向*面向模型*。有了 MCP，智能体可以发现并使用某个 MCP 服务器提供的任何工具，即使智能体的代码事先并未显式包含该工具。事实上，LangChain 已经加入支持，可以把 MCP 服务器当作又一个工具来源 —— 这意味着用 LangChain 构建的智能体能轻松调用 MCP 工具，利用不断壮大的 MCP 服务器生态。区别在于，MCP 通过一种协议（JSON-RPC，带元数据等）把接口形式化，使其更容易接入不同环境，而不只是 Python 框架。类似地，OpenAI 的原生函数调用功能可以看作处理函数调用的*格式*（模型输出一个 JSON 函数调用），而 MCP 以标准化方式处理该调用的*执行*。OpenAI 的函数调用与 MCP 常常协同工作：LLM 产出结构化调用，MCP 客户端/服务器执行它并返回结果，二者结合实现了顺畅的工具调用。

本质上，MCP 并非第一次尝试把 LLM 与外部 API 连起来 —— 但它从过去的做法（插件、工具库等）中吸取经验，并统一了方案。它提供了**开放、与模型无关的协议**，简化了集成与认证。尤其在安全与认证方面，MCP 的设计（支持 OAuth）避免了逐插件密钥的拼凑，也避免了把原始 API 密钥交给模型。取而代之的是，认证可以作为协议的一部分，以一致、标准化的流程处理 —— 相比现状是重大进步。

## MCP 实战：技术深入剖析

我们一步步走一遍典型的 MCP 交互，以巩固对它的理解，并看一点代码。设想我们有一个 AI 助手，它想使用某个提供一组工具的 MCP 服务器（比方说，面向一个假想的「Neon」数据库服务）。高层流程是：

**1. 连接到 MCP 服务器** —— 宿主应用（AI 助手）初始化一个 MCP 客户端，并与服务器建立连接。视服务器位置而定，这可能通过本地进程（stdio）或远程 HTTP 流（SSE）进行。在底层，客户端发送一条 initialize [消息来握手协议版本与能力](https://nshipster.com/model-context-protocol/#:~:text=Like%20LSP%2C%20MCP%20has%20clients,The%20server%20responds%20in%20kind)。

**2. 发现可用工具/资源** —— 客户端接着查询服务器提供什么。如前所示，它可能发送 {"method": "tools/list"}，并拿回一份工具定义列表。助手可以用它来告知 LLM（例如把工具列表放进系统提示词，或通过模型的函数 schema，取决于具体实现）。例如，用某个 SDK 时，这可能就是一行代码：

```javascript
const tools = await mcpClient.request({ method: 'tools/list' }, ListToolsResultSchema);
```

它返回一份结构化的工具列表。每个工具条目都有名称、描述与输入的 JSON schema，[这样 AI 就知道自己能做什么](https://neon.tech/blog/building-a-cli-client-for-model-context-protocol-servers#:~:text=,can%20use%20during%20our%20interaction)。

**3. LLM 选择工具** —— 当用户向 AI 提出需要外部操作的问题时，LLM 会判断（通常借助提示工程或函数调用能力）应当使用某个工具。例如，用户问：*「AAPL 股票的最新价格是多少？」* LLM 看出应当调用 get_current_stock_price(company="AAPL", format="USD")。宿主应用捕获这一意图（例如 OpenAI 的函数调用 API 会以 JSON 返回函数名与参数）。

**4. 通过 MCP 调用工具** —— 客户端随即向服务器发送 tools/call 请求，带上选定的工具名与参数。前面我们看过这样的 JSON 示例。在代码中，用某个 SDK 可能写成：

```javascript
const result = await mcpClient.request({
    method: 'tools/call',
    params: { name: toolName, arguments: toolArgs }
}, CallToolResultSchema);
```

这会让服务器在它那一侧执行该工具的处理函数。服务器可能在调用外部 API、执行数据库查询，或完成该工具封装的任何逻辑。结果（可能是简单值，也可能是复杂的 JSON 对象）会通过 MCP 响应的 result 字段送回。

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
