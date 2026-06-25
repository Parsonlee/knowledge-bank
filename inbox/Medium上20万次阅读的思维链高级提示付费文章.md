---
title: "Medium上20万次阅读的思维链高级提示付费文章"
source: https://mp.weixin.qq.com/s/11QEniDzmFRS_jO5u1snmA
created: 2026-06-25
tags:
  - clipping
  - cubox
---

# Medium上20万次阅读的思维链高级提示付费文章

> [!quote]
> 将高 temperature 与高 top_p 结合使用会生成更多创新和创意的输出，因为更多 token 会成为候选项。

> [!quote]
> 系统首先启动 k 个初始的 top token，然后从每个 token 生成不同的推理路径。一旦答案生成后，系统会根据不同路径中各个 token 的概率（logits）计算置信度得分。
> 最终，模型返回具有最高概率的答案或路径。
> 这种方法被称为“解码CoT”（Decoding CoT），也是由 DeepMind 提出的，其核心思想是观察模型在返回答案时的内部置信度。
