---
title: How to Test Agents Using Agents
source: https://mail.google.com/mail/u/0/#inbox/19be22ee2f9716e1
author:
  - "[[DailyDoseOfDS]]"
published: 2026-01-21
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 How to Test Agents Using Agents 的原理剖析与工程实践。
tags:
  - clippings
---

# How to Test Agents Using Agents

## 1. 核心要点解析

本期内容重点涵盖：
- **How to Test Agents Using Agents**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (
https://fff97757.click.convertkit-mail2.com/v8uqlqw04vhrhvm0dozbghv3xwmllh9hpqloo/x0hph6hekw8nl8h5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Build Agents that never forget with self-evolving AI memory.
* Clean ML datasets with Cleanlab.
* How to test Agents using Agents​.
* ​​Generate code for any research paper using Factory!​

TODAY'S ISSUE

open-source
-----------

-----------------------------------------------------------------
​Build Agents that never forget with self-evolving AI memory (
https://fff97757.click.convertkit-mail2.com/v8uqlqw04vhrhvm0dozbghv3xwmllh9hpqloo/dpheh0hed0zqm4um/aHR0cHM6Ly9naXRodWIuY29tL3RvcG90ZXJldGVzL2NvZ25lZQ==
)​
-----------------------------------------------------------------

​
Most agents have no real memory. Every conversation starts fresh
with no recall of yesterday and no understanding of how
information connects.

And here’s where most devs go wrong when trying to fix this: they
rely entirely on vector DBs and call it a day.

Vector search is fast, but it treats your documents as isolated
chunks with no understanding of how they connect. What your agent
actually needs is memory that captures relationships and persists
over time.

​
​Cognee (
https://fff97757.click.convertkit-mail2.com/v8uqlqw04vhrhvm0dozbghv3xwmllh9hpqloo/dpheh0hed0zqm4um/aHR0cHM6Ly9naXRodWIuY29tL3RvcG90ZXJldGVzL2NvZ25lZQ==
) is an open-source tool built for exactly this.

-->​Cognee GitHub repo​ (
https://fff97757.click.convertkit-mail2.com/v8uqlqw04vhrhvm0dozbghv3xwmllh9hpqloo/dpheh0hed0zqm4um/aHR0cHM6Ly9naXRodWIuY29tL3RvcG90ZXJldGVzL2NvZ25lZQ==
)
​Cognee GitHub repo​ ( https://github.com/topoteretes/cognee )It
combines vector search with graph DBs, making your documents
searchable by meaning and connected by relationships.

Here is what makes it even more interesting:

* Composable pipelines: Build custom workflows by chaining
modular tasks like chunking, embedding, and entity extraction
* Weighted memory: Frequently used connections get stronger.
Feedback from responses flows back into edge weights, so the
graph learns what actually matters.
* Self-improving: The Memify pipeline has RL-inspired
optimization that strengthens useful paths, prunes stale nodes,
and auto-tunes based on real usage.

Getting started with Cognee is as simple as this:

await cognee.add("Your docs here")
await cognee.cognify()
await cognee.memify()
await cognee.search("Your query here")

That’s it. Cognee handles the heavy lifting, and your agent geta
s memory that actually learns over time.

​Find the GitHub repo here → (
https://fff97757.click.convertkit-mail2.com/v8uqlqw04vhrhvm0dozbghv3xwmllh9hpqloo/dpheh0hed0zqm4um/aHR0cHM6Ly9naXRodWIuY29tL3RvcG90ZXJldGVzL2NvZ25lZQ==
)​

We’ll cover this in a hands-on demo soon!

open-source
-----------

-------------------------------
Clean ML datasets with Cleanlab
-------------------------------

For the longest time, no one could get past the 91% accuracy on
ImageNet (92.4% is quite recent).

ImageNet leaderboard on Paperwithcode
This happened because ImageNet had over 100k mislabeled images.

Real-world datasets are messy—noisy labels, missing values, and
outliers that severely degrade your model’s performance.

No sophisticated ML algorithms can compensate for poor-quality
data.

​
Researchers from MIT developed Cleanlab (
https://fff97757.click.convertkit-mail2.com/v8uqlqw04vhrhvm0dozbghv3xwmllh9hpqloo/e0hph7h7m09k2li8/aHR0cHM6Ly9kb2NzLmNsZWFubGFiLmFpL3N0YWJsZS9pbmRleC5odG1s
), which is an open-source library that cleans your data in just
a few lines of code.

​
As shown in the image above, Cleanlab (
https://fff97757.click.convertkit-mail2.com/v8uqlqw04vhrhvm0dozbghv3xwmllh9hpqloo/e0hph7h7m09k2li8/aHR0cHM6Ly9kb2NzLmNsZWFubGFiLmFpL3N0YWJsZS9pbmRleC5odG1s
) can flag errors in any type of data (text, image, tabular,
audio), like:

* out-of-distribution samples
* outliers
* label issues
* duplicates, etc.

All it takes is just four lines of code:

​
* Import the package.
* Pass the dataset and specify the label column.
* Find issues by passing the embedding matrix and the
probabilities predicted by the model.
* Finally, generate the report!

Done!

It will generate a report like the one shown above.

This way, you can easily clean your datasets for training
accurate ML models.

Several notebook demos are available here if you want to learn
more: Cleanlab demo (
https://fff97757.click.convertkit-mail2.com/v8uqlqw04vhrhvm0dozbghv3xwmllh9hpqloo/e0hph7h7m09k2li8/aHR0cHM6Ly9kb2NzLmNsZWFubGFiLmFpL3N0YWJsZS9pbmRleC5odG1s
).

hands-ON
--------

-------------------------------
How to test Agents using Agents
-------------------------------

Traditional testing relies on fixed inputs and exact outputs. But
agents speak in language, and there’s no single “correct”
response.

That’s why we test Agents using other Agents by simulating Users
and Judges.

Today, let’s understand Agent Testing by building a pipeline to
test Agents with other Agents using Scenario.

Our open-source tech stack:

* CrewAI for Agent orchestration.
* LangWatch Scenario to build the eval pipeline.
* PyTest as the test runner.

Here's what the process looks like:

​
1) Define three Agents:

* The Agent you want to test.
* A User Simulator Agent that acts like a real user.
* A Judge Agent for evaluation.

2) Let your Agent and User Simulator Agent interact with each
other.

3) Evaluate the exchange using the Judge Agent based on the
specified criteria.

Let’s implement this!

*******************
Define Planner Crew
*******************

For this demonstration, let’s build a Travel Planner Agent using
CrewAI.

It will accept a user query and respond with travel suggestions,
a brief itinerary, and an 

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
