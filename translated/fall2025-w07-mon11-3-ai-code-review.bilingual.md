# AI code review（fall2025 W7）

# AI 代码评审（fall2025 W7）

## Slide 1

## Slide 1

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

## Slide 2

## Slide 2

themodernsoftware.dev Guest Lecture - 11/7/25 CPO of Graphite , Tomas Reimers

themodernsoftware.dev 嘉宾讲座 - 11/7/25 Graphite 的首席产品官 Tomas Reimers

## Slide 3

## Slide 3

AI Code Review themodernsoftware.dev

AI 代码评审 themodernsoftware.dev

## Slide 4

## Slide 4

themodernsoftware.dev

themodernsoftware.dev

## Slide 5

## Slide 5

- 

- 

Software code review is one of the highest leverage activities you can do to become a better engineer and improve overall team code quality Why themodernsoftware.dev

在软件领域，代码评审是提升工程师自身水平、提高团队整体代码质量最有效的手段之一 为什么 themodernsoftware.dev

## Slide 6

## Slide 6

Statistics

统计

- 

- 

Code review has 55-60% error detection rate compared to 25-45% for different testing modes

代码评审的缺陷检出率为 55-60%，而各种测试方式为 25-45%

- 

- 

Study of errors on programs without/with code review reported 4.5 → 0.82 errors/100 lines

一项针对有无代码评审的程序错误研究显示，每 100 行代码的错误数从 4.5 → 降到 0.82

- 

- 

Study at AT&T showed code review had 14% increase in productivity and 90% decrease in defects themodernsoftware.dev Source: Coding Horror

AT&T 的一项研究显示，代码评审使生产率提升 14%，缺陷减少 90% themodernsoftware.dev 来源： Coding Horror

## Slide 7

## Slide 7

What to Catch

要抓什么

- 

- 

Logic and correctness errors themodernsoftware.dev

逻辑与正确性错误 themodernsoftware.dev

## Slide 8

## Slide 8

themodernsoftware.dev

themodernsoftware.dev

## Slide 9

## Slide 9

What to Catch

要抓什么

- 

- 

Readability and maintainability themodernsoftware.dev

可读性与可维护性 themodernsoftware.dev

## Slide 10

## Slide 10

themodernsoftware.dev

themodernsoftware.dev

## Slide 11

## Slide 11

What to Catch

要抓什么

- 

- 

Performance themodernsoftware.dev

性能 themodernsoftware.dev

## Slide 12

## Slide 12

themodernsoftware.dev

themodernsoftware.dev

## Slide 13

## Slide 13

What to Catch

要抓什么

- 

- 

Security themodernsoftware.dev

安全 themodernsoftware.dev

## Slide 14

## Slide 14

themodernsoftware.dev

themodernsoftware.dev

## Slide 15

## Slide 15

What to Catch

要抓什么

- 

- 

Best practices themodernsoftware.dev

最佳实践 themodernsoftware.dev

## Slide 16

## Slide 16

themodernsoftware.dev

themodernsoftware.dev

## Slide 17

## Slide 17

themodernsoftware.dev Source: Blake Smith

themodernsoftware.dev 来源： Blake Smith

## Slide 18

## Slide 18

What’s a Good Code Review themodernsoftware.dev This won’t work vs I see your new method matches the existing style in this ﬁle, taking [X] parameters. Having that many parameters hurts readability and implies the function is doing too much. What do you think about refactoring this method and the existing ones in a later pull request to reduce how many parameters they take?

什么才算好的代码评审 themodernsoftware.dev 这样不行 对比 我看到你的新方法与本文件现有风格一致，接收 [X] 个参数。参数这么多会损害可读性，也意味着这个函数做得太多了。你觉得在后续的拉取请求（PR）里重构这个方法以及已有的那些方法，减少它们的参数数量，怎么样？

## Slide 19

## Slide 19

The New AI World

新的 AI 世界

- 

- 

Graphite (guest lecture 11/7)

Graphite （嘉宾讲座 11/7）

- 

- 

Greptile

Greptile

- 

- 

Coderabbit

Coderabbit

- 

- 

Claude Code / Codex themodernsoftware.dev

Claude Code / Codex themodernsoftware.dev

## Slide 20

## Slide 20

What Has Changed themodernsoftware.dev

发生了什么变化 themodernsoftware.dev

- 

- 

Eﬃciency

效率

- 

- 

Consistency

一致性

- 

- 

Knowledge sharing

知识共享

- 

- 

Reduced cognitive load

降低认知负荷

- 

- 

Continuous improvement

持续改进

- 

- 

Holistic understanding of your code

对代码的整体理解

## Slide 21

## Slide 21

themodernsoftware.dev Source: Greptile

themodernsoftware.dev 来源： Greptile

## Slide 22

## Slide 22

themodernsoftware.dev Source: Graphite

themodernsoftware.dev 来源： Graphite

## Slide 23

## Slide 23

Let’s See AI Code Review in Action themodernsoftware.dev

来看看 AI 代码评审的实际效果 themodernsoftware.dev

## Slide 24

## Slide 24

Limitations themodernsoftware.dev

局限 themodernsoftware.dev

- 

- 

More conﬁguration/setup

配置/设置更多

- 

- 

False positives

误报

- 

- 

Have to train the system → continuous learning

必须训练系统 → 持续学习

- 

- 

Can’t yet catch the idioms and repo best practices

还抓不住代码习惯用法和仓库最佳实践

- 

- 

Can’t handle complex business logic and architecture decisions

处理不了复杂的业务逻辑与架构决策

- 

- 

But that’s where humans are still needed

但这正是仍然需要人的地方

- 

- 

Must be extra cautious with security changes

对安全相关的改动要格外谨慎

- 

- 

Often misses edge cases

经常漏掉边界情况

- 

- 

Code review is more important now than ever with AI coding systems

有了 AI 编码系统，代码评审比以往任何时候都更重要

- 

- 

You own the code that is merged and shipped, no blaming of the AI

代码一旦合并上线就由你负责，不能甩锅给 AI

## Slide 25

## Slide 25

themodernsoftware.dev Questions?

themodernsoftware.dev 有问题吗？
