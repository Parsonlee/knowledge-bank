---
title: A tricky LLM interview question for AI Engineers
source_key: dailydoseofds
email_subject: How to Beat GRPO Without Touching Model Weights
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Fri, 01 May 2026 22:01:35 +0000
email_id: 19de58fc0d126e4b
article_id: 19de58fc0d126e4b:1
published: '2026-05-01'
tags:
- LLM/arch
- LLM/training/post-train
---

# A tricky LLM interview question for AI Engineers

- **原邮件主题**: How to Beat GRPO Without Touching Model Weights
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 01 May 2026 22:01:35 +0000
- **ID**: 19de58fc0d126e4b

---

## [**A tricky LLM interview question for AI Engineers**](<https://fff97757.click.kit-mail3.com/8ku7d7v34kboh2v2kzkfkhkogw6qxb3hoqxnn/58hvh7hg2qnxvnu6/aHR0cHM6Ly9hcnhpdi5vcmcvYWJzLzI2MDQuMDk3OTE=>)

![](https://substackcdn.com/image/fetch/$s_!f2sB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d13cd79-4c2b-4492-9d4d-52bf14293a85_1080x1080.gif)   
---  
  
You’re fine-tuning a model for Python code generation. The data was generated using the strongest LLMs like Opus/GPT.

But the fine-tuned model performs better when you use a weaker teacher instead.

Why did this happen?

A stronger teacher model can produce worse fine-tuning results. This sounds counterintuitive, but it is a well-documented effect in knowledge distillation research.

Large models solve a basic problem using abstractions, type hints, and patterns.

![](https://substackcdn.com/image/fetch/$s_!Z4TH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a3cd94b-1755-462c-9656-28933bc450ea_851x372.png)   
---  
  
A Qwen3-8B model does not have enough capacity to reproduce those patterns. So instead of learning clean solutions, it learns an approximation of something it cannot fully represent.

However, a weaker teacher solves the same problem correctly, but with simpler patterns that the student can actually replicate.

![](https://substackcdn.com/image/fetch/$s_!ikfv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34418abb-58f0-4dc0-ad55-a453d2da6963_610x259.png)   
---  
  
A [**recent paper from Fastino Labs**](<https://fff97757.click.kit-mail3.com/8ku7d7v34kboh2v2kzkfkhkogw6qxb3hoqxnn/58hvh7hg2qnxvnu6/aHR0cHM6Ly9hcnhpdi5vcmcvYWJzLzI2MDQuMDk3OTE=>) also documented this.

The researchers used Pioneer, their fine-tuning agent that takes a task description, generates training data, selects a base model, runs experiments, and iterates until the model hits a performance target, all without human intervention.

During one of those runs, Pioneer fine-tuned Qwen3-8B on Python code generation.

The agent tried two different teacher models for synthetic data generation: one large frontier model and one smaller model.

  * The frontier model’s data hurt performance.
  * The smaller model’s data performed much better in fewer iterations.

And the fine-tuning Agent was smart enough to catch this behavior. It measured the results from both teachers, saw that the frontier model was making things worse, and dropped it.

![](https://substackcdn.com/image/fetch/$s_!t2Cw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e9d67c2-d11b-4838-bc9c-d8f979ec9591_851x520.png)   
---  
  
A human engineer would likely have defaulted to a bigger model because it is the stronger model, and might not have questioned that choice.

The [**paper**](<https://fff97757.click.kit-mail3.com/8ku7d7v34kboh2v2kzkfkhkogw6qxb3hoqxnn/58hvh7hg2qnxvnu6/aHR0cHM6Ly9hcnhpdi5vcmcvYWJzLzI2MDQuMDk3OTE=>) explains three reasons this happens:

→ Capacity mismatch: The student cannot learn the teacher’s internal representations when the gap is too large. Increasing teacher size first helps, then hurts beyond a certain point.

→ Forgetting pretrained knowledge: Qwen3-8B already knows how to write Python from pretraining. Fine-tuning on a complex coding style from a much larger model can overwrite that existing capability.

→ Over-complexity in training data: A large model will solve “reverse a linked list” with elegant abstractions and comprehensive error handling. That is correct code, but it is also unnecessary complexity for the task. A simpler teacher generates solutions that match the task’s actual complexity, and the student learns them cleanly.

As a takeaway, always match the teacher to the student’s capacity and the task’s complexity.

To fine-tune a 3B or 8B model on a well-defined task, a mid-tier teacher will often produce better training data than powerful one.

[**You can find the paper here →**](<https://fff97757.click.kit-mail3.com/8ku7d7v34kboh2v2kzkfkhkogw6qxb3hoqxnn/58hvh7hg2qnxvnu6/aHR0cHM6Ly9hcnhpdi5vcmcvYWJzLzI2MDQuMDk3OTE=>)
