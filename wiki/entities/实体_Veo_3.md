---
title: Veo 3
tags:
  - AIGC
confidence: high
---

# 实体_Veo_3

> Google 的文本生成视频模型，来自 [[How_to_prompt_Veo3_Replicate]] 和 [[Google_Veo3账号获取与提示技巧全攻略]]。

## 简介

Google Veo 3 是从文本提示词生成**带音频**视频的模型，音频可以是对话、画外音、音效和音乐。生成的视频（水果 ASMR、第一人称大脚怪探险等）在社交平台很火。

## 关键特性

- **文本生成带音频视频**：对话/环境音/音效/音乐都可通过提示词控制。
- **同一提示词产出极相似**：与 Midjourney/Flux 不同，换 seed 结果非常一致（同一个人、同样衣服、同样地点）。
- **物理模拟出色**：保持坠落/弹跳/流体等真实运动轨迹，即使转成不同艺术风格。
- **不支持中文台词**：要让人物说普通话需用英语描述（`Says in Mandarin: "..."`）。
- **当时不原生支持竖屏**：仅 16:9，可用 Luma Reframe Video outpaint；Vertex-ai / AIStudio 中支持竖屏；原生竖屏即将到来。
- **默认画质 1280×720**：可用 Topaz Lab Video Upscaler 提升到 4K 60fps。

## 使用方式

- 需至少 Gemini Pro 账号（教育优惠可免费 15 个月）。
- **Gemini Pro**（gemini.google.com）：每天 3 次生成。
- **Flow 平台**（labs.google/fx/tools/flow/）：1000 积分/月，每视频 100 积分，含 Scene 线上剪辑（8 秒/段，extend/jump 拼接）。
- **Replicate**（replicate.com/google/veo-3）：API 调用。

## 相关

- [[概念_Veo3视频提示词]]
- [[实体_Gemini]]
