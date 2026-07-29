---
title: Corrective RAG Agentic Workflow
source: https://mail.google.com/mail/u/0/#inbox/198ed2e36353fdf7
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-27
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Corrective RAG Agentic Workflow 的原理剖析与工程实践。
tags:
  - clippings
---

# Corrective RAG Agentic Workflow

## 1. 核心要点解析

本期内容重点涵盖：
- **Corrective RAG Agentic Workflow**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/9qhzhnhdgzr4ldt9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Connect any LLM to any MCP server!
* Corrective RAG Agentic Workflow
* Fine-tuning LLM Agents without Fine-tuning LLMs!

TODAY'S ISSUE

open-source
-----------

-----------------------------------------------------------------
​Connect any LLM to any MCP server! (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/3ohphkh3q4gxn4tr/aHR0cHM6Ly9naXRodWIuY29tL21jcC11c2UvbWNwLXVzZQ==
)​
-----------------------------------------------------------------

(
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/3ohphkh3q4gxn4tr/aHR0cHM6Ly9naXRodWIuY29tL21jcC11c2UvbWNwLXVzZQ==
)​
​mcp-use (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/3ohphkh3q4gxn4tr/aHR0cHM6Ly9naXRodWIuY29tL21jcC11c2UvbWNwLXVzZQ==
) is the open source way to connect any LLM to any MCP server and
build custom agents that have tool access, without using closed
source or application clients.

Build 100% local MCP clients.

​GitHub repo → (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/3ohphkh3q4gxn4tr/aHR0cHM6Ly9naXRodWIuY29tL21jcC11c2UvbWNwLXVzZQ==
) (don’t forget to star)

-->mcp-use Github repo (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/3ohphkh3q4gxn4tr/aHR0cHM6Ly9naXRodWIuY29tL21jcC11c2UvbWNwLXVzZQ==
)
mcp-use Github repo ( https://github.com/mcp-use/mcp-use )

hands-on
--------

-----------------------------------------------------------------
​[Hands-on] Corrective RAG Agentic Workflow (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/n2hohvhvn602krs6/aHR0cHM6Ly9naXRodWIuY29tL3BhdGNoeTYzMS9haS1lbmdpbmVlcmluZy1odWIvdHJlZS9tYWluL2ZpcmVjcmF3bC1hZ2VudA==
)​
-----------------------------------------------------------------

Corrective RAG (CRAG) is a common technique to improve RAG
systems. It introduces a self-assessment step of the retrieved
documents, which helps in retaining the relevance of generated
responses.

Here’s an overview of how it works:

​
* First, search the docs with user query.
* Evaluate if the retrieved context is relevant using LLM.
* Only keep the relevant context.
* Do web search if needed.
* Aggregate the context & generate response.

The video at the top shows how it works!

Here’s our tech stack for this demo:

* ​Firecrawl (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/48hvhehm068wnkux/aHR0cHM6Ly9maXJlY3Jhd2wubGluay9hdmktY2hhd2xh
) for deep web search
* ​Milvus (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/wnh2hghqrx6m3mc7/aHR0cHM6Ly9naXRodWIuY29tL21pbHZ1cy1pby9taWx2dXM=
) to self-host vectorDB.
* ​Beam (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/reh8hohmqwzke4f2/aHR0cHM6Ly9naXRodWIuY29tL2JlYW0tY2xvdWQvYmV0YTkv
) for deployment
* ​Cometml’s Opik (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/08hwh9h2mgrnkecl/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1wcmFjdGljYWwtZ3VpZGUtdG8taW50ZWdyYXRlLWV2YWx1YXRpb24tYW5kLW9ic2VydmFiaWxpdHktaW50by1sbG0tYXBwcy8=
) to trace and monitor
* LlamaIndex workflows for orchestration

Setup LLM
---------

We will use gpt-oss as the LLM, locally served using Ollama.

​

Setup vectorDB
--------------

Our primary source of knowledge is the user documents that we
index and store in a Milvus vectorDB collection.

This will be the first source that will be invoked to fetch
context when the user inputs a query.

​

Set up web search tool
----------------------

If the context obtained from the vector DB isn't relevant, we
resort to web search using Firecrawl.

More specifically, we use the latest v2 endpoint that provides
10x faster scraping, semantic crawling, News & image search, and
more.

​

Tracing and Observability
-------------------------

LlamaIndex also offers a seamless integration with CometML’s
Opik. You can use this to trace every LLM call, monitor, and
evaluate your LLM application.

​

Create the workflow
-------------------

Now that we have everything set up, it's time to create the
event-driven agentic workflow that orchestrates our application.

​
We pass in the LLM, vector index, and web search tool to
initialise the workflow.

Kickoff the workflow
--------------------

Finally, when we have everything ready, we kick off our workflow.

Check this out👇

​

Deployment with Beam
--------------------

Beam enables ultra-fast serverless deployment of any AI workflow.

Thus, we wrap our app in a Streamlit interface, specify the
Python libraries, and the compute specifications for the
container.

Finally, we deploy it in a few lines of code:

​

Run the app
-----------

Beam launches the container and deploys our streamlit app as an
HTTPS server that can be accessed from a web browser.

In the video below, our workflow is able to answer a query that's
unrelated to the document. The evaluation step makes this
possible:

video preview (
https://api.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/o8qDqNFuJPYyvf8DHZTYB8/player
)-->
video preview-->
(
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/8ghqhohogqnwxntk/aHR0cHM6Ly9hcGkuZmlsZWtpdGNkbi5jb20vZS9rN1lIUE4yNFNveHlNOG5HS1puRHhhL284cURxTkZ1SlBZeXZmOERIWlRZQjgvcGxheWVy
)

​
If you want to dive into building LLM apps, our full RAG crash
course discusses RAG from basics to beyond:

* ​RAG fundamentals (
https://click.convertkit-mail2.com/27uprpxd03foh826vk8t3hgq3v344hghgmk33/vqh3hrhonermd7cg/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
)​
*

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
