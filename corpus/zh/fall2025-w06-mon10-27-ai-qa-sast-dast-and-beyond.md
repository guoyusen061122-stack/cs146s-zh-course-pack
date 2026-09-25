# AI QA, SAST, DAST, and Beyond（fall2025 W6）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University，Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

themodernsoftware.dev
客座讲座 - 10/31/25
CEO of
Semgrep
，Isaac Evans

## Slide 3

AI 测试与安全 themodernsoftware.dev

## Slide 4

- 
软件错误会动摇用户对产品/公司的信任，并带来巨额财务成本
- 
当大部分代码由大语言模型编写时，你需要大量护栏来防止这些错误
Why themodernsoftware.dev

## Slide 5

现有威胁全景
- 
SQL 注入
- 
跨站脚本
- 
失效的身份认证
- 
不安全的直接对象引用
- 
安全配置错误
- 
敏感数据泄露 themodernsoftware.dev

## Slide 6

漏洞检测技术
- 
SAST
- 
DAST
- 
SCA themodernsoftware.dev

## Slide 7

SAST
- 
S tatic
A pplication
S ecurity
T esting
- 
白盒测试技术
- 
分析二进制文件与源代码
- 
发生在软件开发生命周期早期，此时发现并修正的成本低得多
- 
识别 SQL 注入、命令注入、跨站脚本等漏洞
- 
技术手段
- 
用模式匹配扫描代码库 themodernsoftware.dev

## Slide 8

DAST
- 
D ynamic
A pplication
S ecurity
T esting
- 
黑盒测试技术
- 
模拟真实世界黑客的行为来发现漏洞
- 
可在整个 SDLC 中执行，误报更少
- 
识别 SQL 注入、失效的身份认证、跨站脚本等漏洞
- 
技术手段
- 
输入模糊测试
- 
操纵会话 token
- 
配置/请求头测试
- 
暴力破解限流测试 themodernsoftware.dev

## Slide 9

SCA
- 
S oftware
C omposition
A nalysis
- 
深入分析应用所用的开源软件包
- 
分析包管理器、基础设施即代码，拉取镜像以发现漏洞
- 
技术手段
- 
分析包元数据以获取依赖关系
- 
传递依赖解析
- 
与漏洞数据库比对
- 
二进制/制品扫描 themodernsoftware.dev

## Slide 10

发生了什么变化 themodernsoftware.dev
- 
坏消息：新的 AI 智能体攻击向量
- 
好消息：改进 SAST/DAST/SCA 的新技术

## Slide 11

新的 AI 智能体攻击向量 themodernsoftware.dev
- 
提示注入
- 
向生成式 AI 系统隐藏或误导性地下达指令，使其偏离预期行为

## Slide 12

themodernsoftware.dev

## Slide 13

themodernsoftware.dev

## Slide 14

新的 AI 智能体攻击向量 themodernsoftware.dev
- 
工具滥用
- 
用欺骗性提示词操纵智能体，滥用其集成的工具

## Slide 15

themodernsoftware.dev

## Slide 16

新的 AI 智能体攻击向量 themodernsoftware.dev
- 
代码攻击
- 
利用智能体执行代码的能力，未授权访问其执行环境

## Slide 17

themodernsoftware.dev

## Slide 18

新的 AI 智能体攻击向量 themodernsoftware.dev
- 
提示注入
- 
向生成式 AI 系统隐藏或误导性地下达指令，使其偏离预期行为
- 
工具滥用
- 
用欺骗性提示词操纵智能体，滥用其集成的工具
- 
意图破坏
- 
操纵智能体的计划，把行动导向原始意图之外
- 
身份欺骗
- 
利用被攻陷的身份认证，冒充合法智能体
- 
代码攻击
- 
利用智能体执行代码的能力，未授权访问其执行环境

## Slide 19

发生了什么变化 themodernsoftware.dev
- 
「左移」安全比以往任何时候都更容易落地
- 
可以把大语言模型引入工作流来发现问题
- 
自动化渗透测试

## Slide 20

大语言模型如何用于安全与测试 themodernsoftware.dev

## Slide 21

局限 themodernsoftware.dev
- 
在 AI SAST 中，误报率高得惊人
- 
视漏洞类型而定，Claude Code/Codex 可达 50-100%
- 
相比之下，传统 SAST 技术为 50% 以上
- 
现有基准测试往往不切实际，难以评测大语言模型
- 
非确定性分析
- 
同一个提示词跑多次会得到不同结果
→ 你怎么知道所有漏洞都被抓到了？
- 
上下文腐化
■
并非所有上下文都是等价的
- 
压缩
■
做摘要，让内容塞得进上下文

## Slide 22

开放问题 themodernsoftware.dev
- 
如何降低漏洞检测中的误报与幻觉？
- 
如何验证大语言模型生成的补丁是安全的，且没有引入回归？
- 
大语言模型如何解释自己为何标记某个漏洞或提出某个修复？
- 
衡量大语言模型 AppSec 表现的合适基准测试是什么？
- 
大语言模型应如何嵌入 CI/CD，才不会用噪声淹没团队？
- 
如果 AI 生成的补丁引入了漏洞，责任由谁承担？
