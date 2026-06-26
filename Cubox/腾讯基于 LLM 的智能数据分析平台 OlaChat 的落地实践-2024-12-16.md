---
id: "7268160114224270585"
cubox_url: https://cubox.pro/web/card/7268160114224270585
url: https://mp.weixin.qq.com/s/0Bm_7COAATll5gVBTsz_hA
tags:
  - AI-Agent/AI-BI
---
# 腾讯基于 LLM 的智能数据分析平台 OlaChat 的落地实践

谭云志 腾讯 高级研究员

[Read in Cubox](https://cubox.pro/web/card/7268160114224270585)  
[Read Original](https://mp.weixin.qq.com/s/0Bm_7COAATll5gVBTsz_hA)  

---

## Annotations  

> 结构化数据，比如表和指标，每个表有表名、字段，指标下有维度（如年龄、性别等），这些数据有层次性和明确的结构。这种层次结构不同于非结构化文本，不能简单地通过自然语言的检索增强方法来处理。传统的自然语言检索主要基于 embedding（嵌入向量）技术，将文本分块后，通过相似度匹配来检索相关信息。然而，结构化数据并不遵循自然语言的逻辑，导致传统方法难以直接应用。  

[Link️](https://cubox.pro/web/annotations/cards/7268160114224270585?highlight=7268176844627641180)  

> 我们有两种方案，分别从两个角度来解决元数据检索增强的问题。
> 第一种方案是 FlattenedRAG，在已有元数据基础上进行组合，将结构化的元数据变为非结构化的自然语言，当接收到用户问题后，进行检索、排序，找到与知识库中一致的数据。
> 第二种方案是 StructuredRAG，充分利用好元数据的结构化信息，优先检索出最核心的元素，再围绕这些核心元素进行二次检索，找到所需的数据。  

结构化数据可以转化为非结构化数据，进而套用标准RAG

[Link️](https://cubox.pro/web/annotations/cards/7268160114224270585?highlight=7268160114282989564)  

