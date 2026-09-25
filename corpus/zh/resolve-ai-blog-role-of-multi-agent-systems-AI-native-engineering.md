# 多智能体系统在让软件工程师成为 AI 原生工程师中的角色

返回

7 分钟阅读

# 多智能体系统在让软件工程师成为 AI 原生工程师中的角色

作者

- Spiros Xanthos 创始人兼 CEO
- Gabor Angeli 研究工程师
- Bharat Khandelwal 研究工程师

2025 年 9 月 26 日

生成式 AI 已经彻底改变了[软件开发](https://resolve.ai/glossary/what-is-the-future-of-software-engineering)：你可以在几个小时内搭起整套服务；但要弄清这些服务到底出了什么问题，仍然需要在彼此割裂的工具之间做费力的排查。从代码生成到代码评审，编码智能体负责了构建这一侧。但[生产环境调试](https://resolve.ai/glossary/what-is-debugging)呢？那仍然是手工活。来看下面这个例子：

问题不在于 AI 的能力，而在于我们如何架构 AI 系统。多数工程团队仍然只是用 AI 工具把同样的工作流跑得更快，而没有重新设想软件开发与生产运维应当如何端到端地运作。

在 Resolve AI，我们一直在为工程师构建多智能体系统，让他们能够在[生产系统](https://resolve.ai/glossary/what-are-production-systems-in-software-engineering)上工作。我们一直主张工程应当是 AI 原生的——工程师主要通过[自主智能体](https://resolve.ai/glossary/what-is-agentic-ai)与生产系统打交道；而软件工程领域里大多数生成式 AI 的讨论，却都集中在用 Copilot 和编码助手写出 AI 生成的代码。

最近我们在[斯坦福大学的研究生 AI 课程](https://www.youtube.com/watch?v=z7RBPQL0rZ4)上介绍了我们的方案，深入讲解了 AI 智能体以及支撑 AI 原生工程工作流的架构模式。

### **什么是 AI 原生工程？为什么它很重要？**

AI 原生工程指的是：工程师主要通过 AI 来编排自己的工作，无论是写代码还是在生产系统上工作。*AI 原生*与仅仅「*使用 AI*」有根本区别——在后一种情况下，工程师仍然直接与自己的系统和工具打交道，只是用 AI 来加速流程中的单个步骤。

**下面用一个示例工作流来说明这种区别。**

AI 辅助：你使用 AI 工具更快地完成复杂任务。工作流仍然以人为中心：工程师 → 系统与工具 → 关联 → 行动。*工程师仍然直接与工具打交道，只是用 AI 更快地完成单个任务*

AI 原生：AI 成为你处理生产工作的主要界面。工作流变成由 AI 主导：工程师 → 自然语言请求 → AI 系统 → 响应 / 行动。*工程师设定目标，让 AI 智能体承担操作性工作*

![Screenshot 2025-09-25 at 6.05.44 PM.png](/_next/image?url=https%3A%2F%2Fresolve-prod-strapi-bucket.s3.us-east-2.amazonaws.com%2FScreenshot_2025_09_25_at_6_05_44_PM_4cb3a87090.png&w=3840&q=75)

以事故响应为例。在 AI 辅助的工作流中，你仍然要自己提出假设、判断哪些证据重要、手工关联跨工具的信号。AI 帮助完成数据检索与分析，但调查中的重活仍然由你来干。

AI 原生的事故响应方式不同：AI 智能体实时分诊调查优先级，并行生成相互竞争的假设，并根据跨系统的证据在一次次迭代中修正理论。你不再问「你能分析这些日志吗？」，而是说「解决这个结账失败」，由智能体协调整个调查过程。

这不仅仅是更快。它改变了哪些问题值得投入工程注意力。当 AI 智能体承担日志分析、指标关联和部署时间线重建时，工程师就在更高层面上工作，专注于架构决策与系统设计，而不是战术性的调查。

这种转变需要持久的 AI 智能体，而不只是 AI 工具。虽然 OpenAI 或 Anthropic 这类厂商的 AI 模型能加速单个任务，但只有有状态的智能体才能保持调查上下文、跨多个工具协调，并自主执行贯穿整个事故生命周期的复杂任务。

### **为什么多智能体系统对实现 AI 原生的工程必不可少？**

现代生产系统呈现出学术界所说的「不可约的相互依赖」：要理解它们，需要横跨多个领域的专门知识，而这些知识无法统一成单一连贯的模型。这正是大多数构建者忽视的洞察：没有任何单一 AI 工具或模型组合，能在协调一场实时调查的同时，维持所有这些领域的专家级知识。

*例如：当一次关键事故中 API 延迟飙升 10 倍时，调查需要多个专业智能体同时做实时分析：关联横跨 50+ 微服务的 trace、分析缓慢的数据库查询与连接池耗尽、检查最近的部署与基础设施变更、扫描认证日志以发现安全异常、根据当前负载模式评估自动扩缩函数，并在 SLA 背景下分析支持工单以评估客户影响。每一项功能都需要特定领域的专业知识和上下文数据，没有哪个单一系统能有效地维持它们。*

在大规模场景下，随着系统复杂度上升，单个 AI 工具缺乏适应能力，无法应对上下文需求呈指数级增长。这正是多智能体系统能够发挥扩展性的地方：把编排与各领域的专业化结合起来。下面这张矩阵为工程负责人提供概览。找到与你当前状态相符的那一行，理解它的局限：

这个框架揭示了每个层级的技术局限：

这个演进过程揭示了一条根本性的架构事实：每个层级都会撞上不同的可扩展性上限。LLM 缺乏持久状态。工具增强的 LLM 无法在多次对话之间维持调查上下文。即使有精巧的提示工程，随着系统复杂度增长，单个智能体也会成为决策瓶颈。只有多智能体系统才能突破限制此前所有方案的顺序推理约束。它们能实现并行的假设验证，而单个智能体只能顺序调查，因此从根本上不适合生产事故对时间的要求。

### **构建多智能体系统是一个困难的工程问题**

没有 LangChain 这类现成的智能体框架能单独解决这个问题。构建可用于生产的多智能体系统，需要把深厚的领域专业知识与 AI 工程能力罕见地结合起来。大多数尝试失败，是因为团队只具备其中一个领域的专长，而不是两者兼备。以下是为什么需要这种双重专长：

- **领域专业知识决定架构**：如果不了解生产环境的真实情况，就无法设计智能体架构。只有在 DevOps 或 SRE 岗位上凌晨 3 点排查过生产问题的人，才知道日志模式和指标异常需要根本不同的调查策略。当支付失败激增时，你需要同时具备数据库专业知识和基础设施专业知识，才能确定根因。这类决策不是 AI 问题。它们是生产决策，决定了你如何构建自己的多智能体系统。
- **AI 专业知识让智能体协同工作**：把问题拆解之后，你就会撞上计算机科学中最难的部分。智能体之间的上下文传播不是靠直觉就能做好的。它是在管理信息流动的有向无环图，其中每个智能体的输出都会成为下一个智能体的输入。编排并行智能体需要正式的协调协议，以防止竞态条件和死锁。系统需要持续从交互和短暂的失败模式中学习。在协调智能体时只要错一步，你的系统就会逐步变差，而不是变好。
- **两者的交叉造就突破性系统**：只有领域知识而没有 AI 架构，那只是昂贵的咨询。只有 AI 架构而没有领域知识，产出的结果会去调查错误的东西。突破发生在两者结合时：既知道数据库连接池在负载下会做*什么*（领域），又能构建出可以*协调*连接池健康检查、部署时间线分析和上游服务验证的智能体，让这些工作全部并行运行、互不干扰（AI 系统）。

在 [Resolve AI](https://resolve.ai/product/overview)，我们的团队包括在生产系统领域拥有二十多年经验的工程师、共同创建了 [OpenTelemetry](https://resolve.ai/glossary/what-is-opentelemetry)（生态中最具影响力的开源可观测性项目之一）的创始人，以及深度人工智能专长、Google DeepResearch 和 Gemini Agents 背后大脑的研究人员。这种组合让我们构建出的系统，不仅知道「支付失败是坏事」，还知道要去检查连接池指标，并与上游服务劣化做关联。同时，它还能管理复杂的智能体编排，避免出现循环调查，并在并行的执行路径之间保持连贯的叙述线索。

### **关于 Resolve AI**

Resolve AI 是你随时在线的 [AI SRE](https://resolve.ai/glossary/what-is-ai-sre)，帮助你解决事故并运行生产环境。借助 Resolve AI，Salesforce、[Zscaler](https://resolve.ai/customers/zscaler) 和 [Coinbase](https://resolve.ai/customers/coinbase) 等客户把机器放到值班岗位上替人值守，让工程师专心写代码，从而提升了工程速度与系统可靠性。想进一步了解 AI 原生工程工作流，请访问 resolve.ai。

面向生产的 AI 电子书

了解顶尖工程团队如何用 AI 运行生产环境。

下载

看看那些运行并修复软件的智能体是如何工作的

加入我们工程负责人的「Behind the Build」系列网络研讨会，深入了解我们如何构建运行软件的智能体。

立即观看

## 继续阅读

查看全部

![Your human-in-the-loop is exhausted](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2Fyour_human_in_the_loop_is_exhausted_3751b434de.png&w=3840&q=75)

### [你的「人在回路」已经疲惫不堪](/blog/your-human-in-the-loop-is-exhausted)

![Resolve AI Extends Production Context to Coding Agents](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2FUNMATCHED_agent_diagram_176d50cdc6.png&w=3840&q=75)

### [Resolve AI 把生产上下文延伸给编码智能体](/blog/resolve-ai-plugin-cursor-claude-code-codex)

![Why Resolve AI: Token Efficiency at Scale](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2FUNMATCHED_organic_graphic_screenshot_4c290b5e18.png&w=3840&q=75)

### [为什么选择 Resolve AI：规模化下的 token 效率](/blog/why-resolve-ai-token-efficiency-at-scale)

![Proactively run production tasks with background agents](/_next/image?url=https%3A%2F%2Fmedia.website-prod.resolve.ai%2Fproactively_run_prod_with_background_agents_367c95c6a0.png&w=3840&q=75)

### [用后台智能体主动执行生产任务](/blog/proactively-run-prod-with-background-agents)
