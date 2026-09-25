# 如何做一名智能体管理者（fall2025 W4）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University, Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

themodernsoftware.dev
嘉宾讲座 - 10/17/25
Anthropic
Claude Code
的创造者 Boris Cherny

## Slide 3

如何做一名智能体管理者 themodernsoftware.dev

## Slide 4

为什么
- 
开发的演进
- 
单个开发者管理单个开发者的产出
- 
主管管理许多开发者的产出
- 
主管管理许多开发者的产出（由 AI 系统辅助）
- 
单个开发者管理许多 AI 智能体的工作量 themodernsoftware.dev

## Slide 5

软件团队的简史 themodernsoftware.dev
软件团队成为主流，专业化分工出现
第一批软件团队出现，由 NASA、DoD 项目的需求驱动
1940
2030
2025
由开发者管理多类智能体团队的团队
2023
由 AI 编码系统辅助开发者的软件团队
1960
独立开发者独自承担完整项目
1970
1990

## Slide 6

目标 themodernsoftware.dev
….

## Slide 7

软件任务步骤 themodernsoftware.dev
- 
给出高层需求

- 
把需求转化为设计文档

/

- 
依据文档实现方案

- 
添加测试

- 
确保 CI（持续集成）通过

- 
代码评审

- 
更新文档

## Slide 8

指挥智能体的技巧 themodernsoftware.dev
- 
智能体行为文件（Claude.md/Cursorrules/agents.md）
- 
Hooks
- 
Commands
- 
子智能体

## Slide 9

Hooks
- 
在预定义事件类型上运行的确定性脚本
- 
PreToolUse
- 
PostToolUse
- 
UserPromptSubmit
- 
PreCompact
- 
……以及更多 themodernsoftware.dev

## Slide 10

Commands
- 
把常用提示词做成文件，供智能体执行
- 
用例
- 
运行测试
- 
评审代码
- 
形成一次 git 提交并推送 themodernsoftware.dev

## Slide 11

子智能体
- 
运行时委派
- 
子智能体的用途是
- 
为不同类型的工作（前端、后端等）创建不同的开发者角色
- 
为不同工作流干净地隔离上下文
- 
提供
- 
定制化的系统提示词、工具，以及独立的上下文窗口
- 
向着智能体管理其他智能体迈进
- 
用例
- 
https://github.com/vijaythecoder/awesome-claude-agents/blob/main/CLAUDE.md
- 
https://github.com/SuperClaude-Org/SuperClaude_Framework themodernsoftware.dev

## Slide 12

- 
你需要仔细设置兜底机制
- 
代码库中的测试
- 
CI/CD 最佳实践
- 
每个智能体的可审计性
- 
给智能体产生的每一处差异（diff）打标签
- 
不同类型任务使用不同模型
- 
越复杂的任务，越可能需要在前期多扶一把，而不像完全异步的任务那样
- 
定期设置检查点（提交） themodernsoftware.dev
最佳实践

## Slide 13

工作流走查 themodernsoftware.dev

## Slide 14

- 
如何把任何任务最初 10-20% 的研究阶段自动化？
- 
如何维护一个待办任务队列（对一次性改动更方便）？
themodernsoftware.dev
开放问题
