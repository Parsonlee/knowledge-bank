---
title: "Nano-Banana Pro 论文绘图教程"
source_url: ""
author: "Mark (Datawhale / 华南理工大学)"
date_published: ""
confidence: high
tags:
  - AIGC
  - LLM/arch
---

# Nano-Banana Pro 论文绘图教程

> 以「架构师→渲染器→编辑器」三步工作流，利用 Nano-Banana Pro（Gemini 2.5 Flash Image 模型）将论文内容转化为学术图表。

## Key Points

- **工具定位**：Nano-Banana Pro 即 Gemini 2.5 Flash Image 模型，以强指令遵循和图文生成能力见长，适合学术论文配图场景。

- **标准化三步工作流**
  - **Step 1 The Architect（架构师）**：使用高性能 LLM（Gemini 3 Pro / GPT-5 / Claude 4.5）将论文内容转换为 `[VISUAL SCHEMA]`，明确布局原型：
    - Linear Pipeline（线性流程）
    - Cyclic（循环）
    - Hierarchical（层级树形）
    - Parallel（并列对比）
    - Central Hub（中心辐射）
  - **Step 2 The Renderer（渲染器）**：将 VISUAL SCHEMA 输入 Nano-Banana Pro，利用其指令遵循能力将结构化描述渲染为像素图像；需严格约束文字标签数量与位置，避免文字错位。
  - **Step 3 The Editor（编辑器）**：通过自然语言指令对生成图进行迭代式精修（颜色、布局、细节）。

- **进阶技巧**
  - 参考图风格迁移：上传目标期刊或会议的已有图表作为风格参考。
  - 参数化色彩控制：在 prompt 中直接指定 HEX 颜色码，保持配色一致性。
  - 水印去除：通过 bookmarklet JS 脚本在浏览器端一键移除水印。
  - 后期处理：导出至 Adobe Illustrator 或 Figma 进行矢量化精修。

- **局限与禁忌**
  - 视觉合理性与科学严谨性存在冲突，生成图仅供示意，不能替代实验数据的准确呈现。
  - 文字标签容易出现位置错乱，需人工校对。
  - 过度艺术化风险：模型倾向于美化图形，可能失真概念结构。
  - **绝对禁止**将 AI 生成图用于实验数据图表（折线图、柱状图、散点图等），此类图表必须基于真实数据绘制。

## Related Concepts

- [[Gemini 2.5 Flash]]
- [[提示词工程]]
- [[学术论文写作]]
- [[AIGC 图像生成]]
- [[视觉信息设计]]

## Related Entities

- [[Datawhale]]
- [[华南理工大学]]
- [[Google Gemini]]
- [[Adobe Illustrator]]
- [[Figma]]
