---
type: concept
tags:
- Infra/AI
- LLM/inference
summary: 大语言模型（LLM）推理过程可分为 Prefill（预填充）和 Decode（解码）两个不同的计算阶段。Prefill 阶段是计算密集型（Compute-bound），并行处理输入并填充
  KV Cache；Decode 阶段是内存带宽密集型（Memory-bound），自回归逐字生成 token。
sources:
- wiki/sources/2026-05-03_How-LLM-inference-works-internally_19deee.md
updated: '2026-08-04'
---

# 概念：LLM 推理两阶段

## 定义

在大语言模型（LLM）的单次生成请求中，推理过程由两阶段构成：**Prefill（预填充）** 阶段和 **Decode（解码）** 阶段。由于这两个阶段的计算特征（并行度与存取比）存在本质差异，它们面临的硬件瓶颈、硬件利用率以及性能指标完全不同。

---

## 阶段对比分析

| 维度 | Prefill 阶段 (预填充) | Decode 阶段 (解码) |
| :--- | :--- | :--- |
| **工作内容** | 一次性处理用户输入的所有 Prompt tokens，计算对应的注意力 Key 和 Value，并填充到 KV 缓存（KV Cache），同时生成首个输出 token。 | 自回归地逐个生成后续 tokens。每步仅将新生成的单个 token 输入模型计算其 QKV，并结合 KV Cache 里的历史 K/V 进行注意力计算。 |
| **硬件瓶颈** | **计算绑定（Compute-bound）**<br>所有输入 tokens 并行计算，以大矩阵相乘的形式在 GPU 运行，算力吞吐量（Throughput）是瓶颈。 | **内存带宽绑定（Memory-bound）**<br>由于是一步步串行计算单向量与矩阵的乘法，GPU 每一生成步都必须将模型权重和全部 KV Cache 从显存重新加载到 SRAM 中，算力极大闲置（利用率常低于 30%）。 |
| **核心性能指标** | **首字延迟 (Time to First Token, TTFT)**<br>用户发送请求到模型输出第一个 token 的等待时长。 | **词间延迟 (Inter-Token Latency, ITL)**<br>相邻两个输出 token 之间的平均生成间隔。 |
| **资源消耗规律** | 输入 prompt 越长，TTFT 呈非线性增加。 | 输出 sequence 越长，ITL 和 KV Cache 的显存开销越大。 |

---

## 三大服务优化方案

为了应对这两个阶段的瓶颈，推理服务引擎引入了以下核心优化方案：

### 1. 连续批处理 (Continuous Batching)
传统的 Batching 方式需要等待同一批次中所有的序列都生成完毕后才能开始下一批，这在 Decode 阶段会造成显著的算力空闲（短序列已结束，长序列仍在生成）。连续批处理（迭代级批处理）允许在 token 级别动态合并、交织和重叠不同请求的 Prefill 和 Decode 任务，极大提升了 GPU 利用率。

### 2. 推测解码 (Speculative Decoding)
通过一个参数量小、运行速度极快的“草稿模型”（Draft Model）快速自回归生成多个候选 tokens（草稿），然后将这些草稿一次性输入“目标大模型”（Target Model）进行并行计算和验证。
- **原理**：将 Decode 阶段的多次串行内存加载，转化为一次并行的大矩阵乘法计算（即利用 Prefill 的计算绑定特性来校验草稿），在草稿接受率高的情况下能显著降低 ITL。

### 3. PagedAttention (分页注意力)
在大模型服务中，KV Cache 的动态增长导致了显存的高碎片化与预分配过度。
- **原理**：借鉴了操作系统虚拟内存分页的思想，将 KV Cache 存储在非连续的固定大小物理内存块（Block）中。通过虚拟表映射，在运行时动态分配。这消除了内部和外部显存碎片，使得 GPU 可以容纳更大的 Batch Size。

---

## 关联

- [[2026-05-03_How-LLM-inference-works-internally_19deee]] （来源）
- [[概念_KV_Cache]] （KV Cache 原理及结合）
