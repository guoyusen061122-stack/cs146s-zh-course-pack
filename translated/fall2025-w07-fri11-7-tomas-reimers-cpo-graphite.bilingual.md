# Tomas Reimers, CPO Graphite（fall2025 W7）

# Tomas Reimers, CPO Graphite（fall2025 W7）

## Slide 1

## Slide 1

CS146S ∙ Stanford University, Fall 2025 The Modern Software Developer: Code Review

CS146S ∙ Stanford University，Fall 2025 The Modern Software Developer: 代码评审

## Slide 2

## Slide 2

Agenda 00 Hi! 01 Collaborating with humans 02 Collaborating with AI 03 Software development in the limit

议程 00 你好！ 01 与人协作 02 与 AI 协作 03 极限状态下的软件开发

## Slide 3

## Slide 3

Hi! Who am I? What is Graphite?

你好！ 我是谁？ Graphite 是什么？

## Slide 4

## Slide 4

Graphite is the AI-powered code review platform helping developers create, review, and merge code changes.

Graphite 是 AI 驱动的代码评审平台，帮助开发者创建、评审并合并代码改动。

## Slide 5

## Slide 5

The AI-native code review platform INTRODUCTION Our AI agent can answer questions about the PR. It is fully codebase aware. It can also propose updates, helping reviewers quickly resolve comments and CI.

AI 原生的代码评审平台 引言 我们的 AI 智能体可以回答关于这个 PR 的问题。 它完全了解代码库。 它还能提出修改建议，帮助评审人快速解决评论与 CI 问题。

## Slide 6

## Slide 6

A best-in-class code review platform built on-top of GitHub. Graphite provides a streamlined interface to create, review, and merge PRs, instantly and bi-directionally synced with GitHub. Trusted by the developers and companies you already know. We’re fortunate enough to collaborate with some of the biggest names in technology, and improve developer velocity across a wide swath of metrics. Conﬁdential INTRODUCTION Graphite at a glance Graphite helps engineers ship more. +33% Increase in PRs shipped per developer after adopting Graphite at Shopify 100,000s+ Trusted by 100,000s of developers at 1,000s of organizations +21% LoC/eng at Asana -74% Time between PRs merged at Ramp

一个构建在 GitHub 之上的顶级代码评审平台。 Graphite 提供精简的界面来创建、评审并合并 PR，与 GitHub 瞬时双向同步。 已被你熟悉的开发者和公司信任。 我们很幸运能与一些科技界最知名的公司合作，并在多项指标上提升开发速度。 机密 引言 Graphite 速览 Graphite 帮助工程师交付更多。 +33% Shopify 采用 Graphite 后每位开发者交付的 PR 增幅 100,000s+ 被 1,000s 家组织中的 100,000s 名开发者信任 +21% Asana 每位工程师的代码行数 -74% Ramp PR 合并间隔时间

## Slide 7

## Slide 7

Collaborating with humans How developers work together

与人协作 开发者如何一起工作

## Slide 8

## Slide 8

COLLABORATING WITH HUMANS How developers collaborate A developer proposes a set of code changes, this atomic unit is called a pull request . (a.k.a. diff, patch, changelist, or merge request) The original developer merges their pull request back into the codebase. CREATE REVIEW MERGE Another developer reﬁnes (suggests improvements) through comments and ultimately approves the pull request.

与人协作 开发者如何协作 一位开发者提出一组代码改动，这个原子单元称为拉取请求（pull request） （也叫差异（diff）、补丁（patch）、变更列表（changelist）或合并请求（merge request）） 原始开发者把自己的拉取请求合并回代码库。 创建 评审 合并 另一位开发者通过评论提出改进建议 ，并最终批准该拉取请求。

## Slide 9

## Slide 9

AI means more code than ever is being created, but that also means more code needs to be reviewed and merged .

AI 意味着产生的代码比以往任何时候都多，但这也意味着需要评审和合并的代码更多 。

## Slide 10

## Slide 10

IBM, 1976: an engineer named Michael Fagan introduces Fagan Inspections . ( Link to paper ) The birth of code review: Fagan Inspections COLLABORATING WITH HUMANS

IBM，1976 年：一位名叫 Michael Fagan 的工程师提出 Fagan 检查法 。 （ 论文链接 ） 代码评审的诞生：Fagan 检查法 与人协作

## Slide 11

## Slide 11

Emailed patches replace printed code. The Linux kernel still does this. The birth of code review: Email patches COLLABORATING WITH HUMANS From Icenowy Zheng <REDACTED> Subject [PATCH v3 5/7] clk: sunxi-ng: add support for the Allwinner H6 CCU Date Fri, 23 Feb 2018 20:35:53 +0800 The Allwinner H6 SoC has a CCU which has been largely rearranged. Add support for it in the sunxi-ng CCU framework. diff --git a/…/bindings/clock/sunxi-ccu.txt b/…/bindings/clock/sunxi-ccu.txt index 4ca21c3a6fc9..9ae27881c924 100644 --- a/…/bindings/clock/sunxi-ccu.txt +++ b/…/bindings/clock/sunxi-ccu.txt @@ -20,6 +20,7 @@ Required properties :

邮件补丁取代了打印出来的代码。 Linux 内核至今仍这么做。 代码评审的诞生：邮件补丁 与人协作 发件人 Icenowy Zheng <REDACTED> 主题 [PATCH v3 5/7] clk: sunxi-ng: add support for the Allwinner H6 CCU 日期 Fri, 23 Feb 2018 20:35:53 +0800 Allwinner H6 SoC 的 CCU 已大幅重排。 请在 sunxi-ng CCU 框架中为其添加支持。 diff --git a/…/bindings/clock/sunxi-ccu.txt b/…/bindings/clock/sunxi-ccu.txt index 4ca21c3a6fc9..9ae27881c924 100644 --- a/…/bindings/clock/sunxi-ccu.txt +++ b/…/bindings/clock/sunxi-ccu.txt @@ -20,6 +20,7 @@ Required properties :

- "allwinner,sun50i-a64-ccu"
- "allwinner,sun50i-a64-r-ccu"
- "allwinner,sun50i-h5-ccu"

- "allwinner,sun50i-a64-ccu"
- "allwinner,sun50i-a64-r-ccu"
- "allwinner,sun50i-h5-ccu"

+

+

- "allwinner,sun50i-h6-ccu"
- "nextthing,gr8-ccu"

- "allwinner,sun50i-h6-ccu"
- "nextthing,gr8-ccu"

## Slide 12

## Slide 12

Google, early 2000s: Guido van Rossum* introduces Mondrian : a web UI for review.

Google，2000 年代初期：Guido van Rossum* 提出 Mondrian ：一个用于评审的 Web 界面。

- yes, Python’s Benevolent

- 是的，就是 Python 的仁慈

Dictator The birth of code review: Mondrian COLLABORATING WITH HUMANS

独裁者 代码评审的诞生：Mondrian 与人协作

## Slide 13

## Slide 13

Tools such as:

诸如：

- 

- 

Review Board

Review Board

- 

- 

Gerrit / Critique (Google)

Gerrit / Critique (Google)

- 

- 

Phabricator (Facebook)

Phabricator (Facebook)

- 

- 

GitHub Make their way into the public tool chain, popularizing the practice of code review . The birth of code review: Online tools COLLABORATING WITH HUMANS

GitHub 这类工具进入公共工具链，让代码评审这一实践流行起来 。 代码评审的诞生：在线工具 与人协作

## Slide 14

## Slide 14

Collaborating with AI Keeping up with super-human authors.

与 AI 协作 跟上超人级的作者。

## Slide 15

## Slide 15

AI can already catch more than typos Graphite will proactively scan PRs for bugs. It posts potential issues to both Graphite and GitHub. It works great out of the box and is fully customizable. COLLABORATING WITH AI

AI 已经能发现的不只是错别字 Graphite 会主动扫描 PR 中的 bug。 它把潜在问题同时发布到 Graphite 和 GitHub。 它开箱即用，并且完全可定制。 与 AI 协作

## Slide 16

## Slide 16

COLLABORATING WITH AI With AI, do humans even need to do code review?

与 AI 协作 有了 AI，人类还需要做代码评审吗？

## Slide 17

## Slide 17

01 Alignment conﬁrmation 02 Knowledge diffusion Proofreading 03 The purpose(s) of code review (in order) COLLABORATING WITH AI

01 对齐确认 02 知识扩散 校对 03 代码评审的目的 （按顺序） 与 AI 协作

## Slide 18

## Slide 18

COLLABORATING WITH AI How will humans collaborate with AI? Better for context gathering and augmenting human reviewers. Better for replacing human reviewers entirely. PLATFORM PARTICIPANT

与 AI 协作 人类将如何与 AI 协作？ 更擅长收集上下文，并增强人类评审人。 更擅长完全取代人类评审人。 平台 参与者

## Slide 19

## Slide 19

Live demo

现场演示

## Slide 20

## Slide 20

The limits of AI (today) COLLABORATING WITH AI

AI 的局限（今天） 与 AI 协作

## Slide 21

## Slide 21

The limits of AI (tomorrow) COLLABORATING WITH AI

AI 的局限（明天） 与 AI 协作

## Slide 22

## Slide 22

Software development in the limit Where do we go from here.

极限状态下的软件开发 接下来往哪里走。

## Slide 23

## Slide 23

Software development has always had two parts IN THE LIMIT

软件开发一直包含两部分 极限状态

## Slide 24

## Slide 24

Software development has always had two parts The “inner loop” focused on development IN THE LIMIT

软件开发一直包含两部分 「内环」 聚焦开发 极限状态

## Slide 25

## Slide 25

Software development has always had two parts The “outer loop” focused on review & collaboration IN THE LIMIT

软件开发一直包含两部分 「外环」 聚焦评审 与协作 极限状态

## Slide 26

## Slide 26

AI is already making the inner loop 10x faster IN THE LIMIT

AI 已经让内环快了 10 倍 极限状态

## Slide 27

## Slide 27

What happens to the outer loop? IN THE LIMIT

外环会怎样？ 极限状态

## Slide 28

## Slide 28

IN THE LIMIT Three doors for the next generation software dev Developers directly review changes, augmented by AI. If they’re not authoring the code, does this still make sense? Developers treat AI as a third-party contractor. Underwriting product requirements but not code . CYBORG EM AGENCY Developers manage AI directly. Underwriting architecture, but maybe not technical speciﬁcs.

极限状态 下一代软件开发者的三扇门 开发者直接评审改动，由 AI 增强。 如果他们不写代码，这样做还成立吗？ 开发者把 AI 当作第三方外包。 对产品需求负责，但不对代码负责 。 半人马 雇员 智能体托管 开发者直接管理 AI。 对架构负责，但或许不对技术细节负责。

## Slide 29

## Slide 29

AI Review Agent Graphite Agent is your AI-powered companion to catch bugs, enforce your organization’s conventions, and make sure errors and security vulnerabilities stay out of your codebase. Smarter CI Predictive CI that only runs when you need it. Saving your team time and money. A review experience built for teams Supercharge your team with reviewer assignment, merge queues, automations, and insights. Measure developer productivity See exactly how much more efﬁcient AI-generated coding tools & Graphite’s code review are making your developers with actionable insights. Stacking A git workﬂow optimized for authors who want to keep developing without being blocked on their reviewers.

AI 评审智能体 Graphite Agent 是你的 AI 驱动伙伴，负责抓 bug、执行组织约定，并确保错误与安全漏洞进不了你的代码库。 更聪明的 CI 只在需要时运行的预测式 CI。为团队节省时间和成本。 为团队打造的评审体验 用评审人分配、合并队列、自动化与洞察，为你的团队提速。 度量开发者生产率 用可执行的洞察，清楚看到 AI 编码工具与 Graphite 代码评审为开发者提升了多少效率。 堆叠 一种为作者优化的 git 工作流，让作者无需被评审人阻塞即可持续开发。

## Slide 30

## Slide 30

Thank you! Any questions?

谢谢！有问题吗？
