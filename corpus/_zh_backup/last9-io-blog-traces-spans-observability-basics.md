# 追踪与跨度：你应该了解的可观测性基础

> 了解追踪与跨度如何帮你看见分布式系统内部——从而更快排查问题，并构建更可靠的软件。


来源：https://last9.io/blog/traces-spans-observability-basics/

在现代软件架构中，应用不只是变得更大——它们变得更加分布式。微服务、无服务器函数和容器跨多个环境运行，要理解系统内部正在发生什么，可能就像在暴风雨中追踪一滴雨。

这正是追踪与跨度登场的地方。这些可观测性工具不是流行词——它们是你读懂复杂分布式系统的秘密武器。我们来拆解追踪与跨度是什么、为什么重要，以及如何用它们更快排查问题、构建更可靠的系统。

## 理解追踪与跨度：核心概念

**追踪（trace）**记录一个请求在分布式系统中穿行的旅程。可以把一条追踪理解为某个请求从头到尾的完整故事——从用户点击按钮，到用户看到结果。

**跨度（span）**是构成追踪的积木。每个跨度代表这段旅程中的一个工作单元——比如一次数据库查询、一次 API 调用或一次函数执行。跨度可以相互嵌套，以体现操作之间的父子关系。

用简单的话说，它们的关系是：

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

如果你好奇追踪与跨度如何与[指标、日志和事件](https://last9.io/blog/understanding-metrics-events-logs-traces-key-pillars-of-observability/)并列，这篇文章把四者都拆解了。

## 追踪与跨度对 DevOps 从业者的价值

你的系统很复杂，跑着几十个微服务。突然，用户反馈结账流程很慢。没有追踪，你就得逐个检查每个服务，白白浪费宝贵时间。

有了追踪与跨度，你可以：

1. **立刻找到瓶颈**：准确看出是哪个服务或函数耗时过长
2. **跨服务边界调试**：跟踪请求在服务之间跳转的过程
3. **理解依赖关系**：把服务之间如何连接与依赖可视化
4. **改进性能**：精准识别并修复缓慢的操作
5. **缩短平均恢复时间（MTTR）**：问题出现时更快找到根因

## 追踪与跨度的技术实现

我们来深入了解分布式系统中的追踪是如何工作的。

### 追踪上下文与传播

要让追踪跨服务边界生效，每个服务都需要知道自己正在处理同一个请求的一部分。这通过**上下文传播**实现——在服务之间传递追踪 ID 和跨度 ID。

请求首次到达你的系统时，会被分配一个唯一的追踪 ID。当请求在服务之间流转时，这个 ID 随之传递（通常放在 HTTP 头里）。每个服务随后创建自己的跨度，但都关联到同一条追踪。

### 跨度属性与事件

跨度不只是时间戳——它们富含数据：

- **名称**：这个跨度代表什么操作
- **时间**：开始与结束时间
- **状态**：成功、错误等
- **属性**：自定义键值对（例如 `user_id` 或 `cart_size`）
- **事件**：跨度内值得注意的事件
- **链接**：与其他跨度的连接

### 采样策略

对所有请求都做追踪会产生海量数据。因此大多数系统使用采样——只收集一定比例的追踪。聪明的采样策略包括：

- **头部采样**：在请求开始时决定是否采样
- **尾部采样**：在请求结束后决定（更擅长捕获错误）
- **优先级采样**：始终追踪重要操作，常规操作则采样

如果你想了解可观测性、遥测和监控之间的区别，可以看看这篇文章：[可观测性 vs 遥测 vs 监控](https://last9.io/blog/observability-vs-telemetry-vs-monitoring/)。

## 追踪实现指南：工具与框架

准备好给系统加上追踪了吗？以下是你需要的东西：

### OpenTelemetry：行业标准

[OpenTelemetry](https://opentelemetry.io/) 已经成为实现追踪与跨度的首选框架。它提供：

- 覆盖所有主流编程语言的库
- 厂商中立的 API 与 SDK
- 对流行框架的自动埋点
- 一套一致的数据收集与导出方式

### 追踪工具箱

有若干工具可以帮你收集、存储和可视化追踪：

| 工具 | 类型 | 最适合 |
| ----------------------- | ------------------------ | ----------------------------------------------------------------------- |
| Last9 | 一体化可观测性 | 高性价比、可预测定价的高基数可观测性 |
| Jaeger | 开源追踪 | 自托管的追踪可视化 |
| Zipkin | 开源追踪 | 简单的分布式追踪 |
| Grafana Tempo | 追踪后端 | 与 Grafana 仪表板集成 |
| OpenTelemetry Collector | 数据收集流水线 | 处理并路由遥测数据 |

如果你在寻找一款符合预算的可观测性方案，[Last9](https://last9.io/) 值得一看。它按摄取事件计费，让成本保持可预测。此外，我们的平台能在规模上处理高基数数据，并与 OpenTelemetry 和 Prometheus 集成，把你的指标、日志和追踪汇集到一处。

### 在代码中实现追踪

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

想知道 OpenTelemetry 与传统 APM 工具相比如何？这篇文章拆解了关键差异：[OpenTelemetry vs 传统 APM 工具](https://last9.io/blog/opentelemetry-vs-traditional-apm-tools/)。

## 进阶追踪技术

基础追踪就位之后，这些进阶技术可以把你的可观测性提到另一个层次。

### 分布式上下文管理

在复杂系统中，你需要管理的不只是追踪 ID。W3C Trace Context 规范为以下内容提供了标准：

- **traceparent**：包含追踪 ID 和父跨度 ID
- **tracestate**：允许厂商添加自定义上下文数据

使用这些头部可以确保你的追踪在不同服务和厂商之间都能正常工作。

### 追踪、指标与日志之间的关联

可观测性真正的威力来自把不同信号连接起来：

- **样例追踪**：把指标链接到产生它们的追踪
- **日志中的追踪 ID**：在日志消息里加上追踪 ID，便于交叉引用
- **自定义属性**：在所有遥测类型中使用一致的属性

### 错误处理与异常跟踪

异常发生时，跨度可以提供关键上下文：

- 给跨度标记错误状态
- 记录异常及其堆栈跟踪
- 向跨度添加事件，展示错误的演变过程
- 创建 baggage 条目，让错误上下文跨服务边界传递

想更深入了解如何提前发现问题、提升系统可靠性，可以看看这篇关于主动监控的文章：[主动监控](https://last9.io/blog/proactive-monitoring/)。

## 真实世界的追踪模式与反模式

### 有效的追踪模式

**有意义的跨度名称**：使用 `service_name/operation` 这样一致的命名约定
**合适的粒度**：为重要操作创建跨度，而不是每次函数调用都建
**正确的上下文传播**：确保追踪上下文流经所有通信通道
**有用的属性**：添加有助于排查问题的属性，比如用户 ID 或功能开关
**关注性能开销**：留意创建过多跨度带来的开销

### 应避免的追踪反模式

**埋点过度**：创建太多跨度会导致性能问题
**丢失上下文**：未能传播上下文会让追踪在服务边界处断开
**命名不一致**：使用不同的命名标准会让追踪更难解读
**数据过多**：把大体积载荷放进跨度会压垮追踪后端
**忽视第三方服务**：缺少外部调用的跨度会形成盲区

探索可观测性为何是 LLM 性能与可靠性的核心：[LLM 可观测性](https://last9.io/blog/llm-observability/)。

## 追踪与跨度的业务价值：超越技术收益

追踪不只是用来排查问题——它们也能带来业务洞察：

- 端到端追踪关键用户旅程
- 衡量关键业务操作的性能
- 基于追踪数据设定 SLO（服务级别目标）
- 用真实用户的语言量化性能问题的代价
- 通过给跨度添加相关属性来构建业务上下文

当你能展示技术改进如何影响用户体验和业务指标时，你就在 DevOps 与业务相关方之间架起了桥梁。

## 结论

追踪与跨度为你提供了透视分布式系统的 X 光视野。它们揭示服务之间隐藏的连接，精准定位性能瓶颈，并大幅加快调试速度。

随着系统变得愈发复杂，这类可观测性不是奢侈品——而是必需品。

如果你想继续讨论分布式追踪与可观测性，欢迎加入我们的 [Discord 社区](https://discord.com/invite/W8gMppQC4b)，DevOps 从业者在那里分享经验与最佳实践！

## 常见问题

### 追踪与日志有什么区别？

日志记录离散事件，而追踪展示跨服务的操作之间的关系。日志告诉你发生了什么；追踪告诉你它是如何发生的。

### 加上追踪会让我的应用变慢吗？

现代追踪库带来的开销极小——配置得当的情况下，性能影响通常低于 3%。通过采样，你还可以进一步降低这种影响。

### 我需要改所有代码才能加上追踪吗？

不一定。许多框架提供自动埋点，只需很少的代码改动就能加上追踪。OpenTelemetry 为大多数主流语言中的流行框架提供了自动埋点。

### 分布式追踪会产生多大数据量？

这取决于流量、采样率和跨度细节，差异很大。对于繁忙的系统，可以按每天几 GB 到几 TB 来规划。选择合适的可观测性平台，才能把这项成本控制住。

### 追踪能帮助满足安全与合规要求吗？

可以！追踪为请求在系统中流转的过程留下审计轨迹。配合合适的属性，你可以追踪哪些用户或服务在什么时间访问了哪些数据。

### 追踪与跨度如何与其他可观测性信号配合？

追踪与指标、日志互补。指标在高层展示系统健康状况，日志提供详细事件，而追踪把各个点连起来，展示跨服务的请求流转。
