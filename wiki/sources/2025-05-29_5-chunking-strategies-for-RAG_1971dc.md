---
type: source
tags:
- RAG/retrieval
- RAG/chunking
summary: 本文介绍了在构建 RAG 系统时常用的五种文本切分（chunking）策略，包括固定大小切分、语义切分、递归切分、基于文档结构的切分以及基于 LLM
  的切分，并对比了各自的优缺点和适用场景。
sources:
- raw/articles/2025-05-29_5-chunking-strategies-for-RAG_1971dc.md
updated: '2026-08-03'
---

# 5 chunking strategies for RAG

## 来源信息
- **来源**: Daily Dose of DS
- **作者**: Avi Chawla
- **原始链接**: [A crash course on building RAG systems (Part 1)](https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-1-with-implementations/)
- **归档物理文献**: [[raw/articles/2025-05-29_5-chunking-strategies-for-RAG_1971dc.md]]

## 核心要点
1. **固定大小切分 (Fixed-size chunking)**：基于预设的字符数、单词数或 Token 数将文本均匀切分为片段。为保持语义连贯性通常会设置重叠（Overlap）。实现简单，便于批处理，但容易切断完整的句子或语义。
2. **语义切分 (Semantic chunking)**：基于句子或段落的相似度进行切分。先将文档分成句子等基础单元并计算向量嵌入，若相邻段落的余弦相似度高于特定阈值则合并为一块，直到相似度显著下降时开始新块。能很好地保留完整概念，提高检索精度，但阈值设定依赖于具体文档。
3. **递归切分 (Recursive chunking)**：先根据自然分隔符（如段落、标题）尝试分块，若分出来的块超过预设的限制大小，再用更小粒度的分隔符进一步递归切分。较好保留自然语言流，但计算开销略大。
4. **基于文档结构切分 (Document structure-based chunking)**：利用标题、章节等文档固有的逻辑结构来定义切分边界，维持逻辑结构完整。但需要文档具有良好的结构，且各块大小不一，可能需要结合递归切分。
5. **基于 LLM 的切分 (LLM-based chunking)**：利用大语言模型去理解语义并生成结构独立、意义完整的文本块。语义准确度最高，但计算成本极高，且受 LLM 上下文长度限制。

## 关键引文
- "Since the additional document(s) can be large, step 1 also involves chunking, wherein a large document is divided into smaller/manageable pieces. This step is crucial since it ensures the text fits the input size of the embedding model."
- "Unlike fixed-size chunks, [semantic chunking] maintains the natural flow of language and preserves complete ideas... A minor problem is that it depends on a threshold to determine if cosine similarity has dropped significantly, which can vary from document to document."
- "Prompt the LLM to generate semantically isolated and meaningful chunks. This method ensures high semantic accuracy... But this is the most computationally demanding chunking technique of all five techniques discussed here."

## 联动概念
- [[wiki/concepts/概念_文本切分五层级]]
- [[wiki/concepts/概念_字符切分]]
- [[wiki/concepts/概念_递归字符切分]]
- [[wiki/concepts/概念_文档结构切分]]
- [[wiki/concepts/概念_语义切分]]

> 📎 **物理文献**：[[raw/articles/2025-05-29_5-chunking-strategies-for-RAG_1971dc.md]]
