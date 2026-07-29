title: 将检索 Token 数量降低 3 倍并提升 RAG 准确率：Blockify 框架 source: https://mail.google.com/mail/u/0/#inbox/19d9d1a7d44f86a9 author:


* "[[DailyDoseOfDS]]" published: 2026-04-17 created: 2026-07-28 description: 传统 RAG 检索 5 个 300 Token 的 Chunk 会引入 1500 Token 冗余。Blockify 利用微调模型生成平均 98 Token 的结构化 IdeaBlocks，将 Token 降低 3.09 倍并提升 13.55% 向量准确率。 tags:
* clippings


________________


将检索 Token 数量降低 3 倍并提升 RAG 准确率：Blockify 框架
企业文档中经常存在大量跨版本的重复信息。传统 RAG 按固定字符数切分 Chunk（如每次检索 5 个 300 Token 的 Chunk），在 LLM 生成任何回答前就已经消耗了 1,500 输入 Token。


更严重的问题是，当多个相似 Chunk 包含微小差异时，LLM 会将它们混淆，产生难以察觉的幻觉。
Blockify 解决方案：IdeaBlocks
Blockify 在原始文档与向量数据库之间引入了一个优化层：


* 不使用原始切片，而是利用微调后的 LLM 将文档转化为结构化的微型知识单元——IdeaBlocks。
* 每个 IdeaBlock 围绕“一个问题与一个验证过的解答”构建，平均大小仅为 98 Token。
* 可在 Intel Xeon CPU 上高效运行，无需额外 GPU 部署。
实验效果
在公开 Benchmark 上，IdeaBlock 索引相比传统 Chunk 索引：


* 向量检索准确率提升 13.55%。
* 输入 Token 数量减少 3.09 倍。
* 通过提高知识密度降低了 API 成本，同时消除了信息混淆。