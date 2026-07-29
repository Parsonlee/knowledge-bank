---
title: Clustering Evaluation Without Labels
source: https://mail.google.com/mail/u/0/#inbox/1995434d669b06de
author:
  - "[[DailyDoseOfDS]]"
published: 2025-09-16
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Clustering Evaluation Without Labels 的原理剖析与工程实践。
tags:
  - clippings
---

# Clustering Evaluation Without Labels

## 1. 核心要点解析

本期内容重点涵盖：
- **Clustering Evaluation Without Labels**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.kit-mail1.com/mvug5g3q6xt5hq3o9k4amhrp67qqqb3h5ed66/wnh2hghqww0xklu7/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Free video tutorials to Master LLM evals & observability.
* Clustering evaluation without labels.
* [Hands-on] Scale ML models to billions of parameters.​

TODAY'S ISSUE

LLM evals
---------

-----------------------------------------------------------------
​Free video tutorials to Master LLM evals & observability (
https://click.kit-mail1.com/mvug5g3q6xt5hq3o9k4amhrp67qqqb3h5ed66/reh8hohm006w3pf2/aHR0cHM6Ly93d3cuY29tZXQuY29tL2RvY3Mvb3Bpay9vcGlrLXVuaXZlcnNpdHkvb3ZlcnZpZXc=
)​
-----------------------------------------------------------------

(
https://click.kit-mail1.com/mvug5g3q6xt5hq3o9k4amhrp67qqqb3h5ed66/reh8hohm006w3pf2/aHR0cHM6Ly93d3cuY29tZXQuY29tL2RvY3Mvb3Bpay9vcGlrLXVuaXZlcnNpdHkvb3ZlcnZpZXc=
)​
Opik is an open-source platform for evaluating and monitoring LLM
apps, and if you're new to LLM monitoring, we found some free
learning modules by Opik University (
https://click.kit-mail1.com/mvug5g3q6xt5hq3o9k4amhrp67qqqb3h5ed66/reh8hohm006w3pf2/aHR0cHM6Ly93d3cuY29tZXQuY29tL2RvY3Mvb3Bpay9vcGlrLXVuaXZlcnNpdHkvb3ZlcnZpZXc=
) that start from the basics to production-ready monitoring.

Here's what it teaches:

* Observability: Log and trace your LLM applications
* Evaluation: Build datasets and metrics that matter
* Prompt engineering: Experiment in the Prompt Playground
* Production monitoring: Set up automated evaluation rules
* Testing: Integrate with your PyTest workflows

Each module includes hands-on video tutorials for enhanced
learning.

​You can find them in the documentation here → (
https://click.kit-mail1.com/mvug5g3q6xt5hq3o9k4amhrp67qqqb3h5ed66/reh8hohm006w3pf2/aHR0cHM6Ly93d3cuY29tZXQuY29tL2RvY3Mvb3Bpay9vcGlrLXVuaXZlcnNpdHkvb3ZlcnZpZXc=
)​

-->LLM evals and observability tutorials (
https://click.kit-mail1.com/mvug5g3q6xt5hq3o9k4amhrp67qqqb3h5ed66/reh8hohm006w3pf2/aHR0cHM6Ly93d3cuY29tZXQuY29tL2RvY3Mvb3Bpay9vcGlrLXVuaXZlcnNpdHkvb3ZlcnZpZXc=
)
LLM evals and observability tutorials (
https://www.comet.com/docs/opik/opik-university/overview )

machine learning
----------------

------------------------------------
Clustering evaluation without labels
------------------------------------

Continuing the discussion on evaluation...

Evaluating clustering quality is usually difficult since we have
no labels. Thus, we must rely on intrinsic measures to determine
clustering quality.

Here are three metrics I commonly use:

**************************
1) Silhouette coefficient:
**************************

Here's the core idea:

If the average distance to all data points in the same cluster is
small...

...but that to another cluster is large...

...this indicates that the clusters are well separated and
somewhat "reliable."

It is measured as follows:

For every data point:

* A → average distance to all other points within its cluster.
* B → average distance to all points in the nearest cluster.
* score = (B-A)/max(B, A)

Next, compute the average of all scores to get the overall
clustering score.

If B is much greater than A, then score=1 and it indicates the
clusters are well separated.

Measuring it across a range of centroids (k) can reveal which
clustering results are most promising:

​

*****************************************************************
​2) Calinski-Harabasz Index (
https://click.kit-mail1.com/mvug5g3q6xt5hq3o9k4amhrp67qqqb3h5ed66/08hwh9h2ddlg98sl/aHR0cHM6Ly9zY2lraXQtbGVhcm4ub3JnL3N0YWJsZS9tb2R1bGVzL2NsdXN0ZXJpbmcuaHRtbCNjYWxpbnNraS1oYXJhYmFzei1pbmRleA==
)​
*****************************************************************

The run-time of Silhouette score grows quadratically with total
data points.

Calinski-Harabasz Index handles this, while being similar to
Silhouette score.

​
Here’s how it is measured:

* A → sum of squared distance between centroids and the dataset's
center.
* B → sum of squared distance between all points and their
specific centroid.
* Metric is computed as A/B (with an additional scaling factor).

If A is much greater than B, then score>>1 and it indicates the
clusters are well separated.

Calinski-Harabasz Index makes the same intuitive sense as the
Silhouette Coefficient while being much faster to compute.

*****************************************************************
​3) DBCV (
https://click.kit-mail1.com/mvug5g3q6xt5hq3o9k4amhrp67qqqb3h5ed66/8ghqhohollrq3ehk/aHR0cHM6Ly9naXRodWIuY29tL2NocmlzdG9waGVyamVubmVzcy9EQkNW
)​
*****************************************************************

Silhouette score and Calinski-Harabasz index are typically higher
for globular (spherical in the case of 3D) clusters.

Thus, using them on density-based clustering can produce
misleading results.

DBCV (density-based clustering validation) solves this, and it
computes two values:

* The density within a cluster.
* The density overlap between clusters.

A high density within a cluster and a low density overlap between
clusters indicate good clustering results. The effectiveness of
DBCV is evident from the image below:

​
As depicted above:

* The clustering output of KMeans is worse, but its Silhouette
score is still higher than that of Density-based clustering.
* With DBCV, the score for the clustering output of KMeans is
worse, and that of density-based clustering is higher.

That said, here, we covered centroid-based and density-based
evaluation.

* You can read about Distributed-based clustering and its
evaluation here: Gaussian Mixture Models (GMMs) (
https://click.kit-mail1.com/mvug5g3q6xt5hq3o9k4amhrp67qqqb3h5ed66/vqh3hrhoppwe4xug/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZ2F1c3NpYW4tbWl4dHVyZS1tb2RlbHMtZ21tLw==
).
* Also, you can read about DBSCAN++ here

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
