---
type: entity
tags:
  - LLM/arch/attention
summary: "MiniMax 2025年发布的旗舰模型，回归 Full Attention 架构，定位 Agent/代码生成，定价为 Claude Sonnet 4.5 的 8%"
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：MiniMax M2

## 基本信息

- **机构**：MiniMax
- **发布时间**：2025年10月
- **定位**：Agent、代码生成
- **定价**：$0.3/百万 Token 输入（约 Claude Sonnet 4.5 的 8%）
- **推理速度**：TPS 约 100

## 架构决策：回归 Full Attention

M2 前身 M1 Lightning 采用 Softmax + MoE 混合架构，M2 选择**回归 Full Attention**。

### 放弃 Efficient Attention 的三个理由（Haohai Sun）

1. **工程链路复杂性爆炸**：需同时支持十几种场景，每增加一种 attention 机制工程复杂度指数增长
2. **评测体系局限**：小规模实验结论无法外推至大规模
3. **基建不完善**：Linear Attention 训练访存 bound，推理基础设施尚不成熟

### 策略

"时间换空间"：等待 GPU 进步解决成本问题，通过"高效的激活参数设计"平衡性能与成本

## 参见

- [[MiniMax_vs_Kimi_注意力路线之争]]
- [[实体_Kimi_Linear]]
- [[概念_线性注意力与混合注意力]]
