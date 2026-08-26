---
title: Agent memory and state are not the same thing!
source_key: dailydoseofds
email_subject: Graph Engineering Clearly Explained
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Mon, 27 Jul 2026 21:22:34 +0000
email_id: 19fa5754b2a0ee28
article_id: 19fa5754b2a0ee28:1
published: '2026-07-27'
tags:
- AI-Agent/coding
- Skill/python
---

# Agent memory and state are not the same thing!

- **原邮件主题**: Graph Engineering Clearly Explained
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Mon, 27 Jul 2026 21:22:34 +0000
- **ID**: 19fa5754b2a0ee28

---

## [**Agent memory and state are not the same thing!**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/48hvhehm42e207uxh7/aHR0cHM6Ly9naXRodWIuY29tL2NyZXdBSUluYy9jcmV3QUk=>)

If an agent forgets something it has already learned, that’s a memory problem. If it forgets where it was in the middle of a task and starts over, that’s a state problem.

We once killed one of our agents mid-task to test something else, and it started over like the execution so far never happened.

That’s when it clicked that we’d been treating two different problems as one.

![](https://substackcdn.com/image/fetch/$s_!Lzo1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F106d2285-d15a-448a-a41a-8af78537eca3_1199x654.png)   
---  
  
State is tied to the current run as to what task the agent is working on and what it’s already found.

None of that exists unless something writes it down.

The fix was to add a checkpoint after every completed step that records the agent’s progress, so if the process dies, it resumes from that exact point instead of starting from scratch.

Memory is a different thing entirely. It’s what survives across runs as facts, lessons, and findings that are worth retaining.

![](https://substackcdn.com/image/fetch/$s_!ikeR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05413595-9081-4608-b60c-74fd3c4f90e0_1199x654.png)   
---  
  
At first, we had one shared memory for all our agents and assumed that was enough. But it wasn’t until our agents started reading each other’s findings and treating them as their own.

That’s why giving each agent its own memory scope is important with `memory = memory.scope(”/agent”)`.

![](https://substackcdn.com/image/fetch/$s_!QU09!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1aaf3481-1c6f-4f39-80c6-a3ffc4e7ffa0_1312x1034.gif)   
---  
  
Once we separated state from memory, everything became much easier to reason about.

Here’s what the final Agent Harness looks like:

![](https://substackcdn.com/image/fetch/$s_!Sgx8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3efbbc7-24b4-4c59-965d-6c3d3fc3c694_1200x1200.png)   
---  
  
  * separate memory from state as two different problems
  * scope memory per agent when findings shouldn’t be shared
  * write a checkpoint after every completed task
  * resume interrupted runs from the last checkpoint
  * fork a checkpoint into a new branch without redoing previous work

This is the harness baseline to build any agent. It’s enough for general-purpose workflows, but coding agents and long-running systems need other layers along.

We wrote an article that builds that next layer from scratch. It walks through planning, the agent loop, subagents, sandboxing, memory, and checkpointing, one layer at a time.

![](https://substackcdn.com/image/fetch/$s_!h9iO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd523746-97c0-452b-8231-cbbad3c98d25_1199x654.png)   
---  
  
The whole thing is built with [**CrewAI**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/48hvhehm42e207uxh7/aHR0cHM6Ly9naXRodWIuY29tL2NyZXdBSUluYy9jcmV3QUk=>), a 100% open-source framework.

[**You can read the article here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8m2lvrf3hgrqednzbghgmk33/wnh2hghqeopordc7hx/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9oYW5kcy1vbi1yZWJ1aWxkaW5nLWNsYXVkZS1jb2Rlcy1oYXJuZXNzLw==>)
