# 从零构建一个编码智能体（fall2025 W2）

## Slide 1

现代软件
开发者
CS146S
斯坦福大学，2025 年秋季
Mihail Eric themodernsoftware.dev

## Slide 2

从零构建一个编码
智能体 themodernsoftware.dev

## Slide 3

themodernsoftware.dev
就这么简单

## Slide 4

术语
- 
System prompt
- 
定义整体 LLM 的行为与部分指令
- 
User prompt
- 
用户的定制请求
- 
Assistant prompt
- 
LLM 的回复 themodernsoftware.dev

## Slide 5

步骤
- 
在终端中读取，并持续追加到对话中
- 
告诉 LLM 有哪些工具可用
- 
LLM 在合适的时机请求调用工具
- 
你在本地执行工具并返回结果
- 
“Read_ﬁle”
- 
“List_dir”
- 
“Edit_ﬁle”
- 
新建文件、编辑新文件 themodernsoftware.dev

## Slide 6

让我们从零构建一个编码智能体！
themodernsoftware.dev

## Slide 7

“秘密”配方
- 
掀开 Claude 的引擎盖看一看
- 
用小而精准的提示词把上下文前置
- 
在系统/用户提示词、工具调用、工具结果中到处放置系统提醒以防止漂移（<system-reminder> 标签）
- 
命令前缀提取
- 
生成子智能体（很可能用于帮助避免上下文的过载）
themodernsoftware.dev
