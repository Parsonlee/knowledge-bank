---
type: concept
tags:
  - CV/data-augmentation
summary: OCR 任务数据增强：形态学（腐蚀/膨胀模拟笔画粗细）、噪声（黑/白像素 drop）、变换（旋转/缩放/模糊），用 OneOf 随机组合避免过度叠加。
sources:
  - "wiki/sources/OCR的有效数据增强.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 概念：OCR 数据增强

## 定义

OCR 任务中，通过每次训练时对图像引入小变化来防止过拟合、提升泛化。与检测增强不同，OCR 增强聚焦文字可读性边界——既要引入足够差异，又不能让文本完全不可辨识。

## 要点

- **三类增强手段**：
  1. 形态学：膨胀（粗笔）/ 腐蚀（细笔），需控制迭代次数
  2. 噪声：黑色像素（RandomRain黑色/RandomShadow/PixelDropout）、白色像素（使文字解体）
  3. 变换：ShiftScaleRotate / Affine / Blur
- **组合策略**：用 Albumentations 的 `OneOf` 将同类变换分组，每组仅随机选一个执行；概率 P 控制发生机会
- **核心原则**：如果人都看不懂，模型也一样（但带词典/上下文的模型可能例外）
- 仅增强 3/4 的图像（1/4 保持原样）
- 前提假设：灰度图，已做对比度增强（如 CLAHE）

## 关联

- [[OCR的有效数据增强]]（来源）
- [[实体_Albumentations]]
- [[概念_数据增强_检测]]（检测任务的数据增强对比）
