---
type: concept
tags:
  - CV/data-augmentation
summary: torchvision.transforms 提供的图像增强 API，包括 Resize、Grayscale、Normalize、RandomRotation、CenterCrop、RandomCrop、GaussianBlur、ColorJitter、RandomHorizontalFlip、RandomVerticalFlip 等内置操作。
sources:
  - "wiki/sources/PyTorch图像增强方法总结.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 概念：torchvision 图像增强

## 定义

`torchvision.transforms` 是 PyTorch 官方视觉库提供的图像变换模块，通过链式组合各种变换操作实现数据增强。

## 内置操作清单（全文介绍）

| 方法 | 用途 |
|------|------|
| `T.Resize(size)` | 调整图像大小 |
| `T.Grayscale()` | RGB → 灰度 |
| `T.Normalize(mean, std)` | 每通道减均值除标准差，加速学习 |
| `T.RandomRotation(degrees)` | 按角度随机旋转 |
| `T.CenterCrop(size)` | 裁剪图像中心 |
| `T.RandomCrop(size)` | 随机裁剪 |
| `T.GaussianBlur(kernel_size, sigma)` | 高斯模糊 |
| `T.ColorJitter(brightness, contrast, saturation)` | 亮度/对比度/饱和度调节 |
| `T.RandomHorizontalFlip(p)` | 水平翻转 |
| `T.RandomVerticalFlip(p)` | 垂直翻转 |
| `T.ToTensor()` / `T.ToPILImage()` | Tensor ↔ PIL 转换 |

## 自定义增强（全文实现）

- 高斯噪声：`inputs + randn_like(inputs) * noise_factor`，再 clip 到 [0,1]
- 随机块（Random Boxes）：在随机位置插入正方形黑色补丁（像素置 0）
- 中心区域：在图像中心插入黑色补丁

## 关联

- [[PyTorch图像增强方法总结]]（来源）
- [[概念_OCR数据增强]]（另一增强思路，使用 albumentations）
