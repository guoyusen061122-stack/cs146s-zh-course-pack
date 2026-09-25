# AI QA, SAST, DAST, and Beyond（fall2025 W6）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University, Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

themodernsoftware.dev
Guest Lecture - 10/31/25
CEO of
Semgrep
, Isaac Evans

## Slide 3

AI Testing and Security themodernsoftware.dev

## Slide 4

- 
Software errors can dash user trust in a product/company and incur huge ﬁnancial costs
- 
When an LLM is writing most of your code, you need extensive guardrails to prevent those errors
Why themodernsoftware.dev

## Slide 5

Existing threat landscape
- 
SQL injections
- 
Cross-site scripting
- 
Broken authentication
- 
Insecure direct object references
- 
Security misconﬁgurations
- 
Sensitive data exposure themodernsoftware.dev

## Slide 6

Vulnerability detection techniques
- 
SAST
- 
DAST
- 
SCA themodernsoftware.dev

## Slide 7

SAST
- 
S tatic
A pplication
S ecurity
T esting
- 
White box testing technique
- 
Analyzes binaries and source code
- 
Happens early in software development life cycle when much cheaper to identify and correct
- 
Identify vulnerabilities like SQL injections, command injections, cross-site scripting
- 
Techniques
- 
Codebase scan with pattern matching themodernsoftware.dev

## Slide 8

DAST
- 
D ynamic
A pplication
S ecurity
T esting
- 
Black box testing technique
- 
Mimic actions of real-world hackers to uncover vulnerabilities
- 
Can happen throughout SDLC and offers fewer false positives
- 
Identify vulnerabilities like SQL injections, broken authentication, cross-site scripting
- 
Techniques
- 
Input fuzzing
- 
Manipulating session tokens
- 
Conﬁguration/header testing
- 
Brute force rate-limit tests themodernsoftware.dev

## Slide 9

SCA
- 
S oftware
C omposition
A nalysis
- 
Deep analysis of OSS packages used by application
- 
Perform analysis of package managers, infrastructure-as-code, pull images to ﬁnd vulnerabilities
- 
Techniques
- 
Analyze package metadata for dependencies
- 
Transitive dependency resolution
- 
Match against DB of vulnerabilities
- 
Binary/artifact scanning themodernsoftware.dev

## Slide 10

What has changed themodernsoftware.dev
- 
Bad: new AI agent attack vectors
- 
Good: new techniques for improving SAST/DAST/SCA

## Slide 11

New AI agent attack vectors themodernsoftware.dev
- 
Prompt injection
- 
Hidden or misleading instructions to gen AI system to make it deviate from intended behavior

## Slide 12

themodernsoftware.dev

## Slide 13

themodernsoftware.dev

## Slide 14

New AI agent attack vectors themodernsoftware.dev
- 
Tool misuse
- 
Manipulate agent through deceptive prompts to abuse its integrated tools

## Slide 15

themodernsoftware.dev

## Slide 16

New AI agent attack vectors themodernsoftware.dev
- 
Code attacks
- 
Exploit agent’s ability to execute code to gain unauthorized access to execution environment

## Slide 17

themodernsoftware.dev

## Slide 18

New AI agent attack vectors themodernsoftware.dev
- 
Prompt injection
- 
Hidden or misleading instructions to gen AI system to make it deviate from intended behavior
- 
Tool misuse
- 
Manipulate agent through deceptive prompts to abuse its integrated tools
- 
Intent breaking
- 
Manipulate agent’s plan to redirect actions away from original intent
- 
Identity spooﬁng
- 
Exploit compromised authentication to pose as legitimate agents
- 
Code attacks
- 
Exploit agent’s ability to execute code to gain unauthorized access to execution environment

## Slide 19

What has changed themodernsoftware.dev
- 
“Shift left” security is more accessible than ever
- 
LLMs can be introduced in a workﬂow to spot issues
- 
Automated penetration testing

## Slide 20

How LLMs are used for security and testing themodernsoftware.dev

## Slide 21

Limitations themodernsoftware.dev
- 
In AI SAST, false positive rates are incredibly high
- 
Claude Code/Codex can be 50-100% depending on the vulnerability
- 
Compare to 50+% for traditional SAST techniques
- 
Existing benchmarks are often unrealistic so hard to evaluate LLM
- 
Nondeterministic analysis
- 
Run the same prompt multiple times and get different results
→ how do you know you’re catching all vulnerabilities?
- 
Context rot
■
Not all context is created equally
- 
Compaction
■
Summarize so that things ﬁt into context

## Slide 22

Open Questions themodernsoftware.dev
- 
How to reduce false positives and hallucinations in vulnerability detection?
- 
How do we verify that LLM-generated patches are secure and don’t introduce regressions?
- 
How can LLMs explain why they ﬂag a vulnerability or propose a ﬁx?
- 
What are the right benchmarks for measuring LLMs’ AppSec performance?
- 
How should LLMs be embedded in CI/CD without overwhelming teams with noise?
- 
Who is accountable if an AI-generated patch introduces a vulnerability?
