---
title: "NVIDIA researchers built a new transformer variant"
source: "https://mail.google.com/mail/u/0/#inbox/19f6174c7b5adc67"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-14
created: 2026-07-30
description: "解析 NVIDIA 研究团队提出的 SparDA 架构。通过引入下一层 KV 块预测投影（Forecast Projection），实现 CPU RAM 到 GPU 显存的重叠预取，将解码速度提升 1.7 倍，长链推理准确率提升 6.5 分。"
tags:
  - clippings
---

# NVIDIA 推出新型 Transformer 变体 SparDA（NVIDIA researchers built a new transformer variant）

NVIDIA 研究人员对 Transformer 架构进行了一项微小改进，实现了：
* **解码速度提升 1.7 倍**
* **长链推理（Long-reasoning）准确率提升 6.5 分**

在典型的 Transformer 架构中，每个注意力层都会计算 Q、K 和 V。NVIDIA 的这项改进额外增加了一个**第四投影（Fourth Projection / Forecast Projection）**，用于提前预测下一层将需要哪些 Key-Value 块。

---

### 一、 传统长上下文推理的性能痛点

稀疏注意力（Sparse Attention）是解决长上下文推理的常用尝试。与其关注每一个缓存的 Token，现代设计将 KV Cache 分块计分，仅保留 Top-k 块并只对这些块计算注意力。

虽然这降低了注意力计算量与带宽开销，但依然留有两个棘手问题：

1. **KV Cache 随生成的 Token 持续膨胀**：在 100K+ 上下文中，显存无法再放下 KV Cache，不得不 Offload 卸载到 CPU RAM 中。此时，每一层必须先将选中的 KV 块从 CPU 内存复制回 GPU 显存。这种复制极慢，导致 GPU 处于闲置等待状态，且在每个解码步的每一层重复发生。
2. **选择步（Selection Step）开销并不免费**：标准选择器需要用 GQA 组内的每个 Query 头对每个候选块进行打分，再对每个头的得分做 Softmax 并跨头求和。

---

### 二、 SparDA 的核心技术突破

NVIDIA 提出的 **SparDA** 架构通过以下设计攻克了上述瓶颈：

```
[当前 Layer 计算注意力] ── (并行 CUDA Stream 预取) ──> [将下一层所需的 KV 块从 CPU 提前拉取至 GPU]
```

1. **预测重叠预取（Forecast Prefetching）**：由于在计算当前层时下一层的候选块已被 Forecast 投影提前预测，运行时在独立的 CUDA Stream 上将这些块从 CPU 内存拉取到 GPU 显存。数据传输与当前层的计算完美重叠，GPU 无需再等待数据搬运。
2. **极轻量计分头**：SparDA 为每个 GQA 组仅使用一个 Forecast 头，剥离了逐 Query 头打分的循环，并完全跳过了 Softmax 步骤。

该改动的额外参数极小：在 8B 模型上仅新增了 33.5M 参数（占比仅 **0.41%**），且训练时只需训练这些新增投影，优化损失采用与其原始选择器块分布匹配的 KL 散度。

---

### 三、 实验结果与性能表现

在 MiniCPM4.1-8B 和 NOSA-8B 模型上的实验结果表明：

* **准确率**：达到或超越了稀疏基线，在 NOSA-8B 上长链推理表现获得了 **+6.5 分** 的显著提升。
* **推理延迟**：Prefill 预填阶段提速高达 **1.25x**，Decode 解码阶段提速高达 **1.7x**（对比稀疏 Offload 基线）。
* **吞吐量爆发**：由于预取隐藏了 Offload 的传输成本，绝大部分 KV Cache 可以放心地留存于 CPU RAM 中，释放出的 GPU 显存支持更大 Batch 大小，将解码吞吐量提升至非 Offload 稀疏基线的 **5.3 倍**。

需要说明的是，这种前瞻预取（Lookahead）在配合 CPU Offload 的解码阶段收益最大；在 Prefill 阶段，由于所有 Key 均已存在于 GPU 显存中，此时的性能收益纯粹来自于更轻量的块选择过程。

* 论文地址：[arXiv:2606.04511](https://arxiv.org/abs/2606.04511)
