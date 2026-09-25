# Course intro + build Claude Code in 200 lines（fall2026 W1）

# 课程介绍 + 用 200 行代码构建 Claude Code（fall2026 W1）

## Slide 1

## Slide 1

The Modern Software Developer CS146S Stanford University, Fall 2026 Mihail Eric themodernsoftware.dev

The Modern Software Developer CS146S Stanford University, Fall 2026 Mihail Eric themodernsoftware.dev

## Slide 2

## Slide 2

State of the World: 2026 themodernsoftware.dev

2026 年的世界现状 themodernsoftware.dev

## Slide 3

## Slide 3

What That Means For You

这对你意味着什么

- 

- 

Broader industry-wide AI adoption means companies need you

全行业更广泛的 AI 采用意味着企业需要你

- 

- 

Becoming “AI-native” is now the new goal

成为「AI 原生」如今是新目标

- 

- 

But…the ﬂoor is higher

但是……门槛也更高了

- 

- 

Software developers are more productive than they have ever been in history and so expectations have grown

软件开发者比历史上任何时候都更高产，于是期望值也随之提高

- 

- 

Focus on holistic systems-level thinking, architectures, and abstractions

专注于整体性的系统级思考、架构与抽象

- 

- 

When combined with AI-ﬁrst development practices you will be irreplaceable themodernsoftware.dev

与 AI 优先的开发实践结合，你将不可替代 themodernsoftware.dev

## Slide 4

## Slide 4

The Modern Software Developer themodernsoftware.dev

The Modern Software Developer themodernsoftware.dev

## Slide 5

## Slide 5

This class is about principles not tools themodernsoftware.dev

这门课讲的是原则，不是工具 themodernsoftware.dev

## Slide 6

## Slide 6

10 weeks in 1 slide themodernsoftware.dev

10 周浓缩成 1 页 themodernsoftware.dev

## Slide 7

## Slide 7

The Takeaway

核心要点

- 

- 

Human-agent engineering

人与智能体协同的工程

- 

- 

Focus on the skills that are not yet replaced by AI systems

专注于尚未被 AI 系统取代的技能

- 

- 

Business and product understanding

业务与产品理解

- 

- 

Become the tech architect – develop good taste for software systems

成为技术架构师——培养对软件系统的良好品味

- 

- 

Communication is crucial

沟通至关重要

- 

- 

LLMs are only as good as you are

大语言模型（LLM）的水平不会超过你

- 

- 

Good context leads to good code

好的上下文带来好的代码

- 

- 

If you can’t understand your codebase, neither will an LLM

如果你理解不了自己的代码库，LLM 也理解不了

- 

- 

Prevent AI slop

防止 AI 垃圾内容

- 

- 

Experiment aggressively themodernsoftware.dev

大胆做实验 themodernsoftware.dev

## Slide 8

## Slide 8

Course Logistics themodernsoftware.dev

课程安排 themodernsoftware.dev

- 

- 

Instructor (Hi!)

讲师（你们好！）

- 

- 

Stanford undergrad/grad

Stanford 本科/研究生

- 

- 

Head of AI at Monaco, an SF-based startup in the sales space

Monaco 的 AI 负责人，这是一家位于旧金山、做销售领域的创业公司

- 

- 

AI Advisor for dozens of companies from seed-stage startups to public enterprises

为从种子轮创业公司到上市企业的数十家公司担任 AI 顾问

- 

- 

Built ﬁrst LLMs at Amazon Alexa

在 Amazon Alexa 构建了最早的 LLM

- 

- 

Founded and sold an ML education startup

创办并出售了一家机器学习教育创业公司

- 

- 

Founded a YC-backed AI coding company

创办了一家 YC 投资的 AI 编码公司

- 

- 

2 awesome CAs

2 位优秀的助教

- 

- 

Isaac Kan

Isaac Kan

- 

- 

Vijay Daita

Vijay Daita

## Slide 9

## Slide 9

Course Logistics

课程安排

- 

- 

https://themodernsoftware.dev

https://themodernsoftware.dev

- 

- 

Lectures

讲座

- 

- 

Tue/Thur 5:30-6:20 pm

周二/周四 17:30-18:20

- 

- 

Deliverables

交付物

- 

- 

6 assignments (1x/week) focusing on lecture material practice ■ https://github.com/mihail911/modern-software-dev-assignments

6 次作业（每周 1 次），侧重讲座内容的练习 ■ https://github.com/mihail911/modern-software-dev-assignments

- 

- 

3-4 contributions to OSS repositories

3-4 次对开源仓库的贡献

- 

- 

1 ﬁnal open-ended project in which you will exercise AI coding principles we cover

1 个期末开放式项目，你将在其中实践我们讲的 AI 编码原则

- 

- 

Grading

评分

- 

- 

50/15/30/5 breakdown for project/assignments/OSS/participation themodernsoftware.dev

项目/作业/开源/参与度按 50/15/30/5 分配 themodernsoftware.dev

## Slide 10

## Slide 10

Course Logistics

课程安排

- 

- 

OSS Partners

开源合作伙伴

- 

- 

15 of the top AI-native open-source projects including Vercel, Warp, Marimo, Milvus, Pi, CrewAI, Browserbase, HeyGen, CopilotKit, Semgrep, OpenHands, Cmux, Arize, Sloth, Anyscale

15 个顶尖 AI 原生开源项目，包括 Vercel、Warp、Marimo、Milvus、Pi、 CrewAI、 Browserbase、HeyGen、CopilotKit、Semgrep、OpenHands、Cmux、Arize、Sloth、Anyscale

- 

- 

Guest Lectures

嘉宾讲座

- 

- 

Founders and engineering execs leading top AI developer teams today (creators of Claude Code, Devin, Replit, Factory, and more)

当今顶尖 AI 开发者团队的创始人与工程高管（Claude Code、Devin、Replit、Factory 等的创造者）

- 

- 

Billions of dollars raised, tens of billions in valuation

融资数十亿美元，估值数百亿美元

- 

- 

Don’t miss these talks! themodernsoftware.dev

不要错过这些讲座！ themodernsoftware.dev

## Slide 11

## Slide 11

How to Build Claude Code in 200 Lines of Code themodernsoftware.dev

如何用 200 行代码 构建 Claude Code themodernsoftware.dev

## Slide 12

## Slide 12

themodernsoftware.dev It’s that simple

themodernsoftware.dev 就这么简单

## Slide 13

## Slide 13

Steps

步骤

- 

- 

Read in terminal and keep appending to conversation

在终端读取，并持续追加到对话中

- 

- 

Tell LLM what tools are available

告诉 LLM 有哪些工具可用

- 

- 

It asks for tool use at appropriate time

它在合适的时机请求工具调用

- 

- 

You execute tool oﬄine and return response

你在线下执行工具并返回响应

- 

- 

Tools ■ “Read_ﬁle” ■ “List_dir” ■ “Edit_ﬁle” themodernsoftware.dev

工具 ■ 「Read_file」 ■ 「List_dir」 ■ 「Edit_file」 themodernsoftware.dev

## Slide 14

## Slide 14

Let’s build a coding agent from scratch! themodernsoftware.dev

让我们从零构建一个编码智能体！ themodernsoftware.dev

## Slide 15

## Slide 15

themodernsoftware.dev Questions?

themodernsoftware.dev 有问题吗？
