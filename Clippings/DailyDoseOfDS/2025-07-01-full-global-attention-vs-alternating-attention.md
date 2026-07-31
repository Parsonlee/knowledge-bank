---
title: "完全全局注意力与交替注意力（Full global attention vs alternating attention）"
source: "https://mail.google.com/mail/u/0/#inbox/197c7ace7fc9ab0e"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-07-01
created: 2026-07-30
description: "ModernBERT 通过结合完全全局注意力和滑动窗口局部注意力（交替注意力）来提高效率，使其能处理更长的上下文并提升速度。"
tags:
  - clippings
---

# 完全全局注意力与交替注意力（Full global attention vs alternating attention）

ModernBERT 是 BERT 的升级版，具有以下特点：

* 序列长度增加 16 倍。
* 更好的下游任务表现，无论是分类任务还是检索任务（如 RAG 系统中使用的）。
* 最具内存效率的编码器。

以下是与 ModernBERT 中注意力网络相关的一个有趣细节：

BERT 使用的是完全全局注意力（如上图左侧所示），其具有二次方复杂度。ModernBERT 通过交替注意力（alternating attention）提高了效率。

其核心思路如下：

* 他们在每三层中使用一次完全全局注意力。
* 所有其他层使用滑动窗口注意力，其中每个 token 只关注最近的 128 个 token（称为局部注意力）。

这使得 ModernBERT 能够处理长得多的输入序列，同时比其他编码器模型快得多。
以下是一个直观的解释（直接取自官方公告）：

从概念上讲，这种方法之所以奏效，原因很简单：想象一下你正在读一本书。对于你读的每一个句子，你是否需要完全了解整个情节才能理解其中的大部分内容（完全全局注意力）？还是说，只要你偶尔回想一下当前章节对主线情节的意义（全局注意力），仅仅了解当前章节就足够了（局部注意力）？在绝大多数情况下，答案是后者。
很有道理，不是吗？
