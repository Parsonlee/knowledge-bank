---
type: source
tags:
  - LLM/arch/VLM
  - CV/arch
summary: "微软 Azure AI 提出 Florence-2，基于 Seq2Seq 架构和 FLD-5B 超大数据集，统一处理图像理解、检测、定位、分割等多种视觉任务"
sources:
  - "Cubox/微软 Azure AI 团队新作 - Florence-2- 解锁视觉新境界，万能感知引领未来！-2023-11-26.md"
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

## 来源信息

- **标题**：微软 Azure AI 团队新作 | Florence-2: 解锁视觉新境界，万能感知引领未来！
- **作者**：派派星 CVHub
- **URL**：https://mp.weixin.qq.com/s/On6XBPJ1uyc2YE-CipOPyg
- **发布平台**：微信公众号 CVHub

## 核心要点

- Florence-2 是微软 Azure AI 团队提出的通用视觉基础模型，采用 **Prompt 驱动的统一表示**，一套权重处理 CV 和 Visual-Language 全系列任务
- 核心架构为 **序列到序列（Seq2Seq）框架**：视觉编码器（DaViT）将图像转为视觉 token 嵌入，与提示文本嵌入拼接后送入 Transformer 编码器-解码器，以文本形式输出结果
- 区域表示通过扩展 tokenizer 词汇表实现（1000 个量化坐标 bin），支持矩形框、四边形框、多边形框三种形式，无需任务专用 head
- 多任务学习目标覆盖三个层次：图像级理解（分类/字幕/VQA）、区域/像素级识别（检测/分割/指代理解）、细粒度视觉-语义对齐（Grounding）
- 核心数据集 **FLD-5B** 包含 1.26 亿张图像、54 亿次全面标注（500M 文本注释 + 1.3B 文本区域注释 + 3.6B 文本短语区域注释），通过三阶段构建：特定模型初始标注 → 数据过滤增强 → 迭代细化
- 数据标注融合了 Grounding DINO 和 SAM 生成文本-短语-区域三元组
- 在 COCO 目标检测/实例分割（Mask-RCNN、DINO）及 ADE20K 语义分割（UperNet）上，FT 后分别提升 6.9、5.5、5.9 个点，训练效率比 ImageNet 预训练提高 4 倍
- 作者观点：网络架构差异不大，核心在于高质量数据集；选 Transformer 而非 CNN 是为了模态对齐更方便

## 关键引文

> 本文的另一个突出贡献便是开发了FLD-5B，包括对 1.26 亿张图像进行了 54 亿次全面的标注，当中采用了自动图像标注和模型优化的迭代策略 [重点/高亮]

> 该模型以图像和任务提示作为任务说明，并以文本形式生成最终结果 [重点/高亮]

> Florence-2 展示出卓越的零样本能力，覆盖广泛的视觉任务，包括字幕生成、目标检测、视觉定位和引用分割等 [重点/高亮]

## 关联

- [[概念_视觉基础模型统一范式]] — Florence-2 的 Seq2Seq 多任务统一框架
- [[概念_视觉Grounding]] — 图像区域与文本短语的细粒度对齐
- [[实体_Florence-2]] — 微软 Azure AI 通用视觉模型
- [[实体_FLD-5B数据集]] — Florence-2 配套超大规模标注数据集
- [[实体_DaViT]] — Florence-2 使用的视觉编码器
