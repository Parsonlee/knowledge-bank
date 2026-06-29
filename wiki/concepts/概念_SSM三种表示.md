---
type: concept
tags:
  - LLM/arch/Mamba
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

# SSM 三种表示

同一个 SSM 可以用三种等价方式表示，各有优劣，实践中按任务选择。

## 连续表示（Continuous）

原始微分方程形式：h'(t) = Ah(t) + Bx(t)；y(t) = Ch(t)

- 数学基础，不直接用于计算

## 循环表示（Recurrent）

离散化后的 RNN 形式：
```
h_k = Ā·h_{k-1} + B̄·x_k
y_k = C·h_k
```

- 优势：推理高效，每步只需上一隐状态，O(1) 内存，理论上无限上下文
- 劣势：训练时无法并行，需逐步计算

## 卷积表示（Convolutional）

将 SSM 展开为与固定卷积核的卷积：
```
y = K * x   （K 为 SSM kernel，由 Ā/B̄/C 推导）
```

- 优势：训练可并行（类似 CNN），支持 FFT 加速
- 劣势：kernel 固定，无法用于选择性 SSM；推理不如循环高效

## 实践策略

**训练用卷积表示，推理用循环表示**

这是 LSSL（Linear State-Space Layer）的核心思想，S4 和 Mamba 均继承此策略。

注意：Mamba 引入选择机制后 B/C 依赖输入，卷积 kernel 不再固定，无法直接用卷积形式训练，改为 parallel scan。

## 来源

- [[A_Visual_Guide_to_Mamba_and_SSM]]
