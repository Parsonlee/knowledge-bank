---
title: "RAG从入门到精通系列5：Indexing（索引）"
source: https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495567&idx=1&sn=3c2f6d114a792093f28e8a2b95851de6&chksm=eaecf530dd9b7c26842e80ac68098094bc0f39f911cb8861f32727cea4e858e83bb472189a50&cur_album_id=3689450339863740420&scene=190
created: 2026-06-25
tags:
  - clipping
  - cubox
---

# RAG从入门到精通系列5：Indexing（索引）

> [!quote]
> 通过结合多种表示（例如，文档的摘要、块或完整内容），来在检索和生成过程中取得最佳效果。它通过使用不同层次和粒度的表示（简洁的摘要与详细的文档）来弥补单一表示可能存在的不足。

> [!quote]
> RAPTOR（Recursive Abstractive Processing for Tree-Organized Retrieval）是一种将文档组织成分层结构的索引技术，它能够有效地实现递归式的信息抽象和检索。这种方法以“树”的形式组织文档数据，叶节点代表原始文档或者文档块，树的高层节点则代表这些文档经过抽象后的总结。RAPTOR 的目标是通过分层的方式，提升信息检索的效率，同时能够适应不同粒度的查询需求。

> [!quote]
> 基于细粒度的 token 级嵌入相似性计算，即 ColBERT（Contextualized Late Interaction over BERT）
