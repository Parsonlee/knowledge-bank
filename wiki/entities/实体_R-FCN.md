---
type: entity
tags:
  - CV
  - CV/detection
summary: R-FCN（Region-based Fully Convolutional Networks），通过 Position Sensitive Score Maps 实现全卷积位置敏感检测。
sources:
  - "wiki/sources/目标检测入门_基础网络与分类定位权衡.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 实体：R-FCN

## 简介

R-FCN（Region-based Fully Convolutional Networks, arXiv:1605.06409）解决检测网络全卷积化与位置敏感性的矛盾。

## Position Sensitive Score Maps

- 最后层生成 k²(C+1) 通道特征图，每通道编码物体特定空间部位
- 对每个 RPN 候选区域（RoI），分 k×k bin，每 bin(i,j) 仅取对应 (i,j) 通道做平均池化
- k² 个 bin 投票（均值）→ (C+1) 分数向量 → softmax

## 优势

- 所有可学习参数在共享卷积层，无逐 RoI 非共享计算
- 比 Faster R-CNN 训练/推理更快（Faster R-CNN 有非共享 conv5 逐 RoI 应用）

## 关联

- [[目标检测入门_基础网络与分类定位权衡]]（来源）
- [[概念_位置敏感检测]]
- [[概念_两阶段检测]]
