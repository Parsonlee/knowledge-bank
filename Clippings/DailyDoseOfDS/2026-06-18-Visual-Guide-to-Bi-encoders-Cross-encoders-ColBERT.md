title: "双编码器、交叉编码器与 ColBERT 算法图解指南" source: "https://mail.google.com/mail/u/0/#inbox/19edcc2a8ec8a790" author:

"[[DailyDoseOfDS]]" published: "2026-06-18" created: "2026-07-28" description: "对比 NLP 句对相似度计算的三大主流架构（Cross-encoder、Bi-encoder、ColBERT），详解晚期交互（Late Interaction）的平衡优势。" tags:

clippings

# 双编码器、交叉编码器与 ColBERT 算法图解指南

RAG 系统、问答系统与重复文本检测普遍依赖句对（或上下文）相似度打分。工业界常用的三大方法如下：

### 1. Cross-encoders（交叉编码器）

机制：拼接 Query 与 Document，统一输入 BERT 进行 Attention 计算。

优缺点：语义表达能力最强，但无法预先计算文档向量，面对十亿级文档库时无法扩展。

### 2. Bi-encoders（双编码器）

机制：Query 和 Document 分别独立编码，通过计算 [CLS] Token 的余弦相似度打分。

优缺点：文档向量可离线预计算，检索极快；但损失了词级别的交互信息。

### 3. ColBERT（晚期交互 Late Interaction）

机制：独立编码 Query 与 Document，但保留所有 Token 的向量，计算 late interaction 矩阵（取最大相似度之和）。

优缺点：兼具双编码的高扩展性（离线计算文档向量）与交叉编码的细粒度词级交互能力。
