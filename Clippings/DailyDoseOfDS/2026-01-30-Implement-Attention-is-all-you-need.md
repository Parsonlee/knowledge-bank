---
title: "Implement "Attention is all you need""
source: "https://mail.google.com/mail/u/0/#inbox/19c102bf0ed3e544"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-01-30
created: 2026-07-30
description: "从零开始用 Python 实现经典的 Transformer 架构，深入解析编码器-解码器结构、多头自注意力机制、位置编码、Teacher Forcing 训练与自回归生成。"
tags:
  - clippings
---
# 从零实现《Attention Is All You Need》论文架构（Implement "Attention is all you need"）

这篇论文彻底改变了人工智能领域！

![Transformer 论文背景与介绍](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4e5c7ab-2fa0-4927-81db-606a2e7bbd07_680x470.png)

今天我们将一步步构建完整的 Transformer 模型：

![Transformer 完整架构全景图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63d5a19d-4aaf-4644-b840-6f936f83f3d3_680x409.png)

关键核心组件包含：
* 编码器与解码器堆叠（Encoder & Decoder stacks）
* 多头注意力层（Multi-head attention layers）
* 逐位置前馈网络（Position-wise feed-forward networks）
* 位置编码（Positional encoding）

接下来让我们逐一拆解！

## 1️⃣ 核心两大组件：Encoder 与 Decoder

![Encoder 与 Decoder 大图展示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F139a27f1-6933-485f-82d9-d155e2061849_680x441.png)

* **Encoder**：处理输入序列（如英文句子）；
* **Decoder**：生成目标输出序列（如西班牙语翻译）。

架构中各包含 6 个相同的块堆叠而成。

## 2️⃣ 编码器层：自注意力 + FFN

每个编码器层有两个子层：

![Encoder 层结构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce7db420-2efa-4308-9f4e-115458aad59e_680x441.png)

* 多头自注意力（关注输入序列整体上下文）；
* 逐位置前馈网络（Position-wise Feed-Forward Network）。

每个子层外侧均包含残差连接与层归一化（Layer Normalization）。

## 3️⃣ 解码器层结构

解码器层包含三个子层：

![Decoder 层结构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92659555-38e6-468a-a314-027d9c13b793_680x441.png)

* 掩码自注意力（Masked self-attention，遮挡未来 Token）；
* 编码器-解码器交叉注意力（Encoder-Decoder cross-attention）；
* 逐位置前馈网络。

生成过程在此发生！

## 4️⃣ 多头注意力机制（Multi-Head Attention）

![多头注意力机制结构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8a032fb-f5d5-4279-94c4-4cba0cbf33bc_680x394.png)

更多的注意力头意味着更多的参数与更强的模式学习灵活性：

![不同 Attention Head 捕获的不同语义特征关系](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1bc1a3e-1d46-4597-8735-e8513146d248_680x441.png)

* Head 1：学习主谓关系；
* Head 2：学习形容词与名词修饰关系；
* Head 3：学习长距离依赖……最后将所有头的输出拼接。

## 5️⃣ 核心算法：自注意力（Self-attention）

这是整个架构的灵魂！

![Self-Attention 公式推导与计算过程图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3489744b-e209-41a7-9510-b9764b216e36_680x441.png)

著名的计算公式：
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

* **Q (Query)**：“我在寻找什么信息？”
* **K (Key)**：“可提供哪些信息？”
* **V (Value)**：“实际返回的信息内容是什么？”

## 6️⃣ 前馈网络：思考层（FFN）

注意力计算完成后，每个位置将被独立处理：

![FFN 网络逻辑图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb63cd858-550d-4609-a61e-d79b182be500_680x408.png)

$$\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2$$

即：线性变换 $\rightarrow$ ReLU 激活 $\rightarrow$ 线性变换。

## 7️⃣ 位置编码（Positional Encoding）

由于注意力机制本身没有位置顺序感，我们需要显式注入位置信息：

![位置编码函数变化关系图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba71d4dd-6238-4cdd-b094-d52d51f3c27b_680x441.png)

通过不同频率的正弦和余弦函数生成唯一的位置模式。

## 8️⃣ 训练机制（Training）

在训练阶段：

![Transformer 训练过程图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a6a4c16-9e60-4cf5-94fe-96fe7cb0d511_680x448.png)

编码器编码源语言句子，解码器获得右移（Shift Right）后的目标语句进行 Teacher Forcing：

![Right-Shift 机制与 Masking](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c7ecc54-6b12-4063-8e97-1fb40bba9dea_680x408.png)

![Cross-entropy 损失对比与梯度反传](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c14ec22-8aa2-4813-bd47-fb8c1e071b80_680x408.png)

右移能够让解码器利用历史正解 Token 进行下一 Token 的并行训练预测。

## 9️⃣ 推理过程：自回归生成（Autoregressive Generation）

在推理测试阶段，生成是按步进行的自回归过程：

![自回归推理预测图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f2225e9-8fdc-4643-9d82-127a61dea7d7_680x599.png)

编码器只运行一次，解码器运行多次：
* Step 1: $\rightarrow$ "Hola"
* Step 2: , Hola $\rightarrow$ "mi"
* 依次推进，每一步结合之前的预测结果！
