---
type: concept
tags:
  - LLM/arch/Mamba
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

# HiPPO 矩阵

**Hi**gh-order **P**olynomial **P**rojection **O**perators，一种特殊的矩阵 A 构造方法，使 SSM 的隐状态能够高效压缩和记忆历史。

## 核心思想

HiPPO 将所有输入信号压缩为一组 Legendre 多项式的系数向量，使隐状态能够：
- 精确重建近期 token
- 对较旧的 token 平滑衰减

## 公式

HiPPO 矩阵 A 的元素：
```
A_{nk} = -(2n+1)^(1/2)(2k+1)^(1/2)  if n > k
A_{nk} = n+1                          if n = k
A_{nk} = 0                            if n < k
```

## 作用

- 随机初始化矩阵 A 效果差；HiPPO 初始化显著提升长程记忆能力
- S4 的核心创新之一：将 HiPPO 应用于 SSM 的递归和卷积表示
- Mamba 继承 HiPPO 初始化，矩阵 A 在选择机制中保持静态（仅 B/C/Δ 变为输入依赖）

## 数学背景

基于 Legendre 多项式的投影理论，隐状态可近似重建完整历史序列的系数。详见 Annotated S4（srush.github.io/annotated-s4）。

## 来源

- [[A_Visual_Guide_to_Mamba_and_SSM]]
- [[实体_S4]]
