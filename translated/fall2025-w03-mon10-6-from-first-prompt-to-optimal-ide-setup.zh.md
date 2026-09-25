# 从最初的提示词到最优 IDE 配置（fall2025 W3）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University, Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

themodernsoftware.dev
嘉宾讲座 - 10/10/25 (8:30am PT, 420-041)
Cognition
研究负责人 Silas Alberti

## Slide 3

AI IDE：从基础到
高级用户 themodernsoftware.dev

## Slide 4

为什么
- 
IDE（集成开发环境）
- 
一体化工作空间，用于软件开发，包含编辑器、编译器、调试器等
- 
大部分开发工作都在这里完成，所以它是 AI 增强的天然形态
- 
在 IDE 的演进过程中，功能整合与开发者自定义之间始终存在拉锯 themodernsoftware.dev

## Slide 5

简史 themodernsoftware.dev
2001
Intellij IDEA 发布，带来先进的上下文代码导航、重构、代码补全
2015
Microsoft VSCode 发布，提供轻量编辑器与高度可扩展的生态
1983
Turbo Pascal 发布，第一个真正的 IDE
1997
Microsoft Visual Studio 发布，为 C++/Visual Basic 语言提供先进的调试能力
1980
2030
2023
Cursor 发布，最早被广泛使用的 AI 原生
IDE 之一

## Slide 6

用法
- 
日常主力模式
- 
行内
- 
函数级
- 
单文件
- 
多文件
- 
真正的 AI 原生
- 
后台智能体
- 
MCP
- 
从记忆中学习
- 
Bugbot（PR 评审）
themodernsoftware.dev

## Slide 7

来看看其中一些内容的实际效果 themodernsoftware.dev

## Slide 8

AI IDE 的内部工作原理 themodernsoftware.dev
Tab 补全
- 
当前代码周围的小块上下文窗口会被加密
- 
服务器接收并运行填充用的
大语言模型（LLM）
- 
建议被送回并显示
聊天
- 
把代码块作为嵌入存储到服务器上的语义索引中
（文件名与代码均已混淆）
- 
任何查询都会检索最相关的代码块，并作为上下文送入
LLM
- 
IDE 会定期重建代码块索引并同步嵌入
- 
代码块之间的差异（diff）通过 Merkle 树计算，以实现高效更新

## Slide 9

- 
对于简单的改动，你不必在提示上过于费心
- 
对于更复杂的任务，你要变成一个产品经理
- 
精心编写的规格文档 themodernsoftware.dev
最佳实践

## Slide 10

- 
目标
- 
这次改动的目的是什么
- 
定义
- 
LLM 需要了解这个问题的哪些前置条件
- 
计划
- 
高层实现拆解
- 
涉及改动的源文件
- 
代码库中哪些部分是相关的，以及为什么
- 
测试用例
- 
测试将如何进行
- 
边界情况
- 
需要考虑哪些特殊情况
- 
超出范围
- 
哪些内容*不*应该改动
- 
扩展
- 
后续哪些改动会变得相关，从而让 LLM 做出前瞻性的设计而不走捷径 themodernsoftware.dev
最佳实践

## Slide 11

来看看其中一些内容的实际效果 themodernsoftware.dev

## Slide 12

- 
优化你的代码库，让人类和智能体都能看懂正在发生什么
- 
LLM 的许多困惑，都来自用凌乱的仓库作为上下文去完成任务
- 
通过描述以下内容，为 LLM 提供最优上下文
- 
仓库导览
- 
文件结构
- 
安装与环境
- 
最佳实践
- 
代码风格
- 
访问模式
- 
API 与契约
- 
所有这些都应详尽记录成文档
- 
提示：
强烈建议在仓库中采用 monorepo 设计 themodernsoftware.dev
最佳实践

## Slide 13

- 
用智能体配置帮助 LLM 浏览你的代码库
- 
claude.md
■
CLAUDE.md 是一个特殊文件，Claude 在开始对话时会自动把它拉入上下文。因此它非常适合用来记录：常用的 bash 命令、核心文件与工具函数、代码风格指南以及测试说明。
- 
c ursorrules
- 
AGENTS.md
■
开放格式
- 
llms.txt
■
为抓取网页的 LLM 提供这种导航指引
- 
注意：
智能体并不总会遵守这些描述与指令。这些内容只作指导之用。
themodernsoftware.dev
最佳实践

## Slide 14

themodernsoftware.dev
示例

## Slide 15

来看看其中一些内容的实际效果 themodernsoftware.dev
