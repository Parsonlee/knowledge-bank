---
type: entity
tags:
  - LLM/arch/Mamba
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

# Tri Dao

FlashAttention 和 Mamba 系列的核心作者，硬件感知深度学习算法专家。

## 基本信息

- 斯坦福大学博士，导师 Christopher Ré
- 现任普林斯顿大学助理教授
- Together AI 首席科学家
- Cartesia AI 顾问

## 主要工作

- FlashAttention（2022）：IO 感知精确注意力算法
- FlashAttention-2（2023）：进一步优化
- Mamba（2023）：与 Albert Gu 合作，硬件感知算法设计
- Mamba2（2024）：SSD 框架系统优化部分

## 与 FlashAttention 的联系

Mamba 的硬件感知算法（kernel fusion、SRAM 优化）直接借鉴了 FlashAttention 的设计思路，两者均以减少 SRAM↔HBM 数据搬运为核心。

## 来源

- [[一文读懂Mamba_知乎]]
- [[实体_Mamba]]
- [[实体_FlashAttention]]
