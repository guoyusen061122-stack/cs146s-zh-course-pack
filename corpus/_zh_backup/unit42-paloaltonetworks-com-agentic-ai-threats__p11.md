表 10. 用于通过间接提示注入窃取对话历史的攻击者输入示例。

## 防护与缓解

要为智能体应用不断扩张且日益复杂的攻击面提供安全保障，需要采用分层的纵深防御策略。没有任何单一防御措施能应对所有威胁——每一种缓解措施都只针对特定条件下的一部分威胁。本节概述五条关键的缓解策略，它们与本篇文章中所演示的攻击场景相关。

1. 提示词加固
2. 内容过滤
3. 工具输入净化
4. 工具漏洞扫描
5. 代码执行器沙箱化

### 提示词加固

提示词定义了智能体的行为，就像源代码定义了程序一样。提示词范围界定不当或过于宽松会扩大攻击面，使其成为操纵的首要目标。

在托管于 GitHub 的股票咨询助手示例中，我们也提供了「加固版」提示词（[CrewAI](https://github.com/PaloAltoNetworks/stock_advisory_assistant/tree/main/CrewAI#use-reinforced-prompts)、[AutoGen](https://github.com/PaloAltoNetworks/stock_advisory_assistant/tree/main/AutoGen#use-reinforced-prompts)）。这些提示词通过严格的约束与护栏来限制智能体的能力。尽管这些措施提高了攻击得手的门槛，但仅靠提示词加固并不足够。高级注入技术仍有可能绕过这些防御，因此提示词加固必须配合运行时内容过滤。

提示词加固的最佳实践包括：

* 明确禁止智能体披露其指令、协作智能体与工具模式
* 把每个智能体的职责界定得很窄，并拒绝超出范围的请求
* 把工具调用限制在预期的输入类型、格式与取值范围内

### 内容过滤

内容过滤器充当内联防御，实时检查并有选择地阻断智能体的输入与输出。这些过滤器可以在各类攻击扩散之前就有效地检测并阻止它们。

GenAI 应用长期以来一直依赖内容过滤器来防御越狱与提示注入攻击。由于智能体应用继承了这些风险并引入了新的风险，内容过滤仍是关键的防御层。

诸如 [**Palo Alto Networks AI Runtime Security**](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security) 这样的高级方案，提供了针对 AI 智能体量身定制的更深入检查。除了传统的提示词过滤，它们还能检测：

* **工具模式提取**
* **工具滥用**，包括非预期调用与漏洞利用
* **记忆操纵**，例如注入的指令
* **恶意代码执行**，包括 SQL 注入与利用载荷
* **敏感数据泄露**，例如凭据与密钥
* **恶意 URL 与域名引用**

### 工具输入净化

工具绝不能隐式信任自己的输入，即便调用方是一个看似无害的智能体。攻击者可以操纵智能体，使其提供精心构造的输入，从而利用工具内部的漏洞。为防止滥用，每个工具都应在执行前净化和校验输入。

关键检查包括：

* 输入类型与格式（例如预期的字符串、数字或结构化对象）
* 边界与范围检查
* 特殊字符过滤与编码，以防止注入攻击

### 工具漏洞扫描

所有集成到智能体系统中的工具都应定期接受安全评估，包括：

* SAST，用于源码级代码分析
* DAST，用于运行时行为分析
* SCA，用于检测存在漏洞的依赖项与第三方库

这些做法有助于找出配置错误、不安全的逻辑与过时的组件——它们都可能通过工具滥用被利用。

### 代码执行器沙箱化

代码执行器让智能体能够通过实时代码生成与执行来动态解决问题。这种能力很强大，但也引入了额外风险，包括任意代码执行与横向移动。

大多数智能体框架依赖基于容器的沙箱来隔离执行环境。然而，默认配置往往并不足够。为防止沙箱逃逸或滥用，应施加更严格的运行时控制：

* **限制容器网络**：只允许必要的外部域名。阻断对内网服务的访问（例如元数据端点与私有地址）。
* **限制挂载卷** ：避免挂载范围过大或持久化的路径（例如 ./、/home）。使用 tmpfs 把临时数据存放在内存中
* **移除不必要的 Linux 能力** ：去掉像 CAP\_NET\_RAW、CAP\_SYS\_MODULE 和 CAP\_SYS\_ADMIN 这样的特权权限
* **阻断有风险的系统调用** ：禁用 kexec\_load、mount、unmount、iopl 和 bpf 等系统调用
* **强制资源配额**：施加 CPU 与内存限制，以防止拒绝服务（DoS）、失控代码或加密货币挖矿劫持

## 结论

智能体应用既继承了 LLM 与外部工具的漏洞，又通过复杂工作流、自主决策与动态工具调用扩大了攻击面。这放大了被攻陷可能造成的影响，其后果可能从信息泄露、未授权访问一路升级到远程代码执行与整个基础设施被接管。正如我们的模拟攻击所演示的，多种多样的提示词载荷都能触发同一处弱点，这凸显了此类威胁的灵活性与规避性。

保障 AI 智能体的安全，靠的不是零星修补。它需要一套纵深防御策略，覆盖提示词加固、输入校验、安全的工具集成与强健的运行时监控。

仅靠通用安全机制并不足够。组织必须采用专用的解决方案——例如 Palo Alto Networks 的 [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security)——来**发现、评估与保护**智能体应用特有的威胁。

Palo Alto Networks 的客户可通过以下产品，针对上文讨论的威胁获得更好的防护：

[Unit 42 AI 安全评估](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment)可以帮助你主动识别最有可能针对你的 AI 环境的威胁。

如果你认为自己可能已被攻陷，或有紧急事项，请联系 [Unit 42 事故响应团队](https://start.paloaltonetworks.com/contact-unit42.html)，或致电：

* 北美：免费电话：+1 (866) 486-4842（866.4.UNIT42）
* 英国：+44.20.3743.3660
* 欧洲与中东：+31.20.299.3130
* 亚洲：+65.6983.8730
* 日本：+81.50.1790.0200
* 澳大利亚：+61.2.4062.7950
* 印度：00080005045107

Palo Alto Networks 已与我们的 Cyber Threat Alliance（CTA）伙伴成员分享了这些发现。CTA 成员利用这些情报，快速为其客户部署防护，并系统性地瓦解恶意网络行为者。进一步了解 [Cyber Threat Alliance](https://www.cyberthreatalliance.org)。

## 附加资源

* [Stock Advisory Assistant](https://github.com/PaloAltoNetworks/stock_advisory_assistant) —— GitHub
* [CrewAI](https://docs.crewai.com/introduction) —— CrewAI 文档
* [CrewAI](https://github.com/crewAIInc/crewAI) —— CrewAI GitHub 仓库
* [SerperDevTool](https://github.com/crewAIInc/crewAI-tools/tree/main/crewai_tools/tools/serper_dev_tool) —— CrewAI GitHub 仓库
* [ScrapeWebsiteTool](https://github.com/crewAIInc/crewAI-tools/tree/main/crewai_tools/tools/scrape_website_tool) —— CrewAI GitHub 仓库
* [Hierarchical Process](https://docs.crewai.com/how-to/hierarchical-process) —— CrewAI 文档
* [AutoGen](https://microsoft.github.io/autogen/stable/) —— AutoGen 文档
* [AutoGen](https://github.com/microsoft/autogen) —— AutoGen GitHub 仓库
* [Swarm](https://microsoft.github.io/autogen/dev//user-guide/agentchat-user-guide/swarm.html) —— AutoGen 文档
* [关于 VM 元数据](https://cloud.google.com/compute/docs/metadata/overview) —— Google Cloud 文档
* [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/) —— OWASP
* [OWASP Agentic AI Threats and Mitigation](https://genaisecurityproject.com/resource/agentic-ai-threats-and-mitigations/) —— OWASP
* [Nasdaq](https://www.nasdaq.com/) —— Nasdaq

*2025 年 5 月 2 日下午 2:20（太平洋时间）更新，以调整产品表述。*
返回顶部

### 标签

* [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")
* [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
* [BOLA](https://unit42.paloaltonetworks.com/tag/bola/ "BOLA")
* [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")
* [Prompt injection](https://unit42.paloaltonetworks.com/tag/prompt-injection/ "prompt injection")  
  [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research") [下一篇：Gremlin Stealer：地下论坛上开卖的新型窃密程序](https://unit42.paloaltonetworks.com/new-malware-gremlin-stealer-for-sale-on-telegram/ "Gremlin Stealer: New Stealer on Sale in Underground Forum")

### 目录

* 

### 相关文章

* [带堆视图的保险库：AgentCore Harness 与身份之间令人不安的空白](https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/ "article - table of contents")
* [走进现代 SOC：防御跨环境横向转移](https://unit42.paloaltonetworks.com/soc-cross-environment-pivot/ "article - table of contents")
* [攻击者暴露出针对拉丁美洲组织的持续 AI 工具调用活动](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "article - table of contents")

## 相关恶意软件资源

![插图：一把放大镜照亮深色高科技背景上发光的橙色圆形数字电路界面。](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Myth-Busting_Overview_1920x900-786x368.jpg)  
[![分类图标](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)洞见](https://unit42.paloaltonetworks.com/category/insights/) 2026 年 9 月 16 日 [#### Atomic macOS（AMOS）窃密程序活动](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/)

* [MacOS](https://unit42.paloaltonetworks.com/tag/macos/ "macOS")

* [威胁情报](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")

* [Unit 42](https://unit42.paloaltonetworks.com/tag/unit-42/ "Unit 42")  
  [立即阅读 ![右箭头](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "Atomic macOS (AMOS) Stealer Activity")  
  ![插图：SPIFFE/SPIRE 中利用后身份滥用的示意。一名戴眼镜者的特写，镜片上反射出计算机代码。](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Security-Technology_Category_1920x900-786x368.jpg)  
  [![分类图标](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)威胁研究](https://unit42.paloaltonetworks.com/category/threat-research/) 2026 年 9 月 10 日 [#### 千面机器：SPIFFE/SPIRE 中的利用后身份滥用](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/)

* [API](https://unit42.paloaltonetworks.com/tag/api/ "API")

* [密码学](https://unit42.paloaltonetworks.com/tag/cryptographic/ "cryptographic")

* [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")  
  [立即阅读 ![右箭头](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE")  
  ![插图：按安装付费的威胁组织活动，提供用于传播恶意软件的感染服务。图中是一块带有中央微芯片的计算机电路板特写。红色数字数据流以发光二进制数字和箭头的形式在芯片内外流动，象征数据处理与传输。画面笼罩在未来感的蓝红光芒中。](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Malware_Category_1920x900-6-786x368.jpg)  
  [![分类图标](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)威胁研究](https://unit42.paloaltonetworks.com/category/threat-research/) 2026 年 9 月 9 日 [#### 未被追踪的噩梦：藏在商品化基础设施背后的威胁](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/)

* [ARKTunnel](https://unit42.paloaltonetworks.com/tag/arktunnel/ "ARKTunnel")

* [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")

* [CL-CRI-1171](https://unit42.paloaltonetworks.com/tag/cl-cri-1171/ "CL-CRI-1171")  
  [立即阅读 ![右箭头](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/ "Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure")  
  ![插图：攻击者使用 AI 工具针对拉丁美洲组织。一座充满活力的城市景观，街上众多行人的剪影。画面被明亮的城市灯光与数字化粒子照亮，营造出动态而未来感的氛围。](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/AdobeStock_768915868-2-1-786x373.jpg)  
  [![分类图标](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)威胁研究](https://unit42.paloaltonetworks.com/category/threat-research/) 2026 年 9 月 3 日 [#### 攻击者暴露出针对拉丁美洲组织的持续 AI 工具调用活动](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/)

* [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")

* [ChatGPT](https://unit42.paloaltonetworks.com/tag/chatgpt/ "ChatGPT")

* [CL-CRI-1131](https://unit42.paloaltonetworks.com/tag/cl-cri-1131/ "CL-CRI-1131")  
  [立即阅读 ![右箭头](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America")  
  ![插图：Microsoft Teams 中的语音钓鱼活动。黑色背景上由蓝色二进制代码构成的骷髅图像，散落的一和零与数字噪点，象征隐蔽的提示注入攻击如何利用 AI 逻辑绕过安全控制。](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/01_Malware_Category_1920x900-5-786x368.jpg)  
  [![分类图标](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)威胁研究](https://unit42.paloaltonetworks.com/category/threat-research/) 2026 年 8 月 31 日 [#### Spring Ring：深入剖析 Microsoft Teams 中的语音钓鱼活动](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/)

* [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/ "Cloaked Ursa")

* [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")

* [Microsoft Teams](https://unit42.paloaltonetworks.com/tag/microsoft-teams/ "Microsoft Teams")  
  [立即阅读 ![右箭头](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams")  
  ![插图：AI 驱动的恶意软件。一个充满活力的数字界面，展示各种图标与图表，类似未来感的网络或数据分析仪表盘。画面被发光的光线与图案照亮。](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/AdobeStock_1270203474-2-1-786x368.png)  
  [![分类图标](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)威胁研究](https://unit42.paloaltonetworks.com/category/threat-research/) 2026 年 8 月 25 日 [#### 2026 年 8 月 AI 驱动恶意软件态势：从品牌滥用走向智能体化执行](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/)

* [后门](https://unit42.paloaltonetworks.com/tag/backdoor/ "backdoor")

* [比特币](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")

* [DLL 劫持](https://unit42.paloaltonetworks.com/tag/dll-hijacking/ "DLL hijacking")  
  [立即阅读 ![右箭头](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/ "The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution")  
  ![插图：通过可信通信渠道进行的身份滥用。特写一块数字屏幕，显示经过故障与像素化处理的骷髅状图像。](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/02_Malware_Category_1920x900-2-786x368.jpg)  
  [![分类图标](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)威胁研究](https://unit42.paloaltonetworks.com/category/threat-research/) 2026 年 8 月 20 日 [#### 通过可信通信渠道进行的身份滥用](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/)

* [身份验证](https://unit42.paloaltonetworks.com/tag/authentication/ "authentication")

* [身份盗用](https://unit42.paloaltonetworks.com/tag/identity-theft/ "identity theft")

* [恶意软件](https://unit42.paloaltonetworks.com/tag/malware/ "malware")  
  [立即阅读 ![右箭头](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/ "Identity Abuse Through Trusted Communication Channels")  
  ![插图：Kimwolf 僵尸网络恶意软件家族。数字屏幕上有一个写着「Malware」的警告标志。背景是成行计算机代码与图形，营造出网络安全威胁感。](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)  
  [![分类图标](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)威胁研究](https://unit42.paloaltonetworks.com/category/threat-research/) 2026 年 8 月 11 日 [#### Kimwolf v7：Kimwolf 僵尸网络的演进](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

* [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")

* [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
