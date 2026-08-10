#  6 memory optimization techniques for Agentic systems 

- **原邮件主题**: [Hands-on] Build Semantic Search Inside Your Database Without an Embedding Pipeline
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 07 Aug 2026 20:42:13 +0000
- **ID**: 19fddf64edb10546

---

## [**6 memory optimization techniques for Agentic systems**](<https://www.dailydoseofds.com/ai-agents-crash-course-part-16-with-implementation/>)

We recently added [**Part 16**](<https://www.dailydoseofds.com/ai-agents-crash-course-part-16-with-implementation/>)**** and [**Part 17**](<https://www.dailydoseofds.com/ai-agents-crash-course-part-17-with-implementation/>)**** to our AI Agents crash course**,** where we use LangGraph to implement 6 production-grade memory optimization techniques in agentic workflows.

  * [**You can read Part 16 here →**](<https://www.dailydoseofds.com/ai-agents-crash-course-part-16-with-implementation/>)
  * [**You can read Part 17 here →**](<https://www.dailydoseofds.com/ai-agents-crash-course-part-17-with-implementation/>)

But what exactly is Memory, and why is it so powerful for Agentic systems?

To understand this, consider an Agentic system without Memory (below):

![](https://substackcdn.com/image/fetch/$s_!Lm3M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e04d510-782e-4d64-be8d-f53989346099_2656x1568.png)   
---  
  
  * In iteration #1, the user mentions their favorite color.
  * In iteration #2, the Agent knows nothing about iteration #1.

This means the Agent is mostly stateless, and it has no recall abilities.

But now consider an Agentic system built with Memory (below):

![](https://substackcdn.com/image/fetch/$s_!naVC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19fa4cd6-b689-4b5c-ae9b-547870226a66_2656x1480.png)   
---  
  
  * In iteration #1, the user mentions their favorite color.
  * In iteration #2, the Agent can recall iteration #1.

Memory matters because if a memory-less Agentic system is deployed in production, every interaction with that Agent will be a blank slate.

![](https://substackcdn.com/image/fetch/$s_!6luh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88885543-77fd-4bc6-84fa-c35b5a03a29f_1000x629.png)   
---  
  
It doesn’t matter if the user told the Agent their name five seconds ago, it’s forgotten. If the Agent helped troubleshoot an issue in the last session, it won’t remember any of it now.

With Memory, your Agent becomes context-aware and practically applicable.

But Memory isn’t an abstract concept.

If you dive deeper, it follows a structured and intuitive architecture with several types of Memory.

![](https://substackcdn.com/image/fetch/$s_!Wyy7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2439c514-c2cd-457b-843a-14bcfbec2452_1551x616.png)   
---  
  
  * Short-Term Memory
  * Long-Term Memory
  * Entity Memory
  * Contextual Memory, and
  * User Memory

Each serves a unique purpose in helping agents “remember” and utilize past information.

To simulate memory, the system has to manage context explicitly: choosing what to keep, what to discard, and what to retrieve before each new model call.

![](https://substackcdn.com/image/fetch/$s_!P0BM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7ff1629-c68e-405b-9438-e56640f26ed2_2000x778.png)   
---  
  
This is why memory is not a property of the model itself. It is a system design problem that can also be optimized, and we covered them in these two parts:

  * [**You can read Part 16 with LangGraph →**](<https://www.dailydoseofds.com/ai-agents-crash-course-part-16-with-implementation/>)
  * [**You can read Part 17 with LangGraph →**](<https://www.dailydoseofds.com/ai-agents-crash-course-part-17-with-implementation/>)

Also, Part 8 and Part 9 of the crash course cover memory with CrewAI:

  * [**AI Agents Crash Course Part 8 →**](<https://www.dailydoseofds.com/ai-agents-crash-course-part-8-with-implementation/>)
  * [**AI Agents Crash Course Part 9 →**](<https://www.dailydoseofds.com/ai-agents-crash-course-part-9-with-implementation/>)

Both parts cover:

  * 5 types of Memory from a theoretical, practical, and intuitive perspective.
  * How each type of Memory helps an Agent.
  * How an Agent retrieves relevant details from the Memory.
  * The underlying mechanics of Memory and how it is stored.
  * How to utilize each type of Memory for Agents (implementations).
  * How to customize Memory settings.
  * How to reset the Memory if needed.
  * And more.

