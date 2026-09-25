# Writing Effective Tools for Agents

# 为智能体编写高效工具

Engineering at Anthropic

Anthropic 工程团队

Published Sep 11, 2025

发布于 2025 年 9 月 11 日

Agents are only as effective as the tools we give them. We share how to write high-quality tools and evaluations, and how you can boost performance by using Claude to optimize its tools for itself.

智能体的效能取决于我们给它的工具。我们分享如何编写高质量的工具与评测，以及如何用 Claude 为它自己优化工具来提升表现。

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) can empower LLM agents with potentially hundreds of tools to solve real-world tasks. But how do we make those tools maximally effective?

[模型上下文协议（MCP）](https://modelcontextprotocol.io/docs/getting-started/intro)可以让大语言模型（LLM）智能体拥有多达数百个工具，用来解决真实世界的任务。但我们如何让这些工具发挥最大效力？

In this post, we describe our most effective techniques for improving performance in a variety of agentic AI systems1.

在本文中，我们介绍在各种智能体式 AI 系统中提升表现的最有效技巧 1。

We begin by covering how you can:

我们首先介绍如何：

- Build and test prototypes of your tools
- Create and run comprehensive evaluations of your tools with agents
- Collaborate with agents like Claude Code to automatically increase the performance of your tools

- 构建并测试工具原型
- 与智能体一起为工具创建并运行全面的评测
- 与 Claude Code 等智能体协作，自动提升工具的表现

We conclude with key principles for writing high-quality tools we’ve identified along the way:

最后给出我们在过程中总结的编写高质量工具的关键原则：

- Choosing the right tools to implement (and not to implement)
- Namespacing tools to define clear boundaries in functionality
- Returning meaningful context from tools back to agents
- Optimizing tool responses for token efficiency
- Prompt-engineering tool descriptions and specs

- 选择该实现（以及不该实现）的工具
- 用命名空间划分工具，明确功能边界
- 从工具向智能体返回有意义的上下文
- 针对 token 效率优化工具响应
- 对工具描述和规格做提示工程

![This is an image depicting how an engineer might use Claude Code to evaluate the efficacy of agentic tools.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcdc027ad2730e4732168bb198fc9363678544f99-1920x1080.png&w=3840&q=75)Building an evaluation allows you to systematically measure the performance of your tools. You can use Claude Code to automatically optimize your tools against this evaluation.

![这张图展示工程师如何用 Claude Code 评估智能体化工具的效果。](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcdc027ad2730e4732168bb198fc9363678544f99-1920x1080.png&w=3840&q=75)构建评测让你能系统性地度量工具的表现。你可以用 Claude Code 依据这套评测自动优化工具。

## What is a tool?

## 什么是工具？

In computing, deterministic systems produce the same output every time given identical inputs, while *non-deterministic* systems—like agents—can generate varied responses even with the same starting conditions.

在计算领域，确定性系统在给定相同输入时每次都产生相同输出，而*非确定性*系统——例如智能体——即使在相同的初始条件下也可能产生不同的响应。

When we traditionally write software, we’re establishing a contract between deterministic systems. For instance, a function call like `getWeather(“NYC”)` will always fetch the weather in New York City in the exact same manner every time it is called.

在传统方式下编写软件时，我们是在确定性系统之间建立一种契约。例如，像 `getWeather(“NYC”)` 这样的函数调用，每次被调用时都会以完全相同的方式获取纽约市的天气。

Tools are a new kind of software which reflects a contract between deterministic systems and non-deterministic agents. When a user asks "Should I bring an umbrella today?,” an agent might call the weather tool, answer from general knowledge, or even ask a clarifying question about location first. Occasionally, an agent might hallucinate or even fail to grasp how to use a tool.

工具是一类新的软件，它体现的是确定性系统与非确定性智能体之间的契约。当用户问「今天该带伞吗？」，智能体可能会调用天气工具，可能凭通用知识回答，也可能先追问一句地点。有时智能体会产生幻觉，甚至无法理解该如何使用某个工具。

This means fundamentally rethinking our approach when writing software for agents: instead of writing tools and [MCP servers](https://modelcontextprotocol.io/) the way we’d write functions and APIs for other developers or systems, we need to design them for agents.

这意味着为智能体编写软件时要从根本上重新思考做法：我们不能再按为其他开发者或系统编写函数与 API 的方式来编写工具和 [MCP 服务器](https://modelcontextprotocol.io/)，而要为智能体来设计它们。

Our goal is to increase the surface area over which agents can be effective in solving a wide range of tasks by using tools to pursue a variety of successful strategies. Fortunately, in our experience, the tools that are most “ergonomic” for agents also end up being surprisingly intuitive to grasp as humans.

我们的目标是扩大智能体能够有效解决问题的范围，让它能用工具执行各种成功的策略来解决各类任务。幸运的是，根据我们的经验，对智能体最「顺手」的工具，对人类来说也出奇地直观易懂。

## How to write tools

## 如何编写工具

In this section, we describe how you can collaborate with agents both to write and to improve the tools you give them. Start by standing up a quick prototype of your tools and testing them locally. Next, run a comprehensive evaluation to measure subsequent changes. Working alongside agents, you can repeat the process of evaluating and improving your tools until your agents achieve strong performance on real-world tasks.

本节介绍如何与智能体协作，既编写也改进你交给它的工具。先从快速搭起工具原型并在本地测试开始。接着运行一套全面的评测，用来度量后续的改动。在与智能体并肩工作的过程中，你可以重复「评测—改进」这个循环，直到智能体在真实世界任务上取得良好表现。

### Building a prototype

### 构建原型

It can be difficult to anticipate which tools agents will find ergonomic and which tools they won’t without getting hands-on yourself. Start by standing up a quick prototype of your tools. If you’re using [Claude Code](https://www.anthropic.com/claude-code) to write your tools (potentially in one-shot), it helps to give Claude documentation for any software libraries, APIs, or SDKs (including potentially the [MCP SDK](https://modelcontextprotocol.io/docs/sdk)) your tools will rely on. LLM-friendly documentation can commonly be found in flat `llms.txt` files on official documentation sites (here’s our [API’s](https://docs.anthropic.com/llms.txt)).

如果不动手实践，很难预判智能体会觉得哪些工具顺手、哪些不顺手。先从快速搭起工具原型开始。如果你用 [Claude Code](https://www.anthropic.com/claude-code) 来编写工具（有可能一次成型），那么为 Claude 提供工具所依赖的任何软件库、API 或 SDK（也可能包括 [MCP SDK](https://modelcontextprotocol.io/docs/sdk)）的文档会很有帮助。对 LLM 友好的文档通常可以在官方文档站点上的扁平 `llms.txt` 文件中找到（这是我们 [API 的文档](https://docs.anthropic.com/llms.txt)）。

Wrapping your tools in a [local MCP server](https://modelcontextprotocol.io/docs/develop/connect-local-servers) or [Desktop extension](https://www.anthropic.com/engineering/desktop-extensions) (DXT) will allow you to connect and test your tools in Claude Code or the Claude Desktop app.

把工具包装成[本地 MCP 服务器](https://modelcontextprotocol.io/docs/develop/connect-local-servers)或[桌面扩展](https://www.anthropic.com/engineering/desktop-extensions)（DXT），就能在 Claude Code 或 Claude 桌面应用中连接并测试这些工具。

To connect your local MCP server to Claude Code, run `claude mcp add <name> <command> [args...]`.

要把本地 MCP 服务器连接到 Claude Code，请运行 `claude mcp add <name> <command> [args...]`。

To connect your local MCP server or DXT to the Claude Desktop app, navigate to `Settings > Developer` or `Settings > Extensions`, respectively.

要把本地 MCP 服务器或 DXT 连接到 Claude 桌面应用，请分别进入 `Settings > Developer` 或 `Settings > Extensions`。

Tools can also be passed directly into [Anthropic API](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) calls for programmatic testing.

工具也可以直接传入 [Anthropic API](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) 调用，以便用程序化方式测试。

Test the tools yourself to identify any rough edges. Collect feedback from your users to build an intuition around the use-cases and prompts you expect your tools to enable.

自己先测试这些工具，找出任何粗糙之处。收集用户的反馈，从而对期望工具支持的用例和提示词形成直觉。

### Running an evaluation

### 运行评测

Next, you need to measure how well Claude uses your tools by running an evaluation. Start by generating lots of evaluation tasks, grounded in real world uses. We recommend collaborating with an agent to help analyze your results and determine how to improve your tools. See this process end-to-end in our [tool evaluation cookbook](https://platform.claude.com/cookbook/tool-evaluation-tool-evaluation).

接下来，你需要通过运行评测来度量 Claude 使用这些工具的效果。先生成大量扎根于真实使用场景的评测任务。我们建议与智能体协作，帮助分析结果并确定如何改进工具。可以在我们的[工具评测 cookbook](https://platform.claude.com/cookbook/tool-evaluation-tool-evaluation) 中看到这一流程的端到端示例。

![This graph measures the test set accuracy of human-written vs. Claude-optimized Slack MCP servers.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6e810aee67f3f3c955832fb7bf9033ffb0102000-1920x1080.png&w=3840&q=75)Held-out test set performance of our internal Slack tools

![这张图对比了人工编写与 Claude 优化的 Slack MCP 服务器在测试集上的准确率。](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6e810aee67f3f3c955832fb7bf9033ffb0102000-1920x1080.png&w=3840&q=75)我们内部 Slack 工具的留出测试集表现

**Generating evaluation tasks**

**生成评测任务**

With your early prototype, Claude Code can quickly explore your tools and create dozens of prompt and response pairs. Prompts should be inspired by real-world uses and be based on realistic data sources and services (for example, internal knowledge bases and microservices). We recommend you avoid overly simplistic or superficial “sandbox” environments that don’t stress-test your tools with sufficient complexity. Strong evaluation tasks might require multiple tool calls—potentially dozens.

有了早期原型，Claude Code 可以快速探索你的工具，并生成几十组提示词与响应对。提示词应当源于真实使用场景，并基于贴近现实的数据源与服务（例如内部知识库和微服务）。我们建议避免过于简单或流于表面的「沙箱」环境，它们无法用足够的复杂度对工具做压力测试。强度足够的评测任务可能需要多次工具调用——甚至几十次。

Here are some examples of strong tasks:

以下是一些强度较高的任务示例：

- Schedule a meeting with Jane next week to discuss our latest Acme Corp project. Attach the notes from our last project planning meeting and reserve a conference room.
- Customer ID 9182 reported that they were charged three times for a single purchase attempt. Find all relevant log entries and determine if any other customers were affected by the same issue.
- Customer Sarah Chen just submitted a cancellation request. Prepare a retention offer. Determine: (1) why they're leaving, (2) what retention offer would be most compelling, and (3) any risk factors we should be aware of before making an offer.

- 安排下周与 Jane 开一场会，讨论我们最新的 Acme Corp 项目。附上上次项目规划会议的记录，并预订一间会议室。
- 客户 ID 9182 反馈说，一次购买尝试被扣款三次。找出所有相关日志条目，并判断是否有其他客户受到同一问题影响。
- 客户 Sarah Chen 刚刚提交了取消请求。准备一份挽留方案。确定：(1) 其流失原因，(2) 最具吸引力的挽留方案，以及 (3) 在提出挽留前我们应留意的任何风险因素。

And here are some weaker tasks:

以下则是一些强度较低的任务：

- Schedule a meeting with jane@acme.corp next week.
- Search the payment logs for `purchase_complete` and `customer_id=9182`.
- Find the cancellation request by Customer ID 45892.

- 安排下周与 jane@acme.corp 开一场会。
- 在支付日志中搜索 `purchase_complete` 和 `customer_id=9182`。
- 找出客户 ID 45892 的取消请求。

Each evaluation prompt should be paired with a verifiable response or outcome. Your verifier can be as simple as an exact string comparison between ground truth and sampled responses, or as advanced as enlisting Claude to judge the response. Avoid overly strict verifiers that reject correct responses due to spurious differences like formatting, punctuation, or valid alternative phrasings.

每个评测提示词都应当配一个可验证的响应或结果。验证器可以简单到把标准答案与采样响应做精确字符串比较，也可以复杂到请 Claude 来评判响应。避免过于严格的验证器，不要因为格式、标点或合理的不同措辞这类无关差异就否掉正确的响应。

For each prompt-response pair, you can optionally also specify the tools you expect an agent to call in solving the task, to measure whether or not agents are successful in grasping each tool’s purpose during evaluation. However, because there might be multiple valid paths to solving tasks correctly, try to avoid overspecifying or overfitting to strategies.

对每一组提示词—响应对，你还可以选择性地指定期望智能体在解决任务时调用的工具，以便在评测中度量智能体是否成功理解了每个工具的用途。不过，由于正确解决任务可能存在多条有效路径，尽量避免过度指定或对特定策略过拟合。

**Running the evaluation**

**运行评测**

We recommend running your evaluation programmatically with direct LLM API calls. Use simple agentic loops (`while`-loops wrapping alternating LLM API and tool calls): one loop for each evaluation task. Each evaluation agent should be given a single task prompt and your tools.

我们建议用直接的 LLM API 调用以程序化方式运行评测。使用简单的智能体化循环（用 `while` 循环包住交替进行的 LLM API 调用与工具调用）：每个评测任务一个循环。每个评测智能体都应只接收一个任务提示词以及你的工具。

In your evaluation agents’ system prompts, we recommend instructing agents to output not just structured response blocks (for verification), but also reasoning and feedback blocks. Instructing agents to output these *before*tool call and response blocks may increase LLMs’ effective intelligence by triggering chain-of-thought (CoT) behaviors.

在评测智能体的系统提示词中，我们建议要求智能体不仅输出结构化的响应块（用于验证），还要输出推理块和反馈块。要求智能体在工具调用与响应块*之前*输出这些内容，可以通过触发思维链（CoT）行为来提升 LLM 的有效智能。

If you’re running your evaluation with Claude, you can turn on [interleaved thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking) for similar functionality “off-the-shelf”. This will help you probe why agents do or don’t call certain tools and highlight specific areas of improvement in tool descriptions and specs.

如果你用 Claude 运行评测，可以开启[交错思考](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking)，直接获得类似的功能。这有助于探查智能体为何调用或不调用某些工具，并指出工具描述与规格中需要改进的具体之处。

As well as top-level accuracy, we recommend collecting other metrics like the total runtime of individual tool calls and tasks, the total number of tool calls, the total token consumption, and tool errors. Tracking tool calls can help reveal common workflows that agents pursue and offer some opportunities for tools to consolidate.

除了顶层准确率，我们还建议收集其他指标，例如单次工具调用与任务的总运行时长、工具调用总次数、token 总消耗量以及工具错误。跟踪工具调用有助于揭示智能体常走的常见工作流，也为工具整合提供了一些机会。

![This graph measures the test set accuracy of human-written vs. Claude-optimized Asana MCP servers.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3f1f47e80974750cd924bc51e42b6df1ad997fab-1920x1080.png&w=3840&q=75)Held-out test set performance of our internal Asana tools

![这张图对比了人工编写与 Claude 优化的 Asana MCP 服务器在测试集上的准确率。](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3f1f47e80974750cd924bc51e42b6df1ad997fab-1920x1080.png&w=3840&q=75)我们内部 Asana 工具的留出测试集表现

**Analyzing results** Agents are your helpful partners in spotting issues and providing feedback on everything from contradictory tool descriptions to inefficient tool implementations and confusing tool schemas. However, keep in mind that what agents omit in their feedback and responses can often be more important than what they include. LLMs don’t always [say what they mean](https://www.anthropic.com/research/tracing-thoughts-language-model).

**分析结果** 智能体是你发现问题的好帮手，能从相互矛盾的工具描述，到低效的工具实现、令人困惑的工具 schema，提供各方面的反馈。不过要记住，智能体在反馈和响应中省略的内容，往往比它们写出来的更重要。LLM 并不总是[言如其意](https://www.anthropic.com/research/tracing-thoughts-language-model)。

Observe where your agents get stumped or confused. Read through your evaluation agents’ reasoning and feedback (or CoT) to identify rough edges. Review the raw transcripts (including tool calls and tool responses) to catch any behavior not explicitly described in the agent’s CoT. Read between the lines; remember that your evaluation agents don’t necessarily know the correct answers and strategies.

观察智能体在哪里卡住或困惑。通读评测智能体的推理与反馈（即 CoT），找出粗糙之处。查看原始转录（包括工具调用和工具响应），捕捉智能体 CoT 中未明确描述的任何行为。要读懂字里行间之意；记住评测智能体未必知道正确答案和策略。

Analyze your tool calling metrics. Lots of redundant tool calls might suggest some rightsizing of pagination or token limit parameters is warranted; lots of tool errors for invalid parameters might suggest tools could use clearer descriptions or better examples. When we launched Claude’s [web search tool](https://www.anthropic.com/news/web-search), we identified that Claude was needlessly appending `2025` to the tool’s `query` parameter, biasing search results and degrading performance (we steered Claude in the right direction by improving the tool description).

分析工具调用指标。大量冗余的工具调用可能说明分页或 token 上限参数需要重新调到合适值；大量由无效参数导致的工具错误可能说明工具需要更清晰的描述或更好的示例。我们发布 Claude 的[网页搜索工具](https://www.anthropic.com/news/web-search)时发现，Claude 会不必要地把 `2025` 追加到工具的 `query` 参数上，使搜索结果产生偏斜并降低表现（我们通过改进工具描述把 Claude 引回了正确方向）。

### Collaborating with agents

### 与智能体协作

You can even let agents analyze your results and improve your tools for you. Simply concatenate the transcripts from your evaluation agents and paste them into Claude Code. Claude is an expert at analyzing transcripts and refactoring lots of tools all at once—for example, to ensure tool implementations and descriptions remain self-consistent when new changes are made.

你甚至可以让智能体替你分析结果并改进工具。只要把评测智能体的转录拼接起来，粘贴到 Claude Code 中即可。Claude 擅长分析转录，并一次性重构大量工具——例如确保在做出新改动时，工具的实现与描述仍然自洽。

In fact, most of the advice in this post came from repeatedly optimizing our internal tool implementations with Claude Code. Our evaluations were created on top of our internal workspace, mirroring the complexity of our internal workflows, including real projects, documents, and messages.

事实上，本文的大部分建议都来自我们用 Claude Code 反复优化内部工具实现的实践。我们的评测建立在自己的内部工作区之上，复现了内部工作流的复杂度，包括真实项目、文档和消息。

We relied on held-out test sets to ensure we did not overfit to our “training” evaluations. These test sets revealed that we could extract additional performance improvements even beyond what we achieved with "expert" tool implementations—whether those tools were manually written by our researchers or generated by Claude itself.

我们依靠留出测试集来确保没有对「训练」评测过拟合。这些测试集表明，即便已经采用了「专家级」的工具实现，我们仍能取得额外的表现提升——无论这些工具是由我们的研究人员手写，还是由 Claude 自己生成的。

In the next section, we’ll share some of what we learned from this process.

下一节将分享我们从这个过程中学到的一些内容。

## Principles for writing effective tools

## 编写高效工具的原则

In this section, we distill our learnings into a few guiding principles for writing effective tools.

本节把我们学到的东西提炼成若干编写高效工具的指导原则。

### Choosing the right tools for agents

### 为智能体选择合适的工具

More tools don’t always lead to better outcomes. A common error we’ve observed is tools that merely wrap existing software functionality or API endpoints—whether or not the tools are appropriate for agents. This is because agents have distinct “affordances” to traditional software—that is, they have different ways of perceiving the potential actions they can take with those tools

工具更多并不总能带来更好的结果。我们观察到的一个常见错误，是让工具仅仅包装现有的软件功能或 API 端点——而不考虑这些工具是否适合智能体。这是因为智能体相对于传统软件有独特的「可供性」，也就是说，它们感知自己能用这些工具采取哪些潜在行动的方式不同

LLM agents have limited "context" (that is, there are limits to how much information they can process at once), whereas computer memory is cheap and abundant. Consider the task of searching for a contact in an address book. Traditional software programs can efficiently store and process a list of contacts one at a time, checking each one before moving on.

LLM 智能体的「上下文」是有限的（也就是说，它们一次能处理的信息量有上限），而计算机内存便宜且充裕。设想在通讯录中查找一位联系人的任务。传统软件程序可以高效地存储并逐条处理联系人列表，检查完一条再处理下一条。

However, if an LLM agent uses a tool that returns ALL contacts and then has to read through each one token-by-token, it's wasting its limited context space on irrelevant information (imagine searching for a contact in your address book by reading each page from top-to-bottom—that is, via brute-force search). The better and more natural approach (for agents and humans alike) is to skip to the relevant page first (perhaps finding it alphabetically).

然而，如果 LLM 智能体使用的工具返回全部联系人，然后它必须逐 token 读完每一条，那就是把有限的上下文空间浪费在无关信息上（想象一下从头到尾逐页翻阅通讯录来查找一位联系人——也就是暴力搜索）。更好也更自然的做法（对智能体和人类都一样）是先直接翻到相关的那一页（也许按字母顺序找到它）。

We recommend building a few thoughtful tools targeting specific high-impact workflows, which match your evaluation tasks and scaling up from there. In the address book case, you might choose to implement a `search_contacts` or `message_contact` tool instead of a `list_contacts` tool.

我们建议先针对特定的高影响力工作流构建少数几个经过深思的工具，与你的评测任务相匹配，再由此逐步扩展。在通讯录这个例子里，你可以选择实现 `search_contacts` 或 `message_contact` 工具，而不是 `list_contacts` 工具。

Tools can consolidate functionality, handling potentially *multiple* discrete operations (or API calls) under the hood. For example, tools can enrich tool responses with related metadata or handle frequently chained, multi-step tasks in a single tool call.

工具可以整合功能，在内部处理可能*多个*离散操作（或 API 调用）。例如，工具可以用相关元数据丰富响应内容，或在一次工具调用中处理经常串联的多步任务。

Here are some examples:

以下是一些示例：

- Instead of implementing a `list_users`, `list_events`, and `create_event` tools, consider implementing a `schedule_event` tool which finds availability and schedules an event.
- Instead of implementing a `read_logs` tool, consider implementing a `search_logs` tool which only returns relevant log lines and some surrounding context.
- Instead of implementing `get_customer_by_id`, `list_transactions`, and `list_notes` tools, implement a `get_customer_context` tool which compiles all of a customer’s recent & relevant information all at once.

- 与其实现 `list_users`、`list_events` 和 `create_event` 工具，不如考虑实现一个 `schedule_event` 工具，由它查找可用时间并安排事件。
- 与其实现 `read_logs` 工具，不如考虑实现一个 `search_logs` 工具，只返回相关的日志行以及一些周边上下文。
- 与其实现 `get_customer_by_id`、`list_transactions` 和 `list_notes` 工具，不如实现一个 `get_customer_context` 工具，一次性汇总某位客户全部近期且相关的信息。

Make sure each tool you build has a clear, distinct purpose. Tools should enable agents to subdivide and solve tasks in much the same way that a human would, given access to the same underlying resources, and simultaneously reduce the context that would have otherwise been consumed by intermediate outputs.

确保你构建的每个工具都有清晰、独特的用途。工具应当让智能体能够像人类在能访问同样底层资源时会做的那样，拆分并解决任务，同时减少原本会被中间输出消耗掉的上下文。

Too many tools or overlapping tools can also distract agents from pursuing efficient strategies. Careful, selective planning of the tools you build (or don’t build) can really pay off.

工具过多或彼此重叠，也会让智能体偏离高效策略。对要构建（或不构建）哪些工具做审慎而有选择的规划，确实会有回报。

### Namespacing your tools

### 为工具划分命名空间

Your AI agents will potentially gain access to dozens of MCP servers and hundreds of different tools–including those by other developers. When tools overlap in function or have a vague purpose, agents can get confused about which ones to use.

你的 AI 智能体可能会访问到几十个 MCP 服务器和数百个不同的工具——包括其他开发者提供的工具。当工具在功能上重叠或用途含糊时，智能体会搞不清该用哪些。

Namespacing (grouping related tools under common prefixes) can help delineate boundaries between lots of tools; MCP clients sometimes do this by default. For example, namespacing tools by service (e.g., `asana_search`, `jira_search`) and by resource (e.g., `asana_projects_search`, `asana_users_search`), can help agents select the right tools at the right time.

命名空间（把相关工具归到共同前缀下）有助于划分大量工具之间的边界；MCP 客户端有时会默认这样做。例如，按服务（如 `asana_search`、`jira_search`）和按资源（如 `asana_projects_search`、`asana_users_search`）为工具划分命名空间，能帮助智能体在恰当的时候选到恰当的工具。

We have found selecting between prefix- and suffix-based namespacing to have non-trivial effects on our tool-use evaluations. Effects vary by LLM and we encourage you to choose a naming scheme according to your own evaluations.

我们发现，在前缀式与后缀式命名空间之间做选择，对我们的工具调用评测有不容忽视的影响。影响因 LLM 而异，我们建议你根据自己的评测来选择命名方案。

Agents might call the wrong tools, call the right tools with the wrong parameters, call too few tools, or process tool responses incorrectly. By selectively implementing tools whose names reflect natural subdivisions of tasks, you simultaneously reduce the number of tools and tool descriptions loaded into the agent’s context and offload agentic computation from the agent’s context back into the tool calls themselves. This reduces an agent’s overall risk of making mistakes.

智能体可能调用错误的工具、用错误的参数调用正确的工具、调用的工具太少，或者错误地处理工具响应。有选择地实现那些名称反映任务自然划分的工具，可以同时减少加载到智能体上下文中的工具与工具描述数量，并把智能体化的计算从智能体的上下文转移到工具调用本身。这能降低智能体犯错的整体风险。

### Returning meaningful context from your tools

### 从工具返回有意义的上下文

In the same vein, tool implementations should take care to return only high signal information back to agents. They should prioritize contextual relevance over flexibility, and eschew low-level technical identifiers (for example: `uuid`, `256px_image_url`, `mime_type`). Fields like `name`, `image_url`, and `file_type` are much more likely to directly inform agents’ downstream actions and responses.

同理，工具实现应当注意只向智能体返回高信号量的信息。它们应当优先考虑上下文相关性而非灵活性，并避免使用底层技术标识符（例如：`uuid`、`256px_image_url`、`mime_type`）。像 `name`、`image_url` 和 `file_type` 这样的字段更有可能直接影响智能体的下游行动与响应。

Agents also tend to grapple with natural language names, terms, or identifiers significantly more successfully than they do with cryptic identifiers. We’ve found that merely resolving arbitrary alphanumeric UUIDs to more semantically meaningful and interpretable language (or even a 0-indexed ID scheme) significantly improves Claude’s precision in retrieval tasks by reducing hallucinations.

智能体处理自然语言的名称、术语或标识符，往往比处理晦涩的标识符成功得多。我们发现，仅仅把任意的字母数字 UUID 解析为语义更明确、更易理解的语言（甚至只是改成从 0 开始编号的 ID 方案），就能通过减少幻觉显著提升 Claude 在检索任务中的精确度。

In some instances, agents may require the flexibility to interact with both natural language and technical identifiers outputs, if only to trigger downstream tool calls (for example, `search_user(name=’jane’)` → `send_message(id=12345)`). You can enable both by exposing a simple `response_format` enum parameter in your tool, allowing your agent to control whether tools return `“concise”` or `“detailed”` responses (images below).

在某些情况下，智能体可能需要灵活性，既能处理自然语言输出，也能处理技术标识符输出，哪怕只是为了触发下游工具调用（例如 `search_user(name=’jane’)` → `send_message(id=12345)`）。你可以在工具中暴露一个简单的 `response_format` 枚举参数来同时支持两者，让智能体控制工具返回 `“concise”` 还是 `“detailed”` 响应（见下图）。

You can add more formats for even greater flexibility, similar to GraphQL where you can choose exactly which pieces of information you want to receive. Here is an example ResponseFormat enum to control tool response verbosity:

你还可以增加更多格式以获得更大灵活性，类似 GraphQL 那样，精确选择你想接收哪些信息。以下是一个用于控制工具响应详细程度的 ResponseFormat 枚举示例：

```
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

Here’s an example of a detailed tool response (206 tokens):

以下是一个详细工具响应的示例（206 个 token）：

![This code snippet depicts an example of a detailed tool response.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png&w=3840&q=75)

![这段代码片段展示了一个详细工具响应的示例。](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png&w=3840&q=75)

Here’s an example of a concise tool response (72 tokens):

以下是一个简洁工具响应的示例（72 个 token）：

![This code snippet depicts a concise tool response.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd4f649a66482efb5a80cf14ea85e84974ede1c49-1920x725.png&w=3840&q=75)Slack threads and thread replies are identified by unique `thread_ts` which are required to fetch thread replies. `thread_ts` and other IDs (`channel_id`, `user_id`) can be retrieved from a `“detailed”` tool response to enable further tool calls that require these. `“concise”` tool responses return only thread content and exclude IDs. In this example, we use ~⅓ of the tokens with `“concise”` tool responses.

![这段代码片段展示了一个简洁工具响应。](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd4f649a66482efb5a80cf14ea85e84974ede1c49-1920x725.png&w=3840&q=75)Slack 会话串（thread）和串内回复由唯一的 `thread_ts` 标识，获取串内回复时必须提供该标识。`thread_ts` 和其他 ID（`channel_id`、`user_id`）可以从 `“detailed”` 工具响应中获取，以便支持后续需要这些 ID 的工具调用。`“concise”` 工具响应只返回串内容，不包含 ID。在这个示例中，使用 `“concise”` 工具响应时我们只消耗了约 ⅓ 的 token。

Even your tool response structure—for example XML, JSON, or Markdown—can have an impact on evaluation performance: there is no one-size-fits-all solution. This is because LLMs are trained on next-token prediction and tend to perform better with formats that match their training data. The optimal response structure will vary widely by task and agent. We encourage you to select the best response structure based on your own evaluation.

就连工具响应的结构——例如 XML、JSON 或 Markdown——也会影响评测表现：不存在放之四海而皆准的方案。这是因为 LLM 是在下一 token 预测任务上训练的，对与训练数据格式相匹配的格式往往表现更好。最优的响应结构会因任务和智能体而有很大差异。我们建议你根据自己的评测来选择最佳的响应结构。

### Optimizing tool responses for token efficiency

### 针对 token 效率优化工具响应

Optimizing the quality of context is important. But so is optimizing the *quantity*of context returned back to agents in tool responses.

优化上下文的质量很重要，但优化工具响应返回给智能体的上下文*数量*同样重要。

We suggest implementing some combination of pagination, range selection, filtering, and/or truncation with sensible default parameter values for any tool responses that could use up lots of context. For Claude Code, we restrict tool responses to 25,000 tokens by default. We expect the effective context length of agents to grow over time, but the need for context-efficient tools to remain.

对于任何可能消耗大量上下文的工具响应，我们建议实现分页、范围选择、过滤和/或截断的某种组合，并配以合理的默认参数值。对 Claude Code，我们默认把工具响应限制在 25,000 个 token 以内。我们预计智能体的有效上下文长度会随时间增长，但对上下文高效工具的需求仍将存在。

If you choose to truncate responses, be sure to steer agents with helpful instructions. You can directly encourage agents to pursue more token-efficient strategies, like making many small and targeted searches instead of a single, broad search for a knowledge retrieval task. Similarly, if a tool call raises an error (for example, during input validation), you can prompt-engineer your error responses to clearly communicate specific and actionable improvements, rather than opaque error codes or tracebacks.

如果你选择截断响应，务必用有用的说明来引导智能体。你可以直接鼓励智能体采用更节省 token 的策略，例如在知识检索任务中做许多次小而精准的搜索，而不是做一次宽泛的搜索。同样，如果某次工具调用报错（例如在输入校验期间），你可以对错误响应做提示工程，让它清楚传达具体且可操作的改进建议，而不是给出晦涩的错误码或堆栈回溯。

Here’s an example of a truncated tool response:

以下是一个被截断的工具响应示例：

![This image depicts an example of a truncated tool response.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png&w=3840&q=75)

![这张图展示了一个被截断的工具响应示例。](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png&w=3840&q=75)

Here’s an example of an unhelpful error response:

以下是一个无帮助的错误响应示例：

![This image depicts an example of an unhelpful tool response.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2445187904704fec8c50af0b950e310ba743fac2-1920x733.png&w=3840&q=75)

![这张图展示了一个无帮助的工具响应示例。](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2445187904704fec8c50af0b950e310ba743fac2-1920x733.png&w=3840&q=75)

Here’s an example of a helpful error response:

以下是一个有用的错误响应示例：

![This image depicts an example of a helpful error response.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F810661bd44a35fb273806ae95160040155978c3e-1920x850.png&w=3840&q=75)Tool truncation and error responses can steer agents towards more token-efficient tool-use behaviors (using filters or pagination) or give examples of correctly formatted tool inputs.

![这张图展示了一个有用的错误响应示例。](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F810661bd44a35fb273806ae95160040155978c3e-1920x850.png&w=3840&q=75)工具截断和错误响应可以引导智能体采用更节省 token 的工具调用行为（使用过滤器或分页），或者给出格式正确的工具输入示例。

### Prompt-engineering your tool descriptions

### 对工具描述做提示工程

We now come to one of the most effective methods for improving tools: prompt-engineering your tool descriptions and specs. Because these are loaded into your agents’ context, they can collectively steer agents toward effective tool-calling behaviors.

现在我们来到改进工具最有效的方法之一：对工具描述和规格做提示工程。由于这些内容会被加载到智能体的上下文中，它们可以共同引导智能体形成有效的工具调用行为。

When writing tool descriptions and specs, think of how you would describe your tool to a new hire on your team. Consider the context that you might implicitly bring—specialized query formats, definitions of niche terminology, relationships between underlying resources—and make it explicit. Avoid ambiguity by clearly describing (and enforcing with strict data models) expected inputs and outputs. In particular, input parameters should be unambiguously named: instead of a parameter named `user`, try a parameter named `user_id`.

编写工具描述和规格时，想一想你会如何向团队里的新同事介绍这个工具。考虑你可能默认带入的上下文——专用查询格式、小众术语的定义、底层资源之间的关系——并把它们明确写出来。通过清楚描述（并用严格的数据模型强制约束）预期的输入与输出，来避免歧义。尤其是输入参数应当命名得没有歧义：与其用名为 `user` 的参数，不如用名为 `user_id` 的参数。

With your evaluation you can measure the impact of your prompt engineering with greater confidence. Even small refinements to tool descriptions can yield dramatic improvements. Claude Sonnet 3.5 achieved state-of-the-art performance on the[SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench-sonnet) evaluation after we made precise refinements to tool descriptions, dramatically reducing error rates and improving task completion.

有了评测，你就能更有把握地度量提示工程带来的影响。即使对工具描述做很小的改进，也可能带来显著提升。在我们对工具描述做了精细改进之后，Claude Sonnet 3.5 在 [SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench-sonnet) 评测上取得了当时的最优表现，错误率大幅下降，任务完成度提升。

You can find other best practices for tool definitions in our [Developer Guide](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#best-practices-for-tool-definitions). If you’re building tools for Claude, we also recommend reading about how tools are dynamically loaded into Claude’s [system prompt](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt). Lastly, if you’re writing tools for an MCP server, [tool annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) help disclose which tools require open-world access or make destructive changes.

你可以在我们的[开发者指南](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#best-practices-for-tool-definitions)中找到有关工具定义的其他最佳实践。如果你在为 Claude 构建工具，我们还建议阅读工具如何被动态加载到 Claude 的[系统提示词](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt)中。最后，如果你在为 MCP 服务器编写工具，[工具注解](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)有助于说明哪些工具需要开放世界访问权限或会做出破坏性变更。

## Looking ahead

## 展望

To build effective tools for agents, we need to re-orient our software development practices from predictable, deterministic patterns to non-deterministic ones.

要为智能体构建高效的工具，我们需要把软件开发实践从可预测的确定性模式转向非确定性模式。

Through the iterative, evaluation-driven process we’ve described in this post, we've identified consistent patterns in what makes tools successful: Effective tools are intentionally and clearly defined, use agent context judiciously, can be combined together in diverse workflows, and enable agents to intuitively solve real-world tasks.

通过本文描述的迭代式、评测驱动的流程，我们找到了让工具成功的若干一致规律：高效的工具是有意设计且定义清晰的，能审慎地使用智能体上下文，可以在多样的工作流中相互组合，并让智能体能够直观地解决真实世界任务。

In the future, we expect the specific mechanisms through which agents interact with the world to evolve—from updates to the MCP protocol to upgrades to the underlying LLMs themselves. With a systematic, evaluation-driven approach to improving tools for agents, we can ensure that as agents become more capable, the tools they use will evolve alongside them.

未来，我们预计智能体与世界交互的具体机制会不断演进——从 MCP 协议的更新到底层 LLM 本身的升级。用系统化、评测驱动的方法改进智能体工具，我们就能确保随着智能体能力增强，它们使用的工具也会同步演进。

## Acknowledgements

## 致谢

Written by Ken Aizawa with valuable contributions from colleagues across Research (Barry Zhang, Zachary Witten, Daniel Jiang, Sami Al-Sheikh, Matt Bell, Maggie Vo), MCP (Theodora Chu, John Welsh, David Soria Parra, Adam Jones), Product Engineering (Santiago Seira), Marketing (Molly Vorwerck), Design (Drew Roper), and Applied AI (Christian Ryan, Alexander Bricken).

本文由 Ken Aizawa 撰写，并得到以下同事的宝贵贡献：研究团队（Barry Zhang、Zachary Witten、Daniel Jiang、Sami Al-Sheikh、Matt Bell、Maggie Vo）、MCP 团队（Theodora Chu、John Welsh、David Soria Parra、Adam Jones）、产品工程团队（Santiago Seira）、市场团队（Molly Vorwerck）、设计团队（Drew Roper）以及应用 AI 团队（Christian Ryan、Alexander Bricken）。

1Beyond training the underlying LLMs themselves.

1 超越对底层 LLM 本身的训练。

[![Interlocking puzzle piece with complex geometric shape and detailed surface texture](https://www-cdn.anthropic.com/images/4zrzovbb/website/43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)Looking to learn more?Explore courses](https://anthropic.skilljar.com/)

[![相互咬合的拼图块，具有复杂的几何形状和细致的表面纹理](https://www-cdn.anthropic.com/images/4zrzovbb/website/43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)想了解更多？探索课程](https://anthropic.skilljar.com/)

## Get the developer newsletter

## 订阅开发者通讯

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

产品更新、操作指南、社区聚焦等。每月发送到你的收件箱。
