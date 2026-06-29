---
type: entity
tags:
  - CV
  - CV/detection
summary: MS COCO（Common Objects in Context），80 类像素级实例标注数据集，目标检测/分割主流基准。
sources:
  - "wiki/sources/目标检测入门_评测与训练技巧.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 实体：COCO 数据集

## 简介

MS COCO（Common Objects in Context）为目标检测、分割的主流基准，提供像素级实例标注。

## 关键信息

- 80 个物体类别
- 2014 版：80k 训练 / 40k 验证 / 40k 测试
- 学术标准拆分：trainval35k（train + 35k val 子集）训练，minival 本地测试，test-dev 官方服务器提交
- 平均每张图 3.3 类、7.7 实例，小物体多于 Pascal VOC
- 强调 non-iconic（情境中的物体），区别于 ImageNet 的 iconic（孤立物体）
- 提供官方 API（cocoapi）：可视化、评测、误差分析
- COCO 风格 mAP：IoU 0.5→0.95 步长 0.05 取均值

## 关联

- [[目标检测入门_评测与训练技巧]]（来源）
- [[概念_检测评测指标]]
