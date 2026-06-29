---
type: entity
tags:
  - LLM/reasoning
  - LLM/training/RL
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：Open R1

Open R1 是 HuggingFace 官方发起的 DeepSeek-R1 完全开源复刻项目，计划将全套训练 pipeline（数据/脚本等）开源。

## 三步骤复刻计划

1. 通过从 DeepSeek-R1 蒸馏高质量语料，复现 R1-Distill 模型
2. 复现 DeepSeek 用于创建 R1-Zero 的纯 RL 流程（需要新的大规模数学/推理/代码数据集）
3. 展示如何通过多阶段训练从基础模型发展到 RL 调优模型

## 关联

- [[实体_DeepSeek-R1]] — 被复现的原始模型
- [[DeepSeek-R1复现浪潮]]
