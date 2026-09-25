# AI 代码评审（fall2025 W7）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University, Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

themodernsoftware.dev
嘉宾讲座 - 11/7/25
Graphite
的首席产品官 Tomas Reimers

## Slide 3

AI 代码评审 themodernsoftware.dev

## Slide 4

themodernsoftware.dev

## Slide 5

- 
在软件领域，代码评审是提升工程师自身水平、提高团队整体代码质量最有效的手段之一
为什么 themodernsoftware.dev

## Slide 6

统计
- 
代码评审的缺陷检出率为 55-60%，而各种测试方式为 25-45%
- 
一项针对有无代码评审的程序错误研究显示，每 100 行代码的错误数从 4.5
→
降到 0.82
- 
AT&T 的一项研究显示，代码评审使生产率提升 14%，缺陷减少 90% themodernsoftware.dev
来源：
Coding Horror

## Slide 7

要抓什么
- 
逻辑与正确性错误 themodernsoftware.dev

## Slide 8

themodernsoftware.dev

## Slide 9

要抓什么
- 
可读性与可维护性 themodernsoftware.dev

## Slide 10

themodernsoftware.dev

## Slide 11

要抓什么
- 
性能 themodernsoftware.dev

## Slide 12

themodernsoftware.dev

## Slide 13

要抓什么
- 
安全 themodernsoftware.dev

## Slide 14

themodernsoftware.dev

## Slide 15

要抓什么
- 
最佳实践 themodernsoftware.dev

## Slide 16

themodernsoftware.dev

## Slide 17

themodernsoftware.dev
来源：
Blake Smith

## Slide 18

什么才算好的代码评审 themodernsoftware.dev
这样不行 对比
我看到你的新方法与本文件现有风格一致，接收 [X] 个参数。参数这么多会损害可读性，也意味着这个函数做得太多了。你觉得在后续的拉取请求（PR）里重构这个方法以及已有的那些方法，减少它们的参数数量，怎么样？

## Slide 19

新的 AI 世界
- 
Graphite
（嘉宾讲座 11/7）
- 
Greptile
- 
Coderabbit
- 
Claude Code / Codex themodernsoftware.dev

## Slide 20

发生了什么变化 themodernsoftware.dev
- 
效率
- 
一致性
- 
知识共享
- 
降低认知负荷
- 
持续改进
- 
对代码的整体理解

## Slide 21

themodernsoftware.dev
来源：
Greptile

## Slide 22

themodernsoftware.dev
来源：
Graphite

## Slide 23

来看看 AI 代码评审的实际效果 themodernsoftware.dev

## Slide 24

局限 themodernsoftware.dev
- 
配置/设置更多
- 
误报
- 
必须训练系统
→ 持续学习
- 
还抓不住代码习惯用法和仓库最佳实践
- 
处理不了复杂的业务逻辑与架构决策
- 
但这正是仍然需要人的地方
- 
对安全相关的改动要格外谨慎
- 
经常漏掉边界情况
- 
有了 AI 编码系统，代码评审比以往任何时候都更重要
- 
代码一旦合并上线就由你负责，不能甩锅给 AI

## Slide 25

themodernsoftware.dev
有问题吗？
