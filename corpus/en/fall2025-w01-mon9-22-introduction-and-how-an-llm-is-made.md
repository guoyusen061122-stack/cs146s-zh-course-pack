# Introduction and how an LLM is made（fall2025 W1）

## Slide 1

Structured Writing for
Professionals
English 170
Stanford University, Fall 2025
Mihail Eric

## Slide 2

The Modern Software
Developer
CS146S
Stanford University, Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 3

Introduction and How LLMs are Made themodernsoftware.dev

## Slide 4

State of the World: 2025 themodernsoftware.dev

## Slide 5

Bad News themodernsoftware.dev
-
Windsurf team

## Slide 6

Good News
- 
Software developers have the potential to be more productive than they have ever been in history
- 
With AI coding an engineer can pick up tech stacks and tools at an unprecedented pace
- 
You won’t be replaced by AI. You’ll be replaced by a competent engineer who knows how to use AI.
themodernsoftware.dev

## Slide 7

The Modern Software
Developer themodernsoftware.dev

## Slide 8

This is not the “vibe coding” class themodernsoftware.dev

## Slide 9

10 weeks in 2 slides themodernsoftware.dev

## Slide 10

The Takeaway
- 
Human-agent engineering
- 
Focus on the skills that are not yet replaced by AI systems
- 
Business understanding
- 
Become the tech lead
- 
LLMs are only as good as you are
- 
Good context leads to good code
- 
If you can’t understand your codebase, neither will an LLM themodernsoftware.dev

## Slide 11

The Takeaway
- 
Read and review a lot of code
- 
Learn to discern good from bad, wrong software
- 
Have good taste
- 
Experiment aggressively
- 
There are no established software patterns yet
- 
Everyone is still ﬁguring it out
- 
This class will introduce many workﬂows and tools - ﬁgure out what works for you themodernsoftware.dev

## Slide 12

Course Logistics
- 
A bit about me
- 
Stanford undergrad/grad
- 
Head of AI at a stealth startup in the sales space
- 
Built ﬁrst LLMs at Amazon Alexa
- 
Founded and sold an ML education startup
- 
Founded a YC-backed AI coding company
- 
1 awesome CA
- 
Febie Lin themodernsoftware.dev

## Slide 13

Course Logistics
- 
https://themodernsoftware.dev
- 
Lectures
- 
Mon/Fri 8:30-9:20 am
- 
Deliverables
- 
9 assignments (1x/week) focusing on lecture material practice
■ https://github.com/mihail911/modern-software-dev-assignments
- 
1 ﬁnal open-ended project in which you will exercise AI coding principles we cover
- 
Grading
- 
80/15/5 breakdown for project/assignments/participation
- 
Something pretty awesome
- 
Guest lectures from founders leading top AI developer startups today
- 
$100s of millions raised, billions in valuation
- 
Don’t miss these talks!
themodernsoftware.dev

## Slide 14

How LLMs Work in 5 Slides
(For Engineers)
themodernsoftware.dev

## Slide 15

Basics
- 
LLMs (large language models) are autoregressive models for next-token prediction themodernsoftware.dev

## Slide 16

Basics themodernsoftware.dev a for loop for
Embedding layer
0.3 the
0.6 idx
0.1 cat
Tokenize inputs using ﬁxed vocabulary
Convert tokens into ﬁxed-dimensional numerical vectors (~1-3K dimensions)
Transformers layers (12-96+) using self-attention mechanism (Viswani et.
al. 2017)
Get probability distribution over most likely next token

## Slide 17

Training Process
- 
Stage 1
- 
Self-supervised pretraining
- 
Teach the model notion of language on a variety of often public data sources
- 
100s of billions to trillion+ tokens (language and code)
- 
Common Crawl, Wikipedia, StackExchange, Public Github repos
- 
Write a for loop
→ that could be used in a piece of code
- 
Stage 2
- 
Supervised ﬁnetuning
- 
Teach model to follow instructions
- 
High-quality, curated prompt-response pairs (“ what is the capital of Croatia
” -> “
Zagreb is the capital
”)
- 
Tens of thousands to 100s of thousands of pairs
- 
Write a for loop
→ ok here’s a for loop…
- 
Stage 3
- 
Preferencing tuning
- 
Align model outputs with human preferences (helpfulness, correctness, readability)
- 
Collect pairs of outputs for same prompt and train reward model to predict preferred output
- 
Tens of thousands to 100s of thousands of human-labeled comparisons
- 
Write a for loop
→ for idx in range(10):
themodernsoftware.dev

## Slide 18

Training Process
- 
Reasoning models
- 
Extend training with chain-of-thought reasoning traces
- 
Tool-use integration
- 
Get human preferences on reasoning steps
- 
Reinforcement learning to learn how to evaluate reasoning traces, backtrack, etc
- 
Size
- 
GPT-3/Claude 3.5 Sonnet - 175B parameters
- 
LLaMA 3.1 - 405B parameters
- 
GPT-4 - 1.8T (reported)
themodernsoftware.dev

## Slide 19

In practice
- 
Strengths
- 
Expert-level code completion
- 
Code understanding
- 
Code ﬁxing
- 
Limitations
- 
Hallucinations
■
Generating non-existent/out-of-date APIs (mitigated with robust context engineering)
- 
Context window limits
■
~100-200K tokens but not all are created equal
- 
Latency
■
Seconds to minutes per request depending on task (plan and delegate accordingly)
- 
Cost
■
$1-3 per million input tokens, $10+ per million output tokens for best models themodernsoftware.dev

## Slide 20

themodernsoftware.dev
Questions?
