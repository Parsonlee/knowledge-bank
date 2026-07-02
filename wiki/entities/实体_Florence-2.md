---
type: entity
tags:
  - LLM/Multimodal
  - CV/arch
summary: "微软 Azure AI 团队提出的通用视觉基础模型，基于 FLD-5B 数据集和 Seq2Seq 框架，统一处理图像理解/检测/定位/分割等任务"
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：Florence-2

## 基本信息

- **机构**：微软 Azure AI
- **类型**：视觉基础模型
- **论文**：Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks
- **时间**：2023年11月

## 核心架构

- **视觉编码器**：DaViT
- **框架**：标准编码器-解码器 Transformer（Seq2Seq）
- **输入**：图像 + 任务 Prompt 文本
- **输出**：文本（含量化坐标 token）

## 关键设计

- Tokenizer 词汇表扩展 1000 个坐标 bin，支持矩形/四边形/多边形区域表示
- 无需任务专用 head，统一语言建模目标（交叉熵）

## 训练数据

- **FLD-5B**：1.26 亿图像，54 亿次标注
- 三阶段构建：特定模型初标注 → 过滤增强 → 迭代细化
- 融合 Grounding DINO + SAM 生成文本-短语-区域三元组

## 性能

- 零样本能力覆盖：字幕生成、目标检测、视觉定位、引用分割
- FT 后 COCO 检测/分割分别提升 6.9、5.5 点；ADE20K 分割提升 5.9 点
- 训练效率比 ImageNet 预训练提高 4 倍

## 参见

- [[Florence-2_微软视觉基础模型]]
- [[实体_FLD-5B数据集]]
- [[概念_视觉基础模型统一范式]]
- [[概念_MLLM三位一体架构]]
