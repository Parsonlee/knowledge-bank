---
title: "实战：纠错式 RAG（CRAG）智能体工作流"
source: "https://mail.google.com/mail/u/0/#inbox/198fc6ca70584770"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-30
created: 2026-07-30
description: "以 LlamaIndex 工作流编排 CRAG：先检索用户文档，再用 LLM 评估上下文相关性；必要时转向 Firecrawl 网络搜索，最后聚合上下文生成回答。"
tags:
  - clippings
---

# 实战：纠错式 RAG（CRAG）智能体工作流

纠错式检索增强生成（Corrective RAG，CRAG）是改善 RAG 系统的常见技术。它为检索到的文档加入自我评估步骤，以保留与回答真正相关的上下文。

工作流如下：

1. 用用户查询检索文档。
2. 使用 LLM 评估检索到的上下文是否相关。
3. 只保留相关上下文。
4. 如有需要，执行网络搜索。
5. 聚合上下文并生成回答。

该演示的技术栈包括：

- [Firecrawl](https://firecrawl.link/avi-chawla)：用于深度网络搜索；
- [Milvus](https://github.com/milvus-io/milvus)：自托管向量数据库；
- [Beam](https://github.com/beam-cloud/beta9/)：部署；
- [CometML Opik](https://www.dailydoseofds.com/a-practical-guide-to-integrate-evaluation-and-observability-into-llm-apps/)：追踪和监控；
- LlamaIndex workflows：工作流编排。

## 工作流组件

### 配置 LLM

演示使用通过 Ollama 在本地提供服务的 `gpt-oss` 作为 LLM。

### 配置向量数据库

用户文档被索引并存储在 Milvus 向量数据库集合中。用户输入查询时，这个本地知识源是首先被调用来提取上下文的来源。

### 配置网络搜索工具

若向量数据库取得的上下文不相关，系统会借助 Firecrawl 转向网络搜索。邮件提到其最新 v2 端点提供更快的抓取、语义爬取、新闻与图片搜索等能力。

### 追踪与可观测性

LlamaIndex 可与 CometML 的 Opik 集成，用于追踪每次 LLM 调用、监控并评估 LLM 应用。

### 创建并运行工作流

把 LLM、向量索引和网络搜索工具传入工作流，初始化事件驱动的智能体工作流；一切就绪后再启动它。

### 使用 Beam 部署

系统被包装成 Streamlit 界面，并声明容器所需 Python 库与计算规格。Beam 将容器部署成可通过浏览器访问的 HTTPS Streamlit 服务。邮件中的演示显示：当问题与用户文档无关时，评估步骤会使工作流转用网络搜索，因而仍能回答该问题。

[查看演示视频](https://api.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/o8qDqNFuJPYyvf8DHZTYB8/player)

实现代码位于 [ai-engineering-hub 的 firecrawl-agent 示例](https://github.com/patchy631/ai-engineering-hub/tree/main/firecrawl-agent)。

## 广告 / 推广

邮件推广 RAG 速成课程（基础、评估、优化、多模态、Graph RAG、ColBERT 多向量检索和 ColPali 文档 RAG 等）以及 Daily Dose of Data Science 会员资源；另含广告投放招揽信息。
