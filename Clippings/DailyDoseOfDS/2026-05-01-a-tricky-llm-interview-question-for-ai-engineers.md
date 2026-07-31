---
title: "A tricky LLM interview question for AI Engineers."
source: "https://mail.google.com/mail/u/0/#inbox/19de58fc0d126e4b"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-01
created: 2026-07-30
description: "分析知识蒸馏（Knowledge Distillation）中能力错配现象：为什么使用更弱的 Teacher 模型微调 Student 模型反而效果更好？"
tags:
  - clippings
---

# AI 工程师的高难度 LLM 面试题（A tricky LLM interview question for AI Engineers.）

假设你正在微调一个模型用于 Python 代码生成，训练数据是用最强大的 LLM（如 Opus 或 GPT-4/5）生成的。

然而实验结果却表明：**当你改用一个更弱的 Teacher 模型生成合成数据时，微调后的模型表现反而更好。**

为什么会发生这种情况？

![模型蒸馏效果反常现象动图说明](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d13cd79-4c2b-4492-9d4d-52bf14293a85_1080x1080.gif)

强模型生成的蒸馏数据导致更差的微调效果，这听起来违背直觉，但在知识蒸馏（Knowledge Distillation）研究中是一个被充分验证的已知现象。

![强 Teacher 与弱 Student 之间的能力错配图示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a3cd94b-1755-462c-9656-28933bc450ea_851x372.png)

### 核心原因解析：

1. **能力错配（Capacity Mismatch）**：
   顶尖超大模型在解决简单问题时，习惯使用复杂的抽象设计、类型系统和高级设计模式。一个 8B 参数的小模型（如 Qwen3-8B）根本没有足够的参数容量去拟合这些复杂模式。小模型无法学到干净的解法，反而学会了对其无法完整表达的高维概念的劣质近似。

![弱 Teacher 给出符合小模型容量的简洁解法图示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34418abb-58f0-4dc0-ad55-a453d2da6963_610x259.png)

2. **表达复杂度与可复现性（Expression Complexity）**：
   相比之下，较弱的 Teacher 模型虽然能力上限较低，但在解决相同问题时会使用更直接、更简单的代码模式。这种模式正好落在 Student 模型的表征能力范围内，更容易被 Student 模型完美吸收和复现。

3. **智能体自动化微调实验验证**：
   在 Fastino Labs 提出的 Pioneer 自动微调 Agent 实验中，针对 Qwen3-8B 的代码生成微调测试同样证实了这一点：前沿大模型生成的数据反而降低了模型性能，而较小 Teacher 模型生成的数据在更少的迭代轮次内取得了大幅优胜。
