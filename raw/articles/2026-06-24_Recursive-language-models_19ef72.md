---
title: Recursive language models
source_key: dailydoseofds
email_subject: Loop Engineering, Clearly Explained!
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Wed, 24 Jun 2026 00:59:02 +0000
email_id: 19ef7234678feae5
article_id: 19ef7234678feae5:1
published: '2026-06-24'
tags:
- AI-Agent/context-engineering
---

# Recursive language models

- **原邮件主题**: Loop Engineering, Clearly Explained!
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Wed, 24 Jun 2026 00:59:02 +0000
- **ID**: 19ef7234678feae5

---

## **Recursive language models**

LLMs typically become less effective as conversations become longer.

Even if the context fits within the model’s window, performance drops. The model loses its ability to recall and reason over information.

This is called “context rot.”

Researchers from MIT just proposed a fix called Recursive Language Models (RLMs), and it is explained in the visual below:

![](https://substackcdn.com/image/fetch/$s_!05U-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ae6613e-4904-4676-b5e0-e7262c73b838_1277x1142.gif)   
---  
  
Here’s how they work:

In a normal LLM call, you send the query and the full context together. The model processes everything at once.

In an RLM, the context is stored separately as a variable in a Python REPL environment. The model never sees all of it directly.

Instead, it gets access to tools that let it:

![](https://substackcdn.com/image/fetch/$s_!ATuK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccef5110-cc7d-4c56-8735-980b18f831a5_1024x559.png)   
---  
  
  * Peek at portions of the context (like the first 2000 characters)
  * Grep through it using regex or keywords
  * Partition it into smaller chunks
  * Call itself recursively on those chunks

Each recursive call is like a function call in programming. It gets a smaller piece of the problem, solves it, and returns the result to the parent.

Here’s a concrete example:

You have 5,000 customer support tickets. Each has a User ID and a question. You ask: “Among users 12345, 67890, and 11111, how many questions are about billing?”

![](https://substackcdn.com/image/fetch/$s_!QSej!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d2fcc85-d620-462f-afa4-72b7f48788c3_1024x559.png)   
---  
  
A normal LLM receives all 5,000 tickets, tries to scan through everything, gets overwhelmed, and makes counting errors.

Here’s what an RLM does:

![](https://substackcdn.com/image/fetch/$s_!jfXV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F909152f2-f0bf-49fc-8714-e789a1782a61_1024x559.png)   
---  
  
  * Step 1: It peeks at the first few entries to understand the structure.
  * Step 2: It runs a regex filter to grab only lines with the target user IDs. Now it has 50 lines instead of 5,000.
  * Step 3: It spawns a recursive sub-call: “Classify each of these as billing or other.”
  * Step 4: It counts the billing ones and returns the final answer.

The root model’s context window stays small throughout. It only sees its query, its code, and the results from sub-calls.

The results are incredible.

RLM with GPT-5-mini outperformed GPT-5 on challenging long-context benchmarks. More than double the correct answers on some tasks. And cheaper per query.

![](https://substackcdn.com/image/fetch/$s_!7YDX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4654329-c430-4830-941f-8ef1c634753f_3816x1400.png)   
---  
  
At 10M+ tokens, RLMs didn’t degrade. Regular LLM calls fall apart way before that.

Traditional LLMs treat context as a black box to process all at once. RLMs treat context as data to be programmatically explored. The model decides how to decompose the problem on its own.

Interestingly, this approach also mirrors how agentic coding tools like Claude Code already operate.

They peek at file structures, grep through codebases, and only pull relevant snippets into context rather than loading entire repositories at once.

[**You can find the RLM Paper here →**](<https://fff97757.click.kit-mail3.com/lmu9m96v3wcmhn8nzq4s6h8wpev9nsgh32dww/e0hph7h732kedqt8h2/aHR0cHM6Ly9hcnhpdi5vcmcvYWJzLzI1MTIuMjQ2MDF2MQ==>)

If you want to learn more about Sub-agents in Claude Code, we did a hands-on walkthrough a few months back. Continue reading 👇
