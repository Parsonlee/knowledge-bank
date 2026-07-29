---
title: RAG & Fine-tuning in LLMs
source: https://mail.google.com/mail/u/0/#inbox/19b5c7637722a2ba
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-26
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 RAG & Fine-tuning in LLMs 的原理剖析与工程实践。
tags:
  - clippings
---

# RAG & Fine-tuning in LLMs

## 1. 核心要点解析

本期内容重点涵盖：
- **RAG & Fine-tuning in LLMs**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (
https://fff97757.click.convertkit-mail2.com/68ud0dr3k9i8h50m4wrcohpe59okkh9hnlpoo/6qheh8hl0pmzegco/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* One MCP server to access the web.
* ​RAG & Fine-tuning, explained visually​.
* The right way to use multiple embedding models.
* Loss Function of 16 ML Algos (a single frame summary).

TODAY'S ISSUE

MCP
---

-----------------------------------------------------------------
​One MCP server to access the web (
https://fff97757.click.convertkit-mail2.com/68ud0dr3k9i8h50m4wrcohpe59okkh9hnlpoo/25h2hoh3n7k6wmb3/aHR0cHM6Ly9naXRodWIuY29tL2x1bWluYXRpLWlvL2JyaWdodGRhdGEtbWNw
)​
-----------------------------------------------------------------

When Agents use web-related tools, they run into issues like IP
blocks, bot traffic, captcha solvers, etc.

* Agents get rate-blocked or rate-limited.
* Agents have to deal with JS-heavy or geo-restricted sites.

This hinders the Agent's execution.

​Bright Data MCP server (
https://fff97757.click.convertkit-mail2.com/68ud0dr3k9i8h50m4wrcohpe59okkh9hnlpoo/25h2hoh3n7k6wmb3/aHR0cHM6Ly9naXRodWIuY29tL2x1bWluYXRpLWlvL2JyaWdodGRhdGEtbWNw
) gives you 30+ powerful tools that allow AI agents to access,
search, crawl, and interact with the web without getting blocked.

-->​Bright Data MCP Server (open-source)​ (
https://fff97757.click.convertkit-mail2.com/68ud0dr3k9i8h50m4wrcohpe59okkh9hnlpoo/25h2hoh3n7k6wmb3/aHR0cHM6Ly9naXRodWIuY29tL2x1bWluYXRpLWlvL2JyaWdodGRhdGEtbWNw
)
​Bright Data MCP Server (open-source)​ (
https://github.com/luminati-io/brightdata-mcp )
​
The video below depicts the browser tool usage from Bright Data,
where the Agent is autonomously navigating a web page.

video preview (
https://api.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/hDdv7YCBbVtBiSgYjRg2RC/player
)-->
video preview-->
(
https://fff97757.click.convertkit-mail2.com/68ud0dr3k9i8h50m4wrcohpe59okkh9hnlpoo/9qhzhnhdngo0r7t9/aHR0cHM6Ly9hcGkuZmlsZWtpdGNkbi5jb20vZS9rN1lIUE4yNFNveHlNOG5HS1puRHhhL2hEZHY3WUNCYlZ0QmlTZ1lqUmcyUkMvcGxheWVy
)

​
Unlike typical scraping tools, this MCP server dynamically picks
the most effective tool based on the structure of the target
site.

These are some of the tools:

​
* Browser tool
* Web Unlocker API
* Scraper API
* Platform-specific scrapers for Instagram, LinkedIn, YouTube,
etc.
* SERP API, and more.

​You can try the MCP server using this GitHub repo → (
https://fff97757.click.convertkit-mail2.com/68ud0dr3k9i8h50m4wrcohpe59okkh9hnlpoo/25h2hoh3n7k6wmb3/aHR0cHM6Ly9naXRodWIuY29tL2x1bWluYXRpLWlvL2JyaWdodGRhdGEtbWNw
)​

The steps are detailed in the GitHub repo.

LLMs
----

-----------------------------------------------------------------
​RAG & Fine-tuning, explained visually (
https://fff97757.click.convertkit-mail2.com/68ud0dr3k9i8h50m4wrcohpe59okkh9hnlpoo/n2hohvhvenzmp8s6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
)​
-----------------------------------------------------------------

If you’re building real-world LLM apps, you can rarely use a
model out of the box without adjustments.

Devs typically treat RAG and fine-tuning as interchangeable
options, but in reality, they are not.

RAG and fine-tuning solve fundamentally different problems. One
controls what the model knows at runtime. The other changes how
the model behaves by default.

This visual breaks it down for you:

​
For RAG, look at the top half of the visual.

RAG operates at inference time. When a user sends a query, the
retriever searches your knowledge base (PDFs, vector DBs, APIs,
documents), pulls relevant context, and passes it to the LLM
along with the query. The model weights never change. You’re
giving the LLM a “cheat sheet” at runtime.

Fine-tuning is different. To understand, look at the bottom half
of the visual.

It happens offline, before deployment. You train the model on
domain-specific data, and the weights actually update. The model
now behaves differently by default.

Fine-tuning is for changing how the model behaves. Its tone,
vocabulary, response structure, or specialized reasoning
patterns.

Two questions guide which one you need:

* How much external knowledge does your task require?
* How much behavioral adaptation do you need?

If you need the model to reference specific documents, product
catalogs, or anything that updates frequently, that’s mostly a
RAG territory.

If you need the model to adopt internal vocabulary, match a
specific writing style, or follow domain-specific reasoning
patterns, that’s mostly a fine-tuning territory.

​
For instance, an LLM might struggle to summarize company meeting
transcripts because speakers use internal jargon the model has
never seen. Fine-tuning fixes this.

That said, in production systems, you might often need both. A
customer support bot might need to pull answers from
documentation (RAG) while responding in your brand’s voice
(fine-tuning).

The simple takeaway:

* RAG → What should the model know?
* Fine-tuning → How should the model behave

They’re not competing. They’re complementary layers in an LLM
stack.

On a side note, we started a beginner-friendly crash course on
RAGs recently with implementations, which covers:

* ​​​RAG fundamentals​​ (
https://fff97757.click.convertkit-mail2.com/68ud0dr3k9i8h50m4wrcohpe59okkh9hnlpoo/n2hohvhvenzmp8s6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
)​​​​ (
https://fff97757.click.convertkit-mail2.com/68ud0dr3k9i8h50m4wrcohpe59okkh9hnlpoo/reh8hohmnqg4rvu2/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0yLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
)​
* ​​RAG evaluat

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
