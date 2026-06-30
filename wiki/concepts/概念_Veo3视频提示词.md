---
title: Veo 3 视频提示词
tags:
  - AIGC
confidence: high
---

# 概念_Veo3视频提示词

> [[实体_Veo_3]] 的提示词方法论，来自 [[How_to_prompt_Veo3_Replicate]] 和 [[Google_Veo3账号获取与提示技巧全攻略]]。

## 定义

使用文本提示词引导 Google Veo 3 生成带音频的视频的技巧体系。核心原则是「像电影制作人一样思考」——不是描述发生了什么，而是在**导演一个场景**。

## 提示词七要素

| 要素 | 英文 | 说明 |
|------|------|------|
| 主体 | Subject | 场景里有谁/什么——人、动物、物件、风景 |
| 环境 | Context | 主体在哪里——室内、城市、森林 |
| 动作 | Action | 主体在做什么——走、跳、转头 |
| 风格 | Style | 视觉美学——cinematic、animated、stop-motion 等 |
| 镜头运动 | Camera motion | aerial / eye-level / top-down / low-angle / dolly / tracking |
| 构图 | Composition | wide shot / close-up 等 |
| 氛围 | Ambiance | 情绪与光线——"warm tones"、"nighttime" |

另需包含**音频要素**：对话、环境噪音、场景外音效、音乐。

## Veo 3 核心特性

- **同一提示词产出极相似**（与 Midjourney/Flux 不同）：探索时应大幅改变提示词；修小毛病时换 seed 即可。
- **角色一致性**：原封不动重复角色描述即可跨生成保持一致外貌，描述越独特越好。
- **避免字幕**：台词放冒号后（非引号）、加 "(no subtitles)"、多次重复。
- **发音纠正**：用音标拼出容易读错的词。
- **风格切换**：`In the style of [style name]: ...` 前缀即可切换 LEGO/Claymation/Pixar/Anime 等风格。

## 自拍视频技巧

- 以 "A selfie video of..." 开头
- 让手臂出现在画面里（真实感关键）
- 自然眼神交流（偶尔看镜头再转身）
- 加 "slightly grainy, looks very film-like" 去 AI 感

## 来源

- [[How_to_prompt_Veo3_Replicate]]
- [[Google_Veo3账号获取与提示技巧全攻略]]
