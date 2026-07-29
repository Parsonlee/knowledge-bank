---
title: 5 Chunking Strategies For RAG
source: https://mail.google.com/mail/u/0/#inbox/1971dcca96aa74c3
author:
  - "[[DailyDoseOfDS]]"
published: 2025-05-29
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 5 Chunking Strategies For RAG 的原理剖析与工程实践。
tags:
  - clippings
---

# 5 Chunking Strategies For RAG

## 1. 核心要点解析

本期内容重点涵盖：
- **5 Chunking Strategies For RAG**

## 2. 深度拆解与正文翻译

​

----------------------
In today's newsletter:
----------------------

* Linkup achieves SOTA performance on SimpleQA.
* 5 chunking strategies for RAG
* [Hands-on] Building a real-time voice RAG Agent.

Reading time: 3 minutes.

TODAY'S ISSUE

together with linkup
--------------------

-----------------------------------------------------------------
​Linkup Achieves SOTA Performance on SimpleQA (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/kkhmh6hnexxev6fl/aHR0cHM6Ly93d3cubGlua3VwLnNvLw==
)​
-----------------------------------------------------------------

(
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/kkhmh6hnexxev6fl/aHR0cHM6Ly93d3cubGlua3VwLnNvLw==
)​
​Linkup (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/kkhmh6hnexxev6fl/aHR0cHM6Ly93d3cubGlua3VwLnNvLw==
) search achieved 91% F-Score on OpenAI's SimpleQA benchmark,
outperforming Perplexity.

This establishes Linkup as the best search API for AI:

* Delivers more accurate, relevant results.
* Surfaces the latest information at lightning speed.
* Integrate natively with high-quality data sources.

​Start building with Linkup web search today → (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/kkhmh6hnexxev6fl/aHR0cHM6Ly93d3cubGlua3VwLnNvLw==
)​

-->Start using Linkup web search (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/kkhmh6hnexxev6fl/aHR0cHM6Ly93d3cubGlua3VwLnNvLw==
)
Start using Linkup web search ( https://www.linkup.so/ )

Today's daily dose of data science
----------------------------------

-----------------------------------------------------------------
​5 chunking strategies for RAG (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/58hvh7hg066027a6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
)​
-----------------------------------------------------------------

Here’s the typical workflow of RAG:

​
Since the additional document(s) can be large, step 1 also
involves chunking, wherein a large document is divided into
smaller/manageable pieces.

This step is crucial since it ensures the text fits the input
size of the embedding model.

Here are five chunking strategies for RAG:

​
Let’s understand them today!

If you want to dive into building LLM apps, our full RAG crash
course discusses RAG from basics to beyond:
- RAG fundamentals (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/58hvh7hg066027a6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
)​
- RAG evaluation (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/25h2hoh3gmmgwnh3/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0yLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
)​
- RAG optimization (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/qvh8h7hdvkkvpeil/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0zLXdpdGgtaW1wbGVtZW50YXRpb24v
)​
- Multimodal RAG (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/g3hnh5hmnqqnwrir/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC01LXdpdGgtaW1wbGVtZW50YXRpb24v
)​
- Graph RAG (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/9qhzhnhdx55xrwt9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC03LXdpdGgtaW1wbGVtZW50YXRpb24v
)​
- Multivector retrieval using ColBERT (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/3ohphkh3rpprggtr/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC04LXdpdGgtaW1wbGVtZW50YXRpb24v
)​
- RAG over complex real-world docs ft. ColPali (
https://click.convertkit-mail2.com/mvug5g3q6xt5hq7vvv7fmhrn2l2qqt3/n2hohvhvg77g0pc6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC05LXdpdGgtaW1wbGVtZW50YXRpb24v
)​

**********************
1) Fixed-size chunking
**********************

Split the text into uniform segments based on a pre-defined
number of characters, words, or tokens.

​
Since a direct split can disrupt the semantic flow, it is
recommended to maintain some overlap between two consecutive
chunks (the blue part above).

This is simple to implement. Also, since all chunks are of equal
size, it simplifies batch processing.

But this usually breaks sentences (or ideas) in between. Thus,
important information will likely get distributed between chunks.

********************
2) Semantic chunking
********************

​
* Segment the document based on meaningful units like sentences,
paragraphs, or thematic sections.
* Next, create embeddings for each segment.
* Let’s say we start with the first segment and its embedding.*
If the first segment’s embedding has a high cosine similarity
with that of the second segment, both segments form a chunk.
* This continues until cosine similarity drops significantly.
* The moment it does, we start a new chunk and repeat.

Here’s what the output could look like:

​
Unlike fixed-size chunks, this maintains the natural flow of
language and preserves complete ideas.

Since each chunk is richer, it improves the retrieval accuracy,
which, in turn, produces more coherent and relevant responses by
the LLM.

A minor problem is that it depends on a threshold to determine if
cosine similarity has dropped significantly, which can vary from
document to document.

*********************
3) Recursive chunking
*********************

​
First, chunk based on inherent separators like paragraphs, or
sections.

Next, split each chunk into smaller chunks if the size exceeds

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
