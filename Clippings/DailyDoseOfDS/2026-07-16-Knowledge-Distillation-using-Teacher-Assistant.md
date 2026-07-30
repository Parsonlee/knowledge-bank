---
title: "Knowledge Distillation using Teacher Assistant"
source: "https://mail.google.com/mail/u/0/#inbox/19f6ca0f2c928ca3"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-16
created: 2026-07-30
description: "介绍引入助教模型（Teacher Assistant）改进知识蒸馏（Knowledge Distillation）的方法。解决大教师模型与小学生模型尺寸差距过大导致的蒸馏失效问题。"
tags:
  - clippings
---

# 基于助教模型的知识蒸馏技术（Knowledge Distillation using Teacher Assistant）

知识蒸馏（Knowledge Distillation）常用于在训练后压缩大型机器学习模型。

其核心思想是训练一个更小、更简单的模型（称为“学生模型” Student），去模仿更大、更复杂的模型（称为“教师模型” Teacher）的行为：

![知识蒸馏基本示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcf833bc-f2b3-49f7-aba6-23ec2738bdd3_788x243.png)

今天，我们来讨论一种用于改进该技术的“助教模型”（Teacher Assistant, TAKD）方法。

---

### 一、 传统知识蒸馏存在的问题

理论上，学生模型应该在保持尽可能小的体积的同时，最大限度地保留教师模型的知识。

然而在实践中，人们观察到了两个现象：

![学生模型与教师模型尺寸匹配局限性](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe96be1a-0267-4cc2-a299-20b71982c24f_1456x736.png)

* **固定学生模型尺寸时**：它能有效学习的教师模型尺寸存在上限。在左图中，学生模型尺寸固定（2 层 CNN）。可以看到，随着教师模型尺寸的增加，学生模型的准确率呈现先上升后下降的趋势。
* **固定教师模型尺寸时**：知识只能转移到特定尺寸范围内的学生模型，无法无限变小。在右图中，教师模型尺寸固定（10 层 CNN）。随着学生模型尺寸进一步缩小，通过蒸馏获得的准确率增益（相较于无蒸馏直接训练的学生模型）呈现先增加后衰减的趋势。

两张图都表明：**传统的知识蒸馏只有在教师与学生模型的尺寸差距处于特定范围内时才能有效发挥作用。**

---

### 二、 解决方案：引入助教模型 (TAKD)

这一瓶颈可以通过在教师和学生之间引入一个中间模型——**助教模型（Teacher Assistant）**来解决：

![引入助教模型的两阶段蒸馏流程](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89c5900b-5f2b-44b9-8603-4e6a169f1666_1456x486.png)

* **步骤 1**：助教模型从教师模型中学习（Teacher -> Assistant）。
* **步骤 2**：学生模型从助教模型中学习（Assistant -> Student）。

当然，这增加了一个额外的训练步骤。

但是由于开发环境通常具备足够的灵活性，这种技术可以显著提升最终学生模型的性能与效率。此外，在生产环境中运行模型的开销会随着业务需求呈指数级增长，相比之下，训练阶段的成本依然非常低廉。

---

### 三、 实验结果与对比

助教方法的有效性在下图的对比中清晰可见：

![NOKD vs BLKD vs TAKD 性能对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F193f80f1-ceb6-4314-97e8-1ff360431a83_1456x607.png)

* **NOKD**：直接训练学生模型（No Knowledge Distillation）
* **BLKD**：从教师模型直接蒸馏给学生模型（Baseline Knowledge Distillation）
* **TAKD**：通过助教模型进行蒸馏（Teacher Assistant Knowledge Distillation）

在所有测试配置下，使用助教模型（TAKD）的表现均优于其他两种方法。

上述测试中的具体模型结构配置如下：

![蒸馏实验的具体模型结构配置](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25ce6383-6e73-4ade-89a1-daf3e6465559_1456x1007.png)

在这种方法中，助教模型的尺寸可以明显小于教师模型。如上图所示，助教模型的体积比教师模型小了 50% 以上。

从高层逻辑来看，该方法在代码层面实现大致如下：

![TAKD 代码实现逻辑](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ef9485b-cb33-4043-9bda-2a8b6ad90918_1456x937.png)

其中 `train_with_kd` 假设为一个用户定义的从教师模型蒸馏训练学生模型的函数。
