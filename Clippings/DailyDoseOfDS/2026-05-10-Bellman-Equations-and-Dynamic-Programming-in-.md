---
title: Bellman Equations and Dynamic Programming in RL
source: https://mail.google.com/mail/u/0/#inbox/19e13d76eb927af3
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-10
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Bellman Equations and Dynamic Programming in RL 的原理剖析与工程实践。
tags:
  - clippings
---

# Bellman Equations and Dynamic Programming in RL

## 1. 核心要点解析

本期内容重点涵盖：
- **Bellman Equations and Dynamic Programming in RL**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (

)​

----------------------
In today's newsletter:
----------------------

* Bellman equations and dynamic programming in RL.
* MCP vs CLI was the wrong debate.

* 4 strategies for multi-GPU training.

TODAY'S ISSUE

AI engineering
--------------

-----------------------------------------------------------------
​Bellman equations and dynamic programming in RL (

)​
-----------------------------------------------------------------

Recently, we launched a hands-on course series on reinforcement
learning.

​Part 3 is now available, and you can read it here → (

)​

-->​Reinforcement Learning Nanodegree Part 3 (

)
​Reinforcement Learning Nanodegree Part 3 (
https://www.dailydoseofds.com/rl-course-part-3/ )Part 2 covered
the MDP framework and value functions. This one teaches you the
equations and algorithms that actually compute them.

​
It covers:

* The Bellman expectation equations
* the Bellman optimality equations
* and the dynamic programming methods built on top of them, like
iterative policy evaluation, policy improvement, policy
iteration, and value iteration, with hands-on implementations.

Everything is covered from scratch, so no RL background is
required.

​You can read Part 3 of the course here → (

)​

Why care?
---------

Most ML practitioners today have deep intuition for supervised
learning.

But RL operates on a fundamentally different set of ideas. There
is no labeled dataset. The agent generates its own training data
through interaction. Actions have delayed consequences.
Exploration is not optional but rather a core part of the
learning process.

This is also where the biggest breakthroughs in AI are
compounding right now. The field is having its moment, and the
demand for engineers who understand it deeply is growing fast.

* Every technique that made recent LLMs dramatically better
(RLHF, GRPO, DPO, constitutional AI) is a direct application of
RL.
* Every agentic system that takes multi-step actions, calls
tools, and operates over long horizons is an RL problem.

When you read about these in a paper or blog post, they only land
if you understand what a policy is, what a value function
measures, why reward shaping is hard, and how exploration works.

This series builds that understanding from the ground up, concept
by concept, with math where it matters and hands-on code you can
run.

This series is structured the same way as our MLOps/LLMOps course
(

): concept by concept, with clear explanations, diagrams, math
where it matters, and hands-on implementations you can run.

And no prior RL background is needed.

* ​If you haven’t read Part 1, start there first. It covers the
agent-environment loop, exploration vs. exploitation, and
multi-armed bandits → (

)​
* ​And part 2 covers Markov Decision Processes and Value
Functions (the formal language that every RL algorithm is built
on) → (

)​

Over to you: What topics would you like us to cover in this RL
series?

deep dive
---------

-----------------------------------------------------------------
​MCP vs CLI was the wrong debate (

)​
-----------------------------------------------------------------

For most of 2025, AI engineers argued about how agents should
call tools.

One group asked using MCP (

), the protocol Anthropic released for connecting agents to
external services. The other group asked to skip the protocol and
just give the agent a shell.

Both sides had real arguments. Both sides were also missing the
point.

*************************
What each group got right
*************************

The skeptics measured what MCP servers actually cost in context:

​
* Playwright MCP eats 13.7K tokens
* Chrome DevTools MCP eats 18K
* A 5-server setup burns 55K tokens before any work

The defenders pushed back with the multi-tenant case:

* CLIs break on multi-tenant apps
* No typed contracts, so the agent guesses at outputs
* On unfamiliar APIs, agents waste turns parsing text

​
If you are reading this and thinking "which one wins?", that was
the wrong question.

***********
The reframe
***********

On November 4, 2025, Anthropic published "Code execution with
MCP" and changed this conversation.

The problem was never the protocol but rather the habit of
loading every tool's full description into context the moment a
session starts.

If you added the data those tools returned, passed through the
model on every step, and a single workflow could balloon to 150K
tokens.

The fix proposed was to flip the model's job. Instead of calling
tools through its context, the model writes code that calls tools
through a runtime. The model only sees what it imports.

In Anthropic's example, a Google Drive transcript flows into a
Salesforce CRM update. The old way loaded both tool schemas and
piped the transcript through the model twice. The new way
involved a few lines of TypeScript that import what they need,
completed in just 2k tokens (A 98.7% drop).

Cloudflare pushed it further. They collapsed their entire
2,500-endpoint API from 1.17M tokens of schemas down to 1K tokens
by exposing just two functions: `search` and `execute`. The agent
writes code that searches the catalog, then executes only what
matches.

​

*************************
The new Code Mode pattern
*************************

Code Mode is a runtime where the agent writes code that mixes two
primitives.

1) Bash, for anything with a binary already installed like git,
curl, or grep. The model has seen these in training data and
knows how to compose them. Need to find every Python file that
imports pandas? The agent writes one line:

​
There's no tool definition needed, and the shell does the work.

2) Typed module imports, for proprietary APIs like Salesforce,
Stripe, or your internal services. Think of these as small
TypeScript f

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
