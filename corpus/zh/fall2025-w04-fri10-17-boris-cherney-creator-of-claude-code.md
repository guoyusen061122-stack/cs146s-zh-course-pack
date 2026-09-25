# Boris Cherney, Creator of Claude Code（fall2025 W4）

## Slide 1

欢迎来到 claude code boris cherny

## Slide 2

tl;dr
1.
编程正在改变
2.
用 claude code 选择你的路径
3.
按六个月后的样子来思考

## Slide 3

npm install -g @anthropic-ai/claude-code claude.ai/code

## Slide 4

1/ 编程正处于转折点

## Slide 5

编程语言的生产率呈指数级增长，由 ai 驱动
1950 1960 1970 1980 1990 2000 2010 2020 2030 log(productivity)
fortran algol cobol basic c pascal prolog c++ python java js go rust
✻
✻
✻
✻ haskell swift ts

## Slide 6

1950 1960 1970 1980 1990 2000 2010 2020 2030 ed emacs vi turbo pascal qbasic vb eclipse idea sublime cursor copilot
✻
✻
✻ devin
✻ ide 的生产率遵循相似的指数曲线，同样由 ai 驱动 smalltalk-80 neovim log(productivity)
claude code

## Slide 7

ibm 029 (1964)

## Slide 8

ed (1969)

## Slide 9

smalltalk-80 (1980)

## Slide 10

visual basic (1991)

## Slide 11

eclipse (2001)

## Slide 12

copilot (2021)

## Slide 13

devin (2024)

## Slide 14

ide devx 演进很快，而且还会以更快的速度继续变化

## Slide 15

验证方式也在快速演进
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
-
...

## Slide 16

2/ claude code 的思路

## Slide 17

claude code 的思路：
随处可用
1.
终端原生
2.
底层模型访问
3.
可无限改造

## Slide 18

18
1. 探索
2. 设计
3. 构建
4. 部署
5. 支持与扩展
探索代码库与历史
检索文档
上手与学习
规划项目
编写技术规格
定义架构
实现代码
编写并执行测试
创建提交与 PR
自动化 CI/CD
配置环境
管理部署
调试错误
大规模重构
监控用量与性能
使用并精通你团队的所有 CLI 工具（例如 git、docker、bq），让你专注于解决方案而非语法 覆盖整个 sdlc

## Slide 19

3/ 一个
✻ 代码，多种形态

## Slide 20

终端

## Slide 21

ide

## Slide 22

web 与 ios

## Slide 23

/install-github-app

## Slide 24

sdk
$ claude -p \
“what did i do this week?” \
--allowedTools Bash(git log:*)
--output-format stream-json claude models anthropic, bedrock, or vertex api claude code sdk your app

## Slide 25

sdk
$ get-gcp-logs 1uhd832d | claude -p "correlate errors + commits" \
--output-format=json | jq '.result'
claude models anthropic, bedrock, or vertex api claude code sdk your app

## Slide 26

4/ 使用 claude code

## Slide 27

用例
1. 代码库问答 + 调研
2. 写代码 a. 一次成型 b. 副手 c. 原型
3. 集成工具与 mcp
4. 强力自动化

## Slide 28

1. 向 claude code 询问你的代码
> 我怎样新建一个
@app/services/ValidationTemplateFactory
？
> recoverFromException 为什么接受这么多参数？翻一下 git 历史再回答
> 我们为什么通过给
@src/login.ts api 加 if/else 来修 issue #18363？
> 新的
@api/ext/PreHooks.php api 是在哪个版本发布的？
> 看一下 PR #9383，然后仔细核实哪些应用版本受影响
> 我上周交付了什么？

## Slide 29

2. 教 claude 使用你的工具
> 用 barley cli 查错误日志
$ claude mcp add barley_server -- node myserver
> 用 barley mcp 服务器查错误日志

## Slide 30

3. 让工作流贴合任务 探索 › 计划 › 确认 › 编码 › 提交
> 找出 issue #983 的根因，然后提出几个修复方案。在你编码之前让我先选一个方案。ultrathink

## Slide 31

3. 让工作流贴合任务 测试 › 提交 › 编码 › 迭代 › 提交
> 为
@utils/markdown.ts 写测试，确保链接能正确渲染
（注意这些测试现在还不会通过，因为链接功能尚未实现）。然后提交。然后改代码让测试通过。

## Slide 32

3. 让工作流贴合任务 编码 › 截图 › 迭代
> 实现 [mock.png]。然后用 puppeteer 截图，不断迭代直到它看起来像设计稿。

## Slide 33

4. 用 claude code 做原型

## Slide 34

> 改成这样：待办事项不再来一个显示一个，而是隐藏待办的工具调用与结果，在输入框上方渲染一个固定的待办列表。标题用
"/todo (1 of 3)"，灰色

## Slide 35

> 实际上完全不要显示待办列表，改为把工具调用内联渲染，当模型开始处理某个待办时，作为加粗标题显示。保留
"step 2 of 4" 之类的文字，并在后面用灰色补一个中点 /todo

## Slide 36

> 另外在文本输入框下面加一个待办胶囊，类似后台任务那种。它应该显示 "todos: 1 of 3" 之类的文字。让这个胶囊可交互

## Slide 37

> 实际上把胶囊和标题都撤掉。改为把待办列表渲染在输入框右侧，垂直居中，并加一条灰色分隔线。有待办时显示，全部完成时隐藏

## Slide 38

> 实际上，如果把待办列表显示在输入框上方会怎样。超过
5 条就截断，显示 "... and 4 more" 之类的文字。加一个灰色文字的标题 "Todo:"

## Slide 39

> 实际上，如果把待办列表显示在输入框上方会怎样。超过
5 条就截断，显示 "... and 4 more" 之类的文字。加一个灰色文字的标题 "Todo:"

## Slide 40

> 实际上，如果把待办列表显示在输入框上方会怎样。超过
5 条就截断，显示 "... and 4 more" 之类的文字。加一个灰色文字的标题 "Todo:"

## Slide 41

> 不要把待办显示在输入框上方了，改为合并进加载指示器。用主动语态动词形式把当前待办显示为加载指示器文案，用被动形式把下一个待办显示在原本指示的位置。另外加一个 /todos 斜杠命令查看所有待办，并在 "esc to interrupt" 旁边提一下它

## Slide 42

> 让我可以按 ctrl+t 内联展开待办。另外在显示待办时去掉 "esc to interrupt" 文字，换成 "ctrl+t to expand"

## Slide 44

6/ 经验教训

## Slide 45

1. 为六个月后的模型而构建

## Slide 46

2. 准备好持续演进

## Slide 47

3. 不要问模型能为你做什么

## Slide 48

4.

## Slide 49

谢谢！
npm install -g @anthropic-ai/claude-code claude.ai/code boris@anthropic.com
