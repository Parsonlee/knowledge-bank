---
type: concept
tags:
  - LLM/tokenization
confidence: high
created: "2026-06-29"
updated: "2026-06-29"
---

# 概念：Discrete Tokenization（离散化 Token 化）

## 定义

通过向量量化（Vector Quantization, VQ）等技术，将图像/音频/视频/图结构等高维连续输入压缩为紧凑的离散 token，使其与 LLM 原生 token 机制无缝衔接，实现多模态统一建模。

## 核心价值

- 实现高效存储与计算（连续 → 离散压缩）
- 与 LLM 词表空间对齐，使非文本模态能进入语言模型处理框架
- 支持跨模态理解、推理与生成

## 8 类主要 VQ 方法

| 方法 | 特点 |
|------|------|
| VQ | 经典码本，结构简单 |
| RVQ | 多阶段残差，逐步细化精度 |
| PQ | 子空间划分，独立量化 |
| AQ | 多码本叠加，增强表达 |
| FSQ | 每维映射有限标量，无需完整码本，计算高效 |
| LFQ | 符号函数直接离散化，无查表 |
| BSQ | 球面二值量化，单位球面离散化 |
| Graph AR Tokenization | 图结构锚点-关系离散化 |

## 核心挑战：码本坍塌（Codebook Collapse）

训练中有效码字逐渐集中到极少数，码本利用率下降，表示多样性不足。

**解决方案**：
- 码本重置（Code Reset）：未使用码字重新初始化
- 线性再参数化：线性变换优化码字分布
- 软量化（Soft Quantization）：输入为多码字加权组合
- 正则化：熵正则/KL正则提高利用率

## 多模态应用覆盖

- 单模态：图像、音频、图结构、动作序列、推荐系统
- 双模态：Text+Image（最活跃，2023起）、Text+Audio、Text+Video、Text+Graph
- 三模态+：Text+Image+Audio+Action 统一框架

## 开放挑战

梯度传播困难（离散化阻断梯度流）、信息损失、粒度与语义对齐、离散与连续统一、可解释性

## 来源

- [[Discrete_Tokenization多模态综述]]
