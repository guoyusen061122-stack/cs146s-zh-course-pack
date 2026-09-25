# MCP Introduction

#### Back to blog

# Model Context Protocol (MCP): A comprehensive introduction for developers

Auth & identity

Mar 28, 2025

Author: Reed McGinley-Stempel

![Model Context Protocol (MCP): A comprehensive introduction for developers](https://cdn.sanity.io/images/3jwyzebk/production/e3f8d6ac0106744a859c305e903837fa0c68108c-877x621.png?auto=format&fit=max&w=1920&q=75)

## Executive summary

**Model Context Protocol (MCP)** is an open standard that bridges AI models with external data and services, allowing Large Language Models (LLMs) to make structured API calls in a consistent, secure way. This post will introduce MCP, explain why it’s valuable for connecting AI systems, compare it to existing approaches like ChatGPT plugins and manual API integrations, and dive into its recent support for OAuth-based authentication. We’ll also explore a bit of code to see MCP in action.

MCP acts as a universal adapter between AI tools and external services, eliminating the need for custom integration code for each tool or API. Much like USB-C simplifies connectivity across diverse devices, MCP provides a uniform method for AI models to invoke external functions, retrieve data, or use predefined prompts. At its core, MCP offers one interface that connects to many different systems.

## What is Model Context Protocol MCP?

MCP is essentially a **universal adapter** between AI applications and external tools or data sources. It [defines a common protocol](https://www.anthropic.com/news/model-context-protocol#:~:text=MCP%20addresses%20this%20challenge,to%20the%20data%20they%20need) (built on JSON-RPC 2.0) that lets an AI assistant invoke functions, fetch data, or use predefined prompts from external services in a structured manner. Instead of every LLM app needing custom code for each API or database, [MCP provides one standardized “language” for all interactions.](https://medium.com/data-and-beyond/the-model-context-protocol-mcp-the-ultimate-guide-c40539e2a8e7#:~:text=https%3A%2F%2Fmodelcontextprotocol)

The MCP layer enables AI applications to securely access and interact with external data sources and tools. It serves as a bridge between large language models (LLMs) and various databases, applications, or APIs, facilitating seamless integration and functionality without the need for extensive custom coding.

MCP uses a **client-server architecture** to achieve this. The AI-powered application (e.g. a chatbot, IDE assistant, or agent) acts as the *host* and runs an MCP *client* component, while each external integration runs as an MCP *server*. The server exposes capabilities (like functions, data resources, or prompt templates) over the MCP protocol, and the client connects to it to utilize those capabilities. This separation means the AI model doesn’t talk to APIs directly; instead, it goes through the MCP client/server handshake, which structures the exchange.

![MCP server connections](https://cdn.sanity.io/images/3jwyzebk/production/da5293781d0d860d74d785ac249597d9e39af044-1026x629.png?auto=format&fit=max&w=3840&q=75)

[Source](https://generativeai.pub/mcp-servers-explained-python-and-agentic-ai-tool-integration-aa2ddca6cbe5)

## Why MCP is Valuable

In traditional setups, connecting an AI model to external data or actions was tedious and ad-hoc. Developers often had to write one-off integrations for each API or database they wanted the model to use, dealing with different auth, data formats, and error handling for each. MCP changes the game by **standardizing these interactions**. Key benefits [include](https://huggingface.co/blog/Kseniase/mcp#:~:text=,the%20client%20will%20pick%20on):

- **Rapid Tool Integration**: With MCP, you can plug in new capabilities without custom-coding each from scratch. If an MCP server exists for, say, Google Drive or a SQL database, any MCP-compatible AI app can connect to it and immediately gain that ability. This is a *huge* win for automation—AI agents can fetch documents, query databases, or call APIs as needed, just by adding the appropriate server. It’s like having a library of ready-made “plugins” that all speak the same language. MCP servers serve as lightweight programs that expose specific capabilities through a standardized protocol, acting as intermediaries between the Cursor and various external tools or data sources.
- **Autonomous Agents**: MCP empowers more autonomous AI behavior. Agents are not limited to their built-in knowledge; they can actively retrieve information or perform actions in multi-step workflows. For example, a sophisticated agent might use MCP to gather data from a CRM, then send an email via a communications tool, then log a record in a database – all in one seamless chain. By enabling fluid, context-aware, multi-step interactions, MCP helps AI agents move closer to true autonomous task execution. As one observer noted, MCP turns an AI from an isolated “brain” into a versatile “doer” by giving it standardized access to real-world tools and data.
- **Reduced Friction and Setup**: Because MCP acts as a universal interface, developers avoid the fragmentation of maintaining separate integrations. Once an application supports MCP, it can connect to any number of services through a single mechanism. This dramatically reduces the manual setup required each time you want your AI to use a new API. Teams can focus on higher-level logic rather than reinventing connection code for the 10th time. As Anthropic put it, MCP replaces fragmented integrations with a simpler, more reliable single protocol for data access.
- **Consistency and Interoperability**: MCP enforces a consistent request/response format across tools. This means your AI app doesn’t have to handle one HTTP response for Service A, another XML for Service B, etc. The model’s outputs (function calls) and the tool results are all passed in a [uniform JSON structure](https://dev.to/fotiecodes/function-calling-vs-model-context-protocol-mcp-what-you-need-to-know-4nbo#:~:text=Purpose%20Converts%20user%20prompts%20into,Ensures%20interoperability%20across%20multiple%20tools). That consistency makes it easier to debug and scale. It also future-proofs your integration logic – even if you switch underlying model vendors, MCP’s interface to the tools remains the same.
- **Two-Way Context**: Unlike simple API calls, MCP supports maintaining context and ongoing dialogue between the model and the tool. An MCP server can provide *Prompts* (predefined prompt templates for certain tasks) and *Resources* (data context like documents) in addition to tools. This means the AI can not only “call an API” but also ingest reference data or follow complex workflows guided by the server. The protocol was designed to support rich interactions, not just one-off queries. This is especially useful in applications like coding assistants (where an AI might iterate with a development environment via MCP) or complex decision-making tasks that require back-and-forth with various data sources.

In short, MCP brings a **scalable, plug-and-play approach** to enhancing LLMs. It lets AI systems securely tap into the “live” data and actions they need, without each developer having to reinvent the wheel. Early adopters of MCP have already built servers for tools like Google Drive, Slack, GitHub, databases, and more – showcasing how AI agents can use MCP to work with enterprise content repositories, dev ops tools, and other real-world systems.

## The MCP architecture – How it works at-a-glance

### Client-Server structure

MCP follows a clear client-server architecture:

- **MCP Client**: Embedded in AI applications (chatbots, IDE assistants, automation agents).
- **MCP Server**: Exposes external capabilities such as functions (tools), resources (data), and prompts (templates).

All interactions occur through standardized JSON-RPC messages, maintaining a secure, structured exchange:

**Example JSON-RPC Request:**

For example, to list available tools, an MCP client sends a request like this:

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

The server would reply with a structured JSON listing the tools (each with a name, description, and input schema). For instance, a server might advertise a get_weather tool and describe what inputs it needs.

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    { "name": "get_weather", "description": "Retrieves weather data.", "schema": { "location": "string" } }
  ]
}
```

Later, when the LLM decides to use a tool, the client invokes a call to do so. The MCP server executes the function and returns the result in a structured JSON response. The MCP client (within the host app) can then feed that result back into the model’s context or response. In practice, the host application mediates this process: it translates the LLM’s intent (often via the model’s function call output) into an MCP request, and then passes the server’s structured result back to the LLM. This two-way exchange is **secure and controlled** – the model can only call the specific tools the server exposes, and all data passing in/out goes through the defined protocol.

## Building and deploying MCP servers

Building and deploying MCP servers is a crucial step in leveraging the Model Context Protocol (MCP) for AI integrations. MCP servers act as intermediaries between AI models and external data sources or tools, enabling seamless communication and data exchange. One of the standout features of MCP is its flexibility in server development. Developers can use any programming language that can print to stdout or serve an HTTP endpoint, allowing them to choose their preferred language and technology stack.

When building an MCP server, it’s essential to consider the architecture and design. MCP follows a client-server architecture, where a host application can connect to multiple servers. This architecture enables scalability and flexibility, allowing developers to design MCP servers that handle various tasks and functions, such as data processing, tool integration, or AI model management.

Deploying MCP servers can be done in various environments, including local development environments, cloud platforms, or on-premises infrastructure. For instance, Cloudflare provides a robust platform for building and deploying remote MCP servers, making it easier to manage and scale MCP deployments. This flexibility ensures that MCP servers can be tailored to meet the specific needs of different applications and environments, whether it’s a local setup for development or a cloud-based solution for production.

By focusing on a well-designed architecture and leveraging the flexibility of MCP, developers can create powerful and scalable MCP servers that enhance the capabilities of AI models, enabling them to interact seamlessly with external data sources and tools.

## MCP clients and tools

MCP clients and tools are essential components of the Model Context Protocol ecosystem. MCP clients are applications that connect to MCP servers to access external data sources or tools. These clients can be built using various programming languages and frameworks, such as Python, JavaScript, or Java, providing developers with the flexibility to choose the best tools for their specific needs.

MCP tools, on the other hand, are software components that provide specific capabilities or functions to MCP clients. These tools can be integrated with MCP servers to enable features such as data processing, AI model management, or tool integration. Examples of MCP tools include Claude Desktop, which provides a chat interface for interacting with AI models, and Cursor, which offers a plugin system for extending AI capabilities.

Developers can build custom MCP clients and tools to meet specific use cases or requirements. This flexibility allows for innovation and experimentation in the MCP ecosystem, enabling developers to create new and exciting applications. Whether it’s a specialized tool for data analysis or a client application that integrates with multiple MCP servers, the possibilities are vast.

By leveraging MCP clients and tools, developers can create robust and versatile applications that harness the full potential of AI models, enabling them to interact with a wide range of external data sources and tools seamlessly.

## Comparing MCP to other approaches

Let’s compare a few approaches that existed before or alongside MCP:

- **Custom Integrations & API Key Management**: The most common traditional approach was to write custom code for each service and supply the LLM with credentials (API keys or tokens) to use those integrations. For example, you might write a Python function to query an API, give the LLM the ability to call that function, and manually handle the API key in your backend. This approach is labor-intensive and doesn’t scale – each new data source requires new code, and each environment must securely manage API keys. It often led to brittle systems, since every integration was unique. By contrast, MCP centralizes and standardizes these interactions: the AI agent just needs to handle the MCP protocol, and *any* MCP server (for any service) will work in a plug-and-play way. New servers can be added without changing the client’s code at all. Moreover, MCP provides a formal structure for authentication (discussed later) so that handing API keys to the AI isn’t done ad-hoc but through a secure protocol.
- **ChatGPT Plugins (OpenAI Plugins)**: In 2023, OpenAI introduced a plugins system for ChatGPT that allowed models to call external APIs defined by an OpenAPI spec. This was an early step toward standardized tool use, but it has limitations. Each plugin is essentially its own mini-integration (with its own API schema and authentication), and they need to be built/hosted individually. Only certain platforms (like ChatGPT or Bing Chat) can use those plugins, since it was a proprietary approach. Plugins also were mostly one-shot calls – the model would call an API and get info, without a persistent connection or ongoing exchange. MCP differs in that it’s **open and universal** (not tied to one provider or interface) and it supports rich two-way interactions and continuous context. Think of ChatGPT plugins as specialized tools in a closed toolbox, whereas MCP is an open-standard toolkit that any developer or AI platform can utilize. MCP’s standardized auth (especially OAuth) also means it can handle secure access to user data in a more uniform way than the plugin-by-plugin OAuth flows in ChatGPT’s system. In summary, ChatGPT plugins showed the value of standardizing API access for LLMs, but MCP takes it further by making it an open protocol and by enabling a persistent “conversation” between AI and services.
- **LLM Tool Frameworks (LangChain, Agentic libraries)**: Before MCP, many developers used frameworks like LangChain to give models tools. In these setups, you define a set of tool functions (with descriptions) and the agent’s prompting logic so the LLM can decide to use them. This works, but each tool still requires custom implementation behind the scenes – LangChain ended up with hundreds of tool integrations maintained in its library. Essentially, LangChain provided a *developer-facing* standard (a Python class interface) for integrating tools into an agent’s codebase, but nothing for the model to dynamically discover new tools at runtime. MCP is complementary to these frameworks, shifting the standardization to be *model-facing*. With MCP, an agent can discover and use any tool that an MCP server provides, even if the agent’s code didn’t explicitly include that tool ahead of time. In fact, LangChain has added support so it can treat MCP servers as just another tool source – meaning an agent built with LangChain can call MCP tools easily, leveraging the growing ecosystem of MCP servers. The difference is that MCP formalizes the interface over a protocol (JSON-RPC, with metadata, etc.), making it easier to plug into different environments, not just Python frameworks. Similarly, OpenAI’s native function calling feature can be seen as handling the *formatting* of a function call (the model outputs a JSON function call), whereas MCP handles the *execution* of that call in a standardized way. OpenAI’s function calling and MCP often work in tandem: the LLM produces a structured call, and the MCP client/server execute it and return the result, which together enables seamless tool use.

In essence, MCP isn’t the first attempt to connect LLMs with external APIs – but it learns from those past approaches (plugins, tool libraries, etc.) and unifies the solution. It provides an **open, model-agnostic protocol** that simplifies integration and authentication. Particularly around security and auth, MCP’s design (with OAuth support) avoids the patchwork of per-plugin keys or giving raw API keys to the model. Instead, authentication can be handled in a consistent, standardized flow as part of the protocol – a major step up from the status quo.

## MCP in action: technical deep dive

Let’s walk through a typical MCP interaction step-by-step to solidify how it works, and look at a bit of code. Imagine we have an AI assistant that wants to use an MCP server providing a set of tools (say, for a hypothetical “Neon” database service). The high-level flow is:

**1. Connect to the MCP Server** – The host application (AI assistant) initializes an MCP client and establishes a connection to the server. Depending on the server location, this could be via a local process (stdio) or a remote HTTP stream (SSE). Under the hood, the client sends an initialize[message to handshake protocol versions and capabilities](https://nshipster.com/model-context-protocol/#:~:text=Like%20LSP%2C%20MCP%20has%20clients,The%20server%20responds%20in%20kind).

**2. Discover Available Tools/Resources** – The client then queries what the server offers. As shown earlier, it might send {"method": "tools/list"} and get back a list of tool definitions. The assistant can use this to inform the LLM (for example, by including the tool list in a system prompt or via the model’s function schema, depending on implementation). For instance, using an SDK, this could be one line of code like:

```javascript
const tools = await mcpClient.request({ method: 'tools/list' }, ListToolsResultSchema);
```

which returns a structured list of tools. Each tool entry has a name, description, and JSON schema for inputs,[so the AI knows what it can do](https://neon.tech/blog/building-a-cli-client-for-model-context-protocol-servers#:~:text=,can%20use%20during%20our%20interaction).

**3. LLM Chooses a Tool** – When a user asks the AI something that requires external action, the LLM determines (often via prompt engineering or function calling capabilities) that a certain tool should be used. For example, user asks: *“What’s the latest price of AAPL stock?”* The LLM sees it should call get_current_stock_price(company="AAPL", format="USD"). The host application captures this intent (e.g., OpenAI’s function calling API would return a function name and arguments in JSON).

**4. Invoke the Tool via MCP** – The client now sends a tools/call request to the server with the chosen tool name and parameters. We saw an example JSON for this earlier. In code, using an SDK, it might look like:

```javascript
const result = await mcpClient.request({
    method: 'tools/call',
    params: { name: toolName, arguments: toolArgs }
}, CallToolResultSchema);
```

This will cause the server to execute the tool’s handler on its side. The server might be calling an external API, performing a database query, or whatever logic that tool encapsulates. The result (could be a simple value or a complex JSON object) is sent back in a result field of the MCP response.
