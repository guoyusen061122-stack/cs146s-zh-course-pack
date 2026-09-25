# How OpenAI Uses Codex

# OpenAI 如何使用 Codex

## Slide 1

## Slide 1

How OpenAI uses Codex

OpenAI 如何使用 Codex

## Slide 2

## Slide 2

Contents Introduction 3 Use Cases Code understanding 4 efactoring and migrations erformance otimiation 6 Imroving test coverage 7 Increasing develoment velocity 8 Staying in flow 9 Exloration and ideation 10 Best ractices 11 Looking Ahead 12 2 How OenAI uses Codex

目录 引言 3 用例 代码理解 4 重构与迁移 性能优化 6 提升测试覆盖率 7 提高开发速度 8 保持专注状态 9 探索与构思 10 最佳实践 11 展望未来 12 2 OpenAI 如何使用 Codex

## Slide 3

## Slide 3

Introduction Codex is used daily across numerous technical teams at OpenAI like Security, Product Engineering, Frontend, API, Infrastructure, and Performance Engineering. Teams are using it to accelerate a range of engineering tasks, from understanding complex systems and refactoring large codebases to shipping new features and resolving incidents under tight deadlines. Drawing from interviews with OpenAI engineers and internal usage data, we’ve compiled use cases and best practices that highlight how Codex helps our teams move faster, improve work quality, and manage complexity at scale. How OpenAI uses Codex

引言 Codex 每天都被 OpenAI 众多技术团队使用，例如安全、产品工程、前端、API、基础设施和性能工程。各团队用它加速各类工程任务：从理解复杂系统、重构大型代码库，到交付新功能，以及在紧张的截止期限下处理事故。基于对 OpenAI 工程师的访谈和内部使用数据，我们整理出这些用例与最佳实践，展示 Codex 如何帮助团队加快进度、提升工作质量，并应对大规模复杂性。OpenAI 如何使用 Codex

## Slide 4

## Slide 4

Use case 1 Code understanding Codex heps our teams get up to speed quicky in unfamiiar parts of the codebase when onboarding, debugging, or investigating an incident. They often use Codex to ocate the core ogic of a feature, map out reationships between services or modues, and trace data flow through a system. It aso heps surface architecture patterns or missing pieces of documentation that woud otherwise require significant manua effort to generate. During incident response, Codex heps engineers ramp into new areas quicky by surfacing interactions between components or tracing how faiure states propagate across systems. Anecdotes om ou tems When I fix Ask mode to see where else in the codeb s Peomnce Enginee, Retievl Systems When I’m on‑c the st Codex where the flow lives. It jumps str so I c Site Relibility Enginee, API Pltom Codex ‘Where would I do this?’ repo questions Terr w DevOps Enginee, Instuctue Sevices Ty using Codex o code undestnding with these smple pompts: W here is the authentication ogic impemented in this repo ? S ummari z e how requests flow through this service from entrypoint to response. W hich modues interact with insert modue name and how are faiures handed ? 4 H ow O pen A I uses Codex

用例 1 代码理解 Codex 帮助我们的团队在代码库中不熟悉的部分快速上手，无论是入职、调试还是调查事故。他们常用 Codex 定位某个功能的核心逻辑，梳理服务或模块之间的关系，并追踪数据在系统中的流动。它还有助于发现架构模式，或者补上那些原本需要大量人工才能生成的文档缺失。在事故响应期间，Codex 通过呈现组件之间的交互、或追踪故障状态如何在系统间传播，帮助工程师快速进入新领域。来自我们团队的轶事 修完问题后，我会用 Ask 模式看看代码库里还有哪些地方会出现同样的写法，性能工程师，检索系统 值班时我最想知道流程在哪里，Codex 会直接跳过去，让我能继续往下看，站点可靠性工程师，API 平台 Codex「如果要加这个功能，我该在哪里改？」代码库问题 实际使用中的真实提问，DevOps 工程师，基础设施服务 试试用 Codex 完成代码理解，可以使用这些示例提示词：这个仓库里的认证逻辑实现在哪里 ？ 概述一下请求如何从入口一路流转到响应，经过这个服务。哪些模块会与 insert module name 交互，失败又是如何处理的 ？ 4 OpenAI 如何使用 Codex

## Slide 5

## Slide 5

Use case 2 Refactoring and migrations Code is commonly used to make changes that san multile files or ackages. For eamle, when engineers are udating an AP, changing how a attern is imlemented, or migrating to a new deendency, Code makes it easy to aly changes consistently. t’s esecially useful when the same udate needs to be made across dozens of files, or when the udate reuires awareness of structure and deendencies that aren’t easily caught with a rege or find-and-relace. They’re also using it for code cleanu by breaking u oversized modules, relacing old atterns with modern ones, or rearing code for better testability. Anecdotes from our teams Cod for our n and op would’v getUserById( ) Backend Engineer, ChatGPT Web To cl scan for summariz op Product Engineer, ChatGPT Enterprise Try using Codex for refactoring and migrations with these sample prompts: Slit this file into searate modules by concern and generate tests for each one. Convert all callback-based database access to async / await. 5 H ow O enA uses Code

用例 2 重构与迁移 Codex 常用于跨多个文件或包的改动。例如，工程师更新 API、改变某个模式的实现方式，或迁移到新依赖时，Codex 能让改动保持一致、易于落地。当同一处更新需要覆盖几十个文件，或者更新要求理解那些正则表达式和查找替换难以捕捉的结构与依赖关系时，它尤其有用。团队也用它做代码清理：把过大的模块拆开、用现代模式替换旧模式，或为更好的可测试性整理代码。来自我们团队的轶事 Codex 帮我们找出用 getUserById( ) 查询的地方，本来会漏掉的边界情况 后端工程师，ChatGPT Web 用 Codex 做一次扫描，就能总结出可优化的点 产品工程师，ChatGPT Enterprise 试试用 Codex 完成重构与迁移，可以使用这些示例提示词：把这个文件按关注点拆成若干独立模块，并为每个模块生成测试。把所有基于回调的数据库访问改成 async / await。5 OpenAI 如何使用 Codex

## Slide 6

## Slide 6

Use case 3 Performance optimization Coe is use to ientify an aress performance ottlenecks. uring tuning or reliaility efforts, engineers prompt Coe to analyze slow or memory-intensive coe paths, such as inefficient loops, reunant operations, or costly ueries an suggest optimize alternatives, often resulting in meaningful gains in efficiency an reliaility. Coe is also use to support coe health y ientifying risky or eprecate patterns that are still in active use. Our teams lean on it to help reuce long-term tech et an proactively prevent regressions. Anecdotes from our tems I use Code e hot paths and drafting batched queries I can later tune. Infrstructure Engineer, API Relibility Code issues quickly— I save 30 minutes of work by spending 5 minutes on a prompt. Pltform Engineer, Model Serving Try using Codex for performnce optimiztion with these smple prompts: Optimize this loop for memory efficiency an eplain why your version is faster. Fin repeate epensive operations in this reuest hanler an suggest caching opportunities. Suggest a faster way to atch B ueries in this function. 6 How OpenAI uses Coe

用例 3 性能优化 Codex 用于识别并定位性能瓶颈。在调优或可靠性工作中，工程师会提示 Codex 分析缓慢或内存占用高的代码路径，例如低效的循环、重复的运算或代价高昂的查询，并提出优化方案，往往能带来效率与可靠性上的实质提升。Codex 也用于维护代码健康度，找出那些仍在被使用、但风险较高或已废弃的模式。我们的团队借助它减少长期技术债，并主动预防回归。来自我们团队的轶事 我用 Codex 分析热点路径，并起草后续可继续调优的批量查询。基础设施工程师，API 可靠性 Codex 能很快发现问题——我在提示词上花 5 分钟，就省下 30 分钟的工作。平台工程师，模型服务 试试用 Codex 完成性能优化，可以使用这些示例提示词：针对内存效率优化这个循环，并解释你的版本为什么更快。在这个请求处理程序中找出重复且代价高昂的操作，并指出可以加缓存的地方。给出一种更快的方式，用来批量查询这个函数中的数据库。6 OpenAI 如何使用 Codex

## Slide 7

## Slide 7

Use case 4 Improving test coverage Codex elps engineers write tests faster — especially in places were coverage is tin or completely missing. en woring on a ug x or refactor, engineers often as Codex to suggest tests tat cover edge cases or liely failure pats. For new code, it can generate unit or integration tests ased on te function signature and surrounding logic. Codex is particularly elpful for identifying oundary conditions lie empty inputs, max lengt, or unusual ut valid states tat are often missed in initial tests. Anecdotesomoutems I point Codex at low‑coverage modules overnight and wake up to runnable unit‑test PRs FontendEnginee, ChtGPTDesktop When switching mono-repo branches is painful, I have Codex write the tests and kick-off CI while I keep working on my branch. BckendEnginee, Pyments&Billing TyusingCodexoimpovingtest covegewiththesesmplepompts: rite unit tests for tis function, including edge cases and failure pats. Generate a property-ased test for tis sorting utility. Extend tis test le to cover missing scenarios around null inputs and invalid states. 7 How OpenAI uses Codex

用例 4 提升测试覆盖率 Codex 帮助工程师更快地编写测试——在覆盖率偏低或完全缺失的地方尤其有用。在修 bug 或重构时，工程师常让 Codex 提出能覆盖边界情况或可能失败路径的测试。对于新代码，它可以根据函数签名和周边逻辑生成单元测试或集成测试。Codex 在识别边界条件时特别有帮助，例如空输入、最大长度，或者那些不常见但合法的状态——它们在第一轮测试里往往被漏掉。来自我们团队的轶事 我把 Codex 指向覆盖率低的模块，让它跑一整晚，第二天醒来就能拿到可直接运行的单元测试 PR 前端工程师，ChatGPT Desktop 切换 monorepo 分支很痛苦时，我会让 Codex 写好测试并启动 CI，自己继续在当前分支上工作。后端工程师，支付与账单 试试用 Codex 提升测试覆盖率，可以使用这些示例提示词：为这个函数编写单元测试，包含边界情况和失败路径。为这个排序工具生成一个基于属性的测试。扩展这个测试文件，覆盖空输入和非法状态等缺失场景。7 OpenAI 如何使用 Codex

## Slide 8

## Slide 8

Use case 5 Increasing development velocity ode helps teams move faster by accelerating both the start and end of the development cycle. When kicking off a new featre, engineers se it to scaffold boilerplate — generating folders, modles, and API stbs to get rnnable code p qickly withot hand-wiring every piece. As projects approach release, ode helps meet tight deadlines by handling smaller bt essential tasks like triaging bgs, filling in last-mile implementation gaps, and generating rollot scripts, telemetry hooks, or config files. It’s also sed to trn prodct feedback into starter code. Engineers often paste in a ser reqest or spec and have ode generate a rogh draft they can retrn to and refine later. Anecdotes from our teams I was in meetings all day and still merged background. Product Engineer, ChatGPT Enterprise Codex helped ship 3- perfectly that would’ve languished in the backlog, which was super empowering. Full‑Stack Engineer, Internal Tools Try using Codex for increasing development velocity with these sample prompts: Scaffold a new API rote for POST /events with basic validation and logging. G enerate a telemetry hook for tracking sccess/failre of the new onboarding fl ow, sing this template [ insert eample of yor telemetry code ] . reate a stb implementation based on this spec : [ insert spec or prodct feedback ] . H ow OpenAI ses ode

用例 5 提高开发速度 Codex 通过加速开发周期的起点和终点，帮助团队更快推进。启动新功能时，工程师用它搭建样板代码——生成目录、模块和 API 桩，快速得到可运行的代码，而不必手工拼装每一处。当项目接近发布时，Codex 通过处理那些虽小但关键的任务来赶上紧张的截止日期，例如分诊 bug、补齐最后一公里的实现缺口，以及生成回滚脚本、遥测埋点或配置文件。它也被用来把产品反馈变成起步代码。工程师常直接粘贴用户请求或规格，让 Codex 生成一份粗略草稿，之后再回来细化。来自我们团队的轶事 我整天都在开会，仍然把后台任务合并进去了。产品工程师，ChatGPT Enterprise Codex 帮助交付了 3 个本来会一直积压在待办列表里的功能，这让人特别有掌控感。全栈工程师，内部工具 试试用 Codex 提高开发速度，可以使用这些示例提示词：为 POST /events 搭建一个新的 API 路由，包含基本的校验和日志。用这个模板生成一个遥测埋点，用来跟踪新引导流程的成功/失败：[ 插入你的遥测代码示例 ] 。根据这份规格创建一个桩实现：[ 插入规格或产品反馈 ] 。OpenAI 如何使用 Codex

## Slide 9

## Slide 9

Use case 6 Staying in flow Coex elps our engineers stay prouctive wen teir sceules are fragmente an lle wit interruptions. It’s use to capture unnise wor, turn notes into woring prototypes, or spin off exploratory tass tat can be revisite later. Tis maes it easier to pause an resume wor witout losing context, especially wen tey’re on call or ave a lot of meetings. Anecdoeomouem instead of swapping branches and review its PR when BckendEnginee, ChGPTAPI traces, issues and more to Codex so stay focused on high priority work. APIEnginee, InucueObevbiliy TyuingCodexoyinginlow wihheemplepomp: Generate a plan to refactor tis service an split it into smaller moules. Stub out te retry logic an a a TODO — I’ll ll in te bacoff logic later. Summari z e tis le so I can pic up were I left off tomorrow. 9 H ow Open A I uses Coex

用例 6 保持专注状态 Codex 帮助我们的工程师在日程被切碎、满是打断的情况下保持产出。它被用来记录零散的活儿、把笔记变成可运行的原型，或者把探索性的任务单独分出去，之后再回来看。这样一来，暂停和恢复工作变得更容易，不必担心丢失上下文，尤其是在值班或会议很多的时候。来自我们团队的轶事 与其反复切换分支，不如先让 Codex 跑起来，等它出 PR 时再评审。后端工程师，ChatGPT API 我把 trace、issue 等信息交给 Codex，这样就能专注在高优先级的工作上。API 工程师，基础设施可观测性 试试用 Codex 保持专注状态，可以使用这些示例提示词：制定一个计划，重构这个服务并把它拆成更小的模块。把重试逻辑搭个桩，并留下一个 TODO —— 退避逻辑我稍后补上。总结一下这个文件，方便我明天接着往下做。9 OpenAI 如何使用 Codex

## Slide 10

## Slide 10

Use case 7 Exploration and ideation Codex is also useful for open-ended ork like finding alternative solutions or validating design decisions. You can propt for different ays of solving a proble, explore unfailiar patterns, or pressure-test assuptions. This helps surface tradeoffs, expand design options, and sharpen ipleentation choices. It’s also used to identify related bugs. Given a knon issue or deprecated ethod, Codex can identify siilar patterns elsehere in the code, aking it easier to catch regressions or finish cleanup ork. Anecdotes fom ou tems Cod probl scaffolds cod Poduct Enginee, ChtGPT Desktop Aft bugs might lurk, th Pefomnce Enginee, Retievl Systems Ty using Codex fo explotion nd idetion with these smple pompts Ho ould this ork if the syste ere event-driven instead of request/response? Find all odules that anually build SQL strings instead of using our query builder. R erite this in a ore functional style, avoid utation and side effects. 10 Ho O pen A I uses Codex

用例 7 探索与构思 Codex 也适合开放式的工作，比如寻找替代方案或验证设计决策。你可以让它给出解决问题的不同思路、探索不熟悉的模式，或者对假设做压力测试。这有助于呈现取舍、拓展设计选项，并让实现选择更清晰。它也被用来发现相关的 bug。给定一个已知问题或已废弃的方法，Codex 能找出代码库其他位置上的相似模式，从而更容易抓住回归，或完成清理工作。来自我们团队的轶事 Codex 为问题搭好脚手架，也补上代码。产品工程师，ChatGPT Desktop 查完 bug 可能藏在哪些地方之后，我再动手改。性能工程师，检索系统 试试用 Codex 完成探索与构思，可以使用这些示例提示词 如果这个系统改成事件驱动而不是请求/响应，会怎样运作？找出所有手工拼接 SQL 字符串、而没有使用我们的查询构造器的模块。用更函数式的风格重写这段代码，避免可变状态和副作用。10 OpenAI 如何使用 Codex

## Slide 11

## Slide 11

Best practices Codex works best when it’s given structure, context, and room to iterate. Here are some of the habits OpenAI teams are cultivating to get consistent value out of it in day-to-day work. wsMoe For large changes, start by prompting Codex for an implementation plan using Ask mode, which then becomes the input for follow-up prompts when you switch to Code Mode. This two-step flow keeps Codex grounded and helps avoid errors in its output. Codex works best with well-scoped tasks that would take you or a teammate about an hour to complete or a few hundred lines of code to implement. As models improve, expect the size of the tasks it can take on to increase. IevelympoveCoex’s evelopme Setting a startup script, environment variables, and internet access significantly reduces Codex’s error rate. As you run tasks, look for build errors that can be corrected in Codex’s environment configuration. This may take a few iterations, but gives significant efficiency gains in the long run. ucueyoupompsf youew Codex responds better when prompts mirror how you’d describe a change in a PR or issue. That means including file paths, component names, diffs, and doc snippets when relevant. Prompting with patterns like “Implement this the same way it’s done in [module X]” improves results. UseeCoexsqueue slgwegbclog Fire off tasks to capture tangential ideas, partial work, or incidental fixes. There’s no pressure to generate a full PR in one go. Codex works well as a staging area you can return to when you’re back in focus. 11 How OpenAI uses Codex

最佳实践 Codex 在获得结构、上下文和迭代空间时表现最好。以下是 OpenAI 各团队正在养成的一些习惯，用来在日常工作中稳定获得价值。更多内容 对于大型改动，先用 Ask 模式让 Codex 给出一份实现计划。它随后会成为你切到 Code 模式后继续提问的输入。这种两步流程能让 Codex 保持落地，也有助于避免输出中的错误。Codex 最适合范围明确的任务——大概需要你或同事花一小时完成，或者用几百行代码实现。随着模型变强，它能承担的任务规模也会增大。改进 Codex 的开发环境 设置好启动脚本、环境变量和网络访问，能显著降低 Codex 的错误率。运行任务时，留意那些可以通过调整 Codex 环境配置来修正的构建错误。这可能需要几次迭代，但长期看能带来明显的效率提升。按你写 PR 的方式来写提示词 Codex 对提示词的回应更好，如果提示词模仿你在 PR 或 issue 中描述改动的方式。这意味着在相关时应包含文件路径、组件名、差异（diff）和文档片段。使用「按 [module X] 里的做法同样实现」这类模式来提示，效果会更好。使用 Codex 的队列来排空待办积压 把零散的想法、部分完成的工作或顺手要修的小问题都发成任务，不必强求一次就生成完整的 PR。Codex 很适合当作一个暂存区，等你重新集中注意力时再回到那里。11 OpenAI 如何使用 Codex

## Slide 12

## Slide 12

Best practices Use AGENTS.md to supply persistent context Maintain an AGENTS.d fie t hep dex perate re effectivey in yr rep acrss prpts. These fies typicay incde naing cnventins, bsiness gic, knwn qirks, r dependencies dex can’t infer fr the cde ane. earn re n strctring yr AGENTS.d fie in the dcs. Leverage “Best of N” to improve output The Best-f-N featre ets y sitanesy generate tipe respnses fr a singe task t qicky expre tipe stins and pick the best ne. Fr re cpicated tasks, y can review severa iteratins and cbine parts f different respnses t get a strnger rest. king ahead dex is sti in research preview, bt it’s aready aking a rea ipact in hw we bid, heping s ve faster, write better cde, and take n wrk that wd’ve therwise never been priritized. We’re excited by the ptentia ahead — as r des get better and dex beces re deepy integrated int r wrkflws, we’re king frward t ncking even re pwerf ways t devep sftware with it. We’ cntine t share what we earn ang the way. 12 Hw OpenAI ses dex

最佳实践 用 AGENTS.md 提供持久上下文 维护一份 AGENTS.md 文件，帮助 Codex 在你的仓库中跨提示词更有效地工作。这类文件通常包含命名约定、业务逻辑、已知的怪异之处，或者 Codex 无法从代码中自行获知的依赖关系。在你的文档里可以进一步学习如何组织 AGENTS.md 文件。用「Best of N」改进输出 Best-of-N 功能让你可以同时为同一个任务生成多份回复，快速比较不同方案并挑出最好的那一份。对于更复杂的任务，你可以查看多次迭代，并把不同回复的部分内容组合起来，得到更强的结果。展望未来 Codex 仍处于研究预览阶段，但它已经产生了真实的影响，改变着我们的工作方式：帮助我们更快交付、写出更好的代码，并承接那些原本永远不会被排上优先级的工作。我们对前方的潜力感到兴奋——随着模型变得更好，Codex 更深地融入我们的工作流，我们期待用它解锁更多强大的软件开发方式。我们也会持续分享一路上的收获。12 OpenAI 如何使用 Codex
