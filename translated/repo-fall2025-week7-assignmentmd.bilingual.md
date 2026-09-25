# Week 7 – Exploring AI Code Review Using Graphite

# 第 7 周 — 使用 Graphite 探索 AI 代码评审

## Assignment Overview

## 作业概述

In this assignment, you will practice agent-driven development and AI-assisted code review on a more advanced codebase. You will implement the tasks in `week7/docs/TASKS.md`, validate your work with tests and manual review, and compare your own review notes with AI-generated code reviews.

在本次作业中，你将在更复杂的代码库上练习智能体驱动的开发与 AI 辅助代码评审。你需要实现 `week7/docs/TASKS.md` 中的任务，用测试和人工评审验证你的工作，并将自己的评审笔记与 AI 生成的代码评审进行对比。

## Get Started with Graphite

## 开始使用 Graphite

1. Sign up for Graphite: https://app.graphite.dev/signup
1. Upon sign up, you can claim your 30-day free trial.
1. After the 30 days, you can use code **CS146S** to claim free Graphite under their education program.

1. 注册 Graphite：https://app.graphite.dev/signup
1. 注册后，即可领取 30 天免费试用。
1. 30 天之后，你可以使用优惠码 **CS146S**，通过他们的教育计划免费领取 Graphite。

## What to do

## 要做什么

Implement the tasks from `week7/docs/TASKS.md` using an AI coding tool of your choice (e.g. Cursor, Copilot, Claude, etc.).

使用你自选的 AI 编码工具（例如 Cursor、Copilot、Claude 等）实现 `week7/docs/TASKS.md` 中的任务。

### For each task:

### 对每个任务：

1. Create a separate branch.
1. Implement the task with your AI tool using a 1-shot prompt.
1. Manually review the changes line-by-line. Fix issues you notice and add explanatory commit messages where helpful. You may also pair with a classmate to review each other’s code instead of reviewing your own changes.
1. Open a Pull Request (PR) for the task. Ensure your PRs include:
1. Description of the problem and your approach.
1. Summary of testing performed (include commands and results) and any added/updated tests.
1. Notable tradeoffs, limitations, or follow-ups.
1. Use Graphite Diamond to generate an AI-assisted code review on the PR.
1. Document the results of your PR in the `writeup.md`.

1. 创建一个独立分支。
1. 用你的 AI 工具以一次性提示词（1-shot prompt）实现该任务。
1. 逐行人工评审改动。修复你发现的问题，并在有帮助处补充说明性的提交信息。你也可以与同学结对，互相评审对方的代码，而不是评审自己的改动。
1. 为该任务发起一个拉取请求（PR）。确保你的 PR 包含：
1. 对问题与你的解决思路的描述。
1. 已执行的测试总结（包含命令与结果），以及新增或更新的测试。
1. 值得注意的取舍、局限或后续工作。
1. 使用 Graphite Diamond 在该 PR 上生成 AI 辅助代码评审。
1. 在 `writeup.md` 中记录你该 PR 的结果。

## Deliverables

## 交付物

In your `writeup.md`, we are looking for the follwoing:

在你的 `writeup.md` 中，我们希望看到以下内容：

- Four PRs, one per completed task, each with:
- Clear PR description
- Links to relevant commits/issues.
- Graphite Diamond AI review comments visible on the PR

- 四个 PR，每个已完成任务一个，每个 PR 都包含：
- 清晰的 PR 描述
- 指向相关提交/议题的链接。
- 在 PR 上可见的 Graphite Diamond AI 评审意见

- A brief reflection addressing the following:
- The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).
- A comparison of **your** comments vs. **Graphite’s** AI-generated comments for each PR.
- When the AI reviews were better/worse than yours (cite specific examples)
- Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.

- 一段简短的反思，涵盖以下内容：
- 你在人工评审中通常会给出的意见类型（例如正确性、性能、安全、命名、测试缺口、API 形态、UX、文档）。
- 对每个 PR，将**你的**意见与 **Graphite** 的 AI 生成意见作对比。
- AI 评审在何时比你的更好或更差（请举出具体例子）
- 你对今后信任 AI 评审的放心程度，以及何时可以依赖它们的经验法则。

## Evaluation criteria (100 points total)

## 评分标准（总分 100 分）

- 20 points per completed task
- Technical correctness and completeness of each task.
- Code quality: readability, naming, structure, error handling, and tests.
- Thoughtfulness and depth of manual review notes
- Graphite Diamond AI generated code review
- 20 points for the brief reflection
- Insightful comparison between your review and Graphite’s AI review
- Description of your personal comfort level with AI Reviews

- 每个已完成任务 20 分
- 每个任务的技术正确性与完整性。
- 代码质量：可读性、命名、结构、错误处理与测试。
- 人工评审笔记的思考深度与详尽程度
- Graphite Diamond 生成的 AI 代码评审
- 简短反思 20 分
- 对你自己评审与 Graphite AI 评审之间富有洞见的对比
- 对你在 AI 评审上的个人放心程度的描述

## Submission Instructions

## 提交说明

1. Make sure you have all changes pushed to your remote repository for grading.
1. Make sure you've added both brentju and febielin as collaborators on your assignment repository.
1. Submit via Gradescope.

1. 确保所有改动都已推送到用于评分的远程仓库。
1. 确保你已将 brentju 和 febielin 都添加为作业仓库的协作者。
1. 通过 Gradescope 提交。
