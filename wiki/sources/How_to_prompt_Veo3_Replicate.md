---
type: source
tags:
- AIGC
summary: '[[实体_Veo_3]]（Google）从文本提示词生成带音频的视频，音频可以是对话、画外音、音效和音乐。'
sources:
- raw/How to prompt Veo 3 for the best results....md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
cubox_url: https://cubox.pro/web/card/7350507002675594556
date_clipped: 2025-07-31
---
# How to prompt Veo 3 for the best results（Replicate）

## 来源信息

- **标题**：How to prompt Veo 3 for the best results – Replicate blog
- **作者**：Replicate（fofr / Shridar）
- **URL**：https://replicate.com/blog/using-and-prompting-veo-3


> Replicate 官方博客的 [[实体_Veo_3]] 提示词指南，与中文版「Google Veo 3 账号最新获取方式 + 提示技巧全攻略」互为来源（中文版引用并翻译了本文）。参见 [[Google_Veo3账号获取与提示技巧全攻略]]。

## 核心内容

[[实体_Veo_3]]（Google）从文本提示词生成带音频的视频，音频可以是对话、画外音、音效和音乐。

### Write what happens（提示词七要素）

一个写得好的提示词是生成好视频的关键，描述越具体、语言越朴素越好。应在提示词中包含以下视觉元素：

1. **Subject（主体）**：场景里有谁/有什么——人、动物、物件、风景。
2. **Context（环境）**：主体在哪里——室内、城市街道、森林？
3. **Action（动作）**：主体在做什么——走、跳、转头？
4. **Style（风格）**：视觉美学——cinematic、animated、stop-motion 等。
5. **Camera motion（镜头运动）**：aerial / eye-level / top-down / low-angle。
6. **Composition（构图）**：wide shot / close-up 等。
7. **Ambiance（氛围）**：情绪与光线，如 "warm tones"、"blue light"、"nighttime"。

文中给出基础 prompt（"A man answers a rotary phone"）vs 详细 prompt（带 dolly zoom、neon、shallow depth of field 等结构化元素）的对比。

### Change your prompt each time

与 Midjourney/Flux 不同：同一提示词换 seed，[[实体_Veo_3]] 会输出**非常相似**的结果（同一个人、同样衣服、同样地点）。

- 当结果有小毛病（连贯性/音频 glitch）时，换 seed 重跑很可能修复，这点很有用。
- 处于「探索模式」想看各种可能性时，重复跑同一提示词是浪费钱——应从几个大方向不同的提示词开始。

### Character consistency（角色一致性）

视频模型在无起始帧/场景元素时保持角色一致性很难。因为相似提示词产生相似角色，**在不同生成任务中原封不动地重复角色描述**就能得到长得一样的角色。描述越独特越具体，连贯性越好。示例：`John, a man in his 40s with short brown hair, wearing a blue jacket and glasses, looking thoughtful`。建议创建角色参考表，记下确切用词。

### Prompting audio（音频提示）

Veo 3 每次都生成音频，需要为以下元素写提示：对话、环境噪音、场景外音效（如电话铃声）、音乐。

- **对话两种写法**：明确（"A guy says: My name is Ben"）vs 隐晦（"A guy tells us his name"，模型自行决定）。
- **自己写对话**：保持简短，约 8 秒能说完；太长角色会语速飞快，太短会出现尴尬沉默或 AI 胡话（gibberish）。
- **让 Veo 3 写台词**：不擅长写对话时用隐晦提示，可把喜欢的输出转录后复用。
- **发音纠正**：把词用音标拼出来（如 "fofr" → "foh-fur"，"Shridar" → "Shreedar"）。
- **多人对话**：Veo 3 常搞混谁说什么（角色描述相似时尤甚），要在提示词中明确说话者（"The woman wearing pink says: ..."）。

### Avoiding subtitles（避免字幕）（[重点/高亮]）

Veo 3 训练了大量带内嵌字幕的视频，常输出拼写糟糕的错误字幕。避免方法：

- 把台词放在**冒号后面**（"A guy says: My name is Ben"），而不是用引号。
- 在提示词加 "(no subtitles)"——negatives 在 Veo 3 中很管用。
- 实在不行就多次重复 "No subtitles. No subtitles!"。

### 背景音频问题

不定义背景音频时 Veo 3 自行推断，常见幻觉是「live studio audience」（现场观众笑声）破坏画面。解法：明确提示期望听到的音频（如 "sounds of distant bands, noisy crowd, ambient background of a busy festival field"）。

### Styles（风格）

默认生成制作精良的真人实拍视频（demo/广告/MV 风）。要偏离需在提示词加风格，格式 `In the style of [style name]: ...`。文中给出 LEGO、Claymation、South Park、Pixar、8-bit retro、Graphic novel、Origami、Simpsons、Blueprint、Anime、Marble 等示例。加风格不仅改变画面，也改变角色动作和互动方式。

### Camera motion / Selfie / Vertical / Physics / Upscaling

- **镜头运动**：eye level / high angle / worms eye / dolly shot / zoom shot / pan shot / tracking shot。
- **自拍风格**：以 "A selfie video of..." 开头比描述「人拿相机」效果好得多；让手臂出现在画面里是真实感关键；自然眼神交流（偶尔看镜头）；加 "slightly grainy, looks very film-like" 摆脱过于干净的 AI 感。
- **竖屏**：Veo 3 当时不原生支持竖屏（仅 16:9），可用 Luma 的 Reframe Video outpaint 成竖屏（最长 30s，输出 720p）；原生竖屏即将到来。
- **物理**：Veo 3 擅长模拟真实物理（坠落/弹跳/流体），即使转换成不同艺术风格也保持运动轨迹。
- **画质提升**：默认 1280×720，推荐用 Topaz Lab's Video Upscaler 提升到 4K / 60fps。

### 结语

平庸视频与惊艳视频的区别在提示词——你不只是描述发生了什么，而是在**导演一个场景**，像电影制作人一样思考。

## 相关概念

- [[概念_Veo3视频提示词]]
- [[实体_Veo_3]]
