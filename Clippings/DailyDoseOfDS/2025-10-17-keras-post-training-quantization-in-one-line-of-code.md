---
title: "Keras：一行代码完成训练后量化"
source: "https://mail.google.com/mail/u/0/#inbox/199f3a89f1a116c9"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-17
created: 2026-07-30
description: "Keras 在邮件中介绍了以 model.quantize(quantization_mode) 对自建或 KerasHub 预训练模型执行量化的接口，并列出 int4、int8、float8 与 GPTQ 模式。"
tags:
  - clippings
---

# Keras：一行代码完成训练后量化

邮件介绍，Keras 已提供训练后量化（post-training quantization）接口；对模型调用下面这一行即可指定量化模式：

```python
model.quantize(quantization_mode)
```

该接口既可用于自己训练的模型，也可用于从 KerasHub 获得的预训练模型。邮件列出的可选目标／模式为 `int4`、`int8`、`float8` 和 `GPTQ`。

更多说明见 [Keras 量化概览文档](https://keras.io/guides/quantization_overview/)。
