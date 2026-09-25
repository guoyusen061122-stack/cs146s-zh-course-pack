# SAST 与 DAST

# SAST、DAST 与 RASP：应用安全测试方法对比

学习

2024 年 12 月 18 日

Shanika Wickramasinghe

全球信息安全支出预计到 2025 年将达到 [2120 亿美元](https://www.gartner.com/en/newsroom/press-releases/2024-08-28-gartner-forecasts-global-information-security-spending-to-grow-15-percent-in-2025)。这意味着比 2024 年增长 15%。Gartner 认为，[生成式 AI](/en_us/blog/learn/generative-ai.html) 的兴起与云的普及是这一快速增长的主要原因。该分析机构还预测，到 2027 年，GenAI 将参与 17% 的[网络攻击](/en_us/blog/learn/cybersecurity-attacks.html)。

企业需要超越传统做法的先进安全策略，才能应对这些不断增长的风险。正因如此，企业负责人需要了解 SAST、DAST 和 RASP 这类安全方案，它们能为应用提供多层防护。

*（相关阅读：**[应用安全详解](/en_us/blog/learn/application-security-requirements.html)**与**[常见软件测试方法](/en_us/blog/learn/software-testing.html)。）*

## 什么是 SAST？

静态应用安全测试（SAST）是一种[白盒](https://en.wikipedia.org/wiki/White-box_testing)安全测试方法。SAST [利用应用的静态源代码](/en_us/blog/learn/static-code-analysis.html)或二进制文件来识别漏洞。这意味着 SAST 工具在应用未运行时对应用代码进行分析。

开发者用 SAST 检测各类安全风险，例如代码中的[跨站脚本（XSS）](/en_us/blog/learn/cross-site-scripting-xss-attacks.html)、不安全的反序列化、缓冲区溢出，以及[其他 OWASP 漏洞](/en_us/blog/learn/owasp-top-10.html)。由于单靠 SAST 无法识别运行时特有的漏洞，开发者往往需要把 SAST 与其他测试方法结合，才能实现全面的安全防护。

SAST 是[软件开发生命周期](/en_us/blog/learn/software-development-lifecycle-sdlc.html)的重要组成部分，因为它能尽早发现漏洞。发现问题越早，修复成本越低。由于 SAST 工具可以在开发阶段运行，开发者现在能在产品发布到市场之前，把代码编写并测试上千次（！！）。

SAST 可以集成到 [CI/CD 流水线](/en_us/blog/learn/ci-cd-devops-pipeline.html)中，这样做时被称为「Secure DevOps」或「[DevSecOps](/en_us/blog/learn/devsecops-concepts-principles.html)」。SAST 通过自动化可以大规模扩展。能够落地覆盖 SAST 技术的自动化测试，使 SAST 成为快速处理代码级风险的高效方案。

## 什么是 DAST？

动态应用安全测试是一种[黑盒](https://en.wikipedia.org/wiki/Black-box_testing)测试方法。DAST 中的 [「Dynamic」一词](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)表明，这种方法是在*应用运行期间*评估应用的安全性。与 SAST 不同，DAST 不需要访问应用的源代码，而是：

1. 模拟外部攻击者的行为。
1. 从外部测试应用，以[识别仅在运行时出现的漏洞](/en_us/blog/learn/vulnerability-types.html)。

DAST 能够识别多种安全缺陷，例如拒绝服务（DoS）漏洞和不安全的服务器配置。通过模拟真实攻击场景，DAST 工具评估应用如何响应这些模拟威胁。用这种方法，开发者可以发现 SAST 等静态测试方法可能遗漏的弱点。

通常，开发者在软件开发生命周期的后期执行 DAST，往往就在部署之前。通过在实际运行环境中测试应用，DAST 能清晰呈现运行时安全的整体状况，帮助应用提升表现以抵御潜在攻击。

## SAST 如何工作？

开发者使用 [SAST 工具](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)应用预定义规则和其他检测方法——例如模式匹配与数据流分析——来识别编码错误和其他漏洞。开发者把这些工具集成进 IDE 或 CI/CD 流水线，在编码与测试阶段自动执行扫描。

### 常见的 SAST 方法

以下是 SAST 中常用的一些方法。

![常见的静态应用安全测试方法](/content/dam/splunk-blogs/images/media_14bcb87a7461de3b7ba525cf6cf4c9c17338a9433/common-static-aplication-security-testing-methods.avif?width=750&format=avif&optimize=medium)

**模式匹配**扫描代码库，查找已知的不安全编码实践模式，例如使用弱加密算法或不安全的 API 调用。

**数据流分析**追踪数据在应用中如何流动。它可以把不可信输入的路径追踪到敏感操作，从而识别 [SQL 注入](/en_us/blog/learn/sql-injection.html)或缓冲区溢出等漏洞。

**控制流分析**可以分析应用的控制结构，例如循环和条件语句，以发现逻辑缺陷或竞态条件等潜在漏洞。

**自定义规则创建。** 许多工具允许开发者创建自定义规则，以落实编码最佳实践。以下是这类自定义规则的一些示例：

- 标记 SQL 查询中任何未净化输入的使用。
- 识别把用户提供的数据输出到浏览器却未正确转义的代码。
- 高亮有漏洞或已弃用函数的使用，例如 JavaScript 中的 **`eval()`** 或 C 中的 **`strcpy()`**。
- 检测源代码中出现的硬编码 API 密钥和密码，并标记任何缺少对用户提供数据进行输入校验的位置。

**依赖扫描。** 一些 SAST 工具会分析应用使用的第三方库和框架，以识别依赖中的漏洞。

**语义分析。** 通过解读代码的含义而不仅是结构，SAST 工具可以检测不安全的配置或 API 的误用。

**机器学习模型：** 先进的 SAST 工具引入机器学习算法，通过分析大规模数据集中的模式来识别此前未知的漏洞。

### 使用 SAST 工具时的性能考量

SAST 工具往往需要[大量 CPU](/en_us/blog/learn/cpu-vs-gpu.html) 和内存资源。在分析大型代码库时，这可能是个大问题。对一百万行代码做一次完整扫描，可能消耗数 GB 内存。

SAST 扫描所需的时间会随代码库规模大幅变化：小型项目只需几分钟，企业级应用则要数小时。这可能会影响：

- 构建流水线的时间安排
- [开发者生产力](/en_us/blog/learn/dpe-developer-productivity-engineering.html)

可以考虑使用支持增量扫描的现代 SAST 工具，这样只需分析变更的代码，而不必分析整个代码库。

此外，通过规则选择和范围界定来做性能调优也很关键。配置不当的 SAST 工具会不必要地分析非关键代码路径，白白浪费时间和资源，却带不来安全收益。

## DAST 如何工作？

DAST 工具模拟真实攻击——例如向输入字段发送各种形式的恶意数据，观察应用如何处理——以识别应用行为与响应中的漏洞和弱点。

### DAST 的步骤

该过程通常包含以下步骤。

![动态应用安全测试的步骤](/content/dam/splunk-blogs/images/media_1aece54bbf699307808799045108b90d64c19ee54/dynamic-application-security-testing-steps.avif?width=750&format=avif&optimize=medium)

**第 1 步：扫描。** 扫描 Web 应用以发现入口点（如 URL、表单和 API）。这一步会梳理出应用的结构，并识别[潜在的攻击面](/en_us/blog/learn/attack-surfaces.html)。

**第 2 步：攻击模拟。** 通过向应用发送精心构造的请求来模拟恶意活动。这些请求尝试利用入口点，以检测跨站脚本和跨站请求伪造等漏洞。

**第 3 步：漏洞检测。** 分析应用的响应以识别安全弱点，评估应用在受攻击时是否按预期运行。例如，可以注入恶意数据来检测 SQL 注入缺陷。

**第 4 步：报告。** 生成包含已检测漏洞与修复建议的报告。开发者可以利用报告中的结果修复已识别的问题。

现代 DAST 方案可以纳入 AI 驱动分析和[实时数据集成](/en_us/blog/learn/real-time-data.html)等高级特性。它们自动创建测试集，动态适应应用结构，并用机器学习算法尽量减少误报。

### 使用 DAST 工具时的性能考量

使用 DAST 工具时，有一些性能瓶颈需要注意。

- **DAST 工具会与运行中的应用主动交互**，暂时提高应用服务器和 Web 服务器的 CPU 与内存占用。
- DAST 扫描期间产生的**大量并发请求**会消耗可观的网络带宽。
- **DAST 扫描器常常通过生成唯一请求绕过或使应用缓存失效**，降低缓存机制的有效性。
- DAST 工具**创建和管理多个测试会话**会提高应用服务器的内存占用。

为避免这类问题或尽量降低其影响，请遵循以下做法。

- 把 DAST 扫描安排在应用使用量最少的非高峰时段。
- 在与生产环境一致的预发布或预生产环境中执行扫描。
- 使用 DAST 工具中的限流功能控制并发请求数量。
- 在扫描期间增加应用服务器的线程池。
- 为 DAST 扫描器 IP 配置独立的缓存策略。
- 当超过性能阈值时自动暂停扫描。

## SAST 与 DAST：关键差异

下表总结了 SAST 与 DAST 的差异。

测试类型

白盒测试。在可以访问源代码的情况下，从内到外测试应用。

黑盒测试。在无法访问源代码的情况下，从外部测试应用。

支持的软件类型

支持多种类型的软件，包括 Web 应用、Web 服务和胖客户端。

支持 Web 应用和 Web 服务，但通常不支持其他软件类型。

在 SDLC 中的阶段

在软件开发生命周期的早期执行。

在 SDLC 的后期进行，往往在部署期间或部署之后。

检测到的漏洞

识别编码缺陷，例如：SQL 注入、跨站脚本（XSS）、缓冲区溢出等。

检测运行时问题，例如服务器配置错误、拒绝服务漏洞和应用层缺陷。

漏洞修复成本

由于问题在 SDLC 早期就被发现，成本较低。

由于漏洞发现得较晚，成本更高，往往需要紧急修复才能按时部署。

运行时与环境问题

无法检测运行时特有或与环境相关的漏洞。

可以识别仅在运行时出现或因环境因素而出现的漏洞。

深度与广度

对代码级漏洞提供深入洞察。

提供应用外部安全风险的全局视角。

与工具的集成

与 IDE 和 CI/CD 流水线集成，实现自动化静态分析。

与 CI/CD 流水线集成，实现持续的运行时测试。

误报与漏报

由于代码分析深入，误报的概率更高。

误报更少，但由于内部可见性有限，漏报风险更高。

技术依赖

依赖[编程语言](/en_us/blog/learn/programming-languages.html)和框架；需要与工具兼容。

由于从外部与应用交互，不依赖应用框架。

## SAST 与 DAST 的优缺点

### SAST 的优点

- 在软件开发生命周期的早期识别安全漏洞。
- 分析代码库，包括基础函数和复杂分支。
- 直接在源代码上运行，不需要应用处于运行状态。
- 提供实时反馈和全面的洞察，例如漏洞的确切位置。
- 生成可导出的报告，可用仪表盘跟踪。
- 支持自动化，因此比人工代码评审更快、更高效。

### SAST 的缺点

- 常常产生大量误报，因此可能需要人工复核。
- 无法识别运行时特有的或特定环境下的漏洞，例如配置错误。
- 需要针对每种编程语言的专用工具，因此维护复杂。
- 难以理解外部库、API 和 REST 端点。

### DAST 的优点

- 识别仅在应用执行期间出现的漏洞。
- 从外部运行，不需要访问源代码。这对测试第三方应用或已编译的代码很有效。
- 模拟真实攻击场景，识别 SAST 遗漏的风险。
- 与应用所使用的编程语言无关。
- 评估整个应用与系统，包括内存消耗、资源使用和第三方接口。

### DAST 的缺点

- 只关注应用的外层，可能遗漏更深层的漏洞。
- 在 SDLC 后期才应用，因此修复成本更高、更耗时。
- 会遗漏某些 SAST 工具能通过源代码分析识别出的漏洞。举例来说，假设某个 Web 应用使用不安全的随机数生成器（例如 JavaScript 中的 **`Math.random()`**）来生成会话令牌。DAST 可能遗漏这个缺陷，因为它只测试运行时行为。（但 SAST 能检测到。）
- 大型项目需要定制基础设施，并需要并行运行多个应用实例，因此资源消耗大。

## 何时该用 SAST、何时该用 DAST？

SAST 与 DAST 在保障 SDLC 安全上起着互补作用。了解各自的使用时机，有助于实现全面的安全覆盖。

### 何时使用 SAST

**在开发早期阶段。** 开发者在 SDLC 早期用 SAST 识别 SQL 注入、硬编码凭据等漏洞。在部署前发现这些问题，可以降低修复的成本和复杂度。

例如：SAST 工具扫描 Python 代码，标记出源代码中内嵌硬编码 API 密钥的漏洞。开发者重构代码，改用环境变量安全地存储和读取密钥。

**用于代码评审。** SAST 集成到版本控制系统中，让开发者在提交代码前先做扫描。这样能确保只有安全的代码进入仓库。

示例：SAST 工具可以检测到一种漏洞——文件路径直接由用户输入构造且未经校验，使应用面临路径遍历攻击。开发者通过净化输入并使用安全的库函数处理文件路径来修复该问题。

**在持续集成/持续部署流水线中。** SAST 在 CI/CD 流程中运行自动化扫描，为开发者提供实时反馈。

### 何时使用 DAST

**预生产测试。** 开发者在预发布或 QA 环境中用 DAST 识别运行时漏洞（例如：不安全的配置、身份验证缺陷、访问控制不足）。

示例：DAST 工具可以检测到导致敏感数据暴露的数据库配置错误。开发者随后可以在部署前加固该配置。

**在部署后监控中。** DAST 工具持续扫描已部署的应用，查找由环境变化或新出现的威胁所导致的漏洞。这可以保证应用长期保持安全。

**测试第三方集成。** DAST 可以模拟外部攻击者的视角，识别第三方 API 或互连系统中的漏洞。

例如：DAST 工具测试一个 Web 应用时，发现第三方支付 API 中存在漏洞——信用卡信息通过未加密的 HTTP 连接传输。开发者通过强制所有 API 通信使用 HTTPS 来解决该问题。

## 哪种更有效：SAST 还是 DAST？

SAST 或 DAST 的有效性取决于：

- SDLC 所处阶段
- 所针对的漏洞类型

SAST 在开发早期效果最好，主要用于识别源代码中的漏洞、降低成本并推广安全编码实践。相比之下，DAST 关注预生产或已部署应用的运行时漏洞，能揭示配置错误和不安全集成等问题。

### 采用混合方案

与其在两者之间二选一，**把 SAST 与 DAST 结合起来可以形成多层安全策略，同时覆盖静态代码和运行时环境中的漏洞**。SAST 可以集成到开发早期阶段，在应用编译之前检测并修复代码级问题。当应用在测试环境中运行后，DAST 可以识别运行时漏洞，并评估应用在受攻击条件下的行为。

在 CI/CD 流水线中同时自动化 SAST 和 DAST 扫描，可以提供持续反馈，并在不牺牲安全的前提下加快开发进程。

对于敏捷或 DevOps 环境，加入 IAST 或 RASP 这类工具可以进一步增强安全性。通过关联 SAST 与 DAST 的结果，组织可以实现更全面、[更有效的漏洞管理](/en_us/blog/learn/vulnerability-management.html)。

### 用 RASP 作为 SAST 与 DAST 的替代方案

运行时应用自我保护（RASP）是一种直接安装在[应用所运行的服务器](/en_us/blog/learn/computer-servers.html)上的高级安全方案。

RASP 把自身嵌入应用的运行时环境。这种集成让 RASP 能够分析应用的逻辑和数据。在分析过程中，它可以：

1. 在异常行为发生时立即检测到。
1. 立即阻断恶意活动。

一个关键区别是，RASP 不只是对潜在问题发出告警——它会隔离并处置威胁，主动阻止攻击，而不依赖外部工具。

RASP 为 SAST 和 DAST 提供了一种动态替代方案。SAST 分析静态代码，DAST 模拟外部攻击，而 RASP 是实时运行的。它监控应用在执行期间的行为，并通过终止会话或提醒防御人员来响应实时威胁。

对于绕过网络防御或在开发阶段被遗漏的漏洞，RASP 的保护尤为有效。

不过，过度信任 RASP 可能让组织忽视安全编码实践。此外，由于 RASP 直接在应用的运行时环境内运行，可能影响应用性能。RASP 无法取代修复底层缺陷的必要性，但它能在修复进行期间提供持续保护。

正如[一位 RASP 用户](https://www.gartner.com/peer-community/post/talking-about-app-security-use-rast-tool-substitute-security-control-valuable-add-it-not-valuable-at)所评论的：

「是否使用 RASP 工具，应基于对应用具体需求与风险状况的全面评估。」

## 未来是 SAST、DAST 与 RASP 协同的应用安全测试

应用测试的未来在于把 SAST、DAST 和 RASP 结合起来，形成全面的安全策略。随着安全挑战加剧，把这些工具集成到 CI/CD 流水线并实现流程自动化将变得必不可少。

AI 与机器学习的进步将让测试更高效，有助于减少误报并提升威胁检测能力。

### 金融与金融服务行业

在金融领域，AI 驱动的工具将改变漏洞检测与缓解的方式。SAST 和 DAST 会继续在开发和预生产阶段识别编码缺陷与运行时问题。

但不会止步于此：RASP 会借助 AI 更进一步，[监控实时交易](/en_us/blog/learn/continuous-monitoring.html)。例如，RASP 可以检测异常模式（例如：攻击者试图实时利用某个漏洞），阻断这些活动并通知安全团队。

### IoT、边缘与联网设备

就 IoT 而言，这些工具的组合将在保障联网设备安全方面发挥重要作用。具体如下：

- SAST 可以在开发阶段确认固件不含漏洞。
- DAST 可以测试设备之间通信协议的安全性。
- 而 RASP 则监控已部署的设备，检测并阻止未授权访问尝试，或由新出现的威胁导致的数据泄露。

同样，采用多种方法有助于 IoT 生态保持韧性。正如前文多个示例所示，SAST、DAST 与 RASP 三者结合，预示着未来应用在构建和部署时将具备更强、更主动的安全措施。

## 有韧性的安全始于主动测试

把 SAST、DAST 和 RASP 结合起来，可以提供覆盖整个软件开发生命周期的稳健安全防护。

把这些方法集成到 CI/CD 流水线，并利用 AI 的进步，组织就能主动应对新出现的威胁。这些方法共同构成一套整体方案，保护现代应用免受安全漏洞影响。

[/en_us/blog/fragments/disclaimer-with-divider](/en_us/blog/fragments/disclaimer-with-divider)

样式

两列

标题

相关文章

筛选

分类

博客数量上限

3

learn

分类排序、随机顺序

true

![Shadow AI 简介](https://www.splunk.com/content/dam/splunk-blogs/images/media_1ec85698bab5c96d7de31feebb4d7927c2b22bdb6/introduction-to-shadow-ai.webp?width=300&format=webp&optimize=medium)

4 分钟阅读

### [Shadow AI 简介](/en_us/blog/learn/shadow-ai.html)

了解 Shadow AI 的风险与收益——这类未经授权的生成式 AI 工具提升了工作场所的生产力，却给数据安全和 IT 治理带来挑战。

![什么是 DNS 预取？](https://www.splunk.com/content/dam/splunk-blogs/images/media_1df91062c4ae927641fa60f49987be7b618421f45/what-is-a-dns-prefetch.avif?width=300&format=avif&optimize=medium)

6 分钟阅读

### [什么是 DNS 预取？](/en_us/blog/learn/dns-prefetch.html)

了解 DNS 预取这种资源提示：它是什么、为何以及如何使用，还有审计与扩展的最佳实践。

![什么是 CSIRT？计算机安全事故响应团队完全指南](https://www.splunk.com/content/dam/splunk-blogs/images/media_1a88a67ed7b390e5a04c5f42364d725fbe67f2809/what-is-csirt-the-computer-security-incident-respo.avif?width=300&format=avif&optimize=medium)

8 分钟阅读

### [什么是 CSIRT？计算机安全事故响应团队完全指南](/en_us/blog/learn/csirt-computer-security-incident-response-team.html)

重大安全事件发生时：你需要尽快降低影响并恢复正常。最好的办法是什么？CSIRT。了解这个团队的全部细节。

[/en_us/blog/fragments/about-splunk](/en_us/blog/fragments/about-splunk)

[/en_us/blog/fragments/subscribe-footer](/en_us/blog/fragments/subscribe-footer)
