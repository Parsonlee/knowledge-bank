---
type: entity
tags:
  - LLM/training/post-train
  - LLM/training/pre-train
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：SmolLM3

## 基本信息

- 类型：开源 LLM
- 来源：HuggingFace
- 参数量：3B（30亿）
- 训练规模：384 块 H100 GPU，11T tokens，约 4 周

## 关键架构选择

- 注意力机制：GQA（分组查询注意力）
- 位置编码：RNoPE 混合策略（交替 RoPE 层 + NoPE 层）
- 嵌入：输入/输出嵌入共享
- 稳定性：移除嵌入层权重衰减（OLMo2 技巧）
- Tokenizer：Llama3 词表（128k 词汇量）

## 训练特点

- 消融+调试 GPU 时间 > 主训练一半
- 多阶段数据混合：早期多样数据 + 退火阶段高质量数学/代码数据
- GPU 需求通过公式精确计算：总FLOPs ÷ 单GPU吞吐 ÷ 目标时长 ≈ 379，实际部署 384

## 关联

- [[HuggingFace手把手训练大模型实战指南]]
- [[实体_HuggingFace]]
- [[概念_多阶段训练策略]]
- [[概念_GQA分组查询注意力]]
