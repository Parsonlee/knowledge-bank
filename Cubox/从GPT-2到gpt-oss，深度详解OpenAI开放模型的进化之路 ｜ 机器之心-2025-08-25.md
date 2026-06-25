---
id: "7359469340527169085"
cubox_url: https://cubox.pro/web/card/7359469340527169085
url: https://www.jiqizhixin.com/articles/2025-08-18-7
tags:
  - LLM/arch
---
# 从GPT-2到gpt-oss，深度详解OpenAI开放模型的进化之路 ｜ 机器之心

众所周知，OpenAI 并不够 Open，不仅研究论文发得越来越少，开源模型也是千呼万唤始出来。

[Read in Cubox](https://cubox.pro/web/card/7359469340527169085)  
[Read Original](https://www.jiqizhixin.com/articles/2025-08-18-7)  

---

## Annotations  

> 这很有意思，因为最近的趋势和发展表明，更多、更小的模型是有益的。在总参数大小不变的情况下，这种变化在来自 DeepSeekMoE 论文的下图中得到了很好的展示。  

[Link️](https://cubox.pro/web/annotations/cards/7359469340527169085?highlight=7359484207560655714)  

> 原因是混合模式下的模型性能低于单个模型：「在与社区讨论并反思此事后，我们决定放弃混合思考模式。现在我们将分别训练 Instruct 和 Thinking 模型，以实现最佳质量。」  

[Link️](https://cubox.pro/web/annotations/cards/7359469340527169085?highlight=7359485095691944245)  

> 我推测，GPT-2 之所以使用 Dropout，是因为它继承自原始的 Transformer 架构。研究者可能后面注意到，它并没有真正提升 LLM 的性能（我在小规模的 GPT-2 复现运行中也观察到了同样的情况）。这可能是因为 LLM 通常只在海量数据集上进行单轮训练，这明显不同于 Dropout 最初引入时针对的数百轮训练方案。因此，由于 LLM 在训练过程中每个 token 只被识别一次，因此过拟合的风险很小。
>
> 有趣的是，虽然 Dropout 在 LLM 架构设计中多年来一直被忽略，但我找到了一篇 2025 年的研究论文《Drop Dropout on Single-Epoch Language Model Pretraining》—— 其中包含小规模的 LLM 实验 (Pythia 1.4B)，证实了 Dropout 在这些单轮训练方案中会导致下游性能下降。  

[Link️](https://cubox.pro/web/annotations/cards/7359469340527169085?highlight=7359469340694940303)  

> 因此，总体而言，使用 GLU 变体可以减少参数数量，并且性能也更好。性能更佳的原因是这些 GLU 变体提供了额外的乘法交互，从而提高了表示能力（这与深度细长的神经网络比浅层宽广的神经网络表现更好的原因相同，前提是它们训练得当）。  

[Link️](https://cubox.pro/web/annotations/cards/7359469340527169085?highlight=7359471621683282931)  

> 在 MHA 中，每个注意力头都有自己的一组键和值。GQA 通过将多个注意力头分组以共享相同的键和值投影来减少内存占用  

[Link️](https://cubox.pro/web/annotations/cards/7359469340527169085?highlight=7359471785860925215)  

> LayerNorm 和 RMNSorm 都能稳定激活尺度并改善优化效果，但 RMNSorm 通常更适合大规模 LLM，因为它的计算成本更低。与 LayerNorm 不同，RMNSorm 没有偏差（平移）项，并将昂贵的均值和方差计算简化为一次均方根运算。这将跨特征约简的次数从两次减少到一次，从而降低 GPU 的通信开销并提高训练效率。  

[Link️](https://cubox.pro/web/annotations/cards/7359469340527169085?highlight=7359477698638385080)  

