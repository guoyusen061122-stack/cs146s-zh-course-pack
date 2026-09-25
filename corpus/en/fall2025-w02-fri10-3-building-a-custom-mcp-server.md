# Building a custom MCP server（fall2025 W2）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University, Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

To MCP and Beyond themodernsoftware.dev

## Slide 3

Why
- 
LLMs have vast (but static) world knowledge that only updates when we retrain
- 
To build fully autonomous systems we need robust ways to feed dynamic data in
- 
What’s the weather today
- 
Who’s president
- 
What’s the price of Bitcoin
- 
Who’s the narrator in Nike’s latest ad campaign
- 
RAG and tool-calling are the best answer we have today themodernsoftware.dev

## Slide 4

Basics
- 
M odel
C ontext
P rotocol
- 
Open protocol that allows systems to provide context to AI models in a manner generalizable across integrations
■
In English: standard format for exposing tools to LLMs
- 
History: in the distant past pre-November 2024 when MCP was introduced… themodernsoftware.dev

## Slide 5

themodernsoftware.dev
????
What APIs do you expose?
Imagine integrating with a questionable 3rd party API

## Slide 6

themodernsoftware.dev
????
Now many APIs
????
????

## Slide 7

themodernsoftware.dev
Now many LLM apps

## Slide 8

Basics
- 
MCP
- 
Does away with the need to build M x N connectors from LLM host/agent to underlying tool
■
Don’t need to reimplement auth, error handling, rate-limiting, etc
■
Enforces consistent output format using JSON-RPC
- 
Extends from Language Server Protocols
■
Allows for proactive agentic workﬂows rather than purely reactive ones as in
LSP
- 
Integrating with tools goes from M x N
→
M + N connectors themodernsoftware.dev

## Slide 9

MCP A Bit Deeper
- 
Terminology
- 
Host
: Cursor, Claude Desktop
- 
MCP Client
: Library embedded on host (stateful session per server)
- 
MCP Server
: Lightweight wrapper in front of a tool
- 
Tool
: Callable function (could be data source, API)
- 
Flow
- 
Client calls tools/list to MCP server (what can you do?)
- 
Server returns JSON describing each tool (name, summary, JSON schema)
- 
Host injects that JSON into model’s context
- 
User prompt triggers model, emitting a structured tool call
- 
MCP server executes and conversation resumes
- 
MCP provides stdio and SSE transport layer themodernsoftware.dev

## Slide 10

themodernsoftware.dev
MCP client
Summarize my emails from Jack
MCP server
1
Ask query
2
Get tools
3
Send query and pick tool with params
4
Call function for tool and get response
Send response
5

## Slide 11

Let’s build a custom MCP server from scratch!
themodernsoftware.dev

## Slide 12

Limitations
- 
Agents don’t handle many tools very well today
- 
APIs eat up your context window quickly
- 
Design APIs to be AI-native rather that rigid themodernsoftware.dev

## Slide 13

themodernsoftware.dev
Questions?
