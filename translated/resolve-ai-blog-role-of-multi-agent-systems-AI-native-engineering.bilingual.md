# Role of Multi Agent Systems in Making Software Engineers AI-native

# 多智能体系统在让软件工程师成为 AI 原生工程师中的角色

Back

返回

7 min read

7 分钟阅读

# The role of multi agent systems in making software engineers AI-native

# 多智能体系统在让软件工程师成为 AI 原生工程师中的角色

Written by

作者

- Spiros XanthosFounder and CEO
- Gabor AngeliResearch Engineer
- Bharat KhandelwalResearch Engineer

- Spiros Xanthos 创始人兼 CEO
- Gabor Angeli 研究工程师
- Bharat Khandelwal 研究工程师

September 26, 2025

2025 年 9 月 26 日

Generative AI has transformed [software development](https://resolve.ai/glossary/what-is-the-future-of-software-engineering) so dramatically that you can spin up entire services in hours, yet understanding what went wrong with those services still demands painstaking work across fragmented tools. From code generation to code review, coding agents handle the build side. But [production debugging](https://resolve.ai/glossary/what-is-debugging)? That's still manual. Take the following example:

生成式 AI 已经彻底改变了[软件开发](https://resolve.ai/glossary/what-is-the-future-of-software-engineering)：你可以在几个小时内搭起整套服务；但要弄清这些服务到底出了什么问题，仍然需要在彼此割裂的工具之间做费力的排查。从代码生成到代码评审，编码智能体负责了构建这一侧。但[生产环境调试](https://resolve.ai/glossary/what-is-debugging)呢？那仍然是手工活。来看下面这个例子：

The problem isn't AI's capability; it's how we architect AI systems. Most engineering teams still use AI-powered tools to execute the same workflows faster, not reimagining how software development and production operations should work end-to-end.

问题不在于 AI 的能力，而在于我们如何架构 AI 系统。多数工程团队仍然只是用 AI 工具把同样的工作流跑得更快，而没有重新设想软件开发与生产运维应当如何端到端地运作。

At Resolve AI, we've been building multi-agent systems for engineers to work on [production systems](https://resolve.ai/glossary/what-are-production-systems-in-software-engineering). We've been advocating that engineering should be AI-native (where engineers primarily interface with [autonomous agents](https://resolve.ai/glossary/what-is-agentic-ai) to work on production systems), while most gen AI conversations in software engineering were centered on writing AI generated code with copilots and coding assistants.

在 Resolve AI，我们一直在为工程师构建多智能体系统，让他们能够在[生产系统](https://resolve.ai/glossary/what-are-production-systems-in-software-engineering)上工作。我们一直主张工程应当是 AI 原生的——工程师主要通过[自主智能体](https://resolve.ai/glossary/what-is-agentic-ai)与生产系统打交道；而软件工程领域里大多数生成式 AI 的讨论，却都集中在用 Copilot 和编码助手写出 AI 生成的代码。

We recently presented our approach to [Stanford's graduate AI program](https://www.youtube.com/watch?v=z7RBPQL0rZ4), diving deep into the AI agents and their architectural patterns that enable AI-native engineering workflows.

最近我们在[斯坦福大学的研究生 AI 课程](https://www.youtube.com/watch?v=z7RBPQL0rZ4)上介绍了我们的方案，深入讲解了 AI 智能体以及支撑 AI 原生工程工作流的架构模式。

### **What is AI-native engineering? Why is it important?**

### **什么是 AI 原生工程？为什么它很重要？**

AI-Native Engineering is where engineers primarily interface with AI to orchestrate their work: be it writing code or working on production systems. *AI-native* is a significant departure from just “*using AI”* where engineers are still interfacing with their systems and tools, but using AI to speed up individual steps of the process.

AI 原生工程指的是：工程师主要通过 AI 来编排自己的工作，无论是写代码还是在生产系统上工作。*AI 原生*与仅仅「*使用 AI*」有根本区别——在后一种情况下，工程师仍然直接与自己的系统和工具打交道，只是用 AI 来加速流程中的单个步骤。

**Here is an example workflow to showcase the distinction.**

**下面用一个示例工作流来说明这种区别。**

AI-Assisted: You use AI tools to work faster on complex tasks. The workflow remains human-centric: Engineer → Systems and tools → Correlation → Action. *Engineers still interface with tools, just using AI to perform individual tasks faster*

AI 辅助：你使用 AI 工具更快地完成复杂任务。工作流仍然以人为中心：工程师 → 系统与工具 → 关联 → 行动。*工程师仍然直接与工具打交道，只是用 AI 更快地完成单个任务*

AI-Native: AI becomes your primary interface for production work. The workflow becomes AI-led: Engineer → Natural Language Request → AI System → Response / Action. *Engineers set goals and let AI agents handle the operational work*

AI 原生：AI 成为你处理生产工作的主要界面。工作流变成由 AI 主导：工程师 → 自然语言请求 → AI 系统 → 响应 / 行动。*工程师设定目标，让 AI 智能体承担操作性工作*

![Screenshot 2025-09-25 at 6.05.44 PM.png](/_next/image?url=https%3A%2F%2Fresolve-prod-strapi-bucket.s3.us-east-2.amazonaws.com%2FScreenshot_2025_09_25_at_6_05_44_PM_4cb3a87090.png&w=3840&q=75)

![Screenshot 2025-09-25 at 6.05.44 PM.png](/_next/image?url=https%3A%2F%2Fresolve-prod-strapi-bucket.s3.us-east-2.amazonaws.com%2FScreenshot_2025_09_25_at_6_05_44_PM_4cb3a87090.png&w=3840&q=75)

Take incident response as an example. In AI-assisted workflows, you're still generating hypotheses, deciding which evidence matters, and manually correlating signals across tools. AI helps with data retrieval and analysis, but you're doing the heavy lifting in investigation.

以事故响应为例。在 AI 辅助的工作流中，你仍然要自己提出假设、判断哪些证据重要、手工关联跨工具的信号。AI 帮助完成数据检索与分析，但调查中的重活仍然由你来干。

AI-native incident response operates differently: AI agents perform real-time triage of investigation priorities, generate competing hypotheses in parallel, and refine theories through successive iterations based on cross-system evidence. Instead of asking "Can you analyze these logs?" you say "Resolve this checkout failure" and agents coordinate the entire investigation.

AI 原生的事故响应方式不同：AI 智能体实时分诊调查优先级，并行生成相互竞争的假设，并根据跨系统的证据在一次次迭代中修正理论。你不再问「你能分析这些日志吗？」，而是说「解决这个结账失败」，由智能体协调整个调查过程。

This isn't just faster. It changes what problems deserve engineering attention. When AI agents handle log analysis, metric correlation, and deployment timeline reconstruction, engineers operate at a higher-level, focusing on architectural decision-making and system design rather than tactical investigation.

这不仅仅是更快。它改变了哪些问题值得投入工程注意力。当 AI 智能体承担日志分析、指标关联和部署时间线重建时，工程师就在更高层面上工作，专注于架构决策与系统设计，而不是战术性的调查。

The shift requires persistent AI agents, not just AI tools. While AI models like those from OpenAI or Anthropic can accelerate individual tasks, only stateful agents can maintain investigation context, coordinate across multiple tools, and execute complex tasks across the full incident lifecycle autonomously.

这种转变需要持久的 AI 智能体，而不只是 AI 工具。虽然 OpenAI 或 Anthropic 这类厂商的 AI 模型能加速单个任务，但只有有状态的智能体才能保持调查上下文、跨多个工具协调，并自主执行贯穿整个事故生命周期的复杂任务。

### **Why are multi-agent systems essential to make engineering AI-native?**

### **为什么多智能体系统对实现 AI 原生的工程必不可少？**

Modern production systems exhibit what academics call "irreducible interdependence": understanding them requires specialized knowledge across domains that cannot be unified into a single coherent model. This is the insight most builders miss: No single AI tool or set of AI models can maintain expert-level knowledge across all these domains while coordinating a real-time investigation.

现代生产系统呈现出学术界所说的「不可约的相互依赖」：要理解它们，需要横跨多个领域的专门知识，而这些知识无法统一成单一连贯的模型。这正是大多数构建者忽视的洞察：没有任何单一 AI 工具或模型组合，能在协调一场实时调查的同时，维持所有这些领域的专家级知识。

*For example: When API latency spikes 10x during a critical incident, the investigation requires simultaneous specialized agents performing real-time analysis: correlating traces across 50+ microservices, analyzing slow database queries and connection pool exhaustion, checking recent deployments and infrastructure changes, scanning auth logs for security anomalies, evaluating auto-scaling functions against current load patterns, and analyzing support tickets for customer impact with SLA context. Each of these functions requires domain-specific expertise and contextual data that no single system could effectively maintain.*

*例如：当一次关键事故中 API 延迟飙升 10 倍时，调查需要多个专业智能体同时做实时分析：关联横跨 50+ 微服务的 trace、分析缓慢的数据库查询与连接池耗尽、检查最近的部署与基础设施变更、扫描认证日志以发现安全异常、根据当前负载模式评估自动扩缩函数，并在 SLA 背景下分析支持工单以评估客户影响。每一项功能都需要特定领域的专业知识和上下文数据，没有哪个单一系统能有效地维持它们。*

At large-scale, as system complexity increases, individual AI tools lack the adaptability to handle exponential growth in context requirements. This is where multi-agent systems can scale by combining orchestration and individual domain specialization. This matrix provides an overview for engineering leaders. Find the row that matches your current state to understand its limitations:

在大规模场景下，随着系统复杂度上升，单个 AI 工具缺乏适应能力，无法应对上下文需求呈指数级增长。这正是多智能体系统能够发挥扩展性的地方：把编排与各领域的专业化结合起来。下面这张矩阵为工程负责人提供概览。找到与你当前状态相符的那一行，理解它的局限：

This framework reveals the technical limitations at each level:

这个框架揭示了每个层级的技术局限：

The progression reveals a fundamental architectural truth: Each level hits a different scalability ceiling. LLMs lack a persistent state. Tool-augmented LLMs can't maintain investigation context across multiple chats. Even with sophisticated prompt engineering, single agents become decision-making bottlenecks as system complexity grows. Only multi-agent systems can break through the sequential reasoning constraint that limits all previous approaches. They enable parallel hypothesis testing while single agents must investigate sequentially, making them fundamentally unsuitable for the temporal demands of production incidents.

这个演进过程揭示了一条根本性的架构事实：每个层级都会撞上不同的可扩展性上限。LLM 缺乏持久状态。工具增强的 LLM 无法在多次对话之间维持调查上下文。即使有精巧的提示工程，随着系统复杂度增长，单个智能体也会成为决策瓶颈。只有多智能体系统才能突破限制此前所有方案的顺序推理约束。它们能实现并行的假设验证，而单个智能体只能顺序调查，因此从根本上不适合生产事故对时间的要求。

### **Building multi-agent systems is a hard engineering problem**

### **构建多智能体系统是一个困难的工程问题**

No off-the-shelf agent framework like LangChain solves this alone. Building production-ready multi-agent systems requires a rare combination of deep domain expertise and AI engineering prowess. Most attempts fail because teams have expertise in one area but not both. Here’s why this dual expertise is needed:

没有 LangChain 这类现成的智能体框架能单独解决这个问题。构建可用于生产的多智能体系统，需要把深厚的领域专业知识与 AI 工程能力罕见地结合起来。大多数尝试失败，是因为团队只具备其中一个领域的专长，而不是两者兼备。以下是为什么需要这种双重专长：

- **Domain expertise determines architecture**: You can't architect agents without understanding production realities. Only someone who's debugged production at 3 AM in a DevOps or SRE role knows that log patterns and metric anomalies require fundamentally different investigation strategies. When payment failures spike, you need both database expertise and infrastructure expertise to determine the root cause. Decisions like this aren’t AI problems. They're production decisions that shape how you build your multi agent system.
- **AI expertise makes agents work together**: Once you've decomposed the problem, you hit the hard part of computer science. Context propagation between agents isn't intuition. It is managing directed acyclic graphs of information flow where each agent's output feeds into the next agent's input. Orchestrating parallel agents requires formal coordination protocols to prevent race conditions and deadlocks. The system needs to learn continuously both from interactions and ephemeral failure modes. Get one step wrong in coordinating agents and your system gets progressively worse, not better.
- **The intersection creates breakthrough systems**: Domain knowledge without AI architecture is just expensive consulting. AI architecture without domain knowledge produces output that investigates the wrong things. The breakthrough happens when you combine both: knowing *what* database connection pools do under load (domain) with building agents that can *coordinate* pool health checks with deployment timeline analysis and upstream service validation: all running in parallel without stepping on each other (AI systems).

- **领域专业知识决定架构**：如果不了解生产环境的真实情况，就无法设计智能体架构。只有在 DevOps 或 SRE 岗位上凌晨 3 点排查过生产问题的人，才知道日志模式和指标异常需要根本不同的调查策略。当支付失败激增时，你需要同时具备数据库专业知识和基础设施专业知识，才能确定根因。这类决策不是 AI 问题。它们是生产决策，决定了你如何构建自己的多智能体系统。
- **AI 专业知识让智能体协同工作**：把问题拆解之后，你就会撞上计算机科学中最难的部分。智能体之间的上下文传播不是靠直觉就能做好的。它是在管理信息流动的有向无环图，其中每个智能体的输出都会成为下一个智能体的输入。编排并行智能体需要正式的协调协议，以防止竞态条件和死锁。系统需要持续从交互和短暂的失败模式中学习。在协调智能体时只要错一步，你的系统就会逐步变差，而不是变好。
- **两者的交叉造就突破性系统**：只有领域知识而没有 AI 架构，那只是昂贵的咨询。只有 AI 架构而没有领域知识，产出的结果会去调查错误的东西。突破发生在两者结合时：既知道数据库连接池在负载下会做*什么*（领域），又能构建出可以*协调*连接池健康检查、部署时间线分析和上游服务验证的智能体，让这些工作全部并行运行、互不干扰（AI 系统）。

At [Resolve AI](https://resolve.ai/product/overview), our team includes engineers with over two decades of experience in production systems, founders who co-created [OpenTelemetry](https://resolve.ai/glossary/what-is-opentelemetry) (one of the most impactful open-source observability projects in the ecosystem) and researchers with deep artificial intelligence expertise who are the minds behind Google DeepResearch and Gemini Agents. This combination lets us build systems that don't just understand that "payment failures are bad" but know to check connection pool metrics and correlate with upstream service degradation. All the while managing complex agent orchestration that prevents circular investigations and maintains coherent narrative threads across parallel execution paths.

在 [Resolve AI](https://resolve.ai/product/overview)，我们的团队包括在生产系统领域拥有二十多年经验的工程师、共同创建了 [OpenTelemetry](https://resolve.ai/glossary/what-is-opentelemetry)（生态中最具影响力的开源可观测性项目之一）的创始人，以及深度人工智能专长、Google DeepResearch 和 Gemini Agents 背后大脑的研究人员。这种组合让我们构建出的系统，不仅知道「支付失败是坏事」，还知道要去检查连接池指标，并与上游服务劣化做关联。同时，它还能管理复杂的智能体编排，避免出现循环调查，并在并行的执行路径之间保持连贯的叙述线索。

### **About Resolve AI**

### **关于 Resolve AI**

Resolve AI is your always-on [AI SRE](https://resolve.ai/glossary/what-is-ai-sre) that helps you resolve incidents and run production. With Resolve AI customers like Salesforce, [Zscaler](https://resolve.ai/customers/zscaler), and [Coinbase](https://resolve.ai/customers/coinbase) have increased engineering velocity and systems reliability by putting machines on-call for humans and letting engineers just code. Learn more about AI-native engineering workflows at resolve.ai.

Resolve AI 是你随时在线的 [AI SRE](https://resolve.ai/glossary/what-is-ai-sre)，帮助你解决事故并运行生产环境。借助 Resolve AI，Salesforce、[Zscaler](https://resolve.ai/customers/zscaler) 和 [Coinbase](https://resolve.ai/customers/coinbase) 等客户把机器放到值班岗位上替人值守，让工程师专心写代码，从而提升了工程速度与系统可靠性。想进一步了解 AI 原生工程工作流，请访问 resolve.ai。

AI for prod ebook

面向生产的 AI 电子书

Learn how top engineering teams use AI to run production.

了解顶尖工程团队如何用 AI 运行生产环境。

Download

下载

See the agents that run and fix software in action

看看那些运行并修复软件的智能体是如何工作的

Join our engineering leads for "Behind the Build", a webinar series deep-dive into how we built agents that run software.

加入我们工程负责人的「Behind the Build」系列网络研讨会，深入了解我们如何构建运行软件的智能体。

Watch now

立即观看

## Keep reading

## 继续阅读

View all

查看全部

![Your human-in-the-loop is exhausted](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2Fyour_human_in_the_loop_is_exhausted_3751b434de.png&w=3840&q=75)

![Your human-in-the-loop is exhausted](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2Fyour_human_in_the_loop_is_exhausted_3751b434de.png&w=3840&q=75)

### [Your human-in-the-loop is exhausted](/blog/your-human-in-the-loop-is-exhausted)

### [你的「人在回路」已经疲惫不堪](/blog/your-human-in-the-loop-is-exhausted)

![Resolve AI Extends Production Context to Coding Agents](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2FUNMATCHED_agent_diagram_176d50cdc6.png&w=3840&q=75)

![Resolve AI Extends Production Context to Coding Agents](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2FUNMATCHED_agent_diagram_176d50cdc6.png&w=3840&q=75)

### [Resolve AI Extends Production Context to Coding Agents](/blog/resolve-ai-plugin-cursor-claude-code-codex)

### [Resolve AI 把生产上下文延伸给编码智能体](/blog/resolve-ai-plugin-cursor-claude-code-codex)

![Why Resolve AI: Token Efficiency at Scale](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2FUNMATCHED_organic_graphic_screenshot_4c290b5e18.png&w=3840&q=75)

![Why Resolve AI: Token Efficiency at Scale](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2FUNMATCHED_organic_graphic_screenshot_4c290b5e18.png&w=3840&q=75)

### [Why Resolve AI: Token Efficiency at Scale](/blog/why-resolve-ai-token-efficiency-at-scale)

### [为什么选择 Resolve AI：规模化下的 token 效率](/blog/why-resolve-ai-token-efficiency-at-scale)

![Proactively run production tasks with background agents](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2Fproactively_run_prod_with_background_agents_367c95c6a0.png&w=3840&q=75)

![Proactively run production tasks with background agents](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2Fproactively_run_prod_with_background_agents_367c95c6a0.png&w=3840&q=75)

### [Proactively run production tasks with background agents](/blog/proactively-run-prod-with-background-agents)

### [用后台智能体主动执行生产任务](/blog/proactively-run-prod-with-background-agents)
