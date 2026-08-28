---
title: " Why per-user memory graphs break normal graph DBs "
source_key: "dailydoseofds"
email_subject: "KV vs Prefix vs Prompt vs Semantic Caching"
email_sender: "Daily Dose of DS <avi@dailydoseofds.com>"
email_date: "Thu, 27 Aug 2026 20:02:01 +0000"
email_id: "1a044d0b132124de"
article_id: "1a044d0b132124de:1"
published: "2026-08-27"
tags: []
---

#  Why per-user memory graphs break normal graph DBs 

- **邮件来源**: dailydoseofds
- **原邮件主题**: KV vs Prefix vs Prompt vs Semantic Caching
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Thu, 27 Aug 2026 20:02:01 +0000
- **邮件 ID**: 1a044d0b132124de
- **文章 ID**: 1a044d0b132124de:1

---

## [**Why per-user memory graphs break normal graph DBs**](<https://blog.getzep.com/why-we-built-a-graph-database-service-for-agent-memory/>)

Agent memory stored as a knowledge graph produces one graph per user, per team, and per project. A single enterprise customer can run millions of them.

Most of those graphs are cold at any given moment, and a single query reads exactly one of them.

![](https://substackcdn.com/image/fetch/$s_!Hc5p!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b7eda63-805a-431d-b215-bf55bbf88c03_1376x768.jpeg)   
---  
  
Neo4j and similar systems are built for the opposite workload. One large graph stays resident in memory, and every request passes through a Cypher parser and a query optimizer before it reaches the data.

On millions of small idle graphs, the cost follows provisioned memory rather than the reads actually served. Isolation also becomes a filter on one shared graph rather than a separate graph per tenant.

Adding hardware stopped helping Zep, so the team built [**Konig**](<https://blog.getzep.com/why-we-built-a-graph-database-service-for-agent-memory/>) around this access pattern.

![](https://substackcdn.com/image/fetch/$s_!7gXi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9181ec8e-2a0e-435b-9e3c-f25f0e8f9cd5_1376x768.jpeg)   
---  
  
Konig keeps hot graphs in RAM, recently used graphs on local NVMe, and idle graphs in object storage, loading them back when a query arrives. Encryption keys and retention rules attach to each graph.

Because each query reads a single graph, PageRank runs inline in milliseconds rather than as a batch job. Retrieval holds a p95 under 100ms from a thousand graphs up to tens of millions, and end-to-end latency stays under 200ms.

Konig also keeps two in-memory layouts of every graph and converts between them on demand.

[**We read this interesting blog by the Zep team that covers the full design, including the AVX-512 search kernels and bi-temporal facts, here →**](<https://blog.getzep.com/why-we-built-a-graph-database-service-for-agent-memory/>)
