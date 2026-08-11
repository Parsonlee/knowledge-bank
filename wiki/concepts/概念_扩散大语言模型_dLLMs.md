---
type: concept
tags:
  - Architecture
  - LLM
  - Diffusion-LLM
  - Inference-Optimization
sources:
  - wiki/sources/2026-07-27_The-anatomy-of-diffusion-LLMs_19fa57.md
updated: 2026-08-04
summary: "扩散大语言模型从全掩码序列出发，利用双向注意力多步并行解掩码多个 Token，使推理由内存带宽受限转向更适合现代 GPU 的计算受限模式。"
---

# 概念定义
**扩散大语言模型（Diffusion Large Language Models, dLLMs）** 是一种将扩散模型（Diffusion Models）原理引入文本生成的新一代语言模型架构。与传统的自左向右逐 token 序列生成的自回归模型不同，dLLM 允许模型从完全掩码（Full Mask）的占位序列开始，在多步迭代中通过双向注意力机制，在全局层面上并行且逐步地填充/恢复真实 token（即解掩码，Unmasking）。

---

# 核心架构比对：自回归 vs. 扩散语言模型

| 维度 | 自回归文本生成（Autoregressive） | 扩散语言模型（dLLMs） |
| :--- | :--- | :--- |
| **生成机制** | 自左向右，逐个 token 递归生成（Left-to-Right） | 全掩码开始，多步迭代并行解掩码（Parallel Decentering） |
| **注意力机制** | 单向因果注意力（Causal Attention） | 双向注意力（Bidirectional Attention） |
| **硬件计算特征** | **Memory-Bound（内存带宽受限）**<br>每生成一个 token，都必须将完整的模型权重从显存载入 GPU 寄存器，计算密度极低（在 A100 上约 1 FLOP/Byte）。 | **Compute-Bound（计算受限）**<br>单步内并行计算/预测多个掩码 token，极大提高了单次访存的计算密度，释放 GPU 的浮点算力。 |
| **生成特征** | 吞吐量与序列长度呈强线性负相关（受限于逐 token 推理） | 高并发吞吐，更利于长文本生成和批量并行解码 |

- **关联概念**：关于自回归模式下的 Prefill 和 Decoding 阶段，详见 [[wiki/concepts/概念_LLM推理两阶段|LLM推理两阶段]]。dLLM 通过并行化生成在根本上重塑了传统的 Decoding 阶段瓶颈。

---

# 离散掩码扩散机制（Masked Diffusion）

由于文本由离散的 Token 组成，传统的连续型高斯噪声（Gaussian Noise）无法直接应用于离散的文本符号空间，因此 dLLMs 采用了**离散掩码扩散（Masked Diffusion）**机制：

1. **前向加噪过程（Forward Process）**：在离散空间中，所谓的“加噪”就是将序列中的一部分真实 Token 按照特定的转移概率，替换为特殊的掩码 Token `[MASK]`，直到整个序列变为全 `[MASK]` 状态。
2. **反向去噪/解掩码过程（Reverse Process）**：给定一个被部分掩饰的序列，模型预测每个 `[MASK]` 位置的真实 Token 概率分布。
3. **训练目标函数**：通过变分证据下界（Variational Evidence Lower Bound, ELBO）推导的目标函数进行端到端训练。模型在不同掩码率的文本样本上，学习如何最优化重构缺失的 Token 信息。

---

# 转换与兼容核心技术

为了能够在大参数量下（如 8B 到 100B）训练和无缝过渡，dLLMs 引入了以下关键技术：

### 1. Block Diffusion（块扩散）
- **机制**：传统的扩散模型每次反向迭代需要重写整个序列，因而无法有效利用 KV Cache。Block Diffusion 通过将序列分块，在块级别上执行扩散，从而实现了与传统 KV Cache 机制的无缝兼容（如 BD3-LM 架构）。

### 2. Attention Mask Annealing（注意力掩码退火）
- **机制**：直接从头训练一个大规模 dLLM 非常昂贵。该技术允许开发者直接使用现成的、已在海量数据上预训练好的自回归模型（如 LLaMA-3）。在继续预训练阶段，将因果注意力掩码（Causal Mask）逐步退火（Anneal）并放开为双向注意力掩码，同时引入 MASK 噪声，从而低成本地将自回归模型转换为高性能的双向扩散模型。

---

# 推理加速栈与解码技术

为了在生产环境中跑出高吞吐，dLLM 的推理生态通常包含以下加速机制：

1. **Confidence-Aware（置信度感知）并行解码**：在解掩码的每一步，模型可以根据预测的置信度，优先确定那些高置信度位置的真实 Token，而将置信度较低的 Token 留到下一步再进行预测或修正。这种非自回归的解码机制进一步缩减了生成所需要的迭代步数。
2. **Fast-dLLM 块级 KV 缓存**：优化块级别扩散中的 Key-Value 缓存，大幅减少不必要的重复计算。
3. **Token 编辑与灵活生成**：如 LLaDA 2.1 支持在生成序列中直接对任意位置进行 Token 插入、修改和删除，无需像自回归模型那样必须从头开始重写（Regenerate）。
4. **生产 serving 框架**：SGLang 等服务框架已经集成了对 Dream 7B 等 dLLM 模型的生产级部署支持。
