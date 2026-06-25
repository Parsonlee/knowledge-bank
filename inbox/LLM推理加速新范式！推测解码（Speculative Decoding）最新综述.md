---
title: "LLM推理加速新范式！推测解码（Speculative Decoding）最新综述"
source: https://blog.csdn.net/qq_27590277/article/details/135812738
created: 2026-06-25
tags:
  - clipping
  - cubox
---

# LLM推理加速新范式！推测解码（Speculative Decoding）最新综述

> [!quote]
> 推测解码是一种“先推测后验证” (Draft-then-Verify) 的解码算法：在每个解码步，该算法首先高效地“推测”target LLM未来多个解码步的结果，然后用target LLM同时进行验证，以加速推理。
