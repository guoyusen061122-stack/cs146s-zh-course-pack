# Getting AI to Work In Complex Codebases

# 让 AI 在复杂代码库中真正干活

# Getting AI to Work in Complex Codebases

# 让 AI 在复杂代码库中真正干活

It seems pretty well-accepted that AI coding tools struggle with real production codebases. The [Stanford study on AI's impact on developer productivity](https://www.youtube.com/watch?v=tbDDYKRFjhk) found:

AI 编码工具在真实的生产代码库中很吃力，这一点似乎已被普遍接受。[关于 AI 对开发者生产力影响的斯坦福研究](https://www.youtube.com/watch?v=tbDDYKRFjhk)发现：

1. A lot of the "extra code" shipped by AI tools ends up just reworking the slop that was shipped last week.
1. Coding agents are great for new projects or small changes, but in large established codebases, they can often make developers *less* productive.

1. AI 工具交付的大量「额外代码」，最终只是在返工上周交付的垃圾代码。
1. 编码智能体非常适合新项目或小改动，但在大型成熟代码库中，它们往往会让开发者的效率*更低*。

The common response is somewhere between the pessimist "this will never work" and the more measured "maybe someday when there are smarter models."

常见的反应介于悲观者的「这永远行不通」与更克制的「也许等模型更聪明的那一天」之间。

After several months of tinkering, I've found that **you can get really far with today's models if you embrace core context engineering principles**.

在几个月的摸索之后，我发现**只要拥抱核心的上下文工程原则，用当今的模型就能走得很远**。

This isn't another "10x your productivity" pitch. I [tend to be pretty measured when it comes to interfacing with the ai hype machine](https://hlyr.dev/12fa). But we've stumbled into workflows that leave me with considerable optimism for what's possible. We've gotten claude code to handle 300k LOC Rust codebases, ship a week's worth of work in a day, and maintain code quality that passes expert review. We use a family of techniques I call "frequent intentional compaction" - deliberately structuring how you feed context to the AI throughout the development process.

这不是又一篇「让生产力提升 10 倍」的推销。面对 AI 炒作机器，我[一向比较克制](https://hlyr.dev/12fa)。但我们偶然摸索出的一些工作流，让我对可能性相当乐观。我们让 Claude Code 处理 30 万行 LOC 的 Rust 代码库，在一天内交付一周的工作量，并维持能通过专家评审的代码质量。我们使用的是一套我称为「频繁的有意压缩」的技术——在整个开发过程中刻意设计如何向 AI 投喂上下文。

I am now fully convinced that AI for coding is not just for toys and prototypes, but rather a deeply technical engineering craft.

我现在完全确信，AI 编码不只是用来做玩具和原型的，而是一门技术性很强的工程手艺。

**Video Version**: If you prefer video, this post is based on [a talk given at Y Combinator on August 20th](https://hlyr.dev/ace)

**视频版**：如果你更喜欢看视频，本文基于 [8 月 20 日在 Y Combinator 的一次演讲](https://hlyr.dev/ace)

### Grounding Context from AI Engineer

### 来自 AI Engineer 的背景铺垫

Two talks from AI Engineer 2025 fundamentally shaped my thinking about this problem.

AI Engineer 2025 上的两场演讲从根本上塑造了我对这个问题的思考。

The first is [Sean Grove's talk on "Specs are the new code"](https://www.youtube.com/watch?v=8rABwKRsec4) and the second is [the Stanford study on AI's impact on developer productivity](https://www.youtube.com/watch?v=tbDDYKRFjhk).

第一场是 [Sean Grove 关于「规格即新代码」的演讲](https://www.youtube.com/watch?v=8rABwKRsec4)，第二场是[关于 AI 对开发者生产力影响的斯坦福研究](https://www.youtube.com/watch?v=tbDDYKRFjhk)。

Sean argued that we’re all *vibe coding wrong*. The idea of chatting with an AI agent for two hours, specifying what you want, and then throwing away all the prompts while committing only the final code… is like a Java developer compiling a JAR and checking in the compiled binary while throwing away the source.

Sean 认为我们*用 vibe coding 的方式全都错了*。跟 AI 智能体聊上两小时、说明你想要什么，然后把所有提示词都丢掉、只提交最终代码……这就像一位 Java 开发者编译出 JAR，把编译产物签入仓库，却把源码扔掉。

Sean proposes that in the AI future, the specs will become the real code. That in two years, you'll be opening python files in your IDE with about the same frequency that, today, you might open up a hex editor to read assembly (which, for most of us, is never).

Sean 提出，在 AI 的未来，规格将成为真正的代码。两年后，你在 IDE 里打开 python 文件的频率，大约会等同于今天你打开十六进制编辑器去读汇编的频率（对我们大多数人来说，就是从不打开）。

[Yegor's talk on developer productivity](https://www.youtube.com/watch?v=tbDDYKRFjhk) tackled an orthogonal problem. They analyzed commits from 100k developers and found, among other things,

[Yegor 关于开发者生产力的演讲](https://www.youtube.com/watch?v=tbDDYKRFjhk)处理的是一个正交的问题。他们分析了 10 万名开发者的提交，发现的事情之一是，

1. That AI tools often lead to a lot of rework, diminishing the perceived productivity gains

1. AI 工具常常导致大量返工，削弱了人们感知到的生产力提升

<img width="2008" height="1088" alt="image" src="https://github.com/user-attachments/assets/f7cec497-3ee2-47d1-8f91-a18210625e19" />

<img width="2008" height="1088" alt="image" src="https://github.com/user-attachments/assets/f7cec497-3ee2-47d1-8f91-a18210625e19" />

1. That AI tools work well for greenfield projects, but are often counter-productive for brownfield codebases and complex tasks

1. AI 工具在全新项目上效果很好，但对存量代码库和复杂任务往往适得其反

<img width="1326" height="751" alt="Screenshot 2025-08-29 at 10 55 32 AM" src="https://github.com/user-attachments/assets/06f03232-f9d9-4a92-a182-37056bf877a4" />

<img width="1326" height="751" alt="Screenshot 2025-08-29 at 10 55 32 AM" src="https://github.com/user-attachments/assets/06f03232-f9d9-4a92-a182-37056bf877a4" />

This matched what I heard talking with founders:

这与我同创始人交流时听到的说法一致：

- “Too much slop.”
- “Tech debt factory.”
- “Doesn’t work in big repos.”
- “Doesn’t work for complex systems.”

- 「垃圾代码太多。」
- 「技术债工厂。」
- 「在大型仓库里不管用。」
- 「对复杂系统不管用。」

The general vibe on AI-coding for hard stuff tends to be

对于用 AI 编码处理难活，普遍的调子往往是

> Maybe someday, when models are smarter…

> 也许某一天，等模型更聪明了……

Heck even [Amjad](https://x.com/amasad) was on a [lenny's podcast 9 months ago](https://www.lennysnewsletter.com/p/behind-the-product-replit-amjad-masad) talking about how PMs use Replit agent to prototype new stuff and then they hand it off to engineers to implement for production. (Disclaimer: i haven't caught up with him recently (ok, ever), this stance may have changed)

甚至 [Amjad](https://x.com/amasad) 也在 [9 个月前的 lenny's 播客](https://www.lennysnewsletter.com/p/behind-the-product-replit-amjad-masad)里说，产品经理用 Replit agent 给新东西做原型，然后交给工程师去实现生产版本。 （免责声明：我最近没跟他交流过（好吧，其实从来没有），这个立场可能已经变了）

Whenever I hear "Maybe someday when the models are smart" I generally leap to exclaim **that's what context engineering is all about**: getting the most out of *today's* models.

每当我听到「也许某一天等模型更聪明了」，我一般都会跳起来反驳：**这正是上下文工程的意义所在**——从*当今*的模型里榨取最大价值。

### What's actually possible today

### 今天实际能做到什么

I'll deep dive on this a bit futher down, but to prove this isn't just theory, let me outline a concrete example. A few weeks ago, I decided to test our techniques on [BAML](https://github.com/BoundaryML/baml), a 300k LOC Rust codebase for a programming language that works with LLMs. I'm at best an amateur Rust dev and had never touched the BAML codebase before.

我会在后文深入展开，但为了证明这不只是理论，先举一个具体例子。几周前，我决定在一套 30 万行 LOC 的 Rust 代码库 [BAML](https://github.com/BoundaryML/baml) 上检验我们的技术。BAML 是一门与 LLM 配合使用的编程语言。我顶多算个业余 Rust 开发者，此前从未接触过 BAML 代码库。

Within an hour or so, I had a [PR fixing a bug](https://github.com/BoundaryML/baml/pull/2259#issuecomment-3155883849) which was approved by the maintainer the next morning. A few weeks later, [@hellovai](https://x.com/hellovai) and I paired on shipping 35k LOC to BAML, adding [cancellation support](https://github.com/BoundaryML/baml/pull/2357) and [WASM compilation](https://github.com/BoundaryML/baml/pull/2330) - features the team estimated would take a senior engineer 3-5 days each. We got both draft prs ready in about 7 hours.

大约一小时内，我就提交了一个[修复 bug 的 PR](https://github.com/BoundaryML/baml/pull/2259#issuecomment-3155883849)，第二天早上得到了维护者的批准。几周后，我和 [@hellovai](https://x.com/hellovai) 结对向 BAML 交付了 3.5 万行 LOC，加入了[取消支持](https://github.com/BoundaryML/baml/pull/2357)和 [WASM 编译](https://github.com/BoundaryML/baml/pull/2330)——团队估计这两项功能各需要一位资深工程师花 3–5 天。我们在大约 7 小时内就把两个草稿 PR 准备好了。

Again, this is all built around a workflow we call [frequent intentional compaction](#what-works-even-better-frequent-intentional-compaction) - essentially designing your entire development process around context management, keeping utilization in the 40-60% range, and building in high-leverage human review at exactly the right points. We use a "research, plan, implement" workflow, but the core capabilities/learnings here are FAR more general than any specific workflow or set of prompts.

再次说明，这一切都围绕我们称为[频繁的有意压缩](#what-works-even-better-frequent-intentional-compaction)的工作流构建——本质上是以上下文管理为中心设计整个开发过程，把利用率保持在 40–60% 区间，并在恰到好处的节点嵌入高杠杆的人工评审。我们用的是「研究、计划、实现」工作流，但这里的核心能力与经验远比任何具体工作流或提示词集合更具普适性。

### Our weird journey to get here

### 我们走到这里的古怪历程

I was working with one of the most productive AI coders I've ever met. Every few days they'd drop **2000-line Go PRs**. And this wasn't a nextjs app or a CRUD API. This was complex, [race-prone systems code](https://github.com/humanlayer/humanlayer/blob/main/hld/daemon/daemon_subscription_integration_test.go#L45) that did JSON RPC over unix sockets and managed streaming stdio from forked unix processes (mostly claude code sdk processes, more on that later 🙂).

我曾与一位我见过最高产的 AI 编码者共事。 每隔几天，他就会丢出 **2000 行的 Go PR**。 而且这不是什么 nextjs 应用或 CRUD API。这是复杂的、[容易出现竞态的系统代码](https://github.com/humanlayer/humanlayer/blob/main/hld/daemon/daemon_subscription_integration_test.go#L45)，通过 unix socket 做 JSON RPC，并管理来自 fork 出的 unix 进程的流式 stdio（大多是 Claude Code SDK 进程，后面再细说 🙂）。

The idea of carefully reading 2,000 lines of complex Go code every few days was simply not sustainable. I was starting to feel a bit like Mitchell Hashimoto when he added the [AI contributions must be disclosed](https://github.com/ghostty-org/ghostty/pull/8289) rules for ghostty.

每隔几天就仔细读完 2000 行复杂 Go 代码，这种做法根本无法持续。我开始有点理解 Mitchell Hashimoto 当初为 ghostty 加上[必须披露 AI 贡献](https://github.com/ghostty-org/ghostty/pull/8289)规则时的心情。

Our approach was to adopt something like sean's **spec-driven development**.

我们的做法是采纳类似 Sean 的**规格驱动开发**。

It was uncomfortable at first. I had to learn to let go of reading every line of PR code. I still read the tests pretty carefully, but the specs became our source of truth for what was being built and why.

一开始很不舒服。 我必须学会放手，不再逐行阅读 PR 代码。 测试我仍然会读得比较仔细，但规格成了我们判断「在建什么、为什么建」的事实来源。

The transformation took about 8 weeks. It was incredibly uncomfortable for everyone involved, not least of all for me. But now we're flying. A few weeks back, I shipped 6 PRs in a day. I can count on one hand the number of times I've edited a non-markdown file by hand in the last three months.

这个转变花了大约 8 周。 对参与其中的每个人来说都极不舒服，尤其是我。 但现在我们飞起来了。几周前，我在一天内交付了 6 个 PR。 过去三个月里，我手工编辑非 markdown 文件的次数一只手就数得过来。

## Advanced Context Engineering for Coding Agents

## 面向编码智能体的高级上下文工程

What we needed was:

我们需要的是：

- AI that Works Well in Brownfield Codebases
- AI that Solves Complex Problems
- No Slop
- Maintain Mental Alignment across the team

- 在存量代码库中工作良好的 AI
- 能解决复杂问题的 AI
- 不产垃圾
- 在团队内维持认知对齐

(And yeah sure, let's try to spend as many tokens as possible.)

（当然啦，也让我们尽量多花点 token。）

I'll dive into:

我会深入讲：

1. what we learned applying context engineering to coding agents
1. the dimensions along which using these agents is a deeply technical craft
1. why I don't believe these approaches are generalizable
1. the number of times I've been repeatedly proven wrong about (3)

1. 我们把上下文工程应用于编码智能体时学到的东西
1. 使用这些智能体为何在多个维度上是一门技术性很强的手艺
1. 我为什么认为这些方法无法普适
1. 关于第 3 点，我反复被证明是错的次数

### But first: The Naive Way to manage agent context

### 但首先：管理智能体上下文的天真做法

Most of us start by using a coding agent like a chatbot. You talk (or [drunkenly shout](https://ghuntley.com/six-month-recap/#:~:text=Last%20week%2C%20over%20Zoom%20margaritas%2C%20a%20friend%20and%20I%20reminisced%20about%20COBOL.)) back and forth with it, vibing your way through a problem until you either run out of context, give up, or the agent starts apologizing.

我们大多数人一开始都像用聊天机器人那样使用编码智能体。你与它来回交谈（或者[醉醺醺地冲它喊](https://ghuntley.com/six-month-recap/#:~:text=Last%20week%2C%20over%20Zoom%20margaritas%2C%20a%20friend%20and%20I%20reminisced%20about%20COBOL.))，一路凭感觉把问题混过去，直到上下文用尽、你放弃，或者智能体开始道歉。

<img width="7718" height="4223" alt="image" src="https://github.com/user-attachments/assets/7361a203-9d95-42e2-ac16-1f38b04adb58" />

<img width="7718" height="4223" alt="image" src="https://github.com/user-attachments/assets/7361a203-9d95-42e2-ac16-1f38b04adb58" />

A slightly smarter way is to just start over when you get off track, discarding your session and starting a new one, perhaps with a little more steering in the prompt.

稍微聪明一点的做法是：一旦跑偏就从头开始，丢弃当前会话、开一个新的，也许在提示词里多加一点引导。

> [original prompt], but make sure you use XYZ approach, because ABC approach won't work

> [原始提示词]，但要确保使用 XYZ 方式，因为 ABC 方式行不通

<img width="7727" height="4077" alt="image" src="https://github.com/user-attachments/assets/1bbbc8ad-60da-4f8b-98c3-e6603b04a0ce" />

<img width="7727" height="4077" alt="image" src="https://github.com/user-attachments/assets/1bbbc8ad-60da-4f8b-98c3-e6603b04a0ce" />

### Slightly Smarter: Intentional Compaction

### 稍微聪明一点：有意压缩

You have probably done something I've come to call "intentional compaction". Whether you're on track or not, as your context starts to fill up, you probably want to pause your work and start over with a fresh context window. To do this, you might use a prompt like

你很可能做过一件我称之为「有意压缩」的事。无论进展是否顺利，当上下文开始填满时，你大概会想暂停工作，用一个全新的上下文窗口重新开始。为此，你可能会用这样一个提示词

> "Write everything we did so far to progress.md, ensure to note the end goal, the approach we're taking, the steps we've done so far, and the current failure we're working on"

> 「把我们目前做的所有事情写到 progress.md，务必记录最终目标、我们采取的方式、目前完成的步骤，以及当前正在处理的失败」

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/64b940e5-89b1-4f6c-a79c-ec2810d9af77" />

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/64b940e5-89b1-4f6c-a79c-ec2810d9af77" />

You can also [use commit messages for intentional compaction](https://x.com/dexhorthy/status/1961490837017088051).

你也可以[用提交信息来做有意压缩](https://x.com/dexhorthy/status/1961490837017088051)。

### What Exactly Are We Compacting?

### 我们到底在压缩什么？

What eats up context?

什么在吞噬上下文？

- Searching for files
- Understanding code flow
- Applying edits
- Test/build logs
- Huge JSON blobs from tools

- 搜索文件
- 理解代码流转
- 应用编辑
- 测试/构建日志
- 来自工具的巨大 JSON 数据块

All of these can flood the context window. **Compaction** is simply distilling them into structured artifacts.

这些都会淹没上下文窗口。**压缩**就是把它们蒸馏成结构化的产物。

A good output for an intentional compaction might include something like

一次有意压缩的良好产出可能包含类似这样的内容

<img width="1309" height="747" alt="Screenshot 2025-08-29 at 11 10 36 AM" src="https://github.com/user-attachments/assets/a7d5946d-4e81-46e8-b314-d02dae1f00ee" />

<img width="1309" height="747" alt="Screenshot 2025-08-29 at 11 10 36 AM" src="https://github.com/user-attachments/assets/a7d5946d-4e81-46e8-b314-d02dae1f00ee" />

### Why obsess over context?

### 为什么要执着于上下文？

As we went deep on in [12-factor agents](https://hlyr.dev/12fa), LLMs are stateless functions. The only thing that affects the quality of your output (without training/tuning models themselves) is the quality of the inputs.

正如我们在 [12-factor agents](https://hlyr.dev/12fa) 中深入讨论过的，LLM 是无状态函数。在不训练/调优模型本身的前提下，唯一影响输出质量的就是输入的质量。

This is just as true for [wielding](https://www.youtube.com/watch?v=F_RyElT_gJk) coding agents as it is for general agent design, you just have a smaller problem space, and rather than building agents, we're talking about using agents.

这一点对[驾驭](https://www.youtube.com/watch?v=F_RyElT_gJk)编码智能体和对通用智能体设计同样成立，只是问题空间更小，而且我们讨论的不是构建智能体，而是使用智能体。

At any given point, a turn in an agent like claude code is a stateless function call. Context window in, next step out.

在任意时刻，像 Claude Code 这样的智能体的一轮交互都是一次无状态函数调用。输入上下文窗口，输出下一步。

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/c1e920e8-5dc5-4dd2-b76d-853b85a92e6a" />

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/c1e920e8-5dc5-4dd2-b76d-853b85a92e6a" />

That is, the contents of your context window are the ONLY lever you have to affect the quality of your output. So yeah, it's worth obsessing over.

也就是说，上下文窗口的内容是你影响输出质量的唯一杠杆。所以，确实值得执着。

You should optimize your context window for:

你应当针对以下方面优化上下文窗口：

1. Correctness
1. Completeness
1. Size
1. Trajectory

1. 正确性
1. 完整性
1. 大小
1. 轨迹

Put another way, the worst things that can happen to your context window, in order, are:

换个说法，上下文窗口可能遭遇的最糟糕情况，按严重程度排序是：

1. Incorrect Information
1. Missing Information
1. Too much Noise

1. 信息不正确
1. 信息缺失
1. 噪声过多

If you like equations, here's a dumb one you can reference:

如果你喜欢公式，这里有一个很蠢的公式可供参考：

<img width="1320" height="235" alt="Screenshot 2025-08-29 at 11 11 30 AM" src="https://github.com/user-attachments/assets/a6ea98a6-665b-48af-983b-a1cb2c45e44c" />

<img width="1320" height="235" alt="Screenshot 2025-08-29 at 11 11 30 AM" src="https://github.com/user-attachments/assets/a6ea98a6-665b-48af-983b-a1cb2c45e44c" />

As [Geoff Huntley](https://x.com/GeoffreyHuntley) puts it,

正如 [Geoff Huntley](https://x.com/GeoffreyHuntley) 所说，

> The name of the game is that you only have approximately **170k of context window** to work with. 
> So it's essential to use as little of it as possible. 
> The more you use the context window, the worse the outcomes you'll get.

> 这件事的关键在于，你大约只有 **170k 的上下文窗口**可用。
> 所以，尽可能少用它至关重要。
> 你用得越多，得到的结果就越差。

Geoff's solution to this engineering constraint is a technique he calls [Ralph Wiggum as a Software Engineer](https://ghuntley.com/ralph/), which basically involves running an agent in a while loop forever with a simple prompt.

Geoff 应对这一工程约束的方案，是一种他称为 [Ralph Wiggum as a Software Engineer](https://ghuntley.com/ralph/) 的技术，基本上就是用一段简单的提示词把智能体放进 while 循环里无限运行。

```
while :; do
  cat PROMPT.md | npx --yes @sourcegraph/amp 
done
```

If you wanna learn more about ralph or what's in PROMPT.md, you can check out Geoff's post or dive into the project that [@simonfarshid](https://x.com/simonfarshid), [@lantos1618](https://x.com/lantos1618), [@AVGVSTVS96](https://x.com/AVGVSTVS96) and I built at last weekend's YC Agents Hackathon, which was able to (mostly) [port BrowserUse to TypeScript overnight](https://github.com/repomirrorhq/repomirror/blob/main/repomirror.md)

如果你想进一步了解 ralph 或 PROMPT.md 里有什么，可以看看 Geoff 的文章，或者研究一下 [@simonfarshid](https://x.com/simonfarshid)、[@lantos1618](https://x.com/lantos1618)、[@AVGVSTVS96](https://x.com/AVGVSTVS96) 和我在上周末 YC Agents Hackathon 上构建的项目——它（基本）能[在一夜之间把 BrowserUse 移植到 TypeScript](https://github.com/repomirrorhq/repomirror/blob/main/repomirror.md)

Geoff describes ralph as a "hilariously dumb" solution to the context window problem. [I'm not entirely sure that it is dumb](https://ghuntley.com/content/images/size/w2400/2025/07/The-ralph-Process.png).

Geoff 把 ralph 形容为应对上下文窗口问题「蠢得好笑」的方案。[我并不完全确定它蠢](https://ghuntley.com/content/images/size/w2400/2025/07/The-ralph-Process.png)。

### Back to compaction: Using Sub-Agents

### 回到压缩：使用子智能体

Subagents are another way to manage context, and generic subagents (i.e. not [custom](https://docs.anthropic.com/en/docs/claude-code/sub-agents) ones) have been a feature of claude code and many coding CLIs since the early days.

子智能体是另一种管理上下文的方式。通用子智能体（即非[自定义](https://docs.anthropic.com/en/docs/claude-code/sub-agents)的子智能体）从早期起就是 Claude Code 和许多编码 CLI 的功能。

Subagents are not about [playing house and anthropomorphizing roles](https://x.com/dexhorthy/status/1950288431122436597). Subagents are about context control.

子智能体不是用来[过家家、把角色拟人化](https://x.com/dexhorthy/status/1950288431122436597)的。子智能体关乎上下文控制。

The most common/straightforward use case for subagents is to let you use a fresh context window to do finding/searching/summarizing that enables the parent agent to get straight to work without clouding its context window with `Glob` / `Grep` / `Read` / etc calls.

子智能体最常见、最直接的用法，是让你用一个全新的上下文窗口去做查找/检索/总结，从而让父智能体直接开始干活，不必用 `Glob` / `Grep` / `Read` 等调用来污染自己的上下文窗口。

https://github.com/user-attachments/assets/cb4e7864-9556-4eaa-99ca-a105927f484d

https://github.com/user-attachments/assets/cb4e7864-9556-4eaa-99ca-a105927f484d

<details><summary>(video not playing on mobile? expand for the static image version)</summary> <img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/c72e7dba-1476-4ee9-9cb0-0f97d428b82a" /> </details>

<details><summary>（手机上无法播放视频？展开查看静态图片版本）</summary> <img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/c72e7dba-1476-4ee9-9cb0-0f97d428b82a" /> </details>

The ideal subagent response probably looks similar to the ideal ad-hoc compaction from above

理想的子智能体响应，大概和上面那种理想的临时压缩看起来差不多

<img width="1309" height="747" alt="Screenshot 2025-08-29 at 11 10 36 AM" src="https://github.com/user-attachments/assets/a7d5946d-4e81-46e8-b314-d02dae1f00ee" />

<img width="1309" height="747" alt="Screenshot 2025-08-29 at 11 10 36 AM" src="https://github.com/user-attachments/assets/a7d5946d-4e81-46e8-b314-d02dae1f00ee" />

Getting a subagent to return this is not trivial:

要让子智能体返回这样的结果并不容易：

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/2bcd30f6-84fd-4911-ac15-63f75619e76d" />

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/2bcd30f6-84fd-4911-ac15-63f75619e76d" />

### What works even better: Frequent Intentional Compaction

### 效果更好的做法：频繁的有意压缩

The techniques I want to talk about and that we've adopted in the last few months fall under what I call "frequent intentional compaction".

我想谈的、也是我们过去几个月采纳的技术，都属于我称为「频繁的有意压缩」的做法。

Essentially, this means designing your ENTIRE WORKFLOW around context management, and keeping utilization in the 40%-60% range (depends on complexity of the problem ).

本质上，这意味着围绕上下文管理来设计你的整个工作流，并把利用率保持在 40%–60% 区间（取决于问题的复杂度）。

The way we do it is to split into three (ish) steps.

我们的做法是拆成三步（大概三步）。

I say "ish" because sometimes we skip the research and go straight to planning, and sometimes we'll do multiple passes of compacted research before we're ready to implement.

我说「大概」，是因为有时我们会跳过研究直接进入计划，有时则要反复做几轮压缩后的研究，才准备开始实现。

I'll share example outputs of each step in a concrete example below. For a given feature or bug, we'll tend to do:

下面我会用一个具体例子展示每一步的产出示例。对于给定的功能或 bug，我们通常会做：

**Research**

**研究**

Understand the codebase, the files relevant to the issue, and how information flows, and perhaps potential causes of a problem.

理解代码库、与该 issue 相关的文件、信息如何流转，也许还有问题的潜在成因。

here's our [research prompt](https://github.com/humanlayer/humanlayer/blob/main/.claude/commands/research_codebase.md). It currently uses custom subagents, but in other repos I use a more generic version that uses the claude code Task() tool with `general-agent`. The generic one works almost as well.

这是我们用的[研究提示词](https://github.com/humanlayer/humanlayer/blob/main/.claude/commands/research_codebase.md)。 它目前使用自定义子智能体，但在其他仓库里我用一个更通用的版本，通过 Claude Code 的 Task() 工具配合 `general-agent` 来工作。 通用版本的效果几乎一样好。

**Plan**

**计划**

Outline the exact steps we'll take to fix the issue, and the files we'll need to edit and how, being super precise about the testing / verification steps in each phase.

列出我们修复该 issue 的确切步骤、需要编辑哪些文件以及如何编辑，并对每个阶段的测试/验证步骤做到极其精确。

This is the [prompt we use for planning](https://github.com/humanlayer/humanlayer/blob/main/.claude/commands/create_plan.md).

这是我们[用于计划的提示词](https://github.com/humanlayer/humanlayer/blob/main/.claude/commands/create_plan.md)。

**Implement**

**实现**

Step through the plan, phase by phase. For complex work, I'll often compact the current status back into the original plan file after each implementation phase is verified.

按阶段逐步执行计划。对于复杂工作，在每个实现阶段验证通过后，我常会把当前状态压缩回原始计划文件。

This is the [implementation prompt we use](https://github.com/humanlayer/humanlayer/blob/main/.claude/commands/implement_plan.md).

这是我们[使用的实现提示词](https://github.com/humanlayer/humanlayer/blob/main/.claude/commands/implement_plan.md)。

Aside - if you've been hearing a lot about git worktrees, this is the only step that needs to be done in a worktree. We tend to do everything else on main.

顺带说一句——如果你最近总听到 git worktree，这是唯一需要在 worktree 里完成的步骤。其他事情我们通常都在 main 上做。

**How we manage/share the markdown files**

**我们如何管理/共享这些 markdown 文件**

I will skip this part for brevity but feel free to launch a claude session in [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) and ask how the "thoughts tool" works.

为简洁起见这部分我略过，但你可以随时在 [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) 里启动一个 Claude 会话，问问「thoughts 工具」是怎么工作的。

### Putting this into practice

### 付诸实践

I do a [weekly live-coding session](https://github.com/ai-that-works/ai-that-works) with [@vaibhav](https://www.linkedin.com/in/vaigup/) where we whiteboard and code up a solution to an advanced AI Engineering problem. It's one of the highlights of my week.

我和 [@vaibhav](https://www.linkedin.com/in/vaigup/) 每周做一次[直播编码](https://github.com/ai-that-works/ai-that-works)，在白板上推演并写出一个高级 AI 工程问题的解法。这是我一周里最期待的事之一。

Several weeks ago, I [decided to share some more about the process](https://hlyr.dev/he-gh), curious if our in-house techniques could one-shot a fix to a 300k LOC Rust codebase for BAML, a programming language for working with LLMs. I picked out [an (admittedly small-ish) bug](https://github.com/BoundaryML/baml/issues/1252) from the @BoundaryML repo and got to work.

几周前，我[决定多分享一些过程](https://hlyr.dev/he-gh)，也很好奇我们的内部技术能否一次成型地修复 BAML 那套 30 万行 LOC 的 Rust 代码库——BAML 是一门与 LLM 配合使用的编程语言。我从 @BoundaryML 仓库里挑了一个[（确实偏小的）bug](https://github.com/BoundaryML/baml/issues/1252)，就开始干活了。

You can [watch the episode](https://hlyr.dev/he-yt) to learn more about the process, but to outline it:

你可以[观看这一期](https://hlyr.dev/he-yt)了解更多过程，先概述一下：

**Worth noting**: I am at best an amateur Rust dev, and I have never worked in the BAML codebase before.

**值得注意**：我顶多算个业余 Rust 开发者，而且此前从未在 BAML 代码库中工作过。

#### The research

#### 研究

- I created a piece of research, I read it. Claude decided the bug was invalid and the codebase was correct.
- I threw that research out and kicked off a new one, with more steering.
- here is [the final research doc i ended up using](https://github.com/ai-that-works/ai-that-works/blob/main/2025-08-05-advanced-context-engineering-for-coding-agents/thoughts/shared/research/2025-08-05_05-15-59_baml_test_assertions.md)

- 我生成了一份研究，然后读了它。Claude 判定这个 bug 不成立，代码库本身是正确的。
- 我把那份研究扔掉，带着更多引导重新发起了一份。
- 这是我最终使用的[研究文档](https://github.com/ai-that-works/ai-that-works/blob/main/2025-08-05-advanced-context-engineering-for-coding-agents/thoughts/shared/research/2025-08-05_05-15-59_baml_test_assertions.md)

#### The plans

#### 计划

- While the research was running, I got impatient and kicked off a plan, with no research, to see if claude could go straight to an implementation plan - [you can see it here](https://github.com/ai-that-works/ai-that-works/blob/main/2025-08-05-advanced-context-engineering-for-coding-agents/thoughts/shared/plans/fix-assert-syntax-validation-no-research.md)
- When the research was done, I kicked off another implementation plan that used the research results - [you can see it here](https://github.com/ai-that-works/ai-that-works/blob/main/2025-08-05-advanced-context-engineering-for-coding-agents/thoughts/shared/plans/baml-test-assertion-validation-with-research.md)

- 研究还在跑的时候，我等不及了，在没有任何研究的情况下发起了一份计划，想看看 Claude 能否直接给出实现计划——[你可以在这里看到](https://github.com/ai-that-works/ai-that-works/blob/main/2025-08-05-advanced-context-engineering-for-coding-agents/thoughts/shared/plans/fix-assert-syntax-validation-no-research.md)
- 研究完成后，我又发起了一份使用研究结果的实现计划——[你可以在这里看到](https://github.com/ai-that-works/ai-that-works/blob/main/2025-08-05-advanced-context-engineering-for-coding-agents/thoughts/shared/plans/baml-test-assertion-validation-with-research.md)

The plans are both fairly short, but they differ significantly. They fix the issue in different ways, and have different testing approaches. Without going too much into detail, they both "would have worked" but the one built with research fixed the problem in the *best* place and prescribed testing that was in line with the codebase conventions.

这两份计划都相当短，但差异明显。它们用不同方式修复问题，测试思路也不同。不展开太多细节：两者「本来都能解决问题」，但基于研究的那份把问题修在了*最恰当*的位置，并给出了符合代码库惯例的测试方案。

#### The implementation

#### 实现

- This was all happening the night before the podcast recording. I ran both plans in parallel and submitted both as PRs before signing off for the night.

- 这一切都发生在播客录制的前一晚。我并行跑了两份计划，并在收工睡觉前把两者都作为 PR 提交了。

By the time we were on the show at 10am PT the next day, [the PR from the plan with the research was already approved by @aaron](https://github.com/BoundaryML/baml/pull/2259#issuecomment-3155883849), who didn't even know I was doing a bit for a podcast 🙂. We [closed the other one](https://github.com/BoundaryML/baml/pull/2258/files).

到第二天太平洋时间上午 10 点我们上节目时，[那份基于研究的计划所产出的 PR 已经被 @aaron 批准](https://github.com/BoundaryML/baml/pull/2259#issuecomment-3155883849)，而他根本不知道我在为播客做一个小实验 🙂。我们[关掉了另一个 PR](https://github.com/BoundaryML/baml/pull/2258/files)。

So out of our original 4 goals, we hit:

所以在最初的 4 个目标中，我们达成了：

- ✅ Works in brownfield codebases (300k LOC rust project)
- Solves complex problems
- ✅ no slop (pr merged)
- Keeps mental alignment

- ✅ 在存量代码库中可用（30 万行 LOC 的 Rust 项目）
- 能解决复杂问题
- ✅ 不产垃圾（PR 已合并）
- 保持认知对齐

### Solving complex problems

### 解决复杂问题

Vaibhav was still skeptical, and I wanted to see if we could solve a more complex problem.

Vaibhav 仍然存疑，而我想看看我们能否解决更复杂的问题。

So a few weeks later, the two of us spent 7 hours (3 hours on research/plans, 4 hours on implementation) and shipped 35k LOC to add cancellation and wasm support to BAML. The [cancelation PR just got merged last week](https://github.com/BoundaryML/baml/pull/2357). [The WASM one is still open](https://github.com/BoundaryML/baml/pull/2330), but has a working demo of calling the wasm-compiled rust runtime from a JS app in the browser.

于是几周后，我们两人花了 7 小时（3 小时做研究与计划，4 小时做实现），为 BAML 交付了 3.5 万行 LOC，加入取消支持和 wasm 支持。 [取消功能的 PR 上周刚被合并](https://github.com/BoundaryML/baml/pull/2357)。[WASM 那个还开着](https://github.com/BoundaryML/baml/pull/2330)，但已经有一个可运行的演示：在浏览器里从 JS 应用调用 wasm 编译的 Rust 运行时。

While the cancelation PR required a little more love to take things over the line, we got incredible progress in just a day. Vaibhav estimated that each of these PRs would have been 3-5 days of work for a senior engineer on the BAML team to complete.

虽然取消功能的 PR 需要再打磨一点才能越线，但我们只用一天就取得了惊人的进展。Vaibhav 估计，这两个 PR 若由 BAML 团队的资深工程师来做，各需要 3–5 天。

✅ So we can solve complex problems too.

✅ 所以复杂问题我们也能解决。

### This is not Magic

### 这不是魔法

Remember that part in the example where I read the research and threw it out cause it was wrong? Or me and Vaibhav sitting DEEPLY ENGAGED FOR 7 HOURS? You have to engage with your task when you're doing this or it WILL NOT WORK.

还记得例子里我读了研究、发现不对就把它扔掉的那段吗？或者我和 Vaibhav 深度投入 7 小时的那段？做这件事时你必须真正投入任务，否则它根本不会奏效。

There's a certain type of person who is always looking for the one magic prompt that will solve all their problems. It doesn't exist.

总有一类人一直在寻找那个能解决一切问题的魔法提示词。它并不存在。

Frequent Intentional Compaction via a research/plan/implement flow will make your performance **better**, but what makes it **good enough for hard problems** is that you build high-leverage human review into your pipeline.

通过研究/计划/实现的流程来做频繁的有意压缩，会让你的表现**更好**；但真正让它**足以应对难题**的，是你把高杠杆的人工评审嵌入了流水线。

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/01c7818a-9a0d-4ede-a23b-fb0c2e80f843" />

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/01c7818a-9a0d-4ede-a23b-fb0c2e80f843" />

### Eggs on Faces

### 出丑时刻

A few weeks back, [@blakesmith](https://www.linkedin.com/in/bhsmith/) and I sat down for 7 hours and [tried to remove hadoop dependencies from parquet java](https://github.com/dexhorthy/parquet-java/blob/remove-hadoop/thoughts/shared/plans/remove-hadoop-dependencies.md) - the deep dive on everything that went wrong and my theories as to why, I'll save for another post, suffice it to say that it did not go well. The tl;dr is that the research steps didn't go deep enough through the dependency tree, and assumed classes could be moved upstream without introducing deeply nested hadoop dependencies.

几周前，我和 [@blakesmith](https://www.linkedin.com/in/bhsmith/) 坐下来花了 7 小时，[试图从 parquet-java 中移除 hadoop 依赖](https://github.com/dexhorthy/parquet-java/blob/remove-hadoop/thoughts/shared/plans/remove-hadoop-dependencies.md)——关于所有出错的地方以及我对原因的推测，我留到另一篇文章再写；简单说，事情并不顺利。一句话总结：研究步骤没有沿依赖树挖得足够深，并且假设了某些类可以在不引入深度嵌套的 hadoop 依赖的情况下上移到上游。

There are big hard problems you cannot just prompt your way through in 7 hours, and we're still curiously and excitedly hacking on pushing the boundaries with friends and partners. I think the other learning here is that you probably need at least one person who is an expert in the codebase, and for this case, that was neither of us.

有些大难题不是你花 7 小时靠提示词就能硬推过去的。我们仍然充满好奇与热情地与朋友和伙伴一起探索边界。我想这里还有一条经验：你大概至少需要一位精通该代码库的人，而在这次的情况里，我们俩都不是。

### On Human Leverage

### 关于人的杠杆

If there's one thing you take away from all this, let it be this:

如果这一切只能带走一件事，那就带走这个：

A bad line of code is… a bad line of code. But a bad line of a **plan** could lead to hundreds of bad lines of code. And a bad line of **research**, a misunderstanding of how the codebase works or where certain functionality is located, could land you with thousands of bad lines of code.

一行糟糕的代码……就是一行糟糕的代码。 但**计划**里的一行糟糕内容，可能导致数百行糟糕的代码。 而**研究**里的一行糟糕内容——对代码库如何运作、某项功能位于何处的误解——可能让你产出数千行糟糕的代码。

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/dab49f61-caae-4c15-b481-ee9b8f64995f" />

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/dab49f61-caae-4c15-b481-ee9b8f64995f" />

So you want to **focus human effort and attention** on the HIGHEST LEVERAGE parts of the pipeline.

所以你要把**人的精力和注意力集中**在流水线中杠杆最高的环节。

<img width="9830" height="4520" alt="image" src="https://github.com/user-attachments/assets/cf981f70-5e61-4938-aa9a-7dcb88c9f8a4" />

<img width="9830" height="4520" alt="image" src="https://github.com/user-attachments/assets/cf981f70-5e61-4938-aa9a-7dcb88c9f8a4" />

When you review the research and the plans, you get more leverage than you do when you review the code. (By the way, one of our primary focuses @ [humanlayer](https://hlyr.dev/code) is helping teams build and leverage high-quality workflow prompts and crafting great collaboration workflows for ai-generated code and specs).

评审研究和计划时，你获得的杠杆比评审代码时更大。（顺便说一句，我们 @ [humanlayer](https://hlyr.dev/code) 的主要关注点之一，就是帮助团队构建并利用高质量的工作流提示词，为 AI 生成的代码和规格打造出色的协作工作流）。

### What is code review for?

### 代码评审是为了什么？

People have a lot of different opinions on what code review is for.

对于代码评审的目的，人们有很多不同看法。

I prefer [Blake Smith's framing in Code Review Essentials for Software Teams](https://blakesmith.me/2015/02/09/code-review-essentials-for-software-teams.html), where he says the most important part of code review is mental alignment - keeping members of the team on the page as to how the code is changing and why.

我更倾向于 [Blake Smith 在《Code Review Essentials for Software Teams》中的说法](https://blakesmith.me/2015/02/09/code-review-essentials-for-software-teams.html)：他认为代码评审最重要的部分是认知对齐——让团队成员都清楚代码正在如何变化、以及为什么变化。

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/77f4001b-175f-4da6-a6d4-e00b80489476" />

<img width="7309" height="4083" alt="image" src="https://github.com/user-attachments/assets/77f4001b-175f-4da6-a6d4-e00b80489476" />

Remember those 2k line golang PRs? I cared about them being correct and well designed, but the biggest source of internal unrest and frustration on the team was the lack of mental alignment. **I was starting to lose touch with what our product was and how it worked.**

还记得那些 2000 行的 golang PR 吗？我关心它们是否正确、设计是否良好，但团队内部最大的不安与挫败来源是认知对齐的缺失。**我开始对产品是什么、如何运作失去了感知。**

I would expect that anyone who's worked with a very productive AI coder has had this experience.

我猜任何与高产 AI 编码者共事过的人都有过这种体验。

This is actually the most important part of research/plan/implement to us. A guaranteed side effect of everyone shipping way more code is that a much larger proportion of your codebase is going to be unfamiliar to any given engineer at any point in time.

对我们来说，这其实是研究/计划/实现中最重要的一部分。 每个人都交付多得多的代码，必然带来的一个副作用是：在任意时刻，代码库中都有更大比例的部分是任何一位工程师都不熟悉的。

I won't even try to convince you that research/plan/implement is the right approach for most teams - it probably isn't. But you ABSOLUTELY need an engineering process that

我甚至不打算说服你，研究/计划/实现对大多数团队来说是正确做法——它可能并不是。但你绝对需要一个工程流程，它要

1. keeps team members on the same page
1. enables team members to quickly learn about unfamiliar parts of the codebase

1. 让团队成员保持在同一页上
1. 让团队成员能快速了解代码库中不熟悉的部分

For most teams, this is pull requests and internal docs. For us, it's now specs, plans, and research.

对大多数团队来说，这就是拉取请求和内部文档。对我们来说，现在是规格、计划和研究。

I can't read 2000 lines of golang daily. But I *can* read 200 lines of a well-written implementation plan.

我没法每天读 2000 行 golang。但我*能*读一份写得好的 200 行实现计划。

I can't go spelunking through 40+ files of daemon code for an hour+ when something is broken (okay, I can, but I don't want to). I *can* steer a research prompt to give me the speed-run on where I should be looking and why.

出问题时，我没法在 40 多个守护进程代码文件里钻探一个多小时（好吧，我能，但我不想）。我*能*用引导性的研究提示词，快速了解该看哪里、为什么。

### Recap

### 回顾

Basically we got everything we needed.

基本上，我们得到了需要的一切。

- ✅ Works in brownfield codebases
- ✅ Solves complex problems
- ✅ No slop
- ✅ Maintains mental alignment

- ✅ 在存量代码库中可用
- ✅ 能解决复杂问题
- ✅ 不产垃圾
- ✅ 保持认知对齐

(oh, and yeah, our team of three is averaging about $12k on opus per month)

（哦，还有，我们三个人的团队每月在 opus 上平均花约 1.2 万美元）

So you don't think I'm just another [hyped up mustachio'd sales guy](https://www.youtube.com/watch?v=IS_y40zY-hc&lc=UgzFldRM6LU5unLuFn54AaABAg.AMKlTmJAT5ZAMKrOOAMw3I), I'll note that this does not work perfectly for every problem (we'll be back for another round sound, parquet-java).

为了让你别以为我又是一个[满嘴胡子的炒作型销售](https://www.youtube.com/watch?v=IS_y40zY-hc&lc=UgzFldRM6LU5unLuFn54AaABAg.AMKlTmJAT5ZAMKrOOAMw3I)，我要说明：这并非对每个问题都完美奏效（我们还会再回来的，parquet-java）。

In August the whole team spent 2 weeks spinning circles on a really tricky race condition that spiraled into a rabbit hole of issues with MCP sHTTP keepalives in golang and a whole bunch of other dead ends.

8 月，整个团队花了两周在一个非常棘手的竞态条件上打转，问题一路滚进 golang 中 MCP sHTTP keepalive 的兔子洞，还有一堆其他死胡同。

But that's the exception now. In general, this works well for us. Our intern shipped 2 PRs on his first day, and 10 on his 8th day. I was genuinely skeptical that it would work for anyone else, but me and Vaibhav shipped 35k LOC of working BAML code in 7 hours. (And if you haven't met Vaibhav, he's one of the most meticulous engineers I know when it comes to code design and quality.)

但现在这已是例外。总体而言，这套做法对我们效果很好。我们的实习生第一天就交付了 2 个 PR，第 8 天交付了 10 个。我原本真心怀疑它对别人是否管用，但我和 Vaibhav 在 7 小时内交付了 3.5 万行可用的 BAML 代码。（如果你没接触过 Vaibhav：在代码设计与质量方面，他是我认识的最一丝不苟的工程师之一。）

### What's coming

### 接下来会怎样

I'm reasonably confident that coding agents will be commoditized.

我相当确信，编码智能体会被商品化。

The hard part will be the team and workflow transformation. Everything about collaboration will change in a world where AI writes 99% of our code.

难的部分将是团队与工作流的转型。在一个 AI 编写我们 99% 代码的世界里，协作的方方面面都会改变。

And I believe pretty strongly that if you don't figure this out, you're gonna get lapped by someone who did.

我相当坚定地认为，如果你没搞明白这件事，就会被搞明白的人套圈。

### okay so clearly you have something to sell me

### 好吧，显然你有东西要卖给我

We're pretty bullish on spec-first, agentic workflows, so we're building tools to make it easier. Among many things, I'm obsessed with the problem of scaling these "frequent intentional compaction" workflows collaboratively across large teams.

我们非常看好以规格为先的智能体化工作流，所以正在构建工具让它更易用。在众多事情中，我特别着迷于一个问题：如何把这种「频繁的有意压缩」工作流协作式地扩展到大型团队。

Today, we're launching CodeLayer, our new "post-IDE IDE" in private beta - think "Superhuman for claude code". If you're a fan of Superhuman and/or vim mode and you're ready to move beyond "vibe coding" and get serious about building with agents, we'd love to have you join the waitlist.

今天，我们以非公开测试的形式发布 CodeLayer，这是我们新的「后 IDE 时代的 IDE」——可以理解为「Claude Code 的 Superhuman」。如果你喜欢 Superhuman 和/或 vim 模式，并且准备超越「vibe coding」、认真用智能体来做构建，我们很希望你能加入等候名单。

**Sign up at [https://humanlayer.dev](https://humanlayer.dev)**.

**在 [https://humanlayer.dev](https://humanlayer.dev) 注册**。

## For OSS Maintainers - lets ship something together

## 致开源维护者——让我们一起交付点什么

If you are a maintainer on a complex OSS project and based in the bay area, my open offer - I will pair with you in-person in SF for 7 hours on a saturday and see if we can ship something big.

如果你是复杂开源项目的维护者，并且人在湾区，我有一个长期有效的提议：我可以在某个周六到旧金山与你线下结对 7 小时，看看我们能否交付点大东西。

I get a lot of learning about the limitations and where these techniques fall short (and, with any luck, a working merged PR that adds a ton of value that I can point to). You get to learn the workflow in the only way I've found that works well - direct 1x1 pairing.

我能学到很多关于局限性和这些技术不足之处的东西（运气好的话，还能得到一个已合并、能带来巨大价值、可供我引用的可用 PR）。你能以我发现的唯一有效方式学会这套工作流——直接一对一结对。

## For Engineering Leaders

## 致工程负责人

If you or someone you know is an engineering leader that wants to 10x their team's productivity with AI, we're forward-deploying with teams of all sizes to help drive the culture/process/tech shift needed to transition to an ai-first coding world.

如果你或你认识的人是工程负责人，希望用 AI 让团队生产力提升 10 倍，我们正在与各种规模的团队一起前置部署，帮助推动向 AI 优先的编码世界转型所需的文化、流程和技术变革。

### Thanks

### 致谢

- Thanks to all the friends and founders who've listened through early ramble-y versions of this post - Adam, Josh, Andrew, and many many more
- Thanks Sundeep for weathering this wacky storm
- Thanks Allison, Geoff, and Gerred for dragging us kicking and screaming into the future

- 感谢所有听过本文早期啰嗦版本的朋友和创始人——Adam、Josh、Andrew，以及许许多多其他人
- 感谢 Sundeep 一起扛过这场古怪的风暴
- 感谢 Allison、Geoff 和 Gerred 把我们又踢又叫地拖进未来
