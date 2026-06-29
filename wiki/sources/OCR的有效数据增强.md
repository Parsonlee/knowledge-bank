---
type: source
tags:
  - CV/data-augmentation
summary: 针对 OCR（手写金额识别）的数据增强实战：用 OpenCV + albumentations 实现三类增强——形态学（腐蚀/膨胀模拟细/粗笔画）、噪声（RandomRain/RandomShadow/PixelDropout）、变换（ShiftScaleRotate/Affine/Blur），并用 OneOf 随机组合；附完整 augment_img 代码。
sources:
  - "Cubox/OCR的有效数据增强-2024-10-08.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# OCR 的有效数据增强

## 来源信息

- 标题：OCR的有效数据增强
- URL：https://mp.weixin.qq.com/s/y7wsvmodtm7R9bPuVpvuaA
- 配套 Notebook：https://github.com/Toon-nooT/notebooks/blob/main/OCR_data_augmentations.ipynb
- 基于全文 ingest

## 核心要点

1. **背景**：手写金额识别任务，需保持误判率 < 0.01%；样本数固定，故采用数据增强。配合 TROCR 使用，每次训练引入小变化以防过拟合、提升泛化。假设图像为灰度且已做对比度增强（如 CLAHE）。

2. **[重点/高亮] 工具库**：OpenCV（成熟 CV 库）+ Albumentations（相对较新的 Python 图像增强库，简单但强大）。

3. **[重点/高亮] 形态学修改（OpenCV 实现，albumentations 暂不含）**：
   - 膨胀（dilate）：模拟粗笔画
   - 腐蚀（erode）：模拟细笔画
   - 注意迭代次数不可过高（示例 3），否则手写笔迹被完全去除；该数据集只能设为 1

4. **[重点/高亮] 引入噪声**：可删除黑色像素或添加白色像素。
   - 黑色 drop color 的 RandomRain：非常有害（文本难辨），故发生概率设很低
   - RandomShadow：用不同强度的线模糊文本
   - PixelDropout：随机像素变黑
   - 白色 drop color 的 RandomRain：使文字解体，模拟传真复印的低质量，概率可设高
   - 白色 PixelDropout：程度较小，更多导致图像普遍褪色

5. **变换（Transformation）**：
   - ShiftScaleRotate：同时缩放和旋转，参数需谨慎避免文本被切出边界；可通过更大边界框（文本周围留白）防止
   - Blur 模糊：以不同强度执行

6. **组合（大结局）**：用 albumentations 的 `OneOf`（以概率 P 仅执行其中一个变换）将相似变换分组，避免过度叠加同类方法。仅增强 3/4 的图像。完整代码见全文 `augment_img` 函数。

7. **另一种方法 TACo**（来自 EASTER 2.0 论文）：Tile and Corrupt（平铺与破坏）。作者未尝试，直觉认为原图被破坏过度——若人看不懂，计算机也看不懂；但带词典的模型可能据上下文猜测（如 'TA█O' → 'TACO'）。

## 关联概念

- [[概念_OCR数据增强]]
- [[概念_数据增强_检测]]

## 关联实体

- [[实体_Albumentations]]
