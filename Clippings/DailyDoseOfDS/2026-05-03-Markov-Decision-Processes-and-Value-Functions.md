---
title: Markov Decision Processes and Value Functions in RL
source: https://mail.google.com/mail/u/0/#inbox/19deeeb458239986
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-03
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Markov Decision Processes and Value Functions in RL 的原理剖析与工程实践。
tags:
  - clippings
---

# Markov Decision Processes and Value Functions in RL

## 1. 核心要点解析

本期内容重点涵盖：
- **Markov Decision Processes and Value Functions in RL**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (

)​

----------------------
In today's newsletter:
----------------------

* Markov decision processes and value functions in RL.
* How LLM inference works internally.

TODAY'S ISSUE

AI engineering
--------------

-----------------------------------------------------------------
​Markov decision processes and value functions in RL (

)​
-----------------------------------------------------------------

Last week, we launched a hands-on course series on reinforcement
learning.

​Part 2 is now available, and you can read it here → (

)​

-->​Reinforcement learning nanodegree part 2 (

)
​Reinforcement learning nanodegree part 2 (
https://www.dailydoseofds.com/rl-course-part-2 )Part 1 gave you
the RL interaction loop and the exploration-exploitation tradeoff
through bandits, and this one gives you the formal language that
every RL algorithm is built on.

​
It covers:

* the Markov property and why it makes RL tractable
* the MDP as a 5-tuple (states, actions, transitions, rewards,
discount factor)
* episodic vs. continuing tasks
* returns and discounting with concrete numerical examples
* the reward hypothesis and its limits (including reward
hacking),
* deterministic and stochastic policies, state-value functions
* and a complete hands-on implementation of Monte Carlo policy
evaluation on a 4×4 gridworld.

Everything is covered from scratch, so no RL background is
required.

​You can read Part 2 of the course here → (

)​

Why care?
---------

Every frontier LLM released in the past two years uses RL in its
post-training pipeline.

* ChatGPT was shaped by RLHF.
* DeepSeek-R1 used GRPO to develop reasoning capabilities.
* Claude uses constitutional AI with RL.

The pattern is consistent: pre-training gives the model
knowledge, but RL is what gives it behavior.

And it is not just LLMs.

Agentic AI systems that take actions, interact with tools, and
operate in multi-step environments are fundamentally RL problems.
Robotics, recommendation systems, game-playing, autonomous
driving, drug discovery: RL is the common thread.

Google Trends for “reinforcement learning” was nearly flat from
2004 to 2023. In the past year, it hit an all-time high.

​
The field is having its moment, and the demand for engineers who
understand it deeply is growing fast.

This series builds that understanding from the ground up, concept
by concept, with math where it matters and hands-on code you can
run. No prior RL background needed.

This series is structured the same way as our MLOps/LLMOps course
(

): concept by concept, with clear explanations, diagrams, math
where it matters, and hands-on implementations you can run.

And no prior RL background is needed.

If you haven’t read Part 1, start there (

) first. It covers the agent-environment loop, exploration vs.
exploitation, and multi-armed bandits.

-->​Reinforcement learning nanodegree part 1 (

)
​Reinforcement learning nanodegree part 1 (
https://www.dailydoseofds.com/rl-course-part-1/ )Over to you:
What topics would you like us to cover in this RL series?

LLms
----

-----------------------------------------------------------------
​How LLM inference works internally (

)​
-----------------------------------------------------------------

Every generate() call to an LLM runs two distinct computational
phases on the same GPU:

* prefill (processing the prompt) is compute-bound
* while decode (generating tokens one at a time) is memory-bound.

Most inference optimizations target one phase or the other, and
diagnosing which phase is the bottleneck is the first step in
making a deployment faster.

Today, let's walk through the full pipeline, from tokenized input
to streamed output, and look at where the time goes in each
phase.

​To master the full LLMOps cycle with code, start here → (

)​
​
We published the above LLMOps course, which covers the
fundamentals of AI engineering & LLMs, Building blocks of LLMs
like tokenization, embeddings, attention, architectural designs
and training, decoding, generation parameters, the LLM
Application Lifecycle, context engineering, prompt management,
defense, control, memory, temporal context, evaluation, tool use,
red teaming, Adaptive LLMs, and Serving.

Tokenization and embedding
--------------------------

Tokenizers like Byte Pair Encoding (BPE) convert raw text into
integer IDs from a vocabulary of roughly 50,000 tokens.

​
Each ID maps to a row in the embedding table, a learned matrix of
shape [vocab_size, hidden_dim]. For a model with a hidden
dimension of 4,096, each token becomes a 4,096-dimensional
vector.

​

​
Position information gets injected at this stage.

Most modern architectures use Rotary Position Embeddings (RoPE),
which encode position by rotating the embedding vectors rather
than adding a separate positional vector.

Transformer layers
------------------

The embedded sequence passes through a stack of transformer
layers (typically 32 to 80+, depending on model size).

Each layer applies two operations in sequence:

1) Self-attention computes three projections per token (query Q,
key K, value V) via learned weight matrices.

​
Each token's query is scored against every other token's key, and
those scores (after scaling and softmax) determine how much of
each token's value gets mixed in.

​
2) Feed-forward network (FFN) processes each token's vector
independently through a two-layer MLP. Attention moves
information between positions. The FFN transforms it.

After the final layer, the model projects the last token's hidden
state back to vocabulary size ([hidden_dim, vocab_size]), applies
softmax, and samples from the resulting distribution to produce
the first output token.

Prefill: the compute-bound phase
--------------------------------

Processing the input prompt is the

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
