---
title: [Hands-on] Build a Real-time Federated Data Engine for Agents
source: https://mail.google.com/mail/u/0/#inbox/19a79cbb943dd0f0
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-12
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 [Hands-on] Build a Real-time Federated Data Engine for Agents 的原理剖析与工程实践。
tags:
  - clippings
---

# [Hands-on] Build a Real-time Federated Data Engine for Agents

## 1. 核心要点解析

本期内容重点涵盖：
- **[Hands-on] Build a Real-time Federated Data Engine for Agents**

## 2. 深度拆解与正文翻译

​Master full-stack AI Engineering (
https://click.convertkit-mail2.com/n4uqvqx86whvhxrn35qf6h68wrwgghlhgovww/vqh3hrhoervzq4hg/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* [Hands-on] Build a Real-time Federated Data Engine for Agents.
* 25 most important mathematical definitions in DS

TODAY'S ISSUE

hands-on
--------

-----------------------------------------------------------------
​Build a Real-time Federated Data Engine for Agents (
https://click.convertkit-mail2.com/n4uqvqx86whvhxrn35qf6h68wrwgghlhgovww/l2hehmhl67n8dva6/aHR0cHM6Ly9naXRodWIuY29tL21pbmRzZGIvbWluZHNkYg==
)​
-----------------------------------------------------------------

Real-time sync for agents is incredibly difficult, especially
when your data is scattered across dozens of sources.

Most teams waste weeks building custom connectors for every
database, API, and data warehouse. Then they build ETL pipelines
to sync everything.

By the time your agent retrieves the data, it’s already outdated.

Imagine what it would look like if your Postgres database was
updated 5 minutes ago, a MongoDB collection changed 2 minutes
ago, but your agent is still pulling from yesterday’s snapshot.

This is why most production RAG systems fail.

There’s a better approach:

​
MindsDB is an open-source AI platform with a federated data
engine that lets you query multiple data sources in real-time
using SQL, without moving any data.

Here’s what makes it different:

* Your data stays in place. No ETL pipelines or data duplication
* Query Postgres, MongoDB, REST APIs, and more using consistent
SQL
* JOIN across different sources in real-time with a unified
interface
* Works with both structured and unstructured data

And here’s the best part:

You don’t even need to write SQL. Just describe what you want in
plain English, and MindsDB converts it to SQL automatically. The
system does all the heavy lifting.

The breakthrough for AI agents is simple:

When data updates at the source, your agent gets fresh results
immediately without any sync delays, stale embeddings, or custom
code for each integration.

You can literally write a SQL query that joins a Postgres table
with a MongoDB collection and gets live results. This is what
production AI applications need but rarely get.

In the video below, we have given you a complete walkthrough of
what we just discussed and how to actually do it.

video preview (
https://api.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/677XbTz79bNB8bB9cC3HBA/player
)-->
video preview-->
(
https://click.convertkit-mail2.com/n4uqvqx86whvhxrn35qf6h68wrwgghlhgovww/m2h7h5h3mzqdl7cm/aHR0cHM6Ly9hcGkuZmlsZWtpdGNkbi5jb20vZS9rN1lIUE4yNFNveHlNOG5HS1puRHhhLzY3N1hiVHo3OWJOQjhiQjljQzNIQkEvcGxheWVy
)

​
Make sure you watch this till the end.

​You can find the MindsDB GitHub repo here → (
https://click.convertkit-mail2.com/n4uqvqx86whvhxrn35qf6h68wrwgghlhgovww/l2hehmhl67n8dva6/aHR0cHM6Ly9naXRodWIuY29tL21pbmRzZGIvbWluZHNkYg==
)​

-->MindsDB GitHub repo (
https://click.convertkit-mail2.com/n4uqvqx86whvhxrn35qf6h68wrwgghlhgovww/l2hehmhl67n8dva6/aHR0cHM6Ly9naXRodWIuY29tL21pbmRzZGIvbWluZHNkYg==
)
MindsDB GitHub repo ( https://github.com/mindsdb/mindsdb )

Data science
------------

------------------------------------------------
25 most important mathematical definitions in DS
------------------------------------------------

Here’s a visual with some of the most important mathematical
formulations used in Data Science and Statistics (in no specific
order).

​
Before reading ahead, look at them one by one and calculate how
many of them do you already know:

Some of the terms are pretty self-explanatory, so we won’t go
through each of them, like:

* Gradient Descent, Normal Distribution, Sigmoid, Correlation,
Cosine similarity, Naive Bayes, F1 score, ReLU, Softmax, MSE, MSE
+ L2 regularization, KMeans, Linear regression, SVM, Log loss.

Here are the remaining terms:

* MLE (Maximum Likelihood Estimation): A method for estimating
the parameters of a statistical model by maximizing the
likelihood of the observed data.
* Z-score: A standardized value that indicates how many standard
deviations a data point is from the mean.
* Ordinary Least Squares: A closed-form solution for linear
regression obtained using the MLE step mentioned above.
* Entropy: A measure of the uncertainty or randomness of a random
variable. It is often utilized in decision trees and the t-SNE
algorithm (
https://click.convertkit-mail2.com/n4uqvqx86whvhxrn35qf6h68wrwgghlhgovww/dpheh0he8nol27tm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZm9ybXVsYXRpbmctYW5kLWltcGxlbWVudGluZy10aGUtdC1zbmUtYWxnb3JpdGhtLWZyb20tc2NyYXRjaC8jb3B0aW1pemF0aW9uLW1ldGhvZHMtZm9yLXQtc25l
).
* Eigen Vectors: The non-zero vectors that do not change their
direction when a linear transformation is applied. It is widely
used in dimensionality reduction techniques like PCA. Here’s how
(
https://click.convertkit-mail2.com/n4uqvqx86whvhxrn35qf6h68wrwgghlhgovww/e0hph7h7qol8dks8/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZm9ybXVsYXRpbmctdGhlLXByaW5jaXBhbC1jb21wb25lbnQtYW5hbHlzaXMtYWxnb3JpdGhtLWZyb20tc2NyYXRjaC8=
).
* R2 (R-squared): A statistical measure that represents the
proportion of variance explained by a regression model:

​
* KL divergence: Assess how much information is lost when one
distribution is used to approximate another distribution. It is
used as a loss function in the t-SNE algorithm. We discussed it
here: t-SNE article (
https://click.convertkit-mail2.com/n4uqvqx86whvhxrn35qf6h68wrwgghlhgovww/7qh7h8h9w56rxobz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZm9ybXVsYXRpbmctYW5kLWltcGxlbWVudGluZy10aGUtdC1zbmUtYWxnb3JpdGhtLWZyb20tc2NyYXRjaC8=
).

​
* SVD: A factorization technique that decomposes a matrix into
three other matrices, often noted as U, Σ, and V. It is
fundamental in li

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
