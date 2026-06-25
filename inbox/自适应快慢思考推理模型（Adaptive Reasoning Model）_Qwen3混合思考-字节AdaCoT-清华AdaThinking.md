---
title: "自适应快慢思考推理模型（Adaptive Reasoning Model）：Qwen3混合思考->字节AdaCoT->清华AdaThinking"
source: https://zhuanlan.zhihu.com/p/1910075005586346955
created: 2026-06-25
tags:
  - clipping
  - cubox
---

# 自适应快慢思考推理模型（Adaptive Reasoning Model）：Qwen3混合思考->字节AdaCoT->清华AdaThinking

> [!quote]
> Selective Loss Masking
> 模型在训练的过程中，如果处理不当，很可能会陷入到二元境地，比如一直都输出 CoT token 或者一直不输出 CoT token。比如在 【数学类】数据集中训练之后，很可能一直输出 CoT token。这样模型就不能很好的进行探索，坍缩到一个方向去了。
> 这里的做法也很简单，在 RL 训练的过程中，把 policy gradient 中的 loss 不算所有的 token，而是 mask 掉 <think> 后的第一个 token。这样做有什么好处，我们保持了 SFT/RL 阶段学到的要不要触发 CoT，只是我们 mask 掉了 Loss，通过 Loss 优化控制下一步是否触发 CoT，而不是改变上一步学到的结果。
