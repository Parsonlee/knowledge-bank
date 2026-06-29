---
type: concept
tags:
  - LLM/arch/Mamba
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

# SSM 离散化

将连续时间 SSM 转换为可处理离散序列（如文本 token）的过程。

## 动机

SSM 原始形式处理连续信号，但文本、音频采样等均为离散序列，需要离散化。

## Zero-Order Hold（ZOH）

Mamba 使用 ZOH 离散化方法：
- 每次收到离散输入信号，保持其值直到下一个信号到来，形成连续阶梯信号
- 离散化公式：
  ```
  Ā = exp(Δ·A)
  B̄ = (Δ·A)⁻¹·(exp(Δ·A) - I)·Δ·B
  ```

## 步长参数 Δ（Delta）

- Δ 是可学习参数，表示"持续时间"或"停留时间"（linger time/dwell time）
- **大 Δ**：更关注当前 token（多采样当前输入），忽略历史上下文
- **小 Δ**：跳过当前 token，更依赖历史上下文

在 Mamba 中，Δ 也变为输入依赖的（input-dependent），成为选择机制的一部分。

## 训练时的注意

连续参数 Ā 在训练时保存，每次前向传播时动态离散化，而不是直接存储离散版本。

## 来源

- [[A_Visual_Guide_to_Mamba_and_SSM]]
- [[Mamba_Explained_Kola_Ayonrinde]]
- [[Mamba2_SSD_大一统]]
