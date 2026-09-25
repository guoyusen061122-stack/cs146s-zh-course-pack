# 如何高效做代码评审

[Sarah Vessels](https://github.blog/author/cheshire137/)·[@cheshire137](https://github.com/cheshire137)

2024 年 7 月 23 日

- 分享：
- <https://x.com/share?text=How%20to%20review%20code%20effectively%3A%20A%20GitHub%20staff%20engineer%E2%80%99s%20philosophy&url=https%3A%2F%2Fgithub.blog%2Fdeveloper-skills%2Fgithub%2Fhow-to-review-code-effectively-a-github-staff-engineers-philosophy%2F>
- <https://www.facebook.com/sharer/sharer.php?t=How%20to%20review%20code%20effectively%3A%20A%20GitHub%20staff%20engineer%E2%80%99s%20philosophy&u=https%3A%2F%2Fgithub.blog%2Fdeveloper-skills%2Fgithub%2Fhow-to-review-code-effectively-a-github-staff-engineers-philosophy%2F>
- <https://www.linkedin.com/shareArticle?title=How%20to%20review%20code%20effectively%3A%20A%20GitHub%20staff%20engineer%E2%80%99s%20philosophy&url=https%3A%2F%2Fgithub.blog%2Fdeveloper-skills%2Fgithub%2Fhow-to-review-code-effectively-a-github-staff-engineers-philosophy%2F>

作为 GitHub 的一名资深工程师（staff engineer），[代码评审](https://github.com/features/code-review)是我日常工作中的主要职责之一。过去八年里，我评审了 7000 多个拉取请求。为什么这么多？因为代码评审对构建好软件至关重要，而多一双眼睛往往能发现你本来会漏掉的问题。

我把代码评审视为工作中最重要的环节之一。事实上，只要看到队友有拉取请求可以评审了，我就宁愿放下自己正在做的分支，转去评审他们提出的改动。毕竟，他们的拉取请求已经通过了持续集成（CI）的重重考验，也达到了作者自己判断的「完成」标准，所以它大概比我自己那半成品更接近可发布状态。我更愿意把他们的代码推过终点线，而不愿再耗上无法预估的时间去写完自己的代码。

我越早给出反馈——「这里可能是 nil，会导致报错」「这看起来像是一次 n+1 查询」「这里最好能有一个方法签名」——这些反馈就能越早被处理，缺陷被消灭，功能被发布。

我想分享一下我如何做代码评审，希望我们都能交付更好的代码。

## 什么是代码评审？

严格来说，代码评审——通过 GitHub 上的[拉取请求评审](https://docs.github.com/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)进行——让协作者可以就拉取请求中提出的改动发表评论、表示批准，或在拉取请求合并前要求进一步修改。

我把拉取请求看作一场对话的开端。我把它读作作者在说「我认为这改进了我们现在的做法」。代码评审是塑造产品实现方式的绝佳机会。作为评审者，我的工作就是与作者来回讨论，通过提问、质疑假设、总体充当第二双眼睛来改进他们的代码。

## 优化你的代码评审流程

### 如何找到需要评审的拉取请求

我常驻在我的 [GitHub 通知收件箱](https://github.com/notifications?query=is:unread)里。它是我在浏览器里固定为标签页的少数几个页面之一，所以随时都能打开。每当我在等 CI、处于任务间隙、刚开始一天的工作，或者只是有点空闲，我都喜欢去看一眼收件箱。我评审的大多数拉取请求都是在那里找到的。GitHub 的各团队往往有一个固定的 Slack 频道当作大本营，那里是分享待评审拉取请求的好地方——这也是我发现拉取请求的主要途径之一。

我还发现用 [GitHub Slack 集成](https://slack.github.com/)把某个 Slack 频道订阅到与团队相关的新拉取请求上很有效。为了筛选哪些拉取请求会出现在 Slack 里，我会用一个团队专属的标签，然后在 Slack 里用 `/github subscribe your/repo pulls +label:"your-team-label"` 这样的「subscribe」命令。

我喜欢用 `is:open archived:false is:pr org:github -is:draft team-review-requested:github/relevant-codeowner-team` 这类查询来搜索可能需要评审的未处理拉取请求。用这个查询，我能找到 GitHub 组织内的[处于打开状态](https://docs.github.com/search-github/searching-on-github/searching-issues-and-pull-requests#search-by-open-or-closed-state)、[未归档的](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests#search-based-on-whether-a-repository-is-archived)[拉取请求](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests#search-only-issues-or-pull-requests)，它们[位于该用户或组织的仓库中](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests#search-within-a-users-or-organizations-repositories)、不是[草稿](https://docs.github.com/search-github/searching-on-github/searching-issues-and-pull-requests#search-for-draft-pull-requests)，并且[把相关代码所有者团队列为被请求的评审者](https://docs.github.com/search-github/searching-on-github/searching-issues-and-pull-requests#search-by-pull-request-review-status-and-reviewer)。我通常会省掉 [`review:required`](https://docs.github.com/search-github/searching-on-github/searching-issues-and-pull-requests#search-by-pull-request-review-status-and-reviewer) 这个搜索限定符，因为即使队友已经评审过某个拉取请求，我也有兴趣自己再看一遍。毕竟，评审代码不仅帮助作者，也让我跟上那些影响我所负责代码的变更。

### 用评审者团队管理通知

你不会希望代码变更去打扰一个庞大的团队，以至于团队里每个人都觉得评审这个改动不是自己的[责任](https://en.wikipedia.org/wiki/Diffusion_of_responsibility)。这可能造成两种结果：拉取请求无人问津地搁置，或者在不该合并的时候就先被合并了，因为关键评审者在一大堆通知里漏掉了它。这两种情况都会影响产品质量。

如果可以，我建议精简你所加入的[代码所有者](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)团队数量，让自己的通知量可控。这样一来，落进你收件箱的拉取请求就不只是噪音，而是你确实觉得该评审的东西。庞大且包罗万象的代码所有者团队作为兜底选项还可以，但作为自动评审请求的第一道默认设置就不太合适。把仓库的 CODEOWNERS 文件整理好，并配上界定清晰的代码边界，以限制通知量，帮助评审者避免通知疲劳。

另一种限制团队级通知的办法，是创建一个第一响应者团队，然后用自动化按排班添加和移除团队成员。这样你的团队可以专注日常的代码库，而排班的第一响应者会收到团队服务区域内拉取请求的通知。例如，用 [PagerDuty API](https://developer.pagerduty.com/api-reference/3f03afb2c84a4-get-a-schedule) 可以确定某一天谁是第一响应者。然后你就可以用 [Octokit 库](https://docs.github.com/rest/using-the-rest-api/libraries-for-the-rest-api?apiVersion=2022-11-28#official-github-libraries)来添加和移除团队成员。

### 用自动化在各团队间统一代码评审

仓库级配置与自动化，例如使用 [CODEOWNERS 文件](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners#codeowners-file-location)与[分支保护规则](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)，有助于在各团队间强制统一评审流程标准。其他标准，比如拉取请求里什么值得评论，就得靠我们人来维持。把团队内代码评审如何运作写下来，确保无论是做评审还是提交拉取请求的人，都知道如何让自己的拉取请求得到评审、评审的预期周转时间，以及有哪些自动化在辅助评审。

有些团队用项目看板来跟踪有哪些拉取请求进来待评审；我见过这在管理共享 API 的团队里效果不错，因为这类区域经常被团队之外的人修改。另一些团队只依赖 GitHub 通知，我见过这在代码归属范围界定得很窄、且团队能纪律性地一有拉取请求就评审时效果很好。

如果你遵循的是自己团队特有的流程，自动化可以帮助你向团队之外的人传达预期。例如，如果许多其他团队依赖你们团队的评审，你可以用机器人自动在任何请求你们团队评审的拉取请求上留言，告诉作者大概什么时候能收到回复。

## 什么样的代码评审算好，什么样算差？

好的代码评审能带来清晰度，并把代码推向比原先更好的状态。

作为评审者，沟通清晰是关键。你需要说清哪些评论是你的个人偏好，哪些是批准前的阻塞项。给出你所建议做法的示例，可以提升评审的价值，也让你的意思更清楚。如果你能从与该拉取请求同一个仓库里举例，那就更好——这通过鼓励实现方式的一致性，进一步支撑了你的建议。

相比之下，糟糕的代码评审缺乏清晰度。例如，不带任何评论的一揽子批准或拒绝，会让拉取请求作者怀疑这次评审是否认真。哪怕只是在批准时复述一遍你对作者意图的理解，也能暴露出你和作者的理解是否一致。

如果一次代码评审没有说清其中的建议应该何时落实，对作者来说同样是糟糕的体验。指出既有且未被改动的代码应该重构，或者某个额外情况应该处理，这都没问题，但关键是说明这些是否是批准的前提。如果这些建议不做、拉取请求也可以合入，那一定要说出来。保留一个小的差异（diff）并把那些改动作为单独的拉取请求分别发布，可能更稳妥。

**下面这条代码评审评论体现了具体性，并清楚地传达了建议的实现方式：**

*「我看到你的新方法与这个文件里既有风格一致，接收 [X] 个参数。这么多参数会损害可读性，也意味着这个函数承担了太多职责。你觉得在后续的拉取请求里，把这个方法和既有方法一起重构、减少参数数量怎么样？」*

**这条评论好在哪里：**

- 给出了具体细节。
- 引用了具体的代码或问题。
- 提出了问题的解决方向。
- 给出了依据或作了解释

**在另一个极端，以下是一些本可以更好的评审评论示例：**

*「我不喜欢这个。」*——评审者到底不喜欢什么？他心里有没有可以明确说出来的替代方案？

**可能的改进：**

- 「这一行做的事太多了，能不能简化一下以提升可读性？」
- 「我觉得这会因为一次 n+1 查询而出现性能问题。」
- 「这里能不能改用 [preferred framework] 的方案，而不是自己写一套实现？」

*「这样行不通。」*——为什么这些改动行不通？

- 「这样行不通，因为 [X]，见这个相关问题：[issue link]。」
- 「这个之前在 [pull request link] 里试过，因为 [X] 没成功。」
- 「如果你在 [X] 上遇到问题，可以改用 [alternative approach] 试试。」

*「我觉得这修掉了一个缺陷。」*——我很喜欢这种点名，但有没有更多上下文，比如一个 issue 链接，能让它更清楚？

- 「我觉得这修掉了 [issue link]。」
- 「这是在修 [issue link] 里的那个缺陷吗？」
- 「这看起来就是我们遇到过的 [link to failing build] 里的那个缺陷。谢谢修复！」

## 如何给出好的代码评审

### 提问

我把拉取请求作者看作最了解该改动上下文的人。我可以根据自己的经历——在 Ruby on Rails 单体应用、TypeScript，或者在高流量数据库上的工作经验——指出我看到的问题，但我信任作者对我问题的回答。我认为他们对具体细节的理解比我更可靠。

我也很喜欢就代码中做出的假设提问。他们处理的数据是什么结构？是否存在不符合该结构的数据？代码能妥善应对吗？代码是否资源消耗很大？性能会好吗？作为评审者，我最喜欢的回应是作者提供一个自动化测试，来验证那些场景下的行为。第二喜欢的是实证数据，例如来自我们数据仓库的查询结果，或一张 Datadog 图表，说明为什么那些场景不成问题。

作为拉取请求作者，我也很感激收到提问。有人提问，就等于给我空间去解释我为什么对这次改动有信心，必要时引用 issue、查询或图表。这也让我能把自己的知识与经验分享给他人。作者不仅能看到我的回应，其他评审者和未来的读者也能看到——他们可能正在追溯某个过往决策的来龙去脉。

### 给出肯定

除了提问，对拉取请求中你认同的部分加以评论也是好习惯。这类评论能表明你读过并理解了正在被改动的内容，或者你验证了代码中的某个假设。以下是几个例子：

- 「看起来这与本模块其他类所用的模式一致。」
- 「谢谢你为这个加了测试！」
- 「这比之前可读性好多了。」

就我的经验而言，收到这类评论本身也让人舒服。收到代码评审有时会让人感到消耗。当我要应付来自好几方的提问和建议时，收到几条并不向我索取什么、而是支持并肯定我已完成工作的评论，是很好的鼓舞。

### 警惕偏见与假设

你很容易让对评审者本人、或对其所改动代码领域的偏见影响评审。你会习惯某人长期负责某个领域，或者拥有某种资历，于是假设他知道自己在做什么——但*每个人*都会犯错。你对他们改动的注视，你检验他们假设或验证自己想法的提问，可以在问题部署之前就抓住它。

我非常推崇写测试，因为测试能消除一部分偏见。当你写一个测试来检查代码是否正常工作，[你就不必只听作者的一面之词](https://www.youtube.com/watch?v=NIKAsGC1Iy8)，只需看测试是否通过——当然，前提是你的测试本身写对了。😅

我也非常推崇初级开发者在代码评审中向资深开发者提问，哪怕他们觉得自己的问题很傻或答案显而易见。如果对你来说并不显而易见，那就是成立的。对别人来说也不会显而易见！把问题问出来，给作者留出写下答案的空间，并把这一小段教育留给后来的人。

### 批准还是不批准

我把自己的评审看作一道可能阻止别人改进产品的关卡，所以我会凭良心慎重地保留批准。我常常有个人偏好，也会提出希望作者做的可选改动，但我不会仅凭这些就不给批准。如果我对某人的拉取请求有建议，但按现状它不会破坏生产环境、不会对用户造成负面影响，也不会引起其他问题，我就会批准并附上那些评论。作者可以选择在合并前处理我的反馈，也可以另开分支跟进。

评审代码时要考虑你的建议有多重要。为了让它被落实而推迟发布值得吗？值得让作者看反馈、做修改、等 CI、等再次评审、部署、最后合并这一整轮流程走一遍吗？如果一条建议不落实并不会让谁的日子更难过，那就让作者决定改不改、什么时候改。

[「请求更改」选项](https://docs.github.com/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request#submitting-your-review)会阻止拉取请求被合并，直到评审者回来批准它。我极少使用它，因为它通常显得过于强硬。我信任我的团队知道何时该批准拉取请求，所以队友的批准可以代替我的批准。同样，我也信任拉取请求作者会尊重并考虑我的反馈，而不是因为别人批准了、我没批准就盲目合并。我大概只有一种情况会选择「请求更改」：我认为存在紧迫的安全问题，并且担心他们在合并前看不到我的顾虑。

## 如何充分利用代码评审

### 评审你自己的代码

GitHub 高级软件工程师 [Paul Smith](https://github.com/paulcsmith) 教我，在请别人评审之前先评审自己的拉取请求，我也建议你这么做。先过一遍，对那些不明显的改动、或者如果出现在别人拉取请求里你会问起的改动，留下行内评论。自我评审还能帮助判断一个拉取请求是否过大、是否适合[拆分](https://github.blog/2020-05-21-github-protips-tips-tricks-hacks-and-secrets-from-sarah-vessels/)。

**特别推荐：** 如果你在意让拉取请求保持小巧，可以用 [lerebear/sizeup-action](https://github.com/lerebear/sizeup-action) 自动给拉取请求打上标明其复杂度与规模的标签。

### 欢迎合并后的评审

如果我碰巧在别人有机会评审之前就合并了某个拉取请求，我依然欢迎他们的评审。如果我的拉取请求弄坏了什么或产生了非预期后果，在拉取请求上评论说明，就能留下一条面包屑，帮助未来的读者追溯当时发生了什么！

如果我收到的是对已合并拉取请求的评审，我会像它还合入之前那样去处理反馈。也许是一条解释我视角的评论，也许是再开几个拉取请求来迭代我原先发布的代码。也可能是开新的 issue，把待做的工作记录下来。

### 使用草稿拉取请求

创建新拉取请求时，你可以选择把它设为草稿。我非常依赖[草稿阶段](https://docs.github.com/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request)来表明我是否需要评审。例如，如果某个必需的 CI 构建失败了，或者我只是还没做完，我就会把它保持为草稿。我也倾向于这样理解别人的拉取请求：如果它是草稿，我就假定作者还没准备好接受评审；如果它被标记为可以评审了，我就假定只差足够多的批准，它就能部署了。

草稿状态意味着拉取请求尚未完成，所以在解决合并冲突或处理评审反馈时，我会把拉取请求移回草稿。如果我必须修改代码，我会先把拉取请求标记为草稿，以免让已经评审过的人不堪重负。等我把它移回「可以评审」时，GitHub 会给那些评审者发通知，让他们再看一遍。

### 保持客气

有句话这时会浮现在我脑海里：「蜂蜜比醋能捉到更多苍蝇。」我希望自己的拉取请求得到评审，所以我喜欢回复自己拉取请求上的评论——尤其是在我不同意评审者的时候。即使我不回复某条评审意见，我也常常用 👍 表示同意，或用 ❤ 说声谢谢。

我希望评审者相信他们的建议不会被遗忘，所以我通过评论让他们始终了解进展。如果我同意他们的建议——比如进一步重构既有代码——我可能会在表示同意的同时，就当下这个拉取请求里是否要做这个改动提出保留意见。当我在后续的拉取请求里落实他们的反馈时，我会回来提供链接，让评审者知道他们的反馈没有被忽视。

我还会在后续实现这些建议的拉取请求里标记他们，并附上一句「这处理了 @某某 在 <previous pull request URL> 中的反馈」。这既为其他读者提供了上下文，也是对原评审者的点名致意，把这份点子的功劳记给他们。

当你兑现「在后续分支里处理反馈」的承诺时，这有助于与评审者建立信任，从而让他们更放心地批准你未来的拉取请求，因为他们知道你不会半途而废。

## 结语

代码评审对产品质量的重要性怎么强调都不为过，在 AI 生成代码的时代尤其如此。在我的职业生涯中，有很多次正是因为有了第二双眼睛，缺陷才被发现，事故才被避免。代码评审非常值得投入时间，无论是花在日常评审、梳理流程，还是构建支持它的自动化上。对开发者来说，现在就把拉取请求评审透彻，比日后去处理一个已经发到生产环境的问题更快、也更少痛苦。

感谢你如此在意代码质量，愿意读我这套代码评审的理念。你最近看过[你的评审队列](https://github.com/search?q=review-requested:@me+is:open+archived:false&type=pullrequests)吗？也许现在正是把这些想法付诸行动的好时机。

如果你想进一步了解如何在 GitHub 上使用拉取请求评审，可以看看 GitHub Community 上由资深 DevOps 架构师 [Mickey Gousset](https://github.com/mickeygousset) 与资深 DevOps 架构师 [Joshua Johanning](https://github.com/joshjohanning) 发表的讨论：[评审拉取请求的 5 个技巧](https://github.com/orgs/community/discussions/130771)。

## 标签：

## 作者

![Sarah Vessels](https://avatars.githubusercontent.com/u/82317?v=4&s=200)

GitHub 资深软件工程师

## 相关文章

[职业成长](https://github.blog/developer-skills/career-growth/)

### [从编码者到编排器：智能体如何改变开发者的角色](https://github.blog/developer-skills/career-growth/from-coder-to-orchestrator-how-agents-shift-the-role-of-a-developer/)

开发者正在负责代码之外更多交付体系的工作，而不仅仅是代码本身。欢迎在 GitHub Universe 期间与更多开发者相聚、学到新东西，并探索接下来会发生什么。

![Copilot 出现在带有散落绿色方块的装饰背景前。](https://github.blog/wp-content/uploads/2026/01/generic-github-copilot-logo-stripe.png?resize=400%2C212)

[AI 与机器学习](https://github.blog/ai-and-ml/)

### [GitHub Copilot 应用中的堆叠会话与拉取请求](https://github.blog/ai-and-ml/github-copilot/stacked-sessions-and-pull-requests-in-the-github-copilot-app/)

了解我如何用 GitHub Copilot 应用中的堆叠会话与拉取请求，把一个旧代码库现代化。

### [说「是」的代价已经变了](https://github.blog/engineering/the-cost-of-saying-yes-has-changed/)

写代码的代价下降了；拥有它的代价没有。一个用于判断在 AI 时代哪些改动才真正便宜的框架。
