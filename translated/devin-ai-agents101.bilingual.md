# Devin: Coding Agents 101

# Devin：编码智能体 101

Developer tooling has been rapidly evolving. Ten years ago, it was autocomplete and intellisense, capable of suggesting method names and carrying out programmatic refactors. Four years ago, it was copilots and tab complete, capable of writing the next couple lines of code for you. Two years ago, it was generative chatbots, capable of assisting your development and generating entire files for you. Today, it is autonomous agents, capable of taking initial descriptions to final pull requests with little human intervention. We've focused on realizing this vision over the past two years by building Devin. Now, interest in autonomous agents is reaching new heights, especially with recent releases of similar products [1]Other than Devin, some recent releases include Codex by OpenAI and Jules by Google. Some local agents like Cursor and Claude Code can be run in parallel workspaces to replicate a similar effect.. These agents can appear in many forms, including web apps, mobile apps, and integrations within popular tools like Slack, GitHub, Linear, and Jira.

开发者工具一直在快速演进。十年前是自动补全与智能提示，能建议方法名并执行程序化的重构。四年前是编程助手与 Tab 补全，能替你写下接下来几行代码。两年前是生成式聊天机器人，能辅助你的开发并为你生成整个文件。而今天是自主智能体，能在极少人工干预下，从最初的描述一路做到最终的拉取请求（PR）。过去两年，我们专注于通过构建 Devin 来实现这一愿景。如今，人们对自主智能体的兴趣正达到新高，尤其是近期同类产品的接连发布 [1]除 Devin 之外，近期的发布还包括 OpenAI 的 Codex 和 Google 的 Jules。一些本地智能体如 Cursor 和 Claude Code 可以在并行工作区中运行，以复现类似的效果。。这些智能体可以多种形态出现，包括网页应用、移动应用，以及集成到 Slack、GitHub、Linear 和 Jira 等常用工具之中。

While a human paired with an AI assistant can achieve more than any AI alone, an autonomous agent's ability to handle tasks end to end allows for a new level of multi-tasking, turning every engineer into an engineering manager.

与 AI 助手配对的人类能比任何单独的 AI 产出更多，而自主智能体端到端处理任务的能力，带来了全新层次的多任务并行，把每一位工程师都变成了工程管理者。

Adapting to working effectively alongside these new AI colleagues can take some time. Interestingly, we've observed that senior-to-staff level engineers tend to adopt and become proficient with these tools the fastest. Ultimately, these tools will become commonplace across all levels of engineering. Based on our experience and customer feedback, we want to share key insights and lessons learned to help everyone successfully integrate these tools into their workflows.

适应与这些新的 AI 同事高效协作需要一些时间。有意思的是，我们观察到资深到 Staff 级别的工程师往往最快接纳并熟练使用这些工具。最终，这些工具会普及到所有级别的工程工作中。基于我们的经验与客户反馈，我们想分享一些关键洞察与经验教训，帮助大家顺利把这些工具融入自己的工作流。

### Say *how* you want things done, not just what

### 说清你希望*如何*完成，不只是要做什么

Think of the agent as a junior coding partner whose decision-making can be unreliable. Simple tasks can be described directly, but for more complex tasks, clearly outline your preferred approach from the outset. Providing the agent with the overall architecture and logic upfront not only boosts its chances of success but also reduces your time reviewing code, as you will already be familiar with the intended method.

把智能体看作一位初级编码伙伴，它的决策未必可靠。简单的任务可以直接描述，但面对更复杂的任务，应当一开始就清楚说明你偏好的做法。提前把整体架构与逻辑交给智能体，不仅能提高它成功的概率，也能减少你评审代码的时间，因为你已经熟悉了预期的实现方式。

#### Example:

#### 示例：

Instead of "add unit tests," specify the functionality to test, identify important edge cases, and clarify what needs mocking, if anything.

不要说「加一些单元测试」，而要指明要测试的功能、识别重要的边界情况，并说明哪些东西需要 mock（如果确实需要）。

### Tell the agent where to start

### 告诉智能体从哪里开始

Think about where you'd start if you were handling the task yourself. Even if you don't know specific file or function names, mention the repository, relevant documentation, and key components involved. Clearly indicating these elements minimizes wasted effort and confusion.

想一想如果是你自己处理这个任务，你会从哪里入手。即使不知道具体的文件名或函数名，也要提到相关仓库、相关文档以及涉及的关键组件。把这些要素指明，能最大程度减少无用功与困惑。

"Please add support for Google models to our code. You should look at the latest docs [here](link) and create a new implementation file in the model groups directory"

「请为我们的代码加上对 Google 模型的支持。你应当查看最新文档 [这里](link)，并在 model groups 目录下新建一个实现文件」

### Practice defensive prompting

### 练习防御性提示

Imagine giving the same prompt to a new intern. Where would confusion or errors likely arise? Anticipate these points and proactively clarify your instructions to avoid ambiguity.

想象你把同一段提示词交给一位新来的实习生。哪里最可能出现困惑或错误？提前预判这些点，主动把指令讲清楚，避免歧义。

"Please fix the C++ bindings for our search module to pass the new unit tests. Be careful, you will probably need to recompile the bindings each time you change the code before you test."

「请修复搜索模块的 C++ 绑定，让新的单元测试通过。注意，你很可能每次改完代码都要先重新编译绑定，然后再测试。」

### Give access to CI, tests, types, and linters

### 提供对 CI、测试、类型检查与静态检查器的访问

Much of the magic of agents comes from their ability to fix their own mistakes and iterate against error messages. Providing strong feedback loops through tools like type checkers, linters, and unit tests greatly enhances their performance. Consider typed Python over plain Python, or TypeScript over JavaScript. Teach your agent how to run common checks and tests, ensuring it has all necessary packages and access rights. If the agent can interact with a browser, provide clear instructions on running your front-end development environment.

智能体的魔力很大程度来自它们能修正自己的错误，并针对错误信息反复迭代。通过类型检查器、静态检查器和单元测试等工具提供强反馈回路，能极大提升它们的表现。可以优先选择带类型的 Python 而不是普通 Python，或者选择 TypeScript 而不是 JavaScript。教会你的智能体如何运行常见的检查与测试，并确保它拥有所有必要的依赖包与访问权限。如果智能体能操作浏览器，就清楚说明如何启动你的前端开发环境。

Our team transitioned from mostly untyped Python SDKs to exclusively typed SDKs (this is also a good task ideally for coding agents).

我们团队从大多不带类型的 Python SDK 全面转向带类型的 SDK（这本身也是一个很适合交给编码智能体的任务）。

### Leverage your expertise

### 发挥你的专业能力

Everything above becomes easier when you're familiar with your codebase. Even simple tasks benefit from your ability to verify logic and results. Human oversight remains essential—ultimately, you hold responsibility for the final correctness of the code. Ownership and verification will continue to be critical responsibilities for human engineers, even as these tools become increasingly sophisticated.

当你熟悉自己的代码库时，上面的一切都会变得更容易。即使是简单的任务，也需要你验证逻辑与结果的能力。人的监督依然不可或缺——最终，代码正确与否的责任在你身上。即使这些工具越来越成熟，担责与验证仍将是人类工程师的关键职责。

### Take on new tasks immediately

### 立刻接下新任务

Imagine a teammate messaging you, "Hey, could we build X quickly?" or "We need to tweak Y." Instead of letting it interrupt your flow, just send a quick prompt to an autonomous agent to investigate or make the change. This frees you to stay focused on your main tasks. Got an interesting side project idea? Need to quickly prototype something, scrape data, or reproduce research? Delegate to your agent and circle back later.

想象一位同事给你发消息：「嘿，我们能快速把 X 做出来吗？」或者「Y 需要调整一下。」与其让这些事打断你的心流，不如直接给自主智能体发一条简短的提示词，让它去调研或动手修改。这样你就能继续保持专注，处理手头的主要任务。有个有趣的副业点子？需要快速做个原型、抓点数据，或者复现一篇研究？交给你的智能体，之后再回来看。

Many teams simply tag @Devin on Slack when discussing bug fixes or minor feature updates.

很多团队在 Slack 上讨论缺陷修复或小的功能更新时，直接 @Devin 即可。

### Code on the go

### 随时随地写代码

Picture yourself commuting or traveling when an urgent bug pops up, or you realize you might have left a mistake in your code. No worries! Autonomous agents often support mobile access, letting you address these issues instantly. Whether through Slack's mobile app or a dedicated mobile app, many agents let you resolve problems on the go, even if your wifi is sketchy.

想象你正在通勤或旅行途中，突然冒出一个紧急缺陷，或者你意识到代码里可能留下了一个错误。别担心！自主智能体通常支持移动端访问，让你能立刻处理这些问题。无论是通过 Slack 的手机应用还是专门的手机应用，很多智能体都能让你在路上解决问题，即使 Wi-Fi 信号很差。

Having this optionality has made our own team much more productive on car rides and flights.

这种可选择性让我们团队在乘车和飞行途中高效了许多。

### Hand off your chores

### 把手头的杂活交出去

Stuck bisecting for old commits or updating documentation for a new feature? Hand these repetitive tasks off to your agent. You'll save precious time and stay focused on more creative and impactful work.

在为老提交做二分查找，或者为新功能更新文档而卡住？把这些重复性任务交给你的智能体。你会省下宝贵的时间，专注于更有创造性、更有影响力的工作。

In our team, it is common for an engineer to ship a change and then have an agent update all the relevant docs & user-facing copy.

在我们团队，工程师发布一个改动之后，让智能体去更新所有相关文档和面向用户的文案，是很常见的做法。

### Skip the analysis paralysis

### 跳过分析瘫痪

Stuck deciding if a refactor will actually simplify your code? Can't choose between two architectural approaches? Have your agent implement both options. With concrete examples to compare, decision-making becomes straightforward, and you won't hurt any feelings by discarding a solution.

拿不准一次重构是否真能简化代码？在两种架构方案之间无法抉择？让你的智能体把两个方案都实现出来。有了具体例子可以对比，决策就变得简单了，而且丢弃某个方案也不会伤害任何人的感情。

When choosing between Lexical and Slate for text boxes, we had agents implement each. Slate won out for delivering the better end result.

在文本框方案上于 Lexical 和 Slate 之间做选择时，我们让智能体把两者各实现了一遍。最终 Slate 因为效果更好而胜出。

### Set up preview deployments

### 配置预览部署

Set your CI/CD pipeline to automatically create preview deployments with each new PR, giving you an instant live URL. This is particularly handy when reviewing frontend tasks completed by AI agents.

把 CI/CD 流水线设置为每来一个新 PR 就自动创建预览部署，给你一个可以立即访问的线上地址。在评审由 AI 智能体完成的前端任务时，这尤其方便。

Vercel is a deployment platform that makes preview deployments super easy.

Vercel 是一个部署平台，能让预览部署变得非常简单。

As the size and complexity of your pull requests grow beyond just a few files, handling them in a single pass becomes challenging. Yet, mastering how to delegate medium-to-large tasks (typically 1-6 hours of work) is where autonomous agents give the highest ROI. Rather than saving just a few minutes, you can reclaim hours of productivity. Smaller tasks might work effortlessly, but stretching the capabilities of agents to handle larger tasks brings the biggest returns.

当拉取请求的规模与复杂度超出寥寥几个文件时，想一次处理完就会变得困难。然而，真正掌握如何委派中等偏大的任务（通常相当于 1-6 小时的工作量），才是自主智能体投资回报最高的地方。你省下的不只是几分钟，而是数小时的生产力。小任务也许毫不费力就能完成，但把智能体的能力拉伸到更大的任务上，回报才最大。

### Automate your first drafts

### 自动生成初稿

For substantial tasks, using an autonomous agent to create an initial draft of your PR can kickstart progress and dramatically cut down your workload. Success here depends on clearly communicating your desired approach upfront. Think of yourself as the architect guiding junior developers. Clear, detailed instructions help avoid spending unnecessary time correcting fundamental misunderstandings in the agent's code.

对于体量较大的任务，用自主智能体先做出 PR 的初稿，可以启动进展并大幅削减你的工作量。这里的成败取决于你是否一开始就清楚说明期望的做法。把自己看作指导初级开发者的架构师。清晰、详细的指令能帮你避免把时间浪费在纠正智能体代码中根本性的误解上。

🛑 Remember, large tasks aren't completely hands-free (yet). Expect multiple feedback cycles for more challenging assignments, and anticipate some manual refinements for polish. A realistic goal is around 80% time savings, not complete automation, with your expertise remaining vital for verification and final quality assurance.

🛑 记住，大型任务（目前）还不能完全放手。越是棘手的任务，越要预期多轮反馈；也要预期为了打磨还需要一些人工微调。一个现实的目标是节省约 80% 的时间，而不是完全自动化，你的专业判断在验证与最终质量保证上依然至关重要。

### Co-develop a PRD

### 协同打磨 PRD（产品需求文档）

For tasks that are complex or vaguely defined, collaborating with your autonomous agent to create a detailed plan can be highly effective. It's perfectly okay if you initially don't know every nuance or requirement. Start by prompting your agent to explore discovery questions, like "How does our authentication system function?" or "Which services might be impacted?" You can also ask the agent to identify specific relevant code targets for you to confirm early on.

对于复杂或定义模糊的任务，与你的自主智能体协作制定一份详细计划会非常有效。一开始不清楚每一处细节或需求，完全没关系。可以先让智能体去探索一些调研性问题，比如「我们的认证系统是如何运作的？」或者「哪些服务可能受到影响？」你也可以让智能体指出具体相关的代码位置，供你尽早确认。

Certain agents, such as Devin and Claude Code, offer dedicated planning modes that focus on reading and exploring existing code rather than immediately modifying it. If you'd prefer deeper preparation before delegating a task, specialized codebase search tools like [deepwiki.com](http://deepwiki.com) and Devin Search can quickly provide insights into your codebase, helping streamline the process.

某些智能体（例如 Devin 和 Claude Code）提供专门计划模式，专注于读取和探索现有代码，而不是立刻修改它。如果你希望在委派任务之前做更充分的准备，像 [deepwiki.com](http://deepwiki.com) 和 Devin Search 这样的专用代码库检索工具能快速给出对代码库的洞察，帮助简化流程。

### Set checkpoints

### 设置检查点

For multi-part tasks, especially those involving multiple codebases, establish clear checkpoints along the way:

对于由多部分组成的任务，尤其是涉及多个代码库的任务，要在过程中设立明确的检查点：

Plan → Implement chunk → Test → Fix → Checkpoint review → Next chunk

规划 → 实现一个分块 → 测试 → 修复 → 检查点评审 → 下一分块

Explicitly request pauses after each significant phase, particularly for complex features built across multiple layers (e.g., database, backend, frontend). Use these checkpoints to ensure implementation aligns with your expectations, clarify doubts (ex. "Explain the auth process and confirm its security"), and correct course early to avoid cascading issues.

明确要求在每个重要阶段之后暂停，尤其是横跨多层（例如数据库、后端、前端）构建的复杂功能。利用这些检查点确认实现符合你的预期、澄清疑问（例如「解释认证流程并确认它的安全性」），并尽早纠正方向，避免问题层层累积。

"I want you to implement this feature that will span our database, backend, and multiple frontend interfaces. Please first plan out the database schema changes needed, and let me know when that is done so I can apply the migration." -> "Now please implement the backend changes and add tests to make sure XYZ works. Let me know when that is done" -> "Now implement the changes in both our web and mobile interfaces to call the new backend endpoint"

「我希望你实现这个功能，它会横跨我们的数据库、后端以及多个前端界面。请先规划出所需的数据库 schema 变更，完成后告诉我，我好去执行迁移。」-> 「现在请实现后端的改动，并加上测试来确保 XYZ 正常工作。完成后告诉我」-> 「现在实现我们网页端和移动端的改动，去调用新的后端端点」

### Teach it to verify its own work

### 教会它验证自己的工作

When giving feedback, go beyond simply pointing out issues ("This function isn't working"). Clearly articulate your testing process to enable the agent to independently verify future tasks. For testing patterns you'll frequently repeat, integrate these into your agent's permanent knowledge base (See Add to your agent's knowledge base).

给反馈时，不要只是指出问题（「这个函数不工作」）。要清楚说明你的测试流程，让智能体能够独立验证未来的任务。对于你会反复使用的测试模式，把它们纳入智能体的长期知识库（见「补充智能体的知识库」）。

In Devin, we actively prompt users to save essential testing procedures to the agent's ongoing memory, streamlining future interactions.

在 Devin 中，我们会主动提示用户把关键的测试流程保存到智能体的持续记忆中，从而简化后续的交互。

### Increase test coverage in AI hot spots

### 在 AI 热点区域提高测试覆盖率

Currently, agents aren't fully capable of interactively testing all scenarios thoroughly. Enhancing test coverage in areas heavily modified by AI ensures greater confidence in the agent's output. Solid tests mean that code that appears correct can be confidently merged without worry.

目前，智能体还不完全具备交互式地彻底测试所有场景的能力。在 AI 大量改动的区域增强测试覆盖，能让你对智能体的产出更有信心。可靠的测试意味着，看起来正确的代码可以被放心合并。

Our team strengthened unit tests in a critical section of our codebase before entrusting our AI to translate the implementation from Python to C.

在把「将实现从 Python 翻译到 C」这件事交给 AI 之前，我们团队先加强了代码库中一个关键部分的单元测试。

### Create Shortcuts for Your Most Repetitive Work

### 为最重复的工作创建快捷方式

Engineering teams frequently encounter repetitive, routine tasks. These are perfect candidates for automation with agents. Common examples include:

工程团队经常会遇到重复、例行的任务。这些正是最适合用智能体自动化的对象。常见的例子包括：

- feature flag removal
- dependency upgrades
- fixing and adding tests on new feature PRs

- 移除功能开关
- 依赖升级
- 在新功能 PR 上修复并补充测试

To set this up efficiently, an experienced engineer typically creates a robust, reusable prompt template [2]In Devin, these are called playbooks that can run repeatedly for these scenarios.

为了高效地把它搭起来，有经验的工程师通常会创建一个健壮、可复用的提示词模板 [2]在 Devin 中，这类模板被称为 playbook，可以针对这些场景反复运行。

One of our customers automatically triggers three agents dedicated to writing unit tests whenever new features are developed.

我们的一位客户每当有新功能开发出来，就会自动触发三个专门编写单元测试的智能体。

### Intelligent Code Review & Enforcement

### 智能化的代码评审与规则执行

While specialized tools for fast code review exist [3]Such as Greptile and CodeRabbit, autonomous agents can be an interesting option to deliver more accurate insights, particularly if they've already indexed the functionality of your repositories.

虽然已有一些专做快速代码评审的工具 [3]例如 Greptile 和 CodeRabbit，但自主智能体可以是一个有意思的选择，能给出更准确的洞察，尤其是当它们已经为你的仓库功能建立了索引时。

At Cognition, we like to maintain a list of the most common mistakes engineers make and we commit this list to the codebase. Then, instead of writing classical lint rules to catch these (which is often not possible), we have an agent run on every new PRs to check for these mistakes.

在 Cognition，我们习惯维护一份工程师最常犯错误的清单，并把这份清单提交到代码库中。之后，与其编写传统的静态检查规则来捕获这些错误（这往往做不到），我们让智能体在每个新 PR 上运行，检查是否存在这些错误。

### Hook into incidents and alerts

### 接入事故与告警

You can also set up autonomous agents to trigger automatically in response to specific events. For example, Devin provides an accessible API, and other agents can be integrated into custom workflows via CLI commands. These setups work especially well alongside MCPs to ingest third-party error logs.

你也可以让自主智能体针对特定事件自动触发。例如，Devin 提供了易于使用的 API，其他智能体则可以通过 CLI 命令集成到自定义工作流中。这类方案与 MCP 搭配使用时效果尤其好，可以用来摄入第三方的错误日志。

⚠️When it comes to triaging issues in production services, AI's debugging skills are not that great. Instead of asking the AI to fix bugs end-to-end as they come up, it is often more practical to ask the AI to just flag the most suspicious errors, changes, etc.

⚠️在生产服务的问题分诊上，AI 的调试能力并不算好。与其让 AI 在缺陷一出现时就端到端修复，通常更实际的做法是让 AI 只标出最可疑的错误、改动等。

### Environment Setup

### 环境搭建

Nothing slows down an agent faster than an incomplete or mismatched environment. To keep things running smoothly, align your agent's setup exactly with your team's. This includes language versions, package dependencies, and automated checks. For example, pre-commit should be installed in the agent's environment and environment configurations (secrets, language versions, virtual environments, browser logins) should be sourced automatically using tools like.envrc or custom configuration of.bashrc

没有什么比不完整或不匹配的环境更能拖慢智能体。为了让它顺畅运行，要把智能体的环境配置与团队完全对齐，包括语言版本、依赖包和自动化检查。例如，智能体环境中应当安装 pre-commit，而环境配置（密钥、语言版本、虚拟环境、浏览器登录态）应当借助 .envrc 这类工具或自定义的 .bashrc 配置自动加载。

We set up our agent's browser with pre-authenticated logins, removing the hassle of manual authentication and making testing much easier.

我们为智能体的浏览器配置了预先认证好的登录态，省去手动认证的麻烦，让测试轻松许多。

### Build Custom CLI Tools and MCPs

### 构建自定义 CLI 工具与 MCP

MCPs are widely available and are quick to set up and experiment with connecting your agent to external tools [4]In Devin, MCPs are still in beta as we're figuring out the best way to support them. Please contact us for access!. But many people overlook setting up simple CLI scripts for your agents. As a simple example, you could give your agent a script to pull information about a linear ticket given a ticket ID. You might also want to give your agent a tool to perform common parts of a workflow reliably, such as a script for restarting the local development environment.

MCP 已经广泛可用，把智能体接到外部工具上，配置和试验都很快 [4]在 Devin 中，MCP 仍处于 beta 阶段，我们还在摸索最好的支持方式。如需访问请联系我们！。但很多人忽略了为智能体编写简单的 CLI 脚本。举个简单的例子，你可以给智能体一个脚本，按工单 ID 拉取某个 Linear 工单的信息。你可能还想给智能体一个工具，用来可靠地完成工作流中的常见部分，比如一个重启本地开发环境的脚本。

We have a customer who has had a lot of success with creating a CLI tool that surfaces only the first failing test in a test suite. The CLI prompts the agent to focus on only that test with detailed error information, and this CLI leads the agent to have higher success and faster completion rates on long tasks.

我们有一位客户非常成功地做了一个 CLI 工具，只呈现测试套件中第一个失败的测试。这个 CLI 会提示智能体把注意力只放在那个测试上，并附上详细的错误信息，从而让智能体在长任务上成功率更高、完成更快。

### Add to your agent's knowledge base

### 补充智能体的知识库

If your agent makes some common mistakes, it's a great time to codify your feedback in the agent's knowledge base. In Devin, there is a dedicated knowledge management system. Many products offer.rules files,.md files for the agent to permanently ingest. Don't just give it guidelines on the framework you're using, but also tell it about the overall architecture of your project. Tell it what type of testing is common for different kinds of tasks, how to run important commands and which tools you recommend using.

如果你的智能体总是犯某些常见错误，那正是把反馈固化进智能体知识库的好时机。在 Devin 中有专门的知识管理系统。很多产品提供 .rules 文件、.md 文件，供智能体长期吸收。不要只给它你所使用框架的规范，还要告诉它项目的整体架构。告诉它不同类型的任务常用哪种测试、重要命令怎么运行，以及你推荐使用哪些工具。

We give our agent knowledge about the specific procedure it should follow when adding a new service route. The information includes every place it needs to add boilerplate in the frontend and backend. As a result, these tasks are now easily delegated to our AI.

我们让智能体了解在新增一条服务路由时应当遵循的具体流程。这些信息包含它在前端和后端需要添加样板代码的每一处位置。因此，这类任务现在可以轻松委派给我们的 AI。

### Limited debugging skills

### 调试能力有限

Bugs reports can be deceptively simple. But many bugs often require not only access to databases and logs, but also a level of debugging that is greater than most AI agents today. If using AI to aid in debugging, we recommend asking for a list of probable root causes rather than trying to debug and fix everything itself. Then, a human can decide based on their own experience which one is the real root cause. But once the cause is known, agents can still be quite helpful at implementing the fix.

缺陷报告看起来可能很简单。但很多缺陷不仅需要访问数据库和日志，还需要比当今大多数 AI 智能体更强的调试能力。如果用 AI 辅助调试，我们建议让它给出可能根因的清单，而不是让它自己去调试并修复一切。之后，人可以依据自身经验判断哪一个才是真正的根因。而一旦原因明确，智能体在实现修复上仍然相当有用。

### Poor fine-grained visual reasoning

### 细粒度视觉推理较弱

Generally models today don't have great visual reasoning capabilities at the level of details needed to match screenshots of designs or Figma mockups. They are most reliable on visuals that can be described at the level of code (ex. giving it code from Figma). If you want it to match your visual style, you should use a good design system with reusable components.

总体而言，当今的模型还不具备足够强的视觉推理能力，达不到匹配设计稿截图或 Figma 原型所需的细节水平。它们在可以用代码层面描述的视觉内容上最可靠（例如直接把 Figma 导出的代码给它）。如果你希望它符合你的视觉风格，就应当使用一套带有可复用组件的好设计系统。

### Knowledge Cutoffs

### 知识截止

Whenever you want to work with a new library, you should explicitly point it to the latest docs. Otherwise, most agents will assume the old patterns from these libraries due to knowledge cutoffs in the pretrained base models. A good agent can overcome this if you point it to docs, but you must be mindful of this (remember, the agent doesn't even know that there are new versions of these libraries).

每当你要使用一个新库时，都应当明确把最新文档指给它。否则，由于预训练基础模型存在知识截止，大多数智能体会沿用这些库的旧有模式。只要你把文档指给它，好的智能体就能克服这一点，但你必须意识到这个问题（记住，智能体甚至不知道这些库已经出了新版本）。

### Be willing to cut your losses earlier

### 愿意更早止损

A common mistake for people who are new to using agents is that they commit to making an interaction successful, even when an agent's work is veering off track. If you ever find yourself thinking "it's ignoring my instructions" or "this thing is going in circles", you should be ok discontinuing that conversation or manually taking over. Sending more messages is more likely a sign of the inherent complexity of your task being higher than the agent's capabilities rather than some simple mistake that can be corrected.

刚接触智能体的人常犯的一个错误是：即使智能体的工作已经偏离轨道，也执意要把这次交互做成功。如果你发现自己心里冒出「它在无视我的指令」或者「这东西在原地打转」，那就应该坦然结束这次对话，或者手动接手。继续发更多消息，更可能说明你的任务本身复杂度超出了智能体的能力，而不是某个简单错误可以被纠正。

### Diversifying your experiments

### 让尝试多样化

If you're new to working with agents, we recommend diversifying your bets at the start. Try a range of different prompts and ideas. Double down on the types of tasks you see the agents naturally performing well on - and cut your losses on the ones they don't. Don't feel a need to force your agents to find success every time.

如果你刚开始使用智能体，我们建议一开始就把尝试分散开。多试一些不同的提示词和想法。在智能体天然表现好的任务类型上加大投入，在它们不擅长的类型上及时止损。不必强求智能体每次都成功。

Starting over is the right answer a lot more often with agents than with humans. If you've given an agent a task and it is struggling to address feedback or correct course, starting fresh with a new agent and all of the instructions up front can often get to success much faster. The ability of an agent to correct a messed-up environment is much worse than its ability to spit out fresh code from scratch.

与和人协作相比，和智能体协作时「重来一次」是正确答案的频率要高得多。如果你给智能体派了任务，而它迟迟难以响应反馈或纠正方向，那么换一个全新的智能体、并一次性把所有指令给全，往往能更快成功。智能体修复一团糟的环境的能力，远不如它从零写出新代码的能力。

### Create accounts for your agent

### 为智能体创建账号

A throwaway email is helpful for safe testing of sites. Create custom IAM roles for your agent if it needs to access cloud resources.

一次性邮箱有助于安全地测试各类站点。如果智能体需要访问云资源，就为它创建自定义的 IAM 角色。

### Give it a development / staging environment

### 给它一个开发 / 预发环境

Ideally the agent uses the same testing setup as the engineers on your team. We suggest avoiding giving access to production services entirely. When using remote agents, you can run fully isolated test environments on the agent's remote machine.

理想情况下，智能体使用与团队工程师相同的测试配置。我们建议完全不要给它生产服务的访问权限。使用远程智能体时，你可以在智能体的远程机器上运行完全隔离的测试环境。

### Readonly API keys

### 只读 API 密钥

Where possible, give it readonly access. We find it is still helpful for humans to manually run any script that interacts with outside services.

尽可能给它只读权限。我们发现，凡是与外部服务交互的脚本，由人来手动运行仍然更有帮助。
