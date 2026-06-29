---
type: concept
tags:
  - CV
summary: SAM 开创的以多种 Prompt（点/框/掩码/文本）驱动图像分割的范式。
sources:
  - "wiki/sources/SAM_Segment_Anything模型.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 概念：Prompt 驱动分割

## 定义

由 SAM 提出的交互范式：用户通过多种 Prompt 类型指定分割目标，模型据此生成分割 mask。

## Prompt 类型

| 类型 | 编码方式 |
|------|----------|
| 点（Point） | 位置编码 + 学习嵌入（前景/背景区分） |
| 框（Box） | 角点对编码为两个 Point |
| 掩码（Mask） | 卷积编码为 4×64×64 |
| 文本（Text） | 通过 CLIP 文本编码器生成嵌入 |

## 歧义处理

对模糊 Prompt（如单点），模型输出 3 个候选 mask 并附置信度分数，由用户选择。

## 自动模式

无 Prompt 时用 32×32 点网格覆盖图像，每点生成 mask，NMS 去重实现 Segment Everything。

## 关联

- [[SAM_Segment_Anything模型]]（来源）
- [[实体_SAM]]
- [[实体_CLIP]]
- [[概念_图像分割]]
