# From first prompt to optimal IDE setup（fall2025 W3）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University, Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

themodernsoftware.dev
Guest Lecture - 10/10/25 (8:30am PT, 420-041)
Cognition
Head of Research, Silas Alberti

## Slide 3

The AI IDE: Fundamentals to
Power User themodernsoftware.dev

## Slide 4

Why
- 
IDE (Integrated Development Environment)
- 
All-in-one workspaces for software development containing editor, compiler, debugger, and more
- 
Most development work is done there so it’s a natural form factor for AI enhancement
- 
In their evolution, there’s always a see-saw between functionality consolidation and developer customization themodernsoftware.dev

## Slide 5

A brief history themodernsoftware.dev
2001
Intellij IDEA released with advanced contextual code navigation, refactoring, code completion
2015
Microsoft VSCode released offering lightweight editor with highly extensible ecosystem
1983
Release of Turbo Pascal, ﬁrst true IDE
1997
Microsoft Visual Studio released, offering advanced debugging capabilities for the C++/Visual Basic language
1980
2030
2023
Cursor released, one of the ﬁrst widely used AI native
IDEs

## Slide 6

Usage
- 
Bread-and-butter modes
- 
Inline
- 
Function
- 
Single-ﬁle
- 
Multi-ﬁle
- 
True AI-native
- 
Background agents
- 
MCP
- 
Learn memories
- 
Bugbot (PR review)
themodernsoftware.dev

## Slide 7

Let’s see some of this in action themodernsoftware.dev

## Slide 8

How an AI IDE works under-the-hood themodernsoftware.dev
Tab-complete
- 
Small context window around current code is encrypted
- 
Server receives and runs inﬁlling
LLM
- 
Suggestion sent back and displayed
Chat
- 
Store code chunks as embeddings in semantic index on server
(obfuscated ﬁlename + code)
- 
Any query retrieves most relevant chunks and feeds as context into
LLM
- 
IDE regularly re-index code chunks and syncs embeddings
- 
Chunk diffs are computed via Merkle trees for eﬃcient updates

## Slide 9

- 
For simple changes you don’t have to be too thoughtful about prompting
- 
For more complex tasks, you’re going to become a product manager
- 
Carefully crafted specs doc themodernsoftware.dev
Best practices

## Slide 10

- 
Goal
- 
What is the purpose of the change
- 
Deﬁnitions
- 
What prereqs does the LLM need to know about the problem
- 
Plan
- 
High-level implementation breakdown
- 
Source ﬁles being changed
- 
What parts of the codebase are relevant and why
- 
Test cases
- 
How will testing be done
- 
Edge cases
- 
What special cases need to be accounted for
- 
Out-of-scope
- 
What should *not* be changed
- 
Extensions
- 
What changes will be relevant later so the LLM can future-proof its design and not take shortcuts themodernsoftware.dev
Best practices

## Slide 11

Let’s see some of this in action themodernsoftware.dev

## Slide 12

- 
Optimize your codebase so that a human and an agent could understand what’s going on
- 
Much of LLM confusion comes from trying to ﬁnish a task with a messy repo as context
- 
Provide optimal context for LLMs by describing
- 
Repo orientation
- 
File structure
- 
Setup and environment
- 
Best practices
- 
Code style
- 
Access patterns
- 
APIs and contracts
- 
All of this should be thoroughly documented
- 
Tip:
a monorepo design in your repo is highly encouraged themodernsoftware.dev
Best practices

## Slide 13

- 
Help LLM navigate your codebase with agent conﬁgurations
- 
claude.md
■
CLAUDE.md is a special file that Claude automatically pulls into context when starting a conversation. This makes it an ideal place for documenting: common bash commands, core files and utility functions, code style guidelines, testing instructions.
- 
c ursorrules
- 
AGENTS.md
■
Open format
- 
llms.txt
■
Provide that navigation guidance for LLMs scraping the web
- 
Note:
The agents won’t always adhere to these descriptions/directives. They are intended as guidance.
themodernsoftware.dev
Best practices

## Slide 14

themodernsoftware.dev
Samples

## Slide 15

Let’s see some of this in action themodernsoftware.dev
