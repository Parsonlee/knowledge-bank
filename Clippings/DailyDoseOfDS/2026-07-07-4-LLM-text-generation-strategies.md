---
title: "4 LLM text generation strategies"
source: "https://mail.google.com/mail/u/0/#inbox/19f3d7ecdb9a83ee"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-07
created: 2026-07-30
description: "系统梳理大语言模型文本生成的四种主流解码策略：贪婪搜索（Greedy Search）、多项式采样（Multinomial Sampling）、束搜索（Beam Search）与对比搜索（Contrastive Search）。"
tags:
  - clippings
---

# 4 种大语言模型文本生成解码策略（4 LLM text generation strategies）

每次提示大语言模型（LLM）时，它并不能提前“知道”整句话，而是逐个 Token 地预测下一个词的概率。

但仅仅获得概率分布是不够的，我们还需要选择一种**解码策略（Decoding Strategy）**来决定在每一步具体选取哪个 Token。不同的策略会导致截然不同的文本生成风格。

![4 种主流文本生成策略对比总览](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92fa50e4-d4cd-4b35-b371-647cd97303f0_1790x1396.png)

---

### 一、 策略 1：贪婪搜索策略（Greedy Strategy）

**核心机制**：在每一步解码时，始终选择概率向量中得分最高（Top-1）的 Token。

* **优点**：计算速度极快，结果具有确定性（Deterministic）。
* **缺点**：极易陷入局部最优解，容易产生重复、单调的文本，缺乏多样性。

---

### 二、 策略 2：多项式采样策略（Multinomial Sampling Strategy）

**核心机制**：根据概率向量所提供的概率分布进行随机采样，而非永远只选最高分。

![多项式采样与温度系数控制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd4fa2d4-6175-4d98-8fd3-034efec31de4_1456x582.png)

在此策略中，**温度参数（Temperature）**用于平滑或重塑概率分布：
* 低 Temperature（如 0.2）：使分布更陡峭，偏向高概率 Token；
* 高 Temperature（如 0.8+）：使分布更平缓，增加输出的随机性与创意度。

---

### 三、 策略 3：束搜索（Beam Search）

贪婪搜索与多项式采样都只关注紧接着要生成的单步 Token。然而在理想情况下，我们追求的是**最大化整条生成的概率**，而非仅仅下一步。

![束搜索探索候选序列束](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc506c53e-e6d7-4195-9a8c-3cf376742642_1860x270.png)

![束搜索树状展开过程图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52fe0893-0918-4d23-8554-223f301e03ca_2942x577.png)

**束搜索（Beam Search）**尝试近似实现全局概率最大化：
1. 在每一步解码中，保留 Top-k 个候选序列（称为 Beam Size $k$）。
2. 部分序列在早期挑选的 Token 概率可能略低，但后续能产生概率更高的完整句子。
3. 通过维护多个候选分支，束搜索探索了更广阔的概率树空间。

* **适用场景**：广泛用于机器翻译、文本摘要等准确性优于创造性的任务。

---

### 四、 策略 4：对比搜索（Contrastive Search）

这是近年来提出的一种新颖方法，旨在平衡文本的**流畅度（Fluency）**与**多样性（Diversity）**。

![对比搜索防重复惩罚机制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F513e95ba-7ab6-4c06-ad8c-c63537e0917e_2942x585.png)

**核心机制**：
* 在每一步生成时，模型评估多个候选 Token。
* 测量候选 Token 与当前已生成文本之间的相似度，若相似度过高则施加**退化惩罚（Degeneracy Penalty）**。
* 选择在模型概率分与多样性得分之间达到最佳平衡的 Token。

* **优点**：有效防止大模型在长文本生成中陷入死循环复读机现象，在故事创作和长文写作中表现优异。
