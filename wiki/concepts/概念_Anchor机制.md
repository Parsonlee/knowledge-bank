---
type: concept
tags:
  - CV
  - CV/detection
summary: 在特征图位置上预设多种尺度与宽高比的参考框（Anchor），作为检测回归基准。
sources:
  - "wiki/sources/目标检测入门_经典模型.md"
  - "wiki/sources/目标检测入门_评测与训练技巧.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 概念：Anchor 机制

## 定义

Anchor（锚框）是在特征图每个位置预设的多种尺度、多种宽高比参考框，检测网络在其基础上做分类与坐标回归。

## 来源与发展

- 由 Faster R-CNN 的 RPN 首次引入：滑窗在共享特征图上，每位置生成多尺度多宽高比 Anchor，二分类（含物体/背景）+ 4 个坐标回归值。
- SSD 在多尺度特征图上每位置生成多个 Anchor，逐框预测类别概率。
- YOLOv2 借鉴 Anchor，并用 k-means 聚类训练集真实框尺寸生成更优 Anchor 先验（详见 [[目标检测入门_评测与训练技巧]]）。

## 关联

- [[目标检测入门_经典模型]]（来源）
- [[概念_两阶段检测]]
- [[概念_单阶段检测]]
- [[实体_YOLO]]
