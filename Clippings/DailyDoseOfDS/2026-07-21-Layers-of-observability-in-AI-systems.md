---
title: "Layers of observability in AI systems"
source: "https://mail.google.com/mail/u/0/#inbox/19f86be0631f8e2c"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-21
created: 2026-07-30
description: "解析 AI 系统的可观测性分层架构，详细阐述 Trace 与 Span 的设计原理，以及如何在生产级 RAG 和 Agent 系统中实施细粒度监控与成本追踪。"
tags:
  - clippings
---

# AI 系统中的可观测性分层架构（Trace 与 Span）（Layers of observability in AI systems）

随着 AI 系统逐渐演变为真正的生产级软件，传统的分布式追踪（Distributed Tracing）、Span 与埋点实践在 AI 领域变得不可或缺。

如果仅观察整个 AI 系统的输入与最终输出，一旦发生幻觉或性能下降，你将无法确定问题出在检索、上下文组装还是 LLM 本身。

![RAG 系统中 Trace 与 Spans 的分层结构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F396bbceb-1c96-4f82-8f42-caac63d96aed_3958x780.png)
*图 1：RAG 管道中 Trace 与多个子 Span 的对应关系*

---

### 一、 Trace 与 Span 的基本概念

* **Trace（追踪）**：捕获单次请求的全生命周期，从用户提交 Query 开始到接收最终响应结束。一个请求对应唯一的 Trace ID。
* **Span（跨度）**：Trace 内部的具体子操作单元。每个 colored 区域代表一个独立的 Span。

---

### 二、 RAG 管道中 5 个核心 Span 详解

1. **Query Span**：记录用户输入的原始文本、时间戳及 Session 元数据。
2. **Embedding Span**：监控查询转化为向量的 API 耗时与 Token 数，及时捕获向量接口限流。
3. **Retrieval Span**：记录向量数据库检索过程。经验表明大部分 RAG 异常（如 Bad Chunks、Top-$k$ 设置不当）均暴露在此 Span。
4. **Context Span**：记录检索到的切片与 System Prompt 拼接后的完整上下文，监控 Context 是否溢出。
5. **Generation Span**：记录 LLM 生成响应的过程，耗时最长且成本最高。详细日志化 Input/Output Token 数与延迟。

通过细粒度的 Span 监控，团队能够精准进行成本分摊（Cost Tracking）、性能瓶颈排查以及模型漂移检测。在 [Comet Opik](https://github.com/comet-ml/opik) 等开源工具中均已全面集成该可观测抽象。
