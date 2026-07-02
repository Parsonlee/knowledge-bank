---
type: source
tags:
- LLM/tokenization
summary: 首个面向多模态LLM的离散化Tokenization系统化综述，梳理8类VQ方法与跨模态应用全景
sources:
- raw/从离散token到多模态统一：Discrete Tokenization全景综述....md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
# 从离散token到多模态统一：Discrete Tokenization全景综述

## 来源信息

- **标题**：从离散token到多模态统一：Discrete Tokenization全景综述重磅上线
- **论文**：Discrete Tokenization for Multimodal LLMs: A Comprehensive Survey（arxiv 2507.22920）
- **论文仓库**：https://github.com/jindongli-Ai/LLM-Discrete-Tokenization-Survey
- **来源平台**：微信公众号 PaperWeekly
- **URL**：https://mp.weixin.qq.com/s/_R6enntOYBcBF8eKTMBzwA
- **作者单位**：香港科技大学（广州）、吉林大学、香港中文大学、南京大学、加州大学默塞德分校

## 核心要点

- **背景动机**：LLM能力扩展至非文本模态时，需要将图像/音频/视频/图结构等高维连续信号转化为LLM可处理的离散表示，Discrete Tokenization（向量量化VQ）成为关键方案
- **8类核心VQ方法**：
  1. **VQ**（Vector Quantization）：经典码本设计与更新，结构简单
  2. **RVQ**（Residual VQ）：多阶段残差量化，逐步细化编码精度
  3. **PQ**（Product Quantization）：乘积量化，子空间划分独立量化
  4. **AQ**（Additive Quantization）：多码本叠加建模，增强表达能力
  5. **FSQ**（Finite Scalar Quantization）：每维独立映射有限标量集，无需显式存储完整码本
  6. **LFQ**（Lookup-Free Quantization）：符号函数直接离散化，无码本查表
  7. **BSQ**（Binary Spherical Quantization）：球面二值量化，单位球面上离散化
  8. **Graph Anchor-Relation Tokenization**：面向图结构的锚点-关系离散化
- **码本坍塌（Codebook Collapse）**：训练中有效码字收敛到极少数，码本利用率下降。解决方案：码本重置、线性再参数化、软量化、正则化（熵正则/KL正则）
- **早期应用（pre-LLM）**：图像检索与合成、音频编解码、视频帧级表示、图结构节点/边表示；视觉-语言描述生成、语音-文本互转、跨模态生成
- **LLM驱动单模态**：图像/音频/图结构/动作/推荐系统均可通过离散token与LLM词表空间融合
- **LLM驱动多模态**：双模态（Text+Image为主，起步2023年）和三模态+组合（Text+Image+Audio+Action）统一token空间协同工作
- **当前挑战**：码本利用率不足、信息损失、梯度传播困难、粒度与语义对齐、离散与连续表示统一、跨模态迁移性、可解释性
- **未来方向**：自适应量化、统一框架、生物启发码本、跨模态泛化、可解释性提升

## 关联

### 概念
- [[概念_Transformer架构]] — 离散token与LLM架构衔接基础
- [[概念_向量量化]] — VQ核心技术（Discrete Tokenization的底层）

### 实体
- [[实体_Qwen3-VL]] — 多模态LLM代表，Discrete Tokenization的应用场景
- [[实体_Florence-2]] — 多模态视觉基础模型，统一Seq2Seq框架

### 相关 Source
- [[从LLaVA到Qwen3-VL_多模态架构演进]] — 多模态LLM架构演进视角
- [[A_Visual_Guide_to_Mamba_and_SSM]] — 序列建模替代架构

---
> 📎 **物理文献**：[[raw/从离散token到多模态统一：Discrete Tokenization全景综述....md]]
