# 大语言模型简介及其构建方式（fall2025 W1）

## Slide 1

Structured Writing for
Professionals
English 170
Stanford University，Fall 2025
Mihail Eric

## Slide 2

The Modern Software
Developer
CS146S
Stanford University，Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 3

大语言模型简介及其构建方式 themodernsoftware.dev

## Slide 4

2025 年现状 themodernsoftware.dev

## Slide 5

坏消息 themodernsoftware.dev
-
Windsurf 团队

## Slide 6

好消息
- 
软件开发者有潜力达到历史上前所未有的生产率
- 
借助 AI 编码，工程师能以空前的速度掌握技术栈与工具
- 
你不会被 AI 取代。取代你的是会使用 AI 的合格工程师。
themodernsoftware.dev

## Slide 7

The Modern Software
Developer themodernsoftware.dev

## Slide 8

这不是「氛围编程」课 themodernsoftware.dev

## Slide 9

用两页幻灯片讲完 10 周 themodernsoftware.dev

## Slide 10

核心要点
- 
人与智能体协同工程
- 
专注于尚未被 AI 系统取代的技能
- 
业务理解
- 
成为技术负责人
- 
大语言模型的上限就是你自己的水平
- 
好的上下文带来好的代码
- 
如果你看不懂自己的代码库，大语言模型也看不懂 themodernsoftware.dev

## Slide 11

核心要点
- 
大量阅读并评审代码
- 
学会分辨软件的好坏对错
- 
培养好的品味
- 
大胆实验
- 
目前还没有成型的软件模式
- 
所有人都还在摸索
- 
这门课会介绍许多工作流与工具——找到适合你的那套 themodernsoftware.dev

## Slide 12

课程安排
- 
关于我
- 
Stanford 本科/研究生
- 
某销售领域隐形创业公司的 AI 负责人
- 
在 Amazon Alexa 构建了首批大语言模型
- 
创办并卖出了一家 ML 教育创业公司
- 
创办了一家 YC 投资的 AI 编码公司
- 
1 位超棒的课程助理
- 
Febie Lin themodernsoftware.dev

## Slide 13

课程安排
- 
https://themodernsoftware.dev
- 
课程
- 
周一/周五 8:30-9:20 am
- 
交付物
- 
9 次作业（每周 1 次），侧重课堂内容练习
■ https://github.com/mihail911/modern-software-dev-assignments
- 
1 个开放式期末项目，你将实践本课覆盖的 AI 编码原则
- 
评分
- 
项目/作业/参与度占比 80/15/5
- 
相当精彩的内容
- 
来自当今顶尖 AI 开发者创业公司创始人的客座讲座
- 
融资数亿美元，估值数十亿美元
- 
别错过这些演讲！
themodernsoftware.dev

## Slide 14

用 5 页幻灯片讲清大语言模型如何工作
（面向工程师）
themodernsoftware.dev

## Slide 15

基础
- 
大语言模型（large language model）是用于下一 token 预测的自回归模型 themodernsoftware.dev

## Slide 16

Basics themodernsoftware.dev a for loop for
Embedding layer
0.3 the
0.6 idx
0.1 cat
用固定词表对输入做分词
把 token 转换为固定维度的数值向量（约 1-3K 维）
Transformer 层（12-96+），使用自注意力机制（Viswani et.
al. 2017）
得到最可能的下一个 token 的概率分布

## Slide 17

训练过程
- 
阶段 1
- 
自监督预训练
- 
在各类通常是公开的数据源上，教会模型语言的概念
- 
1000 亿到 1 万亿以上 token（语言与代码）
- 
Common Crawl、Wikipedia、StackExchange、公开的 GitHub 仓库
- 
写一个 for 循环
→ 可用于某段代码中
- 
阶段 2
- 
监督微调
- 
教会模型遵循指令
- 
高质量、精心挑选的提示词-回复对（“ what is the capital of Croatia
” -> “
Zagreb is the capital
”）
- 
数万到数十万对
- 
写一个 for 循环
→ 好的，这是一个 for 循环……
- 
阶段 3
- 
偏好调优
- 
让模型输出与人类偏好对齐（有用性、正确性、可读性）
- 
为同一个提示词收集多组成对输出，训练奖励模型预测更受偏好的输出
- 
数万到数十万条人工标注的偏好比较
- 
写一个 for 循环
→ for idx in range(10):
themodernsoftware.dev

## Slide 18

训练过程
- 
推理模型
- 
用思维链推理轨迹扩展训练
- 
工具调用集成
- 
获取人类对推理步骤的偏好
- 
用强化学习学会如何评测推理轨迹、如何回溯等
- 
规模
- 
GPT-3/Claude 3.5 Sonnet - 175B 参数
- 
LLaMA 3.1 - 405B 参数
- 
GPT-4 - 1.8T（据报告）
themodernsoftware.dev

## Slide 19

实践中
- 
优势
- 
专家级代码补全
- 
代码理解
- 
代码修复
- 
局限
- 
幻觉
■
生成不存在或过时的 API（可用稳健的上下文工程缓解）
- 
上下文窗口限制
■
约 100-200K token，但并非所有 token 都是等价的
- 
延迟
■
视任务而定，每次请求从数秒到数分钟（据此规划与委派）
- 
成本
■
最强模型为每百万输入 token $1-3，每百万输出 token $10+ themodernsoftware.dev

## Slide 20

themodernsoftware.dev
有问题吗？
