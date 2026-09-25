# How Long Contexts Fail

# 长上下文为何会失效

---

---

title: "How Long Contexts Fail" date: 2025-06-22 author: Drew Breunig description: "Taking care of your context is the key to building successful agents. Just because there's a 1 million token context window doesn't mean you should fill it." tags: ["agents", "llm", "ai", "prompting", "context management"] url: https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html

title: "How Long Contexts Fail" date: 2025-06-22 author: Drew Breunig description: "管好上下文是打造成功智能体的关键。有 100 万 token 的上下文窗口，并不意味着你就该把它填满。" tags: ["agents", "llm", "ai", "prompting", "context management"] url: https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html

---

---

![](https://www.dbreunig.com/img/overload.jpg)

![](https://www.dbreunig.com/img/overload.jpg)

### Managing Your Context is the Key to Successful Agents

### 管好上下文，是打造成功智能体的关键

As frontier model context windows continue to grow[^longcontext], with many supporting up to 1 million tokens, I see many excited discussions about how long context windows will unlock the agents of our dreams. After all, with a large enough window, you can simply throw *everything* into a prompt you might need – tools, documents, instructions, and more – and let the model take care of the rest.

随着前沿模型的上下文窗口不断变大[^longcontext]，许多模型已经支持多达 100 万 token，我看到许多兴奋的讨论，认为长上下文窗口将解锁我们梦想中的智能体。毕竟，只要窗口足够大，你就可以把可能需要的一切——工具、文档、指令等等——统统丢进提示词，剩下的交给模型。

Long contexts kneecapped RAG enthusiasm (no need to find the best doc when you can fit it all in the prompt!), enabled MCP hype (connect to every tool and models can do any job!), and fueled enthusiasm for agents[^googledocs].

长上下文削弱了 RAG 的热情（既然能全部塞进提示词，何必再去找最好的那份文档！），助长了 MCP 的炒作（连上所有工具，模型就能做任何工作！），也点燃了人们对智能体的热情[^googledocs]。

But in reality, longer contexts do not generate better responses. Overloading your context can cause your agents and applications to fail in suprising ways. Contexts can become poisoned, distracting, confusing, or conflicting. This is especially problematic for agents, which rely on context to gather information, synthesize findings, and coordinate actions.

但现实是，更长的上下文并不会带来更好的响应。上下文过载会让你的智能体和应用以出人意料的方式失败。上下文可能被污染、被干扰、被混淆，或产生冲突。这对智能体尤其麻烦，因为智能体依赖上下文来收集信息、综合结论并协调行动。

Let's run through the ways contexts can get out of hand, then review methods to mitigate or entirely avoid context fails.

我们先逐一梳理上下文失控的几种方式，再回顾缓解乃至彻底避免上下文失效的方法。

<div class="sidenote">

<div class="sidenote">

<h2>Context Fails</h2>

<h2>上下文失效</h2>

<ul> <li><a href="#context-poisoning">Context Poisoning: When a hallucination makes it into the context</a></li> <li><a href="#context-distraction">Context Distraction: When the context overwhelms the training</a></li> <li><a href="#context-confusion">Context Confusion: When superfluous context influences the response</a></li> <li><a href="#context-clash">Context Clash: When parts of the context disagree</a></li> </ul>

<ul> <li><a href="#context-poisoning">上下文污染：当幻觉进入上下文</a></li> <li><a href="#context-distraction">上下文干扰：当上下文压过训练所得</a></li> <li><a href="#context-confusion">上下文混淆：当多余上下文影响响应</a></li> <li><a href="#context-clash">上下文冲突：当上下文各部分互相矛盾</a></li> </ul>

</div>

</div>

---

---

### Context Poisoning

### 上下文污染

*Context Poisoning is when a hallucination or other error makes it into the context, where it is repeatedly referenced.*

*上下文污染是指幻觉或其他错误进入上下文，并被反复引用。*

The Deep Mind team called out context poisoning in the [Gemini 2.5 technical report](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf), which [we broke down last week](https://www.dbreunig.com/2025/06/17/an-agentic-case-study-playing-pokémon-with-gemini.html). When playing Pokémon, the Gemini agent would occasionally hallucinate while playing, poisoning its context:

Deep Mind 团队在 [Gemini 2.5 技术报告](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf)中指出了上下文污染问题，[我们上周做过解读](https://www.dbreunig.com/2025/06/17/an-agentic-case-study-playing-pokémon-with-gemini.html)。在玩 Pokémon 时，Gemini 智能体会偶尔产生幻觉，从而污染自己的上下文：

> An especially egregious form of this issue can take place with “context poisoning” – where many parts of the context (goals, summary) are “poisoned” with misinformation about the game state, which can often take a very long time to undo. As a result, the model can become fixated on achieving impossible or irrelevant goals.

> 这类问题有一种尤其严重的表现形式，即「上下文污染」——上下文的许多部分（目标、摘要）被关于游戏状态的错误信息「污染」，而这类污染往往需要很长时间才能清除。结果，模型可能执迷于追求不可能或无关的目标。

If the "goals" section of its context was poisoned, the agent would develop nonsensical strategies and repeat behaviors in pursuit of a goal that cannot be met.

如果它上下文中的「目标」部分被污染，智能体就会发展出毫无意义的策略，并为了一个无法达成的目标重复某些行为。

### Context Distraction

### 上下文干扰

*Context Distraction is when a context grows so long that the model over-focuses on the context, neglecting what it learned during training.*

*上下文干扰是指上下文变得太长，以至于模型过度关注上下文，忽略了它在训练中学到的东西。*

As context grows during an agentic workflow—as the model gathers more information and builds up history—this accumulated context can become distracting rather than helpful. The Pokémon-playing Gemini agent demonstrated this problem clearly:

在智能体工作流中，随着上下文不断增长——模型收集更多信息、积累更多历史——这些累积的上下文可能变得干扰而非有帮助。玩 Pokémon 的 Gemini 智能体清楚地展示了这个问题：

> While Gemini 2.5 Pro supports 1M+ token context, making effective use of it for agents presents

> 尽管 Gemini 2.5 Pro 支持 1M+ token 上下文，把它有效地用于智能体仍是一个新的研究前沿。

a new research frontier. In this agentic setup, it was observed that as the context grew significantly beyond 100k tokens, the agent showed a tendency toward favoring repeating actions from its vast history rather than synthesizing novel plans. This phenomenon, albeit anecdotal, highlights an important distinction between long-context for retrieval and long-context for multi-step, generative reasoning.

在这个智能体设置中，可以观察到：当上下文显著增长到超过 100k token 后，智能体表现出倾向于重复其庞杂历史中的动作，而不是综合出新的计划。这一现象虽然只是个案，却凸显出一个重要区别：用于检索的长上下文，与用于多步生成式推理的长上下文并不相同。

Instead of using its training to develop new strategies, the agent became fixated on repeating past actions from its extensive context history.

智能体没有用训练所得去发展新策略，而是执迷于重复其庞大上下文历史中的过往动作。

For smaller models, the distraction ceiling is much lower. A [Databricks study](https://www.databricks.com/blog/long-context-rag-performance-llms) found that model correctness began to fall around 32k for Llama 3.1 405b and earlier for smaller models.

对较小的模型而言，干扰的上限要低得多。一项 [Databricks 研究](https://www.databricks.com/blog/long-context-rag-performance-llms)发现，Llama 3.1 405b 的正确率在 32k 左右就开始下降，更小的模型则更早。

If models start to misbehave long before their context windows are filled, what's the point of super large context windows? In a nutshell: summarization[^summarization] and fact retrieval. If you're not doing either of those, be wary of your chosen model's distraction ceiling.

如果模型在上下文窗口被填满之前很久就开始表现失常，那超大的上下文窗口意义何在？一句话：摘要[^summarization]与事实检索。如果你做的不是这两件事，就要警惕所选模型的干扰上限。

[^summarization]: In fact, in the Databricks study cited above, a frequent way models would fail when given long contexts is they'd return summarizations of the provided context, while ignoring any instructions contained within the prompt.

[^summarization]: 事实上，在上面引用的 Databricks 研究中，模型面对长上下文时常见的失败方式是：它会返回所给上下文的摘要，却忽略提示词中包含的任何指令。

### Context Confusion

### 上下文混淆

*Context Confusion is when superfluous content in the context is used by the model to generate a low-quality response.*

*上下文混淆是指模型把上下文中多余的内容用于生成低质量响应。*

For a minute there, it really seemed like *everyone* was going to ship an [MCP](https://www.dbreunig.com/2025/03/18/mcps-are-apis-for-llms.html). The dream of a powerful model, connected to *all* your services and *stuff*, doing all your mundane tasks felt within reach. Just throw all the tool descriptions into the prompt and hit go. [Claude's system prompt](https://www.dbreunig.com/2025/05/07/claude-s-system-prompt-chatbots-are-more-than-just-models.html) showed us the way, as it's mostly tool definitions or instructions for using tools.

有那么一阵子，看起来*所有人*都要发布一个 [MCP](https://www.dbreunig.com/2025/03/18/mcps-are-apis-for-llms.html)。一个强大的模型连上你*所有*的服务和*所有*东西、替你完成一切琐碎任务，这个梦想似乎近在眼前。只要把所有工具描述塞进提示词，然后按下开始。[Claude 的系统提示词](https://www.dbreunig.com/2025/05/07/claude-s-system-prompt-chatbots-are-more-than-just-models.html)给我们指了路，因为它主要就是工具定义或使用工具的指令。

But even if [consolidation and competition don't slow MCPs](https://www.dbreunig.com/2025/06/16/drawbridges-go-up.html), *Context Confusion* will. It turns out there can be such a thing as too many tools.

但即便[整合与竞争没有让 MCP 慢下来](https://www.dbreunig.com/2025/06/16/drawbridges-go-up.html)，*上下文混淆*也会。事实证明，工具确实可能太多。

The [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) is a tool-use benchmark that evaluates the ability of models to effectively use tools to respond to prompts. Now on its 3rd version, the leaderboard shows that *every* model performs worse when provided with more than one tool[^live]. Further, the Berkeley team, "designed scenarios where none of the provided functions are relevant...we expect the model's output to be no function call." Yet, all models will occasionally call tools that aren't relevant.

[Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) 是一个工具调用基准测试，用来评测模型有效使用工具来回应提示词的能力。目前已是第 3 版，该榜单显示：当提供的工具多于一个时，*每一个*模型的表现都会变差[^live]。此外，Berkeley 团队「设计了所有给定函数都不相关的场景……我们期望模型的输出应当是不调用任何函数」。然而，所有模型都会偶尔调用并不相关的工具。

Browsing the function-calling leaderboard, you can see the problem get worse as the models get smaller:

浏览这个函数调用榜单，你会看到模型越小，问题越严重：

![](https://www.dbreunig.com/img/gemma_irrelevance.png)

![](https://www.dbreunig.com/img/gemma_irrelevance.png)

A striking example of context confusion can be seen in a [recent paper](https://arxiv.org/pdf/2411.15399?) which evaluated small model performance on the [GeoEngine benchmark](https://arxiv.org/abs/2404.15500), a trial that features *46 different tools*. When the team gave a quantized (compressed) Llama 3.1 8b a query with all 46 tools it failed, even though the context was well within the 16k context window. But when they only gave the model 19 tools, it succeeded.

上下文混淆的一个突出例子出现在[最近一篇论文](https://arxiv.org/pdf/2411.15399?)中，该论文评测了小模型在 [GeoEngine 基准测试](https://arxiv.org/abs/2404.15500)上的表现，这项测试包含 *46 种不同的工具*。当团队把一个量化（压缩）过的 Llama 3.1 8b 连同全部 46 个工具一起给到某个查询时，它失败了，尽管上下文远在 16k 上下文窗口之内。但当他们只给模型 19 个工具时，它成功了。

The problem is: if you put something in the context *the model has to pay attention to it.* It may be irrelevant information or needless tool definitions, but the model *will* take it into account. Large models, especially reasoning models, are getting better at ignoring or discarding superfluous context, but we continually see worthless information trip up agents. Longer contexts let us stuff in more info, but this ability comes with downsides.

问题在于：只要你把某样东西放进上下文，*模型就得关注它*。它可能是不相关的信息，也可能是多余的工具定义，但模型*一定*会把它考虑进去。大型模型，尤其是推理模型，在忽略或丢弃多余上下文方面正变得越来越好，但我们不断看到毫无价值的信息让智能体出错。更长的上下文让我们能塞进更多信息，但这种能力也带来代价。

[^live]: If you're on the leaderboard, pay attention to the, "Live (AST)" columns. [These metrics use real-world tool definitions contributed to the product by enterprise](https://gorilla.cs.berkeley.edu/blogs/12_bfcl_v2_live.html), "avoiding the drawbacks of dataset contamination and biased benchmarks."

[^live]: 如果你在关注这个榜单，请注意「Live (AST)」这几列。[这些指标使用企业向该产品贡献的真实工具定义](https://gorilla.cs.berkeley.edu/blogs/12_bfcl_v2_live.html)，「避免了数据集污染和有偏基准测试的弊端」。

### Context Clash

### 上下文冲突

*Context Clash is when you accrue new information and tools in your context that conflicts with other information in the context.*

*上下文冲突是指你在上下文中累积的新信息和工具，与上下文中的其他信息相互矛盾。*

This is a more problematic version of *Context Confusion*: the bad context here isn't irrelevant, it directly conflicts with other information in the prompt.

这是*上下文混淆*更麻烦的一个版本：这里的坏上下文并不是不相关，而是直接与提示词中的其他信息相冲突。

A Microsoft and Salesforce team documented this brilliantly in a [recent paper](https://arxiv.org/pdf/2505.06120). The team took prompts from multiple benchmarks and 'sharded' their information across multiple prompts. Think of it this way: sometimes, you might sit down and type paragraphs into ChatGPT or Claude before you hit enter, considering every necessary detail. Other times, you might start with a simple prompt, then add further details when the chatbot's answer isn't satisfactory. The Microsoft/Salesforce team modified benchmark prompts to look like these multistep exchanges:

微软与 Salesforce 的一个团队在[最近一篇论文](https://arxiv.org/pdf/2505.06120)中出色地记录了这一点。该团队从多个基准测试中取来提示词，并把信息「分片」到多个提示词中。可以这样理解：有时你会坐下来，在按下回车之前先往 ChatGPT 或 Claude 里敲上几段话，把每个必要的细节都考虑周全。另一些时候，你可能先用一个简单的提示词开头，等聊天机器人的回答不满意时再补充更多细节。微软与 Salesforce 团队把基准测试的提示词改造成这类多轮交流的样子：

![](https://www.dbreunig.com/img/sharded_prompt.png)

![](https://www.dbreunig.com/img/sharded_prompt.png)

All the information from the prompt on the left side is contained within the several messages on the right side, which would be played out in multiple chat rounds.

左侧提示词中的全部信息，都包含在右侧的若干条消息里，而这些消息会在多轮对话中依次出现。

The sharded prompts yielded dramatically worse results, with an average drop of 39%. And the team tested a range of models – OpenAI's vaunted o3's score dropped from 98.1 to 64.1.

分片后的提示词带来的结果明显更差，平均下降 39%。该团队测试了多种模型——OpenAI 备受推崇的 o3 得分从 98.1 降到 64.1。

What's going on? Why are models performing worse if information is gathered in stages rather than all at once?

这是怎么回事？如果信息是分阶段收集而不是一次性给出，模型的表现为什么会更差？

The answer is *Context Confusion*: the assembled context, containing the entirety of the chat exchange, contains early attempts by the model to answer the challenge *before it has all the information*. These incorrect answers remain present in the context and influence the model when it generates its final answer. The team writes:

答案是*上下文混淆*：组装起来的上下文包含整段对话交流，其中也就包含了模型在*尚未掌握全部信息*时做出的早期尝试。这些错误答案仍然留在上下文中，并在模型生成最终答案时影响它。该团队写道：

> We find that LLMs often make assumptions in early turns and prematurely attempt to generate final solutions, on which they overly rely. In simpler terms, we discover that when LLMs take a wrong turn in a conversation, they get lost and do not recover.

> 我们发现，大语言模型常常在对话的前几轮就做出假设，并过早尝试生成最终解决方案，然后过度依赖这些方案。更简单地说，我们发现当大语言模型在对话中走错一步，它们就会迷失，并且不会恢复。

This does not bode well for agent builders. Agents assemble context from documents, tool calls, and from other models tasked with subproblems. All of this context, pulled from diverse sources, has the potential to disagree with itself. Further, when you connect to MCP tools you didn't create there's a greater chance their descriptions and instructions clash with the rest of your prompt.

这对智能体构建者可不是好消息。智能体会从文档、工具调用，以及被指派处理子问题的其他模型中组装上下文。所有这些从不同来源汇集而来的上下文，都有可能自相矛盾。更进一步，当你连接的不是自己创建的 MCP 工具时，它们的描述和指令与你提示词其余部分发生冲突的可能性就更大。

---

---

The arrival of million-token context windows felt transformative. The ability to throw everything an agent might need into the prompt inspired visions of superintelligent assistants that could access any document, connect to every tool, and maintain perfect memory.

百万 token 上下文窗口的出现让人感觉是一场变革。能把智能体可能需要的一切都丢进提示词，这激发了对超级智能助手的想象：它可以访问任何文档、连接每一个工具，并保持完美的记忆。

But as we've seen, bigger contexts create new failure modes. Context poisoning embeds errors that compound over time. Context distraction causes agents to lean heavily on their context and repeat past actions rather than push forward. Context confusion leads to irrelevant tool or document usage. Context clash creates internal contradictions that derail reasoning.

但正如我们所见，更大的上下文会制造新的失败模式。上下文污染埋入会随时间不断累积的错误。上下文干扰让智能体严重依赖上下文、重复过往动作，而不是向前推进。上下文混淆导致使用不相关的工具或文档。上下文冲突制造内部矛盾，让推理脱轨。

These failures hit agents hardest because agents operate in exactly the scenarios where contexts balloon: gathering information from multiple sources, making sequential tool calls, engaging in multi-turn reasoning, and accumulating extensive histories.

这些失效对智能体的打击最重，因为智能体恰恰运行在上下文会膨胀的场景中：从多个来源收集信息、连续进行工具调用、开展多轮推理，并累积大量历史记录。

Fortunately, there are solutions! In an upcoming post we'll cover techniques for mitigating or avoding these issues, from methods for dynamically loading tools to spinning up context quarantines.

幸运的是，解决方案是有的！在接下来的一篇文章中，我们会介绍缓解或避免这些问题的技术，从动态加载工具的方法到建立上下文隔离区。

**Read the follow up article, "[How to Fix Your Context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html)"**

**阅读后续文章「[如何修复你的上下文](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html)」**

---

---

[^longcontext]: Gemini 2.5 and GPT-4.1 have 1 million token context windows, large enough to throw [Infinite Jest](https://en.wikipedia.org/wiki/Infinite_Jest) in there, with plenty of room to spare.

[^longcontext]: Gemini 2.5 和 GPT-4.1 拥有 100 万 token 的上下文窗口，大到足以塞进一部 [Infinite Jest](https://en.wikipedia.org/wiki/Infinite_Jest) 还绰绰有余。

[^googledocs]: The "[Long form text](https://ai.google.dev/gemini-api/docs/long-context#long-form-text)" section in the Gemini docs sum up this optmism nicely.

[^googledocs]: Gemini 文档中的「[长文本](https://ai.google.dev/gemini-api/docs/long-context#long-form-text)」一节很好地概括了这种乐观情绪。
