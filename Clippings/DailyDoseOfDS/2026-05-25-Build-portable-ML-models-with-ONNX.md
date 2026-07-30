---
title: "Build portable ML models with ONNX."
source: "https://mail.google.com/mail/u/0/#inbox/19e60c170373504b"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-25
created: 2026-07-30
description: "深入详解开放神经网络交换格式 ONNX 及其执行引擎 ONNX Runtime，涵盖算子标准化、图优化与跨平台部署的最佳工程实践。"
tags:
  - clippings
---

# 使用 ONNX 构建可移植的机器学习模型（Build portable ML models with ONNX.）

大多数机器学习团队都在 PyTorch 或 TensorFlow 中训练模型，但生产部署系统并不关心你使用的是什么训练框架。

生产环境关注的是**推理速度、跨平台便携性与运行时稳定性**。

训练与服务部署之间的这种脱节，正是大多数模型上线遭遇头疼问题的根源。

你可能在 PyTorch 中训练了一个模型，但推理栈可能是一个 C++ 服务、移动端设备、GPU 优化的运行时（如 TensorRT），甚至是浏览器端：

![训练框架与生产运行时的脱节](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F080ae02d-3684-433c-bea2-7531caabf3b2_1209x752.png)

如果没有统一的格式，每一次从框架到运行时的转换都会演变成定制工程问题，团队最终不得不反复重写模型逻辑。

这正是 **ONNX（Open Neural Network Exchange，开放神经网络交换格式）** 旨在解决的问题。下图展现了 ONNX 如何搭建这座桥梁：

![ONNX 搭建训练与部署之间的桥梁](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5730a6c-39fa-42a1-864f-bb3911694340_960x439.webp)

让我们来逐步拆解！

---

### ONNX 的本质是什么

ONNX 充当了介于模型训练与生产部署之间的**框架中立中间表示（Framework-agnostic Intermediate Representation, IR）**。

一个 ONNX 模型本质上是一个保存好的计算图（Computation Graph），包含标准化的算子（Operators）、显式的张量形状（Tensor shapes）、元数据（Metadata）以及节点连接关系。

可以把它想象成神经网络的“中立通用语言”。

PyTorch 和 TensorFlow 可以将模型导出为 ONNX，而生产运行时可以直接加载 ONNX 模型，从而使模型能够在不同硬件和语言间自由移植：

![ONNX 作为通用中间语言架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f721df6-fde8-4eb3-ae8b-04108da33fdc_1456x1103.png)

---

### 为什么算子标准化（Operator Standardization）至关重要

每一个深度学习框架对底层操作都有各自的内部表示。

ONNX 定义了一套通用的算子集（OpSet），以便导出器将框架特有的算子无缝映射到统一的词汇表中：

![算子标准化示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b88a17a-d049-4195-87f0-9275fa0b04a9_1024x572.png)

---

### ONNX Runtime (ORT) 的角色

ONNX 本身只是一种格式与模型表示。

而 **ONNX Runtime (ORT)** 则是将这种格式转化为高效高性能推理的**执行引擎**。

在底层，ORT 会加载 ONNX 计算图，应用图级别的高级优化（Graph-level optimizations，如算子融合 Operator Fusion），并将计算图自动切割分配到不同的硬件后端（CPU, CUDA, TensorRT, OpenVINO 等）：

![ONNX Runtime 的计算图优化与硬件后端分割](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0796145-8fac-4ac1-a125-63269307bbed_1456x708.png)

这一切在你加载并运行模型时都会自动发生。

---

### 预测示例

下图展示了使用 ONNX 和 ORT 进行简单 MNIST 数字预测时的输出验证：

![MNIST 推理验证示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9671f4de-4f26-4549-978d-a0042d5ca78b_1456x630.png)

需要强调的是，虽然 ONNX 大大简化了部署，但在上线前仍然需要进行严格的数值精度对齐验证。

记住以下的核心工作流：

![PyTorch 到 ONNX 到 ONNX Runtime 的流转过程](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d6ddd91-6692-4ab2-aa16-f25769d3f79d_1046x477.png)

这就是 ONNX 在你喜爱的训练框架与你所需的生产运行时之间搭建的高效桥梁。

👉 互动讨论：你最近在什么场景下使用了 ONNX？阻碍你进一步使用它的主要原因是什么？
