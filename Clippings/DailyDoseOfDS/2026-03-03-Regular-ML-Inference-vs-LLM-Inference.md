---
title: "Regular ML Inference vs. LLM Inference"
source: "https://mail.google.com/mail/u/0/#inbox/19cb52ae130cbc14"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-03
created: 2026-07-30
description: "对比传统机器学习推理与大语言模型（LLM）推理的核心差异，深入解析连续批处理、Prefill-Decode 分离、Paged Attention、前缀路由及专家并行等技术。"
tags:
  - clippings
---
# 传统 ML 推理与 LLM 推理的区别（Regular ML Inference vs. LLM Inference）

相比于传统机器学习推理，LLM 推理面临着独特的挑战，这也促使行业开发出了如 vLLM、LMCache、SGLang 和 TensorRT LLM 等专门的高性能 LLM 推理引擎。

本文将探讨这些核心挑战及其解决方案！

## 1. 连续批处理（Continuous batching）

传统模型（如 CNN）具有固定尺寸的图像输入和固定长度的输出（如分类标签），这使得批处理（Batching）变得非常简单：

![传统模型固定尺寸批处理](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe71fbda8-e4bf-4686-92d3-c6e4cef4130a_627x167.png)

然而，LLM 处理的是变长输入（提示词）并生成变长输出：

![LLM 变长输入与输出](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34adfce4-ac6f-4447-adbe-1bcba3021497_627x167.png)

如果按传统方式对请求组批，所有请求结束的时间各不相同，GPU 必须等待最长的请求完成后才能处理新请求，这会导致大量的 GPU 空闲等待时间：

![传统批处理导致的 GPU 空闲碎片](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f7947bf-3b07-4076-9e5c-382717d41b09_820x647.png)

**连续批处理（Continuous Batching）** 解决了这一问题：系统实时监控所有序列，一旦某条序列生成完毕（达到 `<EOS>` Token），便立即将其替换为新请求：

![连续批处理动态替换已完成请求](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F260c0368-3012-4022-974e-1632a306649a_820x647.png)

这保持了 GPU 流水线的满载运行，大幅提升了利用率。

## 2. Prefill 与 Decode 阶段分离（Prefill-decode disaggregation）

LLM 推理包含两个资源需求截然不同的阶段：

* **Prefill 阶段**：一次性处理所有输入 Prompt Token，属于**计算密集型（Compute-heavy）**。
* **Decode 阶段**：自回归逐 Token 生成输出，要求**低延迟（Low latency）**（通常为访存密集型）。

![Prefill 阶段与 Decode 阶段特点对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a4aaf46-75c2-4959-aff9-16d6bf071894_906x161.png)

如果在同一块 GPU 上同时运行这两个阶段，计算密集型的 Prefill 请求会严重干扰对延迟敏感的 Decode 请求。

**Prefill-Decode 分离架构** 解决了这个问题：通过分配专门的 GPU 池处理 Prefill 阶段，另分配独立的 GPU 池处理 Decode 阶段：

![Prefill 与 Decode 节点解耦架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ef916a4-59b1-44c2-aa56-f4f86ff5cbde_886x514.png)

相比之下，标准 ML 模型通常只有一个统一的计算阶段。

## 3. GPU 内存管理与 KV 缓存（GPU memory management + KV caching）

生成新 Token 需要使用之前所有 Token 的 Key 和 Value 向量。为了避免重复计算，我们会将它们缓存起来（即 KV Cache）：

![KV Cache 原理图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86b13d74-204f-4165-81ed-13ef6655dd34_996x1016.jpeg)

该 KV Cache 会随着对话历史长度线性增长。

在许多工作流中，如系统提示词（System Prompt）在许多请求中是共享的。我们可以通过在不同对话间复用这些 Key/Value 向量来避免重复计算：

![共享系统 Prompt 前缀的 KV Cache 复用](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F870313d3-6afb-4573-adec-ed767fd38f6d_1227x807.png)

然而，由于传统 KV Cache 存储在连续内存块中，占用了大量显存，并导致了严重的内存碎片化：

![连续内存分配导致的显存浪费与碎片](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3d247ef-5945-4107-bb9b-03fc7ac12531_2452x676.png)

**Paged Attention** 通过将 KV Cache 存储在非连续的物理块中，并借助查找表（Lookup Table）进行管理，解决了此问题。LLM 只加载所需的内存块，无需一次性分配连续显存。

## 4. 前缀感知路由（Prefix-aware routing）

扩展标准 ML 模型时，只需简单地在多台服务器/GPU 间复制模型，并使用轮询（Round Robin）或发往最空闲服务器的简单负载均衡策略即可，因为每个请求相互独立。

但 LLM 极其依赖缓存（如上述共享 KV 前缀），请求之间不再独立。如果新查询包含已在副本 A 上缓存的公共前缀，但路由将其发往更空闲的副本 B，副本 B 就必须重新计算整个前缀的 KV Cache。

**前缀感知路由（Prefix-aware routing）** 解决了这一瓶颈：

![前缀感知路由示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41885dc8-c398-473c-b39e-a3c186099e44_1440x1490.png)

路由器维护全局映射表（或预测算法），跟踪各 GPU 副本当前缓存的 KV 前缀，并将新请求直接分发到已有该前缀缓存的副本上。

## 5. 模型分片与混合专家架构（Model sharding strategies & MoE）

扩展密集型 ML 模型有多种策略（如张量并行、流水线并行）：

![密集模型分片策略](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19c29872-5d12-4426-9d6f-50db8bf6d0dd_1022x1138.gif)

而大语言模型中的混合专家（MoE）更加复杂：

![MoE 架构示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab3bce91-359f-4410-8019-3518b4535022_1116x1126.gif)

MoE 模型采用特殊的**专家并行（Expert Parallelism）**：将专家网络本身分片部署在不同设备上，而注意力层在所有 GPU 上复制：

![专家并行（Expert Parallelism）在多 GPU 间的分片部署](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e34f5f8-d504-42bc-b298-1853f4dc0065_1745x1596.png)

动态门控网络（Gating Network）根据当前激活的专家决定 Token 路由，这要求推理引擎能高效管理分片专家池之间复杂的动态计算流。
