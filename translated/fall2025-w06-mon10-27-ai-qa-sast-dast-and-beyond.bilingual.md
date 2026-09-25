# AI QA, SAST, DAST, and Beyond（fall2025 W6）

# AI QA, SAST, DAST, and Beyond（fall2025 W6）

## Slide 1

## Slide 1

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

The Modern Software Developer CS146S Stanford University，Fall 2025 Mihail Eric themodernsoftware.dev

## Slide 2

## Slide 2

themodernsoftware.dev Guest Lecture - 10/31/25 CEO of Semgrep , Isaac Evans

themodernsoftware.dev 客座讲座 - 10/31/25 CEO of Semgrep ，Isaac Evans

## Slide 3

## Slide 3

AI Testing and Security themodernsoftware.dev

AI 测试与安全 themodernsoftware.dev

## Slide 4

## Slide 4

- 

- 

Software errors can dash user trust in a product/company and incur huge ﬁnancial costs

软件错误会动摇用户对产品/公司的信任，并带来巨额财务成本

- 

- 

When an LLM is writing most of your code, you need extensive guardrails to prevent those errors Why themodernsoftware.dev

当大部分代码由大语言模型编写时，你需要大量护栏来防止这些错误 Why themodernsoftware.dev

## Slide 5

## Slide 5

Existing threat landscape

现有威胁全景

- 

- 

SQL injections

SQL 注入

- 

- 

Cross-site scripting

跨站脚本

- 

- 

Broken authentication

失效的身份认证

- 

- 

Insecure direct object references

不安全的直接对象引用

- 

- 

Security misconﬁgurations

安全配置错误

- 

- 

Sensitive data exposure themodernsoftware.dev

敏感数据泄露 themodernsoftware.dev

## Slide 6

## Slide 6

Vulnerability detection techniques

漏洞检测技术

- 

- 

SAST

SAST

- 

- 

DAST

DAST

- 

- 

SCA themodernsoftware.dev

SCA themodernsoftware.dev

## Slide 7

## Slide 7

SAST

SAST

- 

- 

S tatic A pplication S ecurity T esting

S tatic A pplication S ecurity T esting

- 

- 

White box testing technique

白盒测试技术

- 

- 

Analyzes binaries and source code

分析二进制文件与源代码

- 

- 

Happens early in software development life cycle when much cheaper to identify and correct

发生在软件开发生命周期早期，此时发现并修正的成本低得多

- 

- 

Identify vulnerabilities like SQL injections, command injections, cross-site scripting

识别 SQL 注入、命令注入、跨站脚本等漏洞

- 

- 

Techniques

技术手段

- 

- 

Codebase scan with pattern matching themodernsoftware.dev

用模式匹配扫描代码库 themodernsoftware.dev

## Slide 8

## Slide 8

DAST

DAST

- 

- 

D ynamic A pplication S ecurity T esting

D ynamic A pplication S ecurity T esting

- 

- 

Black box testing technique

黑盒测试技术

- 

- 

Mimic actions of real-world hackers to uncover vulnerabilities

模拟真实世界黑客的行为来发现漏洞

- 

- 

Can happen throughout SDLC and offers fewer false positives

可在整个 SDLC 中执行，误报更少

- 

- 

Identify vulnerabilities like SQL injections, broken authentication, cross-site scripting

识别 SQL 注入、失效的身份认证、跨站脚本等漏洞

- 

- 

Techniques

技术手段

- 

- 

Input fuzzing

输入模糊测试

- 

- 

Manipulating session tokens

操纵会话 token

- 

- 

Conﬁguration/header testing

配置/请求头测试

- 

- 

Brute force rate-limit tests themodernsoftware.dev

暴力破解限流测试 themodernsoftware.dev

## Slide 9

## Slide 9

SCA

SCA

- 

- 

S oftware C omposition A nalysis

S oftware C omposition A nalysis

- 

- 

Deep analysis of OSS packages used by application

深入分析应用所用的开源软件包

- 

- 

Perform analysis of package managers, infrastructure-as-code, pull images to ﬁnd vulnerabilities

分析包管理器、基础设施即代码，拉取镜像以发现漏洞

- 

- 

Techniques

技术手段

- 

- 

Analyze package metadata for dependencies

分析包元数据以获取依赖关系

- 

- 

Transitive dependency resolution

传递依赖解析

- 

- 

Match against DB of vulnerabilities

与漏洞数据库比对

- 

- 

Binary/artifact scanning themodernsoftware.dev

二进制/制品扫描 themodernsoftware.dev

## Slide 10

## Slide 10

What has changed themodernsoftware.dev

发生了什么变化 themodernsoftware.dev

- 

- 

Bad: new AI agent attack vectors

坏消息：新的 AI 智能体攻击向量

- 

- 

Good: new techniques for improving SAST/DAST/SCA

好消息：改进 SAST/DAST/SCA 的新技术

## Slide 11

## Slide 11

New AI agent attack vectors themodernsoftware.dev

新的 AI 智能体攻击向量 themodernsoftware.dev

- 

- 

Prompt injection

提示注入

- 

- 

Hidden or misleading instructions to gen AI system to make it deviate from intended behavior

向生成式 AI 系统隐藏或误导性地下达指令，使其偏离预期行为

## Slide 12

## Slide 12

themodernsoftware.dev

themodernsoftware.dev

## Slide 13

## Slide 13

themodernsoftware.dev

themodernsoftware.dev

## Slide 14

## Slide 14

New AI agent attack vectors themodernsoftware.dev

新的 AI 智能体攻击向量 themodernsoftware.dev

- 

- 

Tool misuse

工具滥用

- 

- 

Manipulate agent through deceptive prompts to abuse its integrated tools

用欺骗性提示词操纵智能体，滥用其集成的工具

## Slide 15

## Slide 15

themodernsoftware.dev

themodernsoftware.dev

## Slide 16

## Slide 16

New AI agent attack vectors themodernsoftware.dev

新的 AI 智能体攻击向量 themodernsoftware.dev

- 

- 

Code attacks

代码攻击

- 

- 

Exploit agent’s ability to execute code to gain unauthorized access to execution environment

利用智能体执行代码的能力，未授权访问其执行环境

## Slide 17

## Slide 17

themodernsoftware.dev

themodernsoftware.dev

## Slide 18

## Slide 18

New AI agent attack vectors themodernsoftware.dev

新的 AI 智能体攻击向量 themodernsoftware.dev

- 

- 

Prompt injection

提示注入

- 

- 

Hidden or misleading instructions to gen AI system to make it deviate from intended behavior

向生成式 AI 系统隐藏或误导性地下达指令，使其偏离预期行为

- 

- 

Tool misuse

工具滥用

- 

- 

Manipulate agent through deceptive prompts to abuse its integrated tools

用欺骗性提示词操纵智能体，滥用其集成的工具

- 

- 

Intent breaking

意图破坏

- 

- 

Manipulate agent’s plan to redirect actions away from original intent

操纵智能体的计划，把行动导向原始意图之外

- 

- 

Identity spooﬁng

身份欺骗

- 

- 

Exploit compromised authentication to pose as legitimate agents

利用被攻陷的身份认证，冒充合法智能体

- 

- 

Code attacks

代码攻击

- 

- 

Exploit agent’s ability to execute code to gain unauthorized access to execution environment

利用智能体执行代码的能力，未授权访问其执行环境

## Slide 19

## Slide 19

What has changed themodernsoftware.dev

发生了什么变化 themodernsoftware.dev

- 

- 

“Shift left” security is more accessible than ever

「左移」安全比以往任何时候都更容易落地

- 

- 

LLMs can be introduced in a workﬂow to spot issues

可以把大语言模型引入工作流来发现问题

- 

- 

Automated penetration testing

自动化渗透测试

## Slide 20

## Slide 20

How LLMs are used for security and testing themodernsoftware.dev

大语言模型如何用于安全与测试 themodernsoftware.dev

## Slide 21

## Slide 21

Limitations themodernsoftware.dev

局限 themodernsoftware.dev

- 

- 

In AI SAST, false positive rates are incredibly high

在 AI SAST 中，误报率高得惊人

- 

- 

Claude Code/Codex can be 50-100% depending on the vulnerability

视漏洞类型而定，Claude Code/Codex 可达 50-100%

- 

- 

Compare to 50+% for traditional SAST techniques

相比之下，传统 SAST 技术为 50% 以上

- 

- 

Existing benchmarks are often unrealistic so hard to evaluate LLM

现有基准测试往往不切实际，难以评测大语言模型

- 

- 

Nondeterministic analysis

非确定性分析

- 

- 

Run the same prompt multiple times and get different results → how do you know you’re catching all vulnerabilities?

同一个提示词跑多次会得到不同结果 → 你怎么知道所有漏洞都被抓到了？

- 

- 

Context rot ■ Not all context is created equally

上下文腐化 ■ 并非所有上下文都是等价的

- 

- 

Compaction ■ Summarize so that things ﬁt into context

压缩 ■ 做摘要，让内容塞得进上下文

## Slide 22

## Slide 22

Open Questions themodernsoftware.dev

开放问题 themodernsoftware.dev

- 

- 

How to reduce false positives and hallucinations in vulnerability detection?

如何降低漏洞检测中的误报与幻觉？

- 

- 

How do we verify that LLM-generated patches are secure and don’t introduce regressions?

如何验证大语言模型生成的补丁是安全的，且没有引入回归？

- 

- 

How can LLMs explain why they ﬂag a vulnerability or propose a ﬁx?

大语言模型如何解释自己为何标记某个漏洞或提出某个修复？

- 

- 

What are the right benchmarks for measuring LLMs’ AppSec performance?

衡量大语言模型 AppSec 表现的合适基准测试是什么？

- 

- 

How should LLMs be embedded in CI/CD without overwhelming teams with noise?

大语言模型应如何嵌入 CI/CD，才不会用噪声淹没团队？

- 

- 

Who is accountable if an AI-generated patch introduces a vulnerability?

如果 AI 生成的补丁引入了漏洞，责任由谁承担？
