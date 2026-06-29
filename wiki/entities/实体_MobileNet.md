---
type: entity
tags:
  - CV
  - CV/detection
summary: MobileNet 系列，基于深度可分离卷积的轻量网络，面向移动端部署。V2 引入 Inverted Residual + Linear Bottleneck。
sources:
  - "wiki/sources/目标检测入门_特征复用与实时性.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 实体：MobileNet

## 简介

MobileNets 基于深度可分离卷积构建轻量网络，以较少参数达到有竞争力的精度，面向移动端部署。

## MobileNets V2

论文：arXiv:1801.04381（Inverted Residuals and Linear Bottlenecks）

- 相比 V1：重新定位 skip connection 位置；移除部分 ReLU 层
- 核心设计：Inverted Residual（先 1×1 扩展 → depthwise 3×3 → 1×1 压缩）+ Linear Bottleneck（压缩层不加 ReLU）

## SSDLite

- 将 SSD 检测头所有标准卷积替换为深度可分离卷积
- 首次报告移动端单核 CPU 推理速度，为移动部署建立实际性能参考

## 关联

- [[目标检测入门_特征复用与实时性]]（来源）
- [[概念_深度可分离卷积]]
- [[实体_SSD]]
