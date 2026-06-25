---
id: "7339186180103078460"
cubox_url: https://cubox.pro/web/card/7339186180103078460
url: https://zhuanlan.zhihu.com/p/1910075005586346955
tags:
  - CoT
  - Reasoning
  - Test-TimeCompute

---
# 自适应快慢思考推理模型（Adaptive Reasoning Model）：Qwen3混合思考->字节AdaCoT->清华AdaThinking - 知乎

1. 背景OpenAI O 系列发布之后，Inference Time Scaling 的模型一直备受关注，这种具有长思考能力的模型倍称为：Large Reasoning Model（LRM）。所谓的长思考能力指得是 Long Chain-of-Thought（LongCoT），和大家…

[Read in Cubox](https://cubox.pro/web/card/7339186180103078460)  
[Read Original](https://zhuanlan.zhihu.com/p/1910075005586346955)  

---

## Annotations  

> Selective Loss Masking
> 模型在训练的过程中，如果处理不当，很可能会陷入到二元境地，比如一直都输出 CoT token 或者一直不输出 CoT token。比如在 【数学类】数据集中训练之后，很可能一直输出 CoT token。这样模型就不能很好的进行探索，坍缩到一个方向去了。
>
> 这里的做法也很简单，在 RL 训练的过程中，把 policy gradient 中的 loss 不算所有的 token，而是 mask 掉 <think> 后的第一个 token。这样做有什么好处，我们保持了 SFT/RL 阶段学到的要不要触发 CoT，只是我们 mask 掉了 Loss，通过 Loss 优化控制下一步是否触发 CoT，而不是改变上一步学到的结果。  

mask掉<think>后的第一个token，即不参与loss计算，保留模型对是否开启COT输出的决策能力

[Link️](https://cubox.pro/web/annotations/cards/7339186180103078460?highlight=7339186180342156991)  

