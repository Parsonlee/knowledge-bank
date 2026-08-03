# Graph engineering clearly explained

- **原邮件主题**: Graph Engineering Clearly Explained
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Mon, 27 Jul 2026 21:22:34 +0000
- **ID**: 19fa5754b2a0ee28

---

## **Graph engineering clearly explained**

The moment you have several loops that need to work together, you have a coordination problem, and graphs are how engineers have always described coordination.

That’s the whole idea behind graph engineering that Peter Steinberger mentioned a few days back.

![](https://substackcdn.com/image/fetch/$s_!q7v_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffc0aa84-7847-46ff-86bf-d415cdc4d7ef_680x351.png)   
---  
  
Today, let’s understand what exactly graph engineering is!

#### First, the graph itself

A graph is three things.

  * **Nodes** are units of work, whether that’s an agent, a plain model call, a deterministic function, a tool, or a human approving something.
  * **Edges** decide what runs next, either in sequence, in parallel, or conditionally based on what the last node produced.
  * **State** is a shared object that flows along the edges. Every node reads from it and writes to it.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/9AjJ5NxKcD29CmR2GjDGyX/email)   
---  
  
This is the starter graph almost every example uses. A researcher gathers material, a writer drafts, and a reviewer judges. If the review passes, the run ends. If it fails, an edge sends the draft back to the writer.

There are three nodes and four edges, and one of those edges forms a loop.

But here’s what reframes everything. A single agent loop is just a one-node graph with an edge pointing back to itself.

![](https://substackcdn.com/image/fetch/$s_!98QA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe589e33c-f0d4-485c-ba4e-bc6af73817bc_680x406.png)   
---  
  
Graphs don’t replace loops but rather connect and govern them.

#### The stack kept growing

The center of gravity in AI keeps drifting away from the model, and each shift picked up a name.

![](https://substackcdn.com/image/fetch/$s_!IvOP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F918bb549-8ca4-40ba-b9eb-99a6f0609033_1294x1294.png)   
---  
  
  * **Prompt engineering** → The words you send.
  * **Context engineering** → Everything the model sees, not just your instructions.
  * **Harness engineering** → The code around the model that runs tools, tracks state, and handles errors.
  * **Loop engineering** → The autonomous cycle that drives one agent toward a goal.
  * **Graph engineering** → The coordination layer across many loops, covering what runs when, in what order, and who checks whom.

Each layer wraps the one before it:

A graph is made of loops, each loop needs a good harness, each harness call is a context problem, and every context contains prompts.

If you skip a lower layer, the graph just fails in a more elaborate way.

![](https://substackcdn.com/image/fetch/$s_!ZDtU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F164cbf4f-3e7e-4fab-9aeb-117f6253e01c_679x450.png)   
---  
  
Of course, none of this is new technology.

LangGraph shipped this exact model involving nodes and edges over shared state back in January 2024.

Microsoft’s AutoGen has GraphFlow, and Google built ADK 2.0’s entire workflow runtime on the same idea.

So while the name is new, the practice isn’t. In fact, the discipline isn’t inventing graphs but rather knowing when to use one, and how to keep it from rotting.

That part has four hard problems.

#### Hard part 1: knowing when a node deserves to exist

The most common failure is turning “summarize this PDF” into a five-node graph with a fetcher, a chunker, a summarizer, a reviewer, and a formatter.

A node earns its place only if it represents a real specialty, meaning a different model, a different toolset, or a genuinely separate role like a read-only reviewer. Steps you could inline into an existing loop are not nodes.

A useful filter is that if you can’t draw the graph on a napkin, it’s too complex. And if collapsing two nodes into one loses nothing, they were never two nodes.

#### Hard part 2: keeping shared state clean

In a loop, the failure mode is context rot.

In a graph, the same problem moves into a shared state.

Every node writes to the state object, so an uninformed write in node two will become a confident input for node five.

Nobody notices until the output is wrong, and by then, the bad data has flowed through half the system.

![](https://substackcdn.com/image/fetch/$s_!2o-f!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F137efd9c-5304-4ca6-a332-1a0456e80e7e_679x374.png)   
---  
  
The solutions are simple and boring, yet effective:

  * Give the state a typed schema.
  * Decide explicitly which nodes may write to which fields.
  * Checkpoint state between nodes so you can replay a run and see exactly where it went bad.

One caution applies to replays though.

Nodes after a checkpoint execute again, so any node with external side effects, like sending an email or creating a record, must be safe to run twice.

#### Hard part 3: routing you can trust

An edge is a decision, and the question is who makes it.

If a model decides the route, you get flexibility and instability together.

The same state can take different paths on different runs, which makes debugging miserable.

_Google’s design rule for ADK 2.0 is the cleanest position in the discourse. Deterministic code should control predictable routing, and models should only handle the steps that need actual judgment._

Route with code wherever the condition is checkable, and spend model calls only where interpretation is genuinely required.

#### Hard part 4: agents agreeing with each other

Loop engineering’s sharpest rule was to never let an agent grade its own homework.

Graphs raise these stakes.

If you have 20 agents built on the same base model and all are reading the same flawed context, then they will happily agree with each other, and models measurably prefer their own outputs. 

You can fix this with a reviewer node that runs on a different model, give it fresh context instead of the full conversation, and anchor its verdict to evidence the graph can’t fabricate, like tests that actually ran or code that actually compiled.

![](https://substackcdn.com/image/fetch/$s_!IqPs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F963892de-133d-4774-a859-4d3c77a1a2eb_679x410.png)   
---  
  
_Note: Cognition landed in the same place after a year of running Devin, their coding agent. Their working setup lets several agents read the work and weigh in, but only one agent is ever allowed to change anything._

Reading is safe to do in parallel, because a bad opinion costs you nothing until someone acts on it. Writing is where the damage happens, so you keep it in one place where you can see it.

#### Where the graph is an overkill

Most of the time.

Anthropic’s own numbers suggest this.

A single agent burns roughly 4x the tokens of a chat interaction, and multi-agent systems burn roughly 15x.

Every node you add multiplies that.

![](https://substackcdn.com/image/fetch/$s_!8C8B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe6cd162-18c4-4c3e-bbe5-e8e2656938e9_679x481.png)   
---  
  
Anthropic’s multi-agent research system outperformed a single Opus agent by 90.2% on their internal research eval, because research fans out into independent searches naturally.

But their standing advice from Building Effective Agents hasn’t changed. Find the simplest solution possible, and only add complexity when the task demands it.

_Even LangGraph’s own guidance says that if your agent is a straightforward loop with tools, LangGraph is overkill._

The decision rule is pretty straightforward: Reach for a graph when the work splits into genuine specialties, needs parallel fan-out and join, needs different models per step, or needs failure isolation and auditable routing. Otherwise, stay in the loop.

#### Where to start

You don’t need an org chart of agents on day one. Build up to it.

  * Master a single loop first, with brakes, a real completion check, and a critic. A graph of weak loops is just a distributed failure.
  * Draw the graph on paper before writing code, and challenge every node to justify its existence.
  * Define the state schema and write access up front. State drift is the main way graphs rot.
  * Make the reviewer node a different model with fresh context, and anchor it to external evidence.
  * Put budget caps on every node. A graph has many loops spending tokens in parallel, and a weak verifier now burns money concurrently.

#### Key takeaway

Graph engineering isn’t a new discipline replacing loop engineering. It’s the name that stuck for a decision every agent builder eventually faces. When one loop stops being enough, coordination becomes the engineering.

The word may not survive the year. The design question will.

Here’s a summary of key takeaways in graph engineering.

![](https://substackcdn.com/image/fetch/$s_!yS0D!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42aac678-f4e2-459f-a8c2-223f8a2db6a2_680x428.png)   
---
