---
title: "实体_CosyVoice"
tags: [TTS]
confidence: high
---

# CosyVoice

开源 TTS 模型，由阿里通义语音团队开发，[[实体_淘天AIGC团队]] 在数字人直播 TTS 系统 V4 中融合使用。

## 版本信息

- CosyVoice 2.0：基于 Qwen2.5-0.5B 为骨干 LM，参数量相比 V3 提升一倍，设计了更强的 tokenizer
- 码本更大，表征能力更强

## 淘宝直播 V4 融合方案

- 继承 CosyVoice2 Qwen2.5-0.5B 骨干 LM 参数
- 结合自研细粒度特征融合方案，解决多音字/生僻字发音不准问题
- 训练数据：15W 小时高质量中英文 TTS 数据
- 引入 vLLM 框架加速推理：实测 LLM 并发速度比线上快约 10 倍
- 相似度 0.8505（V3）→ 0.9284（V4），DNSMOS 3.2517 → 3.3626

## 来源

- [[淘宝直播数字人_TTS语音合成技术]]
