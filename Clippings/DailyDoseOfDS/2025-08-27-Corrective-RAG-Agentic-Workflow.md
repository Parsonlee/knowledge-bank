---
title: "纠正性 RAG 代理工作流（Corrective RAG Agentic Workflow）"
source: "https://mail.google.com/mail/u/0/#inbox/198ed2e36353fdf7"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-27
created: 2026-07-30
description: "详细解析了一种称为纠正性 RAG (CRAG) 的代理工作流架构，利用自我评估和网络搜索来提升系统质量。"
tags:
  - clippings
---

# 纠正性 RAG 代理工作流（Corrective RAG Agentic Workflow）

纠正性 RAG (CRAG) 是一种改进 RAG 系统的常用技术。它引入了对检索到的文档进行自我评估的步骤，有助于保持生成回答的相关性。工作流如下：

1. 使用用户查询搜索文档。
2. 使用 LLM 评估检索到的上下文是否相关。
3. 仅保留相关的上下文。
4. 如有必要，执行网络搜索。
5. 汇总上下文并生成回复。

在演示的架构中：使用 Firecrawl 进行深度网络搜索；使用 Milvus 作为本地部署的向量数据库；使用 Beam 进行无服务器快速部署；结合 Cometml 的 Opik 追踪和监控 LLM 调用；并用 LlamaIndex 工作流进行编排。
