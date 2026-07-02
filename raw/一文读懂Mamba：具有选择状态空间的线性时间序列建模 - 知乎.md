---
id: "7210560026904103335"
cubox_url: https://cubox.pro/web/card/7210560026904103335
url: https://zhuanlan.zhihu.com/p/680846351
tags:
  - LLM/arch/Mamba
---
# 一文读懂Mamba：具有选择状态空间的线性时间序列建模 - 知乎

Mamba: Linear-Time Sequence Modeling with Selective State SpacesMamba：基于选择状态空间的线性时间序列建模 论文两位作者Albert Gu和Tri Dao，博士都毕业于斯坦福大学，导师为Christopher Ré。 Albert Gu现…

[Read in Cubox](https://cubox.pro/web/card/7210560026904103335)  
[Read Original](https://zhuanlan.zhihu.com/p/680846351)  

---


---

## 📖 正文全文

# 一文读懂Mamba：具有选择状态空间的线性时间序列建模

[zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/680846351)SakuraK

## Mamba: Linear-Time Sequence Modeling with Selective State Spaces

![](https://image.cubox.pro/cardImg/bp3qhiu92qzum99pn62amr2ketvx3djcpog8be8q0ln1ql40f.jpg?imageMogr2/quality/90/ignore-error/1)

Mamba：基于选择状态空间的线性时间序列建模

论文两位作者Albert Gu和Tri Dao，博士都毕业于斯坦福大学，导师为Christopher Ré。

Albert Gu现在是CMU助理教授，多年来一直推动SSM架构发展。他曾在DeepMind 工作，目前是Cartesia AI的联合创始人及首席科学家。

Tri Dao，以FlashAttention、FlashDecoding系列工作闻名，现在是普林斯顿助理教授，和Together AI首席科学家，也在Cartesia AI担任顾问。

Code：[https://github.com/state-spaces/mamba](https://link.zhihu.com/?target=https%3A//github.com/state-spaces/mamba)

## Background

基础模型（FM），即在海量数据上进行预训练，然后针对下游任务进行调整的大型模型，已成为现代机器学习的有效范式。这些模型几乎都基于 Transformer 架构及其核心注意力模块。

自注意力的效果主要归功于它**能够在上下文窗口中密集地传递信息**的能力，使其能够对复杂数据进行建模。然而，这一特性也带来了一些根本性的缺陷：

1. **无法对有限窗口外的任何内容进行建模：**自注意力机制通常在一个固定的上下文窗口（如一个句子或一个图像的一部分）内操作，这意味着它只能考虑并处理这个窗口内的信息。当需要理解或分析的信息分散在更大的上下文中，或者与当前窗口相隔较远时，自注意力可能无法有效捕捉这些信息，因为自注意力缺乏直接的机制来处理或引入窗口之外的信息。这在处理长篇文本或大规模图像时尤其成问题，因为重要信息可能分布在整个文档或图像中。
2. **窗口长度的二次缩放问题：**自注意力的一个关键特点是它在计算时需要比较和加权窗口内的所有元素对。这意味着如果窗口长度增加，所需的比较（和因此的计算资源）会以二次方的方式增加。例如，如果窗口长度加倍，那么所需的计算量将增加四倍。这种二次缩放性质使得自注意力在处理大窗口或长序列时变得效率低下。

为了解决 Transformer 在长序列上的计算效率低下问题，人们开发了许多亚二次时间架构，如线性注意力、门控卷积和递归模型以及结构化状态空间模型（SSM）。此类模型的一个关键弱点是**无法进行基于内容的推理**。

其中SSMs最有潜力，它可以被解释为**递归神经网络（RNN）和卷积神经网络（CNN）的结合**，其灵感来自经典的状态空间模型（卡尔曼，1960）。但它们在离散和信息密集数据（如文本）的建模方面不太有效。

## Contribution

### 改进

作者提出了一类新的选择性状态空间模型，该模型在多个维度上改进了先前的工作，从而在序列长度线性缩放的同时，实现了Transformer的建模能力。主要的改进有以下几点：

1. **选择机制** 先前的模型，特别是那些用于处理序列数据的模型，可能在**有效选择数据** 方面存在局限，它们可能不够有效地关注重要的输入信息或忽略不相关的输入信息。**选择性复制** 和**归纳头**等合成任务在理解和改进模型的选择机制方面提供了重要的直觉。于是作者设计了一种简单的选择机制，根据输入对 SSM 参数进行参数化（让 SSM 参数成为输入的函数）。这样，模型就能过滤掉无关信息，并无限期地记住相关信息。
2. **硬件感知算法**先前的SSM

[Read in Cubox](https://cubox.pro/web/card/7210560026904103335)
