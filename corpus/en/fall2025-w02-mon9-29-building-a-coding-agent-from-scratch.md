# Building a coding agent from scratch（fall2025 W2）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University, Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

Building a Coding Agent From
Scratch themodernsoftware.dev

## Slide 3

themodernsoftware.dev
It’s that simple

## Slide 4

Terminology
- 
System prompt
- 
Deﬁne the behavior and some directives for the overall LLM
- 
User prompt
- 
Custom user requests
- 
Assistant prompt
- 
LLM’s response themodernsoftware.dev

## Slide 5

Steps
- 
Read in terminal and keep appending to conversation
- 
Tell LLM what tools are available
- 
It asks for tool use at appropriate time
- 
You execute tool oﬄine and return response
- 
“Read_ﬁle”
- 
“List_dir”
- 
“Edit_ﬁle”
- 
Create a new ﬁle, edit a new ﬁle themodernsoftware.dev

## Slide 6

Let’s build a coding agent from scratch!
themodernsoftware.dev

## Slide 7

The “Secret” Sauce
- 
Looking under the hood of Claude
- 
Front-load context with tiny targeted prompts
- 
System reminders everywhere including system/user prompts, tool calls, tool results to prevent drift (<system-reminder> tags)
- 
Command preﬁx extraction
- 
Spawns sub agents (likely to help with preventing context overloading)
themodernsoftware.dev
