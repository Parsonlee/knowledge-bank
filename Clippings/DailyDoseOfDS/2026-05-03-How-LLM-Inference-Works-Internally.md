---
title: "How LLM inference works internally."
source: "https://mail.google.com/mail/u/0/#inbox/19deeeb458239986"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-03
created: 2026-07-30
description: "全景拆解 LLM 推理的两阶段机制（计算受限的 Prefill 阶段与内存带宽受限的 Decode 阶段），分析 KV Cache 瓶颈与架构演进。"
tags:
  - clippings
---

# LLM 推理底层工作原理深度拆解（How LLM inference works internally.）

对大语言模型执行的每一次 `generate()` 调用，都会在同一块 GPU 上经历两个截然不同的计算阶段：
- **Prefill（预填充/ Prompt 处理阶段）**：属于**算力受限型（Compute-bound）**。
- **Decode（解码/ 逐 Token 生成阶段）**：属于**内存带宽受限型（Memory-bound）**。

绝大多数推理优化技术都针对其中某一个阶段展开，诊断哪个阶段是性能瓶颈是加速部署的第一步。

---

### 1. 分词与嵌入（Tokenization and Embedding）
BPE 分词器将原始文本转换为词表中的整数 ID。每个 ID 映射到形状为 `[vocab_size, hidden_dim]` 的嵌入矩阵行。位置信息通过 **RoPE（旋转位置编码）** 注入，通过旋转嵌入向量而非加算位置向量来编码位置。

---

### 2. Transformer 层前向传播
嵌入后的序列通过多层 Transformer：
1. **自注意力机制（Self-Attention）**：计算 $Q, K, V$ 投影。每个 Token 的 Query 对所有 Token 的 Key 进行打分，经 Softmax 加权后混合 Value。
2. **前馈网络（FFN）**：通过两层 MLP 独立处理每个 Token 的向量。注意力机制在位置间传递信息，FFN 负责特征转换。

---

### 3. Prefill 阶段 vs Decode 阶段

#### Prefill 阶段（Compute-bound）
并行处理所有输入 Token，计算大矩阵乘法。GPU 算力利用率极高。核心衡量指标为 **TTFT（Time to First Token，首 Token 延迟）**。在此阶段，系统会初始化并填充 **KV Cache**。

#### Decode 阶段（Memory-bound）
每次仅生成一个 Token，只为新 Token 计算 $Q, K, V$。虽然每步算力极小，但 GPU 必须为极小的计算量反复将整个模型权重和全部 KV Cache 从显存加载到算力核心中，瓶颈翻转为**内存带宽**。核心指标为 **ITL（Inter-Token Latency，Token 间延迟）**。

---

### 4. KV Cache 的挑战与工程优化
若无 Cache，生成 $N$ 个 Token 的注意力计算复杂度将呈 $O(N^2)$ 二次增长。KV Cache 带来了巨大的加速（可达 5 倍以上），但也带来了显存开销：例如 13B 模型下每 Token 约占用 1 MB，4K 上下文直接消耗 4 GB VRAM。

主流优化路线包括：
- **KV 缓存量化**（INT8/INT4）
- **滑动窗口注意力（Sliding Window Attention）**
- **分组查询注意力（Grouped-Query Attention, GQA）**
- **PagedAttention**（vLLM 采用的分页内存管理技术）

---

### 5. 前沿突破：围绕 Cache 重新设计注意力机制
DeepSeek V4 系列通过结构化设计直接减小 Cache 体积：
- **CSA（Compressed Sparse Attention，压缩稀疏注意力）**：将 KV 压缩 4 倍后执行稀疏注意力。
- **HCA（Heavily Compressed Attention，强力压缩注意力）**：将 128 个 Token 的 KV 压至单个表示后执行密集注意力。

在 1M Context 上下文中，对比 DeepSeek-V3.2，V4 仅需 27% 的单 Token 推理 FLOPs 和 10% 的 KV Cache 显存占用，彻底重塑了推理服务架构。
