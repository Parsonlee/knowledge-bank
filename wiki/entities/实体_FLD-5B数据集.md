---
type: entity
tags:
  - LLM/arch/VLM
  - CV/arch
summary: "Florence-2 配套的超大规模视觉标注数据集，含 1.26 亿图像、54 亿次标注，覆盖文本/区域-文本对/文本-短语-区域三元组三种类型"
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：FLD-5B 数据集

## 基本信息

- **全称**：Florence Large-scale Dataset - 5 Billion annotations
- **来源**：微软 Azure AI（Florence-2 论文）
- **规模**：1.26 亿张图像，54 亿次标注

## 标注组成

| 类型 | 数量 | 构建方式 |
|------|------|---------|
| 文本注释 | 500M | 专家模型 + LLM + 迭代细化 |
| 文本区域注释 | 1.3B | OCR + 目标检测 |
| 文本-短语-区域三元组 | 3.6B | Grounding DINO + SAM |

## 图像来源

融合五个数据集：ImageNet-22k、Object 365、Open Images、Conceptual Captions、筛选后的 LAION

## 三阶段构建流程

1. **初始标注**：特定任务模型生成合成标签 + 已有标注合并
2. **数据过滤增强**：解析工具提取对象/属性/动作，NMS 去冗余框，过滤低质量标注
3. **迭代细化**：用过滤后数据训练多任务模型，模型预测更新标注，循环迭代

## 参见

- [[实体_Florence-2]]
- [[Florence-2_微软视觉基础模型]]
- [[概念_视觉基础模型统一范式]]
