---
type: entity
tags:
  - CV
  - CV/detection
summary: YOLO（You Only Look Once），首个单阶段检测模型，将检测视为回归问题实现实时推理。YOLOv2 全面升级。
sources:
  - "wiki/sources/目标检测入门_经典模型.md"
  - "wiki/sources/目标检测入门_特征复用与实时性.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 实体：YOLO

## 简介

YOLO（You Only Look Once: Unified, Real-Time Object Detection, arXiv:1506.02640）是首个单阶段检测模型，将检测问题统一为端到端回归。

## YOLO v1

- 图像分 S×S 网格，每格预测 B 个框（坐标+置信度）+ C 个类别概率
- 输出张量：S×S×(B×5+C)
- 损失：坐标误差 + 置信度误差 + 类别误差（加权平衡）
- 优点：实时速度、全局上下文、较少背景误检
- 缺点：粗网格导致小目标和密集目标弱

## YOLOv2（YOLO9000）

论文：arXiv:1612.08242。全面升级：

- 所有卷积层加 Batch Normalization，去 Dropout
- 引入 Anchor Boxes，FC 层换为卷积
- k-means 聚类训练集框尺寸生成 Anchor 先验
- 坐标回归用 log/exp 变换
- Passthrough 层：多尺度特征拼接（类 ResNet skip）
- 多尺度训练
- 新 backbone：Darknet-19（VGG 风格，参数更少）

## 关联

- [[目标检测入门_经典模型]]（来源）
- [[目标检测入门_特征复用与实时性]]（来源）
- [[概念_单阶段检测]]
- [[概念_Anchor机制]]
