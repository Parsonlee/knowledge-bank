---
title: The Anatomy of an Agent Harness
source: https://mail.google.com/mail/u/0/#inbox/19d64a1fd91e185f
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-06
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 The Anatomy of an Agent Harness 的原理剖析与工程实践。
tags:
  - clippings
---

# The Anatomy of an Agent Harness

## 1. 核心要点解析

本期内容重点涵盖：
- **The Anatomy of an Agent Harness**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (

)​

----------------------
In today's newsletter:
----------------------

* The Canvas Framework: A structured approach to building
production Agents.
* The Anatomy of an Agent Harness.

TODAY'S ISSUE

together with MongoDB
---------------------

-----------------------------------------------------------------
​The Canvas Framework: A structured approach to building
production Agents (

)​
-----------------------------------------------------------------

Before foundation models, building an AI feature involved
collecting and labeling training data, training a custom model
from scratch, and only then integrating it into a product. This
took months and a massive compute investment before teams could
even test whether users wanted the feature.

​
Foundation models removed that bottleneck because they come
pre-trained and accessible via API. Teams can now call GPT-4 or
Claude with zero-shot or few-shot prompts, ship an MVP in days,
validate user demand first, and only then invest in curating data
for RAG or fine-tuning.

But for agentic systems, there’s a missing layer.

Agent design needs to come right after defining the product,
because the agent’s capabilities, workflows, and memory
requirements are what determine what knowledge it needs and which
model providers make sense downstream.

​
MongoDB published a detailed breakdown of the Canvas Framework (

) built around this exact sequence. It uses two planning
canvases.

* The POC canvas has 8 squares covering product validation, agent
design (capabilities, autonomy boundaries, memory requirements),
data requirements (knowledge sources, update frequency, feedback
loops), and model integration (provider selection, prompt
strategy, cost validation)
* The production canvas adds 11 squares for scaling, including
fault tolerance, multi-agent coordination, unified data
architecture across application storage, vector search, and agent
memory, plus security hardening and governance.

​You can read the full breakdown here → (

)​

Claude
------

-------------------------------
The Anatomy of an Agent Harness
-------------------------------

A ReAct loop (

), a couple of tools, and a well-written system prompt can get
surprisingly far in a demo.

But the moment the task requires 10+ steps, things fall apart
like the model forgets what it did three steps ago, tool calls
fail silently, and the context window fills up with garbage.

​
The problem isn't the model. It's everything around the model.

LangChain proved this when they changed only the infrastructure
wrapping their LLM (same model, same weights) and jumped from
outside the top 30 to rank 5 on TerminalBench 2.0.

A separate research project hit a 76.4% pass rate by having an
LLM optimize the infrastructure itself, surpassing hand-designed
systems.

That infrastructure has a name now: the agent harness.

What is Agent Harness?
----------------------

The term was formalized in early 2026, but the concept existed
long before.

The harness is the complete software infrastructure wrapping an
LLM, including the orchestration loop, tools, memory, context
management, state persistence, error handling, and guardrails.

Anthropic’s Claude Code documentation puts it simply: the SDK is
“the agent harness that powers Claude Code.“

We really liked the canonical formula, from LangChain’s Vivek
Trivedy: “If you’re not the model, you’re the harness.”

To put it another way, the “agent” is the emergent behavior: the
goal-directed, tool-using, self-correcting entity the user
interacts with. The harness is the machinery producing that
behavior. When someone says “I built an agent,” they mean they
built a harness and pointed it at a model.

​
Beren Millidge made this analogy precise in his 2023 essay:

* A raw LLM is a CPU with no RAM, no disk, and no I/O.
* The context window serves as RAM (fast but limited).
* External databases function as disk storage (large but slow).
* Tool integrations act as device drivers.

The harness is the operating system.

Three levels of engineering
---------------------------

Three concentric levels of engineering surround the model:

* Prompt engineering crafts the instructions the model receives.
* Context engineering manages what the model sees and when.
* Harness engineering encompasses both, plus the entire
application infrastructure: tool orchestration, state
persistence, error recovery, verification loops, safety
enforcement, and lifecycle management.

The harness is not a wrapper around a prompt. It is the complete
system that makes autonomous agent behavior possible.

The 11 components of a production Harness
-----------------------------------------

Synthesizing across Anthropic, OpenAI, LangChain, and the broader
practitioner community, a production agent harness has eleven
distinct components. Let’s walk through each one.

​

1. The Orchestration Loop
-------------------------

This is the heartbeat. It implements the
Thought-Action-Observation (TAO) cycle, also called the ReAct
loop. The loop runs: assemble prompt, call LLM, parse output,
execute any tool calls, feed results back, repeat until done.

Mechanically, it’s often just a while loop. The complexity lives
in everything the loop manages, not the loop itself. Anthropic
describes their runtime as a “dumb loop” where all intelligence
lives in the model. The harness just manages turns.

2. Tools
--------

Tools are the agent’s hands. They’re defined as schemas (name,
description, parameter types) injected into the LLM’s context so
the model knows what’s available. The tool layer handles
registration, schema validation, argument extraction, sandboxed
execution, result capture, and formatting results back into
LLM-readable observations.

Claude Code provides tools across six categories: file
operations,

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
