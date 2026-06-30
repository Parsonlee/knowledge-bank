---
title: "Nano-Banana Pro 论文绘图最全教程发布"
source_url: "https://mp.weixin.qq.com/s/IG8cITKAESi-vomyQiobZg"
author: "Mark（华南理工大学）/ Datawhale"
date_published: "2025-12-09"
tags: [AIGC]
confidence: high
---

# Nano-Banana Pro 论文绘图教程

以「架构师→渲染器→编辑器」三步标准化工作流，利用 LLM 逻辑推理能力指导 [[实体_Nano_Banana_Pro]]（Gemini 2.5 Flash Image）的像素生成，产出 CVPR/NeurIPS 顶刊标准学术插图。

## Key Points

- **核心理念**：将复杂绘图任务拆解为"逻辑构建（The Architect）"与"视觉渲染（The Renderer）"两个独立互补环节

- **三步工作流**（详见 [[概念_Nano_Banana_Pro论文绘图工作流]]）
  - **Step 1 The Architect（逻辑构建）**：用高性能 LLM（Gemini 3 Pro / GPT-5 / Claude 4.5）将论文内容转为 [VISUAL SCHEMA]，核心是将抽象算法逻辑转化为"强硬物理描述"
    - 布局原型五选一：Linear Pipeline / Cyclic-Iterative / Hierarchical Stack / Parallel-Dual-Stream / Central Hub
    - Schema 规则：Dynamic Zoning（2-5 区域）/ Internal Visualization（禁止抽象概念）/ Explicit Connections
  - **Step 2 The Renderer（视觉渲染）**：将 SCHEMA 输入 Nano-Banana Pro 渲染；关键约束——不渲染元标签（ZONE 1 等），只渲染 Key Text Labels 双引号内容
  - **Step 3 The Editor（交互式微调）**：
    - 情况A 布局满意细节瑕疵 → 自然语言编辑（改图标/调颜色/风格统一/文字修正）
    - 情况B 布局错误 → 回到 Step 1 修改 SCHEMA

- **进阶技巧**
  - 人工介入微调：直接修改 VISUAL SCHEMA 文本比反复"抽卡"更快
  - 提供参考图像：建立"科研审美库"风格迁移，从"文生图"切换为"图生图"逻辑
  - 参数化控色：用 HEX 代码精确指定颜色，避免"塑料感"
  - 去水印：Bookmarklet 脚本阻止 Gemini Logo 水印加载
  - 后期处理：AI 生成视为 90% 完成品，用 Photoshop/Illustrator 矢量化精修

- **局限与禁忌**
  - "视觉合理性" vs "科学真实性"冲突：模型可能为构图美观牺牲科学正确性
  - 文本标注"张冠李戴"：信息量大时偶尔逻辑错位，需逐一人工排查
  - 过度艺术化：渐变/阴影/非标准配色不符学术规范
  - **绝对禁止**：用 AI 绘制/修改实验数据相关统计图表（散点图/柱状图/折线图），涉嫌数据造假
  - 禁止 AI 绘图的期刊：将 AI 图作为"草图"底层临摹范本，手动重绘

## Related Concepts

- [[概念_Nano_Banana_Pro论文绘图工作流]]
- [[概念_PPT生成提示词]]

## Related Entities

- [[实体_Nano_Banana_Pro]]

## 来源

- 全文：`tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/Nano-Banana Pro 论文绘图最全教程发布.md`
- Cubox：`Cubox/Nano-Banana Pro 论文绘图最全教程发布-2025-12-09.md`
