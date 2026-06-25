---
title: "万字长文详解优图RAG技术"
source: https://mp.weixin.qq.com/s?__biz=MzU0NjU0ODk2Mg==&mid=2247501175&idx=1&sn=f5dbcbfa21326ab4e6ecd7f2cbb2f30c&chksm=fa33850e7b937994337117b7e0e41ef8ae33916a88243d0b4e171ad4b411a2fcb64872199319&mpshare=1&scene=1&srcid=0913mxhdXINU0klxMQg810mA&sharer_shareinfo=e8eba2a79bf5495dd205b862594c4394&sharer_shareinfo_first=e8eba2a79bf5495dd205b862594c4394
created: 2026-06-25
tags:
  - clipping
  - cubox
---

# 万字长文详解优图RAG技术

> [!quote]
> 具体到编码模型最主要的两类应用场景——文本语义相似性（STS）及信息检索（IR）。STS任务采用Spearman相关系数作为根本指标，该指标通过计算样本的预测排位与真实排位之差来衡量顺序一致性。IR任务的核心指标nDCG同样是list-wise式的，但它更强调高位优先性。鉴于在大部分IR任务中，与给定query相关的文档其实非常稀少，因此将这些正样本有效突出出来是提升模型表现的关键。
