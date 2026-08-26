---
title: Full global attention vs alternating attention
source_key: dailydoseofds
email_subject: uv Cheatsheet and Hands-on Guide for Python Devs
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Tue, 01 Jul 2025 20:28:05 +0000
email_id: 197c7ace7fc9ab0e
article_id: 197c7ace7fc9ab0e:1
published: '2025-07-01'
tags:
- DeepLearning
- LLM/arch/attention
---

# Full global attention vs alternating attention

- **原邮件主题**: uv Cheatsheet and Hands-on Guide for Python Devs
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Tue, 01 Jul 2025 20:28:05 +0000
- **ID**: 197c7ace7fc9ab0e

---

## **Full global attention vs alternating attention**

**ModernBERT** is an upgraded version of BERT with:

  * 16x larger sequence length.
  * Much better downstream performance, both for classification tasks and retrieval (like used in [**RAG systems**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-1-with-implementations/>)).
  * The most memory-efficient encoder.

Here's an interesting detail related to the attention network in ModernBERT:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/gx4t22RxRKL8z93YSTjSnM/email)   
---  
  
BERT used full global attention (shown on the left above), which has a quadratic complexity. ModernBERT made this efficient with **alternating attention**.

Here's the idea:

  * They used full global attention in every third layer.
  * All other layers used a sliding window attention, wherein, every token only attended to 128 nearest tokens (called local attention).

This allows ModernBERT to process much longer input sequences, while also being significantly faster than other encoder models. Here's an intuitive explanation (_taken directly from the announcement_):

_Conceptually, the reason this works is pretty simple: Picture yourself reading a book. For every sentence you read, do you need to be fully aware of the entire plot to understand most of it (full global attention)? Or is awareness of the current chapter enough (local attention), as long as you occasionally think back on its significance to the main plot (global attention)? In the vast majority of cases, it’s the latter._

Makes sense, doesn't it?
