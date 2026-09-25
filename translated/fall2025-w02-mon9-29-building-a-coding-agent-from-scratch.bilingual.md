# Building a coding agent from scratch（fall2025 W2）

# 从零构建一个编码智能体（fall2025 W2）

## Slide 1

## Slide 1

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

现代软件 开发者 CS146S 斯坦福大学，2025 年秋季 Mihail Eric themodernsoftware.dev

## Slide 2

## Slide 2

Building a Coding Agent From Scratch themodernsoftware.dev

从零构建一个编码 智能体 themodernsoftware.dev

## Slide 3

## Slide 3

themodernsoftware.dev It’s that simple

themodernsoftware.dev 就这么简单

## Slide 4

## Slide 4

Terminology

术语

- 

- 

System prompt

System prompt

- 

- 

Deﬁne the behavior and some directives for the overall LLM

定义整体 LLM 的行为与部分指令

- 

- 

User prompt

User prompt

- 

- 

Custom user requests

用户的定制请求

- 

- 

Assistant prompt

Assistant prompt

- 

- 

LLM’s response themodernsoftware.dev

LLM 的回复 themodernsoftware.dev

## Slide 5

## Slide 5

Steps

步骤

- 

- 

Read in terminal and keep appending to conversation

在终端中读取，并持续追加到对话中

- 

- 

Tell LLM what tools are available

告诉 LLM 有哪些工具可用

- 

- 

It asks for tool use at appropriate time

LLM 在合适的时机请求调用工具

- 

- 

You execute tool oﬄine and return response

你在本地执行工具并返回结果

- 

- 

“Read_ﬁle”

“Read_ﬁle”

- 

- 

“List_dir”

“List_dir”

- 

- 

“Edit_ﬁle”

“Edit_ﬁle”

- 

- 

Create a new ﬁle, edit a new ﬁle themodernsoftware.dev

新建文件、编辑新文件 themodernsoftware.dev

## Slide 6

## Slide 6

Let’s build a coding agent from scratch! themodernsoftware.dev

让我们从零构建一个编码智能体！ themodernsoftware.dev

## Slide 7

## Slide 7

The “Secret” Sauce

“秘密”配方

- 

- 

Looking under the hood of Claude

掀开 Claude 的引擎盖看一看

- 

- 

Front-load context with tiny targeted prompts

用小而精准的提示词把上下文前置

- 

- 

System reminders everywhere including system/user prompts, tool calls, tool results to prevent drift (<system-reminder> tags)

在系统/用户提示词、工具调用、工具结果中到处放置系统提醒以防止漂移（<system-reminder> 标签）

- 

- 

Command preﬁx extraction

命令前缀提取

- 

- 

Spawns sub agents (likely to help with preventing context overloading) themodernsoftware.dev

生成子智能体（很可能用于帮助避免上下文的过载） themodernsoftware.dev
