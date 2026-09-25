Table 10. Examples of attacker input for indirect prompt injection to exfiltrate conversation history.

## Protection and Mitigation

Securing the expanded and complex attack surface of agentic applications requires layered, defense-in-depth strategies. No single defense can address all threats --- each mitigation targets only a subset of threats under certain conditions. This section outlines five key mitigation strategies relevant to the attack scenarios demonstrated in this article.

1. Prompt hardening
2. Content filtering
3. Tool input sanitization
4. Tool vulnerability scanning
5. Code executor sandboxing

### Prompt Hardening

A prompt defines an agent's behavior, much like source code defines a program. Poorly scoped or overly permissive prompts expand the attack surface, making them a prime target for manipulation.

In the stock advisory assistant examples hosted on GitHub, we also provide a version of "reinforced" prompts ([CrewAI](https://github.com/PaloAltoNetworks/stock_advisory_assistant/tree/main/CrewAI#use-reinforced-prompts), [AutoGen](https://github.com/PaloAltoNetworks/stock_advisory_assistant/tree/main/AutoGen#use-reinforced-prompts)). These prompts are designed with strict constraints and guardrails to limit agent capabilities. While these measures raise the bar for successful attacks, prompt hardening alone is not sufficient. Advanced injection techniques could still bypass these defenses, which is why prompt hardening must be paired with runtime content filtering.

Best practices for prompt hardening include:

* Explicitly prohibiting agents from disclosing their instructions, coworker agents and tool schemas
* Defining each agent's responsibilities narrowly and rejecting requests outside of scope
* Constraining tool invocations to expected input types, formats and values

### Content Filtering

Content filters serve as inline defenses that inspect and optionally block agent inputs and outputs in real time. These filters can effectively detect and prevent various attacks before they propagate.

GenAI applications have long relied on content filters to defend against jailbreaks and prompt injection attacks. Since agentic applications inherit these risks and introduce new ones, content filtering remains a critical layer of defense.

Advanced solutions such as [**Palo Alto Networks AI Runtime Security**](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security) offer deeper inspection tailored to AI agents. Beyond traditional prompt filtering, they can also detect:

* **Tool schema extraction**
* **Tool misuse**, including unintended invocations and vulnerability exploitation
* **Memory manipulation**, such as injected instructions
* **Malicious code execution**, including SQL injection and exploit payloads
* **Sensitive data leakage**, such as credentials and secrets
* **Malicious URLs and domain references**

### Tool Input Sanitization

Tools must never implicitly trust their inputs, even when invoked by a seemingly benign agent. Attackers can manipulate agents into supplying crafted inputs that exploit vulnerabilities within tools. To prevent abuse, every tool should sanitize and validate inputs before execution.

Key checks include:

* Input type and format (e.g., expected strings, numbers or structured objects)
* Boundary and range checking
* Special character filtering and encoding to prevent injection attacks

### Tool Vulnerability Scanning

All tools integrated into agentic systems should undergo regular security assessments, including:

* SAST for source-level code analysis
* DAST for runtime behavior analysis
* SCA to detect vulnerable dependencies and third-party libraries

These practices help identify misconfigurations, insecure logic and outdated components that can be exploited through tool misuse.

### Code Executor Sandboxing

Code executors enable agents to dynamically solve tasks through real-time code generation and execution. While powerful, this capability introduces additional risks, including arbitrary code execution and lateral movement.

Most agent frameworks rely on container-based sandboxes to isolate execution environments. However, default configurations are often not sufficient. To prevent sandbox escape or misuse, apply stricter runtime controls:

* **Restrict container networking**: Allow only necessary outbound domains. Block access to internal services (e.g., metadata endpoints and private addresses).
* **Limit mounted volumes** : Avoid mounting broad or persistent paths (e.g., ./, /home). Use tmpfs to store temporary data in-memory
* **Drop unnecessary Linux capabilities** : Remove privileged permissions like CAP\_NET\_RAW, CAP\_SYS\_MODULE and CAP\_SYS\_ADMIN
* **Block risky system calls** : Disable syscalls like kexec\_load, mount, unmount, iopl and bpf
* **Enforce resource quotas**: Apply CPU and memory limits to prevent denial of service (DoS), runaway code or cryptojacking

## Conclusion

Agentic applications inherit the vulnerabilities of both LLMs and external tools while expanding the attack surface through complex workflows, autonomous decision-making and dynamic tool invocation. This amplifies the potential impact of compromises, which can escalate from information leakage and unauthorized access to remote code execution and full infrastructure takeover. As our simulated attacks demonstrate, a wide variety of prompt payloads can trigger the same weakness, underscoring how flexible and evasive these threats can be.

Securing AI agents requires more than ad hoc fixes. It demands a defense-in-depth strategy that spans prompt hardening, input validation, secure tool integration and robust runtime monitoring.

General-purpose security mechanisms alone are insufficient. Organizations must adopt purpose-built solutions --- such as Palo Alto Networks [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security) --- to **Discover, Assess and Protect** threats unique to agentic applications.

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

A [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment) can help you proactively identify the threats most likely to target your AI environment.

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

* North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
* UK: +44.20.3743.3660
* Europe and Middle East: +31.20.299.3130
* Asia: +65.6983.8730
* Japan: +81.50.1790.0200
* Australia: +61.2.4062.7950
* India: 00080005045107

Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Additional Resources

* [Stock Advisory Assistant](https://github.com/PaloAltoNetworks/stock_advisory_assistant) -- GitHub
* [CrewAI](https://docs.crewai.com/introduction) -- CrewAI Documentation
* [CrewAI](https://github.com/crewAIInc/crewAI) -- CrewAI GitHub Repository
* [SerperDevTool](https://github.com/crewAIInc/crewAI-tools/tree/main/crewai_tools/tools/serper_dev_tool) -- CrewAI GitHub Repository
* [ScrapeWebsiteTool](https://github.com/crewAIInc/crewAI-tools/tree/main/crewai_tools/tools/scrape_website_tool) -- CrewAI GitHub Repository
* [Hierarchical Process](https://docs.crewai.com/how-to/hierarchical-process) -- CrewAI Documentation
* [AutoGen](https://microsoft.github.io/autogen/stable/) -- AutoGen Documentation
* [AutoGen](https://github.com/microsoft/autogen) -- AutoGen GitHub Repository
* [Swarm](https://microsoft.github.io/autogen/dev//user-guide/agentchat-user-guide/swarm.html) -- AutoGen Documentation
* [About VM metadata](https://cloud.google.com/compute/docs/metadata/overview) -- Google Cloud Documentation
* [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/) -- OWASP
* [OWASP Agentic AI Threats and Mitigation](https://genaisecurityproject.com/resource/agentic-ai-threats-and-mitigations/) -- OWASP
* [Nasdaq](https://www.nasdaq.com/) -- Nasdaq

*Updated May 2, 2025, at 2:20 p.m. PT to update product language.*
Back to top

### Tags

* [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")
* [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
* [BOLA](https://unit42.paloaltonetworks.com/tag/bola/ "BOLA")
* [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")
* [Prompt injection](https://unit42.paloaltonetworks.com/tag/prompt-injection/ "prompt injection")  
  [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research") [Next: Gremlin Stealer: New Stealer on Sale in Underground Forum](https://unit42.paloaltonetworks.com/new-malware-gremlin-stealer-for-sale-on-telegram/ "Gremlin Stealer: New Stealer on Sale in Underground Forum")

### Table of Contents

* 

### Related Articles

* [A Vault with a Heap-View: The Uncomfortable Space Between AgentCore Harness and Identity](https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/ "article - table of contents")
* [Inside the Modern SOC: Defending the Cross-Environment Pivot](https://unit42.paloaltonetworks.com/soc-cross-environment-pivot/ "article - table of contents")
* [Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "article - table of contents")

## Related Malware Resources

![Pictorial representation of a magnifying glass illuminating a glowing orange circular digital circuit interface on a dark, high-tech background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Myth-Busting_Overview_1920x900-786x368.jpg)  
[![category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) September 16, 2026 [#### Atomic macOS (AMOS) Stealer Activity](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/)

* [MacOS](https://unit42.paloaltonetworks.com/tag/macos/ "macOS")

* [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")

* [Unit 42](https://unit42.paloaltonetworks.com/tag/unit-42/ "Unit 42")  
  [Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "Atomic macOS (AMOS) Stealer Activity")  
  ![Pictorial representation of post-exploitation identity misuse in SPIFFE/SPIRE. Close-up of a person wearing glasses, with computer code reflected in the lenses.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Security-Technology_Category_1920x900-786x368.jpg)  
  [![category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 10, 2026 [#### The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/)

* [API](https://unit42.paloaltonetworks.com/tag/api/ "API")

* [Cryptographic](https://unit42.paloaltonetworks.com/tag/cryptographic/ "cryptographic")

* [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")  
  [Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE")  
  ![Pictorial representation of a pay-per-install threat group campaign prodiving infection service for spreading malware. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip, symbolizing data processing and transfer. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Malware_Category_1920x900-6-786x368.jpg)  
  [![category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 9, 2026 [#### Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/)

* [ARKTunnel](https://unit42.paloaltonetworks.com/tag/arktunnel/ "ARKTunnel")

* [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")

* [CL-CRI-1171](https://unit42.paloaltonetworks.com/tag/cl-cri-1171/ "CL-CRI-1171")  
  [Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/ "Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure")  
  ![Pictorial representation of attackers using AI tools to target Latin American organizations. A vibrant cityscape with silhouettes of numerous people walking along a bustling street. The scene is illuminated by bright urban lights and digital-like particles, creating a dynamic and futuristic atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/AdobeStock_768915868-2-1-786x373.jpg)  
  [![category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 3, 2026 [#### Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/)

* [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")

* [ChatGPT](https://unit42.paloaltonetworks.com/tag/chatgpt/ "ChatGPT")

* [CL-CRI-1131](https://unit42.paloaltonetworks.com/tag/cl-cri-1131/ "CL-CRI-1131")  
  [Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America")  
  ![Pictorial representation of vishing campaigns in Microsoft Teams. A digital image of a skull formed by blue binary code on a black background, with scattered ones and zeros and digital noise, symbolizes how stealthy prompt injection attacks can exploit AI logic to bypass security controls.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/01_Malware_Category_1920x900-5-786x368.jpg)  
  [![category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 31, 2026 [#### Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/)

* [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/ "Cloaked Ursa")

* [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")

* [Microsoft Teams](https://unit42.paloaltonetworks.com/tag/microsoft-teams/ "Microsoft Teams")  
  [Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams")  
  ![Pictorial representation of AI-enabled malware. A vibrant digital interface displaying various icons and graphs, resembling a futuristic network or data analysis dashboard. The scene is illuminated with glowing lights and patterns.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/AdobeStock_1270203474-2-1-786x368.png)  
  [![category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 25, 2026 [#### The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/)

* [Backdoor](https://unit42.paloaltonetworks.com/tag/backdoor/ "backdoor")

* [Bitcoin](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")

* [DLL hijacking](https://unit42.paloaltonetworks.com/tag/dll-hijacking/ "DLL hijacking")  
  [Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/ "The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution")  
  ![Pictorial representation of identity abuse through trusted communication channels. Close-up view of a digital screen displaying a glitched and pixelated image of a skull-like shape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/02_Malware_Category_1920x900-2-786x368.jpg)  
  [![category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 20, 2026 [#### Identity Abuse Through Trusted Communication Channels](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/)

* [Authentication](https://unit42.paloaltonetworks.com/tag/authentication/ "authentication")

* [Identity theft](https://unit42.paloaltonetworks.com/tag/identity-theft/ "identity theft")

* [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")  
  [Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/ "Identity Abuse Through Trusted Communication Channels")  
  ![Pictorial representation of Kimwolf botnet malware family. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)  
  [![category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 11, 2026 [#### Kimwolf v7: An Evolution of the Kimwolf Botnet](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

* [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")

* [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
