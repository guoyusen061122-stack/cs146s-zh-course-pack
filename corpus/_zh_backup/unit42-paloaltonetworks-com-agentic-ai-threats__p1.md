# 智能体式 AI 威胁：身份伪装与冒用风险

[![Logo](https://www.paloaltonetworks.com/wp-content/uploads/2021/07/PANW_Parent.png)](https://www.paloaltonetworks.com/)  
[![Unit42 Logo](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/unit42-logo-white.svg)](https://unit42.paloaltonetworks.com/)  
菜单

* [工具](https://unit42.paloaltonetworks.com/tools/)
* [ATOMs](https://unit42.paloaltonetworks.com/atoms/)
* [安全咨询](https://www.paloaltonetworks.com/unit42)
* [关于我们](https://unit42.paloaltonetworks.com/about-unit-42/)
* [**正在遭受攻击？**](https://start.paloaltonetworks.com/contact-unit42.html)
* [威胁研究中心](https://unit42.paloaltonetworks.com "Threat Research")
* [威胁研究](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
* [恶意软件](https://unit42.paloaltonetworks.com/category/malware/ "Malware")  
  [恶意软件](https://unit42.paloaltonetworks.com/category/malware/)

# AI 智能体已经到来。威胁也随之而来。

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 阅读时长 21 分钟  
相关产品  
[![Prisma SASE icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma SASE](https://unit42.paloaltonetworks.com/product-category/prisma-sase/ "Prisma SASE")[![Secure Access Service Edge (SASE) icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)安全访问服务边缘（SASE）](https://unit42.paloaltonetworks.com/product-category/secure-access-service-edge/ "Secure Access Service Edge (SASE)")[![Unit 42 AI Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 AI 安全评估](https://unit42.paloaltonetworks.com/product-category/ai-security-assessment/ "Unit 42 AI Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 事故响应](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

* ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)  
  作者：

  * [Royce Lu](https://unit42.paloaltonetworks.com/author/royce-lu/)
  * [Jay Chen](https://unit42.paloaltonetworks.com/author/jay-chen/)

* ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)  
  发布于：2025 年 5 月 1 日

* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)  
  分类：

  * [恶意软件](https://unit42.paloaltonetworks.com/category/malware/)
  * [威胁研究](https://unit42.paloaltonetworks.com/category/threat-research/)

* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)  
  标签：

  * [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/)
  * [AI](https://unit42.paloaltonetworks.com/tag/ai/)
  * [BOLA](https://unit42.paloaltonetworks.com/tag/bola/)
  * [GenAI](https://unit42.paloaltonetworks.com/tag/genai/)
  * [Prompt injection](https://unit42.paloaltonetworks.com/tag/prompt-injection/)

* [![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/agentic-ai-threats/?pdf=download&lg=en&_wpnonce=63b8b1691f "Click here to download")

* [![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/agentic-ai-threats/?pdf=print&lg=en&_wpnonce=63b8b1691f "Click here to print")

分享 ![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

* ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
* [![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=AI%20Agents%20Are%20Here.%20So%20Are%20the%20Threats.&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fagentic-ai-threats%2F "Share in email")
* [![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fagentic-ai-threats%2F "Share in Facebook")
* [![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fagentic-ai-threats%2F&title=AI%20Agents%20Are%20Here.%20So%20Are%20the%20Threats. "Share in LinkedIn")
* [![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fagentic-ai-threats%2F&text=AI%20Agents%20Are%20Here.%20So%20Are%20the%20Threats. "Share in Twitter")
* [![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](https://www.paloaltonetworks.com//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fagentic-ai-threats%2F&ts=markdown "Share in Reddit")
* [![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=AI%20Agents%20Are%20Here.%20So%20Are%20the%20Threats.%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fagentic-ai-threats%2F "Share in Mastodon")

## 执行摘要

智能体应用是这样一类程序：它们借助 AI 智能体——即被设计用来自主收集数据并朝特定目标采取行动的软件——来驱动自身功能。随着 AI 智能体在真实应用中越来越广泛地被采用，理解其安全影响至关重要。本文研究攻击者针对智能体应用的可行途径，给出了九个具体攻击场景，其后果包括信息泄露、凭据窃取、工具利用与远程代码执行。

为了评估这些风险的适用范围有多广，我们用两种不同的开源智能体框架——[CrewAI](https://github.com/crewAIInc/crewAI) 与 [AutoGen](https://github.com/microsoft/autogen)——实现了两个功能完全相同的应用，并对两者执行了相同的攻击。我们的发现表明，大多数漏洞与攻击向量在很大程度上与框架无关，它们源于不安全的设计模式、配置错误与不安全的工具集成，而不是框架本身的缺陷。

我们还针对每个攻击场景提出了防御策略，并分析其有效性与局限。为支持可复现性与后续研究，我们已在 [GitHub](https://github.com/PaloAltoNetworks/stock_advisory_assistant) 上开源了源代码与数据集。

### **关键发现**

* **攻陷 AI 智能体并不总是需要提示注入**。范围界定不当或未加固的提示词，即使没有显式注入也能被利用。
* ***缓解措施**：在智能体指令中强制加入防护措施，明确阻断超出范围的请求以及套取指令或工具模式的行为。*
* **提示注入仍是最有效、最多样的攻击向量之一**，能够泄露数据、滥用工具或颠覆智能体行为。
* ***缓解措施**：部署内容过滤器，在运行时检测并阻断提示注入尝试。*
* **配置错误或有漏洞的工具**会显著扩大攻击面与影响。
* ***缓解措施**：净化所有工具输入，施加严格的访问控制，并定期做安全测试，例如静态应用安全测试（SAST）、动态应用安全测试（DAST）或软件成分分析（SCA）。*
* **未加固的代码解释器**会让智能体面临任意代码执行以及未授权访问宿主资源与网络的风险。
* ***缓解措施**：施加强沙箱隔离，包括网络限制、系统调用过滤与最小权限的容器配置。*
* **凭据泄露**，例如暴露的服务令牌或密钥，可能导致身份冒用、权限提升或基础设施被攻陷。
* ***缓解措施**：使用数据丢失防护（DLP）方案、审计日志与密钥管理服务来保护敏感信息。*
* **没有任何单一缓解措施是足够的**。要有效降低智能体应用的风险，必须采用分层的纵深防御策略。
* ***缓解措施**：在智能体、工具、提示词与运行时环境之间组合多重防护，构建有韧性的防御。*

需要强调的是，CrewAI 与 AutoGen 本身都不存在固有漏洞。本研究中的攻击场景凸显的是**系统性风险**，其根源在于语言模型抵御提示注入的能力有限，以及所集成工具的配置错误或漏洞——而不是某个具体框架的问题。因此，我们的发现与推荐缓解措施可广泛适用于各类智能体应用，与所采用的底层框架无关。

Palo Alto Networks 用 [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security)（AI Runtime Security）重新定义了 AI 安全——为你的 AI 应用、模型、数据与智能体提供实时防护。通过智能分析网络流量与应用行为，Prisma AIRS 主动检测并阻止提示注入、拒绝服务攻击与数据外泄等高级威胁。它在网络层与 API 层都能无缝地内联执行策略。

同时，AI Access Security 提供对第三方生成式 AI（GenAI）使用的深度可视性与精确控制。它通过策略执行与用户活动监控，帮助防范影子 AI 风险、数据泄露以及 AI 输出中的恶意内容。这两类方案共同提供了分层防御，既保护 AI 系统的运行完整性，也保障外部 AI 工具的安全使用。

[Unit 42 AI 安全评估](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment)可以帮助你主动识别最有可能针对你的 AI 环境的威胁。

如果你认为自己可能已被攻陷，或有紧急事项，请联系 [Unit 42 事故响应团队](https://start.paloaltonetworks.com/contact-unit42.html)。

| **Unit 42 相关主题** | [**GenAI**](https://unit42.paloaltonetworks.com/tag/genai/)、**[Prompt Injection](https://unit42.paloaltonetworks.com/tag/prompt-injection/)** |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|

## AI 智能体概览

AI 智能体是一种软件程序，被设计用来从环境中自主收集数据、处理信息并采取行动，以在无人工直接干预的情况下达成特定目标。这类智能体通常由 AI 模型驱动——其中最典型的是大语言模型（LLM）——这些模型充当其核心推理引擎。

AI 智能体的一个标志性特征，是能够把 AI 模型连接到外部函数或工具，从而自主决定使用哪些工具来推进其目标。函数或工具是一种外部能力——例如 API、数据库或服务——智能体可以调用它来完成超出模型内置知识范围的特定任务。这种集成使智能体能够对给定任务进行推理、规划解决方案并有效执行行动以达成目标。在更复杂的场景中，多个 AI 智能体可以作为团队协作——各自负责问题的不同方面——共同解决更大、更复杂的挑战。​

AI 智能体在各行各业都有多样化的应用。在客户服务领域，它们驱动机器人与虚拟助手来高效处理咨询。在金融领域，它们协助进行欺诈检测与投资组合管理。医疗健康领域也可以利用 AI 智能体进行患者监护与诊断支持。

图 1 是一个典型的 AI 智能体架构，展示了智能体如何使用 LLM 通过执行循环进行规划、推理与行动。它通过函数调用连接到外部工具，以执行访问代码、数据或人工输入等任务。
![示意图：展示集成 AI 模型的应用架构。图中包含三个主要部分：服务、应用与 AI 模型。应用又细分为输入、智能体与输出区域，智能体内部包含规划、执行循环与函数调用。支撑服务包括长期记忆与向量数据存储。AI 模型上标注了 LLM（大语言模型）与函数调用。服务下方展示了代码、人在回路、设备与内容的图标。Palo Alto Networks 与 Unit 42 标志组合。](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/04/word-image-141040-140037-1.png) 图 1. AI 智能体架构。

智能体还可以引入记忆——包括短期与长期记忆——以保留上下文并改进决策。应用通过输入与输出接口向智能体发送请求、接收结果，这些接口通常以 API 的形式暴露。

## AI 智能体的安全风险

由于 AI 智能体通常构建在 LLM 之上，它们继承了 [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/) 中列出的许多安全风险，例如提示注入、敏感数据泄露与供应链漏洞。然而，AI 智能体通过集成常用多种编程语言与框架构建的外部工具，超出了传统 LLM 应用的范畴。

引入这些外部工具，使 LLM 暴露于 SQL 注入、远程代码执行与访问控制失效等经典软件威胁之下。攻击面因此扩大，再加上智能体能够与外部系统乃至物理世界交互，使 AI 智能体的安全保障尤为关键。

最近发表的文章 [OWASP Agentic AI Threats and Mitigation](https://genaisecurityproject.com/resource/agentic-ai-threats-and-mitigations/) 重点介绍了这些新兴威胁。以下概述与下一节所演示攻击场景相关的关键威胁：

* \*\*提示注入：\*\*攻击者向 GenAI 系统偷偷植入隐藏或误导性的指令，试图让应用偏离其预期行为。这可能使智能体以意想不到的方式行事，例如无视既定规则与策略、泄露敏感信息，或利用工具采取非预期行动。
* **工具滥用：**攻击者操纵智能体——往往借助欺骗性提示词——来滥用其集成的工具。这可能涉及触发非预期行动或利用工具内部的漏洞，进而可能导致有害或未授权的执行。
* **意图破坏与目标操纵**：攻击者通过微妙地改变 AI 智能体所感知的目标或推理过程，来攻击其规划与追求目标的能力。攻击者利用这些漏洞把智能体的行动从原本意图上引开。常见手法包括智能体劫持，即对抗性输入扭曲智能体的理解与决策。
* **身份伪装与冒用**：攻击者利用薄弱或已被攻陷的身份验证，冒充合法的 AI 智能体或用户。一个主要风险是智能体凭据被盗，这可能让攻击者以虚假身份访问工具、数据或系统。
* **非预期的 RCE 与代码攻击**：攻击者利用 AI 智能体执行代码的能力。通过注入恶意代码，他们可以未授权访问执行环境中的各个要素，例如内部网络与宿主文件系统。当智能体可以访问敏感数据或高权限工具时，这会带来严重风险。
* **智能体通信投毒**：攻击者针对 AI 智能体之间的交互，向其通信通道注入攻击者控制的信息。这会扰乱协作工作流、削弱协调能力并操纵集体决策——在多智能体系统中尤其如此，因为那里信任与准确的信息交换至关重要。
* **资源过载**：攻击者通过压垮 AI 智能体被分配的计算、内存或服务上限来耗尽其资源。这会降低性能、扰乱运行并使应用失去响应，影响该应用的所有用户。

## 针对 AI 智能体的模拟攻击

为研究 AI 智能体的安全风险，我们用两种流行的开源智能体框架——[CrewAI](https://github.com/crewAIInc/crewAI) 与 [AutoGen](https://github.com/microsoft/autogen)——开发了一个多用户、多智能体的投资咨询助手。两个实现功能完全相同，并共用同一套指令、语言模型与工具。

这一设置表明，这些安全风险并非某个框架或模型所特有。相反，它们源于智能体开发过程中引入的配置错误或不安全设计。需要注意的是，CrewAI 与 AutoGen 框架本身并没有漏洞。

图 2 展示了投资咨询助手的架构，它由三个协同工作的智能体组成：编排智能体、新闻智能体与股票智能体。
![示意图：展示编排智能体与客户、新闻智能体和股票智能体交互。编排智能体处理来自客户的输入与输出，并与新闻智能体协同管理任务，后者使用网页读取器与搜索引擎；股票智能体则使用代码解释器、数据库与股票数据。Palo Alto Networks 与 Unit 42 标志组合。](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/04/word-image-146340-140037-2.png) 图 2. 投资咨询助手架构。

* **编排智能体**：该智能体管理用户交互。它解读用户请求，把任务分派给合适的智能体，汇总其输出并把最终回复交给用户。
* **新闻智能体** ：该智能体收集并总结关于某家公司或某个行业的最新财经新闻。它配备了两个工具：
  * **搜索引擎工具** ：该工具借助 Google 检索指向相关财经新闻的 URL。我们使用 CrewAI 的 [SerperDevTool](https://github.com/crewAIInc/crewAI-tools/tree/main/crewai_tools/tools/serper_dev_tool) 实现。
  * **网页内容读取工具** ：该工具抓取并提取给定网页的文本内容。我们使用 CrewAI 的 [ScrapeWebsiteTool](https://github.com/crewAIInc/crewAI-tools/tree/main/crewai_tools/tools/scrape_website_tool) 实现。
* **股票智能体** ：该智能体帮助用户管理股票投资组合，包括查看交易历史、买入或卖出股票、获取历史股价以及生成可视化图表。它使用了三个工具：
  * **数据库工具**：该工具提供读取或更新投资组合数据库、卖出或买入股票以及查看交易历史的功能。
  * **股票工具** ：该工具从 [Nasdaq](https://www.nasdaq.com/) 获取历史股价。
  * **代码解释器工具**：该工具运行 Python 代码，为投资组合创建数据可视化图表。

**助手可以回答的示例问题：**
