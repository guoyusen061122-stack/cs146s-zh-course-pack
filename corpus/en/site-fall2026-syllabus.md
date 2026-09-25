# CS146S 课程大纲 · fall2026

## Week 1: The Internals of Coding Agents

### Topics
- What an LLM actually is, and what the agent loop looks like under the hood
- The core tool set (read, write, edit, bash) and how tasks flow through it
- How production coding agents structure their system prompts and tool definitions

### Readings
- [Building a Coding Agent](https://youtube.com/watch?v=s7ZzkdvCMDY)

### Sessions
- Tue 9/22: Course intro + build Claude Code in 200 lines
  - [Slides](https://docs.google.com/presentation/d/1uztIhjHAG6O_9QOD1N_3wdhwhABml1fANXEN2dGwdbg/edit?usp=drive_link)
  - [Completed code](https://drive.google.com/file/d/1DxKa_autBOu9s8DvItodgUAwH_pBg7aR/view?usp=drive_link)
- Thu 9/24: How state-of-the-art coding agents are designed: deep dive into the system prompts that define the agent

## Week 2: Advanced Context Engineering

### Topics
- Advanced prompting techniques and when each applies
- RePPIT (Research, Propose, Plan, Implement, Test) and spec-driven development
- MCP fundamentals: servers, clients, tools, and transport
- Designing tools for agent ergonomics

### Sessions
- Tue 9/29: Advanced prompting + agentic dev frameworks (RePPIT, spec-driven development)
- Thu 10/1: Full introduction to MCP and tool-calling (theory, setup, and advanced tool design)

## Week 3: Agent Skills and CLI

### Topics
- What skills are and how SKILL.md + scripts encode a workflow
- Web skills and extending agent capability beyond the repo
- Working effectively from the CLI

### Sessions
- Tue 10/6: All about agent skills (including web skills)
- Thu 10/8: Guest: Lee Robinson (VP of Developer Relations @ Cursor) ([profile](https://leerob.com))

## Week 4: Customizing Your Agent and Repository

### Topics
- CLAUDE.md and AGENTS.md: what to put where
- Hooks for lint gates, test runs, and guardrails
- Subagent patterns (planner / implementer / reviewer)

### Sessions
- Tue 10/13: Customizing your agentic setup (CLAUDE.md, AGENTS.md, hooks)
- Thu 10/15: Guest: Boris Cherny (Creator of Claude Code @ Anthropic) ([profile](https://borischerny.com))

## Week 5: Agent-Ready Codebases

### Topics
- What makes a repo agent-ready: structure, docs, tests, and checks
- Scoring and auditing readiness
- Common gaps that block agents in real repos

### Sessions
- Tue 10/20: Agent readiness in your repos (structure, docs, and checks that make repos agent-friendly)
- Thu 10/22: Guest: Eno Reyes (CTO @ Factory) ([profile](https://www.linkedin.com/in/enoreyes))

## Week 6: Agentic Code Review

### Topics
- What AI review catches well, and what it misses
- Review architectures and custom rules
- Fitting AI review into a team's PR workflow

### Sessions
- Tue 10/27: Agentic code review: best practices and architectures
- Thu 10/29: Guest: Silas Alberti (SVP Research @ Cognition) ([profile](https://sil.as))

## Week 7: Security

### Topics
- SAST / SCA, dependency and secret-leak vulnerabilities
- Prompt injection and agent-specific attack surfaces
- Agent-assisted triage and remediation

### Sessions
- Tue 11/3: Security in AI codebases
- Thu 11/5: Guest: Isaac Evans (CEO @ Semgrep) ([profile](https://www.linkedin.com/in/isaacevans))

## Week 8: Background Agents

### Topics
- Async, cloud-delegated agents
- Managing fleets of parallel agents
- Issue-to-PR pipelines and triggers (Slack, Linear, GitHub)

### Sessions
- Tue 11/10: Background agents: launching tasks asynchronously
- Thu 11/12: Guest: Rajesh Bhatia (Senior Director @ Cloudflare) ([profile](https://www.linkedin.com/in/rajeshbh))

## Week 9: Building an AI-Native Team

### Topics
- MCP portals and centralized, permissioned tool access
- LLM gateways, model routing, and cost optimization
- Org-wide adoption patterns

### Sessions
- Tue 11/17: Guest: Elad Gil (Investor @ Gil Capital) ([profile](https://eladgil.com))
- Thu 11/19: Guest: Amjad Masad (CEO @ Replit) ([profile](https://amasad.me))

## Week 10: The Software Factory + The Future

### Topics
- Self-running, self-improving software systems
- Running and securing agents post-deployment
- Where AI software engineering goes next

### Sessions
- Tue 12/1: Coding agents in big teams (MCP portals, LLM gateways, org patterns, cost optimization, and model routing)
- Thu 12/3: The Software Factory: self-running, self-improving software systems
