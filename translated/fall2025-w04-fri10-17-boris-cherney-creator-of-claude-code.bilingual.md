# Boris Cherney, Creator of Claude Code（fall2025 W4）

# Boris Cherney, Creator of Claude Code（fall2025 W4）

## Slide 1

## Slide 1

welcome to claude code boris cherny

欢迎来到 claude code boris cherny

## Slide 2

## Slide 2

tl;dr 1. programming is changing 2. choose your path with claude code 3. think six months out

tl;dr 1. 编程正在改变 2. 用 claude code 选择你的路径 3. 按六个月后的样子来思考

## Slide 3

## Slide 3

npm install -g @anthropic-ai/claude-code claude.ai/code

npm install -g @anthropic-ai/claude-code claude.ai/code

## Slide 4

## Slide 4

1/ programming is at an inflection point

1/ 编程正处于转折点

## Slide 5

## Slide 5

programming language productivity is increasing exponentially, driven by ai 1950 1960 1970 1980 1990 2000 2010 2020 2030 log(productivity) fortran algol cobol basic c pascal prolog c++ python java js go rust ✻ ✻ ✻ ✻ haskell swift ts

编程语言的生产率呈指数级增长，由 ai 驱动 1950 1960 1970 1980 1990 2000 2010 2020 2030 log(productivity) fortran algol cobol basic c pascal prolog c++ python java js go rust ✻ ✻ ✻ ✻ haskell swift ts

## Slide 6

## Slide 6

1950 1960 1970 1980 1990 2000 2010 2020 2030 ed emacs vi turbo pascal qbasic vb eclipse idea sublime cursor copilot ✻ ✻ ✻ devin ✻ ide productivity is following a similar exponential, also driven by ai smalltalk-80 neovim log(productivity) claude code

1950 1960 1970 1980 1990 2000 2010 2020 2030 ed emacs vi turbo pascal qbasic vb eclipse idea sublime cursor copilot ✻ ✻ ✻ devin ✻ ide 的生产率遵循相似的指数曲线，同样由 ai 驱动 smalltalk-80 neovim log(productivity) claude code

## Slide 7

## Slide 7

ibm 029 (1964)

ibm 029 (1964)

## Slide 8

## Slide 8

ed (1969)

ed (1969)

## Slide 9

## Slide 9

smalltalk-80 (1980)

smalltalk-80 (1980)

## Slide 10

## Slide 10

visual basic (1991)

visual basic (1991)

## Slide 11

## Slide 11

eclipse (2001)

eclipse (2001)

## Slide 12

## Slide 12

copilot (2021)

copilot (2021)

## Slide 13

## Slide 13

devin (2024)

devin (2024)

## Slide 14

## Slide 14

ide devx has evolved quickly, and will continue to change even more quickly

ide devx 演进很快，而且还会以更快的速度继续变化

## Slide 15

## Slide 15

verification is evolving quickly, too

验证方式也在快速演进

- manual debugging
- static types (algol)
- formal verification
- abstract interpretation
- automated testing
- continuous integration
- property-based testing (quickcheck)
- dependent typing
- e2e testing
- chaos testing (chaos monkey)
- ai-powered vulnerability testing
- ai-powered unit testing (testgen)
- ai-powered fuzz testing (sapienz)
- self play

- 人工调试
- 静态类型（algol）
- 形式化验证
- 抽象解释
- 自动化测试
- 持续集成
- 基于性质的测试（quickcheck）
- 依赖类型
- 端到端测试
- 混沌测试（chaos monkey）
- AI 驱动的漏洞测试
- AI 驱动的单元测试（testgen）
- AI 驱动的模糊测试（sapienz）
- 自我对弈

- ...

- ...

## Slide 16

## Slide 16

2/ claude code’s approach

2/ claude code 的思路

## Slide 17

## Slide 17

claude code’s approach: works everywhere 1. terminal-native 2. low-level model access 3. infinitely hackable

claude code 的思路： 随处可用 1. 终端原生 2. 底层模型访问 3. 可无限改造

## Slide 18

## Slide 18

18

18

1. Discover
1. Design
1. Build
1. Deploy
1. Support & Scale

1. 探索
1. 设计
1. 构建
1. 部署
1. 支持与扩展

Explore codebase and history Search documentation Onboard & learn Plan project Develop tech specs Deﬁne architecture Implement code Write and execute tests Create commits and PRs Automate CI/CD Conﬁgure environments Manage deployments Debug errors Large-scale refactor Monitor usage & performance Using and mastering all of your team’s CLI tools (e.g., git, docker, bq) so you can focus on solutions, not syntax works across the whole sdlc

探索代码库与历史 检索文档 上手与学习 规划项目 编写技术规格 定义架构 实现代码 编写并执行测试 创建提交与 PR 自动化 CI/CD 配置环境 管理部署 调试错误 大规模重构 监控用量与性能 使用并精通你团队的所有 CLI 工具（例如 git、docker、bq），让你专注于解决方案而非语法 覆盖整个 sdlc

## Slide 19

## Slide 19

3/ one ✻ code, many faces

3/ 一个 ✻ 代码，多种形态

## Slide 20

## Slide 20

terminal

终端

## Slide 21

## Slide 21

ide

ide

## Slide 22

## Slide 22

web & ios

web 与 ios

## Slide 23

## Slide 23

/install-github-app

/install-github-app

## Slide 24

## Slide 24

sdk $ claude -p \ “what did i do this week?” \ --allowedTools Bash(git log:*) --output-format stream-json claude models anthropic, bedrock, or vertex api claude code sdk your app

sdk $ claude -p \ “what did i do this week?” \ --allowedTools Bash(git log:*) --output-format stream-json claude models anthropic, bedrock, or vertex api claude code sdk your app

## Slide 25

## Slide 25

sdk $ get-gcp-logs 1uhd832d | claude -p "correlate errors + commits" \ --output-format=json | jq '.result' claude models anthropic, bedrock, or vertex api claude code sdk your app

sdk $ get-gcp-logs 1uhd832d | claude -p "correlate errors + commits" \ --output-format=json | jq '.result' claude models anthropic, bedrock, or vertex api claude code sdk your app

## Slide 26

## Slide 26

4/ using claude code

4/ 使用 claude code

## Slide 27

## Slide 27

use cases

用例

1. codebase q&a + research
1. write code a. 1-shot b. sidekick c. prototype
1. integrate tools & mcps
1. power automation

1. 代码库问答 + 调研
1. 写代码 a. 一次成型 b. 副手 c. 原型
1. 集成工具与 mcp
1. 强力自动化

## Slide 28

## Slide 28

1. ask claude code about your code

1. 向 claude code 询问你的代码

> how do I make a new

> 我怎样新建一个

@app/services/ValidationTemplateFactory ?

@app/services/ValidationTemplateFactory ？

> why does recoverFromException take so many arguments? look through git history to answer
> why did we fix issue #18363 by adding the if/else in

> recoverFromException 为什么接受这么多参数？翻一下 git 历史再回答
> 我们为什么通过给

@src/login.ts api?

@src/login.ts api 加 if/else 来修 issue #18363？

> in which version did we release the new

> 新的

@api/ext/PreHooks.php api?

@api/ext/PreHooks.php api 是在哪个版本发布的？

> look at PR #9383, then carefully verify which app versions were impacted
> what did I ship last week?

> 看一下 PR #9383，然后仔细核实哪些应用版本受影响
> 我上周交付了什么？

## Slide 29

## Slide 29

1. teach claude to use your tools

1. 教 claude 使用你的工具

> use the barley cli to check for error logs

> 用 barley cli 查错误日志

$ claude mcp add barley_server -- node myserver

$ claude mcp add barley_server -- node myserver

> use the barley mcp server to check for error logs

> 用 barley mcp 服务器查错误日志

## Slide 30

## Slide 30

1. fit the workflow to the task explore › plan › confirm › code › commit

1. 让工作流贴合任务 探索 › 计划 › 确认 › 编码 › 提交

> figure out the root cause for issue #983, then propose a few fixes. Let me choose an approach before you code. ultrathink

> 找出 issue #983 的根因，然后提出几个修复方案。在你编码之前让我先选一个方案。ultrathink

## Slide 31

## Slide 31

1. fit the workflow to the task tests › commit › code › iterate › commit

1. 让工作流贴合任务 测试 › 提交 › 编码 › 迭代 › 提交

> write tests for

> 为

@utils/markdown.ts to make sure links render properly (note the tests won’t pass yet, since links aren’t yet implemented). then commit. then update the code to make the tests pass.

@utils/markdown.ts 写测试，确保链接能正确渲染 （注意这些测试现在还不会通过，因为链接功能尚未实现）。然后提交。然后改代码让测试通过。

## Slide 32

## Slide 32

1. fit the workflow to the task code › screenshot › iterate

1. 让工作流贴合任务 编码 › 截图 › 迭代

> implement [mock.png]. Then screenshot it with puppeteer and iterate till it looks like the mock.

> 实现 [mock.png]。然后用 puppeteer 截图，不断迭代直到它看起来像设计稿。

## Slide 33

## Slide 33

1. use claude code to prototype

1. 用 claude code 做原型

## Slide 34

## Slide 34

> make it so instead of todos showing up as they come in, we hide the tool use and result for todos, and render a fixed todo list above the input. title it

> 改成这样：待办事项不再来一个显示一个，而是隐藏待办的工具调用与结果，在输入框上方渲染一个固定的待办列表。标题用

"/todo (1 of 3)" in grey

"/todo (1 of 3)"，灰色

## Slide 35

## Slide 35

> actually don't show a todo list at all, and instead render the tool uses inline, as bold headings when the model starts working on a todo. keep the

> 实际上完全不要显示待办列表，改为把工具调用内联渲染，当模型开始处理某个待办时，作为加粗标题显示。保留

"step 2 of 4" or whatever, and add middot /todo to see after in grey

"step 2 of 4" 之类的文字，并在后面用灰色补一个中点 /todo

## Slide 36

## Slide 36

> also add a todo pill under the text input, similar to bg tasks. it should render "todos: 1 of 3" or whatever. make the pill interactive

> 另外在文本输入框下面加一个待办胶囊，类似后台任务那种。它应该显示 "todos: 1 of 3" 之类的文字。让这个胶囊可交互

## Slide 37

## Slide 37

> actually undo both the pill and headings. instead, make the todo list render to the right of the input, vertically centered with a grey divider. show it when todos are active, hide it when it's done

> 实际上把胶囊和标题都撤掉。改为把待办列表渲染在输入框右侧，垂直居中，并加一条灰色分隔线。有待办时显示，全部完成时隐藏

## Slide 38

## Slide 38

> actually what if you show the todo list above the input instead. truncate at

> 实际上，如果把待办列表显示在输入框上方会怎样。超过

5 and show "... and 4 more" or whatever. add a heading "Todo:" in grey text

5 条就截断，显示 "... and 4 more" 之类的文字。加一个灰色文字的标题 "Todo:"

## Slide 39

## Slide 39

> actually what if you show the todo list above the input instead. truncate at

> 实际上，如果把待办列表显示在输入框上方会怎样。超过

5 and show "... and 4 more" or whatever. add a heading "Todo:" in grey text

5 条就截断，显示 "... and 4 more" 之类的文字。加一个灰色文字的标题 "Todo:"

## Slide 40

## Slide 40

> actually what if you show the todo list above the input instead. truncate at

> 实际上，如果把待办列表显示在输入框上方会怎样。超过

5 and show "... and 4 more" or whatever. add a heading "Todo:" in grey text

5 条就截断，显示 "... and 4 more" 之类的文字。加一个灰色文字的标题 "Todo:"

## Slide 41

## Slide 41

> instead of showing todos above the input, merge them into the spinner. show the current todo as the spinner message in active verb form, and the next todo instead of the spinner tip, in passive form. also add a /todos slash command to see all todos, and mention it next to "esc to interrupt"

> 不要把待办显示在输入框上方了，改为合并进加载指示器。用主动语态动词形式把当前待办显示为加载指示器文案，用被动形式把下一个待办显示在原本指示的位置。另外加一个 /todos 斜杠命令查看所有待办，并在 "esc to interrupt" 旁边提一下它

## Slide 42

## Slide 42

> make it so i can hit ctrl+t to expand todos inline. also rm the "esc to interrupt" message when we show the todos, and replace it w "ctrl+t to expand"

> 让我可以按 ctrl+t 内联展开待办。另外在显示待办时去掉 "esc to interrupt" 文字，换成 "ctrl+t to expand"

## Slide 44

## Slide 44

6/ lessons

6/ 经验教训

## Slide 45

## Slide 45

1. build for the model six months from now

1. 为六个月后的模型而构建

## Slide 46

## Slide 46

1. be ready to evolve

1. 准备好持续演进

## Slide 47

## Slide 47

1. ask not what the model can do for you

1. 不要问模型能为你做什么

## Slide 48

## Slide 48

4.

4.

## Slide 49

## Slide 49

thanks! npm install -g @anthropic-ai/claude-code claude.ai/code boris@anthropic.com

谢谢！ npm install -g @anthropic-ai/claude-code claude.ai/code boris@anthropic.com
