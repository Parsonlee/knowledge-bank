title: 双编码器、交叉编码器与 ColBERT 语义匹配图解指南 source: https://mail.google.com/mail/u/0/#inbox/19edcc2a8ec8a790 author:


* "[[DailyDoseOfDS]]" published: 2026-06-18 created: 2026-07-28 description: 详细对比 Cross-encoders（高精度/低可扩展性）、Bi-encoders（高扩展性/离线预计算）与 ColBERT（延迟交互/兼顾精度与速度）的核心原理。 tags:
* clippings


________________


双编码器、交叉编码器与 ColBERT 语义匹配图解指南
文本句对相似度打分（Pairwise Context Scoring）是 RAG、问答与重排系统的核心技术。
3 种主流架构对比
1. Cross-encoders（交叉编码器）：将 Query 与 Document 拼接后共同送入 Transformer，利用 Attention 进行充分交叉交互。语义表达最强，但每次检索需实时前向计算，无法扩展至千万级文档。
2. Bi-encoders（双编码器）：Query 与 Document 分别独立编码，预先将文档向量化存入 Vector DB，在线计算余弦相似度。极具可扩展性，但丢失了词级交互信息。
3. ColBERT（Late Interaction 延迟交互）：保留文档每个 Token 的向量表示，在 Query 与 Document Token 之间计算点积矩阵，并取 MaxSim 累加。既支持文档向量离线索引，又保留了精确的词级交互。