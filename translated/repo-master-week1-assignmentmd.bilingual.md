# Week 1: Trace Dissection of a Real Claude Code Session

# 第 1 周：剖析一次真实 Claude Code 会话的追踪（ trace ）

## Assignment Overview

## 作业概述

This week you will put a real Claude Code session behind a proxy, capture the actual HTTP requests it sends, and **dissect them**. You are not building anything new. You are reading someone else's production system at the level of detail where its design decisions become visible.

本周你要把一次真实的 Claude Code 会话放到代理后面，捕获它实际发出的 HTTP 请求，并**剖析这些请求**。你不需要构建任何新东西。你要做的是阅读别人的生产系统，细致到它的设计决策变得可见的程度。

### Learning Goals

### 学习目标

- **Trace** a real coding session from a production-grade coding agent and understand its call structure.
- **Identify** how prompting, tool schemas, and model responses interact during a non-trivial coding task.
- **Reflect** on which behaviors you would replicate, and which you would change, in your own custom agents.

- **追踪** 一次来自生产级编码智能体的真实编码会话，理解它的调用结构。
- **辨识** 在一项非平凡的编码任务中，提示词、工具模式与模型响应如何相互作用。
- **反思** 在你自己的自定义智能体中，哪些行为你会照搬，哪些你会改变。

## Materials

## 材料

- **[Intercepting Claude Code Requests](https://www.ai.moda/en/blog/tutorial-intercepting-claude-code-requests)**: the technique this assignment is built on. Read it first.
- **[Anthropic Messages API reference](https://docs.claude.com/en/api/messages)**: the request shape you will be reading (`system`, `tools`, `messages`).
- **[Claude Code settings reference](https://docs.claude.com/en/docs/claude-code/settings)**: how user-level (`~/.claude/settings.json`) and project-level (`.claude/settings.json`) settings work.

- **[拦截 Claude Code 请求 ](https://www.ai.moda/en/blog/tutorial-intercepting-claude-code-requests)**：本作业所依托的技术。请先读这一份。
- **[Anthropic Messages API 参考 ](https://docs.claude.com/en/api/messages)**：你将阅读的请求结构（ `system` 、 `tools` 、 `messages` ）。
- **[Claude Code 设置参考 ](https://docs.claude.com/en/docs/claude-code/settings)**：用户级（ `~/.claude/settings.json` ）与项目级（ `.claude/settings.json` ）设置如何工作。

## Setup

## 环境搭建

**Prerequisite: Claude Code**. Stanford provides access to Claude Code via your SUNet ID. If you haven't activated your account yet, [request access](https://uit.stanford.edu/service/claude), then [install and sign in](https://code.claude.com/docs/en/setup). After your account is approved and you have completed the install, confirm with `claude --version` and record that version in your writeup.

**前提条件： Claude Code 。** Stanford 通过你的 SUNet ID 提供 Claude Code 访问权限。如果你还没激活账号，请先[申请访问权限 ](https://uit.stanford.edu/service/claude)，然后[安装并登录 ](https://code.claude.com/docs/en/setup)。账号获批并完成安装后，用 `claude --version` 确认，并在你的书面说明中记录该版本号。

**1. Install mitmproxy:**

**1. 安装 mitmproxy ：**

- **macOS**: `brew install --cask mitmproxy`.
- **Windows**: run the installer from [mitmproxy.org](https://mitmproxy.org/), which puts `mitmweb` on your `PATH`.
- **Linux, or any platform**: `pip install mitmproxy`, inside the course conda env if you made one.

- **macOS**： `brew install --cask mitmproxy` 。
- **Windows**：运行来自 [mitmproxy.org](https://mitmproxy.org/) 的安装程序，它会把 `mitmweb` 放进你的 `PATH` 。
- **Linux ，或任意平台**： `pip install mitmproxy` ，如果你建了课程 conda 环境，就在其中安装。

**2. Start it as a reverse proxy:**

**2. 以反向代理方式启动它：**

```bash
mitmweb --listen-host 127.0.0.1 --listen-port 58888 \
        --web-open-browser --mode reverse:https://api.anthropic.com \
        -w session.flows
```

Traffic sent to `127.0.0.1:58888` is forwarded to the real API; the inspection UI opens at `http://localhost:8081`. Reverse mode means you point Claude Code at a plain-HTTP local address, so there is no CA certificate to install. `-w session.flows` saves every flow to disk; run the command from a directory **outside** any git repo so the capture file won't be committed by accident.

发往 `127.0.0.1:58888` 的流量会被转发到真实的 API ；检查界面在 `http://localhost:8081` 打开。反向模式意味着你把 Claude Code 指向一个纯 HTTP 的本地地址，因此不需要安装 CA 证书。 `-w session.flows` 会把每个流量保存到磁盘；请从**任何 git 仓库之外**的目录运行该命令，这样抓包文件就不会被意外提交。

**3. Point Claude Code at it**: in the repo you will use for Part I, create a **project-level** `.claude/settings.json`:

**3. 把 Claude Code 指向它**：在你要用于第一部分的仓库里，创建一个**项目级**的 `.claude/settings.json` ：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://127.0.0.1:58888",
    "ENABLE_TOOL_SEARCH": "true"
  }
}
```

> ⚠️ **Don't put this in `~/.claude/settings.json`!** Otherwise, any Claude Code session on your machine will land in your capture (and sessions won't work once `mitmweb` is stopped).

> ⚠️ **不要把它写进 `~/.claude/settings.json` ！** 否则你机器上任何 Claude Code 会话都会落进你的抓包文件（而且一旦 `mitmweb` 停止，会话就无法工作）。

**4. Verify**: start a new `claude` session, send anything, and confirm a `POST /v1/messages` flow appears in mitmweb.

**4. 验证**：启动一个新的 `claude` 会话，随便发送任何内容，确认 mitmweb 中出现一条 `POST /v1/messages` 流量。

**5. Post-Assignment**: when you're done, delete the repo's `.claude/settings.json` (or its `env` block) and stop `mitmweb`.

**5. 作业完成后**：完成后，删除该仓库的 `.claude/settings.json` （或其中的 `env` 块），并停止 `mitmweb` 。

## Part I: Capture a Session (15 pts)

## 第一部分：捕获一次会话（ 15 分）

Run **one** session under the proxy meeting all four requirements:

在代理下运行**一次**会话，同时满足以下四项要求：

1. **Multi-file**: touches at least two files.
1. **Fails at least once**: you need an error-recovery sequence. Breaking a test on purpose is the reliable way to get one.
1. **Long enough to plan**: the agent should make an explicit plan, not fire a single tool call: a task list, plan mode, or a plan file.
1. **Your own repo**: a scratch project, not this one.

1. **多文件**：至少改动两个文件。
1. **至少失败一次**：你需要一段错误恢复过程。故意弄坏一个测试是获得错误恢复最可靠的方式。
1. **长到足以做计划**：智能体应当给出明确的计划，而不是只发一次工具调用：一份任务列表、计划模式，或一个计划文件。
1. **你自己的仓库**：一个临时练手项目，不是本仓库。

**Task ideas**, if you'd rather not invent one:

**任务点子**，如果你不想自己设计：

- Delete a function that other modules import, then ask Claude to restore full functionality with the tests passing.
- Add an endpoint plus tests to a small web app, then ask it to make the suite pass on a dependency version you don't have installed.
- Rename a module and have it update every import, then run lint and tests.
- Ask for a feature that requires an unfamiliar library, so the agent has to look up the API before it can write anything.

- 删除一个被其他模块导入的函数，然后要求 Claude 在测试通过的前提下恢复完整功能。
- 给一个小型 Web 应用添加一个端点及相应测试，然后要求它在你没有安装的某个依赖版本上让测试套件通过。
- 重命名一个模块，让它更新每一处导入，然后运行静态检查与测试。
- 要求实现一个需要用到你不熟悉的库的特性，这样智能体必须先查阅 API 才能动手写任何东西。

In the mitmweb UI, select a `POST /v1/messages` flow and download the **request body** as JSON. Keep these locally. You are not submitting them, but every later part is graded on evidence drawn from them, so keep enough to support your answers.

在 mitmweb 界面中，选中一条 `POST /v1/messages` 流量，把**请求体**下载为 JSON 。把这些文件保存在本地。你不必提交它们，但后面每一部分都依据从它们中提取的证据评分，所以要保留足够多的内容来支撑你的回答。

If your mitmweb session terminates, you can work from the saved `session.flows` file: reopen it with `mitmweb -r session.flows`.

如果你的 mitmweb 会话终止了，你可以基于保存下来的 `session.flows` 文件继续工作：用 `mitmweb -r session.flows` 重新打开它。

### ⚠️ Sanitize what you quote

### ⚠️ 对你引用的内容做净化处理

Your capture contains your own source code, file paths, and credentials. Nothing from it should reach the repo except the excerpts you deliberately quote in `writeup.md`.

你的抓包文件里有你自己的源代码、文件路径和凭证。除了你在 `writeup.md` 中刻意引用的片段之外，任何内容都不应进入仓库。

- Never paste raw flows or HTTP headers, since that is where `x-api-key` / `authorization` live.
- **Request bodies can contain secrets too.** Anything the agent read (`.env`, config files, command outputs) is replayed in `messages`. Check tool results before quoting them.
- Keep `session.flows` out of every git repo.
- Redact private content in your quotes with a visible marker (`[REDACTED: internal hostname]`), not a silent deletion.
- If an excerpt can't be sanitized without destroying its meaning, re-capture on a throwaway repo.

- 绝不要粘贴原始流量或 HTTP 头，因为 `x-api-key` / `authorization` 就在那里。
- **请求体也可能包含机密信息。** 智能体读过的任何内容（ `.env` 、配置文件、命令输出）都会在 `messages` 中被重放。引用工具结果之前先检查。
- 让 `session.flows` 远离每一个 git 仓库。
- 用可见的标记（ `[REDACTED: internal hostname]` ）遮蔽引用内容中的私密信息，而不是悄悄删掉。
- 如果某个片段无法在不破坏其含义的情况下净化，就换一个用后即弃的仓库重新抓一次。

## Part II: Annotate the System Prompt (25 pts)

## 第二部分：为系统提示词写注解（ 25 分）

Break the `system` block and any messages with `role: "system"` into their sections. For each, answer: **what behavior is this buying, and what failure mode is it defending against?** An annotation, not a summary.

把 `system` 块以及任何带有 `role: "system"` 的消息拆分成各自的段落。对每一段回答：**它换来了什么行为，又在防御哪种失败模式？** 这是写注解，不是写摘要。

Cover at least:

至少覆盖：

- **Structure**: the major sections, their order, and why that order.
- **Tone and verbosity**: the specific language controlling response length and format, and why it is worth the tokens.
- **When not to act**: destructive-operation gates, scope limits, refusal conditions.
- **Environment context**: what the agent is told about the machine, repo, and session, and where that lives in the request.

- **结构**：主要段落、它们的顺序，以及为什么是这个顺序。
- **语气与篇幅**：控制响应长度与格式的具体措辞，以及为什么它值得花掉这些 token 。
- **何时不行动**：破坏性操作的关卡、范围限制、拒绝条件。
- **环境上下文**：智能体被告知了关于机器、仓库和会话的哪些信息，以及这些信息在请求中的什么位置。

Then, on `<system-reminder>` specifically: where do they appear (system block, messages, or both, citing an example), what two distinct purposes can you evidence, and why inject them mid-conversation rather than stating them once up front?

然后专门针对 `<system-reminder>` 回答：它们出现在哪里（ system 块、 messages ，还是两者都有，并举例说明），你能找到证据的两种不同用途是什么，以及为什么要在对话中途注入它们，而不是一开始就一次性说明？

## Part III: Annotate the Tool Design (25 pts)

## 第三部分：为工具设计写注解（ 25 分）

**Inventory: numbers, not prose.** How many tools were available, broken down by built-in vs. MCP-provided vs. deferred/searchable? Note any change in the tool set across requests and what triggered it. A good answer reads *"117 tools in the first request: 35 built-in, 82 from three MCP servers"*, not *"there were many tools available."*

**清点：给数字，不要写散文。** 当时有多少个工具可用，按内置、 MCP 提供、延迟提供/可检索分类统计是多少？记下工具集在各次请求之间的任何变化，以及是什么触发了变化。好的回答读起来像 *“第一次请求中有 117 个工具： 35 个内置， 82 个来自三个 MCP 服务器”*，而不是 *“当时有很多工具可用。”*

**Design analysis.** Pick **two** tools and analyze each as interface design:

**设计分析。** 挑**两个**工具，把每一个都当作接口设计来分析：

- Reproduce the relevant part of the schema.
- Why this parameter set? What is required, what is optional, what is deliberately not exposed?
- What is the description defending against? Tool descriptions in a mature agent are largely accumulated scar tissue. Find a sentence that exists only because a model kept doing the wrong thing, and name that wrong thing.
- What does the tool deliberately *not* do, and what does that imply about the surrounding system?

- 重现该模式（ schema ）的相关部分。
- 为什么是这组参数？哪些是必填，哪些是可选，哪些是被刻意不暴露的？
- 这段描述在防御什么？成熟智能体中的工具描述大多是日积月累的疤痕组织。找出一句仅仅因为模型总是做错某件事才存在的描述，并指出那件错事是什么。
- 这个工具刻意*不*做什么，这又暗示了周边系统的什么设计？

Pick two tools that differ. Two file-manipulation tools is a weak selection; a file tool paired with an orchestration tool or one with an unusual failure contract is a strong one.

挑两个彼此不同的工具。两个文件操作类工具是弱选择；一个文件工具搭配一个编排工具，或者搭配一个失败约定不寻常的工具，才是强选择。

## Part IV: Behavioral Analysis with Evidence (25 pts)

## 第四部分：基于证据的行为分析（ 25 分）

Answer each question from your own trace. Every answer must **cite its evidence** (which request, message index, tool call) and **label itself `[OBSERVED]` or `[INFERRED]`**: observed means you can point at it in your capture, inferred means you are reasoning from definitions without having watched it happen. Both are acceptable; mislabeling is not, and unlabeled answers earn no credit.

每个问题都要用你自己的追踪记录来回答。每个回答都必须**引用其证据**（哪次请求、第几条消息、哪次工具调用）并**标注 `[OBSERVED]` （已观察）或 `[INFERRED]` （已推理）**：已观察意味着你能在抓包文件中指出它，已推理意味着你是根据定义推理，而没有亲眼看到它发生。两者都可以接受；标注错误则不行，未标注的回答不得分。

- **Error recovery**: walk one failure end to end. What did the agent see, what did it try next, how many turns did recovery take? Quote verbatim.
- **Planning**: a tool, a prompt instruction, emergent behavior, or a combination? What evidence separates those?
- **Plans and task state**: how does one get created and advanced? What does the model see about task state each turn, and where does it live in the request?
- **Subagents**: when does the agent delegate? What does the subagent get told, and what comes back? (An honest `[INFERRED]` is fine if your session never triggered one.)
- **Context management**: as the session grows, what changes in the payloads? How are earlier turns represented later?

- **错误恢复**：完整走一遍一次失败的端到端过程。智能体看到了什么，它接下来尝试了什么，恢复花了多少轮？逐字引用。
- **计划**：它来自一个工具、一条提示词指令、涌现行为，还是几者的组合？什么证据能把它们区分开？
- **计划与任务状态**：计划是如何创建并推进的？模型每轮能看到关于任务状态的哪些信息，这些信息在请求中位于哪里？
- **子智能体**：智能体什么时候委派任务？子智能体被告知了什么，又返回了什么？（如果你的会话从未触发子智能体，一个诚实的 `[INFERRED]` 也可以。）
- **上下文管理**：随着会话增长，负载中有什么变化？较早的轮次在后来的请求中如何表示？

## Part V: Reflection (10 pts)

## 第五部分：反思（ 10 分）

At most one page: **two decisions you would copy** and the problem each solves; **one you would make differently**, engaging with why it might be there; and **one thing the trace changed** about how you will steer a coding agent day to day.

最多一页：**两个你会照搬的决策**以及各自解决了什么问题；**一个你会做得不同的决策**，并论述它为什么可能被那样设计；以及**追踪记录改变了你的一件事**，即你日后会如何逐日驾驭编码智能体。

## Deliverables

## 交付物

A completed **`week1/writeup.md`** with every `TODO` filled in. Your captured traces stay on your machine.

一份填写完所有 `TODO` 的 **`week1/writeup.md`**。你抓到的追踪记录留在你自己的机器上。

## Evaluation Rubric (100 pts total)

## 评分细则（总分 100 分）

| Part | Points | What earns full credit |
| --- | --- | --- |
| I. Capture & reproducibility | 15 | All four session requirements met; setup and session documented well enough to reproduce from your writeup alone |
| II. System prompt annotation | 25 | Sections tied to behavior and failure modes; `<system-reminder>` explained with cited examples |
| III. Tool inventory & design | 25 | Concrete counts with a breakdown; two genuinely different tools analyzed as interface design |
| IV. Behavioral analysis | 25 | Every answer cited and correctly labeled; error recovery quoted verbatim |
| V. Reflection | 10 | Specific, argued positions rather than restatement |

| 部分 | 分值 | 怎样拿满分 |
| --- | --- | --- |
| I. 捕获与可复现性 | 15 | 四项会话要求全部满足；环境搭建与会话记录详尽到只看你的书面说明就能复现 |
| II. 系统提示词注解 | 25 | 各段落与行为和失败模式挂钩；用有出处的例子解释 `<system-reminder>` |
| III. 工具清点与设计 | 25 | 给出具体数字与分类；分析两个确实不同的工具作为接口设计 |
| IV. 行为分析 | 25 | 每个回答都有出处且标注正确；错误恢复逐字引用 |
| V. 反思 | 10 | 给出具体、有论证的立场，而不是复述 |

Deductions for unsanitized credentials in quoted excerpts, and for claims presented as observation that your trace does not support.

引用片段中出现未净化的凭证，以及把追踪记录并不支持的断言当作观察来陈述，都会扣分。

## SUBMISSION INSTRUCTIONS

## 提交说明

1. Make sure you have all changes pushed to your remote repository for grading.
1. **Make sure you've added `mihail911`, `isaackann`, and `vdaita` as collaborators on your assignment repository.**
1. Submit via Gradescope.
1. **Don't forget to remove `ANTHROPIC_BASE_URL` from your repo's `.claude/settings.json`!**

1. 确保所有改动都已经推送到你的远程仓库以供评分。
1. **确保你已经把 `mihail911` 、 `isaackann` 和 `vdaita` 添加为作业仓库的协作者。**
1. 通过 Gradescope 提交。
1. **别忘了从你仓库的 `.claude/settings.json` 中删除 `ANTHROPIC_BASE_URL` ！**
