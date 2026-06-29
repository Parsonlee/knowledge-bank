---
type: entity
tags:
  - CV
  - CV/detection
summary: SENet（Squeeze-and-Excitation Network），通道注意力机制，ILSVRC 最后一届冠军。
sources:
  - "wiki/sources/目标检测入门_基础网络与分类定位权衡.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 实体：SENet

## 简介

SENet（Squeeze-and-Excitation Network, arXiv:1709.01507）提出通道注意力 SE Block，为 ILSVRC（ImageNet 大规模视觉识别挑战赛）最后一届冠军。

## SE Block

1. Squeeze：全局平均池化压缩空间维度
2. Excitation：FC 层生成通道权重
3. Reweight：权重回乘特征图

## 特性

- 插件式模块：可接入 ResNet、ResNeXt 等任意 backbone（如 SE-ResNet）
- MS COCO Challenge 2017 UCenter 团队使用 SE-ResNet 取得优异成绩

## 相关论文

- arXiv:1709.01507 — Squeeze and Excitation Network

## 关联

- [[目标检测入门_基础网络与分类定位权衡]]（来源）
- [[概念_通道注意力]]
- [[概念_Backbone设计范式]]
- [[实体_ResNet]]
