# Good Context Good Code

# 好的上下文，好的代码

![Good context leads to good code: How we built an AI-Native Eng Culture](/content/images/size/w2000/2025/08/Gemini_Generated_Image_k6ucawk6ucawk6uc-1.jpeg)Humans and agents working together

![好的上下文带来好的代码：我们如何打造 AI 原生的工程文化](/content/images/size/w2000/2025/08/Gemini_Generated_Image_k6ucawk6ucawk6uc-1.jpeg)人类与智能体协同工作

Waleed Kadous, Charles Feng, Justin Berman, Dennis Yilmaz, Amr Elsayed, Mohammed Mogasbe, James Feng, Bruno Fantauzzi

Waleed Kadous、Charles Feng、Justin Berman、Dennis Yilmaz、Amr Elsayed、Mohammed Mogasbe、James Feng、Bruno Fantauzzi

## TL;DR

## TL;DR

Creating StockApp gave us the chance to build an AI-native development culture from scratch. Our experience is that this is materially (~2.5x) more productive than manual development, and considerably more efficient (~2x) than taking an existing development culture and enhancing it with AI. AI-native development isn't about replacing engineers—it's about creating systematic human-AI collaboration through meticulously crafted shared context. To do so, we’ve had to make some changes:

创建 StockApp 让我们有机会从零开始构建一种 AI 原生的开发文化。我们的经验是：这种方式的产出效率明显高于纯手工开发（约 2.5 倍），也比拿一套既有开发文化再用 AI 去增强要高效得多（约 2 倍）。AI 原生开发并不是要取代工程师 —— 它指的是通过精心打磨的共享上下文，建立起系统化的人机协作。为此，我们不得不做出一些改变：

- Organize all of your code, technical docs and agent guidance in a monorepo. It’s the shared human-agent workspace. With agents, docs are just as important as code.
- Start with a high-level design, align with the agent on that and work your way down to the code.
- Use agents everywhere you can as often as you can, but supervise and audit their work and consistently integrate new rules into their guidelines.
- Set up MCP servers and command line tools in your environment in order to give AI the context it needs to act with higher quality and confidence. Share that configuration among your team to increase consistency and quality of outcomes for all.
- Use multiple different agents to review work and approve it before a human reviews it. Human and multi-agent ensembles consistently outperform single agent or agent only approaches.

- 把全部代码、技术文档和智能体指引都组织到一个单一仓库里。它是人与智能体共享的工作区。有了智能体，文档和代码同样重要。
- 从高层设计开始，先和智能体在这份设计上对齐，再一路向下推进到代码。
- 凡是用得上、用得上的地方都尽量用智能体，但要监督并审计它们的工作，并持续把新规则并入它们的指引。
- 在环境里配置好 MCP 服务器和命令行工具，让 AI 获得以更高质量和更强信心行动所需的上下文。把这份配置在团队中共享，以提升所有人产出一致性与质量。
- 用多个不同的智能体来评审工作，并在人类评审之前先由它们批准。人类与多智能体集成的方式，始终优于单智能体或仅用智能体的方式。

## Details

## 细节

StockApp started in January 2025 with a unique opportunity: building an engineering culture designed from day one around AI-native development. Rather than retrofitting AI tools into existing processes, we architected our entire development workflow to leverage human-AI collaboration systematically.

StockApp 于 2025 年 1 月启动，带着一个独特的机会：从第一天起就围绕 AI 原生开发来设计一种工程文化。我们没有把 AI 工具硬塞进既有流程，而是把整个开发工作流都围绕系统化的人机协作来架构。

While measuring developer productivity is notoriously difficult, our subjective experience, supported by objective measurements[1], points to productivity gains of roughly 2.5x—significantly beyond what we've experienced elsewhere. Several of us have worked at companies where AI has been partially adopted, and there, the productivity gains due to AI have been in the 30 to 50 percent range. With collective experience from top-tier engineering organizations like Google, we have a firm grasp on what high-performance development looks like, and this is the most productive environment any of us have experienced. Furthermore, the productivity boost is only getting larger as the models improve (witness the release of [Claude 4.1](https://www.anthropic.com/news/claude-opus-4-1?ref=blog.stockapp.com) with its improvements in coding performance) and humans and agents learning to work more closely together. The latter is significant: we iterate and experiment a lot with how to work together, and even when we’ve used the same model, better techniques like those below have boosted productivity measurably.

虽然衡量开发者生产力出了名地困难，但我们的主观体验（并有客观测量数据[1]作为支撑）显示，生产力大约提升了 2.5 倍 —— 明显超出我们在别处的经历。我们中有几个人待过部分采用 AI 的公司，在那里，AI 带来的生产力提升在 30% 到 50% 之间。凭借来自 Google 这类顶级工程组织的集体经验，我们对高性能开发是什么样子有清晰的把握，而这是我们所有人经历过的最有生产力的环境。此外，随着模型不断改进（例如 [Claude 4.1](https://www.anthropic.com/news/claude-opus-4-1?ref=blog.stockapp.com) 在编码表现上的进步），以及人与智能体学会更紧密地协作，这种生产力提升还在扩大。后一点很重要：我们在如何协作上做了大量迭代和试验，即便使用同一个模型，下面这类更好的做法也能带来可测量的生产力提升。

Our core insight: **Good code is a side effect of good context.** The new AI-native development process is about how humans and agents progressively build and share context together. When done effectively, superior software artifacts naturally emerge.

我们的核心洞察是：**好的代码是好的上下文带来的副作用。** 全新的 AI 原生开发流程，关注的是人与智能体如何逐步共同构建并共享上下文。这件事做得好，优秀的软件产物就会自然涌现。

We want to share our development process in the hope that others will find it useful.

我们想分享自己的开发流程，希望别人也能从中获益。

One thing to emphasize is that this approach requires *more*expertise in software engineering, not less. Defining context effectively is at least as challenging technically as writing good code: you need to consider carefully what the most critical information is, and how the agent will interpret it; two things you don’t have to worry about when it’s all in your head. Furthermore, the blast radius when agents screw up can be large (misbehaving agents have nuked our dev databases a few times, for example), and when we’re using agents, we are usually paying full attention. Agents at their current level of development can definitely lead you down the wrong path, and it requires a vigilant, attentive and experienced eye to stop them.

需要强调一点：这种做法对软件工程专业能力的要求是*更高*，而不是更低。有效地定义上下文，在技术难度上至少不亚于写好代码：你必须仔细考虑哪些信息最关键、智能体会如何解读它；而当一切都在你脑子里时，这两件事你根本不用操心。此外，智能体搞砸时的波及范围可能很大（例如，行为失常的智能体有几次把我们开发数据库清空了），而且在用智能体时，我们通常是全神贯注的。以智能体目前的发展水平，它们完全可能把你带偏，需要一双警觉、专注且有经验的眼睛才能拦住它们。

## The basic development environment

## 基本的开发环境

To put our technical decisions in context, it helps to outline the essentials of our development environment. The web front-end is written in TypeScript, and the backend services are split between Python and TypeScript, all maintained in a single monorepo. For day-to-day coding assistance we lean on Claude Code, which most teammates run inside Cursor for real-time autocompletion; Cursor's own built-in AI is seldom used. Although we have tried VS Code, Windsurf, and the Gemini CLI, this configuration has proven to be the most effective for our workflow.

为了让我们的技术决策有背景可循，有必要先勾勒一下开发环境的要点。Web 前端用 TypeScript 编写，后端服务则分在 Python 和 TypeScript 两边，全部维护在单一仓库中。日常编码辅助我们依靠 Claude Code，大多数队友把它跑在 Cursor 里以获得实时自动补全；Cursor 自带的 AI 很少使用。虽然我们也试过 VS Code、Windsurf 和 Gemini CLI，但事实证明这套配置对我们的工作流最有效。

## Five principles we've learned

## 我们总结出的五条原则

All five principles stem from one idea: humans and agents must iteratively create, refine, and consume shared context. When that happens, great software emerges and the code itself becomes an intermediate artifact; much as assembly sits between high-level and machine code.

五条原则都源自同一个想法：人与智能体必须迭代地创建、改进并消费共享上下文。做到这一点，出色的软件就会涌现，而代码本身则成为一件中间产物；就像汇编介于高级语言与机器码之间那样。

### The repo is the shared workspace for humans and agents

### 仓库是人与智能体共享的工作区

Our repository is organized for machines as well as humans because AI performance depends heavily on accessible context. This is why context engineering now matters more than prompt engineering. It is also why having a monorepo is an important part of our operational process.

我们的仓库既为机器组织，也为人类组织，因为 AI 的表现很大程度上取决于能否取到上下文。这就是为什么上下文工程如今比提示工程更重要。这也是为什么采用单一仓库是我们运营流程中重要的一环。

Natural language is as critical as programming languages, so we treat English prose with the same care we give TypeScript or Python.

自然语言和编程语言同样关键，所以我们对待英文文本，就像对待 TypeScript 或 Python 一样用心。

To achieve this, the state of the system must be visible to both humans and agents. We intentionally put more into the repository than a human-only team would, because our repo isn't just for humans; it's for machines, too.

要做到这一点，系统的状态必须对人类和智能体都可见。我们有意往仓库里放了比纯人类团队更多的内容，因为我们的仓库不只是给人看的，也是给机器看的。

Our document-driven approach treats natural language artifacts as first-class citizens. Key context is stored in:

我们的文档驱动方法把自然语言产物当作一等公民。关键上下文存放在：

- **docs/designs/**: Product requirements, high-level goals, and schemas. This is the "why" and "what."
- **docs/plans/**: Detailed, phased implementation plans, often generated jointly by humans and agents. This is the "how."
- **docs/guides/**: Tutorials for APIs and tools, often drafted by an agent after reading relevant documentation.
- **schema.sql**: A single, canonical schema for the entire project, providing ground truth for data structures.
- **README.md & CLAUDE.md**: Placed throughout the repository, these files provide localized instructions for both humans and agents working in specific parts of the codebase.

- **docs/designs/**：产品需求、高层目标与 schema。这是「为什么」和「做什么」。
- **docs/plans/**：详细的分阶段实现计划，通常由人与智能体共同生成。这是「怎么做」。
- **docs/guides/**：API 与工具的教程，通常由智能体在阅读相关文档后起草。
- **schema.sql**：整个项目唯一的规范 schema，为数据结构提供标准答案。
- **README.md & CLAUDE.md**：散布在仓库各处，为在代码库特定部分工作的人和智能体提供本地化的说明。

### Hierarchical development allows progressive building of context

### 分层开发让上下文得以逐步积累

Better context leads to better code, but creating context is non-trivial. We work top-down, with humans and agents collaborating at each level:

更好的上下文带来更好的代码，但创建上下文并非易事。我们自上而下推进，在每一层由人与智能体协作：

1. **Design** – A human supplies key requirements and constraints; the agent drafts a design doc; both iterate and commit it.
1. **Plan** – The agent converts the design into phased tasks; the human reviews and approves.
1. **Implement** – The agent handles most coding; the human reviews the result.
1. **Backstop** – Tests and other safeguards ensure later changes don't erode hard-won context. The most obvious backstop is testing, but this more broadly includes any mechanism that enforces the context we've built.
1. **Review** – Human and agent perform a final review of the feature, ensuring it meets the goals outlined in the original design document.
1. **Update & refine** – Docs, CLAUDE.md files, and schemas are updated so future agents inherit accurate context.

1. **设计** —— 人类给出关键需求与约束；智能体起草设计文档；双方迭代并提交。
1. **计划** —— 智能体把设计转化为分阶段任务；人类评审并批准。
1. **实现** —— 智能体负责大部分编码；人类评审结果。
1. **兜底** —— 测试与其他保障手段确保后续改动不会侵蚀来之不易的上下文。最显而易见的兜底是测试，但更广义上，它包含任何能强制执行我们已构建上下文的机制。
1. **评审** —— 人与智能体对功能做最终评审，确保它符合原始设计文档中列出的目标。
1. **更新与改进** —— 更新文档、CLAUDE.md 文件和 schema，让未来的智能体继承准确的上下文。

### Use agents for *everything* unless there's a good reason not to

### 对所有事都用智能体，除非有充分理由不用

We use agents for almost every aspect of our work and before we undertake any task, we ask if it could be done with AI. As mentioned above, we rarely – if ever – let agents take the steering wheel unsupervised. We meticulously check what the agents do and recommend before hitting enter. We do not “vibe code”. This supervision and checking still requires our deepest technical expertise.

我们几乎在工作的每个方面都用智能体，在动手做任何任务之前，我们都会先问：这件事能不能用 AI 来做？如上所述，我们很少 —— 如果有的话 —— 让智能体在无人监督的情况下掌舵。在按下回车之前，我们会仔细核查智能体做了什么、建议了什么。我们不做「Vibe Coding」。这种监督与核查，仍然要求我们拿出最深的技术功底。

We wanted to enumerate some of the perhaps unconventional ways we use agents:

我们想列举一些或许不太常规的智能体用法：

- Agents are excellent sounding boards for ideas and can help with the more menial aspects of research such as surveying the available libraries for a task.
- Agents write most of our commit and PR messages.
- We instruct agents to update documents rather than editing those documents ourselves when there is enough context. For example, after major code changes the agent and human have built together, there is enough information to update README files, and design docs if there were changes to the design.
- We instruct agents to update the CLAUDE.md files rather than editing them ourselves. It knows how to instruct itself better than we do.
- We do not write prompts. We ask the agent to write them for us taking into account both the context and our “meta prompt.”
- We have agents write tests, though we are careful to ensure that the agents don’t “overmock” the tests which they have a tendency to do. More importantly, we ask the agents to update the tests after changes. Testing plays an even more important role in AI-native codebases because it is a critical backstop. Since agents literally have limited context (in terms of their context windows), there is a high tendency with agents to solve problems locally that break things globally. Extensive testing has helped us reduce this problem.
- Debugging is a joint activity between human and agent. Usually the human is the one that comes up with the hypothesis of the root cause, and then asks the agent to verify if it is. Agents appear far more competent at verifying hypotheses than coming up with them themselves. In addition, agents are excellent at instrumentation that would be too tedious for a human to do. One of the biggest lessons we've learned is how efficient AI is at debugging complex cross-library problems. We had a particularly gnarly bug where information had to go through four libraries between the LLM and the frontend. We asked the AI to insert debug statements through all the libraries (directly in the Python library directory), analyze the logs, and determine which library contained the bug.
- We instruct agents to look for improvements to make to the code, e.g., finding duplicate code, dead code, security issues, privacy issues, etc. We then ask agents to fix them.
- We rarely do manual merges when we have conflicts. Most of the time merges are relatively simple, and in complex cases, the agents are intelligent enough to stop and ask for guidance.

- 智能体是非常好的想法碰撞板，也能在研究中承担较为琐碎的部分，比如为某个任务调研可用的库。
- 我们的提交信息和 PR 描述大部分由智能体撰写。
- 当上下文足够时，我们让智能体去更新文档，而不是自己动手编辑。例如，在人与智能体共同完成较大的代码改动之后，信息已经足够更新 README 文件；如果设计有变动，也可以更新设计文档。
- 我们让智能体去更新 CLAUDE.md 文件，而不是自己编辑。它比自己更懂得如何给自己下指令。
- 我们不写提示词。我们请智能体替我们写，同时考虑上下文和我们的「元提示词」。
- 我们让智能体编写测试，但会小心确保智能体不要「过度 mock」测试 —— 它们有这种倾向。更重要的是，我们要求智能体在改动之后更新测试。在 AI 原生的代码库里，测试的作用更加重要，因为它是一道关键的兜底。由于智能体的上下文实际上是有限的（受上下文窗口限制），它们很容易在局部解决问题却破坏全局。大量测试帮助我们缓解了这个问题。
- 调试是人与智能体共同的活动。通常由人提出关于根因的假设，然后请智能体验证是否成立。智能体在验证假设方面显得比自行提出假设强得多。此外，智能体非常擅长人类做起来过于繁琐的插桩工作。我们学到的最重要的一课之一，就是 AI 在调试复杂的跨库问题上有何等高效。我们遇到过一个特别棘手的 bug，信息必须经过大语言模型与前端之间的四个库。我们让 AI 在所有库里插入调试语句（直接插到 Python 库目录中），分析日志，并判断出是哪个库含有该 bug。
- 我们让智能体寻找代码中可以改进之处，比如找出重复代码、死代码、安全问题、隐私问题等等。然后让智能体去修掉它们。
- 遇到冲突时，我们很少手工合并。多数时候合并都相对简单，而在复杂情况下，智能体足够聪明，会停下来寻求指引。

For every stage of development, we're basically trying to do as much as we can using agents. This level of agent autonomy is not magic; it's a direct result of our systematic investment in creating and maintaining shared context. It's because of the design documents and plans that the AI can write great commit messages and write prompts better than humans can.

在开发的每个阶段，我们基本上都在尽量用智能体做尽可能多的事。这种程度的智能体自主性不是魔法；它是我们系统性地投入于创建和维护共享上下文的直接结果。正是因为有了设计文档和计划，AI 才能写出比人类更好的提交信息和提示词。

### MCP and commands make understanding and augmenting context even easier

### MCP 与命令让理解和增强上下文更简单

We make extensive use of MCP (Model Context Protocol) servers in our system. We also give the AI access to powerful command line options to explore information itself. We have a script called install_mcp.sh that we run when we set up a new repo to install the MCP servers we use. At current count we have about 6 MCP servers we install. These include:

我们的系统大量使用 MCP（模型上下文协议）服务器。我们也让 AI 使用强大的命令行选项来自行探索信息。我们有一个名为 install_mcp.sh 的脚本，在搭建新仓库时就运行它来安装我们使用的 MCP 服务器。目前我们大约安装 6 个 MCP 服务器，其中包括：

- **Notion and Linear**: This gives us the chance to both get more context for decision making (e.g. reading a feature description in Linear) as well as a way of updating information, e.g. we can say something like "report that the issue we worked on is fixed" and it will update Linear. It’s also extremely convenient for creating new issues – so we can use it as a bridge between high level designs in notion and issues in linear with commands like “take the list of tasks at this page and add them to Linear.”
- **AWS and SQL Dev databases**: The agents can now directly read these sources of information to get the information they need to debug. For example, they can pull logs for a server from AWS to analyze and they can check that the information stored in the dev database is correct.
- **Git and GitHub commands**: To research previous versions of the code, to look at all the commits that have been submitted to get context, to create PRs, to fix repo challenges. Agents probably have a better understanding of how to manipulate Git than most engineers.

- **Notion 和 Linear**：这让我们既能获得更多用于决策的上下文（例如读取 Linear 中的功能描述），也能更新信息，比如我们可以说「把那个我们处理过的 issue 报告为已修复」，它就会更新 Linear。它在创建新 issue 时也极为方便 —— 我们可以把它当作 Notion 中的高层设计与 Linear 中的 issue 之间的桥梁，用类似「把这个页面上的任务列表加到 Linear 里」这样的命令。
- **AWS 和 SQL 开发数据库**：智能体现在可以直接读取这些信息源，获取调试所需的信息。例如，它们可以从 AWS 拉取某台服务器的日志进行分析，也可以检查开发数据库里存的信息是否正确。
- **Git 和 GitHub 命令**：用于研究代码的历史版本、查看已提交的全部提交以获取上下文、创建 PR、解决仓库中的难题。在如何操作 Git 这件事上，智能体可能比大多数工程师理解得更好。

Most exciting is how easy MCP servers make it to "bridge gaps" that would be difficult to do in other ways. For example, you can say things like: read the bug description in Linear, and go through the last 10 commits to identify which one most likely caused the bug.

最令人兴奋的是，MCP 服务器让「弥合差距」变得非常容易，而用其他方式很难做到。例如，你可以这样说：读取 Linear 里的 bug 描述，然后浏览最近 10 次提交，找出最可能是哪一次引入了这个 bug。

### Ensembles outperform individuals

### 集成优于个体

If there is one lesson old-school machine learning teaches us, it's that ensembles outperform individuals. There are a variety of techniques like random forests, stacking, bagging and boosting. In all of these techniques you build more than one classifier and then employ some kind of voting mechanism between them. As long as there is sufficient variety in the classifiers, you are likely to see considerably better results from an ensemble than any one individual.

如果说老派机器学习给我们留下了一条教训，那就是集成优于个体。有随机森林、堆叠、装袋和提升等多种技术。在所有这些技术中，你都会构建不止一个分类器，然后在它们之间采用某种投票机制。只要分类器之间有足够多样性，集成往往会比任何单个个体给出明显更好的结果。

Perhaps the most interesting MCP server we have is the [Zen MCP server](https://github.com/BeehiveInnovations/zen-mcp-server?ref=blog.stockapp.com). This allows Claude Code to also seek feedback from other LLMs like Gemini and o3. We have used this to enhance the performance of our system and we've found that different LLMs have strengths and weaknesses. We use this combined with the development process above, so after Claude Code finishes a design, for example, we will also get it reviewed by Gemini. This diversity helps in many ways, for example, Gemini has shown significantly better results in preemptively identifying security issues. Here’s a recent example where we were trying to work out how to implement auth for MCP servers, where o3 and Gemini differed in opinions. Gemini's Perspective: Strongly recommends payload-based auth as the primary choice, calling it "the most pragmatic and scalable solution" that "strikes the best balance between performance, scalability, and maintainability."

我们拥有的最有趣的 MCP 服务器或许是 [Zen MCP 服务器](https://github.com/BeehiveInnovations/zen-mcp-server?ref=blog.stockapp.com)。它让 Claude Code 也能向 Gemini、o3 等其他大语言模型征求反馈。我们用它增强了系统的表现，并发现不同的大语言模型各有长短。我们把它与上面的开发流程结合起来使用，比如当 Claude Code 完成一份设计后，我们还会让 Gemini 评审它。这种多样性在很多方面都有帮助，例如 Gemini 在预先识别安全问题上表现明显更好。这里有一个近期的例子：我们当时在琢磨如何为 MCP 服务器实现认证，o3 与 Gemini 的意见并不一致。Gemini 的观点：强烈推荐把基于有效载荷的认证作为首选，称它是「最务实、最可扩展的方案」，「在性能、可扩展性与可维护性之间取得了最佳平衡」。

o3's Perspective: More cautious, ranking per-user clients as #1 for production systems, citing security concerns and LLM interference. Rates payload-based auth as #2 but warns about token leakage risks and complexity.

o3 的观点：更为谨慎，把每用户客户端列为生产系统的第 1 选择，理由是安全顾虑以及来自大语言模型的干扰。它把基于有效载荷的认证排在第 2，但警告存在 token 泄漏风险和复杂度问题。

Ultimately, the human and the agents form an ensemble. The bridge that allows this ensemble to perform better than any individual member is shared context. This is why investing in context is the most important part of building an AI-native system.

最终，人类与智能体共同构成了一个集成。让这个集成表现优于任何单个成员的桥梁，就是共享上下文。这就是为什么在构建 AI 原生系统时，投资于上下文是最重要的部分。

*We're looking for exceptional engineers to help us push the boundaries of AI-native development and build great products at the intersection of AI and commerce. If you want to define the future of how software is built while creating transformative technology, contact us at*[*careers@stockapp.com*](mailto:careers@stockapp.com)*.*

*我们正在寻找出色的工程师，帮助我们拓展 AI 原生开发的边界，并在 AI 与商业的交汇处打造优秀产品。如果你想在创造变革性技术的同时定义软件构建方式的未来，请联系我们：*[*careers@stockapp.com*](mailto:careers@stockapp.com)*。*

## Footnotes

## 脚注

¹ **Development Metrics (Q2 2025)**: While developer productivity metrics should be interpreted cautiously, our objective measurements include: 1,098 PRs delivered in 13 weeks (84.5 PRs/week), 10.6 PRs per developer per week vs. ~1 PR/dev/week industry standard (LinearB 2025). But we are in the "build" phase of the project, usually the fastest phase, vs the industry standard "build + maintain" average.

¹ **开发指标（2025 年第二季度）**：开发者生产力指标应当谨慎解读，不过我们的客观测量数据包括：13 周内交付 1,098 个 PR（每周 84.5 个 PR），每位开发者每周 10.6 个 PR，而行业标准约为每位开发者每周 1 个 PR（LinearB 2025）。但我们处于项目的「构建」阶段，这通常是最快的阶段，而行业标准对应的是「构建 + 维护」的平均水平。
