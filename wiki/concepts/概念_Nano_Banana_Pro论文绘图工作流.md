---
title: "概念_Nano_Banana_Pro论文绘图工作流"
tags: [AIGC]
confidence: high
---

# Nano Banana Pro 论文绘图工作流

以「架构师→渲染器→编辑器」三步标准化工作流，将复杂学术绘图任务拆解为逻辑构建与视觉渲染两阶段。

## 核心流程

1. **Step 1 The Architect（逻辑构建）**：用高性能 LLM 将论文内容转为 [VISUAL SCHEMA]
   - 布局原型选择（5种）：Linear Pipeline / Cyclic-Iterative / Hierarchical Stack / Parallel-Dual-Stream / Central Hub
   - Schema 规则：Dynamic Zoning（2-5区域）/ Internal Visualization（禁止抽象概念，必须具象化）/ Explicit Connections

2. **Step 2 The Renderer（视觉渲染）**：将 SCHEMA 输入 [[实体_Nano_Banana_Pro]] 渲染为像素
   - 约束：不渲染元标签（ZONE/LAYOUT等），只渲染 Key Text Labels 双引号内容
   - 抽卡对整体布局风格改动不大，但细节线条/颜色可能变化

3. **Step 3 The Editor（交互式微调）**：自然语言编辑迭代
   - 布局满意细节瑕疵 → 自然语言指令精修
   - 布局错误 → 回 Step 1 修改 SCHEMA

## 进阶技巧

- 人工介入微调 SCHEMA 文本比抽卡更快
- 参考图风格迁移：从"文生图"切换为"图生图"
- 参数化控色：HEX 代码精确指定
- AI 生成视为 90% 完成品，后期 Illustrator/Figma 精修

## 局限

- 视觉合理性与科学真实性冲突
- 文本标注逻辑错位
- 绝对禁止用于实验数据图表

## 来源

- [[Nano-Banana_Pro论文绘图教程]]
