---
title: "淘宝直播数字人 TTS 语音合成技术"
source_url: ""
author: "平江 / 泷予 / 沧亭（淘天集团直播 AIGC 团队）"
date_published: ""
confidence: high
tags:
  - TTS
  - LLM/arch
  - Infra/AI
---

# 淘宝直播数字人 TTS 语音合成技术

> 淘天集团直播 AIGC 团队详述数字人直播中 TTS 系统从数据管道到四代模型演进的完整技术路径。

## Key Points

- **TTS 在数字人直播中的定位**：连接 LLM 生成的播报文稿与口型驱动模块，是数字人直播链路的关键中间层，要求低延迟、高相似度、强表现力。

- **数据处理管道**
  - 音频规范化 → UVR_MDXNET 背景音分离 → Speaker Diarization（说话人分离）
  - VAD / 停顿截断 → DNSMOS 质量过滤
  - 文本标注：ASR（Seaco-Paraformer + Whisper-large-v3-turbo 交叉验证，领域词热词微调，迭代伪标签训练）→ 标点修复 → 韵律 / 拖音标注
  - 说话人聚类：基于 embedding 余弦相似度进行主播身份归类

- **模型四代演进**
  - **V1 两阶段架构**：语言模型（LM）+ 声学模型解耦；使用 Encodec / HuBERT 音频 tokenization；VALL-E 风格自回归生成。
  - **V2 发音准确性**：文本规范化规则 + LLM 联合纠错（准确率 94.7%）；G2P 多音字优化（错误率从 5.81% 降至 3.25%）；细粒度特征融合改善中英文混读。
  - **V3 韵律与情感**：引入显式停顿 / 拖音标签；参考音频情感注入；按主播建立个性化韵律表。
  - **V4 CosyVoice2 融合**：以 Qwen2.5-0.5B 为骨干 LM；训练数据扩展至 15 万小时；vLLM 推理加速，速度提升约 10 倍。

- **关键指标（V1 → V4）**

  | 指标 | V1 | V4 |
  |------|----|----|
  | CER（字符错误率） | 0.054 | 0.023 |
  | 说话人相似度 | 0.82 | 0.93 |
  | DNSMOS（音质） | 3.22 | 3.36 |

- **工程要点**
  - 热词微调解决电商垂直领域（品牌名、产品型号）ASR 误识别。
  - 伪标签迭代训练在无人工标注数据上持续提升 ASR 质量。
  - 参考音频情感注入使同一主播在不同播报场景（促销 vs. 讲解）呈现差异化情绪。
  - vLLM 推理加速是 V4 达到直播实时性要求的关键工程突破。

## Related Concepts

- [[TTS]]
- [[语音合成]]
- [[数字人]]
- [[CosyVoice]]
- [[VALL-E]]
- [[Speaker Diarization]]
- [[ASR]]
- [[vLLM]]
- [[韵律建模]]

## Related Entities

- [[淘天集团]]
- [[阿里巴巴]]
- [[Qwen2.5]]
- [[Whisper]]
- [[HuBERT]]
- [[Encodec]]
- [[Seaco-Paraformer]]
