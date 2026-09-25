# Claude Best Practices

# Claude 最佳实践

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> ## 文档索引
> 完整的文档索引可在以下地址获取：https://code.claude.com/docs/llms.txt
> 在继续探索之前，可用这个文件发现所有可用页面。

# Best practices for Claude Code

# Claude Code 最佳实践

> Tips and patterns for getting the most out of Claude Code, from configuring your environment to scaling across parallel sessions.

> 充分发挥 Claude Code 效能的技巧与模式，从配置环境到在并行会话之间扩展。

Claude Code is an agentic coding environment. Unlike a chatbot that answers questions and waits, Claude Code can read your files, run commands, make changes, and autonomously work through problems while you watch, redirect, or step away entirely.

Claude Code 是一个智能体化的编码环境。与回答问题后静静等待的聊天机器人不同，Claude Code 可以读取你的文件、运行命令、做出修改，并在你旁观、纠正或干脆走开时自主地把问题解决下去。

This changes how you work. Instead of writing code yourself and asking Claude to review it, you describe what you want and Claude figures out how to build it. Claude explores, plans, and implements.

这会改变你的工作方式。你不必自己写代码再请 Claude 评审，而是描述你想要什么，由 Claude 想办法把它构建出来。Claude 会探索、规划并实现。

But this autonomy still comes with a learning curve. Claude works within certain constraints you need to understand.

但这种自主性依然伴随着学习曲线。Claude 会在一些你需要理解的约束内工作。

This guide covers patterns that have proven effective across Anthropic's internal teams and for engineers using Claude Code across various codebases, languages, and environments. For how the agentic loop works, see [How Claude Code works](/docs/en/how-claude-code-works).

本指南涵盖的经验模式，已在 Anthropic 内部团队以及在不同代码库、语言和环境中使用 Claude Code 的工程师身上得到验证。关于智能体化循环如何运作，见 [Claude Code 的工作原理](/docs/en/how-claude-code-works)。

---

---

Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills.

大多数最佳实践都源自同一个约束：Claude 的上下文窗口会很快被填满，而随着它被填满，表现会下降。

Claude's context window holds your entire conversation, including every message, every file Claude reads, and every command output. However, this can fill up fast. A single debugging session or codebase exploration might generate and consume tens of thousands of tokens.

Claude 的上下文窗口容纳你的整个对话，包括每一条消息、Claude 读取的每一个文件，以及每一条命令的输出。但它可能很快被填满。一次调试会话或代码库探索，就可能生成并消耗数万个 token（词元）。

This matters since LLM performance degrades as context fills. When the context window is getting full, Claude may start "forgetting" earlier instructions or making more mistakes. The context window is the most important resource to manage. To see how a session fills up in practice, [watch an interactive walkthrough](/docs/en/context-window) of what loads at startup and what each file read costs. Track context usage continuously with a [custom status line](/docs/en/statusline), and see [Reduce token usage](/docs/en/costs#reduce-token-usage) for strategies on reducing token usage.

这一点很关键，因为随着上下文被填满，大语言模型（LLM）的表现会下降。当上下文窗口快满时，Claude 可能开始「忘记」先前的指令，或者犯更多错误。上下文窗口是最需要管理的资源。想看一次会话在现实中如何被填满，可以[观看一段交互式演示](/docs/en/context-window)，了解启动时加载了什么、每次读取文件要付出多少代价。用[自定义状态栏](/docs/en/statusline)持续跟踪上下文用量，并参阅[减少 token 用量](/docs/en/costs#reduce-token-usage)了解降低 token 消耗的策略。

---

---

## Give Claude a way to verify its work

## 让 Claude 有办法验证自己的工作

<Tip> Give Claude a check it can run: tests, a build, a screenshot to compare. It's the difference between a session you watch and one you walk away from. </Tip>

<Tip> 给 Claude 一个它能运行的检查：测试、构建、用来对比的截图。这决定了你是要盯着这次会话，还是可以放手离开。 </Tip>

Claude stops when the work looks done. Without a check it can run, "looks done" is the only signal available, and you become the verification loop: every mistake waits for you to notice it. Give Claude something that produces a pass or fail, and the loop closes on its own. Claude does the work, runs the check, reads the result, and iterates until the check passes.

Claude 会在工作看起来完成时停下来。如果没有它能运行的检查，「看起来完成」就是唯一可用的信号，而你本人就成了验证回路：每一个错误都在等你发现。给 Claude 一个能产出通过或失败的东西，回路就会自行闭合。Claude 完成工作、运行检查、读取结果，并持续迭代直到检查通过。

The check is anything that returns a signal Claude can read in the conversation: a test suite, a build exit code, a linter, a script that diffs output against a fixture, or a [browser screenshot](/docs/en/chrome) compared against a design. Run [`/verify`](/docs/en/skills#run-and-verify-your-app) yourself after Claude's check passes to confirm the change against the running app.

检查可以是任何能在对话中给 Claude 返回可读信号的东西：测试套件、构建退出码、静态检查器、把输出与基准文件做比对的脚本，或者一张与设计稿对比的[浏览器截图](/docs/en/chrome)。在 Claude 的检查通过之后，你自己再运行 [`/verify`](/docs/en/skills#run-and-verify-your-app)，对着正在运行的应用确认这次改动。

| Strategy | Before | After |
| --- | --- | --- |
| **Provide verification criteria** | *"implement a function that validates email addresses"* | *"write a validateEmail function. example test cases: [user@example.com](mailto:user@example.com) is true, invalid is false, [user@.com](mailto:user@.com) is false. run the tests after implementing"* |
| **Verify UI changes visually** | *"make the dashboard look better"* | *"[paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them"* |
| **Address root causes, not symptoms** | *"the build is failing"* | *"the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error"* |

| 策略 | 修改前 | 修改后 |
| --- | --- | --- |
| **提供验证标准** | *「实现一个校验邮箱地址的函数」* | *「写一个 validateEmail 函数。示例测试用例：[user@example.com](mailto:user@example.com) 为 true，invalid 为 false，[user@.com](mailto:user@.com) 为 false。实现完成后运行测试」* |
| **以可视方式验证 UI 改动** | *「把仪表盘做得好看一些」* | *「[粘贴截图] 实现这个设计。对结果截图，并与原设计对比。列出差异并逐条修复」* |
| **解决根因，而不是症状** | *「构建失败了」* | *「构建报了如下错误：[粘贴报错]。修好它并验证构建成功。解决根因，不要压制这个错误」* |

Once the check exists, decide how hard it gates the stop:

检查就位之后，再决定它对「停止」的拦截有多强：

- **In one prompt**: ask Claude to run the check and iterate in the same message, as in the table above.
- **Across a session**: set the check as a [`/goal` condition](/docs/en/goal). A separate evaluator re-checks it after every turn and Claude keeps working until the goal resolves. If Claude stalls, Claude Code eventually stops the run with the goal still set — see [how /goal evaluation works](/docs/en/goal#how-evaluation-works).
- **As a deterministic gate**: a [Stop hook](/docs/en/hooks#stop) runs your check as a script and blocks the turn from ending until it passes. Claude Code overrides the hook and ends the turn after 8 consecutive blocks.
- **By a second opinion**: a [verification subagent](/docs/en/sub-agents) or a [dynamic workflow](/docs/en/workflows) that checks its own findings has a fresh model try to refute the result, so the agent doing the work isn't the one grading it.

- **在同一条提示词里**：让 Claude 运行检查，并在同一条消息里迭代，如上表所示。
- **贯穿整个会话**：把检查设为 [`/goal` 条件](/docs/en/goal)。一个独立的评估器会在每一轮之后重新检查它，Claude 会一直工作到目标达成。如果 Claude 停滞不前，Claude Code 最终会在目标仍然设定的情况下结束这次运行——见 [/goal 的评估机制](/docs/en/goal#how-evaluation-works)。
- **作为确定性闸门**：一个 [Stop 钩子](/docs/en/hooks#stop) 会把你的检查作为脚本运行，并在它通过之前阻止这一轮结束。连续 8 次阻止之后，Claude Code 会覆盖该钩子并结束这一轮。
- **借助第二意见**：一个[验证子智能体](/docs/en/sub-agents)或一个会检查自身发现的[动态工作流](/docs/en/workflows)，会让一个全新的模型尝试反驳结果，这样干活的智能体就不是给自己打分的那一个。

Each step trades setup for attention. The prompt version works on any task today. The `/goal` and Stop hook versions are what let an unattended run finish correctly without you.

每一步都是在用前期准备换取注意力。提示词版本今天就能适用于任何任务。`/goal` 与 Stop 钩子版本才能让无人值守的运行在没有你的情况下正确完成。

Have Claude show evidence rather than asserting success: the test output, the command it ran and what it returned, or a screenshot of the result. Reviewing evidence is faster than re-running the verification yourself, and it works for sessions you weren't watching.

让 Claude 拿出证据，而不是声称成功：测试输出、它运行过的命令及其返回结果，或者结果的截图。审阅证据比自己重跑一遍验证更快，而且对你没有旁观的会话同样有效。

---

---

## Explore first, then plan, then code

## 先探索，再规划，然后写代码

<Tip> Separate research and planning from implementation to avoid solving the wrong problem. </Tip>

<Tip> 把调研与规划和实现分开，以免解决错误的问题。 </Tip>

Letting Claude jump straight to coding can produce code that solves the wrong problem. Use [plan mode](/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode) to separate exploration from execution.

让 Claude 直接跳到编码，可能产出解决错误问题的代码。用[计划模式](/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)把探索与执行分开。

The recommended workflow has four phases:

推荐的工作流分四个阶段：

<Steps> <Step title="Explore"> Enter plan mode by pressing `Shift+Tab` until the status bar shows `⏸ plan mode on`, or start the session with `claude --permission-mode plan`. Claude reads files and answers questions without making changes.

<Steps> <Step title="Explore"> 一直按 `Shift+Tab`，直到状态栏显示 `⏸ plan mode on` 即可进入计划模式；也可以用 `claude --permission-mode plan` 启动会话。Claude 会读取文件并回答问题，但不做任何修改。

```txt
    read /src/auth and understand how we handle sessions and login.
    also look at how we manage environment variables for secrets.
```

</Step>

</Step>

<Step title="Plan"> Ask Claude to create a detailed implementation plan.

<Step title="Plan"> 请 Claude 制定一份详细的实现计划。

```txt
    I want to add Google OAuth. What files need to change?
    What's the session flow? Create a plan.
```

Press `Ctrl+G` to open the plan in your text editor for direct editing before Claude proceeds. </Step>

按 `Ctrl+G` 在文本编辑器中打开这份计划，好在 Claude 继续之前直接修改。 </Step>

<Step title="Implement"> Switch out of plan mode by approving the plan or pressing `Shift+Tab`, then let Claude code, verifying against its plan.

<Step title="Implement"> 通过批准计划或按 `Shift+Tab` 退出计划模式，然后让 Claude 编码，并对照它的计划做验证。

```txt
    implement the OAuth flow from your plan. write tests for the
    callback handler, run the test suite and fix any failures.
```

</Step>

</Step>

<Step title="Commit"> Ask Claude to commit with a descriptive message and create a PR.

<Step title="Commit"> 请 Claude 用一段描述清晰的提交信息提交，并创建一个 PR。

```txt
    commit with a descriptive message and open a PR
```

</Step> </Steps>

</Step> </Steps>

<Callout> Plan mode is useful, but also adds overhead.

<Callout> 计划模式很有用，但也会带来额外开销。

For tasks where the scope is clear and the fix is small (like fixing a typo, adding a log line, or renaming a variable) ask Claude to do it directly.

对于范围清晰、改动很小的任务（比如改一个错别字、加一行日志、重命名一个变量），直接让 Claude 去做即可。

Planning is most useful when you're uncertain about the approach, when the change modifies multiple files, or when you're unfamiliar with the code being modified. If you could describe the diff in one sentence, skip the plan. </Callout>

当你不确定实现方式、当改动涉及多个文件，或者当你不熟悉被改动的代码时，规划最有用。如果你能用一句话把差异（diff）说清楚，就跳过规划。 </Callout>

---

---

## Provide specific context in your prompts

## 在提示词中提供具体的上下文

<Tip> The more precise your instructions, the fewer corrections you'll need. </Tip>

<Tip> 你的指令越精确，需要纠正的地方就越少。 </Tip>

Claude can infer intent, but it can't read your mind. Reference specific files, mention constraints, and point to example patterns.

Claude 能领会你的意图，但读不了你的心。要引用具体文件、说明约束，并指向可参照的示例模式。

| Strategy | Before | After |
| --- | --- | --- |
| **Scope the task.** Specify which file, what scenario, and testing preferences. | *"add tests for foo.py"* | *"write a test for foo.py covering the edge case where the user is logged out. avoid mocks."* |
| **Point to sources.** Direct Claude to the source that can answer a question. | *"why does ExecutionFactory have such a weird api?"* | *"look through ExecutionFactory's git history and summarize how its api came to be"* |
| **Reference existing patterns.** Point Claude to patterns in your codebase. | *"add a calendar widget"* | *"look at how existing widgets are implemented on the home page to understand the patterns. HotDogWidget.php is a good example. follow the pattern to implement a new calendar widget that lets the user select a month and paginate forwards/backwards to pick a year. build from scratch without libraries other than the ones already used in the codebase."* |
| **Describe the symptom.** Provide the symptom, the likely location, and what "fixed" looks like. | *"fix the login bug"* | *"users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it"* |

| 策略 | 修改前 | 修改后 |
| --- | --- | --- |
| **限定任务范围。** 指明改哪个文件、什么场景，以及测试偏好。 | *「给 foo.py 加上测试」* | *「给 foo.py 写一个测试，覆盖用户已登出的边界情况。不要用 mock。」* |
| **指向信息来源。** 让 Claude 去看能回答问题的来源。 | *「ExecutionFactory 的 api 为什么这么奇怪？」* | *「翻一翻 ExecutionFactory 的 git 历史，总结它的 api 是怎么变成现在这样的」* |
| **参照已有模式。** 让 Claude 参照你代码库里的模式。 | *「加一个日历组件」* | *「看看首页上现有组件是怎么实现的，理解其中的模式。HotDogWidget.php 是个好例子。照这个模式实现一个新的日历组件，让用户能选择月份，并前后翻页选择年份。除了代码库中已经在用的库，其他都从零实现。」* |
| **描述症状。** 给出症状、可能的位置，以及「修好」是什么样子。 | *「修一下登录的缺陷」* | *「用户反馈会话超时后登录会失败。检查 src/auth/ 里的认证流程，尤其是 token 刷新。先写一个能复现该问题的失败测试，再修好它」* |

Vague prompts can be useful when you're exploring and can afford to course-correct. A prompt like `"what would you improve in this file?"` can surface things you wouldn't have thought to ask about.

当你还在探索、也承担得起随时纠偏时，模糊的提示词也可以很有用。像 `"what would you improve in this file?"` 这样的提示词，能引出你原本想不到要问的东西。

### Provide rich content

### 提供丰富的内容

<Tip> Use `@` to reference files, paste screenshots/images, or pipe data directly. </Tip>

<Tip> 用 `@` 引用文件、粘贴截图或图片，或者把数据直接传进去。 </Tip>

You can provide rich data to Claude in several ways:

你可以用几种方式给 Claude 提供丰富的数据：

- **Reference files with `@`** instead of describing where code lives. Claude reads the file before responding.
- **Paste images directly**. Copy/paste or drag and drop images into the prompt.
- **Give URLs** for documentation and API references. Use `/permissions` to allowlist frequently-used domains.
- **Pipe in data** by running `cat error.log | claude` to send file contents directly.
- **Let Claude fetch what it needs**. Tell Claude to pull context itself using Bash commands, MCP tools, or by reading files.

- **用 `@` 引用文件**，而不是描述代码在哪里。Claude 会先读文件再回答。
- **直接粘贴图片**。把图片复制粘贴或拖拽进提示词。
- **给出 URL**，用于文档与 API 参考。用 `/permissions` 把常用域名加入允许列表。
- **把数据直接传进来**，运行 `cat error.log | claude` 就能把文件内容发过去。
- **让 Claude 自己取需要的东西**。告诉 Claude 用 Bash 命令、MCP 工具或读取文件来自行拉取上下文。

---

---

## Configure your environment

## 配置你的环境

A few setup steps make Claude Code significantly more effective across all your sessions. For a full overview of extension features and when to use each one, see [Extend Claude Code](/docs/en/features-overview).

几个设置步骤就能让 Claude Code 在你所有的会话中显著更有效。关于扩展功能的完整概览以及各自适用的场景，见 [扩展 Claude Code](/docs/en/features-overview)。

### Write an effective CLAUDE.md

### 写一份有效的 CLAUDE.md

<Tip> Run `/init` to generate a starter CLAUDE.md file based on your current project structure, then refine over time. </Tip>

<Tip> 运行 `/init`，根据当前项目结构生成一份 CLAUDE.md 起始文件，然后逐步打磨。 </Tip>

CLAUDE.md is a special file that Claude reads at the start of every conversation. Include Bash commands, code style, and workflow rules. This gives Claude persistent context it can't infer from code alone.

CLAUDE.md 是一个特殊文件，Claude 会在每次对话开始时读取它。把 Bash 命令、代码风格和工作流规则写进去，能给 Claude 提供它无法仅从代码中推测出的持久上下文。

There's no required format for CLAUDE.md files, but keep it short and human-readable. For example:

CLAUDE.md 文件没有规定的格式，但要保持简短、便于人阅读。例如：

```markdown
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

Run `/context` to confirm Claude loaded the file. CLAUDE.md is loaded every session, so only include things that apply broadly. For domain knowledge or workflows that are only relevant sometimes, use [skills](/docs/en/skills) instead. Claude loads them on demand without bloating every conversation.

运行 `/context` 确认 Claude 已加载该文件。CLAUDE.md 每个会话都会加载，所以只写适用范围广的内容。对于只在某些时候相关的领域知识或工作流，改用[智能体技能](/docs/en/skills)。Claude 会按需加载它们，不会让每次对话都变得臃肿。

Keep it concise. For each line, ask: *"Would removing this cause Claude to make mistakes?"* If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!

保持简洁。对每一行都问一句：*「删掉它会让 Claude 犯错吗？」* 如果不会，就删掉。臃肿的 CLAUDE.md 会让 Claude 忽略你真正的指令！

| ✅ Include | ❌ Exclude |
| --- | --- |
| Bash commands Claude can't guess | Anything Claude can figure out by reading code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Testing instructions and preferred test runners | Detailed API documentation (link to docs instead) |
| Repository etiquette (branch naming, PR conventions) | Information that changes frequently |
| Architectural decisions specific to your project | Long explanations or tutorials |
| Developer environment quirks (required env vars) | File-by-file descriptions of the codebase |
| Common gotchas or non-obvious behaviors | Self-evident practices like "write clean code" |

| ✅ 应该写进去 | ❌ 不要写 |
| --- | --- |
| Claude 猜不到的 Bash 命令 | Claude 读代码就能弄明白的东西 |
| 与默认约定不同的代码风格规则 | Claude 已经知道的标准语言惯例 |
| 测试说明与偏好的测试运行器 | 详细的 API 文档（改为给出链接） |
| 仓库礼仪（分支命名、PR 约定） | 经常变化的信息 |
| 你项目特有的架构决策 | 长篇解释或教程 |
| 开发环境的特殊之处（必需的环境变量） | 逐文件的代码库说明 |
| 常见坑或反直觉的行为 | 像「写干净的代码」这种不言自明的做法 |

If Claude keeps doing something you don't want despite having a rule against it, the file is probably too long and the rule is getting lost. If Claude asks you questions that are answered in CLAUDE.md, the phrasing might be ambiguous. Treat CLAUDE.md like code: review it when things go wrong, prune it regularly, and test changes by observing whether Claude's behavior actually shifts. For a checked-in CLAUDE.md, run [`/doctor`](/docs/en/commands#all-commands) and Claude proposes cuts for content it can derive from the codebase.

如果明明写了规则，Claude 还是老做你不想要的事，那多半是文件太长、这条规则被淹没了。如果 Claude 问你的问题在 CLAUDE.md 里已经有答案，那可能是措辞有歧义。把 CLAUDE.md 当代码对待：出问题时评审它、定期精简，并通过观察 Claude 的行为是否真的改变来检验改动。对于已签入仓库的 CLAUDE.md，运行 [`/doctor`](/docs/en/commands#all-commands)，Claude 会针对它可以从代码库中推导出的内容提出删减建议。

If Claude keeps skipping one instruction, add emphasis such as "IMPORTANT" to that line alone. If you emphasize many lines, none of them stands out. Check CLAUDE.md into git so your team can contribute. The file compounds in value over time.

如果 Claude 老是跳过某一条指令，就单独给这一行加上诸如「IMPORTANT」的强调。如果你强调了很多行，就没有一行会突出。把 CLAUDE.md 签入 git，让团队一起贡献。这个文件的价值会随时间累积。

CLAUDE.md files can import additional files using `@path/to/import` syntax. For import rules and where CLAUDE.md files can live, see [CLAUDE.md files](/docs/en/memory#claude-md-files).

CLAUDE.md 文件可以用 `@path/to/import` 语法导入其他文件。关于导入规则以及 CLAUDE.md 可以放在哪里，见 [CLAUDE.md 文件](/docs/en/memory#claude-md-files)。

### Configure permissions

### 配置权限

<Tip> To get fewer prompts without giving up control, pre-approve the tools you trust with `/permissions` and let sandboxed commands run without asking with `/sandbox`. Switch to Manual mode when you want to approve edits and commands yourself. </Tip>

<Tip> 想在保住控制权的同时减少提示，就用 `/permissions` 预先批准你信任的工具，并用 `/sandbox` 让沙箱内的命令免询问运行。当你想自己批准编辑和命令时，切到 Manual 模式。 </Tip>

On Pro, Max, and Team plans, auto mode is the [built-in starting permission mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) for interactive terminal and VS Code sessions: a separate classifier model reviews most actions instead of you and blocks only what looks risky, such as scope escalation, unknown infrastructure, or hostile-content-driven actions.

在 Pro、Max 和 Team 套餐上，auto 模式是交互式终端与 VS Code 会话的[内置起始权限模式](/docs/en/permission-modes#eliminate-prompts-with-auto-mode)：由一个独立的分类器模型代替你评审大多数操作，只拦截看起来有风险的动作，比如扩大权限范围、未知的基础设施，或由恶意内容驱动的操作。

In Manual mode, the built-in starting permission mode on other plans, Claude Code asks before actions that might modify your system: file writes, Bash commands, MCP tools. That's safe but tedious. After the tenth approval you're clicking through rather than reviewing. Two tools cut those interruptions in Manual mode and apply in auto mode as well:

在 Manual 模式下——其他套餐的内置起始权限模式——Claude Code 会在可能修改你系统的操作之前询问：文件写入、Bash 命令、MCP 工具。这很安全，但很繁琐。到第十次批准时，你已经是在一路点确认而不是在评审。有两个工具能在 Manual 模式下减少这些打断，并且在 auto 模式同样适用：

- **Permission allowlists**: permit specific tools you know are safe, like `npm run lint` or `git commit`
- **Sandboxing**: enable OS-level isolation that restricts filesystem and network access, allowing Claude to work more freely within defined boundaries

- **权限允许列表**：放行你确知安全的特定工具，比如 `npm run lint` 或 `git commit`
- **沙箱**：启用操作系统级隔离，限制文件系统与网络访问，让 Claude 能在划定的边界内更自由地工作

Read more about [permission modes](/docs/en/permission-modes), [permission rules](/docs/en/permissions), and [sandboxing](/docs/en/sandboxing).

进一步了解[权限模式](/docs/en/permission-modes)、[权限规则](/docs/en/permissions)和[沙箱](/docs/en/sandboxing)。

### Use CLI tools

### 使用 CLI 工具

<Tip> Tell Claude Code to use CLI tools like `gh`, `aws`, `gcloud`, and `sentry-cli` when interacting with external services. </Tip>

<Tip> 告诉 Claude Code 在与外部服务交互时使用 `gh`、`aws`、`gcloud`、`sentry-cli` 这类 CLI 工具。 </Tip>

CLI tools are the most context-efficient way to interact with external services. If you use GitHub, install the `gh` CLI. Claude knows how to use it for creating issues, opening pull requests, and reading comments. Without `gh`, Claude can still use the GitHub API, but unauthenticated requests often hit rate limits.

CLI 工具是与外部服务交互时最省上下文的方式。如果你用 GitHub，就装上 `gh` CLI。Claude 知道怎么用它创建 issue、发起拉取请求和读取评论。没有 `gh` 时，Claude 仍然可以用 GitHub API，但未认证的请求常常会触到速率限制。

Claude is also effective at learning CLI tools it doesn't already know. Try prompts like `Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C.`

Claude 也很擅长学习它原本不认识的 CLI 工具。可以试试这样的提示词：`Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C.`

### Connect MCP servers

### 连接 MCP 服务器

<Tip> Run `claude mcp add` with a server name and URL or command to connect external tools like Notion, Figma, or your database. For example: `claude mcp add --transport http notion https://mcp.notion.com/mcp`. </Tip>

<Tip> 用服务器名称加 URL 或命令运行 `claude mcp add`，就能连接 Notion、Figma 或你的数据库这类外部工具。例如：`claude mcp add --transport http notion https://mcp.notion.com/mcp`。 </Tip>

With [MCP servers](/docs/en/mcp), you can ask Claude to implement features from issue trackers, query databases, analyze monitoring data, integrate designs from Figma, and automate workflows.

有了 [MCP 服务器](/docs/en/mcp)，你可以让 Claude 实现来自 issue 跟踪器的功能、查询数据库、分析监控数据、集成 Figma 的设计稿，以及自动化工作流。

### Set up hooks

### 设置钩子

<Tip> Use hooks for actions that must happen every time with zero exceptions. </Tip>

<Tip> 对必须每次发生、毫无例外的动作，就用钩子。 </Tip>

[Hooks](/docs/en/hooks-guide) run scripts automatically at specific points in Claude's workflow. Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens.

[钩子](/docs/en/hooks-guide)会在 Claude 工作流中的特定时点自动运行脚本。与 CLAUDE.md 里只是建议性的指令不同，钩子是确定性的，能保证动作发生。

Claude can write hooks for you. Try prompts like *"Write a hook that runs eslint after every file edit"* or *"Write a hook that blocks writes to the migrations folder."* Edit `.claude/settings.json` directly to configure hooks by hand, and run `/hooks` to browse what's configured.

Claude 可以替你写钩子。试试这样的提示词：*「写一个钩子，在每次文件编辑后运行 eslint」* 或 *「写一个钩子，阻止写入 migrations 文件夹。」* 直接编辑 `.claude/settings.json` 手动配置钩子，并运行 `/hooks` 浏览已配置的内容。

### Create skills

### 创建技能

<Tip> Create `SKILL.md` files in `.claude/skills/` to give Claude domain knowledge and reusable workflows. </Tip>

<Tip> 在 `.claude/skills/` 里创建 `SKILL.md` 文件，给 Claude 提供领域知识和可复用的工作流。 </Tip>

[Skills](/docs/en/skills) extend Claude's knowledge with information specific to your project, team, or domain. Claude applies them automatically when relevant, or you can invoke them directly with `/skill-name`.

[智能体技能](/docs/en/skills)用你项目、团队或领域特有的信息扩展 Claude 的知识。Claude 会在相关时自动应用它们，你也可以用 `/skill-name` 直接调用。

Create a skill by adding a directory with a `SKILL.md` to `.claude/skills/`:

在 `.claude/skills/` 下新增一个包含 `SKILL.md` 的目录，就创建了一个技能：

```markdown
---
name: api-conventions
description: REST API design conventions for our services
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
- Version APIs in the URL path (/v1/, /v2/)
```

Skills can also define repeatable workflows you invoke directly:

技能还可以定义你可以直接调用的可重复工作流：

```markdown
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

Run `/fix-issue 1234` to invoke it. Use `disable-model-invocation: true` for workflows with side effects that you want to trigger manually.

运行 `/fix-issue 1234` 即可调用它。对于带有副作用、你希望手动触发的工作流，请设置 `disable-model-invocation: true`。

### Create custom subagents

### 创建自定义子智能体

<Tip> Define specialized assistants in `.claude/agents/` that Claude can delegate to for isolated tasks. </Tip>

<Tip> 在 `.claude/agents/` 中定义专用助手，Claude 可以把彼此隔离的任务委派给它们。 </Tip>

[Subagents](/docs/en/sub-agents) run in their own context with their own set of allowed tools. They're useful for tasks that read many files or need specialized focus without cluttering your main conversation.

[子智能体](/docs/en/sub-agents) 在自己的上下文中运行，并拥有自己的一套可用工具。对于需要读取大量文件、或需要专门聚焦而又不想让主对话变得杂乱的任务，子智能体很有用。

```markdown
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

Tell Claude to use subagents explicitly: *"Use a subagent to review this code for security issues."*

明确要求 Claude 使用子智能体：*「用子智能体检查这段代码有没有安全问题。」*

### Install plugins

### 安装插件

<Tip> Run `/plugin` to browse the marketplace. Plugins add skills, tools, and integrations without configuration. </Tip>

<Tip> 运行 `/plugin` 浏览插件市场。插件可以添加技能、工具与集成，无需额外配置。 </Tip>

[Plugins](/docs/en/plugins/overview) bundle skills, hooks, subagents, and MCP servers into a single installable unit from the community and Anthropic. If you work with a typed language, install a [code intelligence plugin](/docs/en/plugins/code-intelligence) to give Claude precise symbol navigation and automatic error detection after edits.

[插件](/docs/en/plugins/overview) 把技能、钩子、子智能体与 MCP 服务器打包成一个可安装单元，来源包括社区与 Anthropic。如果你使用带类型的语言，可以安装[代码智能插件](/docs/en/plugins/code-intelligence)，让 Claude 获得精确的符号导航，并在编辑后自动检测错误。

For guidance on choosing between skills, subagents, hooks, and MCP, see [Extend Claude Code](/docs/en/features-overview#match-features-to-your-goal).

关于如何在技能、子智能体、钩子与 MCP 之间做选择，见[扩展 Claude Code](/docs/en/features-overview#match-features-to-your-goal)。

---

---

## Communicate effectively

## 有效沟通

Ask Claude the questions you'd ask another engineer, and for larger features have Claude interview you and write a spec before you start implementing.

像向另一位工程师提问那样向 Claude 提问；对于较大的功能，先让 Claude 采访你并写出规格，然后再动手实现。

### Ask codebase questions

### 询问代码库相关问题

<Tip> Ask Claude questions you'd ask a senior engineer. </Tip>

<Tip> 向 Claude 提出你会向资深工程师提出的问题。 </Tip>

When onboarding to a new codebase, use Claude Code for learning and exploration. You can ask Claude the same sorts of questions you would ask another engineer:

在熟悉新代码库时，用 Claude Code 来学习和探索。你可以向 Claude 提的问题，和向另一位工程师提的一样：

- How does logging work?
- How do I make a new API endpoint?
- What does `async move { ... }` do on line 134 of `foo.rs`?
- What edge cases does `CustomerOnboardingFlowImpl` handle?
- Why does this code call `foo()` instead of `bar()` on line 333?

- 日志是怎么工作的？
- 怎么新建一个 API 端点？
- `foo.rs` 第 134 行的 `async move { ... }` 是做什么的？
- `CustomerOnboardingFlowImpl` 处理哪些边界情况？
- 为什么这段代码在第 333 行调用 `foo()` 而不是 `bar()`？

Using Claude Code this way is an effective onboarding workflow, improving ramp-up time and reducing load on other engineers. No special prompting required: ask questions directly.

以这种方式使用 Claude Code 是一种有效的上手工作流，可以缩短上手时间，并减轻其他工程师的负担。不需要特殊的提示技巧：直接提问即可。

### Let Claude interview you

### 让 Claude 采访你

<Tip> For larger features, have Claude interview you first. Start with a minimal prompt and ask Claude to interview you using the `AskUserQuestion` tool. </Tip>

<Tip> 对于较大的功能，先让 Claude 采访你。从一个极简的提示词开始，让 Claude 用 `AskUserQuestion` 工具来采访你。 </Tip>

Claude asks about things you might not have considered yet, including technical implementation, UI/UX, edge cases, and tradeoffs. Replace `[brief description]` with your feature before sending the prompt.

Claude 会询问你尚未考虑到的方面，包括技术实现、UI/UX、边界情况与取舍。发送提示词前，先把 `[brief description]` 替换成你的功能描述。

```text
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

Once the spec is complete, start a fresh session to execute it. The new session has clean context focused entirely on implementation, and you have a written spec to reference.

规格写完后，新开一个会话来执行它。新会话拥有干净的上下文，完全聚焦于实现，而你手上有一份可随时查阅的书面规格。

The most useful specs are self-contained: they name the files and interfaces involved, state what is out of scope, and end with an end-to-end verification step that proves the feature works. Time spent making the spec precise pays off more than time spent watching the implementation.

最有用的规格是自包含的：写明涉及的文件与接口，说明哪些内容不在范围内，并以一个端到端验证步骤收尾，证明该功能确实可用。把时间花在把规格写精确上，比花在盯着实现过程上回报更高。

---

---

## Manage your session

## 管理会话

Conversations are persistent and reversible. Use this to your advantage!

对话是持久的，也是可逆的。请充分利用这一点。

### Course-correct early and often

### 尽早且经常纠偏

<Tip> Correct Claude as soon as you notice it going off track. </Tip>

<Tip> 一旦发现 Claude 偏离方向，就立刻纠正它。 </Tip>

The best results come from tight feedback loops. Though Claude occasionally solves problems perfectly on the first attempt, correcting it quickly generally produces better solutions faster.

最好的结果来自紧密的反馈回路。虽然 Claude 偶尔能一次就把问题完美解决，但快速纠正通常能更快得到更好的方案。

- **`Esc`**: stop Claude mid-action with the `Esc` key. Context is preserved, so you can redirect.
- **`Esc + Esc` or `/rewind`**: press `Esc` twice or run `/rewind` to open the rewind menu and restore previous conversation and code state, or summarize from a selected message.
- **`"Undo that"`**: have Claude revert its changes.
- **`/clear`**: reset context between unrelated tasks. Long sessions with irrelevant context can reduce performance.

- **`Esc`**：按 `Esc` 键可在 Claude 执行动作的过程中停下它。上下文会保留，因此你可以重新引导。
- **`Esc + Esc` 或 `/rewind`**：连按两次 `Esc`，或运行 `/rewind`，打开倒回菜单，恢复此前的对话与代码状态，或从选中的消息开始摘要。
- **`"Undo that"`**：让 Claude 撤销它的改动。
- **`/clear`**：在互不相关的任务之间重置上下文。带有无关上下文的长会话会降低表现。

If you've corrected Claude more than twice on the same issue in one session, the context is cluttered with failed approaches. Run `/clear` and start fresh with a more specific prompt that incorporates what you learned. A clean session with a better prompt almost always outperforms a long session with accumulated corrections.

如果在同一个会话里就同一个问题纠正 Claude 超过两次，上下文已经堆满了失败的尝试。运行 `/clear`，带上你学到的东西，用一个更具体的提示词重新开始。一个干净的会话加一个更好的提示词，几乎总能胜过一场不断纠错的漫长会话。

### Manage context aggressively

### 积极管理上下文

<Tip> Run `/clear` between unrelated tasks to reset context. </Tip>

<Tip> 在互不相关的任务之间运行 `/clear` 重置上下文。 </Tip>

Claude Code automatically compacts conversation history when you approach context limits, which preserves important code and decisions while freeing space.

当你接近上下文上限时，Claude Code 会自动压缩对话历史，在释放空间的同时保留重要的代码与决策。

During long sessions, Claude's context window can fill with irrelevant conversation, file contents, and commands. This can reduce performance and sometimes distract Claude.

在长会话中，Claude 的上下文窗口会被无关的对话、文件内容和命令填满。这会降低表现，有时还会让 Claude 分心。

- Use `/clear` frequently between tasks to reset the context window entirely
- When auto compaction triggers, Claude summarizes what matters most, including code patterns, file states, and key decisions
- For more control, run `/compact <instructions>`, like `/compact Focus on the API changes`
- To compact only part of the conversation, use `Esc + Esc` or `/rewind`, select a message checkpoint, and choose **Summarize from here** or **Summarize up to here**. The first condenses messages from that point forward while keeping earlier context intact; the second condenses earlier messages while keeping recent ones in full. See [the rewind menu's summarize options](/docs/en/checkpointing#rewind-and-summarize).
- Customize compaction behavior in CLAUDE.md with instructions like `"When compacting, always preserve the full list of modified files and any test commands"` to ensure critical context survives summarization
- For questions that don't need to stay in context, use [`/btw`](/docs/en/interactive-mode#side-questions-with-%2Fbtw). The answer never enters conversation history, so you can check a detail without growing context.

- 在任务之间频繁使用 `/clear`，把上下文窗口完全重置
- 自动压缩触发时，Claude 会总结最重要的内容，包括代码模式、文件状态与关键决策
- 想要更多控制，可以运行 `/compact <instructions>`，例如 `/compact Focus on the API changes`
- 只压缩对话的一部分时，用 `Esc + Esc` 或 `/rewind`，选择一条消息检查点，再选 **Summarize from here** 或 **Summarize up to here**。前者压缩该点之后的消息，同时保留更早的上下文；后者压缩更早的消息，同时完整保留近期内容。参见[倒回菜单的摘要选项](/docs/en/checkpointing#rewind-and-summarize)。
- 在 CLAUDE.md 中自定义压缩行为，例如写 `"When compacting, always preserve the full list of modified files and any test commands"`，确保关键上下文能挺过摘要
- 对于不需要留在上下文里的问题，使用 [`/btw`](/docs/en/interactive-mode#side-questions-with-%2Fbtw)。答案不会进入对话历史，因此你可以在不撑大上下文的情况下确认某个细节。

### Use subagents for investigation

### 用子智能体做调研

<Tip> Delegate research with `"use subagents to investigate X"`. They explore in a separate context, keeping your main conversation clean for implementation. </Tip>

<Tip> 用 `"use subagents to investigate X"` 把调研委派出去。它们在独立的上下文中探索，让你的主对话保持干净，便于实现。 </Tip>

Since context is your fundamental constraint, use subagents to keep research out of it. When Claude researches a codebase it reads lots of files, all of which consume your context. Subagents run in separate context windows and report back summaries:

既然上下文是你的根本约束，就用子智能体把调研挡在上下文之外。Claude 调研代码库时会读取大量文件，这些都会占用你的上下文。子智能体在独立的上下文窗口中运行，只把摘要汇报回来：

```text
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.
```

You can also use subagents for verification after Claude implements something. See [Add an adversarial review step](#add-an-adversarial-review-step).

你也可以在 Claude 实现完某项功能之后，用子智能体做验证。参见[增加一个对抗性评审步骤](#add-an-adversarial-review-step)。

### Rewind with checkpoints

### 用检查点倒回

<Tip> Every prompt you send that starts a turn creates a checkpoint. You can restore conversation, code, or both to any previous checkpoint. </Tip>

<Tip> 你发送的每一条开启一轮对话的提示词都会创建一个检查点。你可以把对话、代码或两者都恢复到任意一个此前的检查点。 </Tip>

Claude automatically snapshots files before each change so a checkpoint can restore them. Double-tap `Escape` or run `/rewind` to open the rewind menu. You can restore conversation only, restore code only, restore both, or summarize from a selected message. See [Checkpointing](/docs/en/checkpointing) for details.

Claude 会在每次改动前自动为文件创建快照，这样检查点就能恢复它们。连按两次 `Escape`，或运行 `/rewind` 打开倒回菜单。你可以只恢复对话、只恢复代码、两者都恢复，或从选中的消息开始摘要。详情见[检查点](/docs/en/checkpointing)。

Instead of carefully planning every move, you can tell Claude to try something risky. If it doesn't work, rewind and try a different approach. Checkpoints are saved with the conversation, so you can close your terminal, resume the session later, and still rewind.

与其仔细规划每一步，不如让 Claude 去尝试有风险的改动。如果行不通，就倒回并换一种思路。检查点与对话一起保存，所以你可以关闭终端，之后恢复会话，仍然能倒回。

<Warning> Checkpoints only track changes made through Claude's file editing tools. Changes made through Bash commands or external processes are not captured. This isn't a replacement for git. </Warning>

<Warning> 检查点只跟踪通过 Claude 的文件编辑工具做出的改动。通过 Bash 命令或外部进程做出的改动不会被记录。它不能替代 git。 </Warning>

### Resume conversations

### 恢复会话

<Tip> Name sessions with `/rename` and treat them like branches: each workstream gets its own persistent context. </Tip>

<Tip> 用 `/rename` 给会话命名，并像对待分支一样对待它们：每条工作线都有自己的持久上下文。 </Tip>

Claude Code saves conversations locally, so when a task spans multiple sittings you don't have to re-explain the context. Run [`claude --continue`](/docs/en/sessions#resume-a-session) to pick up where you left off, or `claude --resume` to choose from a list. Give sessions descriptive names like `oauth-migration` so you can find them later. See [Manage sessions](/docs/en/sessions) for the full set of resume, branch, and naming controls.

Claude Code 会在本地保存对话，因此当一项任务跨越多次坐下来工作时，你不必重新解释上下文。运行 [`claude --continue`](/docs/en/sessions#resume-a-session) 从上次中断的地方继续，或用 `claude --resume` 从列表中选择。给会话起有描述性的名字，比如 `oauth-migration`，方便以后查找。恢复、分支与命名控制的完整说明见[管理会话](/docs/en/sessions)。

---

---

## Automate and scale

## 自动化与规模化

Once you're effective with one Claude, multiply your output with parallel sessions, non-interactive mode, and fan-out patterns.

当你用一个 Claude 就能高效工作时，再用并行会话、非交互模式与扇出模式把产出放大。

### Run non-interactive mode

### 运行非交互模式

<Tip> Use `claude -p "prompt"` in CI, pre-commit hooks, or scripts. Add `--output-format stream-json --verbose` for streaming JSON output. </Tip>

<Tip> 在 CI、预提交钩子或脚本中使用 `claude -p "prompt"`。加上 `--output-format stream-json --verbose` 可获得流式 JSON 输出。 </Tip>

With `claude -p "your prompt"`, you can run Claude non-interactively, without an interactive prompt. The run still creates a resumable session unless you pass `--no-session-persistence`. [Non-interactive mode](/docs/en/headless) is how you integrate Claude into CI pipelines, pre-commit hooks, or any automated workflow. The output formats let you parse results programmatically: plain text, JSON, or streaming JSON.

借助 `claude -p "your prompt"`，你可以非交互地运行 Claude，不需要进入交互式界面。除非传入 `--no-session-persistence`，这次运行仍会创建一个可恢复的会话。[非交互模式](/docs/en/headless) 是把 Claude 接入 CI 流水线、预提交钩子或任何自动化工作流的方式。输出格式让你能以程序化方式解析结果：纯文本、JSON 或流式 JSON。

```bash
# One-off queries
claude -p "Explain what this project does"

# Structured output for scripts
claude -p "List all API endpoints" --output-format json

# Streaming for real-time processing
claude -p "Analyze this log file" --output-format stream-json --verbose
```

The first command prints plain text. The `json` format returns a single JSON object with a `result` field. The `stream-json` format prints one JSON object per line, starting with an init event.

第一条命令打印纯文本。`json` 格式返回一个带有 `result` 字段的 JSON 对象。`stream-json` 格式每行打印一个 JSON 对象，以 init 事件开头。

### Run multiple Claude sessions

### 运行多个 Claude 会话

<Tip> Run multiple Claude sessions in parallel to speed up development, run isolated experiments, or start complex workflows. </Tip>

<Tip> 并行运行多个 Claude 会话，可以加速开发、运行隔离实验，或启动复杂工作流。 </Tip>

Pick the parallel approach that fits how much coordination you want to do yourself, and add messaging when the sessions need to pass findings between them:

选择适合你愿意投入多少协调工作的并行方式，并在会话之间需要传递发现时加上消息机制：

- [Worktrees](/docs/en/worktrees): run separate CLI sessions in isolated git checkouts so edits don't collide
- [Cross-session messaging](/docs/en/cross-session-messaging): let the sessions you run yourself pass findings to each other
- [Desktop app](/docs/en/desktop#work-in-parallel-with-sessions): manage multiple local sessions visually, optionally each in its own worktree
- [Use Claude Code in the cloud](/docs/en/claude-code-on-the-web): run sessions on Anthropic-managed infrastructure by default
- [Agent view](/docs/en/agent-view): research preview. Run `claude agents` to dispatch sessions that keep running in the background and watch them from one screen
- [Agent teams](/docs/en/agent-teams): experimental and disabled by default. Automated coordination of multiple sessions with shared tasks, messaging, and a team lead

- [Worktree](/docs/en/worktrees)：在隔离的 git 检出中运行各自独立的 CLI 会话，避免改动互相冲突
- [跨会话消息](/docs/en/cross-session-messaging)：让你自己运行的会话彼此传递发现
- [桌面应用](/docs/en/desktop#work-in-parallel-with-sessions)：以可视化方式管理多个本地会话，可选让每个会话位于自己的 worktree 中
- [在云端使用 Claude Code](/docs/en/claude-code-on-the-web)：默认在 Anthropic 托管的基础设施上运行会话
- [Agent 视图](/docs/en/agent-view)：研究预览。运行 `claude agents` 派发会话，它们会在后台持续运行，你可以在一个界面上观察它们
- [Agent 团队](/docs/en/agent-teams)：实验性功能，默认禁用。对多个会话做自动化协调，共享任务、消息与团队负责人

Beyond parallelizing work, multiple sessions enable quality-focused workflows. A fresh context improves code review since Claude won't be biased toward code it just wrote.

除了并行化工作之外，多个会话还能支撑以质量为中心的工作流。全新的上下文能改善代码评审，因为 Claude 不会偏向自己刚写过的代码。

For example, use a Writer/Reviewer pattern:

例如，使用「写作者/评审者」模式：

| Session A (Writer) | Session B (Reviewer) |
| --- | --- |
| `Implement a rate limiter for our API endpoints` |  |
|  | `Review the rate limiter implementation in @src/middleware/rateLimiter.ts. Look for edge cases, race conditions, and consistency with our existing middleware patterns.` |
| `Here's the review feedback: [Session B output]. Address these issues.` |  |

| 会话 A（写作者） | 会话 B（评审者） |
| --- | --- |
| `Implement a rate limiter for our API endpoints` |  |
|  | `Review the rate limiter implementation in @src/middleware/rateLimiter.ts. Look for edge cases, race conditions, and consistency with our existing middleware patterns.` |
| `Here's the review feedback: [Session B output]. Address these issues.` |  |

You can do something similar with tests: have one Claude write tests, then another write code to pass them.

你也可以对测试做类似的事情：让一个 Claude 写测试，另一个写代码让测试通过。

### Fan out across files

### 跨文件扇出

<Tip> Loop through tasks calling `claude -p` for each. Use `--allowedTools` to scope permissions for batch operations. </Tip>

<Tip> 逐个任务循环调用 `claude -p`。用 `--allowedTools` 限定批量操作的权限范围。 </Tip>

For large migrations or analyses, you can distribute work across many parallel Claude invocations. Run [`/batch <instruction>`](/docs/en/commands#all-commands) to have Claude split the change across 5 to 30 subagents. Each subagent works in its own worktree. To drive the fan-out from your own script instead, loop over `claude -p`:

对于大规模的迁移或分析，你可以把工作分发给大量并行的 Claude 调用。运行 [`/batch <instruction>`](/docs/en/commands#all-commands)，让 Claude 把改动拆分给 5 到 30 个子智能体。每个子智能体在自己的 worktree 中工作。如果你想用自己的脚本驱动扇出，就循环调用 `claude -p`：

<Steps> <Step title="Generate a task list"> Have Claude write the list of files that need migrating to a file, so the loop in the next step can read it, with a prompt like `list all 2,000 Python files that need migrating and save the list to files.txt` </Step>

<Steps> <Step title="生成任务清单"> 让 Claude 把需要迁移的文件清单写到一个文件里，以便下一步的循环读取它，提示词类似 `list all 2,000 Python files that need migrating and save the list to files.txt` </Step>

<Step title="Write a script to loop through the list">

<Step title="写一个脚本遍历该清单">

```bash
    for file in $(cat files.txt); do
      claude -p "Migrate $file from Python 2 to Python 3. Return OK or FAIL." \
        --allowedTools "Edit,Bash(git commit *)"
    done
```

</Step>

</Step>

<Step title="Test on a few files, then run on all of them"> Refine your prompt based on what goes wrong with the first 2-3 files, then run on the full set. The `--allowedTools` flag restricts what Claude can do, which matters when you're running unattended. </Step> </Steps>

<Step title="先在几个文件上试，再对全部文件运行"> 根据前 2-3 个文件暴露的问题打磨提示词，然后对全集运行。`--allowedTools` 标志会限制 Claude 能做的事，这在无人值守运行时很重要。 </Step> </Steps>

You can also integrate Claude into existing data/processing pipelines:

你也可以把 Claude 接入现有的数据/处理流水线：

```bash
claude -p "<your prompt>" --output-format json | your_command
```

### Run autonomously with auto mode

### 用自动模式自主运行

For uninterrupted execution with background safety checks, use [auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode). A classifier model reviews commands before they run, blocking scope escalation, unknown infrastructure, and hostile-content-driven actions while letting routine work proceed without prompts.

对于无人值守的不间断执行，并带有后台安全检查，请使用[自动模式](/docs/en/permission-modes#eliminate-prompts-with-auto-mode)。分类器模型会在命令执行前进行审查，阻止权限范围升级、未知基础设施以及由恶意内容驱动的操作，同时让常规工作无需确认即可继续。

```bash
claude --permission-mode auto -p "fix all lint errors"
```

When the classifier repeatedly blocks actions in a non-interactive run with the `-p` flag, Claude Code doesn't stop the run. See [when auto mode falls back](/docs/en/permission-modes#when-auto-mode-falls-back) for what happens instead and for the thresholds.

当分类器在带 `-p` 标志的非交互式运行中反复阻止操作时，Claude Code 不会停止这次运行。替代行为与相关阈值见[自动模式失效时会发生什么](/docs/en/permission-modes#when-auto-mode-falls-back)。

### Add an adversarial review step

### 增加一个对抗性评审步骤

<Tip> Before treating a task as done, have a subagent review the diff in a fresh context and report gaps. </Tip>

<Tip> 在把一项任务当作完成之前，让一个子智能体在全新的上下文中评审差异（diff），并报出缺口。 </Tip>

The longer Claude works unattended, the more an independent check matters before you count the work as done. A reviewer running in a fresh [subagent](/docs/en/sub-agents) context sees only the diff and the criteria you give it, not the reasoning that produced the change, so it evaluates the result on its own terms.

Claude 无人值守工作的时间越长，在你认定工作完成之前，独立检查就越重要。在全新的[子智能体](/docs/en/sub-agents)上下文中运行的评审者，只能看到差异（diff）和你给它的标准，看不到产生这次改动的推理过程，因此它会独立评价结果。

For a correctness check, run the bundled [`/code-review` skill](/docs/en/commands), which reviews the current diff for bugs in a fresh subagent and returns findings to the session. To check the diff against your plan instead, write the review prompt yourself. Name the work to check, the plan to check it against, and what counts as a finding:

要做正确性检查，可以运行内置的 [`/code-review` 技能](/docs/en/commands)，它会在全新的子智能体中评审当前差异（diff）并找出缺陷，再把发现返回会话。如果你想改为对照计划检查差异（diff），就自己写评审提示词。写清楚要检查的工作、对照的计划，以及什么算作一个发现：

```text
Use a subagent to review the rate limiter diff against PLAN.md. Check that
every requirement is implemented, the listed edge cases have tests, and
nothing outside the task's scope changed. Report gaps, not style preferences.
```

Because the reviewer runs as a subagent, the implementing session receives the gaps directly and can fix them and re-review without you copying findings between windows.

因为评审者以子智能体方式运行，实现方会话会直接收到这些缺口，可以修复并重新评审，无需你在窗口之间来回复制发现。

<Callout> A reviewer prompted to find gaps will usually report some, even when the work is sound, because that is what it was asked to do. Chasing every finding leads to over-engineering: extra abstraction layers, defensive code, and tests for cases that can't happen. Tell the reviewer to flag only gaps that affect correctness or the stated requirements, and treat the rest as optional. </Callout>

<Callout> 被要求找出缺口的评审者通常会报出一些，即使工作本身是扎实的，因为这就是它的任务。追着每条发现跑会导致过度工程：多余的抽象层、防御性代码，以及为不可能发生的情况写的测试。告诉评审者只标记影响正确性或既定需求的缺口，其余当作可选项。 </Callout>

---

---

## Avoid common failure patterns

## 避免常见失败模式

These are common mistakes. Recognizing them early saves time:

这些都是常见错误。早点识别它们能省下时间：

- **The kitchen sink session.** You start with one task, then ask Claude something unrelated, then go back to the first task. Context is full of irrelevant information. > **Fix**: `/clear` between unrelated tasks.
- **Correcting over and over.** Claude does something wrong, you correct it, it's still wrong, you correct again. Context is polluted with failed approaches. > **Fix**: After two failed corrections, `/clear` and write a better initial prompt incorporating what you learned.
- **The over-specified CLAUDE.md.** If your CLAUDE.md is too long, Claude ignores half of it because important rules get lost in the noise. > **Fix**: Ruthlessly prune. If Claude already does something correctly without the instruction, delete it or convert it to a hook.
- **The trust-then-verify gap.** Claude produces a plausible-looking implementation that doesn't handle edge cases. > **Fix**: Always provide verification (tests, scripts, screenshots). If you can't verify it, don't ship it.
- **The infinite exploration.** You ask Claude to "investigate" something without scoping it. Claude reads hundreds of files, filling the context. > **Fix**: Scope investigations narrowly or use subagents so the exploration doesn't consume your main context.

- **「杂物间」会话。** 你先开始做一个任务，然后问 Claude 一件不相关的事，再回到第一个任务。上下文里塞满了无关信息。 > **修复**：在互不相关的任务之间运行 `/clear`。
- **反复纠正。** Claude 做错了，你纠正它，它还是错，你又纠正一次。上下文被失败的尝试污染了。 > **修复**：两次纠错失败之后，运行 `/clear`，把你学到的东西写进一个更好的初始提示词。
- **过度细化的 CLAUDE.md。** 如果你的 CLAUDE.md 太长，Claude 会忽略其中一半，因为重要规则淹没在噪音里。 > **修复**：毫不留情地删减。如果 Claude 不用这条指令也能做对，就删掉它，或把它改写成钩子。
- **信任之后再验证的缺口。** Claude 给出一个看起来合理、却没有处理边界情况的实现。 > **修复**：始终提供验证手段（测试、脚本、截图）。如果你无法验证，就不要交付。
- **无限探索。** 你让 Claude 去「调研」某件事，却没有限定范围。Claude 读了数百个文件，把上下文填满。 > **修复**：把调研范围收窄，或者用子智能体，让探索不占用你的主上下文。

---

---

## Develop your intuition

## 培养你的直觉

The patterns in this guide aren't set in stone. They're starting points that work well in general, but might not be optimal for every situation.

本指南里的模式并非一成不变。它们是普遍适用的起点，但未必是每种情况下的最优解。

Sometimes you *should* let context accumulate because you're deep in one complex problem and the history is valuable. Sometimes you should skip planning and let Claude figure it out because the task is exploratory. Sometimes a vague prompt is exactly right because you want to see how Claude interprets the problem before constraining it.

有时你*应该*让上下文累积，因为你正深陷一个复杂问题，历史信息很有价值。有时你该跳过规划、让 Claude 自己摸索，因为任务本身是探索性的。有时一个含糊的提示词恰恰正确，因为你想先看看 Claude 如何理解这个问题，再去约束它。

Pay attention to what works. When Claude produces great output, notice what you did: the prompt structure, the context you provided, the mode you were in. When Claude struggles, ask why. Was the context too noisy? The prompt too vague? The task too big for one pass?

关注什么方法有效。当 Claude 给出优秀产出时，注意你做了什么：提示词的结构、你提供的上下文、你当时所处的模式。当 Claude 举步维艰时，问问为什么。上下文太嘈杂？提示词太含糊？任务大到一次做不完？

Over time, you'll develop intuition that no guide can capture. You'll know when to be specific and when to be open-ended, when to plan and when to explore, when to clear context and when to let it accumulate.

随着时间推移，你会形成任何指南都无法记录的直觉。你会知道何时该具体、何时该开放，何时该规划、何时该探索，何时该清空上下文、何时该让它累积。

## Related resources

## 相关资源

- [How Claude Code works](/docs/en/how-claude-code-works): the agentic loop, tools, and context management
- [Extend Claude Code](/docs/en/features-overview): skills, hooks, MCP, subagents, and plugins
- [Common workflows](/docs/en/common-workflows): step-by-step recipes for debugging, testing, PRs, and more
- [CLAUDE.md](/docs/en/memory): store project conventions and persistent context

- [Claude Code 的工作原理 ](/docs/en/how-claude-code-works)：智能体化循环、工具与上下文管理
- [扩展 Claude Code](/docs/en/features-overview)：智能体技能、钩子、模型上下文协议（ MCP ）、子智能体与插件
- [常见工作流 ](/docs/en/common-workflows)：调试、测试、拉取请求（ PR ）等场景的分步操作指南
- [CLAUDE.md](/docs/en/memory)：存储项目约定与持久上下文
