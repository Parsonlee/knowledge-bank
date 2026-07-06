---
type: concept
tags:
- DeepLearning
- LLM/arch/attention
summary: FlashAttention 是 I/O 感知的精确注意力优化，通过 Kernel 融合、分块计算（Tiling）和在线 Softmax 避免在
  HBM 物化 N×N 中间矩阵，将注意力从内存密集型转为计算密集型。
sources:
- raw/Attention复杂度解析与改进方向 - GRITJW - 博客园.md
- raw/Mamba Explained _ Kola Ayonrinde.md
- raw/[LLM]大模型显存计算公式与优化 - 知乎.md
- raw/一文读懂Mamba：具有选择状态空间的线性时间序列建模 - 知乎.md
- raw/从DeepSeek-V3到Kimi K2：八种现代 LLM 架构大比较.md
- raw/大模型算法岗，面试百问百答.md
- wiki/sources/2025年七大顶流大模型架构.md
- wiki/sources/A_Visual_Guide_to_Mamba_and_SSM.md
- wiki/sources/Attention复杂度解析与改进方向.md
- wiki/sources/LLM面试50题_MIT_CSAIL.md
- wiki/sources/Transformer大模型3D可视化_NanoGPT.md
- wiki/sources/Transformer被挑战_Mamba解析与PyTorch复现.md
- wiki/sources/一文读懂Mamba_知乎.md
- wiki/sources/从DeepSeek-V3到Kimi_K2_八种现代LLM架构大比较.md
- wiki/sources/大模型显存计算公式与优化.md
- wiki/sources/推测解码Speculative_Decoding综述.md
created: '2026-06-26'
updated: '2026-06-26'
confidence: high
---


# 概念：FlashAttention

## 定义

FlashAttention（Tri Dao 等，2022）是一种 I/O 感知（I/O-aware）的注意力优化方法，核心是通过算法重组与硬件协同设计最大限度减少全局显存（HBM）访问，且不做任何近似、保持精度。

## 三大技术要点

1. **核融合（Kernel Fusion）与避免显存物化**：所有前/后向操作融合到一个 CUDA Kernel，在片上 SRAM 完成，只把 N×d 输出写回 HBM，不显式生成 N×N 中间矩阵
2. **分块计算（Tiling）**：Q/K/V 按序列长度分块，外层循环加载 K/V 块、内层加载 Q 块到 SRAM，逐对块算矩阵乘+Softmax 并累加，避免完整 N×N 矩阵
3. **在线 Softmax（Online Softmax）**：维护当前行最大值与归一化累积值，处理每个块时实时更新归一化因子，无需访问完整得分行

## 演进

- **FA-1**：空间复杂度降至线性，加速 2-4 倍
- **FA-2**：优化线程块布局/工作划分，A100 FP16 达约 70% 峰值，H100 540-570 TFLOPs
- **FA-3**：异步重叠（乒乓调度 GEMM/Softmax）+ FP8 低精度（非相干处理抑制异常值），H100 FP16 达 740 TFLOPs（75% 峰值），FP8 接近 1.2 PFLOPs

## 关联

- [[Attention复杂度解析与改进方向]]（来源）
- [[概念_自注意力复杂度]]
- [[实体_FlashAttention]]