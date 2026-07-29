---
title: [Hands-on] Deploy and Run LLMs on your Phone!
source: https://mail.google.com/mail/u/0/#inbox/19b522575aa6f7ef
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-24
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 [Hands-on] Deploy and Run LLMs on your Phone! 的原理剖析与工程实践。
tags:
  - clippings
---

# [Hands-on] Deploy and Run LLMs on your Phone!

## 1. 核心要点解析

本期内容重点涵盖：
- **[Hands-on] Deploy and Run LLMs on your Phone!**

## 2. 深度拆解与正文翻译

​Master full-stack AI Engineering (
https://fff97757.click.convertkit-mail2.com/e5unmnq5evf7hl58pvri8h8mgnw22blhvzgnn/6qheh8hl020g87co/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Build a podcast generator with MiniMax’s latest M2.1.
* [Hands-on] Deploy and Run LLMs on your Phone!
* AI Agent Tech Stack!

TODAY'S ISSUE

LLM update
----------

-----------------------------------------------------------------
​Build a podcast generator with MiniMax’s latest M2.1 (
https://fff97757.click.convertkit-mail2.com/e5unmnq5evf7hl58pvri8h8mgnw22blhvzgnn/kkhmh6hn494q0nil/aHR0cHM6Ly93d3cubWluaW1heC5pby9uZXdzL21pbmltYXgtbTIx
)​
-----------------------------------------------------------------

​MiniMax just dropped M2.1 (
https://fff97757.click.convertkit-mail2.com/e5unmnq5evf7hl58pvri8h8mgnw22blhvzgnn/kkhmh6hn494q0nil/aHR0cHM6Ly93d3cubWluaW1heC5pby9uZXdzL21pbmltYXgtbTIx
), and devs are calling it “Claude at 10% the cost.”

* 72.5% SWE-Multilingual. Beats Sonnet 4.5
* 88.6% VIBE-bench. Beats Gemini 3 Pro

We used it to build an AI studio that turns any website into a
podcast, and have detailed the process in this video:

video preview (
https://api.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/or6ebM85DECgLqgcLccBXB/player
)-->
video preview-->
(
https://fff97757.click.convertkit-mail2.com/e5unmnq5evf7hl58pvri8h8mgnw22blhvzgnn/58hvh7hgl9l8dkc6/aHR0cHM6Ly9hcGkuZmlsZWtpdGNkbi5jb20vZS9rN1lIUE4yNFNveHlNOG5HS1puRHhhL29yNmViTTg1REVDZ0xxZ2NMY2NCWEIvcGxheWVy
)

​
Here’s how it works:

* You provide a website URL
* Firecrawl scrapes the content
* MiniMax M2.1 refines it and generates a podcast script
* Speech 2.6 turns this into a multi-speaker podcast

​You can find more details in the official announcement blog here
→ (
https://fff97757.click.convertkit-mail2.com/e5unmnq5evf7hl58pvri8h8mgnw22blhvzgnn/kkhmh6hn494q0nil/aHR0cHM6Ly93d3cubWluaW1heC5pby9uZXdzL21pbmltYXgtbTIx
)​

​And you find the code for this demo here → (
https://fff97757.click.convertkit-mail2.com/e5unmnq5evf7hl58pvri8h8mgnw22blhvzgnn/25h2hoh3nonzpdi3/aHR0cHM6Ly9naXRodWIuY29tL3BhdGNoeTYzMS9haS1lbmdpbmVlcmluZy1odWIvdHJlZS9tYWluL2FpLXBvZGNhc3QtZ2VuZXJhdG9y
)​

hands-on
--------

-----------------------------------------------------------------
​[Hands-on] Deploy and Run LLMs on your Phone! (
https://fff97757.click.convertkit-mail2.com/e5unmnq5evf7hl58pvri8h8mgnw22blhvzgnn/qvh8h7hdq6q5mqbl/aHR0cHM6Ly9kb2NzLnVuc2xvdGguYWkvbmV3L2RlcGxveS1sbG1zLXBob25l
)​
-----------------------------------------------------------------

​
You can now fine-tune LLMs and deploy them directly on your
phone.

Today, we are covering a step-by-step guide that shows how to
fine-tune Qwen3 and then export it to a mobile-ready format,
which can then run 100% locally on your iOS or Android device.

We’ll use:

* ​UnslothAI (
https://fff97757.click.convertkit-mail2.com/e5unmnq5evf7hl58pvri8h8mgnw22blhvzgnn/qvh8h7hdq6q5mqbl/aHR0cHM6Ly9kb2NzLnVuc2xvdGguYWkvbmV3L2RlcGxveS1sbG1zLXBob25l
) for fine-tuning
* TorchAO for phone-friendly quantization
* ExecuTorch to run it on iOS

Let’s begin!

1️⃣ Load the model
------------------

First, we load Qwen3-0.6B in phone-deployment mode.

This enables quantization-aware training, so everything stays
compatible with mobile export later.

​

2️⃣ Load datasets
-----------------

Next, we decide what the model should learn.

​
We load:

* a reasoning dataset for enhanced capabilities
* a chat dataset so it behaves like an assistant

At this point, both datasets are still raw.

3️⃣ Convert reasoning data
--------------------------

​
Now we convert the reasoning data into user → assistant
conversations.

This teaches the model how to reason, not just the final answer.

4️⃣ Standardize chat data
-------------------------

Next, we convert them to the chat dataset format.

​
This ensures both datasets follow the same schema. At this point,
reasoning and chat data look identical to the model.

5️⃣ Mix datasets
----------------

​
Now, we decide how much the model should reason versus chat.

We keep 75% reasoning so the model can think, and 25% chat so it
talks naturally.

This gives us one clean dataset that does both.

6️⃣ Train the model
-------------------

​
Next, we set up the trainer and start fine-tuning.

We keep the run short so we can move quickly to mobile export.

Here, the loss decreases, indicating that the model is being
trained correctly.

​

7️⃣ Save the model
------------------

Once training finishes, we save the model in TorchAO format.

This is exactly what ExecuTorch expects next.

​

8️⃣ Export to .pte
------------------

Now we export a single .pte file that iOS can load.

​
Here, we do three things:

* convert weights
* fetch the model config
* Export the final artifact

Note: the .pte file is ~470 MB, which is expected for on-device
models.

9️⃣ Run on iOS
--------------

Finally, we run the model with the ExecuTorch iOS demo app.

On the Simulator, we copy the .pte and tokenizer, load them in
the app, and start chatting.

The Simulator needs no developer account. Physical iPhones
require an increased memory limit in Xcode.

video preview (
https://api.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/p3wcwxJXih7t7GYEMcrrxr/player
)-->
video preview-->
(
https://fff97757.click.convertkit-mail2.com/e5unmnq5evf7hl58pvri8h8mgnw22blhvzgnn/g3hnh5hmxzx58gcr/aHR0cHM6Ly9hcGkuZmlsZWtpdGNkbi5jb20vZS9rN1lIUE4yNFNveHlNOG5HS1puRHhhL3Azd2N3eEpYaWg3dDdHWUVNY3JyeHIvcGxheWVy
)

​
In the above video, we have Qwen3 running locally on an iPhone 17
Pro at ~25 tokens/s, powered by the same ExecuTorch runtime used
in production across Meta apps like Instagram, WhatsApp, and
Messenger.

​Here is the colab notebook for the complete code → (
https://fff97757.click.convertkit-mail2.

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
