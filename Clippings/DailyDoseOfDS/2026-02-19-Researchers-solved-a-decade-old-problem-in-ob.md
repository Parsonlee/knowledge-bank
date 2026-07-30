---
title: "Researchers solved a decade-old problem in object detection"
source: "https://mail.google.com/mail/u/0/#inbox/19c7821062a6ceb4"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-02-19
created: 2026-07-30
description: "解析 Ultralytics YOLO26 如何通过端到端双头架构彻底消除传统目标检测中非极大值抑制（NMS）后处理步骤，实现开箱即用高效率部署。"
tags:
  - clippings
---
# 研究人员解决了目标检测领域十年难题（Researchers solved a decade-old problem in object detection）

从表面上看，目标检测似乎很简单：给模型一张图片，它返回物体周围的边界框（Bounding Box）。

但其内部的推导过程却非常复杂。

在传统 YOLO 中，模型会为它找到的每个目标生成多个候选框。一辆汽车可能会得到 10 个候选框，一个人可能会得到 15 个。虽然在训练过程中保留多个预测有助于模型更好地学习特征模式，但推理阶段每个物体只需要一个最佳结果。

因此在模型预测完成后，需要依赖独立的**非极大值抑制（NMS，Non-Maximum Suppression）**步骤在神经网络外部筛选并剔除重叠的劣质框。

问题在于，这个清理步骤发生在神经网络之外，属于额外的后处理代码。

如果能彻底跳过后处理步骤会怎样？

这就是**端到端推理（End-to-End Inference）**做到的事情。

**Ultralytics YOLO26** 采用了这种全新设计，在单次前向传播中直接产生最终预测结果，无需任何单独的后处理清理步骤。

它采用了**双头架构（Dual-head Architecture）**，包含两种模式：
* **一对一头（One-to-one head）**：默认模式，直接输出干净的预测框；
* **一对多头（One-to-many head）**：保留传统模式，支持需要传统 NMS 后处理的特定应用场景。

默认模式在实践中意味着：
* 每张图像支持多达 300 个检测目标，每个物体仅输出一个框；
* 无需滤波或后处理步骤；
* 推理速度更快，部署流水线更简单；
* 在不同的硬件平台（如边缘设备、低功耗芯片）上具备一致的表现。

除了更快的推理速度外，端到端设计还彻底改变了模型的部署方式。由于模型的输出即最终结果，你不再需要在各个平台上移植 NMS 清理逻辑或为不同场景微调阈值，使集成变得前所未有的简单。

你可以在 Ultralytics 平台上体验 YOLO26：[Ultralytics YOLO26 Platform](https://platform.ultralytics.com/ultralytics/yolo26)。在 AGPL 许可下开源用于学术研究，商业用途提供企业授权。
