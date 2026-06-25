---
id: "7390291325532245163"
cubox_url: https://cubox.pro/web/card/7390291325532245163
url: https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651000674&idx=2&sn=39634c52d4546d5bb9ab0f8b039f1252&poc_token=HHW7Gmmjvpge58KdOAVjkmYQhBd-LFpfSiM4pTPB
tags:
  - LLM
  - Post-training
  - Training
  - Pre-training

---
# HuggingFace从决策到落地「手把手」教你训练大模型

一次关于训练最先进语言模型的挑战、决策和混乱现实的实用之旅。

[Read in Cubox](https://cubox.pro/web/card/7390291325532245163)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651000674&idx=2&sn=39634c52d4546d5bb9ab0f8b039f1252&poc_token=HHW7Gmmjvpge58KdOAVjkmYQhBd-LFpfSiM4pTPB)  

---

## Annotations  

> 基线虽好，但并非为你量身定制，因此需要修改。然而，「任何架构上的改变都伴随着风险」。为此，必须遵守「去风险」的纪律，即：「除非你测试过它确实有帮助，否则不要改变任何东西。」
>
>
>
> 修改的难点在于组件太多且相互作用。你不能测试所有组合。正确的方法是：一次只测试一个有潜力的变更。如果它有效，就将其整合，使其成为新的基线，然后再测试下一个变更。  

[Link️](https://cubox.pro/web/annotations/cards/7390291325532245163?highlight=7390300891464599772)  

> 为了解决这些平衡性问题，现代 LLM 训练已经从「静态混合」（如 GPT-3）演变为多阶段训练（如 Llama3、SmolLM2）。这种方法在训练过程中动态地改变数据混合比例。
>
>
>
> 其核心洞察是，模型的最终行为深受其在训练末期看到的数据的影响。因此，策略是：
>
>
>
> 在训练早期，使用丰富、多样化但质量稍低的数据（如网页文本）。
>
> 在训练末期（特别是在学习率衰减的「退火阶段」），引入稀缺、高质量的数据（如专业数学和代码数据集），以最大化其影响力。  

[Link️](https://cubox.pro/web/annotations/cards/7390291325532245163?highlight=7390302613238974476)  

> 另外，文章还指出，在现代 LLM 的预训练中，通常会采用多阶段训练策略（multi-stage training），每个阶段使用不同的数据混合比例，并在最后阶段进行上下文长度扩展。比如 Qwen3 就采用了通用阶段、推理阶段、长上下文阶段的三阶段训练方案。而 SmolLM3 采用了类似的理念，在训练过程中计划性地引入高质量数据集并扩展上下文长度，同时根据性能监控结果进行动态调整。  

[Link️](https://cubox.pro/web/annotations/cards/7390291325532245163?highlight=7390336970905357683)  

