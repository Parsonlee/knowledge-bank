---
title: Phases of ML Modeling
source: https://mail.google.com/mail/u/0/#inbox/19c102bf0ed3e544
author:
  - "[[DailyDoseOfDS]]"
published: 2026-01-30
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Phases of ML Modeling 的原理剖析与工程实践。
tags:
  - clippings
---

# Phases of ML Modeling

## 1. 核心要点解析

本期内容重点涵盖：
- **Phases of ML Modeling**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnqp957t6h8kxn400igh32dww/48hvhehmwl6qewfx/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Give your Agents access to live, high-quality web data!
* Phases of ML Modeling
* Implement "Attention is all you need"

TODAY'S ISSUE

together with Firecrawl
-----------------------

-----------------------------------------------------------------
​Give your Agents access to live, high-quality web data! (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnqp957t6h8kxn400igh32dww/wnh2hghqm7xvpns7/aHR0cHM6Ly9kb2NzLmZpcmVjcmF3bC5kZXYvc2Rrcy9jbGk=
)​
-----------------------------------------------------------------

​
Firecrawl just launched Firecrawl Skill + CLI (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnqp957t6h8kxn400igh32dww/wnh2hghqm7xvpns7/aHR0cHM6Ly9kb2NzLmZpcmVjcmF3bC5kZXYvc2Rrcy9jbGk=
) for Agents.

Agents like Claude Code, Codex, and OpenCode need live quality
context from the web.

The CLI pulls web content to local files with bash-powered search
for the highest token efficiency.

All you need is to go to your terminal and run:

$ npx skills add firecrawl/cli

​Read more → (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnqp957t6h8kxn400igh32dww/wnh2hghqm7xvpns7/aHR0cHM6Ly9kb2NzLmZpcmVjcmF3bC5kZXYvc2Rrcy9jbGk=
)​

machine learning
----------------

-----------------------------------------------------------------
​Phases of ML Modeling (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnqp957t6h8kxn400igh32dww/reh8hohmkdwvrdc2/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWxvcHMtY3Jhc2gtY291cnNlLXBhcnQtMS8=
)​
-----------------------------------------------------------------

Most ML systems don’t jump straight to deep learning. They
evolve.

A practical way to think about this evolution is in phases,
starting from the simplest possible solution and gradually
increasing complexity only when it’s justified. Because
unnecessary complexity = low utility.

​
A staged approach reduces risk, improves debuggability, and
aligns naturally with MLOps best practices.

Now let’s walk through the different phases of ML model
development:

Phase 1: Before ML (heuristics and rules):
------------------------------------------

If you’re solving a problem for the first time, resist the urge
to start with a model. Begin with a non-ML baseline: a rule, a
heuristic, or a simple deterministic strategy.

For example, in a movie recommendation system, a phase-1 solution
could be as simple as recommending the top-10 most popular movies
to every user.

This might sound naive, but such heuristics are often
surprisingly strong.

These baselines are fast to build, easy to reason about, and set
a minimum performance bar. If a complex ML model cannot beat a
naive heuristic, something is wrong, either ML isn’t adding
value, or there’s a bug in the pipeline.

Here is a conceptual diagram summarizing the Phase 1:

​
Conceptually, Phase 1 looks like a direct mapping from input to
output using rules, without any learning component.

Phase 2: The Simplest ML Model
------------------------------

Once a heuristic baseline exists (or once it’s clear that
heuristics aren’t enough), the next step is not a deep model.

It’s the simplest possible ML model.

Think logistic regression, a shallow decision tree, k-nearest
neighbors, or a basic linear model; something easy to train,
interpret, and deploy.

The goal here is not peak accuracy. This phase answers
foundational questions:

* Can we train on historical data and get sensible predictions?
* Are the features informative?
* Does the model generalize better than the heuristic?

This is where you validate the end-to-end ML pipeline: data
ingestion, feature extraction, training, evaluation, and serving.

​
Conceptually, Phase 2 introduces learning, but keeps the model
and serving logic minimal.

Phase 3: Optimizing the Simple Model:
-------------------------------------

Once the basic model works, there’s often significant performance
left on the table, without changing the model class at all.

Phase 3 focuses on extracting as much value as possible from the
existing approach.

Typical levers include:

* Feature engineering: creating better representations of the
input data.
* Hyperparameter tuning: systematically searching for better
configurations.
* More data: expanding the dataset or improving data quality.

This phase is where returns on investment are often highest.

You’re working with models that are easy to understand, cheap to
train, and simple to serve, while still achieving meaningful
gains.

Many real-world ML systems stop here. A well-tuned logistic
regression, gradient boosted tree, or modest ensemble can meet
production requirements without the complexity of deep learning.

Here’s the entire thing summarized as a diagram:

​
Hence, phase 3 overall, looks like a refinement loop around the
same model family, not a shift in paradigm.

Phase 4: Complex Models:
------------------------

Only after simpler approaches are exhausted should you move to
fundamentally more complex models.

This includes deep neural networks, transformers, or large
pretrained architectures, depending on the domain.

​
Complex models bring capacity, but also cost. The decision to
enter Phase 4 should be evidence-driven.

Conceptually, Phase 4 introduces higher model expressiveness
alongside increased engineering complexity.

A key point to keep in mind is, at every phase, the previous
phase’s best model becomes the baseline.

This phased approach encourages incremental progress and
disciplined decision-making.

If you want to learn more about these real-world ML practices and
start your with MLOps, we have already

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
