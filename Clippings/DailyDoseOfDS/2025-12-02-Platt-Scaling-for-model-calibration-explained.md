---
title: "Platt Scaling for model calibration"
source: "https://mail.google.com/mail/u/0/#inbox/19ae0c67c504face"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-02
created: 2026-07-30
description: "图解模型概率校准技术 Platt Scaling，解决分类模型过度自信与概率不准问题。"
tags:
  - clippings
---

# 图解模型校准方法：Platt Scaling（Platt Scaling for model calibration）

Platt Scaling 是校准二分类模型预测概率最简单且最有效的技术之一。

![校准数据集示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5993c7cc-82d7-46d2-9ebe-75332f1ae4c5_2828x1623.png)

### 为什么需要模型校准？

假设公立医院希望对患者进行一项高昂的医疗检测。为了确保资金高效利用，医生需要模型输出一个可靠的预测概率来准确反映患者患病的可能性。

例如，如果模型对一组患者预测的患病概率均为 75%，那么在理想状态下，这 100 名患者中应当有大约 75 人实际患病。这就是**良好校准（Well-calibrated）**的模型，即预测置信度与真实准确率保持一致。

![CIFAR-100 上 LeNet 与 ResNet 校准度对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3ecbe22d-3d72-4b06-b41b-da55dfb6fc2e_1739x974.png)

然而研究表明，现代深度学习模型通常缺乏良好的概率校准。如上图在 CIFAR-100 数据集上的测试所示：
* **较早期的 LeNet 模型**：准确率约为 0.55，平均置信度约为 0.54（校准表现良好）。
* **较新的 ResNet 模型**：准确率提升至 0.7，但平均置信度高达 0.9（呈现明显的过度自信过度估值）。

### Platt Scaling 的基本工作原理

Platt Scaling 主要是通过在原模型的输出 Logits 上训练一个额外的逻辑回归（Logistic Regression）模型来校准概率。

![Platt Scaling 工作流程步骤 1-2](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fcecbaa-03a1-491b-8d35-03eea22f5e80_2980x900.png)

![Platt Scaling 工作流程步骤 3](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5d2bb77-4cad-4b9f-a9be-1f2e7caedd4d_2976x688.png)

![Platt Scaling 工作流程步骤 4](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf15ff09-aacb-440e-8382-bc2093670a2f_2976x716.png)

**具体实现步骤：**
1. 在训练集上训练主模型（如神经网络或 SVM），获得一个未校准的模型。
2. 将验证集（校准集）数据输入主模型，获取 Sigmoid 前的 Logits 输出。
3. 以该 Logits 作为输入特征，实际标签为目标，训练一个逻辑回归模型。
4. 推理阶段：新样本先经由主模型计算出 Logit，再将其输入训练好的逻辑回归模型，最终输出校准后的可靠概率。

![SVM 模型校准前后效果对比图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ef653dc-8058-4cee-a22b-fd6a62cc69c1_2980x580.png)

理想的校准线为 ^\circ$ 对角线。从 SVM 校准对比图中可以看出：原始 SVM（蓝线）呈现严重的非校准偏置，而经 Platt Scaling 校准后（绿线）概率质量得到了极大改善。

**注意事项**：Platt Scaling 对校准集的数据量较为敏感。当校准数据集规模较小时，可能会导致估计的拟合参数不够稳定。
