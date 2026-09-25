```markdown .claude/skills/fix-issue/SKILL.md theme={null}
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR
```

运行 `/fix-issue 1234` 即可调用它。对于带有副作用、你希望手动触发的工作流，请设置 `disable-model-invocation: true`。

### 创建自定义子智能体

<Tip>
 在 `.claude/agents/` 中定义专用助手，Claude 可以把彼此隔离的任务委派给它们。
</Tip>

[子智能体](/docs/en/sub-agents) 在自己的上下文中运行，并拥有自己的一套可用工具。对于需要读取大量文件、或需要专门聚焦而又不想让主对话变得杂乱的任务，子智能体很有用。

```markdown .claude/agents/security-reviewer.md theme={null}
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.
```

明确要求 Claude 使用子智能体：*「用子智能体检查这段代码有没有安全问题。」*

### 安装插件

<Tip>
 运行 `/plugin` 浏览插件市场。插件可以添加技能、工具与集成，无需额外配置。
</Tip>

[插件](/docs/en/plugins/overview) 把技能、钩子、子智能体与 MCP 服务器打包成一个可安装单元，来源包括社区与 Anthropic。如果你使用带类型的语言，可以安装[代码智能插件](/docs/en/plugins/code-intelligence)，让 Claude 获得精确的符号导航，并在编辑后自动检测错误。

关于如何在技能、子智能体、钩子与 MCP 之间做选择，见[扩展 Claude Code](/docs/en/features-overview#match-features-to-your-goal)。

***

## 有效沟通

像向另一位工程师提问那样向 Claude 提问；对于较大的功能，先让 Claude 采访你并写出规格，然后再动手实现。

### 询问代码库相关问题

<Tip>
 向 Claude 提出你会向资深工程师提出的问题。
</Tip>

在熟悉新代码库时，用 Claude Code 来学习和探索。你可以向 Claude 提的问题，和向另一位工程师提的一样：

* 日志是怎么工作的？
* 怎么新建一个 API 端点？
* `foo.rs` 第 134 行的 `async move { ... }` 是做什么的？
* `CustomerOnboardingFlowImpl` 处理哪些边界情况？
* 为什么这段代码在第 333 行调用 `foo()` 而不是 `bar()`？

以这种方式使用 Claude Code 是一种有效的上手工作流，可以缩短上手时间，并减轻其他工程师的负担。不需要特殊的提示技巧：直接提问即可。

### 让 Claude 采访你

<Tip>
 对于较大的功能，先让 Claude 采访你。从一个极简的提示词开始，让 Claude 用 `AskUserQuestion` 工具来采访你。
</Tip>

Claude 会询问你尚未考虑到的方面，包括技术实现、UI/UX、边界情况与取舍。发送提示词前，先把 `[brief description]` 替换成你的功能描述。

```text wrap theme={null}
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

规格写完后，新开一个会话来执行它。新会话拥有干净的上下文，完全聚焦于实现，而你手上有一份可随时查阅的书面规格。

最有用的规格是自包含的：写明涉及的文件与接口，说明哪些内容不在范围内，并以一个端到端验证步骤收尾，证明该功能确实可用。把时间花在把规格写精确上，比花在盯着实现过程上回报更高。

***

## 管理会话

对话是持久的，也是可逆的。请充分利用这一点。

### 尽早且经常纠偏

<Tip>
 一旦发现 Claude 偏离方向，就立刻纠正它。
</Tip>

最好的结果来自紧密的反馈回路。虽然 Claude 偶尔能一次就把问题完美解决，但快速纠正通常能更快得到更好的方案。

* **`Esc`**：按 `Esc` 键可在 Claude 执行动作的过程中停下它。上下文会保留，因此你可以重新引导。
* **`Esc + Esc` 或 `/rewind`**：连按两次 `Esc`，或运行 `/rewind`，打开倒回菜单，恢复此前的对话与代码状态，或从选中的消息开始摘要。
* **`"Undo that"`**：让 Claude 撤销它的改动。
* **`/clear`**：在互不相关的任务之间重置上下文。带有无关上下文的长会话会降低表现。

如果在同一个会话里就同一个问题纠正 Claude 超过两次，上下文已经堆满了失败的尝试。运行 `/clear`，带上你学到的东西，用一个更具体的提示词重新开始。一个干净的会话加一个更好的提示词，几乎总能胜过一场不断纠错的漫长会话。

### 积极管理上下文

<Tip>
 在互不相关的任务之间运行 `/clear` 重置上下文。
</Tip>

当你接近上下文上限时，Claude Code 会自动压缩对话历史，在释放空间的同时保留重要的代码与决策。

在长会话中，Claude 的上下文窗口会被无关的对话、文件内容和命令填满。这会降低表现，有时还会让 Claude 分心。

* 在任务之间频繁使用 `/clear`，把上下文窗口完全重置
* 自动压缩触发时，Claude 会总结最重要的内容，包括代码模式、文件状态与关键决策
* 想要更多控制，可以运行 `/compact <instructions>`，例如 `/compact Focus on the API changes`
* 只压缩对话的一部分时，用 `Esc + Esc` 或 `/rewind`，选择一条消息检查点，再选 **Summarize from here** 或 **Summarize up to here**。前者压缩该点之后的消息，同时保留更早的上下文；后者压缩更早的消息，同时完整保留近期内容。参见[倒回菜单的摘要选项](/docs/en/checkpointing#rewind-and-summarize)。
* 在 CLAUDE.md 中自定义压缩行为，例如写 `"When compacting, always preserve the full list of modified files and any test commands"`，确保关键上下文能挺过摘要
* 对于不需要留在上下文里的问题，使用 [`/btw`](/docs/en/interactive-mode#side-questions-with-%2Fbtw)。答案不会进入对话历史，因此你可以在不撑大上下文的情况下确认某个细节。

### 用子智能体做调研

<Tip>
 用 `"use subagents to investigate X"` 把调研委派出去。它们在独立的上下文中探索，让你的主对话保持干净，便于实现。
</Tip>

既然上下文是你的根本约束，就用子智能体把调研挡在上下文之外。Claude 调研代码库时会读取大量文件，这些都会占用你的上下文。子智能体在独立的上下文窗口中运行，只把摘要汇报回来：

```text wrap theme={null}
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.
```

你也可以在 Claude 实现完某项功能之后，用子智能体做验证。参见[增加一个对抗性评审步骤](#add-an-adversarial-review-step)。

### 用检查点倒回

<Tip>
 你发送的每一条开启一轮对话的提示词都会创建一个检查点。你可以把对话、代码或两者都恢复到任意一个此前的检查点。
</Tip>

Claude 会在每次改动前自动为文件创建快照，这样检查点就能恢复它们。连按两次 `Escape`，或运行 `/rewind` 打开倒回菜单。你可以只恢复对话、只恢复代码、两者都恢复，或从选中的消息开始摘要。详情见[检查点](/docs/en/checkpointing)。

与其仔细规划每一步，不如让 Claude 去尝试有风险的改动。如果行不通，就倒回并换一种思路。检查点与对话一起保存，所以你可以关闭终端，之后恢复会话，仍然能倒回。

<Warning>
 检查点只跟踪通过 Claude 的文件编辑工具做出的改动。通过 Bash 命令或外部进程做出的改动不会被记录。它不能替代 git。
</Warning>

### 恢复会话

<Tip>
 用 `/rename` 给会话命名，并像对待分支一样对待它们：每条工作线都有自己的持久上下文。
</Tip>

Claude Code 会在本地保存对话，因此当一项任务跨越多次坐下来工作时，你不必重新解释上下文。运行 [`claude --continue`](/docs/en/sessions#resume-a-session) 从上次中断的地方继续，或用 `claude --resume` 从列表中选择。给会话起有描述性的名字，比如 `oauth-migration`，方便以后查找。恢复、分支与命名控制的完整说明见[管理会话](/docs/en/sessions)。

***

## 自动化与规模化

当你用一个 Claude 就能高效工作时，再用并行会话、非交互模式与扇出模式把产出放大。

### 运行非交互模式

<Tip>
 在 CI、预提交钩子或脚本中使用 `claude -p "prompt"`。加上 `--output-format stream-json --verbose` 可获得流式 JSON 输出。
</Tip>

借助 `claude -p "your prompt"`，你可以非交互地运行 Claude，不需要进入交互式界面。除非传入 `--no-session-persistence`，这次运行仍会创建一个可恢复的会话。[非交互模式](/docs/en/headless) 是把 Claude 接入 CI 流水线、预提交钩子或任何自动化工作流的方式。输出格式让你能以程序化方式解析结果：纯文本、JSON 或流式 JSON。

```bash theme={null}

# One-off queries

claude -p "Explain what this project does"

# Structured output for scripts

claude -p "List all API endpoints" --output-format json

# Streaming for real-time processing

claude -p "Analyze this log file" --output-format stream-json --verbose
```

第一条命令打印纯文本。`json` 格式返回一个带有 `result` 字段的 JSON 对象。`stream-json` 格式每行打印一个 JSON 对象，以 init 事件开头。

### 运行多个 Claude 会话

<Tip>
 并行运行多个 Claude 会话，可以加速开发、运行隔离实验，或启动复杂工作流。
</Tip>

选择适合你愿意投入多少协调工作的并行方式，并在会话之间需要传递发现时加上消息机制：

* [Worktree](/docs/en/worktrees)：在隔离的 git 检出中运行各自独立的 CLI 会话，避免改动互相冲突
* [跨会话消息](/docs/en/cross-session-messaging)：让你自己运行的会话彼此传递发现
* [桌面应用](/docs/en/desktop#work-in-parallel-with-sessions)：以可视化方式管理多个本地会话，可选让每个会话位于自己的 worktree 中
* [在云端使用 Claude Code](/docs/en/claude-code-on-the-web)：默认在 Anthropic 托管的基础设施上运行会话
* [Agent 视图](/docs/en/agent-view)：研究预览。运行 `claude agents` 派发会话，它们会在后台持续运行，你可以在一个界面上观察它们
* [Agent 团队](/docs/en/agent-teams)：实验性功能，默认禁用。对多个会话做自动化协调，共享任务、消息与团队负责人

除了并行化工作之外，多个会话还能支撑以质量为中心的工作流。全新的上下文能改善代码评审，因为 Claude 不会偏向自己刚写过的代码。

例如，使用「写作者/评审者」模式：

| 会话 A（写作者） | 会话 B（评审者） |
| --- | --- |
| `Implement a rate limiter for our API endpoints` | |
| | `Review the rate limiter implementation in @src/middleware/rateLimiter.ts. Look for edge cases, race conditions, and consistency with our existing middleware patterns.` |
| `Here's the review feedback: [Session B output]. Address these issues.` | |

你也可以对测试做类似的事情：让一个 Claude 写测试，另一个写代码让测试通过。

### 跨文件扇出

<Tip>
 逐个任务循环调用 `claude -p`。用 `--allowedTools` 限定批量操作的权限范围。
</Tip>

对于大规模的迁移或分析，你可以把工作分发给大量并行的 Claude 调用。运行 [`/batch <instruction>`](/docs/en/commands#all-commands)，让 Claude 把改动拆分给 5 到 30 个子智能体。每个子智能体在自己的 worktree 中工作。如果你想用自己的脚本驱动扇出，就循环调用 `claude -p`：

<Steps>
 <Step title="生成任务清单">
 让 Claude 把需要迁移的文件清单写到一个文件里，以便下一步的循环读取它，提示词类似 `list all 2,000 Python files that need migrating and save the list to files.txt`
 </Step>

 <Step title="写一个脚本遍历该清单">
    ```bash theme={null}
    for file in $(cat files.txt); do
      claude -p "Migrate $file from Python 2 to Python 3. Return OK or FAIL." \
        --allowedTools "Edit,Bash(git commit *)"
    done
    ```
 </Step>

 <Step title="先在几个文件上试，再对全部文件运行">
 根据前 2-3 个文件暴露的问题打磨提示词，然后对全集运行。`--allowedTools` 标志会限制 Claude 能做的事，这在无人值守运行时很重要。
 </Step>
</Steps>

你也可以把 Claude 接入现有的数据/处理流水线：

```bash theme={null}
claude -p "<your prompt>" --output-format json | your_command
```

### 用自动模式自主运行

对于无人值守的不间断执行，并带有后台安全检查，请使用[自动模式](/docs/en/permission-modes#eliminate-prompts-with-auto-mode)。分类器模型会在命令执行前进行审查，阻止权限范围升级、未知基础设施以及由恶意内容驱动的操作，同时让常规工作无需确认即可继续。

```bash theme={null}
claude --permission-mode auto -p "fix all lint errors"
```

当分类器在带 `-p` 标志的非交互式运行中反复阻止操作时，Claude Code 不会停止这次运行。替代行为与相关阈值见[自动模式失效时会发生什么](/docs/en/permission-modes#when-auto-mode-falls-back)。

### 增加一个对抗性评审步骤

<Tip>
 在把一项任务当作完成之前，让一个子智能体在全新的上下文中评审差异（diff），并报出缺口。
</Tip>

Claude 无人值守工作的时间越长，在你认定工作完成之前，独立检查就越重要。在全新的[子智能体](/docs/en/sub-agents)上下文中运行的评审者，只能看到差异（diff）和你给它的标准，看不到产生这次改动的推理过程，因此它会独立评价结果。

要做正确性检查，可以运行内置的 [`/code-review` 技能](/docs/en/commands)，它会在全新的子智能体中评审当前差异（diff）并找出缺陷，再把发现返回会话。如果你想改为对照计划检查差异（diff），就自己写评审提示词。写清楚要检查的工作、对照的计划，以及什么算作一个发现：

```text wrap theme={null}
Use a subagent to review the rate limiter diff against PLAN.md. Check that
every requirement is implemented, the listed edge cases have tests, and
nothing outside the task's scope changed. Report gaps, not style preferences.
```

因为评审者以子智能体方式运行，实现方会话会直接收到这些缺口，可以修复并重新评审，无需你在窗口之间来回复制发现。

<Callout>
 被要求找出缺口的评审者通常会报出一些，即使工作本身是扎实的，因为这就是它的任务。追着每条发现跑会导致过度工程：多余的抽象层、防御性代码，以及为不可能发生的情况写的测试。告诉评审者只标记影响正确性或既定需求的缺口，其余当作可选项。
</Callout>

***

## 避免常见失败模式

这些都是常见错误。早点识别它们能省下时间：

* **「杂物间」会话。** 你先开始做一个任务，然后问 Claude 一件不相关的事，再回到第一个任务。上下文里塞满了无关信息。
  > **修复**：在互不相关的任务之间运行 `/clear`。
* **反复纠正。** Claude 做错了，你纠正它，它还是错，你又纠正一次。上下文被失败的尝试污染了。
  > **修复**：两次纠错失败之后，运行 `/clear`，把你学到的东西写进一个更好的初始提示词。
* **过度细化的 CLAUDE.md。** 如果你的 CLAUDE.md 太长，Claude 会忽略其中一半，因为重要规则淹没在噪音里。
  > **修复**：毫不留情地删减。如果 Claude 不用这条指令也能做对，就删掉它，或把它改写成钩子。
* **信任之后再验证的缺口。** Claude 给出一个看起来合理、却没有处理边界情况的实现。
  > **修复**：始终提供验证手段（测试、脚本、截图）。如果你无法验证，就不要交付。
* **无限探索。** 你让 Claude 去「调研」某件事，却没有限定范围。Claude 读了数百个文件，把上下文填满。
  > **修复**：把调研范围收窄，或者用子智能体，让探索不占用你的主上下文。

***

## 培养你的直觉

本指南里的模式并非一成不变。它们是普遍适用的起点，但未必是每种情况下的最优解。

有时你*应该*让上下文累积，因为你正深陷一个复杂问题，历史信息很有价值。有时你该跳过规划、让 Claude 自己摸索，因为任务本身是探索性的。有时一个含糊的提示词恰恰正确，因为你想先看看 Claude 如何理解这个问题，再去约束它。

关注什么方法有效。当 Claude 给出优秀产出时，注意你做了什么：提示词的结构、你提供的上下文、你当时所处的模式。当 Claude 举步维艰时，问问为什么。上下文太嘈杂？提示词太含糊？任务大到一次做不完？

随着时间推移，你会形成任何指南都无法记录的直觉。你会知道何时该具体、何时该开放，何时该规划、何时该探索，何时该清空上下文、何时该让它累积。

## 相关资源
