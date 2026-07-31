---
title: "为使用自托管技术栈的 AI 开发者提供的重大更新（Massive update for AI devs working on self-hosted stacks.）"
source: "https://mail.google.com/mail/u/0/#inbox/19acc373a89bc8c4"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-28
created: 2026-07-30
description: "MongoDB 推出了社区版和企业版 Search 和 Vector Search 的公开预览，为构建 RAG 和语义搜索的自托管基础设施带来了重大升级，去除了以往需要组合多个系统的复杂性。"
tags:
  - clippings
---

# 为使用自托管技术栈的 AI 开发者提供的重大更新（Massive update for AI devs working on self-hosted stacks.）

MongoDB 刚刚在社区版（Community Edition）和企业版（Enterprise Server）中推出了 Search（搜索）和 Vector Search（向量搜索）的公开预览。如果您倾向于运行自己的基础设施，这绝对是一个巨大的利好。

在此之前，任何构建语义搜索或 RAG（检索增强生成）系统的人，都需要结合使用 Elasticsearch、一个单独的向量数据库，以及一条 ETL 流水线来保持所有数据的同步。

现在，您可以抛开所有这些复杂性了。

MongoDB 在其数据库内部直接为您提供了全文搜索、模糊搜索、语义搜索以及向量搜索的功能。

其中有两大亮点：

* **您可以免费在本地构建和测试 AI 应用**：社区版现在原生支持向量索引和混合搜索，因此您可以无需云环境即可进行原型开发。
* **您的搜索索引和操作数据保持完美一致**：原生的向量搜索消除了因为协调多个外部系统而带来的“同步税”。

对于那些在裸机或自托管基础设施上构建 RAG 系统、智能体记忆层或语义搜索功能的开发者来说，这是一次重大的升级。
