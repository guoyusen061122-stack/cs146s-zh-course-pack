# CS146S 课程大纲 · fall2025

## Week 1: Introduction to Coding LLMs and AI Development

### Topics
- Course logistics
- What is an LLM actually
- How to prompt effectively

### Readings
- [Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI)
- [Prompt Engineering Overview](https://cloud.google.com/discover/what-is-prompt-engineering)
- [Prompt Engineering Guide](https://www.promptingguide.ai/techniques)
- [AI Prompt Engineering: A Deep Dive](https://www.youtube.com/watch?v=T9aRN5JkmL8)
- [How OpenAI Uses Codex](https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf)

### Assignments
- [LLM Prompting Playground](https://github.com/mihail911/modern-software-dev-assignments/tree/master/week1)

### Sessions
- Mon 9/22: Introduction and how an LLM is made
  - [Slides](https://docs.google.com/presentation/d/1zT2Ofy88cajLTLkd7TcuSM4BCELvF9qQdHmlz33i4t0/edit?usp=sharing)
- Fri 9/26: Power prompting for LLMs
  - [Slides](https://docs.google.com/presentation/d/1MIhw8p6TLGdbQ9TcxhXSs5BaPf5d_h77QY70RHNfeGs/edit?usp=drive_link)

## Week 2: The Anatomy of Coding Agents

### Topics
- Agent architecture and components
- Tool use and function calling
- MCP (Model Context Protocol)

### Readings
- [MCP Introduction](https://stytch.com/blog/model-context-protocol-introduction/)
- [Sample MCP Server Implementations](https://github.com/modelcontextprotocol/servers)
- [MCP Server Authentication](https://developers.cloudflare.com/agents/guides/remote-mcp-server/#add-authentication)
- [MCP Server SDK](https://github.com/modelcontextprotocol/typescript-sdk/tree/main?tab=readme-ov-file#server)
- [MCP Registry](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/)
- [MCP Food-for-Thought](https://www.reillywood.com/blog/apis-dont-make-good-mcp-tools/)

### Assignments
- [First Steps in the AI IDE](https://github.com/mihail911/modern-software-dev-assignments/tree/master/week2)

### Sessions
- Mon 9/29: Building a coding agent from scratch
  - [Slides](https://docs.google.com/presentation/d/11CP26VhsjnZOmi9YFgLlonzdib9BLyAlgc4cEvC5Fps/edit?usp=sharing)
  - [Completed Exercise](https://drive.google.com/file/d/1YtpKFVG13DHyQ2i3HOtwyVJOV90nWeL2/view?usp=drive_link)
- Fri 10/3: Building a custom MCP server
  - [Slides](https://docs.google.com/presentation/d/1zSC2ra77XOUrJeyS85houg1DU7z9hq5Y4ebagTch-5o/edit?usp=drive_link)
  - [Completed Exercise](https://drive.google.com/file/d/1J6lgZWcxPzpCpjujJSnW1aAkCYF6Yxv3/view?usp=drive_link)

## Week 3: The AI IDE

### Topics
- Context management and code understanding
- PRDs for agents
- IDE integrations and extensions

### Readings
- [Specs Are the New Source Code](https://blog.ravi-mehta.com/p/specs-are-the-new-source-code)
- [How Long Contexts Fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)
- [Devin: Coding Agents 101](https://devin.ai/agents101#introduction)
- [Getting AI to Work In Complex Codebases](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)
- [How FAANG Vibe Codes](https://x.com/rohanpaul_ai/status/1959414096589422619)
- [Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

### Assignments
- [Build a Custom MCP Server](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week3/assignment.md)

### Sessions
- Mon 10/6: From first prompt to optimal IDE setup
  - [Slides](https://docs.google.com/presentation/d/11pQNCde_mmRnImBat0Zymnp8TCS_cT_1up7zbcj6Sjg/edit?usp=sharing)
  - [Design Doc Template](https://drive.google.com/file/d/1MZ0Qx68Vzw4x5x_XcV8XiPLp7fFDe1LJ/view?usp=drive_link)
- Fri 10/10: Silas Alberti, Head of Research Cognition ([profile](https://sil.as))
  - [Slides](https://docs.google.com/presentation/d/1i0pRttHf72lgz8C-n7DSegcLBgncYZe_ppU7dB9zhUA/edit?usp=sharing)

## Week 4: Coding Agent Patterns

### Topics
- Managing agent autonomy levels
- Human-agent collaboration patterns

### Readings
- [How Anthropic Uses Claude Code](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)
- [Claude Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Awesome Claude Agents](https://github.com/vijaythecoder/awesome-claude-agents)
- [Super Claude](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- [Good Context Good Code](https://blog.stockapp.com/good-context-good-code/)
- [Peeking Under the Hood of Claude Code](https://medium.com/@outsightai/peeking-under-the-hood-of-claude-code-70f5a94a9a62)

### Assignments
- [Coding with Claude Code](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week4/assignment.md)

### Sessions
- Mon 10/13: How to be an agent manager
  - [Slides](https://docs.google.com/presentation/d/19mgkwAnJDc7JuJy0zhhoY0ZC15DiNpxL8kchPDnRkRQ/edit?usp=sharing)
- Fri 10/17: Boris Cherney, Creator of Claude Code ([profile](https://borischerny.com))
  - [Slides](https://docs.google.com/presentation/d/1bv7Zozn6z45CAh-IyX99dMPMyXCHC7zj95UfwErBYQ8/edit?usp=sharing)

## Week 5: The Modern Terminal

### Topics
- AI-enhanced command line interfaces
- Terminal automation and scripting

### Readings
- [Warp University](https://www.warp.dev/university?slug=university)
- [Warp vs Claude Code](https://www.warp.dev/university/getting-started/warp-vs-claude-code)
- [How Warp Uses Warp to Build Warp](https://notion.warp.dev/How-Warp-uses-Warp-to-build-Warp-21643263616d81a6b9e3e63fd8a7380c)

### Assignments
- [Agentic Development with Warp](https://github.com/mihail911/modern-software-dev-assignments/tree/master/week5)

### Sessions
- Mon 10/20: How to Build a Breakout AI Developer Product
  - [Slides](https://docs.google.com/presentation/d/1Djd4eBLBbRkma8rFnJAWMT0ptct_UGB8hipmoqFVkxQ/edit?usp=sharing)
- Fri 10/24: Zach Lloyd, CEO Warp ([profile](https://www.linkedin.com/in/zachlloyd))
  - [Slides](https://www.figma.com/slides/kwbcmtqTFQMfUhiMH8BiEx/Warp---Stanford--Copy-?node-id=9-116&t=oBWBCk8mjg2l2NR5-1)

## Week 6: AI Testing and Security

### Topics
- Secure vibe coding
- History of vulnerability detection
- AI-generated test suites

### Readings
- [SAST vs DAST](https://www.splunk.com/en_us/blog/learn/sast-vs-dast.html)
- [Copilot Remote Code Execution via Prompt Injection](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/)
- [Finding Vulnerabilities in Modern Web Apps Using Claude Code and OpenAI Codex](https://semgrep.dev/blog/2025/finding-vulnerabilities-in-modern-web-apps-using-claude-code-and-openai-codex/)
- [Agentic AI Threats: Identity Spoofing and Impersonation Risks](https://unit42.paloaltonetworks.com/agentic-ai-threats/)
- [OWASP Top Ten: The Leading Web Application Security Risks](https://owasp.org/www-project-top-ten/)
- [Context Rot: Understanding Degradation in AI Context Windows](https://research.trychroma.com/context-rot)
- [Vulnerability Prompt Analysis with O3](https://github.com/SeanHeelan/o3_finds_cve-2025-37899/blob/master/system_prompt_uafs.prompt)

### Assignments
- [Writing Secure AI Code](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week6/assignment.md)

### Sessions
- Mon 10/27: AI QA, SAST, DAST, and Beyond
  - [Slides](https://docs.google.com/presentation/d/1C05bCLasMDigBbkwdWbiz4WrXibzi6ua4hQQbTod_8c/edit?usp=sharing)
- Fri 10/31: Isaac Evans, CEO Semgrep ([profile](https://www.linkedin.com/in/isaacevans))

## Week 7: Modern Software Support

### Topics
- What AI code systems can we trust
- Debugging and diagnostics
- Intelligent documentation generation

### Readings
- [Code Reviews: Just Do It](https://blog.codinghorror.com/code-reviews-just-do-it/)
- [How to Review Code Effectively](https://github.blog/developer-skills/github/how-to-review-code-effectively-a-github-staff-engineers-philosophy/)
- [AI-Assisted Assessment of Coding Practices in Modern Code Review](https://arxiv.org/pdf/2405.13565)
- [AI Code Review Implementation Best Practices](https://graphite.dev/guides/ai-code-review-implementation-best-practices)
- [Code Review Essentials for Software Teams](https://blakesmith.me/2015/02/09/code-review-essentials-for-software-teams.html)
- [Lessons from millions of AI code reviews](https://www.youtube.com/watch?v=TswQeKftnaw)

### Assignments
- [Code Review Reps](https://github.com/mihail911/modern-software-dev-assignments/tree/master/week7)

### Sessions
- Mon 11/3: AI code review
  - [Slides](https://docs.google.com/presentation/d/1NkPzpuSQt6Esbnr2-EnxM9007TL6ebSPFwITyVY-QxU/edit?usp=sharing)
- Fri 11/7: Tomas Reimers, CPO Graphite ([profile](https://www.linkedin.com/in/tomasreimers))
  - [Slides](https://drive.google.com/file/d/1hwF-RIkOJ_OFy17BKhzFyCtxSS7Pcf7p/view?usp=drive_link)

## Week 8: Automated UI and App Building

### Topics
- Design and frontend for everyone
- Rapid UI/UX prototyping and iteration

### Assignments
- [Multi-stack Web App Builds](https://github.com/mihail911/modern-software-dev-assignments/tree/master/week8)

### Sessions
- Mon 11/10: End-to-end apps with a single prompt
  - [Slides](https://docs.google.com/presentation/d/1GrVLsfMFIXMiGjIW9D7EJIyLYh_-3ReHHNd_vRfZUoo/edit?usp=sharing)
- Fri 11/14: Gaspar Garcia, Head of AI Research Vercel ([profile](https://www.linkedin.com/in/gaspargarcia))
  - [Slides](https://docs.google.com/presentation/d/1Jf2aN5zIChd5tT86rZWWqY-iDWbxgR-uynKJxBR7E9E/edit?usp=sharing)

## Week 9: Agents Post-Deployment

### Topics
- Monitoring and observability for AI systems
- Automated incident response
- Triaging and debugging

### Readings
- [Introduction to Site Reliability Engineering](https://sre.google/sre-book/introduction/)
- [Observability Basics You Should Know](https://last9.io/blog/traces-spans-observability-basics/)
- [Kubernetes Troubleshooting with AI](https://resolve.ai/blog/kubernetes-troubleshooting-in-resolve-ai)
- [Your New Autonomous Teammate](https://resolve.ai/blog/product-deep-dive)
- [Role of Multi Agent Systems in Making Software Engineers AI-native](https://resolve.ai/blog/role-of-multi-agent-systems-AI-native-engineering)
- [Benefits of Agentic AI in On-call Engineering](https://resolve.ai/blog/Top-5-Benefits)

### Sessions
- Mon 11/17: Incident response and DevOps
  - [Slides](https://docs.google.com/presentation/d/1Mfe-auWAsg9URCujneKnHr0AbO8O-_U4QXBVOlO4qp0/edit?usp=sharing)
- Fri 11/21: Mayank Agarwal, CTO Resolve, and Milind Ganjoo, Technical Staff Resolve
  - [Slides](https://drive.google.com/file/d/11WnEbMGc9kny_WBpMN10I8oP8XsiQOnM/view?usp=sharing)

## Week 10: What's Next for AI Software Engineering

### Topics
- Future of software development roles
- Emerging AI coding paradigms
- Industry trends and predictions

### Sessions
- Mon 12/1: Software development in 10 years
- Fri 12/5: Martin Casado, General Partner a16z ([profile](https://a16z.com/author/martin-casado/))
