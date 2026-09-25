# Mayank Agarwal, CTO Resolve, and Milind Ganjoo, Technical Staff Resolve（fall2025 W9）

## Slide 1

Agentic AI for software in production
CS146S Guest Lecture
Mayank Agarwal
Milind Ganjoo
Nov 2025

## Slide 2

Milind Ganjoo
Member of Technical Staff
Resolve AI
Mayank Agarwal
Founder & CTO
Resolve AI

## Slide 3

How we imagine software engineering

## Slide 4

In reality, software engineering is complex and messy
Code
AI
Telemetry
Cloud
Knowledge
Systems
Teams
Workflows
Application and product
- 
Development
- 
Deployments
- 
On-call
- 
Cost management
- 
Compliance
- 
Security Vulnerability
- 
Documentation
….
Systems and infra
Networking
Security

## Slide 5

Grunt work application deployment
Creative work
Software Engineering
On call and more...
Log queries
Building context
Evidence gathering
Documentation
Coordination
Working across tools
Compliance
Software
Engineers spend 70+% of their time on
Grunt work
Problem solving
Optimization
Design decisions
Trade offs

## Slide 6

Life of a software engineer who is on call

## Slide 7

What happens when someone is paged at 3:04 AM?
L1 support
Infra
App & product
Eng / Director
Comms manager
Incident commander
Database
App & product
App & product
Multiple team escalations
Come together to research and reason about how to fix the problem.
Manual effort
Engineering team members
On-call
320 AM
400 AM
445 AM
✓
304 AM
?
Eng mitigates post mortem runbooks
Observability
Code
Infra

## Slide 8

What makes production hard for humans (and models)?

## Slide 9

Tooling
Complex, ephemeral infra with databases, messaging services and more
Code
1000ʼs of services across 100ʼs of teams
Low-level tools for logs, metrics, dashboards, feature mgmt, CICD etc
Infra
Navigating siloed data across many systems and tools

## Slide 10

Application
Engineers
Platform
Engineers
SREs
IT Ops
Security
Engineers
Support
Engineers
Specialized skills
Tooling
Code
Infra
Complex production
Coordinating across multiple teams with varied expertise

## Slide 11

Tooling
Code
Infra
Application
Engineers
Platform
Engineers
SREs
IT Ops
Security
Engineers
Support
Engineers
Specialized skills
Fragmented knowledge
Complex production
Messaging
Fragmented and often undocumented context

## Slide 12

Specialized skills
Fragmented knowledge
Complex production
Code
Infra
Messaging
Incidents take hours or days to resolve
Changes are hard to make and trigger issues
Infrastructure spend is constantly increasing
Customers report issues before we discover them
AI generated code exacerbates the problem
Incidents regularly involve
20+ engineers
Only small # of engineers fully understand prod
Takes 3-6 months for new engineers to onboard
Lot of costs incurred in maintaining tools
… directly impacts revenue and costs every day

## Slide 13

What is needed for AI to help engineers with production systems?

## Slide 14

Combined expertise of all your engineers
Understand and operate all your production + tools
Application
Engineers
Platform
Engineers
SREs
IT Ops
Security
Engineers
Support
Engineers
Captures the tribal knowledge of your unique system
Code
Infra
Tooling
Knowledge
3
1
2
Agent-ﬁrst approach to work on production systems

## Slide 15

Let us see it in action

## Slide 16

How AI for production systems works
16
Production systems are complex and always changing
Understands and operates all your production tools
Knowledge is fragmented or undocumented
Captures the tribal knowledge and gets smarter over time
Investigations need expertise from multiple teams
Combines expertise of all your engineers
03
01
02

## Slide 17

Understands and operates all your production tools
Production systems are complex and always changing
- 
Hundreds of tools: different query languages, access mechanisms, and operational behaviors for each
- 
Should map across code <> infra <> telemetry and identify complex dependencies
- 
Massive scale (millions of logs lines, thousands of metrics, dozens of platforms, etc.)

## Slide 18

AI systems should deeply understand your production
18
Production
Logs
Change Events
Metrics
Runbooks
Traces
Alerts
Dashboards
Connects to code, infra, tools, and knowledge
1

## Slide 19

AI systems should deeply understand your production
19
Connects to code, infra, tools, and knowledge
Models how your systems works
1
2

## Slide 20

AI systems should deeply understand your production
20
Connects to code, infra, tools, and knowledge
Models how your systems works
Navigates to the right nodes in the graph to gather evidence
1
2
3

## Slide 21

AI systems should deeply understand your production
21
Connects to code, infra, tools, and knowledge
Models how your systems works
Navigates to the right nodes in the graph to gather evidence
Operates every tool or system like experts
1
2
3
4

## Slide 22

Understands and operates all your production tools
Knowledge is fragmented or undocumented
22
- 
Knowledge is scattered across different runbooks, documentation, chats (if youʼre lucky! Might be completely undocumented otherwise)
- 
In-the-loop feedback or learnings are often undocumented or lost
- 
New investigations need to adapt continuously and require learnings from previous iterations

## Slide 23

AI systems should capture tribal knowledge and get smarter with every interaction
Captures company and team-wide knowledge
1

## Slide 24

AI systems should capture tribal knowledge and get smarter with every interaction
Captures company and team-wide knowledge
Remembers In-the-loop feedback/teachings
1
2

## Slide 25

AI systems should capture tribal knowledge and get smarter with every interaction
25
Captures company and team-wide knowledge
Remembers In-the-loop feedback/teachings
Retrieves context specific information
1
2
3

## Slide 26

Understands and operates all your production tools
Investigating production needs expertise from multiple teams
26
- 
Triaging an incident is hard. Especially for novel incidents or new engineers
- 
Sequential investigations take a lot of time if not on the right path
- 
Coordination across teams adds time or loss of information in hand-offs
- 
Organizational and expertise boundaries make it hard to gather context

## Slide 27

AI systems should combine expertise of all engineers across teams
Creates an investigation plan
1

## Slide 28

AI systems should combine expertise of all engineers across teams
Creates an investigation plan
Pursues multiple hypotheses in parallel
1
2

## Slide 29

AI systems should combine expertise of all engineers across teams
29
Creates an investigation plan
Pursues multiple hypotheses in parallel
Refines plan continuously until you get to root cause
1
2
3

## Slide 30

AI systems should combine expertise of all engineers across teams
30
1
2
3
4
Creates an investigation plan
Pursues multiple hypotheses in parallel
Refines plan continuously until you get to the root cause
Enables multi user collaboration across org boundaries to get to the right answer every time

## Slide 31

How AI for production systems works
31
Production systems are complex and always changing
Understands and operates all your production tools
Knowledge is fragmented or undocumented
Captures the tribal knowledge and gets smarter over time
Investigations need expertise from multiple teams
Combines expertise of all your engineers
03
01
02

## Slide 32

Lessons learned building AI for prod
- 
This isn't just a model problem
- 
Navigating production requires a lot of domain expertise which is coded into the architecture. You canʼt just prompt-engineer models to build production AI
- 
Context windows are limited and production context is infinite
- 
Can't fit 10M logs in any context window. Intelligence is knowing WHAT to query, WHEN, and HOW to filter based on production understanding.
- 
Working with tools is a non-trivial problem
- 
Raw APIs are unusable: large responses, outputs are messy, and meant for humans. Must build AI systems that can filter noise, return structured summaries, handle errors gracefully, work in parallel
- 
Evals are as hard as the product itself
- 
Building evals requires replicating production complexity - (services, dependencies, etc.,). Without evals, you can't trust the outputs.

## Slide 33

AI is changing software engineering
By next year software engineering will look fundamentally different
Grunt work
Grunt work
Creative work
Creative work
Grunt work
Creative work
Models
Agents
Closed loop agents

## Slide 34

Thank You
@resolveai
Weʼre hiring!
linkedin.com/in/resolveai

## Slide 35

Q&A
LETʼS DISCUSS
