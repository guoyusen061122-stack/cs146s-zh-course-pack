# Power prompting for LLMs（fall2025 W1）

# 大语言模型提示进阶（fall2025 W1）

## Slide 1

## Slide 1

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

The Modern Software Developer CS146S Stanford University，Fall 2025 Mihail Eric themodernsoftware.dev

## Slide 2

## Slide 2

LLM Power Prompting themodernsoftware.dev

LLM 提示进阶 themodernsoftware.dev

## Slide 3

## Slide 3

Prompting background

提示背景

- 

- 

Prompts are the lingua franca for getting LLMs to do what we want and also effectively programming them Courtesy of Andrej Karpathy themodernsoftware.dev

提示词是让大语言模型照我们意愿行事、并有效地对其编程的通用语言 鸣谢 Andrej Karpathy themodernsoftware.dev

## Slide 4

## Slide 4

An analogy

一个类比

- 

- 

Look to how we’ve changed our search engine interactions themodernsoftware.dev

看看我们与搜索引擎的交互方式发生了怎样的变化 themodernsoftware.dev

## Slide 5

## Slide 5

Prompting Background

提示背景

- 

- 

Prompting is both an art and a science

提示词既是一门艺术，也是一门科学

- 

- 

Black-box nature of LLMs means there’s some magic to LLM-whispering effectively

大语言模型的黑箱特性意味着，想有效地「耳语 LLM」多少有些玄学

- 

- 

…but there are established techniques that have empirically improved LLM performance themodernsoftware.dev

……但已有一些经验证能提升大语言模型表现的技术 themodernsoftware.dev

## Slide 6

## Slide 6

Zero-shot prompting

零样本提示

- 

- 

Ask the LLM to do a thing

让大语言模型做一件事

- 

- 

no support

无额外支持

- 

- 

no examples themodernsoftware.dev Write me a Rust for-loop that iterates over a list of strings for every, printing every value in an even index

无示例 themodernsoftware.dev 写一个 Rust for 循环，遍历一个字符串列表，打印出所有偶数下标的值

## Slide 7

## Slide 7

K-shot prompting

K 样本提示

- 

- 

Ask the LLM to do the thing but give it some examples of how to do it

让大语言模型做这件事，但给它一些如何做的示例

- 

- 

Sometimes called in-context learning

有时称为上下文学习

- 

- 

k-shot

k-shot

- 

- 

1, 3, 5 (some empirical results justify these numbers)

1、3、5（一些实证结果支持这些数字）

- 

- 

Ideal for tasks that don’t have too many reasoning steps themodernsoftware.dev

最适合推理步骤不太多的任务 themodernsoftware.dev

## Slide 8

## Slide 8

Write a for-loop iterating over a list of strings using the naming convention in our repo. Write a for-loop iterating over a list of strings using the naming convention in our repo. Here are some examples of how we typically format variable names. <example> var StRaRrAy = [‘cat’, ‘dog’, ‘wombat’] </example> <example> def func CaPiTaLiZeStR = () => {} </example> themodernsoftware.dev

按照我们仓库的命名约定，写一个遍历字符串列表的 for 循环。 按照我们仓库的命名约定，写一个遍历字符串列表的 for 循环。以下是我们通常如何格式化变量名的一些示例。 <example> var StRaRrAy = [‘cat’, ‘dog’, ‘wombat’] </example> <example> def func CaPiTaLiZeStR = () => {} </example> themodernsoftware.dev

## Slide 9

## Slide 9

Chain-of-Thought Prompting

思维链提示

- 

- 

Show reasoning steps for a given task

展示完成给定任务的推理步骤

- 

- 

Multi-shot CoT ■ Work out reasoning traces

多样本 CoT ■ 写出推理轨迹

- 

- 

Zero-shot CoT ■ “Let’s think step-by-step”

零样本 CoT ■ “Let’s think step-by-step”

- 

- 

Prompt for reasoning in explicit <reasoning> tags

用显式的 <reasoning> 标签提示模型进行推理

- 

- 

Best for steps with multiple logical steps

最适合包含多个逻辑步骤的任务

- 

- 

Programming

编程

- 

- 

Math themodernsoftware.dev

数学 themodernsoftware.dev

## Slide 10

## Slide 10

Write a function to check if a number is a perfect cube and a perfect square. I want to write a function to check if a number is a perfect cube and a perfect square. Make sure to provide your reasoning first. Here are some examples of how to provide reasoning for a coding task. <example> Write a function that finds the maximum element in a list. Steps: Initialize a variable with the first element. Traverse the list, comparing… </example> <example> Write a function that checks is a number is a palindrome Steps: Take the number. Reverse the elements in the numbers. Check if … </example> themodernsoftware.dev Multi-shot CoT

写一个函数，检查一个数是否既是完全立方数又是完全平方数。 我想写一个函数，检查一个数是否既是完全立方数又是完全平方数。请务必先给出你的推理。以下是完成编码任务时如何给出推理的一些示例。 <example> 写一个函数，找出列表中的最大元素。 步骤：用一个变量初始化，存入第一个元素。遍历列表，逐个比较…… </example> <example> 写一个函数，检查一个数是否为回文数 步骤：取出这个数。反转数字中的各位。检查是否…… </example> themodernsoftware.dev 多样本 CoT

## Slide 11

## Slide 11

Write a function to find the longest increasing subsequence in an array. Write a function to find the longest increasing subsequence in an array. Think step by step about the subproblems before coding. Include worked out examples of subarrays you are considering as you answer this question. themodernsoftware.dev Zero-shot CoT

写一个函数，找出数组中最长递增子序列。 写一个函数，找出数组中最长递增子序列。 在编码之前先一步步思考各个子问题。回答时给出你正在考虑的子数组的具体例子。 themodernsoftware.dev 零样本 CoT

## Slide 12

## Slide 12

Self-consistency Prompting

自洽性提示

- 

- 

Sample multiple times from output (typically with CoT) and aggregate most common results

对输出多次采样（通常配合 CoT），并汇总最常见的结果

- 

- 

Reduces hallucinations/incorrect answers via a form of model ensembling by sampling diverse reasoning paths themodernsoftware.dev

通过采样多条不同的推理路径，以模型集成的方式减少幻觉与错误答案 themodernsoftware.dev

## Slide 13

## Slide 13

What’s the root cause for this error: Traceback (most recent call last): File "example.py", line 3, in <module> print(nums[i]) IndexError: list index out of range What’s the root cause for this error: Traceback (most recent call last): File "example.py", line 3, in <module> print(nums[i]) IndexError: list index out of range Prompt 5x Take majority result themodernsoftware.dev

这个错误的根因是什么： Traceback (most recent call last): File "example.py", line 3, in <module> print(nums[i]) IndexError: list index out of range 这个错误的根因是什么： Traceback (most recent call last): File "example.py", line 3, in <module> print(nums[i]) IndexError: list index out of range 采样 5 次 取多数结果 themodernsoftware.dev

## Slide 14

## Slide 14

Tool Use

工具调用

- 

- 

Allow LLM to defer to an external system that it needs to interact with

允许大语言模型把任务交给它需要交互的外部系统

- 

- 

One of the most important techniques for reducing hallucinations and enabling the autonomy of LLMs themodernsoftware.dev

减少幻觉、并让大语言模型具备自主性的最重要技术之一 themodernsoftware.dev

## Slide 15

## Slide 15

After you have fixed this IndexError can you ensure that the CI tests still pass? Fix the IndexError. Ensure the CI tests still pass once you have made the fix. Here are the available tools. <tools> pytest -s /path/to/unit_tests pytest -v /path/to/integration_tests </tools> themodernsoftware.dev

在你修好这个 IndexError 之后，能否确保 CI 测试仍然通过？ 修好这个 IndexError。确保修好之后 CI 测试仍然通过。以下是可用的工具。 <tools> pytest -s /path/to/unit_tests pytest -v /path/to/integration_tests </tools> themodernsoftware.dev

## Slide 16

## Slide 16

Retrieval Augmented Generation

检索增强生成

- 

- 

Infuse the LLM with contextual data

为大语言模型注入上下文数据

- 

- 

Keeps LLMs up-to-date (without retraining)

让大语言模型保持最新（无需重新训练）

- 

- 

Faster iteration

迭代更快

- 

- 

You get interpretability and citations for free

免费获得可解释性与引用

- 

- 

Reduces hallucinations themodernsoftware.dev

减少幻觉 themodernsoftware.dev

## Slide 17

## Slide 17

Extend the UserAuthService class to check that the client provides a valid OAuth token. I want to extend the UserAuthService class to check that the client provides a valid OAuth token. Here is how the UserAuthService works now: <code_snippet> def issue_oauth_token(): …. </code_snippet> Here is the path to the requests-oauthlib documentation: <url> https://requests-oauthlib.readthedocs.io/en/ latest/ </url> themodernsoftware.dev

扩展 UserAuthService 类，检查客户端是否提供了有效的 OAuth token。 我想扩展 UserAuthService 类，检查客户端是否提供了有效的 OAuth token。 以下是 UserAuthService 目前的工作方式： <code_snippet> def issue_oauth_token(): …. </code_snippet> 以下是 requests-oauthlib 文档的路径： <url> https://requests-oauthlib.readthedocs.io/en/ latest/ </url> themodernsoftware.dev

## Slide 18

## Slide 18

Reﬂexion

反思（Reflexion）

- 

- 

Make the LLM reﬂect on its output

让大语言模型反思自己的输出

- 

- 

Verbal feedback from environment signals are reincorporated into the LLM by augmenting the context

来自环境信号的言语反馈，通过扩充上下文被重新纳入大语言模型

- 

- 

After an action is taken in an environment and an observation made, add a prompt suﬃx:

在环境中采取行动并得到观察结果之后，追加一段提示词后缀：

- 

- 

“Now critique your answer. Was it correct? If not, explain why and try again.”

“Now critique your answer. Was it correct? If not, explain why and try again.”

- 

- 

Multi-turn prompting

多轮提示

- 

- 

Turn 1: Model gives a ﬁrst try.

第 1 轮：模型先试一次。

- 

- 

Turn 2: You ask “ Was that correct? Reﬂect and revise if needed. ” themodernsoftware.dev

第 2 轮：你问“ Was that correct? Reﬂect and revise if needed. ” themodernsoftware.dev

## Slide 19

## Slide 19

Ensure that the company_location column can handle string and json representations. Extend the logic for company_location to be able to handle string and json representations The unit tests for the company_location type aren’t passing. It appears that the unit tests for company_location are throwing a JSONDecodeError. I am extending the company_location column. I must ensure that when a string is provided as input it doesn’t throw a JSONDecodeError. observe reflect Extend prompt themodernsoftware.dev

确保 company_location 列能处理字符串和 json 表示形式。 扩展 company_location 的逻辑，使其能处理字符串和 json 表示形式 company_location 类型的单元测试没有通过。 看起来 company_location 的单元测试抛出了 JSONDecodeError。 我正在扩展 company_location 列。 我必须确保当输入是字符串时不会抛出 JSONDecodeError。 observe reflect 扩展提示词 themodernsoftware.dev

## Slide 20

## Slide 20

Additional Terminology

附加术语

- 

- 

System prompt

系统提示词

- 

- 

First message provided to LLM (usually not seen by end user)

提供给大语言模型的第一条消息（终端用户通常看不到）

- 

- 

Provides persona, rules about LLM output, style themodernsoftware.dev

规定人设、关于大语言模型输出的规则、风格 themodernsoftware.dev

## Slide 21

## Slide 21

themodernsoftware.dev …

themodernsoftware.dev …

## Slide 22

## Slide 22

themodernsoftware.dev …

themodernsoftware.dev …

## Slide 23

## Slide 23

Additional Terminology

附加术语

- 

- 

User prompt

用户提示词

- 

- 

The actual ask or instruction from a human

人类实际提出的请求或指令

- 

- 

Basically all of our examples so far

基本上就是到目前为止我们所有的例子

- 

- 

Assistant

助手

- 

- 

What the LLM actually generates themodernsoftware.dev

大语言模型实际生成的内容 themodernsoftware.dev

## Slide 24

## Slide 24

themodernsoftware.dev System prompt User prompt Assistant prompt

themodernsoftware.dev 系统提示词 用户提示词 助手提示词

## Slide 25

## Slide 25

Best Practices

最佳实践

- 

- 

Prompt improvement

提示词改进

- 

- 

https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver

https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver

- 

- 

Clear prompting

清晰的提示词

- 

- 

Give prompt to someone with minimal context and if they’re confused an LLM will be too

把提示词交给一个几乎不了解背景的人，如果他看不懂，大语言模型也看不懂

- 

- 

Use role prompting aggressively to make system prompts more powerful themodernsoftware.dev

大胆使用角色提示，让系统提示词更有威力 themodernsoftware.dev

## Slide 26

## Slide 26

themodernsoftware.dev You are a helpful assistant that loves programming at the level of a senior software developer and is very detailed and pedantic in your answers.

themodernsoftware.dev 你是一个乐于助人的助手，热爱编程，水平相当于资深软件开发者，回答非常细致甚至吹毛求疵。

## Slide 27

## Slide 27

themodernsoftware.dev

themodernsoftware.dev

## Slide 28

## Slide 28

themodernsoftware.dev You are a Gen Z digital bestie. Always sound like you’re texting on Snapchat at 2am.

themodernsoftware.dev 你是一个 Z 世代的数字闺蜜。永远像凌晨两点在 Snapchat 上发消息那样说话。

## Slide 29

## Slide 29

- 

- 

Prompts should be formatted with structure Best Practices themodernsoftware.dev Here are the logs: <log> LOG MESSAGE <log> and the stack trace: <error> STACK TRACE <error>

提示词应结构化排版 最佳实践 themodernsoftware.dev 以下是日志： <log> LOG MESSAGE <log> 以及堆栈跟踪： <error> STACK TRACE <error>

## Slide 30

## Slide 30

Best Practices

最佳实践

- 

- 

Be explicit about what you want (languages, tech stacks, libraries, constraints)

明确说出你想要什么（语言、技术栈、库、约束）

- 

- 

Decompose tasks themodernsoftware.dev

拆解任务 themodernsoftware.dev

## Slide 31

## Slide 31

themodernsoftware.dev Questions?

themodernsoftware.dev 有问题吗？
