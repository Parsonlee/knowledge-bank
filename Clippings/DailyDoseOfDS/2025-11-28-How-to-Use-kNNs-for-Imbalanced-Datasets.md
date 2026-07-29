---
title: How to Use kNNs for Imbalanced Datasets
source: https://mail.google.com/mail/u/0/#inbox/19acc373a89bc8c4
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-28
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 How to Use kNNs for Imbalanced Datasets 的原理剖析与工程实践。
tags:
  - clippings
---

# How to Use kNNs for Imbalanced Datasets

## 1. 核心要点解析

本期内容重点涵盖：
- **How to Use kNNs for Imbalanced Datasets**

## 2. 深度拆解与正文翻译

​Master full-stack AI Engineering (
https://click.convertkit-mail2.com/gkukxk8wqdf5hlp08eoarh8we3e99imho2n00/p8heh9h4x9d835aq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Massive update for AI devs working on self-hosted stacks.
* How to use kNNs for imbalanced datasets.
* ​Two techniques to extend the context length of LLMs​.

TODAY'S ISSUE

Together with MongoDB
---------------------

-----------------------------------------------------------------
​Massive update for AI devs working on self-hosted stacks (
https://click.convertkit-mail2.com/gkukxk8wqdf5hlp08eoarh8we3e99imho2n00/x0hph6he3nzxrlc5/aHR0cHM6Ly9mYW5kZi5jby8zWG5iTWFU
)​
-----------------------------------------------------------------

MongoDB just rolled out Search and Vector Search in public
preview for both Community Edition and Enterprise Server. This is
huge if you prefer running your own infra.

​
Until now, anyone building semantic search or RAG needed a mix of
Elasticsearch, a separate vector DB, and an ETL pipeline to keep
everything in sync.

Now you can drop all that complexity.

MongoDB gives you full-text search, fuzzy search, semantic
search, and vector search right inside your database.

Two things stand out:

* You can build and test AI apps locally for free: Community
Edition now ships with vector indexing and hybrid search, so you
can prototype without the cloud.
* Your search index and operational data stay perfectly aligned:
Native vector search removes the sync tax that comes from
juggling multiple external systems.

This is a serious upgrade for developers building RAG systems,
agent memory layers, or semantic search features on bare metal or
self-hosted infra.

​You can try the quick start here → (
https://click.convertkit-mail2.com/gkukxk8wqdf5hlp08eoarh8we3e99imho2n00/x0hph6he3nzxrlc5/aHR0cHM6Ly9mYW5kZi5jby8zWG5iTWFU
)​

-->MongoDB quick start docs (
https://click.convertkit-mail2.com/gkukxk8wqdf5hlp08eoarh8we3e99imho2n00/x0hph6he3nzxrlc5/aHR0cHM6Ly9mYW5kZi5jby8zWG5iTWFU
)
MongoDB quick start docs ( https://fandf.co/3XnbMaT )

data science
------------

-----------------------------------------------------------------
​How to use kNNs for imbalanced datasets (
https://click.convertkit-mail2.com/gkukxk8wqdf5hlp08eoarh8we3e99imho2n00/6qheh8hlopw0k2ho/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vOC1mYXRhbC15ZXQtbm9uLW9idmlvdXMtcGl0ZmFsbHMtYW5kLWNhdXRpb25hcnktbWVhc3VyZXMtaW4tZGF0YS1zY2llbmNlLw==
)​
-----------------------------------------------------------------

kNN is highly sensitive to the parameter k.

To understand this, consider this dummy 2D dataset below (the red
data point is a test instance we want to generate a prediction
for using kNN and k=7):

​
Generating a prediction will involve:

​
* counting its 7 nearest neighbors
* assigning it to the class with the highest count among those 7
neighbors.

The problem with Step 2 is that it is entirely based on class
contribution. So the class that maximally contributes to the k
nearest neighbors is picked.

But this fails when you have imbalanced datasets.

For instance, with k=7, the red data point below can NEVER be
assigned to the yellow class, no matter how close it is:

​
There are two ways to address this.

**************************************
Solution #1: Used distance-weighed kNN
**************************************

Distance-weighted kNNs are a robust alternative to traditional
kNNs, that consider distance to the nearest neighbor for
classification.

For instance, below, the green data point gets classified as red
with traditional kNN (k=7), despite being closer to the blue
cluster:

​
But the same data point gets classified as blue with
distance-weighed kNN:

​
That said, it is not the default option in implementations like
sklearn, so make sure to enable it:

​

****************************************************
Solution #2: Dynamically update the hyperparameter k
****************************************************

Recall the above dataset again:

​
Here, you may argue that one must refrain from setting the
hyperparameter k to any value greater than the minimum number of
samples across all classes.

But there’s a problem with it.

Setting a super low value of k is usually not ideal in extremely
imbalanced datasets:

​
Setting a globally low value of k (say, 1 or 2) leads to
suboptimal performance since it does not holistically evaluate
the nearest neighbor patterns compared to what a large value of k
can do.

But we just discussed above that setting a large value of k, also
leads to the domination problem.

Both problems can be solved by dynamically updating the
hyperparameter k based on the situation.

More specifically, there are three steps in this approach.

For every test instance:

* Set a standard value of k as we usually would and find the k
nearest neighbors.
* Next, for all classes that appear in the k nearest neighbors,
find the total number of training instances they have.

Here, we found blue and yellow classes in the 7 nearest
neighbors, with a total of 40 and 3 samples respectively.
* Update the value of k to:

​
Now perform majority voting only on the first k’ neighbors only.

Here’s why this makes sense:

* If a minority class appears in the top k nearest neighbor, the
update rule will reduce the value of k so that the majority class
does not dominate.
* If a minority class DOES NOT appear in the top k nearest
neighbor, it will likely not update the value of k (because k
would be the smallest value during the update process) and do a
holistic classification.

The only shortcoming is that you wouldn’t find this approach in
any open-source implementations.

Some further reading:

* ​We covered 8 fatal (yet non-obvious) pitfalls and cautionary
measures in data 

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
