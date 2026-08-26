---
title: How does BM25 ranking algorithm work?
source_key: dailydoseofds
email_subject: Train Classical ML Models on Large Datasets
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Tue, 05 May 2026 21:57:27 +0000
email_id: 19dfa25648e2f2cb
article_id: 19dfa25648e2f2cb:1
published: '2026-05-05'
tags:
- RAG/retrieval
---

# How does BM25 ranking algorithm work?

- **原邮件主题**: Train Classical ML Models on Large Datasets
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Tue, 05 May 2026 21:57:27 +0000
- **ID**: 19dfa25648e2f2cb

---

## [**How does BM25 ranking algorithm work?**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hlg2xd9f8h855rmmqclhvzgnn/58hvh7hg28ndq5t6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==>)

A 30-year-old algorithm with zero training, zero embeddings, and zero fine-tuning still powers Elasticsearch, OpenSearch, and most production search systems today.

It’s called BM25.

Let’s understand what makes it so powerful:

![](https://substackcdn.com/image/fetch/$s_!Bhxe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d71335e-5177-4228-87bf-dde550e55e79_1936x1200.png)   
---  
  
Imagine you’re searching for “transformer attention mechanism” in a library of ML papers.

BM25 asks three simple questions:

“How rare is this word?”

Every paper contains “the” and “is”, which makes it useless. But “transformer” is specific and informative. BM25 boosts rare words and ignores the noise.

→ This is `IDF(qᵢ)` in the formula

“How many times does it appear?”

If “attention” appears 10 times in a paper, that’s a good sign. But 10 vs 100 occurrences won’t make much difference. BM25 applies diminishing returns.

→ This is `f(qᵢ, D)` combined with `k₁` that controls saturation

“Is this document unusually long?”

A 50-page paper will naturally contain more keywords than a 5-page paper. BM25 levels the playing field so longer documents don’t cheat their way to the top.

→ This is `|D|/avgdl` controlled by parameter b

Overall, BM25 is based around three questions, with no requirement for neural networks (refer to the image below again):

![](https://substackcdn.com/image/fetch/$s_!TM-A!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb25056d-1348-4811-98ea-84192ae1d976_1936x1200.png)   
---  
  
BM25 excels at exact keyword matching, which is something embeddings often struggle with. It also shines when your corpus has domain-specific terminology that embedding models probably weren’t trained on.

If your user searches for “error code 5012,” embeddings might return semantically similar results. BM25 will find the exact match.

This is why hybrid search exists.

Top [**RAG systems**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hlg2xd9f8h855rmmqclhvzgnn/58hvh7hg28ndq5t6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==>) today combine BM25 with vector search. You get the best of both worlds: semantic understanding AND precise keyword matching.

So before you throw GPUs at every search problem, consider BM25. It might already solve your problem, or make your semantic search even better when combined.

👉 Over to you: What topics would you like to learn next?
