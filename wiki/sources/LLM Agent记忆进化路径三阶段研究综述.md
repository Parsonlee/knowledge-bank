---
type: source
tags:
- AI-Agent/memory
summary: 港中深与上海 AI 实验室关于 LLM Agent 记忆机制综述，提出 Storage -> Reflection -> Experience 三阶段演进框架及前沿探索与跨轨迹抽象机制。
sources:
- raw/articles/LLM Agent 的记忆进化路径研究综述.md
updated: '2026-07-06'
published: '2026-05-11'
---
## 来源信息

- 原文：[LLM Agent 的记忆进化路径研究综述](https://mp.weixin.qq.com/s/3UrrMSXV6_t-lb6Kp7CPqA)
- 来源：[[实体_AI_Online]] / arXiv:2605.06716 / 2026-05-11
- 物理文献：`raw/articles/LLM Agent 的记忆进化路径研究综述.md`

## 核心要点与关键引文

### 1. 记忆机制研究的“派系撕裂”与桥梁构建
- **工程派 vs 认知派**：工程派仅关注数据库检索与存储怎么做（将记忆简化为 DB 问题），认知派过于纠结心理学与哲学概念而难以落地。
- **本综述定位**：用工程落地视角解决实际遗忘与上下文爆仓问题，同时借鉴认知科学框架保证系统完整性。

### 2. 记忆演进三阶段框架（Storage → Reflection → Experience）
- **Storage（存储阶段 - 轨迹保存）**：核心解决“如何存储 Agent 与环境的交互记录”。
- **Reflection（反思阶段 - 轨迹精炼）**：核心解决“如何从历史中提取与提炼有价值的信息”，避免记忆膨胀。
- **Experience（经验阶段 - 轨迹抽象）**：核心解决“如何形成可迁移、跨任务泛化的通用经验”。

### 3. 推动记忆演进的三大根本驱动力
- **长期一致性需求（Long-term Consistency）**：确保 Agent 在跨时间跨周期的多轮对话中保持目标连贯无遗忘。
- **动态环境适应（Dynamic Adaptation）**：在变化莫测的环境中持续做出有效决策。
- **持续学习目标（Continual Learning）**：从不断增长的经验中优化策略，且不触发[[概念_灾难性遗忘]]。

### 4. Experience 阶段的两大前沿方向
- **主动探索（Proactive Exploration）**：Agent 主动寻找并获取对完成任务有价值的信息，突破被动等待检索的局限。
- **跨轨迹抽象（Cross-trajectory Abstraction）**：从多条历史执行路径中归纳提炼通用行为模式与高阶规律，不依赖单一轨迹经验。

## 涉及主题与概念

- 核心理论：[[概念_Agent三段式记忆演进]]、跨轨迹抽象与主动探索
- 关联概念：[[概念_AI_Agent记忆策略]]、[[概念_Agent三层记忆体系]]、[[概念_灾难性遗忘]]
- 相关实体：[[实体_港中深与上海AI实验室]]

> 📎 **物理文献**：[[raw/articles/LLM Agent 的记忆进化路径研究综述.md]]