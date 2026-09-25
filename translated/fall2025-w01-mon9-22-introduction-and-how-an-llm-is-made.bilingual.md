# Introduction and how an LLM is made（fall2025 W1）

# 大语言模型简介及其构建方式（fall2025 W1）

## Slide 1

## Slide 1

Structured Writing for Professionals English 170 Stanford University, Fall 2025 Mihail Eric

Structured Writing for Professionals English 170 Stanford University，Fall 2025 Mihail Eric

## Slide 2

## Slide 2

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

The Modern Software Developer CS146S Stanford University，Fall 2025 Mihail Eric themodernsoftware.dev

## Slide 3

## Slide 3

Introduction and How LLMs are Made themodernsoftware.dev

大语言模型简介及其构建方式 themodernsoftware.dev

## Slide 4

## Slide 4

State of the World: 2025 themodernsoftware.dev

2025 年现状 themodernsoftware.dev

## Slide 5

## Slide 5

Bad News themodernsoftware.dev - Windsurf team

坏消息 themodernsoftware.dev - Windsurf 团队

## Slide 6

## Slide 6

Good News

好消息

- 

- 

Software developers have the potential to be more productive than they have ever been in history

软件开发者有潜力达到历史上前所未有的生产率

- 

- 

With AI coding an engineer can pick up tech stacks and tools at an unprecedented pace

借助 AI 编码，工程师能以空前的速度掌握技术栈与工具

- 

- 

You won’t be replaced by AI. You’ll be replaced by a competent engineer who knows how to use AI. themodernsoftware.dev

你不会被 AI 取代。取代你的是会使用 AI 的合格工程师。 themodernsoftware.dev

## Slide 7

## Slide 7

The Modern Software Developer themodernsoftware.dev

The Modern Software Developer themodernsoftware.dev

## Slide 8

## Slide 8

This is not the “vibe coding” class themodernsoftware.dev

这不是「氛围编程」课 themodernsoftware.dev

## Slide 9

## Slide 9

10 weeks in 2 slides themodernsoftware.dev

用两页幻灯片讲完 10 周 themodernsoftware.dev

## Slide 10

## Slide 10

The Takeaway

核心要点

- 

- 

Human-agent engineering

人与智能体协同工程

- 

- 

Focus on the skills that are not yet replaced by AI systems

专注于尚未被 AI 系统取代的技能

- 

- 

Business understanding

业务理解

- 

- 

Become the tech lead

成为技术负责人

- 

- 

LLMs are only as good as you are

大语言模型的上限就是你自己的水平

- 

- 

Good context leads to good code

好的上下文带来好的代码

- 

- 

If you can’t understand your codebase, neither will an LLM themodernsoftware.dev

如果你看不懂自己的代码库，大语言模型也看不懂 themodernsoftware.dev

## Slide 11

## Slide 11

The Takeaway

核心要点

- 

- 

Read and review a lot of code

大量阅读并评审代码

- 

- 

Learn to discern good from bad, wrong software

学会分辨软件的好坏对错

- 

- 

Have good taste

培养好的品味

- 

- 

Experiment aggressively

大胆实验

- 

- 

There are no established software patterns yet

目前还没有成型的软件模式

- 

- 

Everyone is still ﬁguring it out

所有人都还在摸索

- 

- 

This class will introduce many workﬂows and tools - ﬁgure out what works for you themodernsoftware.dev

这门课会介绍许多工作流与工具——找到适合你的那套 themodernsoftware.dev

## Slide 12

## Slide 12

Course Logistics

课程安排

- 

- 

A bit about me

关于我

- 

- 

Stanford undergrad/grad

Stanford 本科/研究生

- 

- 

Head of AI at a stealth startup in the sales space

某销售领域隐形创业公司的 AI 负责人

- 

- 

Built ﬁrst LLMs at Amazon Alexa

在 Amazon Alexa 构建了首批大语言模型

- 

- 

Founded and sold an ML education startup

创办并卖出了一家 ML 教育创业公司

- 

- 

Founded a YC-backed AI coding company

创办了一家 YC 投资的 AI 编码公司

- 

- 

1 awesome CA

1 位超棒的课程助理

- 

- 

Febie Lin themodernsoftware.dev

Febie Lin themodernsoftware.dev

## Slide 13

## Slide 13

Course Logistics

课程安排

- 

- 

https://themodernsoftware.dev

https://themodernsoftware.dev

- 

- 

Lectures

课程

- 

- 

Mon/Fri 8:30-9:20 am

周一/周五 8:30-9:20 am

- 

- 

Deliverables

交付物

- 

- 

9 assignments (1x/week) focusing on lecture material practice ■ https://github.com/mihail911/modern-software-dev-assignments

9 次作业（每周 1 次），侧重课堂内容练习 ■ https://github.com/mihail911/modern-software-dev-assignments

- 

- 

1 ﬁnal open-ended project in which you will exercise AI coding principles we cover

1 个开放式期末项目，你将实践本课覆盖的 AI 编码原则

- 

- 

Grading

评分

- 

- 

80/15/5 breakdown for project/assignments/participation

项目/作业/参与度占比 80/15/5

- 

- 

Something pretty awesome

相当精彩的内容

- 

- 

Guest lectures from founders leading top AI developer startups today

来自当今顶尖 AI 开发者创业公司创始人的客座讲座

- 

- 

$100s of millions raised, billions in valuation

融资数亿美元，估值数十亿美元

- 

- 

Don’t miss these talks! themodernsoftware.dev

别错过这些演讲！ themodernsoftware.dev

## Slide 14

## Slide 14

How LLMs Work in 5 Slides (For Engineers) themodernsoftware.dev

用 5 页幻灯片讲清大语言模型如何工作 （面向工程师） themodernsoftware.dev

## Slide 15

## Slide 15

Basics

基础

- 

- 

LLMs (large language models) are autoregressive models for next-token prediction themodernsoftware.dev

大语言模型（large language model）是用于下一 token 预测的自回归模型 themodernsoftware.dev

## Slide 16

## Slide 16

Basics themodernsoftware.dev a for loop for Embedding layer 0.3 the 0.6 idx 0.1 cat Tokenize inputs using ﬁxed vocabulary Convert tokens into ﬁxed-dimensional numerical vectors (~1-3K dimensions) Transformers layers (12-96+) using self-attention mechanism (Viswani et. al. 2017) Get probability distribution over most likely next token

Basics themodernsoftware.dev a for loop for Embedding layer 0.3 the 0.6 idx 0.1 cat 用固定词表对输入做分词 把 token 转换为固定维度的数值向量（约 1-3K 维） Transformer 层（12-96+），使用自注意力机制（Viswani et. al. 2017） 得到最可能的下一个 token 的概率分布

## Slide 17

## Slide 17

Training Process

训练过程

- 

- 

Stage 1

阶段 1

- 

- 

Self-supervised pretraining

自监督预训练

- 

- 

Teach the model notion of language on a variety of often public data sources

在各类通常是公开的数据源上，教会模型语言的概念

- 

- 

100s of billions to trillion+ tokens (language and code)

1000 亿到 1 万亿以上 token（语言与代码）

- 

- 

Common Crawl, Wikipedia, StackExchange, Public Github repos

Common Crawl、Wikipedia、StackExchange、公开的 GitHub 仓库

- 

- 

Write a for loop → that could be used in a piece of code

写一个 for 循环 → 可用于某段代码中

- 

- 

Stage 2

阶段 2

- 

- 

Supervised ﬁnetuning

监督微调

- 

- 

Teach model to follow instructions

教会模型遵循指令

- 

- 

High-quality, curated prompt-response pairs (“ what is the capital of Croatia ” -> “ Zagreb is the capital ”)

高质量、精心挑选的提示词-回复对（“ what is the capital of Croatia ” -> “ Zagreb is the capital ”）

- 

- 

Tens of thousands to 100s of thousands of pairs

数万到数十万对

- 

- 

Write a for loop → ok here’s a for loop…

写一个 for 循环 → 好的，这是一个 for 循环……

- 

- 

Stage 3

阶段 3

- 

- 

Preferencing tuning

偏好调优

- 

- 

Align model outputs with human preferences (helpfulness, correctness, readability)

让模型输出与人类偏好对齐（有用性、正确性、可读性）

- 

- 

Collect pairs of outputs for same prompt and train reward model to predict preferred output

为同一个提示词收集多组成对输出，训练奖励模型预测更受偏好的输出

- 

- 

Tens of thousands to 100s of thousands of human-labeled comparisons

数万到数十万条人工标注的偏好比较

- 

- 

Write a for loop → for idx in range(10): themodernsoftware.dev

写一个 for 循环 → for idx in range(10): themodernsoftware.dev

## Slide 18

## Slide 18

Training Process

训练过程

- 

- 

Reasoning models

推理模型

- 

- 

Extend training with chain-of-thought reasoning traces

用思维链推理轨迹扩展训练

- 

- 

Tool-use integration

工具调用集成

- 

- 

Get human preferences on reasoning steps

获取人类对推理步骤的偏好

- 

- 

Reinforcement learning to learn how to evaluate reasoning traces, backtrack, etc

用强化学习学会如何评测推理轨迹、如何回溯等

- 

- 

Size

规模

- 

- 

GPT-3/Claude 3.5 Sonnet - 175B parameters

GPT-3/Claude 3.5 Sonnet - 175B 参数

- 

- 

LLaMA 3.1 - 405B parameters

LLaMA 3.1 - 405B 参数

- 

- 

GPT-4 - 1.8T (reported) themodernsoftware.dev

GPT-4 - 1.8T（据报告） themodernsoftware.dev

## Slide 19

## Slide 19

In practice

实践中

- 

- 

Strengths

优势

- 

- 

Expert-level code completion

专家级代码补全

- 

- 

Code understanding

代码理解

- 

- 

Code ﬁxing

代码修复

- 

- 

Limitations

局限

- 

- 

Hallucinations ■ Generating non-existent/out-of-date APIs (mitigated with robust context engineering)

幻觉 ■ 生成不存在或过时的 API（可用稳健的上下文工程缓解）

- 

- 

Context window limits ■ ~100-200K tokens but not all are created equal

上下文窗口限制 ■ 约 100-200K token，但并非所有 token 都是等价的

- 

- 

Latency ■ Seconds to minutes per request depending on task (plan and delegate accordingly)

延迟 ■ 视任务而定，每次请求从数秒到数分钟（据此规划与委派）

- 

- 

Cost ■ $1-3 per million input tokens, $10+ per million output tokens for best models themodernsoftware.dev

成本 ■ 最强模型为每百万输入 token $1-3，每百万输出 token $10+ themodernsoftware.dev

## Slide 20

## Slide 20

themodernsoftware.dev Questions?

themodernsoftware.dev 有问题吗？
