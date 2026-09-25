# Boris Cherney, Creator of Claude Code（fall2025 W4）

## Slide 1

welcome to claude code boris cherny

## Slide 2

tl;dr
1.
programming is changing
2.
choose your path with claude code
3.
think six months out

## Slide 3

npm install -g @anthropic-ai/claude-code claude.ai/code

## Slide 4

1/ programming is at an inflection point

## Slide 5

programming language productivity is increasing exponentially, driven by ai
1950 1960 1970 1980 1990 2000 2010 2020 2030 log(productivity)
fortran algol cobol basic c pascal prolog c++ python java js go rust
✻
✻
✻
✻ haskell swift ts

## Slide 6

1950 1960 1970 1980 1990 2000 2010 2020 2030 ed emacs vi turbo pascal qbasic vb eclipse idea sublime cursor copilot
✻
✻
✻ devin
✻ ide productivity is following a similar exponential, also driven by ai smalltalk-80 neovim log(productivity)
claude code

## Slide 7

ibm 029 (1964)

## Slide 8

ed (1969)

## Slide 9

smalltalk-80 (1980)

## Slide 10

visual basic (1991)

## Slide 11

eclipse (2001)

## Slide 12

copilot (2021)

## Slide 13

devin (2024)

## Slide 14

ide devx has evolved quickly, and will continue to change even more quickly

## Slide 15

verification is evolving quickly, too
- manual debugging
- static types (algol)
- formal verification
- abstract interpretation
- automated testing
- continuous integration
- property-based testing (quickcheck)
- dependent typing
- e2e testing
- chaos testing (chaos monkey)
- ai-powered vulnerability testing
- ai-powered unit testing (testgen)
- ai-powered fuzz testing (sapienz)
- self play
-
...

## Slide 16

2/ claude code’s approach

## Slide 17

claude code’s approach:
works everywhere
1.
terminal-native
2.
low-level model access
3.
infinitely hackable

## Slide 18

18
1. Discover
2. Design
3. Build
4. Deploy
5. Support & Scale
Explore codebase and history
Search documentation
Onboard & learn
Plan project
Develop tech specs
Deﬁne architecture
Implement code
Write and execute tests
Create commits and PRs
Automate CI/CD
Conﬁgure environments
Manage deployments
Debug errors
Large-scale refactor
Monitor usage & performance
Using and mastering all of your team’s CLI tools (e.g., git, docker, bq) so you can focus on solutions, not syntax works across the whole sdlc

## Slide 19

3/ one
✻ code, many faces

## Slide 20

terminal

## Slide 21

ide

## Slide 22

web & ios

## Slide 23

/install-github-app

## Slide 24

sdk
$ claude -p \
“what did i do this week?” \
--allowedTools Bash(git log:*)
--output-format stream-json claude models anthropic, bedrock, or vertex api claude code sdk your app

## Slide 25

sdk
$ get-gcp-logs 1uhd832d | claude -p "correlate errors + commits" \
--output-format=json | jq '.result'
claude models anthropic, bedrock, or vertex api claude code sdk your app

## Slide 26

4/ using claude code

## Slide 27

use cases
1. codebase q&a + research
2. write code a. 1-shot b. sidekick c. prototype
3. integrate tools & mcps
4. power automation

## Slide 28

1. ask claude code about your code
> how do I make a new
@app/services/ValidationTemplateFactory
?
> why does recoverFromException take so many arguments? look through git history to answer
> why did we fix issue #18363 by adding the if/else in
@src/login.ts api?
> in which version did we release the new
@api/ext/PreHooks.php api?
> look at PR #9383, then carefully verify which app versions were impacted
> what did I ship last week?

## Slide 29

2. teach claude to use your tools
> use the barley cli to check for error logs
$ claude mcp add barley_server -- node myserver
> use the barley mcp server to check for error logs

## Slide 30

3. fit the workflow to the task explore › plan › confirm › code › commit
> figure out the root cause for issue #983, then propose a few fixes. Let me choose an approach before you code. ultrathink

## Slide 31

3. fit the workflow to the task tests › commit › code › iterate › commit
> write tests for
@utils/markdown.ts to make sure links render properly
(note the tests won’t pass yet, since links aren’t yet implemented). then commit. then update the code to make the tests pass.

## Slide 32

3. fit the workflow to the task code › screenshot › iterate
> implement [mock.png]. Then screenshot it with puppeteer and iterate till it looks like the mock.

## Slide 33

4. use claude code to prototype

## Slide 34

> make it so instead of todos showing up as they come in, we hide the tool use and result for todos, and render a fixed todo list above the input. title it
"/todo (1 of 3)" in grey

## Slide 35

> actually don't show a todo list at all, and instead render the tool uses inline, as bold headings when the model starts working on a todo. keep the
"step 2 of 4" or whatever, and add middot /todo to see after in grey

## Slide 36

> also add a todo pill under the text input, similar to bg tasks. it should render "todos: 1 of 3" or whatever. make the pill interactive

## Slide 37

> actually undo both the pill and headings. instead, make the todo list render to the right of the input, vertically centered with a grey divider. show it when todos are active, hide it when it's done

## Slide 38

> actually what if you show the todo list above the input instead. truncate at
5 and show "... and 4 more" or whatever. add a heading "Todo:" in grey text

## Slide 39

> actually what if you show the todo list above the input instead. truncate at
5 and show "... and 4 more" or whatever. add a heading "Todo:" in grey text

## Slide 40

> actually what if you show the todo list above the input instead. truncate at
5 and show "... and 4 more" or whatever. add a heading "Todo:" in grey text

## Slide 41

> instead of showing todos above the input, merge them into the spinner. show the current todo as the spinner message in active verb form, and the next todo instead of the spinner tip, in passive form. also add a /todos slash command to see all todos, and mention it next to "esc to interrupt"

## Slide 42

> make it so i can hit ctrl+t to expand todos inline. also rm the "esc to interrupt" message when we show the todos, and replace it w "ctrl+t to expand"

## Slide 44

6/ lessons

## Slide 45

1. build for the model six months from now

## Slide 46

2. be ready to evolve

## Slide 47

3. ask not what the model can do for you

## Slide 48

4.

## Slide 49

thanks!
npm install -g @anthropic-ai/claude-code claude.ai/code boris@anthropic.com
