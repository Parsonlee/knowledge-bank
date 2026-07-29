---
title: 4 Ways to Test ML Models in Production
source: https://mail.google.com/mail/u/0/#inbox/194cd43e281f59cc
author:
  - "[[DailyDoseOfDS]]"
published: 2025-02-03
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 4 Ways to Test ML Models in Production 的原理剖析与工程实践。
tags:
  - clippings
---

# 4 Ways to Test ML Models in Production

## 1. 核心要点解析

本期内容重点涵盖：
- **4 Ways to Test ML Models in Production**

## 2. 深度拆解与正文翻译

​

----------------------
In today's newsletter:
----------------------

* Simulate, evaluate, and observe your AI agents with Maxim!
* 4 ways to test ML models in production, explained visually.

Reading time: 3 minutes.

TODAY'S ISSUE

Together with Maxim
-------------------

-----------------------------------------------------------------
​Simulate, evaluate, and observe your AI agents! (
https://click.convertkit-mail2.com/92umdmr368anh6qre5ra9hzeql333uw/p8heh9hzvldrr2uq/aHR0cHM6Ly9kdWIuc2gvbWF4aW0tYWktZXZhbA==
)​
-----------------------------------------------------------------

(
https://click.convertkit-mail2.com/92umdmr368anh6qre5ra9hzeql333uw/p8heh9hzvldrr2uq/aHR0cHM6Ly9kdWIuc2gvbWF4aW0tYWktZXZhbA==
)​
Most AI agents never make it to production—not because they
aren’t useful, but because real-world testing is hard.

​Maxim (
https://click.convertkit-mail2.com/92umdmr368anh6qre5ra9hzeql333uw/p8heh9hzvldrr2uq/aHR0cHM6Ly9kdWIuc2gvbWF4aW0tYWktZXZhbA==
) makes it effortless.

-->I want to test my Agents (
https://click.convertkit-mail2.com/92umdmr368anh6qre5ra9hzeql333uw/p8heh9hzvldrr2uq/aHR0cHM6Ly9kdWIuc2gvbWF4aW0tYWktZXZhbA==
)
I want to test my Agents ( https://dub.sh/maxim-ai-eval )With
Maxim (
https://click.convertkit-mail2.com/92umdmr368anh6qre5ra9hzeql333uw/p8heh9hzvldrr2uq/aHR0cHM6Ly9kdWIuc2gvbWF4aW0tYWktZXZhbA==
)’s AI-powered simulations and evaluations, you can:

* Define realistic scenarios that simulate different user
personas.
* Run multi-turn conversations where your AI agent responds
dynamically in real-world settings.
* Evaluate performance at scale by automatically testing agents
across multiple scenarios to get detailed evaluation scores on
trajectory, step completion, and task success.

This way, you can reliably test your AI’s performance before
deployment.

-->I want to test my Agents (
https://click.convertkit-mail2.com/92umdmr368anh6qre5ra9hzeql333uw/p8heh9hzvldrr2uq/aHR0cHM6Ly9kdWIuc2gvbWF4aW0tYWktZXZhbA==
)
I want to test my Agents ( https://dub.sh/maxim-ai-eval )

IN CASE YOU MISSED IT
---------------------

-----------------------------------------------------------------
​4 ways to test ML models in production (
https://click.convertkit-mail2.com/92umdmr368anh6qre5ra9hzeql333uw/x0hph6hwglzkkzi5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vNS1tdXN0LWtub3ctd2F5cy10by10ZXN0LW1sLW1vZGVscy1pbi1wcm9kdWN0aW9uLWltcGxlbWVudGF0aW9uLWluY2x1ZGVk
)​
-----------------------------------------------------------------

Continuing the discussion from agent testing…

…the following visual depicts 4 strategies to test ML models in
production:

Current model is called the legacy model, and new model is called
the candidate model.
We covered one more technique (Multi-armed bandits deployments)
and the implementation of all five techniques: 5 Must-Know Ways
to Test ML Models in Production (Implementation Included) (
https://click.convertkit-mail2.com/92umdmr368anh6qre5ra9hzeql333uw/x0hph6hwglzkkzi5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vNS1tdXN0LWtub3ctd2F5cy10by10ZXN0LW1sLW1vZGVscy1pbi1wcm9kdWN0aW9uLWltcGxlbWVudGF0aW9uLWluY2x1ZGVk
).

*********
Why care?
*********

Despite rigorously testing an ML model locally (on validation and
test sets), it could be a terrible idea to instantly replace the
previous model with the new model.

​
A more reliable strategy is to test the model in production (yes,
on real-world incoming data).

While this might sound risky, ML teams do it all the time, and it
isn’t that complicated.

***************
#1) A/B testing
***************

​
* Distribute the incoming requests non-uniformly between the
legacy model and the candidate model.
* Limit the exposure of the candidate model to avoid any
potential risks.

******************
#2) Canary testing
******************

​
* A/B testing may affect all users since it randomly distributes
“traffic” to either model (irrespective of the user).
* In canary testing, the candidate model is exposed to a small
subset of users in production and gradually rolled out to more
users.

***********************
#3) Interleaved testing
***********************

​
* This involves mixing the predictions of multiple models in the
response.
* Consider Amazon’s recommendation engine. In interleaved
deployments, some product recommendations displayed on their
homepage can come from the legacy model, and others from the
candidate model.

******************
#4) Shadow testing
******************

​
* All of the above techniques affect some (or all) users.
* Shadow testing (or dark launches) lets us test a new model in a
production environment without affecting the user experience.
* The candidate model is deployed alongside the existing legacy
model and serves requests like the legacy model. However, the
output is not sent back to the user. Instead, the output is
logged for later use to benchmark its performance against the
legacy model.
* We explicitly deploy the candidate model instead of testing
offline because the exact production environment can be difficult
to replicate offline.
* Shadow testing offers risk-free testing of the candidate model
in a production environment.

That said, don't forget to check out Maxim (
https://click.convertkit-mail2.com/92umdmr368anh6qre5ra9hzeql333uw/p8heh9hzvldrr2uq/aHR0cHM6Ly9kdWIuc2gvbWF4aW0tYWktZXZhbA==
) for Agent testing.

-->Test Agents with Maxim (
https://click.convertkit-mail2.com/92umdmr368anh6qre5ra9hzeql333uw/p8heh9hzvldrr2uq/aHR0cHM6Ly9kdWIuc2gvbWF4aW0tYWktZXZhbA==
)
Test Agents with Maxim ( https://dub.sh/maxim-ai-eval )It
provides an end-to-end evaluation and observability platform that
will help you ship AI agents reliably and >5x faster!

👉 Over to you: Which ML testing technique looks most interesting
to you?

Thanks for reading!

THAT'S A WRAP

SPONSOR US
----------

-------------------------------------
ADVERTISE T

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
