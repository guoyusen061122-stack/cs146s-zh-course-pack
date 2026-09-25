# Finding Vulnerabilities in Modern Web Apps Using Claude Code and OpenAI Codex

**TL;DR:** We evaluated how effective AI Coding Agents are at finding vulnerabilities in real code.

**Key take-aways**:

In this post we'll cover:

---

*This post was last edited on Sept 3, 2025, 11:15am UTC*

---

## Introduction

Here at Semgrep, we live and breathe application security (AppSec). We've been productionizing AI for a long time in our products ([tech behind Assistant](https://semgrep.dev/blog/2024/the-tech-behind-semgrep-assistant/), [promptfoo for testing our AI workflows](https://semgrep.dev/blog/2024/does-your-llm-thing-work-how-we-use-promptfoo/), [using security researcher triage to evaluate auto triage performance](https://semgrep.dev/blog/2025/building-an-appsec-ai-that-security-researchers-agree-with-96-of-the-time/)), constantly researching the best combination of traditional, deterministic analysis and the contextual power of modern AI without chasing trends.

This research is part of that ongoing mission. We're embarking on a deep, public exploration to answer a question that's on everyone's mind: **how effective are LLMs really at finding vulnerabilities in source code?**

## Open Research Questions about AI-based Vulnerability Hunting

To guide our investigation, we broke down the broad question of "Are LLMs good at finding bugs?" into more specific, measurable sub-questions.

For injection vulnerabilities specifically, we wanted to know:

## The Problem with Usual SAST Benchmarks: Lack of Realism

Before diving into our findings, let's talk about how we measure AI performance. Much of the current research/claims relies on benchmarks that, while valuable, don't fully capture the complexity of real-world code.

More recently academics have designed benchmarks such as [CyberGym](https://www.cybergym.io/), [Eyeballvul](https://tchauvin.com/eyeballvul-paper), or [SecVulEval](https://huggingface.co/datasets/arag0rn/SecVulEval). These show a great improvement and are closer to real-world examples but they lack the focus on modern web apps or isolate vulnerabilities from the broader application context.

While each of these approaches are useful and should be used at times, they don't necessarily reflect the reality of modern software development. Real-world applications are not clean, isolated functions. They are complex webs of dependencies, frameworks, and business logic.

Our approach is different. We tested on **11 large, Python based, actively maintained open-source projects, written in common web frameworks (Django, Flask, FastAPI)**. Our method is complementary to the previous ones, and we believe it's unique in that it a) aims to be representative of AI-driven vulnerability finding in the real world (vs. small, isolated synthetic examples), b) is not contaminated by model training data, and c) represents the types of applications most developers and companies are actually building – web applications using modern languages and frameworks.

## Scope for this Blog Post

To make this tractable, we focused on:

To ground our research, we selected popular and actively maintained projects. Here's a look at the scale of the applications we analyzed. **Note that we are not releasing the names of these popular open-source web apps today, since we are still in the process of responsible disclosure**, we will release the dataset once the process has concluded.

*Application names will be released when all vulnerabilities are disclosed and handled.*

## The Experiment: AI vs. Real-World Apps Code

We ran our analysis across the 11 applications and then triaged every one of the 445 findings manually, **validating most of them (especially IDOR or Auth bypass) dynamically**.

#### Anthropic Claude Code (v1.0.32, Sonnet 4)

Using the following command:

```
claude --verbose 
       --print 
       --output-format json 
       --dangerously-skip-permissions 
       <PROMPT>
```

#### OpenAI Codex (v0.2.0, o4-mini/high reasoning)

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

## Same Code, Same AI, Different Bugs Every Time: AI Coding Agents' Non-Determinism Problem

To explore how non-determinism manifested in practice, we selected three of these applications and ran the same prompt multiple times with the same prompt, targeting the same security issue: IDOR. A pattern emerged: **the AI's findings were different every single time we ran the test**.

In the context of vulnerability detection this is a major issue. First, as a security engineer, ideally we want stronger guarantees that our code was scanned for important vulnerability classes than "I hope the model searched thoroughly this time."

Second, intermittently detecting vulnerabilities can cause inconsistencies and noise in your security tools or vulnerability management systems. For example, if you're using a SAST platform, ASPM, or something you've built internally, oftentimes those systems assume that when a previously detected vulnerability is no longer present, then it has been fixed. But that may not be the case with LLM-driven detection, as a single scan might miss it, and thus a "new" finding will be created when a subsequent scan re-finds the same issue, leading to duplicate JIRA tickets and developer frustration.

Here are some specific examples we observed:

So, what's behind this? We believe the key factors are what's known as [context rot](https://research.trychroma.com/context-rot) and [compaction](https://docs.anthropic.com/en/docs/claude-code/costs#reduce-token-usage). When an AI agent is tasked with analyzing an entire codebase, it's dealing with a massive amount of information: context rot leads to the inability to retrieve accurately from its own context. To manage this, LLMs use a form of lossy compression (sometimes called compaction), which means that some of the finer reasoning details like function names, paths, etc. can get lost in the summarization process.

Think of it like trying to summarize a long, complex novel. You'll capture the main plot points, but you're bound to miss some of the subtleties and nuances. In the same way, the AI might lose track of a specific architectural pattern or a subtle data flow, leading it to miss a vulnerability in one run that it might catch in another. We saw a clear example of this in PY-APP-006, where one of the AI's proposed fixes was incomplete because it failed to reuse an existing base class for user authorization — a crucial piece of context that was seemingly lost in that particular run.

This non-determinism has significant implications for how we approach AI native SAST. On one hand, the ability of the AI to "think" differently each time means it can explore a wider range of potential attack vectors, much like a team of human penetration testers with diverse perspectives. On the other hand, it introduces a level of uncertainty that can lead to confusion or mis-behaviors.

## How Effective is Claude Code's New `/security-review` Command?

Anthropic released a [new command for Claude Code, called](https://www.anthropic.com/news/automate-security-reviews-with-claude-code)`/security-review`. It's designed to be run on a pull request to examine the changed files and ask questions to identify specific security issues. [You can find the prompt here](https://github.com/anthropics/claude-code-security-review/blob/68982a6bf10d545e94dd0390af08306d94ef684c/.claude/commands/security-review.md).

When running this command on the entire codebase, we found that the security issues identified were fairly limited. Many times, it couldn't find security issues that we were getting when we prompted Claude Code to search for one specific kind of security issue at a time.

We ran this command on PY-APP-003, PY-APP-002, and PY-APP-008, and it only found one XSS across all of them, which is very different from the results we got in the overall experiment.

## Answering Our Questions

Let's revisit our initial research questions based on what we've learned.

## Dataset: Future Release

We are not releasing a dataset today nor the names of the open source applications analyzed because we're in the process of responsible disclosure, reaching out to the application developers to get all the security issues fixed and validated. Once that's done, we'll be comfortable releasing the data.

## Conclusion

LLMs are not a silver bullet that will replace human security engineers tomorrow, in fact they are pretty weak on finding high-severity injection-style vulnerabilities end to end. However, they are an incredibly powerful tool. Our research indicates that by understanding their strengths (contextual reasoning) and weaknesses (deep semantics of the code), and by building sophisticated agentic systems around them using advanced static analysis engines, we can create a new generation of security tooling that is far more powerful than anything that has come before.

---

[1] Scripted simple prompt for Claude Code and Codex
