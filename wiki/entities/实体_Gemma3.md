---
type: entity
tags:
  - LLM/arch
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体_Gemma3

Google DeepMind 发布的 Gemma 3 系列开源 LLM，以滑动窗口注意力和双层 Norm 为主要架构特点。

## 基本信息

- **机构**：Google DeepMind
- **版本**：Gemma 3（1B/4B/12B/27B）+ Gemma 3n（移动端优化）
- **论文**：https://arxiv.org/abs/2503.19786

## 架构特点

- **滑动窗口注意力**：全局:局部 = 1:5，局部窗口大小 1024（相比 Gemma 2 的 4096 缩小）
- **Pre+Post Norm 双层 RMSNorm**：Attention/FFN 模块前后各一层，结合了两种 Norm 策略优点
- **GQA（分组查询注意力）**

## Gemma 3n（移动端）
- **Per-Layer Embedding（PLE）**：特定 Token 层嵌入从 CPU/SSD 按需流式传输
- **MatFormer**：单一大模型可切片为更小独立可用子模型

## 评价

- 在开源社区有些被低估，实际性能（尤其 27B）非常出色
- 27B 在能力和计算成本之间达到理想平衡点

## 相关文件

- [[从DeepSeek-V3到Kimi_K2_八种现代LLM架构大比较]]
- [[2025年七大顶流大模型架构]]
- [[概念_滑动窗口注意力]]
