# Claude 最佳实践

> ## 文档索引
> 完整的文档索引可在以下地址获取：https://code.claude.com/docs/llms.txt
> 在继续探索之前，可用这个文件发现所有可用页面。

# Claude Code 最佳实践

> 充分发挥 Claude Code 效能的技巧与模式，从配置环境到在并行会话之间扩展。

Claude Code 是一个智能体化的编码环境。与回答问题后静静等待的聊天机器人不同，Claude Code 可以读取你的文件、运行命令、做出修改，并在你旁观、纠正或干脆走开时自主地把问题解决下去。

这会改变你的工作方式。你不必自己写代码再请 Claude 评审，而是描述你想要什么，由 Claude 想办法把它构建出来。Claude 会探索、规划并实现。

但这种自主性依然伴随着学习曲线。Claude 会在一些你需要理解的约束内工作。

本指南涵盖的经验模式，已在 Anthropic 内部团队以及在不同代码库、语言和环境中使用 Claude Code 的工程师身上得到验证。关于智能体化循环如何运作，见 [Claude Code 的工作原理](/docs/en/how-claude-code-works)。

***

大多数最佳实践都源自同一个约束：Claude 的上下文窗口会很快被填满，而随着它被填满，表现会下降。

Claude 的上下文窗口容纳你的整个对话，包括每一条消息、Claude 读取的每一个文件，以及每一条命令的输出。但它可能很快被填满。一次调试会话或代码库探索，就可能生成并消耗数万个 token（词元）。

这一点很关键，因为随着上下文被填满，大语言模型（LLM）的表现会下降。当上下文窗口快满时，Claude 可能开始「忘记」先前的指令，或者犯更多错误。上下文窗口是最需要管理的资源。想看一次会话在现实中如何被填满，可以[观看一段交互式演示](/docs/en/context-window)，了解启动时加载了什么、每次读取文件要付出多少代价。用[自定义状态栏](/docs/en/statusline)持续跟踪上下文用量，并参阅[减少 token 用量](/docs/en/costs#reduce-token-usage)了解降低 token 消耗的策略。

***

## 让 Claude 有办法验证自己的工作

<Tip>
  给 Claude 一个它能运行的检查：测试、构建、用来对比的截图。这决定了你是要盯着这次会话，还是可以放手离开。
</Tip>

Claude 会在工作看起来完成时停下来。如果没有它能运行的检查，「看起来完成」就是唯一可用的信号，而你本人就成了验证回路：每一个错误都在等你发现。给 Claude 一个能产出通过或失败的东西，回路就会自行闭合。Claude 完成工作、运行检查、读取结果，并持续迭代直到检查通过。

检查可以是任何能在对话中给 Claude 返回可读信号的东西：测试套件、构建退出码、静态检查器、把输出与基准文件做比对的脚本，或者一张与设计稿对比的[浏览器截图](/docs/en/chrome)。在 Claude 的检查通过之后，你自己再运行 [`/verify`](/docs/en/skills#run-and-verify-your-app)，对着正在运行的应用确认这次改动。

| 策略 | 修改前 | 修改后 |
| ------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **提供验证标准** | *「实现一个校验邮箱地址的函数」* | *「写一个 validateEmail 函数。示例测试用例：[user@example.com](mailto:user@example.com) 为 true，invalid 为 false，[user@.com](mailto:user@.com) 为 false。实现完成后运行测试」* |
| **以可视方式验证 UI 改动** | *「把仪表盘做得好看一些」* | *「\[粘贴截图] 实现这个设计。对结果截图，并与原设计对比。列出差异并逐条修复」* |
| **解决根因，而不是症状** | *「构建失败了」* | *「构建报了如下错误：\[粘贴报错]。修好它并验证构建成功。解决根因，不要压制这个错误」* |

检查就位之后，再决定它对「停止」的拦截有多强：

* **在同一条提示词里**：让 Claude 运行检查，并在同一条消息里迭代，如上表所示。
* **贯穿整个会话**：把检查设为 [`/goal` 条件](/docs/en/goal)。一个独立的评估器会在每一轮之后重新检查它，Claude 会一直工作到目标达成。如果 Claude 停滞不前，Claude Code 最终会在目标仍然设定的情况下结束这次运行——见 [/goal 的评估机制](/docs/en/goal#how-evaluation-works)。
* **作为确定性闸门**：一个 [Stop 钩子](/docs/en/hooks#stop) 会把你的检查作为脚本运行，并在它通过之前阻止这一轮结束。连续 8 次阻止之后，Claude Code 会覆盖该钩子并结束这一轮。
* **借助第二意见**：一个[验证子智能体](/docs/en/sub-agents)或一个会检查自身发现的[动态工作流](/docs/en/workflows)，会让一个全新的模型尝试反驳结果，这样干活的智能体就不是给自己打分的那一个。

每一步都是在用前期准备换取注意力。提示词版本今天就能适用于任何任务。`/goal` 与 Stop 钩子版本才能让无人值守的运行在没有你的情况下正确完成。

让 Claude 拿出证据，而不是声称成功：测试输出、它运行过的命令及其返回结果，或者结果的截图。审阅证据比自己重跑一遍验证更快，而且对你没有旁观的会话同样有效。

***

## 先探索，再规划，然后写代码

<Tip>
  把调研与规划和实现分开，以免解决错误的问题。
</Tip>

让 Claude 直接跳到编码，可能产出解决错误问题的代码。用[计划模式](/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)把探索与执行分开。

推荐的工作流分四个阶段：

<Steps>
  <Step title="Explore">
    一直按 `Shift+Tab`，直到状态栏显示 `⏸ plan mode on` 即可进入计划模式；也可以用 `claude --permission-mode plan` 启动会话。Claude 会读取文件并回答问题，但不做任何修改。

    ```txt title="claude (plan mode)" wrap theme={null}
    read /src/auth and understand how we handle sessions and login.
    also look at how we manage environment variables for secrets.
    ```
  </Step>

  <Step title="Plan">
    请 Claude 制定一份详细的实现计划。

    ```txt title="claude (plan mode)" wrap theme={null}
    I want to add Google OAuth. What files need to change?
    What's the session flow? Create a plan.
    ```

    按 `Ctrl+G` 在文本编辑器中打开这份计划，好在 Claude 继续之前直接修改。
  </Step>

  <Step title="Implement">
    通过批准计划或按 `Shift+Tab` 退出计划模式，然后让 Claude 编码，并对照它的计划做验证。

    ```txt title="claude" wrap theme={null}
    implement the OAuth flow from your plan. write tests for the
    callback handler, run the test suite and fix any failures.
    ```
  </Step>

  <Step title="Commit">
    请 Claude 用一段描述清晰的提交信息提交，并创建一个 PR。

    ```txt title="claude" wrap theme={null}
    commit with a descriptive message and open a PR
    ```
  </Step>
</Steps>

<Callout>
  计划模式很有用，但也会带来额外开销。

  对于范围清晰、改动很小的任务（比如改一个错别字、加一行日志、重命名一个变量），直接让 Claude 去做即可。

  当你不确定实现方式、当改动涉及多个文件，或者当你不熟悉被改动的代码时，规划最有用。如果你能用一句话把差异（diff）说清楚，就跳过规划。
</Callout>

***

## 在提示词中提供具体的上下文

<Tip>
  你的指令越精确，需要纠正的地方就越少。
</Tip>

Claude 能领会你的意图，但读不了你的心。要引用具体文件、说明约束，并指向可参照的示例模式。

| 策略 | 修改前 | 修改后 |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **限定任务范围。** 指明改哪个文件、什么场景，以及测试偏好。 | *「给 foo.py 加上测试」* | *「给 foo.py 写一个测试，覆盖用户已登出的边界情况。不要用 mock。」* |
| **指向信息来源。** 让 Claude 去看能回答问题的来源。 | *「ExecutionFactory 的 api 为什么这么奇怪？」* | *「翻一翻 ExecutionFactory 的 git 历史，总结它的 api 是怎么变成现在这样的」* |
| **参照已有模式。** 让 Claude 参照你代码库里的模式。 | *「加一个日历组件」* | *「看看首页上现有组件是怎么实现的，理解其中的模式。HotDogWidget.php 是个好例子。照这个模式实现一个新的日历组件，让用户能选择月份，并前后翻页选择年份。除了代码库中已经在用的库，其他都从零实现。」* |
| **描述症状。** 给出症状、可能的位置，以及「修好」是什么样子。 | *「修一下登录的缺陷」* | *「用户反馈会话超时后登录会失败。检查 src/auth/ 里的认证流程，尤其是 token 刷新。先写一个能复现该问题的失败测试，再修好它」* |

当你还在探索、也承担得起随时纠偏时，模糊的提示词也可以很有用。像 `"what would you improve in this file?"` 这样的提示词，能引出你原本想不到要问的东西。

### 提供丰富的内容

<Tip>
  用 `@` 引用文件、粘贴截图或图片，或者把数据直接传进去。
</Tip>

你可以用几种方式给 Claude 提供丰富的数据：

* **用 `@` 引用文件**，而不是描述代码在哪里。Claude 会先读文件再回答。
* **直接粘贴图片**。把图片复制粘贴或拖拽进提示词。
* **给出 URL**，用于文档与 API 参考。用 `/permissions` 把常用域名加入允许列表。
* **把数据直接传进来**，运行 `cat error.log | claude` 就能把文件内容发过去。
* **让 Claude 自己取需要的东西**。告诉 Claude 用 Bash 命令、MCP 工具或读取文件来自行拉取上下文。

***

## 配置你的环境

几个设置步骤就能让 Claude Code 在你所有的会话中显著更有效。关于扩展功能的完整概览以及各自适用的场景，见 [扩展 Claude Code](/docs/en/features-overview)。

### 写一份有效的 CLAUDE.md

<Tip>
  运行 `/init`，根据当前项目结构生成一份 CLAUDE.md 起始文件，然后逐步打磨。
</Tip>

CLAUDE.md 是一个特殊文件，Claude 会在每次对话开始时读取它。把 Bash 命令、代码风格和工作流规则写进去，能给 Claude 提供它无法仅从代码中推测出的持久上下文。

CLAUDE.md 文件没有规定的格式，但要保持简短、便于人阅读。例如：

```markdown CLAUDE.md theme={null}

# Code style

- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow

- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

运行 `/context` 确认 Claude 已加载该文件。CLAUDE.md 每个会话都会加载，所以只写适用范围广的内容。对于只在某些时候相关的领域知识或工作流，改用[智能体技能](/docs/en/skills)。Claude 会按需加载它们，不会让每次对话都变得臃肿。

保持简洁。对每一行都问一句：*「删掉它会让 Claude 犯错吗？」* 如果不会，就删掉。臃肿的 CLAUDE.md 会让 Claude 忽略你真正的指令！

| ✅ 应该写进去 | ❌ 不要写 |
| ---------------------------------------------------- | -------------------------------------------------- |
| Claude 猜不到的 Bash 命令 | Claude 读代码就能弄明白的东西 |
| 与默认约定不同的代码风格规则 | Claude 已经知道的标准语言惯例 |
| 测试说明与偏好的测试运行器 | 详细的 API 文档（改为给出链接） |
| 仓库礼仪（分支命名、PR 约定） | 经常变化的信息 |
| 你项目特有的架构决策 | 长篇解释或教程 |
| 开发环境的特殊之处（必需的环境变量） | 逐文件的代码库说明 |
| 常见坑或反直觉的行为 | 像「写干净的代码」这种不言自明的做法 |

如果明明写了规则，Claude 还是老做你不想要的事，那多半是文件太长、这条规则被淹没了。如果 Claude 问你的问题在 CLAUDE.md 里已经有答案，那可能是措辞有歧义。把 CLAUDE.md 当代码对待：出问题时评审它、定期精简，并通过观察 Claude 的行为是否真的改变来检验改动。对于已签入仓库的 CLAUDE.md，运行 [`/doctor`](/docs/en/commands#all-commands)，Claude 会针对它可以从代码库中推导出的内容提出删减建议。

如果 Claude 老是跳过某一条指令，就单独给这一行加上诸如「IMPORTANT」的强调。如果你强调了很多行，就没有一行会突出。把 CLAUDE.md 签入 git，让团队一起贡献。这个文件的价值会随时间累积。

CLAUDE.md 文件可以用 `@path/to/import` 语法导入其他文件。关于导入规则以及 CLAUDE.md 可以放在哪里，见 [CLAUDE.md 文件](/docs/en/memory#claude-md-files)。

### 配置权限

<Tip>
  想在保住控制权的同时减少提示，就用 `/permissions` 预先批准你信任的工具，并用 `/sandbox` 让沙箱内的命令免询问运行。当你想自己批准编辑和命令时，切到 Manual 模式。
</Tip>

在 Pro、Max 和 Team 套餐上，auto 模式是交互式终端与 VS Code 会话的[内置起始权限模式](/docs/en/permission-modes#eliminate-prompts-with-auto-mode)：由一个独立的分类器模型代替你评审大多数操作，只拦截看起来有风险的动作，比如扩大权限范围、未知的基础设施，或由恶意内容驱动的操作。

在 Manual 模式下——其他套餐的内置起始权限模式——Claude Code 会在可能修改你系统的操作之前询问：文件写入、Bash 命令、MCP 工具。这很安全，但很繁琐。到第十次批准时，你已经是在一路点确认而不是在评审。有两个工具能在 Manual 模式下减少这些打断，并且在 auto 模式同样适用：

* **权限允许列表**：放行你确知安全的特定工具，比如 `npm run lint` 或 `git commit`
* **沙箱**：启用操作系统级隔离，限制文件系统与网络访问，让 Claude 能在划定的边界内更自由地工作

进一步了解[权限模式](/docs/en/permission-modes)、[权限规则](/docs/en/permissions)和[沙箱](/docs/en/sandboxing)。

### 使用 CLI 工具

<Tip>
  告诉 Claude Code 在与外部服务交互时使用 `gh`、`aws`、`gcloud`、`sentry-cli` 这类 CLI 工具。
</Tip>

CLI 工具是与外部服务交互时最省上下文的方式。如果你用 GitHub，就装上 `gh` CLI。Claude 知道怎么用它创建 issue、发起拉取请求和读取评论。没有 `gh` 时，Claude 仍然可以用 GitHub API，但未认证的请求常常会触到速率限制。

Claude 也很擅长学习它原本不认识的 CLI 工具。可以试试这样的提示词：`Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C.`

### 连接 MCP 服务器

<Tip>
  用服务器名称加 URL 或命令运行 `claude mcp add`，就能连接 Notion、Figma 或你的数据库这类外部工具。例如：`claude mcp add --transport http notion https://mcp.notion.com/mcp`。
</Tip>

有了 [MCP 服务器](/docs/en/mcp)，你可以让 Claude 实现来自 issue 跟踪器的功能、查询数据库、分析监控数据、集成 Figma 的设计稿，以及自动化工作流。

### 设置钩子

<Tip>
  对必须每次发生、毫无例外的动作，就用钩子。
</Tip>

[钩子](/docs/en/hooks-guide)会在 Claude 工作流中的特定时点自动运行脚本。与 CLAUDE.md 里只是建议性的指令不同，钩子是确定性的，能保证动作发生。

Claude 可以替你写钩子。试试这样的提示词：*「写一个钩子，在每次文件编辑后运行 eslint」* 或 *「写一个钩子，阻止写入 migrations 文件夹。」* 直接编辑 `.claude/settings.json` 手动配置钩子，并运行 `/hooks` 浏览已配置的内容。

### 创建技能

<Tip>
  在 `.claude/skills/` 里创建 `SKILL.md` 文件，给 Claude 提供领域知识和可复用的工作流。
</Tip>

[智能体技能](/docs/en/skills)用你项目、团队或领域特有的信息扩展 Claude 的知识。Claude 会在相关时自动应用它们，你也可以用 `/skill-name` 直接调用。

在 `.claude/skills/` 下新增一个包含 `SKILL.md` 的目录，就创建了一个技能：

```markdown .claude/skills/api-conventions/SKILL.md theme={null}
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

技能还可以定义你可以直接调用的可重复工作流：
