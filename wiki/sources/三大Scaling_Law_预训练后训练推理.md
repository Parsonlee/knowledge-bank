---
type: source
tags:
- LLM/training
summary: 大模型三大 Scaling Law：预训练/后训练/推理阶段 Scaling 的定义、技术手段与行业意义
sources:
- Cubox/一文详细了解：大模型三大缩放定律（Scaling Law）-2025-06-29.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
## 来源信息

- **标题**：一文详细了解：大模型三大缩放定律（Scaling Law）
- **作者**：ShuYini，AINLPer
- **URL**：https://mp.weixin.qq.com/s/TmANwuqCawcq1Zr3vfNgFg

## 核心要点

- 三大法则总览：预训练 Scaling Law / 后训练 Scaling Law / 推理阶段 Scaling Law（Long Thinking），分别对应训练前、训练后、推理时三个阶段的计算资源利用规律
- **预训练 Scaling Law**（论文：arxiv 2203.15556）：扩大数据集规模、模型参数量和算力，模型性能系统性提升；推动了万亿参数 Transformer、MoE 架构、分布式训练技术的发展；多模态数据（文本/图像/音频/视频）仍在持续驱动这一法则
- **后训练 Scaling Law**（论文：arxiv 2410.12119）：通过微调、蒸馏、RL（RLHF/RLAIF）、Best-of-n 采样、搜索方法等技术提升预训练模型的计算效率、准确率或领域适应性；合成数据增强可补充稀少数据场景
- **推理阶段 Scaling Law**（论文：arxiv 2504.02495，又称 Long Thinking）：推理时动态调整奖励机制提升推理能力，而非增加参数；让模型探索多条推理路径后选最佳；计算方法包括多次/并行采样、SPCT（拒绝式微调+在线 RL）、元奖励模型
- 代表模型：DeepSeek R1（引爆推理 Scaling）、OpenAI o1、Gemini 2.0 Flash Thinking、Qwen3 推理模型

## 关键引文（Cubox 高亮）

> 后训练技术能够进一步提升模型针对特定应用的适应性与相关性。 [重点/高亮]

> 推理阶段 Scaling Law（Long Thinking）发生在推理过程中。强调通过动态调整奖励机制来提升模型的推理能力，而非传统的通过增加模型参数或训练数据。 [重点/高亮]

## 关联

- [[概念_Scaling_Law预训练]] — 预训练规模律核心内容
- [[概念_Scaling_Law后训练]] — 后训练规模律五种技术手段
- [[概念_Scaling_Law推理]] — 推理阶段 Long Thinking 机制
- [[概念_大模型训练三阶段]] — 预训练/指令微调/RLHF 三阶段
- [[概念_MoE混合专家]] — 预训练 Scaling 的架构创新
- [[实体_DeepSeek-R1]] — 推理 Scaling 代表模型
