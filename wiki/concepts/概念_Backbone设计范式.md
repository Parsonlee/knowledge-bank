---
type: concept
tags:
  - CV
  - CV/detection
summary: 三种经典 CNN 设计范式（Repeat/Multi-path/Skip-connection）及其在检测 Backbone 中的应用。
sources:
  - "wiki/sources/目标检测入门_基础网络与分类定位权衡.md"
created: "2026-06-26"
updated: "2026-06-26"
confidence: high
---

# 概念：Backbone 设计范式

## 三种范式

1. **Repeat（重复）**：堆叠相同拓扑结构块。由 AlexNet 开创，VGG 发扬，几乎所有后续网络沿用。
2. **Multi-path（多路径）**：输入分为多并行路径分别变换后拼接。Inception 系列代表。允许单层内多尺度特征提取。
3. **Skip-connection（跳跃连接）**：浅深层直接通路。Highway Network 首提，ResNet 流行。恒等捷径稳定梯度传播。

## 另一趋势

深度可分离卷积（[[概念_深度可分离卷积]]）——非三大范式之一，但与之并行发展，贯穿 Xception、MobileNet 等。

## 代表性 Backbone 演进

| 网络 | 范式 | 核心创新 |
|------|------|----------|
| ResNet | Skip-connection | 残差学习 F(x)=H(x)-x |
| Xception | Repeat + Skip | 极端 Inception → 逐通道深度可分离卷积 |
| ResNeXt | Skip + Multi-path | 引入 cardinality 维度，所有并行路径拓扑一致 |
| SENet | 插件式 | 通道注意力 Squeeze-Excitation |
| NASNet | Repeat（自动搜索 Cell） | RL 搜索 Normal/Reduction Cell 堆叠 |

## 关联

- [[目标检测入门_基础网络与分类定位权衡]]（来源）
- [[概念_通道注意力]]
- [[实体_ResNet]]
- [[实体_SENet]]
