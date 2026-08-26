---
title: Delta attention in Kimi K3 to fix growing KV cache
source_key: dailydoseofds
email_subject: 11 LLM Evaluation Methods
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Fri, 24 Jul 2026 22:05:08 +0000
email_id: 19f962933027e3e6
article_id: 19f962933027e3e6:1
published: '2026-07-24'
tags:
- LLM/arch/attention
- LLM/inference
- LLM/arch
---

# Delta attention in Kimi K3 to fix growing KV cache

- **原邮件主题**: 11 LLM Evaluation Methods
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 24 Jul 2026 22:05:08 +0000
- **ID**: 19f962933027e3e6

---

## [**Delta attention in Kimi K3 to fix growing KV cache**](<https://fff97757.click.kit-mail3.com/68ud0dr3k9i8h5927wzuohpzxd0kva9hnlpoo/wnh2hghqev6oe8b7hx/aHR0cHM6Ly9raW1pLmNvbS9ibG9nL2tpbWktazM=>)

Kimi K3 leans on a new mechanism called delta attention that does not keep a growing KV cache.

That is how it holds a million tokens of context without the memory blowing up.

Before we can understand delta attention, we need to understand attention itself.

It is a lookup. Every token stores a key, which works like an address, and a value, which is the content at that address.

![](https://substackcdn.com/image/fetch/$s_!ab3R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44a11973-6572-4b28-b2a2-d30f4127f66c_1268x569.jpeg)   
---  
  
To build its output, a token sends out a query, matches it against every key in the sequence, and pulls back a blend of the values whose keys matched.

Standard attention keeps every one of those key and value pairs as a list, one entry per token.

That list is the KV cache, and it grows with the sequence, so each new token has to scan the whole thing to build its output.

Delta attention keeps the lookup process but throws away the list.

![](https://substackcdn.com/image/fetch/$s_!x4qz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c16b109-ac40-4b6a-bed3-0a553382b4d2_1237x516.jpeg)   
---  
  
The entire past collapses into one fixed-size matrix that still behaves like the lookup table.

When you hand it a key, it returns the value vector, blended from everything the past tokens wrote, and it’s weighted by how closely each stored key matches the one you handed in.

Writing is a constrained operation. A fixed matrix has no free slot to append to, so every write lands in a direction that earlier writes already occupy and merges the two associations together.

The delta rule handles this in two moves per token, depicted below:

![](https://substackcdn.com/image/fetch/$s_!yGpl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c1b69e7-4fc8-441b-bab8-175db61a7f6f_1376x768.jpeg)   
---  
  
→ It reads before it writes. It hands the matrix the new token’s key and sees what value the memory currently returns, its existing guess for that address.

→ It writes the difference, not the value. It compares that guess against the value it actually wants stored and writes only the gap. That gap is the delta, and it corrects the old association instead of stacking a new one on top.

The matrix also lets old entries fade over time, so a fixed size can keep absorbing a long sequence without filling up.

Standard attention remembers by keeping everything and pays a quadratic cost to re-scan it.

Delta attention remembers by rewriting one matrix and pays a linear cost.

Of course, a compressed matrix cannot store every token exactly, so recall of any single token becomes approximate. That is why production models interleave the two, i.e., a few full-attention layers for exact lookup and the rest running linear.

[**Read more in the official announcement blog here →**](<https://fff97757.click.kit-mail3.com/68ud0dr3k9i8h5927wzuohpzxd0kva9hnlpoo/wnh2hghqev6oe8b7hx/aHR0cHM6Ly9raW1pLmNvbS9ibG9nL2tpbWktazM=>)
