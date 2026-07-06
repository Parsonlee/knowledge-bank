---
type: entity
tags:
- CV
- CV/detection
summary: ResNet（Deep Residual Learning），通过残差学习与 skip connection 实现超深网络训练，替代 VGG 成为检测标准
  Backbone。
sources:
- raw/一文读懂向量数据库，原理到应用全解析！.md
- raw/信息过载时代，如何真正「懂」LLM？从MIT分享的50个面试题开始 ｜ 机器之心.md
- raw/目标检测入门（三）：基础网络演进、分类与定位的权衡 - 知乎.md
- raw/目标检测入门（二）：模型的评测与训练技巧 - 知乎.md
- raw/目标检测入门（四）：特征复用、实时性 - 知乎.md
- wiki/sources/LLM面试50题_MIT_CSAIL.md
- wiki/sources/PyTorch常用代码段合集.md
- wiki/sources/向量数据库原理与应用全解析.md
- wiki/sources/目标检测入门_基础网络与分类定位权衡.md
created: '2026-06-26'
updated: '2026-06-26'
confidence: high
---

# 实体：ResNet

## 简介

ResNet（Deep Residual Learning for Image Recognition, arXiv:1512.03385）由何恺明等人提出。

## 核心思想

- 将层学习重新定义为拟合残差 F(x)=H(x)-x，而非完整映射 H(x)
- 恒等捷径（identity shortcut）使梯度可直接回传至浅层，解决深层网络梯度消失/爆炸问题
- 类比 Boosting：每层拟合残差即为加法模型

## 检测领域意义

- 替代 VGG 成为标准特征提取 Backbone
- Faster R-CNN + ResNet 成为后续检测研究的标准基线
- 衍生：ResNeXt（引入 cardinality 维度）、SE-ResNet（加入通道注意力）

## 相关论文

- arXiv:1512.03385 — Deep Residual Learning for Image Recognition

## 关联

- [[目标检测入门_基础网络与分类定位权衡]]（来源）
- [[概念_Backbone设计范式]]
- [[实体_SENet]]