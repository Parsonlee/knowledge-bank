---
title: "Trace and monitor any AI/LLM app"
source: "https://mail.google.com/mail/u/0/#inbox/19b7766d2c7e9ffc"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-01-01
created: 2026-07-30
description: "介绍生产级开源 LLM 可观测性与追踪平台 Opik (Arize Phoenix)，实现对 Agent 轨迹、Tool Call 延迟与 Token 消耗的全流程监控。"
tags:
  - clippings
---

# 追踪与监控任意 AI/LLM 应用（Trace and monitor any AI/LLM app）

在生产环境中部署大语言模型与 Agent 应用时，缺乏完备的可观测性往往会导致难以定位死循环、高延迟调用以及非预期幻觉输出。

**Opik**（以及 Arize Phoenix）是专为 AI 应用打造的开源、生产级端到端 LLM 可观测性与评估追踪平台。

![图 1：Opik / Phoenix 动态追踪与评估面板](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F151737c6-eded-473d-a0f2-77f29a995a16_1280x1044.gif)
*说明：图 1：Opik / Phoenix 动态追踪与评估面板*

## 核心功能与应用场景

1. **全流程 Trace 追踪**：抓取并可视化 Prompt 链条、系统提示词、检索到的 RAG 上下文片段及 LLM 的最终响应结果。
2. **自动化 Evaluation 评测**：内置幻觉检测（Hallucination Detection）、检索相关性评分以及定制化的 LLM-as-a-Judge 评估算子。
3. **工具调用与性能监控**：精准记录 Agent 循环中每一次外部工具调用（Tool Call）、执行耗时与 Token 成本，帮助优化系统瓶颈。

![图 2：Agent 执行轨迹与 Tool Call 延迟监控图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29552713-e3e0-43d1-9528-e17568df94dd_1620x1096.png)
*说明：图 2：Agent 执行轨迹与 Tool Call 延迟监控图解*
