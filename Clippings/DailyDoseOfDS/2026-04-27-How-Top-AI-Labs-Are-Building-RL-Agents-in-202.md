---
title: How Top AI Labs Are Building RL Agents in 2026
source: https://mail.google.com/mail/u/0/#inbox/19dd11ff55feb3f6
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-27
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 How Top AI Labs Are Building RL Agents in 2026 的原理剖析与工程实践。
tags:
  - clippings
---

# How Top AI Labs Are Building RL Agents in 2026

## 1. 核心要点解析

本期内容重点涵盖：
- **How Top AI Labs Are Building RL Agents in 2026**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (

)​

----------------------
In today's newsletter:
----------------------

* How top AI labs are building RL Agents in 2026:* Introduction
* Applying RL to LLMs and problems
* DeepSeek R1 breakthrough using verifiable rewards
* The problem with the DeepSeek R1 strategy
* How are AI labs approaching this?
* RULER
* Trajectories and Groups
* Two concrete examples
* The full training loop
* Application to non-verifiable tasks
* Practical details

TODAY'S ISSUE

Hands-on
--------

-----------------------------------------------------------------
​How top AI labs are building RL Agents in 2026 (

)​
-----------------------------------------------------------------

Reinforcement learning, at its core, is straightforward: a system
takes an action, the environment rewards it, and the agent
updates its behavior to maximize that reward over time.

The interaction above works in discrete steps. At each step,
three things happen in order:

​
* The agent observes the current state of the environment (S). A
state is a description of the situation the agent is in, enough
to decide what to do next. For instance, in chess, the state is
the board position, and in a dialogue model, the state is the
conversation history so far.
* The agent picks an action (A) based on what it sees. The action
is the agent’s output, the only way it can influence the
environment. For instance, in chess, an action is a legal move.
For an LLM, an action is the generated response.
* The environment then does two things: it transitions to a new
state (S’), and it emits a reward (R), a scalar number that
evaluates the action. The next step begins, and the loop
continues.

Stringing these steps together gives a trajectory:

​
Reading left to right, this is the entire history of the agent’s
interaction with the environment. Each (S, A, R, S’) quartet is
one transition, and much of RL is about learning from these
transitions.

*******************
Applying RL to LLMs
*******************

When RL was first applied to LLMs, the environment was human
preference.

OpenAI’s InstructGPT (2022) introduced RLHF (Reinforcement
Learning from Human Feedback), where:

​
* humans ranked model outputs
* those rankings trained a reward model
* and PPO (Proximal Policy Optimization) used that reward model
to fine-tune the LLM.

ChatGPT was built on this exact pipeline.

But humans can’t sit in the training loop rating every output in
real time. If the model generates 16 responses per prompt across
thousands of training steps, that’s hundreds of thousands of
evaluations.

OpenAI solved this by splitting the process into two phases.

​
* First, the offline phase. Here, humans ranked a relatively
small set of model outputs and generated pairwise comparisons.
This was the expensive human labor part, but it was a one-time
cost.
* Second, they trained a reward model on those rankings, which
was a separate LLM that learned to predict what humans would
prefer. Now you had a neural network that could score any output
instantly, without waiting for a human. The reward model was a
compressed approximation of human judgment, fast enough to sit
inside the training loop.

With the reward model in place, PPO could run the actual RL
training at GPU speed. The model generated responses, the reward
model scored them, and PPO updated the weights, without extensive
need for humans.

The cost, however, was that PPO required four full-size models in
memory simultaneously.

​
* The policy (the LLM being trained).
* The reference policy (a frozen copy of the original, used to
prevent training from drifting too far via a KL divergence
penalty).
* The reward model (the human-preference approximator discussed
above to score every output).
* And the critic, also called the value model (more about it
below).

The critic exists to answer one question:

Was this reward good or bad relative to what we’d normally expect
for this prompt?
We need this because a raw reward of 0.7 means nothing in
isolation. For instance, on a simple factual question where most
responses score 0.9, a 0.7 is below average.

But on a complex open-ended question where most responses score
0.4, a 0.7 is excellent.

​
The critic learns this baseline by observing thousands of
(prompt, reward) pairs during training.

PPO’s actual training signal is the advantage, which is estimated
as the reward minus the critic’s predicted baseline.

This makes the signal stable across prompts of different
difficulty. But the cost involved here is that the critic is a
full-size LLM itself, adding another model’s worth of memory.

For a 7B parameter LLM, that meant roughly 28B parameters in
memory at once.

*************************************************
DeepSeek R1 breakthrough using verifiable rewards
*************************************************

In January 2025, DeepSeek released R1 with a fundamentally
different approach to the reward signal.

Instead of training a reward model from human preferences (Phases
1 and 2 of the RLHF pipeline), they used RLVR (Reinforcement
Learning with Verifiable Rewards).

It’s a simple, rule-based verification where the environment
itself provides the signal.

​
For instance:

* For math problems, the verifier checked if the model’s answer
matched the known solution.
* For code, a compiler ran the output and returned pass or fail.
Binary rewards: 1 for correct, 0 for wrong.

There are no human rankings or explicit reward models required
since the ground truth was available (or inferable) to be used as
the reward.

The RL optimizer was GRPO (Group Relative Policy Optimization),
which stripped away most of PPO’s infrastructure.

It removed the critic model entirely.

Instead of training a separate model to predict expected reward
per prompt, GRPO generated multiple responses to th

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
