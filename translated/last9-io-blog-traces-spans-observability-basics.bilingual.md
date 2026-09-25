# Traces & Spans: Observability Basics You Should Know

# 追踪与跨度：你应该了解的可观测性基础

> Learn how traces and spans help you see inside distributed systems—so you can troubleshoot faster and build more reliable software.

> 了解追踪与跨度如何帮你看见分布式系统内部——从而更快排查问题，并构建更可靠的软件。

Source: https://last9.io/blog/traces-spans-observability-basics/

来源：https://last9.io/blog/traces-spans-observability-basics/

In modern software architecture, applications aren't just getting bigger—they're getting more distributed. With microservices, serverless functions, and containers running across multiple environments, understanding what's happening inside your systems can feel like trying to track a single raindrop in a storm.

在现代软件架构中，应用不只是变得更大——它们变得更加分布式。微服务、无服务器函数和容器跨多个环境运行，要理解系统内部正在发生什么，可能就像在暴风雨中追踪一滴雨。

That's where traces and spans come in. These observability tools aren't just buzzwords—they're your secret weapon for making sense of complex distributed systems. Let's break down what traces and spans are, why they matter, and how you can use them to troubleshoot faster and build more reliable systems.

这正是追踪与跨度登场的地方。这些可观测性工具不是流行词——它们是你读懂复杂分布式系统的秘密武器。我们来拆解追踪与跨度是什么、为什么重要，以及如何用它们更快排查问题、构建更可靠的系统。

## Understanding Traces and Spans: Core Concepts

## 理解追踪与跨度：核心概念

**Traces** capture the journey of a request as it moves through your distributed system. Think of a trace as the complete story of a request from start to finish—from when a user clicks a button until they see the result.

**追踪（trace）**记录一个请求在分布式系统中穿行的旅程。可以把一条追踪理解为某个请求从头到尾的完整故事——从用户点击按钮，到用户看到结果。

**Spans** are the building blocks of traces. Each span represents a unit of work within that journey—like a database query, an API call, or a function execution. Spans nest within each other to show parent-child relationships between operations.

**跨度（span）**是构成追踪的积木。每个跨度代表这段旅程中的一个工作单元——比如一次数据库查询、一次 API 调用或一次函数执行。跨度可以相互嵌套，以体现操作之间的父子关系。

Here's the relationship in simple terms:

用简单的话说，它们的关系是：

- A trace contains multiple spans
- Each span represents one operation
- Spans have timing data and metadata
- Spans can be nested to show how operations relate to each other

- 一条追踪包含多个跨度
- 每个跨度代表一个操作
- 跨度带有时间数据和元数据
- 跨度可以嵌套，以体现操作之间如何相互关联

```
Trace
├── Span (API Gateway)
│   ├── Span (Auth Service)
│   └── Span (User Service)
│       └── Span (Database Query)
└── Span (Response Formatting)
```

If you're curious how traces and spans fit alongside [metrics, logs, and events](https://last9.io/blog/understanding-metrics-events-logs-traces-key-pillars-of-observability/), this post breaks down all four.

如果你好奇追踪与跨度如何与[指标、日志和事件](https://last9.io/blog/understanding-metrics-events-logs-traces-key-pillars-of-observability/)并列，这篇文章把四者都拆解了。

## Benefits of Traces and Spans for DevOps Professionals

## 追踪与跨度对 DevOps 从业者的价值

You're running a complex system with dozens of microservices. Suddenly, users report the checkout process is slow. Without tracing, you'd need to check each service individually, wasting precious time.

你的系统很复杂，跑着几十个微服务。突然，用户反馈结账流程很慢。没有追踪，你就得逐个检查每个服务，白白浪费宝贵时间。

With traces and spans, you can:

有了追踪与跨度，你可以：

1. **Find bottlenecks instantly**: See exactly which service or function is taking too long
1. **Debug across service boundaries**: Follow requests as they jump between services
1. **Understand dependencies**: Visualize how your services connect and depend on each other
1. **Improve performance**: Identify and fix slow operations with precision
1. **Reduce mean time to recovery (MTTR)**: Get to the root cause faster when issues arise

1. **立刻找到瓶颈**：准确看出是哪个服务或函数耗时过长
1. **跨服务边界调试**：跟踪请求在服务之间跳转的过程
1. **理解依赖关系**：把服务之间如何连接与依赖可视化
1. **改进性能**：精准识别并修复缓慢的操作
1. **缩短平均恢复时间（MTTR）**：问题出现时更快找到根因

## Technical Implementation of Traces and Spans

## 追踪与跨度的技术实现

Let's get into the nuts and bolts of how tracing works in distributed systems.

我们来深入了解分布式系统中的追踪是如何工作的。

### Trace Context and Propagation

### 追踪上下文与传播

For tracing to work across service boundaries, each service needs to know it's handling part of the same request. This happens through **context propagation**—passing a trace ID and span ID between services.

要让追踪跨服务边界生效，每个服务都需要知道自己正在处理同一个请求的一部分。这通过**上下文传播**实现——在服务之间传递追踪 ID 和跨度 ID。

When a request first hits your system, it gets assigned a unique trace ID. As the request moves between services, this ID travels with it (usually as HTTP headers). Each service then creates its own spans but links them to the same trace.

请求首次到达你的系统时，会被分配一个唯一的追踪 ID。当请求在服务之间流转时，这个 ID 随之传递（通常放在 HTTP 头里）。每个服务随后创建自己的跨度，但都关联到同一条追踪。

### Span Attributes and Events

### 跨度属性与事件

Spans aren't just timestamps—they're rich with data:

跨度不只是时间戳——它们富含数据：

- **Name**: What operation this span represents
- **Timing**: Start and end times
- **Status**: Success, error, etc.
- **Attributes**: Custom key-value pairs (like `user_id` or `cart_size`)
- **Events**: Notable occurrences within the span
- **Links**: Connections to other spans

- **名称**：这个跨度代表什么操作
- **时间**：开始与结束时间
- **状态**：成功、错误等
- **属性**：自定义键值对（例如 `user_id` 或 `cart_size`）
- **事件**：跨度内值得注意的事件
- **链接**：与其他跨度的连接

### Sampling Strategies

### 采样策略

Tracing everything can create massive amounts of data. That's why most systems use sampling—collecting only a percentage of traces. Smart sampling strategies include:

对所有请求都做追踪会产生海量数据。因此大多数系统使用采样——只收集一定比例的追踪。聪明的采样策略包括：

- **Head-based sampling**: Decide whether to sample at the beginning of a request
- **Tail-based sampling**: Decide after the request completes (better for catching errors)
- **Priority sampling**: Always trace important operations, but sample routine ones

- **头部采样**：在请求开始时决定是否采样
- **尾部采样**：在请求结束后决定（更擅长捕获错误）
- **优先级采样**：始终追踪重要操作，常规操作则采样

If you're looking to understand the differences between observability, telemetry, and monitoring, check out this helpful post: [Observability vs Telemetry vs Monitoring](https://last9.io/blog/observability-vs-telemetry-vs-monitoring/).

如果你想了解可观测性、遥测和监控之间的区别，可以看看这篇文章：[可观测性 vs 遥测 vs 监控](https://last9.io/blog/observability-vs-telemetry-vs-monitoring/)。

## Tracing Implementation Guide: Tools and Frameworks

## 追踪实现指南：工具与框架

Ready to add tracing to your systems? Here's what you need:

准备好给系统加上追踪了吗？以下是你需要的东西：

### OpenTelemetry: The Industry Standard

### OpenTelemetry：行业标准

[OpenTelemetry](https://opentelemetry.io/) has become the go-to framework for implementing traces and spans. It provides:

[OpenTelemetry](https://opentelemetry.io/) 已经成为实现追踪与跨度的首选框架。它提供：

- Libraries for all major programming languages
- A vendor-neutral API and SDK
- Automatic instrumentation for popular frameworks
- A consistent way to collect and export data

- 覆盖所有主流编程语言的库
- 厂商中立的 API 与 SDK
- 对流行框架的自动埋点
- 一套一致的数据收集与导出方式

### The Tracing Toolbox

### 追踪工具箱

Several tools can help you collect, store, and visualize your traces:

有若干工具可以帮你收集、存储和可视化追踪：

| Tool | Type | Best For |
| --- | --- | --- |
| Last9 | All-in-one observability | Cost-effective, high-cardinality observability with predictable pricing |
| Jaeger | Open-source tracing | Self-hosted tracing visualization |
| Zipkin | Open-source tracing | Simple distributed tracing |
| Grafana Tempo | Tracing backend | Integration with Grafana dashboards |
| OpenTelemetry Collector | Data collection pipeline | Processing and routing telemetry data |

| 工具 | 类型 | 最适合 |
| --- | --- | --- |
| Last9 | 一体化可观测性 | 高性价比、可预测定价的高基数可观测性 |
| Jaeger | 开源追踪 | 自托管的追踪可视化 |
| Zipkin | 开源追踪 | 简单的分布式追踪 |
| Grafana Tempo | 追踪后端 | 与 Grafana 仪表板集成 |
| OpenTelemetry Collector | 数据收集流水线 | 处理并路由遥测数据 |

If you're after an observability solution that fits your budget, [Last9](https://last9.io/) is worth checking out. With pricing based on ingested events, it keeps things predictable. Plus, our platform handles high-cardinality data at scale and integrates with OpenTelemetry and Prometheus to bring your metrics, logs, and traces together in one place.

如果你在寻找一款符合预算的可观测性方案，[Last9](https://last9.io/) 值得一看。它按摄取事件计费，让成本保持可预测。此外，我们的平台能在规模上处理高基数数据，并与 OpenTelemetry 和 Prometheus 集成，把你的指标、日志和追踪汇集到一处。

### Implementing Tracing in Your Code

### 在代码中实现追踪

Here's a simplified example of how to create spans in a Node.js application using OpenTelemetry:

下面是一个简化示例，演示如何在 Node.js 应用中使用 OpenTelemetry 创建跨度：

```javascript
// Initialize the OpenTelemetry SDK (once in your app)
const { NodeTracerProvider } = require("@opentelemetry/sdk-trace-node");
const { SimpleSpanProcessor } = require("@opentelemetry/sdk-trace-base");
const {
  OTLPTraceExporter,
} = require("@opentelemetry/exporter-trace-otlp-http");

const provider = new NodeTracerProvider();
const exporter = new OTLPTraceExporter({
  url: "http://localhost:4318/v1/traces",
});
provider.addSpanProcessor(new SimpleSpanProcessor(exporter));
provider.register();

// Get a tracer
const { trace } = require("@opentelemetry/api");
const tracer = trace.getTracer("my-service");

// Create spans in your code
async function processOrder(orderId) {
  const span = tracer.startSpan("process-order");

  // Add attributes to the span
  span.setAttribute("order.id", orderId);
  span.setAttribute("customer.type", "premium");

  try {
    // Do work...

    // Create a child span
    const dbSpan = tracer.startSpan("database-query", {
      parent: span,
    });

    try {
      // Run database query...
      dbSpan.end();
    } catch (error) {
      dbSpan.setStatus({ code: SpanStatusCode.ERROR });
      dbSpan.recordException(error);
      dbSpan.end();
      throw error;
    }

    span.end();
  } catch (error) {
    span.setStatus({ code: SpanStatusCode.ERROR });
    span.recordException(error);
    span.end();
    throw error;
  }
}
```

Wondering how OpenTelemetry stacks up against traditional APM tools? This post breaks down the key differences: [OpenTelemetry vs Traditional APM Tools](https://last9.io/blog/opentelemetry-vs-traditional-apm-tools/).

想知道 OpenTelemetry 与传统 APM 工具相比如何？这篇文章拆解了关键差异：[OpenTelemetry vs 传统 APM 工具](https://last9.io/blog/opentelemetry-vs-traditional-apm-tools/)。

## Advanced Tracing Techniques

## 进阶追踪技术

Once you've got basic tracing in place, these advanced techniques can take your observability to the next level.

基础追踪就位之后，这些进阶技术可以把你的可观测性提到另一个层次。

### Distributed Context Management

### 分布式上下文管理

In complex systems, you need to manage context beyond just trace IDs. The W3C Trace Context specification provides standards for:

在复杂系统中，你需要管理的不只是追踪 ID。W3C Trace Context 规范为以下内容提供了标准：

- **traceparent**: Contains the trace ID and parent span ID
- **tracestate**: Allows vendors to add custom context data

- **traceparent**：包含追踪 ID 和父跨度 ID
- **tracestate**：允许厂商添加自定义上下文数据

Using these headers ensures your tracing works across different services and vendors.

使用这些头部可以确保你的追踪在不同服务和厂商之间都能正常工作。

### Correlation Between Traces, Metrics, and Logs

### 追踪、指标与日志之间的关联

The real power of observability comes from connecting different signals:

可观测性真正的威力来自把不同信号连接起来：

- **Exemplar traces**: Link metrics to the traces that generated them
- **Trace IDs in logs**: Add trace IDs to log messages for cross-referencing
- **Custom attributes**: Use consistent attributes across all telemetry types

- **样例追踪**：把指标链接到产生它们的追踪
- **日志中的追踪 ID**：在日志消息里加上追踪 ID，便于交叉引用
- **自定义属性**：在所有遥测类型中使用一致的属性

### Error Handling and Exception Tracking

### 错误处理与异常跟踪

When exceptions occur, spans can provide crucial context:

异常发生时，跨度可以提供关键上下文：

- Mark spans with error status
- Record exceptions with stack traces
- Add events to spans that show the error's progression
- Create baggage items that carry error context across service boundaries

- 给跨度标记错误状态
- 记录异常及其堆栈跟踪
- 向跨度添加事件，展示错误的演变过程
- 创建 baggage 条目，让错误上下文跨服务边界传递

For a deeper look at staying ahead of issues and improving system reliability, check out this post on proactive monitoring: [Proactive Monitoring](https://last9.io/blog/proactive-monitoring/).

想更深入了解如何提前发现问题、提升系统可靠性，可以看看这篇关于主动监控的文章：[主动监控](https://last9.io/blog/proactive-monitoring/)。

## Real-World Tracing Patterns and Anti-Patterns

## 真实世界的追踪模式与反模式

### Effective Tracing Patterns

### 有效的追踪模式

**Meaningful span names**: Use consistent naming conventions like `service_name/operation` **Right granularity**: Create spans for significant operations, not every function call **Proper context propagation**: Ensure trace context flows through all communication channels **Useful attributes**: Add attributes that help with troubleshooting, like user IDs or feature flags **Performance awareness**: Watch out for the overhead of excessive span creation

**有意义的跨度名称**：使用 `service_name/operation` 这样一致的命名约定 **合适的粒度**：为重要操作创建跨度，而不是每次函数调用都建 **正确的上下文传播**：确保追踪上下文流经所有通信通道 **有用的属性**：添加有助于排查问题的属性，比如用户 ID 或功能开关 **关注性能开销**：留意创建过多跨度带来的开销

### Tracing Anti-Patterns to Avoid

### 应避免的追踪反模式

**Over-instrumentation**: Creating too many spans can cause performance issues **Missing context**: Failing to propagate context breaks traces across service boundaries **Inconsistent naming**: Using different naming standards makes traces harder to interpret **Too much data**: Putting large payloads in spans can overwhelm your tracing backend **Ignoring third-party services**: Missing spans for external calls creates blind spots

**埋点过度**：创建太多跨度会导致性能问题 **丢失上下文**：未能传播上下文会让追踪在服务边界处断开 **命名不一致**：使用不同的命名标准会让追踪更难解读 **数据过多**：把大体积载荷放进跨度会压垮追踪后端 **忽视第三方服务**：缺少外部调用的跨度会形成盲区

Explore how observability is central to the performance and reliability of LLMs: [LLM Observability](https://last9.io/blog/llm-observability/).

探索可观测性为何是 LLM 性能与可靠性的核心：[LLM 可观测性](https://last9.io/blog/llm-observability/)。

## Business Value of Traces and Spans: Beyond Technical Benefits

## 追踪与跨度的业务价值：超越技术收益

Traces aren't just for troubleshooting—they can provide business insights too:

追踪不只是用来排查问题——它们也能带来业务洞察：

- Track critical user journeys from end-to-end
- Measure the performance of key business operations
- Set SLOs (Service Level Objectives) based on trace data
- Quantify the cost of performance issues in real user terms
- Create business context by adding relevant attributes to spans

- 端到端追踪关键用户旅程
- 衡量关键业务操作的性能
- 基于追踪数据设定 SLO（服务级别目标）
- 用真实用户的语言量化性能问题的代价
- 通过给跨度添加相关属性来构建业务上下文

When you can show how technical improvements affect user experience and business metrics, you bridge the gap between DevOps and business stakeholders.

当你能展示技术改进如何影响用户体验和业务指标时，你就在 DevOps 与业务相关方之间架起了桥梁。

## Conclusion

## 结论

Traces and spans give you X-ray vision into your distributed systems. They reveal the hidden connections between services, pinpoint performance bottlenecks, and dramatically speed up debugging.

追踪与跨度为你提供了透视分布式系统的 X 光视野。它们揭示服务之间隐藏的连接，精准定位性能瓶颈，并大幅加快调试速度。

As systems grow more complex, this kind of observability isn't a luxury—it's essential.

随着系统变得愈发复杂，这类可观测性不是奢侈品——而是必需品。

If you'd like to continue the conversation about distributed tracing and observability, join our [Discord Community](https://discord.com/invite/W8gMppQC4b) where DevOps professionals share their experiences and best practices!

如果你想继续讨论分布式追踪与可观测性，欢迎加入我们的 [Discord 社区](https://discord.com/invite/W8gMppQC4b)，DevOps 从业者在那里分享经验与最佳实践！

## FAQs

## 常见问题

### What's the difference between tracing and logging?

### 追踪与日志有什么区别？

Logging captures discrete events, while tracing shows the relationships between operations across services. Logs tell you what happened; traces show you how it happened.

日志记录离散事件，而追踪展示跨服务的操作之间的关系。日志告诉你发生了什么；追踪告诉你它是如何发生的。

### Will adding tracing slow down my application?

### 加上追踪会让我的应用变慢吗？

Modern tracing libraries add minimal overhead — typically less than 3% performance impact when properly configured. With sampling, you can further reduce this impact.

现代追踪库带来的开销极小——配置得当的情况下，性能影响通常低于 3%。通过采样，你还可以进一步降低这种影响。

### Do I need to modify all my code to add tracing?

### 我需要改所有代码才能加上追踪吗？

Not necessarily. Many frameworks offer automatic instrumentation that adds tracing with minimal code changes. OpenTelemetry provides auto-instrumentation for popular frameworks in most languages.

不一定。许多框架提供自动埋点，只需很少的代码改动就能加上追踪。OpenTelemetry 为大多数主流语言中的流行框架提供了自动埋点。

### How much data does distributed tracing generate?

### 分布式追踪会产生多大数据量？

It varies widely based on traffic, sampling rate, and span detail. Plan for anywhere from gigabytes to terabytes per day for busy systems. Choosing the right observability platform is what keeps that cost under control.

这取决于流量、采样率和跨度细节，差异很大。对于繁忙的系统，可以按每天几 GB 到几 TB 来规划。选择合适的可观测性平台，才能把这项成本控制住。

### Can traces help with security and compliance?

### 追踪能帮助满足安全与合规要求吗？

Yes! Traces create an audit trail of request flow through your system. With the right attributes, you can track which users or services accessed what data and when.

可以！追踪为请求在系统中流转的过程留下审计轨迹。配合合适的属性，你可以追踪哪些用户或服务在什么时间访问了哪些数据。

### How do traces and spans fit with other observability signals?

### 追踪与跨度如何与其他可观测性信号配合？

Traces complement metrics and logs. Metrics show system health at a high level, logs provide detailed events, and traces connect the dots to show request flows across services.

追踪与指标、日志互补。指标在高层展示系统健康状况，日志提供详细事件，而追踪把各个点连起来，展示跨服务的请求流转。
