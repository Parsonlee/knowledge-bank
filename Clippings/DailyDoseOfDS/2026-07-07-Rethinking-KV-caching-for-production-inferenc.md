---
title: "Rethinking KV caching for production inference"
source: "https://mail.google.com/mail/u/0/#inbox/19f3d7ecdb9a83ee"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-07
created: 2026-07-30
description: "深入剖析生产级 LLM 推理的 KV Cache 瓶颈。分析前缀缓存（Prefix Caching）的局限性与推理与缓存管理的计算资源冲突，详解开源项目 LMCache 及其 EuroSys 2025 获奖算法 CacheBlend 实现的解耦缓存架构。"
tags:
  - clippings
---

# 重新思考生产级推理中的 KV 缓存（Rethinking KV caching for production inference）

斯坦福大学的研究人员研究了 AI Agent 实际消耗推理预算的情况。

一项关键发现是：**每次发送给 Agent 的内容中，约有 62% 是重复内容**——即每次对话步骤中重复传入的系统提示词（System Prompts）、工具定义（Tool Definitions）和参考文档。

![Agent 每次步骤中重复发送的大量上下文](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ebb39b4-9521-4593-8c33-50617cad14f3_1200x900.png)

在 2023 至 2026 年间，每个 Token 的价格下降了 80%（GPT-4 级模型从 $30/M 降至 $0.40/M）。但 Agentic 工作流每个任务消耗的 Token 数量是标准 Chatbot 的 **5 到 30 倍**，因为每一步都在重新发送所有上下文。

因此，即使单 Token 变便宜了，总账单依然飙升，因为使用体积的翻倍远远跑赢了降价幅度。

整个行业在优化错误的变量。**如果绝大多数 Token 本就不应该存在，让 Token 变便宜并不能解决根本问题。**

本文将深入拆解开源架构 **LMCache**——它将缓存管理彻底从推理引擎中解耦出来，能够实现高达 **14 倍** 的首 Token 响应时间（Time-To-First-Token, TTFT）提升。

---

### 一、 朴素配置下 Prompt 模型的底层代价

每次提示模型时，模型都会将每一个 Token 传递给注意力机制，为其计算 Key 向量与 Value 向量。

![KV 向量计算过程图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3469bd3a-08a1-4389-89fb-59434b6cb71c_960x671.gif)

这些 K 和 V 向量的集合被称为 **KV Cache**，其计算量随输入长度呈**二次方（Quadratic）**级数上升。

![二次方级数上升的计算复杂度](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b4b874e-c487-4872-a9df-eb59252341ba_1200x900.png)

![显存与算力浪费示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F098550ae-41d0-4c13-83ab-a84e8d010185_1200x800.png)

单块 AMD MI300X GPU 每天产生约 15 TB 的 KV Cache，但大部分在每次请求后就被随手丢弃。系统提示词与文档的 KV Cache 本应完全一致，模型却在每次请求中从头重新计算。

---

### 二、 前缀缓存（Prefix Caching）能解决什么，解决不了什么？

针对该问题，行业提出了前缀缓存（Prefix Caching / Prompt Caching）：如果连续两次请求共享相同的开头 Token（前缀 Prefix），推理引擎便缓存并重用第一轮的 KV 状态。

![前缀缓存匹配原理图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5560c971-cd1f-4e6c-babd-2ca69a6d94fe_1024x565.png)

但这存在**硬性天花板**：缓存部分必须是新请求的**逐字节完全精确前缀**。即使修改单个字符，也会导致缓存彻底失效：

![前缀失效的三个典型场景](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b235653-a216-4f9d-a696-0bc3d1849358_1200x675.png)

![文档顺序变更导致缓存失效](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01ff49cb-bcea-4f62-a4f2-7f5aeadc2ddc_1024x559.png)

1. **多文档 RAG 组合**：分别缓存了文档 A 和文档 B，当查询同时需要 A 和 B 时，B 的缓存状态因未感知 A 的存在而失效。
2. **文档顺序变更**：相同的 3 个文档只要排列顺序不同，每一次排列组合都会导致缓存未命中。
3. **增长的对话历史**：每一轮新对话都会改变前缀之后的完整上下文，导致稳定前缀之后的早期缓存状态失效。

---

### 三、 缓存与推理的算力资源冲突

![推理引擎资源抢占瓶颈](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ce860fb-5781-405c-ac3b-a7aa6afa5a0e_1200x675.jpeg)

在现有引擎（如 vLLM）中，缓存管理与推理工作共用相同的 GPU 线程与显存。当引擎忙于搬运缓存时，推理就会暂停。

缓存管理是 **I/O 密集型**（在 GPU、CPU 与存储间搬运海量张量），而推理则是 **计算密集型**（GPU 上的矩阵乘法），两者本质上是截然不同的工作负载。

---

### 四、 LMCache 的解耦架构与 CacheBlend 突破

**LMCache** 将缓存层与推理引擎彻底解耦：

![LMCache 解耦架构设计](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4d68035-dc85-47a2-807e-ae3019333712_2397x1333.png)

![LMCache 三层共享架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf6a69a5-e245-4987-b37a-7fcd52a3a3bb_1200x800.png)

此架构带来三大收益：
1. **无限缓存容量**：利用 CPU 内存与本地 NVMe SSD/S3 扩展 KV 存储。
2. **跨 Engine/Pod 共享缓存**：在一个 Worker 上计算的 KV Cache 可立刻供其他集群 Worker 重用。
3. **零推理暂停**：后台异步执行 Cache 换入换出。

#### CacheBlend 算法（EuroSys 2025 Best Paper）

为了解决非前缀/多文档组合的缓存失效问题，LMCache 团队研发了 **CacheBlend** 算法：

![CacheBlend 混合缓存选择机制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80e0eaa8-329d-4687-a3bc-62a29400170c_1200x675.png)

CacheBlend 仅需重新计算极其一小部分受交叉注意力（Cross-Attention）影响关键 Token 的 KV 状态，并将它们与已缓存的独立 KV 块平滑融合，从而在打破前缀限制的前提下保持 99%+ 的回答准确率。

* GitHub 仓库：[github.com/lmcache/lmcache](https://github.com/lmcache/lmcache)
