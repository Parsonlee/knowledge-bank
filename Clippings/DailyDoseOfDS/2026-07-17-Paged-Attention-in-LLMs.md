---
title: "Paged Attention in LLMs"
source: "https://mail.google.com/mail/u/0/#inbox/19f721c214ca5038"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-17
created: 2026-07-30
description: "解析 PagedAttention 技术的原理，说明其如何借鉴操作系统虚拟内存分页机制解决大模型推理服务中的 KV Cache 显存碎片化问题。"
tags:
  - clippings
---

# 大模型推理中的 PagedAttention 技术原理（Paged Attention in LLMs）

在高并发大模型推理服务中，显存（GPU Memory）往往比算力更早成为系统瓶颈。

传统 KV Cache 管理方式要求在连续显存空间中预分配最大序列长度的内存，这导致了严重的**显存碎片化与内部浪费（高达 60%-80% 显存被浪费）**。

![PagedAttention 虚拟内存与物理 Block 映射图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F594d51b3-7540-47bc-a4be-72d174a1f6df_1456x794.png)
*图 1：PagedAttention 虚拟内存与物理 Block 映射机制*

---

### 一、 PagedAttention 的核心思想

vLLM 提出的 **PagedAttention** 灵感直接来源于操作系统的**虚拟内存分页（Virtual Memory Paging）**技术：

1. **逻辑切块（Logical Blocks）**：将 Key 和 Value 张量按固定大小（如 16 个 Token）切分为逻辑块；
2. **物理映射（Physical Blocks）**：物理显存不必连续，通过 Block Table 将逻辑块动态映射至离散的物理显存块中；
3. **按需分配**：仅在产生新 Token 时才分配新的物理 Block，几乎消除了所有内部显存碎片。

---

### 二、 工程价值

* **近乎零显存浪费**：显存浪费率从 60%+ 降低至 4% 以下；
* **支持高并发共享**：在 Parallel Sampling、Beam Search 及 Complex Agents 场景下，多个 Request 可以安全共享相同的 Physical Block（如相同的 System Prompt），大幅提升服务吞吐量。
