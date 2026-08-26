---
type: entity
tags:
- LLM/arch
- DeepLearning
summary: '- 全称：Large Language and Vision Assistant'
sources:
- wiki/sources/Discrete_Tokenization多模态综述.md
- wiki/sources/从LLaVA到Qwen3-VL_多模态架构演进.md
updated: '2026-07-06'
---

# 实体：LLaVA

## 基本信息

- **全称**：Large Language and Vision Assistant
- **机构**：Haotian Liu et al.（University of Wisconsin-Madison / Microsoft Research）
- **开源**：是

## 版本演进

| 版本 | 连接器 | 分辨率 | 特色 |
|------|--------|--------|------|
| LLaVA 1.0 | 单层线性投影 | 224×224 | 极简范式奠基 |
| LLaVA 1.5 | 两层 MLP | 336×336 | 数据驱动迭代 |
| LLaVA-1.5-HD | 两层 MLP + AnyRes | 高清 | 全局+局部双路 |
| LLaVA-OneVision | Higher AnyRes | 任意 | 图像+视频统一 |

## 核心哲学

"简洁即正确"（Simplicity is Correct）：极简架构 + 大规模指令微调数据 = 强大多模态能力

## 参见

- [[从LLaVA到Qwen3-VL_多模态架构演进]]
- [[概念_MLLM三位一体架构]]
- [[概念_AnyRes高分辨率处理]]
- [[实体_Qwen3-VL]]