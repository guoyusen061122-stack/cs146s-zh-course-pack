# 事故响应与 DevOps（fall2025 W9）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University, Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

themodernsoftware.dev
嘉宾讲座 - 11/21/25
Resolve
技术团队成员
Milind Ganjoo
Resolve
的 CTO
Mayank Agarwal

## Slide 3

AI DevOps themodernsoftware.dev

## Slide 4

- 
在生产环境中监控软件系统仍是一项关键任务
- 
编码只占工程时间的 30%
- 
更难的那 70% 是在生产环境中运行这些代码，那里复杂性、工具孤岛、知识缺口和相互依赖全都撞在一起
- 
管理生产环境往往需要由 SRE 完成的繁琐的软件分诊
为什么 themodernsoftware.dev

## Slide 5

themodernsoftware.dev

## Slide 6

旧世界
- 
SRE 的职责
- 
运维监控
■ 值班、故障排查、基础设施管理与安全
- 
解决事故需要把来自许多不同来源和团队的信息拼在一起
- 
维护用于解决问题的运行手册，而这些手册常常已经过时
- 
转向采用容器化工作负载和
Kubernetes 的云原生架构，带来了更多数据、依赖关系和跨系统的复杂性
- 
SRE 常常因值班班次而倦怠 themodernsoftware.dev

## Slide 7

基础设施与 DevOps 的原则
- 
监控的四个黄金信号
- 
延迟
- 
错误
- 
流量
■
每秒请求数
- 
饱和度
- 
监控生产环境的追踪（trace） themodernsoftware.dev

## Slide 8

themodernsoftware.dev
凌晨 3:12，你收到 PagerDuty 的告警，说数据库查询的 500 错误在激增。我们该怎么办？

## Slide 9

一套可能的应对手册
- 
确认并评估
- 
检查数据库 + 应用
- 
识别最近的改动
- 
定位影响范围
- 
执行缓解措施
- 
稳定并监控
- 
沟通
- 
记录 themodernsoftware.dev

## Slide 10

themodernsoftware.dev

## Slide 11

追踪的指标
- 
平均修复时间（MTTR）
- 
有多少工程师被拉进事故
- 
对客户承诺的 SLA themodernsoftware.dev

## Slide 12

新的 AI 世界
- 
Resolve AI
（嘉宾讲座 11/21）
- 
DataDog Bits AI Agent
- 
Splunk Observability Assistant themodernsoftware.dev

## Slide 13

AI SRE 的特征
- 
知识图谱的动态映射
- 
横跨可观测性技术栈与各云的智能体化的系统
- 
生成关于正在发生什么的实时叙述，结合支持性证据指出可能的根因，并给出有指导性的修复步骤建议
- 
高度重视预测/推理的可解释性与可审计性 themodernsoftware.dev

## Slide 14

themodernsoftware.dev

## Slide 15

发生了什么变化 themodernsoftware.dev
- 
AI 有望把组织层面的知识和服务层面的知识规模化铺开
- 
信息不再只掌握在少数工程师手里——只有他们知道那些未记录的依赖、脆弱的遗留服务，以及只在高风险事故中才暴露的怪癖。

## Slide 16

发生了什么变化 themodernsoftware.dev
- 
自动化缩短评审时间，并及早发现问题
- 
开发者通过 AI 建议学习最佳实践
- 
AI 在每次代码评审中应用同一套标准
- 
AI 处理例行检查，让人专注于复杂逻辑
- 
AI 系统随着数据增多而不断改进
- 
现代 AI 代码评审工具更深入，能提供上下文分析与模式识别

## Slide 17

来看看 AI SRE 的实际效果 themodernsoftware.dev

## Slide 18

局限 themodernsoftware.dev
- 
可解决事故的复杂程度
- 
现代生产环境技术栈的异构性
- 
基于检测结果修复实际代码的能力
- 
不过最终目标仍是如此，目前所有厂商都从根因分析做起
- 
好的根因分析需要好的监控打理
- 
安全可能成为新的攻击面

## Slide 19

themodernsoftware.dev
有问题吗？
