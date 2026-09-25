# 大语言模型提示进阶（fall2025 W1）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University，Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

LLM 提示进阶 themodernsoftware.dev

## Slide 3

提示背景
- 
提示词是让大语言模型照我们意愿行事、并有效地对其编程的通用语言
鸣谢
Andrej Karpathy themodernsoftware.dev

## Slide 4

一个类比
- 
看看我们与搜索引擎的交互方式发生了怎样的变化 themodernsoftware.dev

## Slide 5

提示背景
- 
提示词既是一门艺术，也是一门科学
- 
大语言模型的黑箱特性意味着，想有效地「耳语 LLM」多少有些玄学
- 
……但已有一些经验证能提升大语言模型表现的技术 themodernsoftware.dev

## Slide 6

零样本提示
- 
让大语言模型做一件事
- 
无额外支持
- 
无示例 themodernsoftware.dev
写一个 Rust for 循环，遍历一个字符串列表，打印出所有偶数下标的值

## Slide 7

K 样本提示
- 
让大语言模型做这件事，但给它一些如何做的示例
- 
有时称为上下文学习
- 
k-shot
- 
1、3、5（一些实证结果支持这些数字）
- 
最适合推理步骤不太多的任务 themodernsoftware.dev

## Slide 8

按照我们仓库的命名约定，写一个遍历字符串列表的 for 循环。
按照我们仓库的命名约定，写一个遍历字符串列表的 for 循环。以下是我们通常如何格式化变量名的一些示例。
<example> var StRaRrAy = [‘cat’, ‘dog’, ‘wombat’]
</example>
<example> def func CaPiTaLiZeStR = () => {}
</example> themodernsoftware.dev

## Slide 9

思维链提示
- 
展示完成给定任务的推理步骤
- 
多样本 CoT
■
写出推理轨迹
- 
零样本 CoT
■
“Let’s think step-by-step”
- 
用显式的 <reasoning> 标签提示模型进行推理
- 
最适合包含多个逻辑步骤的任务
- 
编程
- 
数学 themodernsoftware.dev

## Slide 10

写一个函数，检查一个数是否既是完全立方数又是完全平方数。
我想写一个函数，检查一个数是否既是完全立方数又是完全平方数。请务必先给出你的推理。以下是完成编码任务时如何给出推理的一些示例。
<example>
写一个函数，找出列表中的最大元素。
步骤：用一个变量初始化，存入第一个元素。遍历列表，逐个比较……
</example>
<example>
写一个函数，检查一个数是否为回文数
步骤：取出这个数。反转数字中的各位。检查是否……
</example> themodernsoftware.dev
多样本 CoT

## Slide 11

写一个函数，找出数组中最长递增子序列。
写一个函数，找出数组中最长递增子序列。
在编码之前先一步步思考各个子问题。回答时给出你正在考虑的子数组的具体例子。
themodernsoftware.dev
零样本 CoT

## Slide 12

自洽性提示
- 
对输出多次采样（通常配合 CoT），并汇总最常见的结果
- 
通过采样多条不同的推理路径，以模型集成的方式减少幻觉与错误答案 themodernsoftware.dev

## Slide 13

这个错误的根因是什么：
Traceback (most recent call last):
File "example.py", line 3, in
<module> print(nums[i])
IndexError: list index out of range
这个错误的根因是什么：
Traceback (most recent call last):
File "example.py", line 3, in
<module> print(nums[i])
IndexError: list index out of range
采样 5 次
取多数结果 themodernsoftware.dev

## Slide 14

工具调用
- 
允许大语言模型把任务交给它需要交互的外部系统
- 
减少幻觉、并让大语言模型具备自主性的最重要技术之一 themodernsoftware.dev

## Slide 15

在你修好这个
IndexError 之后，能否确保 CI 测试仍然通过？
修好这个 IndexError。确保修好之后 CI 测试仍然通过。以下是可用的工具。
<tools> pytest -s /path/to/unit_tests pytest -v /path/to/integration_tests
</tools> themodernsoftware.dev

## Slide 16

检索增强生成
- 
为大语言模型注入上下文数据
- 
让大语言模型保持最新（无需重新训练）
- 
迭代更快
- 
免费获得可解释性与引用
- 
减少幻觉 themodernsoftware.dev

## Slide 17

扩展 UserAuthService 类，检查客户端是否提供了有效的 OAuth token。
我想扩展 UserAuthService 类，检查客户端是否提供了有效的 OAuth token。
以下是 UserAuthService 目前的工作方式：
<code_snippet> def issue_oauth_token():
….
</code_snippet>
以下是 requests-oauthlib 文档的路径：
<url> https://requests-oauthlib.readthedocs.io/en/ latest/
</url> themodernsoftware.dev

## Slide 18

反思（Reflexion）
- 
让大语言模型反思自己的输出
- 
来自环境信号的言语反馈，通过扩充上下文被重新纳入大语言模型
- 
在环境中采取行动并得到观察结果之后，追加一段提示词后缀：
- 
“Now critique your answer. Was it correct? If not, explain why and try again.”
- 
多轮提示
- 
第 1 轮：模型先试一次。
- 
第 2 轮：你问“
Was that correct? Reﬂect and revise if needed.
”
themodernsoftware.dev

## Slide 19

确保 company_location 列能处理字符串和 json 表示形式。
扩展 company_location 的逻辑，使其能处理字符串和 json 表示形式
company_location 类型的单元测试没有通过。
看起来 company_location 的单元测试抛出了 JSONDecodeError。
我正在扩展 company_location 列。
我必须确保当输入是字符串时不会抛出 JSONDecodeError。
observe reflect
扩展提示词 themodernsoftware.dev

## Slide 20

附加术语
- 
系统提示词
- 
提供给大语言模型的第一条消息（终端用户通常看不到）
- 
规定人设、关于大语言模型输出的规则、风格 themodernsoftware.dev

## Slide 21

themodernsoftware.dev
…

## Slide 22

themodernsoftware.dev
…

## Slide 23

附加术语
- 
用户提示词
- 
人类实际提出的请求或指令
- 
基本上就是到目前为止我们所有的例子
- 
助手
- 
大语言模型实际生成的内容 themodernsoftware.dev

## Slide 24

themodernsoftware.dev
系统提示词
用户提示词
助手提示词

## Slide 25

最佳实践
- 
提示词改进
- 
https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver
- 
清晰的提示词
- 
把提示词交给一个几乎不了解背景的人，如果他看不懂，大语言模型也看不懂
- 
大胆使用角色提示，让系统提示词更有威力 themodernsoftware.dev

## Slide 26

themodernsoftware.dev
你是一个乐于助人的助手，热爱编程，水平相当于资深软件开发者，回答非常细致甚至吹毛求疵。

## Slide 27

themodernsoftware.dev

## Slide 28

themodernsoftware.dev
你是一个 Z 世代的数字闺蜜。永远像凌晨两点在
Snapchat 上发消息那样说话。

## Slide 29

- 
提示词应结构化排版
最佳实践 themodernsoftware.dev
以下是日志：
<log>
LOG MESSAGE
<log> 以及堆栈跟踪：
<error>
STACK TRACE
<error>

## Slide 30

最佳实践
- 
明确说出你想要什么（语言、技术栈、库、约束）
- 
拆解任务 themodernsoftware.dev

## Slide 31

themodernsoftware.dev
有问题吗？
