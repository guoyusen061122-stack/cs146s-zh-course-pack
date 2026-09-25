# Finding Vulnerabilities in Modern Web Apps Using Claude Code and OpenAI Codex

# 使用 Claude Code 与 OpenAI Codex 挖掘现代 Web 应用中的漏洞

**TL;DR:** We evaluated how effective AI Coding Agents are at finding vulnerabilities in real code.

**TL;DR：** 我们评测了 AI 编码智能体在真实代码中挖掘漏洞的效率。

**Key take-aways**:

**要点**：

In this post we'll cover:

本文涵盖以下内容：

---

---

*This post was last edited on Sept 3, 2025, 11:15am UTC*

*本文最后编辑于 2025 年 9 月 3 日 11:15 UTC*

---

---

## Introduction

## 引言

Here at Semgrep, we live and breathe application security (AppSec). We've been productionizing AI for a long time in our products ([tech behind Assistant](https://semgrep.dev/blog/2024/the-tech-behind-semgrep-assistant/), [promptfoo for testing our AI workflows](https://semgrep.dev/blog/2024/does-your-llm-thing-work-how-we-use-promptfoo/), [using security researcher triage to evaluate auto triage performance](https://semgrep.dev/blog/2025/building-an-appsec-ai-that-security-researchers-agree-with-96-of-the-time/)), constantly researching the best combination of traditional, deterministic analysis and the contextual power of modern AI without chasing trends.

在 Semgrep，我们全身心投入应用安全（AppSec）。长期以来，我们一直在自家产品中把 AI 产品化（[Assistant 背后的技术](https://semgrep.dev/blog/2024/the-tech-behind-semgrep-assistant/)、[用 promptfoo 测试我们的 AI 工作流](https://semgrep.dev/blog/2024/does-your-llm-thing-work-how-we-use-promptfoo/)、[用安全研究员的分诊来评测自动分诊表现](https://semgrep.dev/blog/2025/building-an-appsec-ai-that-security-researchers-agree-with-96-of-the-time/)），持续研究传统确定性分析与现代 AI 上下文能力的最佳组合，而不去追逐潮流。

This research is part of that ongoing mission. We're embarking on a deep, public exploration to answer a question that's on everyone's mind: **how effective are LLMs really at finding vulnerabilities in source code?**

这项研究是那项长期使命的一部分。我们正在展开一次深入且公开的探索，以回答一个人人都在想的问题：**大语言模型在源代码中挖掘漏洞的效率究竟如何？**

## Open Research Questions about AI-based Vulnerability Hunting

## 关于基于 AI 的漏洞挖掘的开放研究问题

To guide our investigation, we broke down the broad question of "Are LLMs good at finding bugs?" into more specific, measurable sub-questions.

为了引导我们的调查，我们把「大语言模型擅长挖 bug 吗？」这个宽泛问题拆解成更具体、可度量的子问题。

For injection vulnerabilities specifically, we wanted to know:

具体到注入类漏洞，我们想知道：

## The Problem with Usual SAST Benchmarks: Lack of Realism

## 常见 SAST 基准测试的问题：缺乏真实性

Before diving into our findings, let's talk about how we measure AI performance. Much of the current research/claims relies on benchmarks that, while valuable, don't fully capture the complexity of real-world code.

在深入介绍我们的发现之前，先谈谈我们如何度量 AI 的表现。当前许多研究／说法都依赖基准测试，这些基准测试虽然有价值，却没能完整刻画真实世界代码的复杂度。

More recently academics have designed benchmarks such as [CyberGym](https://www.cybergym.io/), [Eyeballvul](https://tchauvin.com/eyeballvul-paper), or [SecVulEval](https://huggingface.co/datasets/arag0rn/SecVulEval). These show a great improvement and are closer to real-world examples but they lack the focus on modern web apps or isolate vulnerabilities from the broader application context.

更近期，学者们设计了诸如 [CyberGym](https://www.cybergym.io/)、[Eyeballvul](https://tchauvin.com/eyeballvul-paper) 或 [SecVulEval](https://huggingface.co/datasets/arag0rn/SecVulEval) 这样的基准测试。它们相比以往有巨大改进，也更接近真实世界的样本，但它们没有把重点放在现代 Web 应用上，或者把漏洞从更广泛的应用上下文中孤立出来。

While each of these approaches are useful and should be used at times, they don't necessarily reflect the reality of modern software development. Real-world applications are not clean, isolated functions. They are complex webs of dependencies, frameworks, and business logic.

这些方法各有各的用处，有时也该用，但它们未必反映现代软件开发的现实。真实世界的应用并不是干净、孤立的函数，而是依赖、框架与业务逻辑交织成的复杂网络。

Our approach is different. We tested on **11 large, Python based, actively maintained open-source projects, written in common web frameworks (Django, Flask, FastAPI)**. Our method is complementary to the previous ones, and we believe it's unique in that it a) aims to be representative of AI-driven vulnerability finding in the real world (vs. small, isolated synthetic examples), b) is not contaminated by model training data, and c) represents the types of applications most developers and companies are actually building – web applications using modern languages and frameworks.

我们的方法不同。我们在 **11 个大型、基于 Python、持续维护的开源项目上做了测试，这些项目用常见的 Web 框架写成（Django、Flask、FastAPI）**。我们的方法与前述方法互补，并且我们认为它的独特之处在于：a) 力求代表真实世界中由 AI 驱动的漏洞挖掘（而不是小型、孤立的合成样例），b) 没有被模型训练数据污染，c) 代表了大多数开发者和公司实际在构建的应用类型——使用现代语言与框架的 Web 应用。

## Scope for this Blog Post

## 本文的范围

To make this tractable, we focused on:

为了让工作可推进，我们聚焦于：

To ground our research, we selected popular and actively maintained projects. Here's a look at the scale of the applications we analyzed. **Note that we are not releasing the names of these popular open-source web apps today, since we are still in the process of responsible disclosure**, we will release the dataset once the process has concluded.

为了让研究落地，我们挑选了流行且持续维护的项目。下面是所分析应用的规模概览。**请注意，我们目前不公开这些流行开源 Web 应用的名称，因为我们仍处于负责任披露的过程中**，等流程结束后我们会发布数据集。

*Application names will be released when all vulnerabilities are disclosed and handled.*

*应用名称将在所有漏洞都被披露和处理之后公布。*

## The Experiment: AI vs. Real-World Apps Code

## 实验：AI 对比真实世界应用代码

We ran our analysis across the 11 applications and then triaged every one of the 445 findings manually, **validating most of them (especially IDOR or Auth bypass) dynamically**.

我们在 11 个应用上跑了分析，然后人工分诊了全部 445 个发现，**并对其中大多数（尤其是 IDOR 或认证绕过）做了动态验证**。

#### Anthropic Claude Code (v1.0.32, Sonnet 4)

#### Anthropic Claude Code（v1.0.32，Sonnet 4）

Using the following command:

使用以下命令：

```
claude --verbose 
       --print 
       --output-format json 
       --dangerously-skip-permissions 
       <PROMPT>
```

#### OpenAI Codex (v0.2.0, o4-mini/high reasoning)

#### OpenAI Codex（v0.2.0，o4-mini/high reasoning）

```
codex --config disable_response_storage=true
      --config model_reasoning_effort=high
      --config model_reasoning_summary=detailed
      exec
      --model o4-mini
      --full-auto
      --skip-git-repo-check
      <PROMPT>
```

### What we Found

### 我们的发现

## Same Code, Same AI, Different Bugs Every Time: AI Coding Agents' Non-Determinism Problem

## 同样的代码、同样的 AI，每次却有不同的 bug：AI 编码智能体的非确定性问题

To explore how non-determinism manifested in practice, we selected three of these applications and ran the same prompt multiple times with the same prompt, targeting the same security issue: IDOR. A pattern emerged: **the AI's findings were different every single time we ran the test**.

为了探究非确定性在实践中如何表现，我们从中挑出三个应用，用同一个提示词、针对同一类安全问题（IDOR）重复运行多次。一个规律浮现出来：**每次运行测试，AI 的发现都不一样**。

In the context of vulnerability detection this is a major issue. First, as a security engineer, ideally we want stronger guarantees that our code was scanned for important vulnerability classes than "I hope the model searched thoroughly this time."

在漏洞检测这一背景下，这是个重大问题。首先，作为安全工程师，我们理想上希望得到比「但愿这次模型搜得够仔细」更强的保证，确认代码已经针对重要的漏洞类别做过扫描。

Second, intermittently detecting vulnerabilities can cause inconsistencies and noise in your security tools or vulnerability management systems. For example, if you're using a SAST platform, ASPM, or something you've built internally, oftentimes those systems assume that when a previously detected vulnerability is no longer present, then it has been fixed. But that may not be the case with LLM-driven detection, as a single scan might miss it, and thus a "new" finding will be created when a subsequent scan re-finds the same issue, leading to duplicate JIRA tickets and developer frustration.

其次，间歇性地检出漏洞会在你的安全工具或漏洞管理系统中造成不一致与噪声。例如，如果你在使用 SAST 平台、ASPM，或者内部自建的系统，这些系统往往假定：当之前检测到的漏洞不再出现，就意味着它已被修复。但在由大语言模型驱动的检测里未必如此，因为单次扫描可能漏掉它，于是后续扫描重新发现同一问题时就会创建一条「新」发现，导致 JIRA 工单重复、开发者不胜其烦。

Here are some specific examples we observed:

以下是我们观察到的一些具体例子：

So, what's behind this? We believe the key factors are what's known as [context rot](https://research.trychroma.com/context-rot) and [compaction](https://docs.anthropic.com/en/docs/claude-code/costs#reduce-token-usage). When an AI agent is tasked with analyzing an entire codebase, it's dealing with a massive amount of information: context rot leads to the inability to retrieve accurately from its own context. To manage this, LLMs use a form of lossy compression (sometimes called compaction), which means that some of the finer reasoning details like function names, paths, etc. can get lost in the summarization process.

那么，这背后是什么原因？我们认为关键因素是所谓的[上下文腐化](https://research.trychroma.com/context-rot)与[压缩](https://docs.anthropic.com/en/docs/claude-code/costs#reduce-token-usage)。当 AI 智能体被指派分析整个代码库时，它要处理海量信息：上下文腐化会让它无法从自身上下文里准确检索。为了应对这一点，大语言模型会使用一种有损压缩（有时称为压缩），这意味着函数名、路径等更精细的推理细节可能在总结过程中丢失。

Think of it like trying to summarize a long, complex novel. You'll capture the main plot points, but you're bound to miss some of the subtleties and nuances. In the same way, the AI might lose track of a specific architectural pattern or a subtle data flow, leading it to miss a vulnerability in one run that it might catch in another. We saw a clear example of this in PY-APP-006, where one of the AI's proposed fixes was incomplete because it failed to reuse an existing base class for user authorization — a crucial piece of context that was seemingly lost in that particular run.

可以把它想象成试图概括一部又长又复杂的小说。你能抓住主要情节点，但必然会漏掉一些微妙与细微之处。同样地，AI 可能跟丢某个特定的架构模式或某条微妙的数据流，导致某次运行漏掉一个漏洞，而另一次运行却抓到了。我们在 PY-APP-006 中看到一个清晰的例子：AI 提出的某个修复并不完整，因为它没有复用现有的用户授权基类——那是一段关键的上下文，似乎在那一特定运行中丢失了。

This non-determinism has significant implications for how we approach AI native SAST. On one hand, the ability of the AI to "think" differently each time means it can explore a wider range of potential attack vectors, much like a team of human penetration testers with diverse perspectives. On the other hand, it introduces a level of uncertainty that can lead to confusion or mis-behaviors.

这种非确定性对我们如何开展 AI 原生 SAST 有重大影响。一方面，AI 每次「思考」方式不同，意味着它能探索更广泛的潜在攻击向量，很像一支视角多元的人类渗透测试团队。另一方面，它引入了不确定性，可能导致困惑或不当行为。

## How Effective is Claude Code's New `/security-review` Command?

## Claude Code 新的 `/security-review` 命令效果如何？

Anthropic released a [new command for Claude Code, called](https://www.anthropic.com/news/automate-security-reviews-with-claude-code)`/security-review`. It's designed to be run on a pull request to examine the changed files and ask questions to identify specific security issues. [You can find the prompt here](https://github.com/anthropics/claude-code-security-review/blob/68982a6bf10d545e94dd0390af08306d94ef684c/.claude/commands/security-review.md).

Anthropic 发布了[一个面向 Claude Code 的新命令](https://www.anthropic.com/news/automate-security-reviews-with-claude-code)`/security-review`。该命令设计用于在拉取请求（PR）上运行，检查变更的文件并提出问题，以识别特定的安全问题。[你可以在这里找到该提示词](https://github.com/anthropics/claude-code-security-review/blob/68982a6bf10d545e94dd0390af08306d94ef684c/.claude/commands/security-review.md)。

When running this command on the entire codebase, we found that the security issues identified were fairly limited. Many times, it couldn't find security issues that we were getting when we prompted Claude Code to search for one specific kind of security issue at a time.

我们在整个代码库上运行该命令，发现它识别出的安全问题相当有限。很多时候，我们逐类提示 Claude Code 去查找某一类特定安全问题就能发现的问题，它却找不到。

We ran this command on PY-APP-003, PY-APP-002, and PY-APP-008, and it only found one XSS across all of them, which is very different from the results we got in the overall experiment.

我们在 PY-APP-003、PY-APP-002 和 PY-APP-008 上运行了该命令，它在这三个应用中只找到一个 XSS，这与我们在整体实验中得到的结果相差很大。

## Answering Our Questions

## 回答我们的问题

Let's revisit our initial research questions based on what we've learned.

让我们基于所学到的东西，重新审视最初的研究问题。

## Dataset: Future Release

## 数据集：未来发布

We are not releasing a dataset today nor the names of the open source applications analyzed because we're in the process of responsible disclosure, reaching out to the application developers to get all the security issues fixed and validated. Once that's done, we'll be comfortable releasing the data.

我们今天不发布数据集，也不公布所分析开源应用的名称，因为我们正处于负责任披露的过程中，正在联系应用开发者，把所有安全问题修复并验证完毕。等这些做完，我们就会放心地发布数据。

## Conclusion

## 结论

LLMs are not a silver bullet that will replace human security engineers tomorrow, in fact they are pretty weak on finding high-severity injection-style vulnerabilities end to end. However, they are an incredibly powerful tool. Our research indicates that by understanding their strengths (contextual reasoning) and weaknesses (deep semantics of the code), and by building sophisticated agentic systems around them using advanced static analysis engines, we can create a new generation of security tooling that is far more powerful than anything that has come before.

大语言模型并不是明天就能取代人类安全工程师的灵丹妙药，事实上，它们在端到端挖掘高危注入类漏洞方面相当弱。然而，它们是极其强大的工具。我们的研究表明，通过理解它们的优势（上下文推理）与弱点（代码的深层语义），并借助先进的静态分析引擎围绕它们构建复杂的智能体化系统，我们可以创造出远比以往任何东西都更强大的新一代安全工具。

---

---

[1] Scripted simple prompt for Claude Code and Codex

[1] 为 Claude Code 与 Codex 编写的简单脚本化提示词
