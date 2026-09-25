# Tomas Reimers, CPO Graphite（fall2025 W7）

## Slide 1

CS146S
∙
Stanford University, Fall 2025
The Modern Software Developer:
Code Review

## Slide 2

Agenda
00
Hi!
01
Collaborating with humans
02
Collaborating with AI
03
Software development in the limit

## Slide 3

Hi!
Who am I?
What is Graphite?

## Slide 4

Graphite is the AI-powered code review platform helping developers create, review, and merge code changes.

## Slide 5

The AI-native code review platform
INTRODUCTION
Our AI agent can answer questions about the PR.
It is fully codebase aware.
It can also propose updates, helping reviewers quickly resolve comments and CI.

## Slide 6

A best-in-class code review platform built on-top of GitHub.
Graphite provides a streamlined interface to create, review, and merge PRs, instantly and bi-directionally synced with GitHub.
Trusted by the developers and companies you already know.
We’re fortunate enough to collaborate with some of the biggest names in technology, and improve developer velocity across a wide swath of metrics.
Conﬁdential
INTRODUCTION
Graphite at a glance
Graphite helps engineers ship more.
+33%
Increase in PRs shipped per developer after adopting Graphite at Shopify
100,000s+
Trusted by 100,000s of developers at
1,000s of organizations
+21%
LoC/eng at
Asana
-74%
Time between
PRs merged at
Ramp

## Slide 7

Collaborating with humans
How developers work together

## Slide 8

COLLABORATING WITH HUMANS
How developers collaborate
A developer proposes a set of code changes, this atomic unit is called a pull request
.
(a.k.a. diff, patch, changelist, or merge request)
The original developer merges their pull request back into the codebase.
CREATE
REVIEW
MERGE
Another developer reﬁnes
(suggests improvements) through comments and ultimately approves the pull request.

## Slide 9

AI means more code than ever is being created, but that also means more code needs to be reviewed and merged
.

## Slide 10

IBM, 1976: an engineer named
Michael Fagan introduces
Fagan
Inspections
.
(
Link to paper
)
The birth of code review: Fagan Inspections
COLLABORATING WITH HUMANS

## Slide 11

Emailed patches replace printed code.
The Linux kernel still does this.
The birth of code review: Email patches
COLLABORATING WITH HUMANS
From
Icenowy Zheng <REDACTED>
Subject
[PATCH v3 5/7] clk: sunxi-ng: add support for the Allwinner H6 CCU
Date
Fri, 23 Feb 2018 20:35:53 +0800
The Allwinner H6 SoC has a CCU which has been largely rearranged.
Add support for it in the sunxi-ng CCU framework.
diff --git a/…/bindings/clock/sunxi-ccu.txt b/…/bindings/clock/sunxi-ccu.txt index 4ca21c3a6fc9..9ae27881c924 100644
--- a/…/bindings/clock/sunxi-ccu.txt
+++ b/…/bindings/clock/sunxi-ccu.txt
@@ -20,6 +20,7 @@ Required properties :
- "allwinner,sun50i-a64-ccu"
- "allwinner,sun50i-a64-r-ccu"
- "allwinner,sun50i-h5-ccu"
+
- "allwinner,sun50i-h6-ccu"
- "nextthing,gr8-ccu"

## Slide 12

Google, early 2000s: Guido van Rossum* introduces
Mondrian
: a web UI for review.
- yes, Python’s Benevolent
Dictator
The birth of code review: Mondrian
COLLABORATING WITH HUMANS

## Slide 13

Tools such as:
- 
Review Board
- 
Gerrit / Critique (Google)
- 
Phabricator (Facebook)
- 
GitHub
Make their way into the public tool chain, popularizing the practice of code review
.
The birth of code review: Online tools
COLLABORATING WITH HUMANS

## Slide 14

Collaborating with AI
Keeping up with super-human authors.

## Slide 15

AI can already catch more than typos
Graphite will proactively scan
PRs for bugs.
It posts potential issues to both Graphite and GitHub.
It works great out of the box and is fully customizable.
COLLABORATING WITH AI

## Slide 16

COLLABORATING WITH AI
With AI, do humans even need to do code review?

## Slide 17

01
Alignment conﬁrmation
02
Knowledge diffusion
Proofreading
03
The purpose(s) of code review
(in order)
COLLABORATING WITH AI

## Slide 18

COLLABORATING WITH AI
How will humans collaborate with AI?
Better for context gathering and augmenting human reviewers.
Better for replacing human reviewers entirely.
PLATFORM
PARTICIPANT

## Slide 19

Live demo

## Slide 20

The limits of AI (today)
COLLABORATING WITH AI

## Slide 21

The limits of AI (tomorrow)
COLLABORATING WITH AI

## Slide 22

Software development in the limit
Where do we go from here.

## Slide 23

Software development has always had two parts
IN THE LIMIT

## Slide 24

Software development has always had two parts
The “inner loop”
focused on development
IN THE LIMIT

## Slide 25

Software development has always had two parts
The “outer loop”
focused on review
& collaboration
IN THE LIMIT

## Slide 26

AI is already making the inner loop 10x faster
IN THE LIMIT

## Slide 27

What happens to the outer loop?
IN THE LIMIT

## Slide 28

IN THE LIMIT
Three doors for the next generation software dev
Developers directly review changes, augmented by AI.
If they’re not authoring the code, does this still make sense?
Developers treat AI as a third-party contractor.
Underwriting product requirements but not code
.
CYBORG
EM
AGENCY
Developers manage
AI directly.
Underwriting architecture, but maybe not technical speciﬁcs.

## Slide 29

AI Review Agent
Graphite Agent is your AI-powered companion to catch bugs, enforce your organization’s conventions, and make sure errors and security vulnerabilities stay out of your codebase.
Smarter CI
Predictive CI that only runs when you need it. Saving your team time and money.
A review experience built for teams
Supercharge your team with reviewer assignment, merge queues, automations, and insights.
Measure developer productivity
See exactly how much more efﬁcient
AI-generated coding tools & Graphite’s code review are making your developers with actionable insights.
Stacking
A git workﬂow optimized for authors who want to keep developing without being blocked on their reviewers.

## Slide 30

Thank you! Any questions?
