---
title: "Technical LLM interview question!"
source: "https://mail.google.com/mail/u/0/#inbox/19d8df42bfdf06fb"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-14
created: 2026-07-30
description: "解答高频大模型面试题：如何在禁止使用 LLM 评估的前提下，从 8 万条生产环境 Agent 轨迹中筛选出最具价值的 100 条进行人工审查（对比随机采样、长度过滤及基于嵌入的多样性与聚类筛选）。"
tags:
  - clippings
---
# 大模型技术面试题：8万条 Agent 轨迹的高效采样筛选（Technical LLM interview question!）

### 面试问题

> **题目**：你的生产环境系统中积累了 **80,000 条 Agent 交互轨迹（Trajectories）**。你需要从中挑选出**最值得人工审查的 100 条轨迹**以改进 Agent 性能。
> 
> **限制条件**：**严禁使用 LLM 来自动评估这些轨迹**。你将如何设计筛选方案？

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbccf0d6c-f393-4343-9de2-aa5ed72f3dc6_1081x516.png)

下面我们来逐层探讨可能的解法与工程考量。

### 解法一：随机采样（Random Sampling）

最简单的做法是随机抽取 100 条轨迹。

**缺点**：绝大多数生产环境 Agent 处理的都是常规、简单的请求。随机采样会将宝贵的人工标注预算浪费在毫无难度的标准对话上，无法暴露边界缺陷。

### 解法二：按对话长度过滤（Filter by Conversation Length）

筛选包含 10 轮以上用户消息的长对话。

**原理**：对话轮次越多，说明交互复杂度越高，或者 Agent 在执行任务时遇到了困难并不断重试。

**缺点**：仅依赖长度会导致样本极度偏向特定复杂任务，而忽视了短会话中潜在的死循环或直接拒绝答复的情况。

### 解法三：异常与错误状态过滤（Exception & Failure Filtering）

直接检索标注有 Tool Error、API 超时、JSON 解析失败或反复盲目调用同一工具的轨迹。

**优点**：可以高密度捕获 Agent 崩溃和失败的硬伤场景。

### 解法四：基于嵌入向量的语义聚类与最大多样性筛选（Embedding-based Diversity Clustering）

为了在 100 条配额内最大化审查轨迹的代表性与覆盖面，业界标准的做法是基于向量嵌入进行无监督采样：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F348b55cc-2e33-45b0-8a80-f31681a7ce21_1061x1015.png)

1. **轨迹向量化（Trajectory Embedding）**：将每条轨迹的文本、调用的工具序列及返回结果融合生成一个综合语义 Embedding。
2. **K-Means 聚类**：在嵌入空间中将 80,000 个向量聚类为 100 个簇（Cluster）。
3. **簇内采样**：
   - 从每个簇的质心（Centroid）处抽取 1 条代表性轨迹（捕捉典型场景）。
   - 或者从离质心最远、处于簇边界（Border Points）的孤立点中抽取（捕捉极端边界场景 Outliers）。

通过这种无监督方法，无需调用 LLM 即可在极低开销下挑选出最具代表性与异质性的轨迹组合。
