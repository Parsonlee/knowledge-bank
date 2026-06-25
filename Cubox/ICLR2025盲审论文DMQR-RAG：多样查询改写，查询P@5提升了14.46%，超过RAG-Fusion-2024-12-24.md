---
id: "7271069011834571080"
cubox_url: https://cubox.pro/web/card/7271069011834571080
url: https://mp.weixin.qq.com/s/PQF8Ka5UPYxpnEASTUSs5w
tags:
  - RAG
  - QueryProcessing

---
# ICLR2025盲审论文DMQR-RAG：多样查询改写，查询P@5提升了14.46%，超过RAG-Fusion

论文解析

[Read in Cubox](https://cubox.pro/web/card/7271069011834571080)  
[Read Original](https://mp.weixin.qq.com/s/PQF8Ka5UPYxpnEASTUSs5w)  

---

## Annotations  

> 改写策略
> 为了提升检索文档的多样性，同时考虑到用户查询可能存在的信息噪音或冗余问题，本文提出四种改写策略：
>
> 信息等同：改写的目标是消除用户查询中的噪音并精炼查询。具体实现为通用查询改写（GQR）和关键词提取改写（KWR），分别通过保留原始查询中的关键信息或直接提取关键词来提升检索精度。
>
> 信息扩展：通过整合LLMs的先验知识生成伪答案，使查询扩展更多信息；该策略被称为伪答案改写（PAR）。
>
> 信息缩减：当查询包含过多细节时，对其进行核心内容提取以简化查询并突出重点，定义为核心内容提取（CCE）。  

[Link️](https://cubox.pro/web/annotations/cards/7271069011834571080?highlight=7271069011884901992)  

