---
title: What are RL environments, and how to build them
source_key: dailydoseofds
email_subject: How to Actually Use Train, Validation, and Test Sets in ML
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Fri, 13 Mar 2026 22:04:43 +0000
email_id: 19ce93b00b8a14f0
article_id: 19ce93b00b8a14f0:1
published: '2026-03-13'
tags:
- LLM/training/RL
- AI-Agent/coding
- LLM/training
---

# What are RL environments, and how to build them

- **原邮件主题**: How to Actually Use Train, Validation, and Test Sets in ML
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 13 Mar 2026 22:04:43 +0000
- **ID**: 19ce93b00b8a14f0

---

## [**What are RL environments, and how to build them**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2m7wzripu4pxp99eu7h64xll/qvh8h7hdwg5nl2il/aHR0cHM6Ly91bnNsb3RoLmFpL2Jsb2cvcmwtZW52aXJvbm1lbnRz>)

The real bottleneck in building AI agents that need to reason across multiple steps isn’t the training algorithm.

It’s the environment your agent trains in.

This is because training algorithms like GRPO or PPO are essentially optimizers. They take a reward signal and update model weights to maximize it.

![](https://substackcdn.com/image/fetch/$s_!OYJy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5270997c-91ee-4d09-989d-12d337cc9237_1108x615.png)   
---  
  
The hard part is everything that comes before that, like defining what "better" actually means for your agent, building the infrastructure to generate thousands of parallel rollouts, managing isolated session state across multi-turn interactions, and designing verification logic that reliably scores agent behavior.

And unlike single-turn fine-tuning, where you just need input-output pairs, agentic RL requires your environment to handle tool calls, maintain state across steps, spin up sandboxed execution contexts, and clean up resources after every rollout.

![](https://substackcdn.com/image/fetch/$s_!Z8vJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F844abf4c-9a3c-4d65-9b4a-24bf25f51402_1108x602.png)   
---  
  
Most RL workflows today tightly couple this logic into the training pipeline, which makes it painful to iterate on environment design without touching the optimizer code. That tight coupling is exactly what slows teams down.

Unsloth and NVIDIA have published [**a deep dive on building RL environments for agentic AI**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2m7wzripu4pxp99eu7h64xll/qvh8h7hdwg5nl2il/aHR0cHM6Ly91bnNsb3RoLmFpL2Jsb2cvcmwtZW52aXJvbm1lbnRz>).

![](https://substackcdn.com/image/fetch/$s_!9p2T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf624d46-8019-4d9f-bb7c-b8dcfd97df5d_1957x2300.png)   
---  
  
The post covers how NVIDIA NeMo Gym lets you decouple environment logic from training, so you can design verifiable reward signals independently of your optimizer.

It also walks through the full stack of building an environment, including agent servers for orchestrating rollouts, resource servers for maintaining session state, and verification logic for computing rewards.

Unsloth plugs in as the training backend, consuming rollout trajectories and running GRPO to update model weights efficiently.

[**You can read it here →**](<https://fff97757.click.kit-mail3.com/38u030zrokckh2m7wzripu4pxp99eu7h64xll/qvh8h7hdwg5nl2il/aHR0cHM6Ly91bnNsb3RoLmFpL2Jsb2cvcmwtZW52aXJvbm1lbnRz>)
