title: BM25 文本排序算法工作原理剖析 source: https://mail.google.com/mail/u/0/#inbox/19dfa25648e2f2cb author:

"[[DailyDoseOfDS]]" published: 2026-05-05 created: 2026-07-28 description: 解读拥有 30 年历史的经典检索算法 BM25 解决关键词稀缺度、词频饱和度与文档长度归一化的三核心数学逻辑及其在混合检索（Hybrid Search）中的应用。 tags:

clippings

# BM25 文本排序算法工作原理剖析

无需训练、无需 Embedding 的经典 BM25 算法至今依然是 Elasticsearch 与主流生产级搜索系统的基石。

## BM25 的 3 大核心回答：

词的稀有度（IDF）：提升稀有词权重，忽视通用停用词。

词频饱和度（Term Frequency Saturation）：词出现 10 次与 100 次的边际效益递减，通过参数 k1 抑制高频词过调。

文档长度归一化（Document Length Normalization）：避免长文档因天然包含更多词而作弊得分，通过参数 b 惩罚超长文档。

在现代 RAG 系统中，将 BM25 的精准关键词匹配与向量搜索（Vector Search）结合构成的**混合检索（Hybrid Search）**能同时兼顾语义理解与精确匹配。
