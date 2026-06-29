---
type: entity
tags:
  - CV
summary: ViT（Vision Transformer），将图像分 patch 序列输入 Transformer 的视觉 Backbone；SAM 用 ViT-H 作图像编码器。
sources:
  - "wiki/sources/SAM_Segment_Anything模型.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: medium
---

# 实体：ViT

## 简介

ViT（Vision Transformer）由 Google（Dosovitskiy et al.）提出，将图像分割为 patch，作为序列 token 输入标准 Transformer 编码器，借自注意力获取全局上下文。

## 在 SAM 中的应用

- SAM 图像编码器使用 ViT-H/16（Huge，16×16 patch）
- 采用 MAE（Masked Autoencoder, Kaiming He 等）预训练
- 三种规模对应 SAM 三个版本：ViT-B/L/H

## 备注

全文主要在 SAM 架构语境下介绍 ViT（confidence: medium）。

## 关联

- [[SAM_Segment_Anything模型]]（来源）
- [[概念_Vision_Transformer]]
- [[实体_SAM]]
- [[实体_CLIP]]
