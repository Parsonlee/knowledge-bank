---
type: concept
tags:
  - LLM/arch/VLM
  - CV/arch
summary: "多模态大模型通用架构蓝图：视觉编码器（眼睛）+ 连接器（灵魂之桥）+ LLM（大脑）三部分协同工作"
created: "2026-06-29"
updated: "2026-06-29"
---

# 概念：MLLM 三位一体架构

多模态大模型（Multimodal Large Language Model, MLLM）的通用架构由三个核心部分组成，缺一不可。

## 三大组件

### 1. 视觉编码器（AI 的"眼睛"）
- 主流实现：**Vision Transformer (ViT)**，将输入图像/视频帧转换为高维特征向量（视觉 token）
- 常用预训练模型：CLIP ViT、DaViT 等
- 输入：像素矩阵（H×W×C）
- 输出：视觉 token 序列（N×D）

### 2. 连接器（"灵魂之桥"）
- 负责将视觉特征空间映射到语言模型可接受的表示空间
- 演进路径：
  - 单层线性投影（LLaVA 1.0）
  - 两层 MLP（LLaVA 1.5）
  - Q-Former（BLIP-2）
  - Resampler
- 核心矛盾：如何在不牺牲效率的前提下看得更"清晰"（处理高分辨率）

### 3. 大语言模型（AI 的"大脑"）
- 负责理解、推理和生成
- 接收连接器输出的视觉 token 与文本 token 拼接后的序列

## 两条演进路线

| 路线 | 代表模型 | 技术 | 哲学 |
|------|---------|------|------|
| 输入端工程 | LLaVA 系列 | AnyRes 分块 | 大道至简 |
| 内部架构改造 | Qwen3-VL | DeepStack 多层注入 | 精巧设计 |

## 参见

- [[概念_AnyRes高分辨率处理]]
- [[概念_DeepStack深度视觉融合]]
- [[从LLaVA到Qwen3-VL_多模态架构演进]]
- [[Florence-2_微软视觉基础模型]]
