---
title: Visual Guide to Bi-encoders, Cross-encoders and ColBERT
source: https://mail.google.com/mail/u/0/#inbox/197658945bda228b
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-12
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Visual Guide to Bi-encoders, Cross-encoders and ColBERT 的原理剖析与工程实践。
tags:
  - clippings
---

# Visual Guide to Bi-encoders, Cross-encoders and ColBERT

## 1. 核心要点解析

本期内容重点涵盖：
- **Visual Guide to Bi-encoders, Cross-encoders and ColBERT**

## 2. 深度拆解与正文翻译

​

----------------------
In today's newsletter:
----------------------

* ​Transform your terminal into an Agent​.
* Visual guide to Bi-encoders, Cross-encoders, and ColBERT.

* [Hands-on] ​Supervised vs Reinforcement finetuning (with
code)​.

Reading time: 3 minutes.

TODAY'S ISSUE

Together with Altassian
-----------------------

-----------------------------------------------------------------
​Transform your terminal into an Agent (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/owhkhqhwlwwllquv/aHR0cHM6Ly9mbmYuZGV2LzRrUmI3Ym0=
)​
-----------------------------------------------------------------

(
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/owhkhqhwlwwllquv/aHR0cHM6Ly9mbmYuZGV2LzRrUmI3Ym0=
)​
Atlassian’s new Rovo Dev CLI (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/owhkhqhwlwwllquv/aHR0cHM6Ly9mbmYuZGV2LzRrUmI3Ym0=
) brings AI right into the command line in a way that actually
helps you ship:

* Generate, refactor, and review code using plain English.
* Debug without context switching.
* Auto-generate docs from your commit history.
* Pull in Jira tickets + Confluence context, all in one flow.

It’s seamlessly integrated with Atlassian tools, so you can go
from idea → code → doc → deployment without leaving your flow.

-->Use Rovo Dev CLI Agent (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/owhkhqhwlwwllquv/aHR0cHM6Ly9mbmYuZGV2LzRrUmI3Ym0=
)
Use Rovo Dev CLI Agent ( https://fnf.dev/4kRb7bm )​Try Rovo Dev
CLI here → (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/owhkhqhwlwwllquv/aHR0cHM6Ly9mbmYuZGV2LzRrUmI3Ym0=
)​

NLP systems
-----------

-----------------------------------------------------------------
​Visual Guide to Bi-encoders, Cross-encoders & ColBERT (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/z2hghnhereerrmip/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYmktZW5jb2RlcnMtYW5kLWNyb3NzLWVuY29kZXJzLWZvci1zZW50ZW5jZS1wYWlyLXNpbWlsYXJpdHktc2NvcmluZy1wYXJ0LTEv
)​
-----------------------------------------------------------------

So many real-world NLP systems, implicitly or explicitly, rely on
pairwise sentence (or context) scoring (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/z2hghnhereerrmip/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYmktZW5jb2RlcnMtYW5kLWNyb3NzLWVuY29kZXJzLWZvci1zZW50ZW5jZS1wYWlyLXNpbWlsYXJpdHktc2NvcmluZy1wYXJ0LTEv
) in one form or another.

* ​RAG systems (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/p8heh9h454455esq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
)​
* QA systems
* Duplicate text detection systems, etc.

The visual depicts three popular approaches used in the industry
to handle this:

​
Let’s understand them one by one!

We covered them with implementation here:
1) Bi-encoders and Cross-encoders for sentence pair similarity
scoring (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/z2hghnhereerrmip/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYmktZW5jb2RlcnMtYW5kLWNyb3NzLWVuY29kZXJzLWZvci1zZW50ZW5jZS1wYWlyLXNpbWlsYXJpdHktc2NvcmluZy1wYXJ0LTEv
).

2) AugSBERT for sentence pair similarity scoring (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/x0hph6hedeeddgt5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYXVnc2JlcnQtYmktZW5jb2RlcnMtY3Jvc3MtZW5jb2RlcnMtZm9yLXNlbnRlbmNlLXBhaXItc2ltaWxhcml0eS1zY29yaW5nLXBhcnQtMi8=
).

3) A deep dive into ColBERT and ColBERTv2 for improving RAG
systems (with implementation). (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/dpheh0heweewmzcm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC04LXdpdGgtaW1wbGVtZW50YXRpb24v
)​

*****************
1) Cross-encoders
*****************

These are conceptually one of the most powerful approaches.

​
* Concatenate the query text and the document text.
* Encode it using a BERT-like encoder model.
* Apply a transformation (a dense layer) to the [CLS] token
representations to get a similarity score.

Since the model attends to both contexts, this produces an
incredibly semantically expressive representation.

But it does not scale because if you have 1B documents, you must
do 1B forward passes to determine the most relevant documents to
a query.

**************
2) Bi-encoders
**************

​
* Encode the query and the documents separately.
* Compute the cosine similarity between the [CLS] token of the
query and the document.

This is highly scalable since the document embeddings can be
computed offline.

But we lose all the interaction and simply “hope” that the entire
information about the query and the document is well summarized
in the [CLS] token.

**********
3) ColBERT
**********

This brings together the power of cross-encoders and the
scalability of bi-encoders.

​
* Encode the query and the documents separately.
* Compute a late interaction matrix, which contains similarity
scores (dot product) between all query tokens and all document
tokens.
* For every token, determine the max score across all document
tokens.
* Sum these max scores to get a matching score.

Advantages:

* Like bi-encoders, it is highly scalable since document
embeddings can be computed offline.
* Like cross-encoders, it maintains cross-interactions between
the query and the document tokens (called late interaction).

We covered them with implementation here:

* ​Bi-encoders and Cross-encoders for Sentence Pair Similarity
Scoring (
https://click.convertkit-mail2.com/wvuv9vo06zughkok933u7hnvgwxxxh8h4wlvv/z2hghnhereerrmip/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYmktZW5jb2RlcnMtYW5kLWNyb3NzLWVuY29kZXJzLWZvci1zZW50ZW5jZS1wYWlyLXNpbWlsYXJpdHktc2Nv

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
