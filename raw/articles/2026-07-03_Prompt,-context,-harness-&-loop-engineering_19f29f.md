# Prompt, context, harness & loop engineering

- **原邮件主题**: Prompt, Context, Harness & Loop Engineering
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 03 Jul 2026 21:51:22 +0000
- **ID**: 19f29f70428b228f

---

## [**Prompt, context, harness & loop engineering**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8kdnera3hg95p5nrighgmk33/8ghqhoho6krx3vikh9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9sb29wLWVuZ2luZWVyaW5nLWNsZWFybHktZXhwbGFpbmVkLw==>)

At its core, an agent is a while loop:

![](https://substackcdn.com/image/fetch/$s_!v7ER!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43aa720f-b498-4bfc-9c78-182941430581_1376x540.jpeg)   
---  
  
  * The model runs
  * It requests tool calls
  * The tool results return to the context
  * The model runs again until it stops requesting tools

ReAct described this form of loop back in 2022-23, and almost every agent/framework runs a similar implementation of this ([**we implemented ReAct from scratch in pure Python here**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8kdnera3hg95p5nrighgmk33/vqh3hrho98wd49fghl/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYWktYWdlbnRzLWNyYXNoLWNvdXJzZS1wYXJ0LTEwLXdpdGgtaW1wbGVtZW50YXRpb24v>)).

But this whole loop wraps four layers of engineering around it:

  * Prompt engineering
  * Context engineering
  * Harness engineering
  * Loop engineering

![](https://substackcdn.com/image/fetch/$s_!bdCF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a5a6d38-30f6-4b7f-bb1f-88e15d536f06_1294x1294.png)   
---  
  
Each one wraps the last, and the model sits in the middle, so none of them compete with the others. Instead, they just zoom one level further out.

#### [Prompt engineering:](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8kdnera3hg95p5nrighgmk33/l2hehmhlmwxz48a6h0/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbGxtb3BzLWNyYXNoLWNvdXJzZS1wYXJ0LTUv>)

This defines the input the model sees on one call, often composed of a role, instructions, examples, and an output format.

The techniques here alter the internal computation and reasoning the model goes through due to the wording it sees:

![](https://substackcdn.com/image/fetch/$s_!5XWH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac4ffdb4-a6e6-42d0-bda8-d3f34c488883_1300x1080.jpeg)   
---  
  
  * Chain-of-thought makes it work in steps before answering
  * Few-shot examples define the format and the edge cases
  * A JSON schema or XML tags make the output parseable by code
  * Self-consistency samples a few chains and takes the majority

#### [Context engineering:](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8kdnera3hg95p5nrighgmk33/m2h7h5h36w4794imhq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbGxtb3BzLWNyYXNoLWNvdXJzZS1wYXJ0LTYv>)

It’s everything the model sees on a turn, not just the prompt. That includes the query, retrieved docs, memory, prior turns, and tool outputs from earlier steps.

![](https://substackcdn.com/image/fetch/$s_!q_63!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb03483bf-8b3d-432e-acf6-43176e9ae06a_1080x1080.gif)   
---  
  
The window is finite and fills up fast, so the engineering work is to rank inputs and cut everything that isn’t pulling weight.

You do this by:

  * Retrieving only the chunks relevant to the query, then reranking them
  * Keeping key facts out of the middle, where accuracy drops
  * Summarizing old turns, evict stale outputs, push big blobs to files

#### [Harness engineering:](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8kdnera3hg95p5nrighgmk33/dpheh0he9rpmk2fmh4/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC90aGUtYW5hdG9teS1vZi1hbi1hZ2VudC1oYXJuZXNzLw==>)

It’s the code around the model that defines the tools, parses the calls, retries on failure, and can route work to sub-agents so one handles retrieval and another handles code.

![](https://substackcdn.com/image/fetch/$s_!cGdx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd913227d-857c-4771-a345-170b32bfa3bf_1200x1200.png)   
---  
  
A verifier then grades the result by running tests, validating a schema, etc.

Prompt and context involve getting one call right. The harness involves everything that has to happen around that call for it to run in a real system.

#### [Loop engineering:](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8kdnera3hg95p5nrighgmk33/8ghqhoho6krx3vikh9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9sb29wLWVuZ2luZWVyaW5nLWNsZWFybHktZXhwbGFpbmVkLw==>)

In the usual setup, you manage the outer loop, i.e, you write a prompt, read the turns the agent runs, write the next prompt, and repeat, while catching failures.

This layer hands that job to the agent itself. It kicks off on a schedule or an event, and runs many turns with no prompt in between.

![](https://substackcdn.com/image/fetch/$s_!ZK2o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb52d8006-5880-450c-8414-37ac67bb877f_2400x1650.jpeg)   
---  
  
A loop inherently doesn’t know when it’s finished. An agent can report that it’s done and halt while the tests still fail. So the stop can’t be the agent’s word, but rather it has to be a real signal, like:

  * A turn and token cap to stop stuck runs
  * A no-progress detector to catch repeated calls
  * A completion check to verify the goal with a separate model or a deterministic test

By this layer, you’re operating on the whole run, so the engineering moves from writing each prompt to setting the goal and the stop conditions up front and letting it run.

If you want to dive deeper into loop engineering, we wrote [**a full breakdown of loop engineering**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8kdnera3hg95p5nrighgmk33/8ghqhoho6krx3vikh9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9sb29wLWVuZ2luZWVyaW5nLWNsZWFybHktZXhwbGFpbmVkLw==>) recently.

It goes from the basic while loop to a run that finishes on its own, with the code behind each part, and the parts that are hard to get right, like knowing when to stop, context rot over a long run, and keeping the checker separate from the maker.

[**Read it here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8kdnera3hg95p5nrighgmk33/8ghqhoho6krx3vikh9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9sb29wLWVuZ2luZWVyaW5nLWNsZWFybHktZXhwbGFpbmVkLw==>)
