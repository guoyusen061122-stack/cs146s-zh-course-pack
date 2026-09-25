# MCP Food-for-Thought

# 关于 MCP 的思考

The [Model Context Protocol](https://modelcontextprotocol.io/overview) (MCP) is a pretty big deal these days. It’s become the de facto standard for giving LLMs access to tools that someone else wrote, which, of course, turns them into [agents](https://simonwillison.net/2025/May/22/tools-in-a-loop/). But writing tools for a new MCP server is hard, and so people often propose [auto-converting existing APIs into MCP tools](https://blog.christianposta.com/semantics-matter-exposing-openapi-as-mcp-tools/); typically using OpenAPI metadata ([1](https://jedisct1.github.io/openapi-mcp/), [2](https://www.gravitee.io/blog/turn-any-rest-api-into-mcp-server-inside-gravitee)).

[模型上下文协议](https://modelcontextprotocol.io/overview)（MCP）如今是件相当重要的事。它已成为事实上的标准，用来让大语言模型（LLM）访问别人编写的工具，而这自然就把大语言模型变成了[智能体](https://simonwillison.net/2025/May/22/tools-in-a-loop/)。但是为一个新的 MCP 服务器编写工具很难，因此人们常常提议[把现有 API 自动转换成 MCP 工具](https://blog.christianposta.com/semantics-matter-exposing-openapi-as-mcp-tools/)，通常借助 OpenAPI 元数据（[1](https://jedisct1.github.io/openapi-mcp/)、[2](https://www.gravitee.io/blog/turn-any-rest-api-into-mcp-server-inside-gravitee)）。

In my experience, this can work but it doesn’t work *well*. Here are a few reasons why:

以我的经验，这种做法可行，但效果*并不好*。原因有以下几点：

## Agents don’t do well with large numbers of tools

## 智能体不擅长处理大量工具

Infamously, [VS Code has a hard limit of 128 tools](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) - but [many models struggle with accurate tool calling well before that number](https://arxiv.org/abs/2411.15399). Also, each tool and its description takes up valuable context window space.

众所周知，[VS Code 对工具数量有 128 个的硬性上限](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)，但[许多模型在远低于这个数字时就已经难以准确调用工具](https://arxiv.org/abs/2411.15399)。此外，每个工具及其描述都会占用宝贵的上下文窗口空间。

Most web APIs weren’t designed with these constraints in mind! It’s fine to have umpteen APIs for a single product area when those APIs are called from code, but if each of those APIs is mapped to an MCP tool the results might not be great.

大多数 Web API 在设计时并没有考虑这些约束！当 API 由代码调用时，为同一个产品领域提供大量 API 并无问题；但如果每个 API 都映射成一个 MCP 工具，结果可能就不太好。

MCP tools designed from the ground up are typically [much more flexible than individual web APIs](https://engineering.block.xyz/blog/blocks-playbook-for-designing-mcp-servers), with each tool being able to do the work of several individual APIs.

从零开始设计的 MCP 工具通常[比单个 Web API 灵活得多](https://engineering.block.xyz/blog/blocks-playbook-for-designing-mcp-servers)，每个工具都能完成好几个单独 API 的工作。

## APIs can blow through context windows quickly

## API 会迅速耗尽上下文窗口

Imagine an API that returns 100 records at a time, and each record is very wide (say, 50 fields). Sending those results to an agent as-is will use up a lot of tokens; even if a query can be satisfied with only a few fields, every field ends up in the context window.

设想某个 API 一次返回 100 条记录，而每条记录都很宽（比如 50 个字段）。把这些结果原样发给智能体会消耗大量 token（词元）；即使某个查询只用少数几个字段就能满足，每一个字段最终仍会进入上下文窗口。

APIs are typically paginated by the number of records, but records can vary a *lot* in size. One record might contain a large text field that takes up 100,000 [tokens](https://learn.microsoft.com/en-us/dotnet/ai/conceptual/understanding-tokens), while another might contain 10. Putting these API results directly into an agent’s context window is a gamble; sometimes it works, sometimes it will blow up.

API 通常按记录数量分页，但记录的大小可能相差*极大*。一条记录可能包含一个占用 100,000 个 [token](https://learn.microsoft.com/en-us/dotnet/ai/conceptual/understanding-tokens) 的大文本字段，而另一条可能只占 10 个。把这些 API 结果直接放进智能体的上下文窗口是一场赌博；有时可行，有时会彻底崩掉。

The format of the data can also be an issue. Most web APIs these days return JSON, but JSON is a very token-inefficient format. Take this:

数据的格式也可能成为问题。如今大多数 Web API 返回 JSON，但 JSON 是一种非常浪费 token 的格式。请看这个：

```json
[{"firstName":"Alice","lastName":"Johnson","age":28},{"firstName":"Bob","lastName":"Smith","age":35}]
```

Compare to the same data in CSV format:

与同样数据的 CSV 格式对比：

```csv
firstName,lastName,ageAlice,Johnson,28Bob,Smith,35
```

The CSV data is *much* more succinct - it uses up half as many tokens per record. [Typically CSV, TSV, or YAML (for nested data) are better choices than JSON](https://david-gilbertson.medium.com/llm-output-formats-why-json-costs-more-than-tsv-ebaf590bd541).

CSV 数据*简洁得多*——每条记录消耗的 token 只有原来的一半。[通常 CSV、TSV 或 YAML（用于嵌套数据）比 JSON 更合适](https://david-gilbertson.medium.com/llm-output-formats-why-json-costs-more-than-tsv-ebaf590bd541)。

None of these issues are insurmountable. You could imagine automatically adding tool arguments that let agents [project](https://en.wikipedia.org/wiki/Projection_(relational_algebra)) fields, automatically truncating or summarizing large results, and automatically converting JSON results to CSV (or YAML for nested data). But most servers I’ve seen do none of those things.

这些问题都不是无法解决的。你可以设想自动添加工具参数，让智能体能够[投影](https://en.wikipedia.org/wiki/Projection_(relational_algebra))字段；自动截断或摘要过大的结果；以及自动把 JSON 结果转换为 CSV（嵌套数据则转为 YAML）。但我见过的大多数服务器一样都没做。

## APIs don’t make the most of agents’ unique capabilities

## API 没有充分利用智能体的独特能力

APIs return structured data for programmatic consumption. That’s often what agents want from tool calls… but agents can *also* handle other, more free-form instructions.

API 返回结构化数据，供程序化消费。这往往正是智能体希望从工具调用中得到的东西……但智能体*也*能处理其他更自由形式的指令。

For example an `ask_question` tool could perform a RAG query over some documentation, then return information in plain text that is used to inform the next tool call - skipping structured data entirely.

例如，`ask_question` 工具可以对某些文档执行一次 RAG 查询，然后用纯文本返回信息，再用这些信息指导下一次工具调用——完全跳过结构化数据。

Or, a call to a `search_cities` tool could return a structured list of cities *and* a suggestion of what to call next:

或者，对 `search_cities` 工具的一次调用可以返回结构化的城市列表，*同时*给出接下来该调用什么的建议：

```csv
city_name,population,country,regionTokyo,37194000,Japan,AsiaDelhi,32941000,India,AsiaShanghai,28517000,China,AsiaSuggestion: To get more specific information (weather, attractions, demographics), try calling get_city_details with the city_name parameter.
```

That sort of layering and tool chaining [can be very effective](https://engineering.block.xyz/blog/build-mcp-tools-like-ogres-with-layers) in MCP servers, and it’s something you’ll miss out on completely if auto-converting APIs to tools.

在 MCP 服务器中，这种分层与工具链式调用[可以非常有效](https://engineering.block.xyz/blog/build-mcp-tools-like-ogres-with-layers)，而如果自动把 API 转换成工具，你将完全错失这一点。

## If an agent needs to call an API, it could just do that

## 如果智能体需要调用 API，那直接调用即可

Agents like Claude Code are remarkably capable of writing+executing code these days, including scripts that call web APIs. Some people take this so far as to [argue that MCP isn’t needed at all](https://lucumr.pocoo.org/2025/7/3/tools/)!

如今，像 Claude Code 这样的智能体在编写并执行代码方面能力惊人，包括调用 Web API 的脚本。有些人甚至极端到[主张根本不需要 MCP](https://lucumr.pocoo.org/2025/7/3/tools/)！

I disagree with that conclusion, but I do think we should skate to where the puck is going. [Sandboxing of agents is improving rapidly](https://github.com/openai/codex), and if it’s easy+safe for an agent to call APIs directly then we might as well do that and cut out the middleman.

我不同意这个结论，但我确实认为我们应该滑向冰球将要到达的位置。[智能体的沙箱隔离正在快速改进](https://github.com/openai/codex)，如果智能体直接调用 API 既简单又安全，那我们不妨就这么做，省掉中间环节。

## Conclusion

## 结论

Agents are fundamentally different from the typical consumers of APIs. It’s possible to automatically create MCP tools from existing APIs, but doing that is unlikely to work *well*. Agents do best when given tools that are designed for their unique capabilities and limitations.

智能体与 API 的典型消费者有本质区别。从现有 API 自动创建 MCP 工具是可行的，但这样做不太可能取得*好*效果。当工具是针对智能体的独特能力与局限而设计时，智能体的表现最好。
