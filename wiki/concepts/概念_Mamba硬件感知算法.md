---
type: concept
tags:
  - LLM/arch/Mamba
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

# Mamba 硬件感知算法

Hardware-Aware Algorithm，Mamba 为弥补选择机制丧失卷积并行性而设计的 GPU 高效计算方案。

## 背景

GPU 有两类内存：
- **SRAM**：小（约几十 MB）但极快
- **HBM/DRAM**：大（数十 GB）但相对慢

频繁在 SRAM↔HBM 之间搬运数据是计算瓶颈，FlashAttention 已用类似思路解决 Attention 的 IO 问题。

## 三个核心技术

### 1. Parallel Scan（并行扫描）

选择性 SSM 的递归计算看似串行（每步依赖上一步），但利用结合律可以分段并行处理，再迭代合并：

```
普通扫描：h1→h2→h3→...→hT  （串行）
并行扫描：[h1,h2] [h3,h4] ... 分块计算后合并  （并行）
```

### 2. Kernel Fusion（算子融合）

将多个操作合并为一个 CUDA kernel，在 SRAM 中连续执行，避免中间结果写回 HBM：

融合的操作：离散化（Δ 作用）→ Selective Scan → 乘以矩阵 C

### 3. Recomputation（重计算）

反向传播需要中间隐状态，但不存储（存储会占用大量 HBM）。改为在反向传播时重新计算，比从 HBM 读取更快。

## 效果

- 内存需求与 FlashAttention 优化的 Transformer 相当
- 推理速度最高 5× 快于同等参数量 Transformer

## 与 FlashAttention 的联系

两者思路相同：减少 SRAM↔HBM 数据搬运次数，将计算尽量保留在 SRAM 中。Tri Dao 是 FlashAttention 和 Mamba 的共同作者。

## 来源

- [[A_Visual_Guide_to_Mamba_and_SSM]]
- [[Mamba_Explained_Kola_Ayonrinde]]
- [[Transformer被挑战_Mamba解析与PyTorch复现]]
- [[实体_FlashAttention]]
