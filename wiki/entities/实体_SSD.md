---
type: entity
tags:
  - CV
  - CV/detection
summary: SSD（Single Shot MultiBox Detector），多尺度特征图单阶段检测器，兼顾速度与精度，后续单阶段工作的基础。
sources:
  - "wiki/sources/目标检测入门_经典模型.md"
  - "wiki/sources/目标检测入门_特征复用与实时性.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 实体：SSD

## 简介

SSD（Single Shot MultiBox Detector, arXiv:1512.02325）基于 VGG backbone，在多个卷积阶段的特征图上做检测，每位置多种尺寸/宽高比 Anchor 逐框预测。

## 关键创新

- 多尺度特征图检测：利用不同层级特征图改善小物体检测
- 每格更多 Anchor：不同大小和宽高比，类别概率逐框预测
- 输出：(C+4)×k×m×n，C=类别数，k=每位置框数，m×n=特征图尺寸

## 衍生工作

- DSSD：加学习式反卷积
- RON：反向连接 + Objectness Prior
- FSSD：通道拼接式特征融合
- SSDLite（MobileNets V2）：深度可分离卷积替换检测头

## 关联

- [[目标检测入门_经典模型]]（来源）
- [[目标检测入门_特征复用与实时性]]（来源）
- [[概念_单阶段检测]]
- [[概念_Anchor机制]]
- [[概念_多尺度检测]]
