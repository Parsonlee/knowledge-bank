---
type: entity
tags:
  - CV/data-augmentation
summary: Albumentations 是一个 Python 图像增强库，提供丰富的变换操作和 OneOf/Compose 组合机制，支持概率控制。
sources:
  - "wiki/sources/OCR的有效数据增强.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: medium
---

# 实体：Albumentations

## 简介

Albumentations 是一个相对较新的 Python 库，用于简单但强大的图像增强。提供多种变换操作，通过 `Compose` 和 `OneOf` 机制灵活组合。

## 要点（基于全文提及）

- 支持变换：RandomRain、RandomShadow、PixelDropout、ShiftScaleRotate、Affine、Blur 等
- `OneOf`：包含一组可能的变换，仅以概率 P 执行其中一个，用于将相似变换分组避免过度使用
- `Compose`：串联多个变换/OneOf 块
- P 参数控制变换发生概率（0~1）
- 官网有演示但不能用自定义图像测试
- 形态学操作（腐蚀/膨胀）当时未包含在 albumentations 中，需借助 OpenCV

## 关联

- [[OCR的有效数据增强]]（来源）
- [[概念_OCR数据增强]]
