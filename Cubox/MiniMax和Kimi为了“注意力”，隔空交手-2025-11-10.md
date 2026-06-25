---
id: "7387381961167212077"
cubox_url: https://cubox.pro/web/card/7387381961167212077
url: https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247619925&idx=1&sn=375f3d4c9dfae099424769ecd31c9ddf&poc_token=HLFJEWmjOjKhclaNoe8QweFOQ3k4Rfpj1MU8HpYN
tags:
  - LLM

---
# MiniMax和Kimi为了“注意力”，隔空交手

MiniMax回归Full Attention，Kimi开源Kimi Linear。一个向左，一个向右

[Read in Cubox](https://cubox.pro/web/card/7387381961167212077)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247619925&idx=1&sn=375f3d4c9dfae099424769ecd31c9ddf&poc_token=HLFJEWmjOjKhclaNoe8QweFOQ3k4Rfpj1MU8HpYN)  

---

## Annotations  

> Haohai详细阐述了三个核心困难。第一个是工程链路复杂性爆炸。用他的话说，“需要同时满足code/math、agent、多模态、Long CoT、RL、低精度运算、缓存、speculative decoding等众多场景”。翻译成人话就是，现代大模型不只是做一件事，而是要同时支持十几种不同的应用场景。每增加一种efficient attention机制，就要在所有这些场景下验证，工程复杂度呈指数级增长。  

[Link️](https://cubox.pro/web/annotations/cards/7387381961167212077?highlight=7387381961381118165)  

> 第二个困难是评测体系局限。“小规模实验的结论无法外推，复杂多跳推理任务的缺陷只在大规模时暴露。”在小模型上测试效果好，不代表在大模型上也好。很多问题只有在训练到一定规模时才会暴露，但那时候已经投入了大量资源，来不及调整。Haohai在评论区补充说，复杂多跳推理任务可以参考KorBench、BBEH等榜单，以及BBH里的dyck language任务。  

[Link️](https://cubox.pro/web/annotations/cards/7387381961167212077?highlight=7387382136581390959)  

> 第三个困难是基建不完善。“Linear Attention的训练是访存bound，推理需要解决低精度存储、Prefix Cache、投机解码等问题。”即使理论上linear attention更快，但实际工程中需要解决很多基础设施问题。训练时内存带宽成为瓶颈，推理时需要支持各种优化技术，这些都还没有成熟的解决方案。  

[Link️](https://cubox.pro/web/annotations/cards/7387381961167212077?highlight=7387382169376653540)  

