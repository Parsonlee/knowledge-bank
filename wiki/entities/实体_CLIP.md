---
type: entity
tags:
- CV
summary: CLIP（Contrastive Language-Image Pre-training），OpenAI 视觉-语言对齐模型，为 SAM 提供文本
  Prompt 能力。
sources:
- raw/Jina AI创业复盘：AI团队的Scaling Law是什么.md
- raw/R1 的一些认知 - 知乎.md
- raw/RAG之延迟交互与残差压缩：从ColBERT到ColBERTv2的演进及其应用.md
- raw/Sora的幕后功臣？详解大火的DiT：拥抱Transformer的扩散模型.md
- raw/Transformer被挑战？新架构Mamba解析以及Pytorch复现.md
- raw/一文读懂向量数据库，原理到应用全解析！.md
- raw/从LLaVA到Qwen3-VL，多模态大模型主流架构的演进之路.md
- raw/信息过载时代，如何真正「懂」LLM？从MIT分享的50个面试题开始 ｜ 机器之心.md
- raw/分割一切(Segment Anything)不是梦，SAM模型引领图像分割新时代....md
- raw/基于 Elasticsearch 创建企业 AI 搜索应用实践.md
- raw/实战｜13个Pytorch 图像增强方法总结（附代码）.md
- raw/自适应快慢思考推理模型（Adaptive Reasoning Model）：Qw....md
- wiki/sources/LLM面试50题_MIT_CSAIL.md
- wiki/sources/PyTorch图像增强方法总结.md
- wiki/sources/R1复现认知与误区.md
- wiki/sources/SAM_Segment_Anything模型.md
- wiki/sources/从LLaVA到Qwen3-VL_多模态架构演进.md
- wiki/sources/向量数据库原理与应用全解析.md
created: '2026-06-26'
updated: '2026-06-26'
confidence: medium
---

# 实体：CLIP

## 简介

CLIP（Contrastive Language-Image Pre-training）由 OpenAI 提出，用于视觉-语言理解，通过对比学习对齐图像与文本嵌入。

## 关键信息（全文所述）

- 训练使用对比损失对齐图文嵌入
- 在 SAM 中的作用：提供文本 Prompt 能力，使 SAM 可接受文本指定分割目标（SAM 基础模型不原生支持文本，需 CLIP 集成）

## 补充知识（非本文）

- 双编码器架构：图像编码器（ViT 或 ResNet）+ 文本编码器（Transformer）

## 备注

全文在 SAM 多模态集成语境下介绍 CLIP，细节有限（confidence: medium）。

## 关联

- [[SAM_Segment_Anything模型]]（来源）
- [[概念_Prompt驱动分割]]
- [[实体_SAM]]
- [[实体_ViT]]