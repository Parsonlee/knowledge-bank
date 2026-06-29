---
type: entity
tags:
  - CV
  - CV/detection
summary: FPN（Feature Pyramid Networks），自顶向下多尺度特征金字塔，成为检测近乎标配组件。
sources:
  - "wiki/sources/目标检测入门_特征复用与实时性.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 实体：FPN

## 简介

FPN（Feature Pyramid Networks for Object Detection, arXiv:1612.03144）构建自顶向下特征金字塔，融合高层语义与低层空间信息。

## 结构

- 高层特征图经最近邻上采样至低层同尺寸
- 横向连接：1×1 卷积降维 + 逐元素相加
- 每层金字塔独立做 RoI Proposal 和 RoI Pooling
- Max-Pooling 建模位置不变性，FPN 解决尺度不变性

## 影响

已成为目标检测近乎标配组件，后续 TDM、DSSD、FSSD、RefineDet 均为其变体。

## 相关论文

- arXiv:1612.03144 — Feature Pyramid Networks for Object Detection

## 关联

- [[目标检测入门_特征复用与实时性]]（来源）
- [[概念_特征金字塔网络]]
- [[概念_多尺度检测]]
