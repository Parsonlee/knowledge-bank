---
title: How to Actually Use Train, Validation, and Test Sets in ML
source: https://mail.google.com/mail/u/0/#inbox/19ce93b00b8a14f0
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-13
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 How to Actually Use Train, Validation, and Test Sets in ML 的原理剖析与工程实践。
tags:
  - clippings
---

# How to Actually Use Train, Validation, and Test Sets in ML

## 1. 核心要点解析

本期内容重点涵盖：
- **How to Actually Use Train, Validation, and Test Sets in ML**

## 2. 深度拆解与正文翻译

​

----------------------
In today's newsletter:
----------------------

* What are RL environments, and how to build them.
* How to actually use train, validation, and test sets in ML.

TODAY'S ISSUE

Reinforcement learning
----------------------

-----------------------------------------------------------------
​What are RL environments, and how to build them (

)​
-----------------------------------------------------------------

The real bottleneck in building AI agents that need to reason
across multiple steps isn’t the training algorithm.

It’s the environment your agent trains in.

This is because training algorithms like GRPO or PPO are
essentially optimizers. They take a reward signal and update
model weights to maximize it.

​
The hard part is everything that comes before that, like defining
what "better" actually means for your agent, building the
infrastructure to generate thousands of parallel rollouts,
managing isolated session state across multi-turn interactions,
and designing verification logic that reliably scores agent
behavior.

And unlike single-turn fine-tuning, where you just need
input-output pairs, agentic RL requires your environment to
handle tool calls, maintain state across steps, spin up sandboxed
execution contexts, and clean up resources after every rollout.

​
Most RL workflows today tightly couple this logic into the
training pipeline, which makes it painful to iterate on
environment design without touching the optimizer code. That
tight coupling is exactly what slows teams down.

Unsloth and NVIDIA have published a deep dive on building RL
environments for agentic AI (

).

​
The post covers how NVIDIA NeMo Gym lets you decouple environment
logic from training, so you can design verifiable reward signals
independently of your optimizer.

It also walks through the full stack of building an environment,
including agent servers for orchestrating rollouts, resource
servers for maintaining session state, and verification logic for
computing rewards.

Unsloth plugs in as the training backend, consuming rollout
trajectories and running GRPO to update model weights
efficiently.

​You can read it here → (

)​

machine learning
----------------

-----------------------------------------------------------------
​How to actually use train, validation, and test sets (

)​
-----------------------------------------------------------------

It is conventional to split the available data into train, test,
and validation sets.

​
However, there are quite a few misconceptions about how they are
meant to be used, especially the validation and test sets.

Today, let’s clear them up and see how to truly use train,
validation, and test sets.

​We covered 8 Cautionary measures in ML here → (

)​
​
​And 11 powerful techniques to supercharge ML models here → (

)​

Let’s begin!

The standard split
------------------

As we all know, we begin by splitting the data into:

* Train
* Validation
* Test

At this point, just assume that the test data does not even
exist. Forget about it instantly.

​
Begin with the train set. This is your whole world now.

​
* You analyze it
* You transform it
* You use it to determine features
* You fit a model on it

After modeling, you will measure the model’s performance on
unseen data.

Bring in the validation set now.

Based on validation performance, improve the model.

Here’s how you iteratively build your model:

​
* Train using a train set
* Evaluate it using the validation set
* Improve the model
* Evaluate again using the validation set
* Improve the model again
* and so on.

Until you are satisfied with the model’s performance.

The validation overfitting problem
----------------------------------

Here’s something critical that many practitioners miss:

If you repeatedly tune your model based on validation performance
over many iterations, you risk indirectly overfitting to the
validation set.

​
This is because every decision you make based on validation
performance leaks information from that set into your model
selection process.

Think of it this way: If you try 1000 different model
configurations and pick the one with the best validation score,
you’ve essentially used the validation set as part of your
training process.

The solution: Cross-validation
------------------------------

Instead of relying on a single train-validation split, use k-fold
cross-validation.

Here’s how it works:

​
* Split your data into k folds (commonly k=5 or k=10).
* For each fold, use (k-1) folds for training and use the
remaining fold for validation.
* Average the performance across all folds.

This gives you a more robust estimate of model performance
because:

* Every data point gets used for both training and validation
* You reduce the variance that comes from a single random split
* You get a better sense of how your model generalizes

When to use cross-validation:

* When you don’t have much data (highly recommended)
* When you want robust performance estimates
* When you’re comparing multiple models or hyperparameter
configurations

Trade-off: Cross-validation is computationally more expensive
since you train k models instead of one.

For rigorous hyperparameter tuning: Nested Cross-Validation
-----------------------------------------------------------

If you’re doing extensive hyperparameter tuning, consider nested
cross-validation.

This involves two loops:

* Outer loop: Evaluates the overall modeling approach
* Inner loop: Tunes hyperparameters

This prevents the hyperparameter tuning process from biasing your
performance estimates.

​
Yes, it’s computationally intensive. But it’s the gold standard
when you need unbiased performance estimates.

The test set
------------

Now, if you are happy with the model’s performance on validation

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
