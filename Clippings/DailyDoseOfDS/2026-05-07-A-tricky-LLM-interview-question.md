---
title: "A tricky LLM interview question."
source: "https://mail.google.com/mail/u/0/#inbox/19e0470d88335c78"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-07
created: 2026-07-30
description: "深入拆解大模型面试高频难题：为什么 RAG 系统在语料库从 5k 扩展到 500k 时检索准确率会剧烈暴跌？结合 EnterpriseRAG-Bench 实验数据剖析向量空间邻域密度对召回率的影响。"
tags:
  - clippings
---

# 一道非常棘手的 LLM 面试题（A tricky LLM interview question.）

面试问题：

> 你的 RAG 系统在 5,000 份公司文档上达到了 **90%** 的检索准确率。
> 
> 但在保持相同 Embedding 模型和 Retriever 的情况下，将文档规模扩展到 500,000 份后，准确率暴跌到了仅 **50%**。
> 
> 为什么会出现这种情况？

![检索准确率随着文档规模扩大而剧烈下降](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2d9eb8f-b3c0-4274-9c0c-0e79ee19f5fe_1080x1080.gif)

最简单的回答是：文档越多，意味着对 Top-K 检索槽位的竞争越激烈。这虽然是事实，但无法完全解释为什么准确率会出现如此剧烈的下降。

问题的核心在于**企业文档在向量空间（Embedding Space）中的分布特征**。

在现代企业中，单个业务决策会同时产生会议转录、Slack 聊天记录、Confluence 文档、Jira 任务以及 Email 邮件：

![同一业务事件关联的多源文档在向量空间中紧密聚集](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9581535a-317d-4c4e-a0c5-a2f56bf7c458_1376x768.jpeg)

因为它们都围绕同一个项目或事件，所以它们都会落在向量空间的同一紧密区域内。随着公司运营数月，这一模式在每个项目、客户和路线图中反复出现，向量空间被大量高度相关的文档簇填充。

然而，**所有相关的文档并不包含相同的事实**：
- Slack 讨论涵盖了决策做出的背景；
- Jira 包含具体的开发截止日期；
- Confluence 包含技术架构规范；
- 邮件包含客户的原始需求。

当用户查询针对某个具体事实（例如“截止日期”）时，真正的答案仅存在于其中某一份文档中。

在 **5K 语料库规模**下，触及该主题的文档可能只有 3-5 份，包含正确答案的那一份文档能轻易挺进 Top-K 检索结果中：

![不同规模下的向量空间簇与 Top-K 挤出机制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74f11d2b-44e7-469c-ba97-a964cd542cfe_2752x1536.jpeg)

但在 **500K 语料库规模**下，相关文档可能多达 40-60 份。包含实际答案的那份文档非常容易被其他主题相关但缺乏关键事实的文档挤出 Top-K，导致检索召回率严重退化。

Onyx 最近发表的开源基准数据集 **EnterpriseRAG-Bench**（包含 50 万+ 真实企业仿真文档）证实了这一现象：

![邻域密度与 Recall 的强相关关系](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce290718-fba5-45e7-8b10-e01e778d5f50_1376x768.jpeg)

研究人员在 5K 到 500K 的五个语料库规模上测试了相同的检索器：

- 纯向量检索（Vector Search）准确率从 5K 文档时的 **90.7%** 一路降至 500K 文档时的 **50.6%**；
- 传统 BM25 检索表现得更为平缓，从 **85.8%** 降至 **68.4%**；
- 在任何规模下，向量空间中更高的**邻域密度（Neighborhood density）**都与更低的召回率呈现出单调强相关。

![向量检索与 BM25 在不同规模下的衰减曲线对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F628fff35-5b1a-4575-ae14-69bc8791f724_1201x646.png)
