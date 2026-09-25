# AI code review（fall2025 W7）

## Slide 1

The Modern Software
Developer
CS146S
Stanford University, Fall 2025
Mihail Eric themodernsoftware.dev

## Slide 2

themodernsoftware.dev
Guest Lecture - 11/7/25
CPO of
Graphite
, Tomas Reimers

## Slide 3

AI Code Review themodernsoftware.dev

## Slide 4

themodernsoftware.dev

## Slide 5

- 
Software code review is one of the highest leverage activities you can do to become a better engineer and improve overall team code quality
Why themodernsoftware.dev

## Slide 6

Statistics
- 
Code review has 55-60% error detection rate compared to 25-45% for different testing modes
- 
Study of errors on programs without/with code review reported 4.5
→
0.82 errors/100 lines
- 
Study at AT&T showed code review had 14% increase in productivity and 90% decrease in defects themodernsoftware.dev
Source:
Coding Horror

## Slide 7

What to Catch
- 
Logic and correctness errors themodernsoftware.dev

## Slide 8

themodernsoftware.dev

## Slide 9

What to Catch
- 
Readability and maintainability themodernsoftware.dev

## Slide 10

themodernsoftware.dev

## Slide 11

What to Catch
- 
Performance themodernsoftware.dev

## Slide 12

themodernsoftware.dev

## Slide 13

What to Catch
- 
Security themodernsoftware.dev

## Slide 14

themodernsoftware.dev

## Slide 15

What to Catch
- 
Best practices themodernsoftware.dev

## Slide 16

themodernsoftware.dev

## Slide 17

themodernsoftware.dev
Source:
Blake Smith

## Slide 18

What’s a Good Code Review themodernsoftware.dev
This won’t work vs
I see your new method matches the existing style in this ﬁle, taking [X]
parameters. Having that many parameters hurts readability and implies the function is doing too much. What do you think about refactoring this method and the existing ones in a later pull request to reduce how many parameters they take?

## Slide 19

The New AI World
- 
Graphite
(guest lecture 11/7)
- 
Greptile
- 
Coderabbit
- 
Claude Code / Codex themodernsoftware.dev

## Slide 20

What Has Changed themodernsoftware.dev
- 
Eﬃciency
- 
Consistency
- 
Knowledge sharing
- 
Reduced cognitive load
- 
Continuous improvement
- 
Holistic understanding of your code

## Slide 21

themodernsoftware.dev
Source:
Greptile

## Slide 22

themodernsoftware.dev
Source:
Graphite

## Slide 23

Let’s See AI Code Review in Action themodernsoftware.dev

## Slide 24

Limitations themodernsoftware.dev
- 
More conﬁguration/setup
- 
False positives
- 
Have to train the system
→ continuous learning
- 
Can’t yet catch the idioms and repo best practices
- 
Can’t handle complex business logic and architecture decisions
- 
But that’s where humans are still needed
- 
Must be extra cautious with security changes
- 
Often misses edge cases
- 
Code review is more important now than ever with AI coding systems
- 
You own the code that is merged and shipped, no blaming of the AI

## Slide 25

themodernsoftware.dev
Questions?
