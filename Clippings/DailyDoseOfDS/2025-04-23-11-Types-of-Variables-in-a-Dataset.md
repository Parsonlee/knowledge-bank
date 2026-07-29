---
title: 11 Types of Variables in a Dataset
source: https://mail.google.com/mail/u/0/#inbox/19664020d007efe2
author:
  - "[[DailyDoseOfDS]]"
published: 2025-04-23
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 11 Types of Variables in a Dataset 的原理剖析与工程实践。
tags:
  - clippings
---

# 11 Types of Variables in a Dataset

## 1. 核心要点解析

本期内容重点涵盖：
- **11 Types of Variables in a Dataset**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/d0uwowlp78h0how0l2mcmhz8vv544fl/dpheh0heorlopgbm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* ​Your natural language browser automation tool​.
* 11 types of variables in a dataset.
* ​PyTorch Dataloader has two terrible default settings​.

Reading time: 3 minutes.

TODAY'S ISSUE

Together with Browserbase
-------------------------

-----------------------------------------------------------------
​Your natural language browser automation tool (
https://click.convertkit-mail2.com/d0uwowlp78h0how0l2mcmhz8vv544fl/7qh7h8h963r6nrtz/aHR0cHM6Ly9kdWIuc2gvc2hk
)​
-----------------------------------------------------------------

Stagehand bridges the gap between fully agentic workflows and
hardcoded automation by letting you control browsers with simple
natural language commands.

(
https://click.convertkit-mail2.com/d0uwowlp78h0how0l2mcmhz8vv544fl/owhkhqhw6526qqbv/aHR0cHM6Ly9zdGFnZWgubGluay9yZWFzb24=
)​
Stagehand was used to test different LLM models (like Gemini,
GPT, Claude, etc.) on their ability to perform specific browser
automation tasks (
https://click.convertkit-mail2.com/d0uwowlp78h0how0l2mcmhz8vv544fl/owhkhqhw6526qqbv/aHR0cHM6Ly9zdGFnZWgubGluay9yZWFzb24=
).

-->Stagehand LLM leaderboard (
https://click.convertkit-mail2.com/d0uwowlp78h0how0l2mcmhz8vv544fl/owhkhqhw6526qqbv/aHR0cHM6Ly9zdGFnZWgubGluay9yZWFzb24=
)
Stagehand LLM leaderboard ( https://stageh.link/reason )​See the
results (
https://click.convertkit-mail2.com/d0uwowlp78h0how0l2mcmhz8vv544fl/z2hghnhek0qklmfp/aHR0cHM6Ly9zdGFnZWgubGluay9ldmFsdWF0aW9ucw==
) for yourself and use Stagehand for free, fully open source,
today.

TODAY'S DAILY DOSE OF DATA SCIENCE
----------------------------------

----------------------------------
11 Types of Variables in a Dataset
----------------------------------

In any tabular dataset, we typically categorize the columns as
either a feature or a target.

However, there are so many variables that one may find/define in
their dataset, as shown below:

​
Let’s understand today!

*****************************************
#1-2) Independent and dependent variables
*****************************************

Independent variables are the features that are used as input to
predict the outcome. They are also referred to as
predictors/features/explanatory variables.

​
The dependent variable is the outcome that is being predicted. It
is also called the target, response, or output variable.

******************************************
#3-4) Confounding and correlated variables
******************************************

Confounding variables are usually found in a cause-and-effect
study (causal inference (
https://click.convertkit-mail2.com/d0uwowlp78h0how0l2mcmhz8vv544fl/p8heh9h428n2qehq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tY2F1c2FsaXR5LXBhcnQtMS8=
)).

These are not always of primary interest, but can lead to weird
associations if not handled correctly.

Say we want to measure the effect of ice cream sales on the sales
of air conditioners, both of which are highly correlated:

​
However, there’s a confounding variable—temperature, which
influences both ice cream sales and the sales of air
conditioners.

​
To study the actual causal impact, one must consider the
confounder (temperature). Otherwise, the study will produce
misleading results.

It is due to the confounding variables that we say, “Correlation
does not imply causation.”

We did a crash course on Causal inference some time back:
- A Crash Course on Causality – Part 1 (
https://click.convertkit-mail2.com/d0uwowlp78h0how0l2mcmhz8vv544fl/p8heh9h428n2qehq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tY2F1c2FsaXR5LXBhcnQtMS8=
)​
- A Crash Course on Causality – Part 2 (
https://click.convertkit-mail2.com/d0uwowlp78h0how0l2mcmhz8vv544fl/x0hph6hepx5pqgc5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tY2F1c2FsaXR5LXBhcnQtMi8=
)​

*********************
#5) Control variables
*********************

In the above example, we must ensure that the temperature is
controlled to measure the true effect of ice cream sales on AC
sales.

​
Once controlled, temperature becomes a control variable.

These variables are not the primary focus of the study, but are
crucial to account for. This ensures that the effect we intend to
measure is not biased or confounded by other factors.

********************
#6) Latent variables
********************

A variable that is not directly observed but is inferred from
other observed variables.

For instance, there is no true label in clustering—it is a latent
variable.

​
We also learned about Latent variables when we implemented
Gaussian mixture models (
https://click.convertkit-mail2.com/d0uwowlp78h0how0l2mcmhz8vv544fl/dpheh0heorlo2zsm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZ2F1c3NpYW4tbWl4dHVyZS1tb2RlbHMtZ21tLw==
) from scratch.

*************************
#7) Interaction variables
*************************

They measure the interaction effect between two or more variables
and are often used in regression analysis.

For instance, if you have two variables:

* Population density → HIGH, MEDIUM, and LOW (one-hot encoded).
* Income levels → HIGH, MEDIUM, and LOW (one-hot encoded).

​
You can multiply them to get interaction variables, which will
produce 9 interaction variables. Studying them will likely
produce better insights.

**********************************************
#8-9) Stationary and Non-Stationary variables:
**********************************************

Stationary variables are those whose statistical properties
(mean, variance) DO NOT change over time.

​
If it does, the variable is called a non-stationary variable.

Preserving stationarity is critica

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
