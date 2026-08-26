---
title: 6 components of context engineering
source_key: dailydoseofds
email_subject: The AI Engineering Master Stack for 2026!
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Thu, 25 Jun 2026 21:49:30 +0000
email_id: 19f00c2716d4e27d
article_id: 19f00c2716d4e27d:1
published: '2026-06-25'
tags:
- AI-Agent/context-engineering
---

# 6 components of context engineering

- **原邮件主题**: The AI Engineering Master Stack for 2026!
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Thu, 25 Jun 2026 21:49:30 +0000
- **ID**: 19f00c2716d4e27d

---

## **6 components of context engineering**

Here’s rough math on what determines your AI app’s output quality:

![](https://substackcdn.com/image/fetch/$s_!NsBY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F733113ce-f515-4f91-a7e5-0f2ef4822869_2008x751.png)   
---  
  
  * Model selection: 15%
  * Prompt: 10%
  * Everything else (retrieval, memory, tools, query handling): 75%

We’ve seen teams obsessing over the wrong 25% when the actual problem lies elsewhere.

And this is exactly why “context engineering” has quietly become the most important skill in AI engineering today.

It’s the art of getting the right information to the model at the right time in the right format.

And it has 6 core components, as depicted in the visual below:

![](https://substackcdn.com/image/fetch/$s_!YA0s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9cf66394-2d29-4ecf-80ab-55deb54dc559_1280x968.gif)   
---  
  
#### **Prompting techniques**

This is where most people stop. But even here, there’s more depth than people realize.

Classic prompting is about pattern recognition. You give the model examples, and it learns the format, style, and logic you want. Few-shot prompting still works remarkably well for structured tasks.

But advanced prompting is where things get interesting.

![](https://substackcdn.com/image/fetch/$s_!wwXj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d2733c3-db89-4900-a596-7551248233e5_994x201.gif)   
---  
  
Techniques like Chain-of-thought prompting give the model thinking room. Instead of jumping straight to an answer, you ask it to reason step-by-step. This simple change can dramatically improve accuracy on complex problems.

#### **Query augmentation**

Users are lazy in writing queries.

When someone types “How do I make this work when my API call keeps failing?”, that’s almost useless to a retrieval system.

Query augmentation fixes this through several techniques:

![](https://substackcdn.com/image/fetch/$s_!zL_P!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd19ad755-521e-40e5-bfd0-4806f21ec5f7_1024x559.png)   
---  
  
  * Query Rewriting: An LLM takes that vague question and transforms it.
  * Query Expansion: Adding related terms and synonyms to cast a wider net.
  * Query Decomposition: Breaking a complex question into sub-questions that can be answered independently.
  * Query Agents: Using an agent to dynamically decide how to reformulate the query based on initial results.

#### Long-term memory

Say an agent has a great conversation with a user. The user shared preferences, context, and history. But as the session ends, it’s all gone.

Long-term memory fixes this with external storage:

![](https://substackcdn.com/image/fetch/$s_!9ys0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c345a35-7c26-40ad-bafe-3cb9b396a319_1478x1371.gif)   
---  
  
  * Vector Databases: Store embeddings of past interactions for semantic search.
  * Graph Databases: Store conversations as relationships and entities.

The type of memory matters too:

  * Episodic memory signifies specific events
  * Semantic memory maintains general facts about the user, and
  * Procedural memory handles how the user likes things done.

Open-source tools like [**Zep Graphiti**](<https://fff97757.click.kit-mail3.com/0vueve7zg6h9h93wxkmalhv7nwevotnh9n5ll/reh8hohml5g4mzi2h6/aHR0cHM6Ly9naXRodWIuY29tL2dldHplcC9ncmFwaGl0aQ==>) make this accessible, and you don’t need to build from scratch.

#### Short-term memory

Short-term memory is simply the conversation history. This one seems obvious, but it’s often mismanaged.

And here’s where teams mess up:

  * Stuffing too much into the context window (noise drowns out signal)
  * Not including enough (model lacks critical information)
  * Poor ordering (important context buried at the end)
  * No summarization strategy for long conversations

#### **Knowledge base retrieval**

Most teams think about this as RAG, but that’s too narrow. RAG is one pattern, not the whole picture.

The real question is: How do you connect your AI to your organization’s data?

That knowledge lives everywhere, like: docs, wikis, databases, SaaS tools like Notion and Google Drive, APIs, and code repositories.

![](https://substackcdn.com/image/fetch/$s_!TOwO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F351b396c-aca5-46f9-9f98-0fa8541e764c_957x266.png)   
---  
  
The retrieval pipeline has three layers:

  * Pre-Retrieval: How do you chunk docs? What metadata do you preserve? How do you handle tables and structured data? How do you keep everything in sync?
  * Retrieval: Which embedding model? Which retrieval strategy do you use: Vector search or hybrid with BM25? How do you re-rank?
  * Augmentation: How do you format retrieved context, include citations, handle contradictions, etc?

Open-source tooling like [**Airweave**](<https://fff97757.click.kit-mail3.com/0vueve7zg6h9h93wxkmalhv7nwevotnh9n5ll/08hwh9h2673v25ulh5/aHR0cHM6Ly9naXRodWIuY29tL2FpcndlYXZlLWFpL2FpcndlYXZl>) solves this end-to-end. Instead of building custom connectors for every data source, you can sync your knowledge bases and get unified access to Notion, Google Drive, databases, and more.

![](https://substackcdn.com/image/fetch/$s_!Onav!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3275ca7-7198-4d6c-be2f-a60c0edad4d2_960x955.gif)   
---  
  
You can get 10x improvements in retrieval quality without changing the model, but by just fixing the chunking strategy or properly syncing knowledge sources.

#### **Tools and agents**

A tool extends what the model can do because, without it, the model is stuck with just what’s in its weights and context window.

Moreover, an agent decides when and how to use those tools.

The basic loop looks like this: Query → Thought → Action → Observation → (repeat until goal satisfied) → Response

![](https://substackcdn.com/image/fetch/$s_!vjUR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c38b38e-7c30-4a2e-a39f-a023d6092076_1024x559.png)   
---  
  
  * Single-agent architecture works for straightforward tasks. Most chatbots and copilots fall into this category.
  * A multi-agent architecture is better for complex workflows. You have specialized agents that collaborate. One does research, another writes, another critiques. They hand off work to each other.

[**MCPs**](<https://fff97757.click.kit-mail3.com/0vueve7zg6h9h93wxkmalhv7nwevotnh9n5ll/8ghqhoho65mzo6hkh9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0xLw==>) take this to the next step!

[![](https://substackcdn.com/image/fetch/$s_!qN27!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40f3cb2a-84b5-4556-8bcc-026f43f393d9_1024x559.png)](<https://fff97757.click.kit-mail3.com/0vueve7zg6h9h93wxkmalhv7nwevotnh9n5ll/vqh3hrho9kzlozughl/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXFOMjchLGZfYXV0byxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRjQwZjNjYjJhLTg0YjUtNDU1Ni04YmNjLTAyNmY0M2YzOTNkOV8xMDI0eDU1OS5wbmc=>)  
---  
  
  * Traditional tool integration requires N×M connections. If you have 3 models and 4 tools, you need 12 integration points.
  * MCP changes this to N+M. Models and tools both connect to a standard protocol layer.

* * *

Some time back, prompt engineering made it sound like the magic was in crafting the perfect instruction.

Context engineering recognized that the real gains lie in the entire info pipeline instead:

  * What context do you provide?
  * Where does that context come from?
  * How is it retrieved, filtered, and formatted?
  * What can the model do with tools?
  * What does it remember across sessions?

👉 Over to you: How are you building your Agentic systems?
