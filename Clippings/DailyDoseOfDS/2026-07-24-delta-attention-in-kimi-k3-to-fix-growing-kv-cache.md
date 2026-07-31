---
title: "Delta attention in Kimi K3 to fix growing KV cache"
source: "https://mail.google.com/mail/u/0/#inbox/19f962933027e3e6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-24
created: 2026-07-30
description: "深度解析 Kimi K3 模型采用的 Delta Attention 机制，阐述其如何通过维护动态增量状态消除传统膨胀 KV Cache 带来的显存瓶颈。"
tags:
  - clippings
---

# Kimi K3 中的 Delta Attention 机制：解决持续膨胀的 KV Cache（Delta attention in Kimi K3 to fix growing KV cache）

在传统 Transformer 架构中，随着上下文长度 $N$ 的增长，KV Cache 的显存占用呈线性增长 $\mathcal{O}(N)$，极大限制了超长文本推理时的并发能力与 Batch Size。

月之暗面（Moonshot AI）最新发布的 **Kimi K3** 依靠一种名为 **Delta Attention** 的新机制，完全打破了对持续膨胀 KV Cache 的依赖。

![Kimi K3 Delta Attention 架构示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44a11973-6572-4b28-b2a2-d30f4127f66c_1268x569.jpeg)
*图 1：Delta Attention 核心逻辑架构*

---

### 一、 Delta Attention 的工作原理

与保存过往所有 Token 的 Key 和 Value 张量不同，Delta Attention 引入了一种**固定大小的动态增量状态（Delta State）**。

在每一步生成时：
1. 传入的新 Token 计算其增量变化（Delta）；
2. 增量变化被用于更新循环隐状态（Recurrent State）；
3. 注意力计算直接在该常数复杂度的隐状态上完成，无需回溯历史序列。

![Delta Attention 显存占用与计算开销对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c16b109-ac40-4b6a-bed3-0a553382b4d2_1237x516.jpeg)
*图 2：Delta Attention 与传统 KV Cache 的显存开销对比*

---

### 二、 工程价值与性能收益

* **显存开销固定**：推演时的显存复杂度从 $\mathcal{O}(N)$ 降至 $\mathcal{O}(1)$；
* **极大吞吐提升**：消除显存瓶颈后，单卡 GPU 上可以支持 10 倍以上的大 Batch 推理；
* **超长上下文支持**：无论上下文扩展到几十万还是数百万 Token，推理延迟与显存使用始终保持平稳。

这一技术创新使 Kimi K3 在保持全上下文注意力质量的同时，获得了极高的生产级推理效率。
