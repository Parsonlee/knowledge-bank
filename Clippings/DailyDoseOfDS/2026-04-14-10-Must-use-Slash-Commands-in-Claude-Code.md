---
title: 10 Must-use Slash Commands in Claude Code
source: https://mail.google.com/mail/u/0/#inbox/19d8df42bfdf06fb
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-14
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 10 Must-use Slash Commands in Claude Code 的原理剖析与工程实践。
tags:
  - clippings
---

# 10 Must-use Slash Commands in Claude Code

## 1. 核心要点解析

本期内容重点涵盖：
- **10 Must-use Slash Commands in Claude Code**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (

)​

----------------------
In today's newsletter:
----------------------

* Technical LLM interview question!
* 10 must-use slash commands in Claude Code.
* [Hands-on] Build a Real-time Federated Data Engine for Agents.

TODAY'S ISSUE

Agents
------

-----------------------------------------------------------------
​Technical LLM interview question! (

)​
-----------------------------------------------------------------

​
You have 80,000 agent trajectories from production. You need to
find top 100 worth reviewing to improve your agent.

No LLM allowed to evaluate trajectories. How will you do this?

Let’s look at some approaches.

The simplest solution one could start with is random sampling.
Pick 100 random trajectories and review.

​
But most production agents handle routine requests just fine, so
you end up wasting a big chunk of your annotation budget.

Another approach can filter for longer conversations since 10+
user messages means more complexity.

But longer conversations skew heavily toward outright failures.
You’ll surface obvious breakdowns but miss subtle issues hiding
in conversations where the agent technically succeeded.

A recent paper from DigitalOcean (

) takes a new approach.

​
It computes lightweight behavioral signals directly from the
trajectory data using deterministic rules.

The signals fall into three groups:

​
1) Interaction signals:

* If a user rephrases the request or corrects the agent, that’s
misalignment.
* Agent repeating itself is stagnation.
* User abandoning the agent is disengagement.
* User confirming something worked is satisfaction.

All are detected through normalized phrase matching and
similarity checks.

2) Execution signals:

* A tool call that doesn’t advance the task is a failure signal.
* Repeated calls with identical or drifting inputs indicate a
loop.

These are straightforward to extract from execution logs.

3) Environment signals, like rate limits, context overflow, and
API errors.

* Useful to diagnose but not for training since they reflect
system constraints, not agent decisions.

Each trajectory gets scored based on which signals fire, and you
sample the highest-signal ones for review.

On τ-bench, they compared all three approaches on 100
trajectories:

​
* Random sampling hit a 54% informativeness rate.
* The length-based heuristic reached 74%.
* Signal-based sampling reached 82%.

This means roughly 4 out of every 5 trajectories are genuinely
useful to improve the agent.

In fact, among conversations where the agent completed the task
correctly, signal sampling still identified useful patterns in
66.7% of cases vs. 41.3% for random.

These are the subtle issues like policy violations, inefficient
tool use, and unnecessary steps that don’t break the task but
still matter for optimization.

The whole framework runs without any LLM overhead and can sit
always-on in a production pipeline.

If you want to see this in practice, this signal-based approach
is already integrated into Plano (

), an open-source AI-native proxy that handles routing,
orchestration, guardrails, and observability in one place.

​Here’s the Plano GitHub repo → (

)​

​Here’s the paper on arxiv → (

)​

👉 Over to you: What is your approach to solve this?

Claude
------

-----------------------------------------------------------------
​10 must-use slash commands in Claude Code (

)​
-----------------------------------------------------------------

Setting up shell aliases is such a natural part of working in a
terminal that most developers do it almost reflexively. If you
run a command often enough, you alias it.

With Claude Code prompts, though, devs typically skip this step
entirely and keep retyping the same 10-15 line instructions from
memory, like their code review checklist, test gen constraints,
pre-commit scan...and all this session after session.

​
The real cost isn’t just the repetition you do as a dev, but the
prompt drift.

Every time you retype a prompt from memory, the wording shifts
slightly. For instance, you might forget a constraint or phrase
the expected output format differently.

With shell commands, this doesn’t matter because they’re
deterministic, but with an LLM, slightly different phrasing may
produce noticeably different output.

​
Claude Code’s custom commands fix both problems.

You can save a markdown file in .claude/commands/, and it becomes
a slash command you can invoke with identical instructions every
time.

The prompts are version-controlled through Git, so your whole
team runs the same commands, and when someone improves a prompt,
everyone gets the update on their next pull.

This is the same pattern Boris Cherny described in his thread on
Claude Code workflows, where his every repeated workflow becomes
a command, checked into Git, and shared with the team:

​
Let’s walk through how to set them up, then the 10 commands that
have been most useful in my workflow. We'll demo each one on a
real ML inference service (FastAPI, scikit-learn, Alembic) so you
can see the actual output, with full prompt templates you can
drop into your own project.

How custom commands work
------------------------

A custom command is a Markdown file inside a .claude/commands/
directory. The filename becomes the command name.

​
The file content is the prompt that gets sent to Claude when you
run the command. You can use $ARGUMENTS as a placeholder for
anything typed after the command name.

For instance, running “/dissect src/auth/session.ts” substitutes
$ARGUMENTS with “src/auth/session.ts“.

You can also inject dynamic context using shell commands with the
!command syntax:

​
Claude runs those shell commands before processing the prompt, so
the context is always fresh.

Lastly, an optional YAML frontmatter at t

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
