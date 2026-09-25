# Incident response and DevOps（fall2025 W9）

# 事故响应与 DevOps（fall2025 W9）

## Slide 1

## Slide 1

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

The Modern Software Developer CS146S Stanford University, Fall 2025 Mihail Eric themodernsoftware.dev

## Slide 2

## Slide 2

themodernsoftware.dev Guest Lecture - 11/21/25 Member of Technical Staff Resolve Milind Ganjoo CTO of Resolve Mayank Agarwal

themodernsoftware.dev 嘉宾讲座 - 11/21/25 Resolve 技术团队成员 Milind Ganjoo Resolve 的 CTO Mayank Agarwal

## Slide 3

## Slide 3

AI DevOps themodernsoftware.dev

AI DevOps themodernsoftware.dev

## Slide 4

## Slide 4

- 

- 

Monitoring software systems in production remains a mission-critical task

在生产环境中监控软件系统仍是一项关键任务

- 

- 

Coding represents just 30 percent of engineering time

编码只占工程时间的 30%

- 

- 

Harder 70 percent is running that code in production where complexity, tool silos, knowledge gaps, and interdependencies all collide

更难的那 70% 是在生产环境中运行这些代码，那里复杂性、工具孤岛、知识缺口和相互依赖全都撞在一起

- 

- 

Managing production often requires laborious software triaging handled by SREs Why themodernsoftware.dev

管理生产环境往往需要由 SRE 完成的繁琐的软件分诊 为什么 themodernsoftware.dev

## Slide 5

## Slide 5

themodernsoftware.dev

themodernsoftware.dev

## Slide 6

## Slide 6

The Old World

旧世界

- 

- 

Responsibilities of SRE

SRE 的职责

- 

- 

Operational monitoring ■ on-call, troubleshooting, infrastructure management and security

运维监控 ■ 值班、故障排查、基础设施管理与安全

- 

- 

Incident resolution involves piecing together info from many different sources and teams

解决事故需要把来自许多不同来源和团队的信息拼在一起

- 

- 

Maintain oftentimes outdated runbooks for how to resolve issues

维护用于解决问题的运行手册，而这些手册常常已经过时

- 

- 

Shift to cloud-native architectures with containerized workloads and Kubernetes has introduced more data, dependencies, and complexity across systems

转向采用容器化工作负载和 Kubernetes 的云原生架构，带来了更多数据、依赖关系和跨系统的复杂性

- 

- 

SREs often get burned out due to on-call shifts themodernsoftware.dev

SRE 常常因值班班次而倦怠 themodernsoftware.dev

## Slide 7

## Slide 7

Principles of Infrastructure and DevOps

基础设施与 DevOps 的原则

- 

- 

Four golden signals of monitoring

监控的四个黄金信号

- 

- 

Latency

延迟

- 

- 

Errors

错误

- 

- 

Traﬃc ■ Requests/sec

流量 ■ 每秒请求数

- 

- 

Saturation

饱和度

- 

- 

Monitor production traces themodernsoftware.dev

监控生产环境的追踪（trace） themodernsoftware.dev

## Slide 8

## Slide 8

themodernsoftware.dev At 3:12 am you get a ping from PagerDuty that you’re seeing a spike in 500s on your database queries. What do we do?

themodernsoftware.dev 凌晨 3:12，你收到 PagerDuty 的告警，说数据库查询的 500 错误在激增。我们该怎么办？

## Slide 9

## Slide 9

A Potential Playbook

一套可能的应对手册

- 

- 

Acknowledge and assess

确认并评估

- 

- 

Check DB + app

检查数据库 + 应用

- 

- 

Identify recent changes

识别最近的改动

- 

- 

Localize blast radius

定位影响范围

- 

- 

Execute mitigations

执行缓解措施

- 

- 

Stabilize + monitor

稳定并监控

- 

- 

Communicate

沟通

- 

- 

Document themodernsoftware.dev

记录 themodernsoftware.dev

## Slide 10

## Slide 10

themodernsoftware.dev

themodernsoftware.dev

## Slide 11

## Slide 11

Metrics Tracked

追踪的指标

- 

- 

Mean-time-to-repair (MTTR)

平均修复时间（MTTR）

- 

- 

How many engineers are pulled into incident

有多少工程师被拉进事故

- 

- 

Reported SLA for customers themodernsoftware.dev

对客户承诺的 SLA themodernsoftware.dev

## Slide 12

## Slide 12

The New AI World

新的 AI 世界

- 

- 

Resolve AI (guest lecture 11/21)

Resolve AI （嘉宾讲座 11/21）

- 

- 

DataDog Bits AI Agent

DataDog Bits AI Agent

- 

- 

Splunk Observability Assistant themodernsoftware.dev

Splunk Observability Assistant themodernsoftware.dev

## Slide 13

## Slide 13

Characteristics of an AI SRE

AI SRE 的特征

- 

- 

Dynamic mapping of a knowledge graph

知识图谱的动态映射

- 

- 

Agentic system across observability stack and clouds

横跨可观测性技术栈与各云的智能体化的系统

- 

- 

Generates real-time narratives of what is happening, pinpoints likely root causes with supporting evidence, and recommends prescriptive remediation steps

生成关于正在发生什么的实时叙述，结合支持性证据指出可能的根因，并给出有指导性的修复步骤建议

- 

- 

Heavy emphasis on explainability and auditability of predictions/reasoning themodernsoftware.dev

高度重视预测/推理的可解释性与可审计性 themodernsoftware.dev

## Slide 14

## Slide 14

themodernsoftware.dev

themodernsoftware.dev

## Slide 15

## Slide 15

What Has Changed themodernsoftware.dev

发生了什么变化 themodernsoftware.dev

- 

- 

AI promises to scale out organizational and service level knowledge

AI 有望把组织层面的知识和服务层面的知识规模化铺开

- 

- 

Information is not siloed to the only engineers who know the undocumented dependencies, brittle legacy services, and quirks that only surface during high-stakes incidents.

信息不再只掌握在少数工程师手里——只有他们知道那些未记录的依赖、脆弱的遗留服务，以及只在高风险事故中才暴露的怪癖。

## Slide 16

## Slide 16

What Has Changed themodernsoftware.dev

发生了什么变化 themodernsoftware.dev

- 

- 

Automation reduces review time and catches issues early

自动化缩短评审时间，并及早发现问题

- 

- 

Developers learn best practices through AI suggestions

开发者通过 AI 建议学习最佳实践

- 

- 

AI applies the same standards across all code reviews

AI 在每次代码评审中应用同一套标准

- 

- 

AI handles routine checks, letting humans focus on complex logic

AI 处理例行检查，让人专注于复杂逻辑

- 

- 

AI systems improve over time with more data

AI 系统随着数据增多而不断改进

- 

- 

modern AI code review tools go deeper, offering contextual analysis and pattern recognition

现代 AI 代码评审工具更深入，能提供上下文分析与模式识别

## Slide 17

## Slide 17

Let’s See AI SRE in Action themodernsoftware.dev

来看看 AI SRE 的实际效果 themodernsoftware.dev

## Slide 18

## Slide 18

Limitations themodernsoftware.dev

局限 themodernsoftware.dev

- 

- 

Complexity of incidents that can be resolved

可解决事故的复杂程度

- 

- 

Heterogeneity of modern production stacks

现代生产环境技术栈的异构性

- 

- 

Ability to remediate actual code based on what has been detected

基于检测结果修复实际代码的能力

- 

- 

Eventual goal though all providers are starting with root cause analysis

不过最终目标仍是如此，目前所有厂商都从根因分析做起

- 

- 

Good root cause analysis requires good monitoring gardening

好的根因分析需要好的监控打理

- 

- 

Security could be a new attack vector

安全可能成为新的攻击面

## Slide 19

## Slide 19

themodernsoftware.dev Questions?

themodernsoftware.dev 有问题吗？
