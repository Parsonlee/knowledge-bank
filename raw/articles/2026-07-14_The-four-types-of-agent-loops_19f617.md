---
title: The four types of agent loops
source_key: dailydoseofds
email_subject: The Four Types of Agent Loops
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Tue, 14 Jul 2026 16:27:49 +0000
email_id: 19f6174c7b5adc67
article_id: 19f6174c7b5adc67:1
published: '2026-07-14'
tags:
- AI-Agent/coding
---

# The four types of agent loops

- **原邮件主题**: The Four Types of Agent Loops
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Tue, 14 Jul 2026 16:27:49 +0000
- **ID**: 19f6174c7b5adc67

---

## [**The four types of agent loops**](<https://fff97757.click.kit-mail3.com/n4uqvqx86whvhxz7pxxc6h673wwnlclhgovww/wnh2hghq20p8wzs7hx/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9sb29wLWVuZ2luZWVyaW5nLWNsZWFybHktZXhwbGFpbmVkLw==>)

Loop engineering keeps getting talked about as one thing, when it’s actually a choice between four structures, each fitting a different kind of task.

It means designing the system that steers the agent, instead of steering it by hand, move by move.

That system always answers two questions: what starts a run, and what decides the work is done.

In a hand-run session, the human answers both, every single time. Each loop type moves more of that into the system.

![](https://substackcdn.com/image/fetch/$s_!pSId!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6296b4b4-3f8c-4d3e-b193-24b456d14b03_960x922.gif)   
---  
  
Here’s each type, what triggers it, and when to reach for it.

\#1) Turn-based loops, triggered by a user prompt.

The agent gathers context, acts, and checks its work inside a single turn. Then a human reviews the output and writes the next prompt.

![](https://substackcdn.com/image/fetch/$s_!-hZp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F03f8a20d-3be6-4667-b9b1-528e817e4ca6_1188x308.png)   
---  
  
Use this when requirements are still forming and every output changes what the next prompt should ask for.

\#2) Goal-based loops, triggered by a /goal command that carries success criteria and a budget, like “get the homepage Lighthouse score to 90, stop after 5 tries.”

When the agent tries to stop, an evaluator model checks whether the goal is met, and it sends it back to work.

![](https://substackcdn.com/image/fetch/$s_!SDSi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc34a00c-adcd-4197-941b-56457404e9e3_1187x236.png)   
---  
  
Use this when the outcome is measurable but the path there doesn’t need human attention.

\#3) Time-based loops, triggered by a clock.

An interval fires, the agent runs a fixed prompt like “check the PR, fix CI,” then waits for the next tick. The /loop command runs on the local machine, and /schedule moves it to the cloud so it survives a closed laptop.

![](https://substackcdn.com/image/fetch/$s_!pA7S!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedda4aa4-0acd-44b6-831a-6e875f9b76a9_1187x228.png)   
---  
  
Use this for recurring work where the task is known in advance and only the timing repeats.

\#4) Proactive loops, triggered by an event or schedule with no human present.

A routine watches a channel and spawns a workflow when something needs handling. That workflow runs a triage agent, a fix agent, and a reviewer who adversarially judges the work before the task closes.

![](https://substackcdn.com/image/fetch/$s_!JiWy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67dc6ddc-7ee4-4a4d-b96d-73b7b1d5943f_1187x275.png)   
---  
  
Use this for standing responsibilities where nobody can predict what will come in, only that something will.

Each type hands off one more job than the last. Turn-based keeps both jobs with the human, goal-based automates the checking, time-based automates the trigger, and proactive automates both while deciding the workflow shape at runtime.

So the mapping question isn’t which loop is most advanced. It’s whether the task is exploratory, measurable, recurring, or standing.

The more you hand off, the less you monitor yourself.

We wrote a full breakdown on loop engineering.

[**You can read it here →**](<https://fff97757.click.kit-mail3.com/n4uqvqx86whvhxz7pxxc6h673wwnlclhgovww/wnh2hghq20p8wzs7hx/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9sb29wLWVuZ2luZWVyaW5nLWNsZWFybHktZXhwbGFpbmVkLw==>)
