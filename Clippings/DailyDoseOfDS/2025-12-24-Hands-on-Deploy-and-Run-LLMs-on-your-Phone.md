---
title: "[Hands-on] Deploy and Run LLMs on your Phone!"
source: "https://mail.google.com/mail/u/0/#inbox/19b522575aa6f7ef"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-24
created: 2026-07-30
description: "实操演示使用 UnslothAI 微调 Qwen3，结合 TorchAO 量化导出为 .pte 格式，并在 iOS 设备上基于 ExecuTorch 100% 本地高效运行。"
tags:
  - clippings
---

# 实战：在手机上部署并运行大语言模型！（[Hands-on] Deploy and Run LLMs on your Phone!）

现在，你可以对 LLM 进行微调，并直接将其部署到手机上运行。

今天，我们将通过一份逐步实战指南，展示如何微调 Qwen3，并将其导出为适用于移动端的格式，从而在 iOS 或 Android 设备上实现 100% 本地离线运行。

我们将使用以下工具链：
* **UnslothAI**：用于高效微调
* **TorchAO**：用于手机友好的量化（Quantization）
* **ExecuTorch**：用于在 iOS/Android 设备上高效推理

让我们开始吧！

---

### 1️⃣ 加载模型（Load the model）

首先，我们在“手机部署模式”下加载 Qwen3-0.6B。

这会启用量化感知训练（Quantization-aware training），从而确保后续导出时与移动端完全兼容。

![加载 Qwen3 模型](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5bb89520-2d90-486a-b286-daee3d75f793_2604x1080.png)

---

### 2️⃣ 加载数据集（Load datasets）

接下来，决定模型需要学习什么。

我们加载：
* 推理数据集（Reasoning dataset）：增强逻辑推理能力
* 对话数据集（Chat dataset）：使其表现得像一个随手可用的助手

在此阶段，两个数据集都是原始状态。

![加载原始数据集](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F622e0ac2-1ba9-4a54-b790-a3f1d96c23d0_2384x1292.png)

---

### 3️⃣ 转换推理数据（Convert reasoning data）

现在我们将推理数据转换为 `User -> Assistant` 的对话格式。

这能教会模型如何一步步思考推理，而不仅仅是输出最终答案。

![转换推理数据格式](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54f49c9e-6d30-4c6c-871a-bc27aecd160d_3020x2168.png)

---

### 4️⃣ 标准化对话数据（Standardize chat data）

接着，将对话数据集同样标准化为统一的 Schema 格式。

这确保了两个数据集在模型视角下拥有完全一致的数据结构。

![标准化对话数据](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9782233d-43ae-4f15-aac4-5fe90db5792c_2628x1136.png)

---

### 5️⃣ 混合数据集（Mix datasets）

现在，决定模型进行深度推理与常规对话的比例。

我们保持 75% 的推理数据以赋予模型思考能力，25% 的对话数据以保持自然的交流语气。

这为我们提供了一个兼具两者优势的干净数据集。

![混合数据集比例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82a2b93e-9833-4c37-9829-c0da549a89df_2500x1888.png)

---

### 6️⃣ 训练模型（Train the model）

配置 Trainer 并开始微调。损失函数（Loss）持续下降，表明模型正在正确地学习与拟合。

![训练模型过程](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc8f0e9e-bf87-4266-886b-a6db44429b15_1200x892.png)

---

### 7️⃣ 保存模型（Save the model）

训练完成后，将模型保存为 TorchAO 格式。这正是 ExecuTorch 后续步骤所期待的格式。

![保存 TorchAO 格式模型](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4034417-075e-446a-8d09-6b9d3365a5f0_2459x1838.png)

---

### 8️⃣ 导出为 .pte 文件（Export to .pte）

现在导出可由 iOS 加载的单一 `.pte` 文件。包括：转换权重、读取模型配置以及导出最终文件。导出的 `.pte` 文件大小约为 470 MB，这完全符合端侧模型的预期。

![导出 .pte 移动端模型](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4717ec87-2be9-4b11-89bb-d31e59289f04_1200x678.png)

---

### 9️⃣ 在 iOS 上运行（Run on iOS）

最后，使用 ExecuTorch iOS Demo App 运行模型。在 Simulator 上复制 `.pte` 和 tokenizer，即可在 App 中加载并实时对话。在真实 iPhone 上运行速度可达 ~25 tokens/s，底座由 Meta 在 Instagram、WhatsApp 中使用的生产级 ExecuTorch 运行时驱动。
