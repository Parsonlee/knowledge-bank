---
type: source
tags:
- AIGC
summary: '**Nano Banana 定位**：Gemini 2.5 Flash Image 的别名，原生多模态快速高效模型，单步同时处理文字与图像'
sources:
- raw/关于 Nano Banana 的一些浅思.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
# 关于 Nano Banana 的一些浅思

## 来源信息

- **标题**：关于 Nano Banana 的一些浅思
- **作者**：lencx（浮之静）
- **发布时间**：2025-09-08
- **URL**：https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247490591&idx=1&sn=de04b231aa519679939fc7cf00181b58


lencx 围绕 [[实体_Nano_Banana_Pro]]（Gemini 2.5 Flash Image）的功能解析、提示词工程实践指南，以及关于人类与大模型协作的深度思考。

## Key Points

- **Nano Banana 定位**：Gemini 2.5 Flash Image 的别名，原生多模态快速高效模型，单步同时处理文字与图像
  - 原生多模态架构（图文统一处理）
  - 强角色一致性（跨图保持人物/产品稳定）
  - 原生世界知识（理解物体使用方式和环境关系）
  - 对话式编辑（自然语言多轮精确局部编辑）

- **能力清单**：文生图 / 图像编辑 / 多图合成与风格迁移 / 迭代细化 / 图中文字

- **提示词工程**（详见 [[概念_Nano_Banana图像生成提示词]]）
  - 核心原则：描述场景，不要只堆关键词
  - 思维模式：摄影师思维（景别/光线/镜头/氛围）、设计师思维（风格/线条/着色/背景）
  - 六大生成模板：写实摄影/风格插画贴纸/图中文字/产品商摄/留白极简/分镜连环画
  - 四大编辑模板：添加移除元素/局部修复 Inpainting/风格迁移/多图组合
  - 最佳实践：越具体越可控、角色一致性、交代用途意图、迭代微调、语义式负向提示、镜头语言控制
  - API：Python google-genai 客户端，替换 contents 字符串即可

- **人与大模型协作思考**（详见 [[概念_人与大模型协作]]）
  - 问题一：普通人如何让 AI 帮助创意——忘掉技术聚焦描述、四步构建策略（核心场景→细节→迭代→进阶）、正向为主负向为辅
  - 问题二：Gemini 关于协作的回答——从"答案提供者"到"思想催化剂"、拥抱认知谦逊（达克效应）、重新定义有价值工作（Knowing-What→Knowing-Why/How）
  - 人类独特价值：提出好问题/整合决策/共情连接/身体力行
  - GPT-5 点评 Gemini：从"相处手感"补充，按回车前给三颗钉子（要做的事/口味/底线）

- **AI 编程（Vibe Coding）三阶段**（详见 [[概念_Vibe_Coding三阶段]]）
  1. 初级：生成最小可行原型
  2. 中级：审阅重构老项目，清理技术债
  3. 高级：原型→模块化实现→全局审阅的"整体→细节→整体"循环
  - UI/UX 目前 AI 不太适合生成（千篇一律），更适合生成重复/有挑战性的逻辑代码

## Related Concepts

- [[概念_Nano_Banana图像生成提示词]]
- [[概念_人与大模型协作]]
- [[概念_Vibe_Coding三阶段]]

## Related Entities

- [[实体_Nano_Banana_Pro]]

## 来源

- 全文：`tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/关于 Nano Banana 的一些浅思.md`
- Cubox：`raw/关于 Nano Banana 的一些浅思.md`

---
> 📎 **物理文献**：[[raw/关于 Nano Banana 的一些浅思.md]]
