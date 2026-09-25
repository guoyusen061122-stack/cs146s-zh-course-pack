# 课程介绍 + 用 200 行代码构建 Claude Code（fall2026 W1）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University, Fall 2026
Mihail Eric themodernsoftware.dev

## Slide 2

2026 年的世界现状 themodernsoftware.dev

## Slide 3

这对你意味着什么
- 
全行业更广泛的 AI 采用意味着企业需要你
- 
成为「AI 原生」如今是新目标
- 
但是……门槛也更高了
- 
软件开发者比历史上任何时候都更高产，于是期望值也随之提高
- 
专注于整体性的系统级思考、架构与抽象
- 
与 AI 优先的开发实践结合，你将不可替代 themodernsoftware.dev

## Slide 4

The Modern Software
Developer themodernsoftware.dev

## Slide 5

这门课讲的是原则，不是工具 themodernsoftware.dev

## Slide 6

10 周浓缩成 1 页 themodernsoftware.dev

## Slide 7

核心要点
- 
人与智能体协同的工程
- 
专注于尚未被 AI 系统取代的技能
- 
业务与产品理解
- 
成为技术架构师——培养对软件系统的良好品味
- 
沟通至关重要
- 
大语言模型（LLM）的水平不会超过你
- 
好的上下文带来好的代码
- 
如果你理解不了自己的代码库，LLM 也理解不了
- 
防止 AI 垃圾内容
- 
大胆做实验 themodernsoftware.dev

## Slide 8

课程安排 themodernsoftware.dev
- 
讲师（你们好！）
- 
Stanford 本科/研究生
- 
Monaco 的 AI 负责人，这是一家位于旧金山、做销售领域的创业公司
- 
为从种子轮创业公司到上市企业的数十家公司担任 AI 顾问
- 
在 Amazon Alexa 构建了最早的 LLM
- 
创办并出售了一家机器学习教育创业公司
- 
创办了一家 YC 投资的 AI 编码公司
- 
2 位优秀的助教
- 
Isaac Kan
- 
Vijay Daita

## Slide 9

课程安排
- 
https://themodernsoftware.dev
- 
讲座
- 
周二/周四 17:30-18:20
- 
交付物
- 
6 次作业（每周 1 次），侧重讲座内容的练习
■ https://github.com/mihail911/modern-software-dev-assignments
- 
3-4 次对开源仓库的贡献
- 
1 个期末开放式项目，你将在其中实践我们讲的 AI 编码原则
- 
评分
- 
项目/作业/开源/参与度按 50/15/30/5 分配 themodernsoftware.dev

## Slide 10

课程安排
- 
开源合作伙伴
- 
15 个顶尖 AI 原生开源项目，包括 Vercel、Warp、Marimo、Milvus、Pi、
CrewAI、
Browserbase、HeyGen、CopilotKit、Semgrep、OpenHands、Cmux、Arize、Sloth、Anyscale
- 
嘉宾讲座
- 
当今顶尖 AI 开发者团队的创始人与工程高管（Claude
Code、Devin、Replit、Factory 等的创造者）
- 
融资数十亿美元，估值数百亿美元
- 
不要错过这些讲座！
themodernsoftware.dev

## Slide 11

如何用 200 行代码
构建 Claude Code themodernsoftware.dev

## Slide 12

themodernsoftware.dev
就这么简单

## Slide 13

步骤
- 
在终端读取，并持续追加到对话中
- 
告诉 LLM 有哪些工具可用
- 
它在合适的时机请求工具调用
- 
你在线下执行工具并返回响应
- 
工具
■
「Read_file」
■
「List_dir」
■
「Edit_file」
themodernsoftware.dev

## Slide 14

让我们从零构建一个编码智能体！
themodernsoftware.dev

## Slide 15

themodernsoftware.dev
有问题吗？
