---
title: 6 automatic optimization methods for LLM systems
source_key: dailydoseofds
email_subject: 6 Automatic Optimization Methods for LLM Systems
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Fri, 31 Jul 2026 20:49:06 +0000
email_id: 19fb9f018f6c5eda
article_id: 19fb9f018f6c5eda:1
published: '2026-07-31'
tags:
- LLM/arch
- Skill/data-analysis
- AI-Agent/prompt-engineering
---

# 6 automatic optimization methods for LLM systems

- **原邮件主题**: 6 Automatic Optimization Methods for LLM Systems
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 31 Jul 2026 20:49:06 +0000
- **ID**: 19fb9f018f6c5eda

---

## [**6 automatic optimization methods for LLM systems**](<https://fff97757.click.kit-mail3.com/v8uqlqw04vhrhvw8lw8ighvz3og4oi9hpqloo/m2h7h5h3d3rqm7imhq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbGxtb3BzLWNyYXNoLWNvdXJzZS1wYXJ0LTEv>)

Tuning an AI system no longer means training it.

Several methods now improve a system by editing its text, the prompt, the code, sometimes the training loop itself, and all of it runs automatically.

The visual below depicts several such methods:

![](https://substackcdn.com/image/fetch/$s_!kmTD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6843dd89-55c0-40bd-9603-6058f1c4c674_1418x1350.png)   
---  
  
They share one skeleton:

  * An LLM proposes a change
  * An evaluator scores it
  * And the best changes are kept while the rest are dropped.

What separates them is what they edit and what feedback they get to read.

Let’s understand each of these techniques below.

* * *

1) OPRO, from Google DeepMind, treats the language model itself as the optimizer.

It hands the model a running leaderboard of past prompts and their scores, then asks it to write a stronger instruction each round, which gets scored and added back to the board.

![](https://substackcdn.com/image/fetch/$s_!6gEx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F611fb811-1b39-42e2-9c89-7755fdc3cdc6_1396x209.gif)   
---  
  
This method typically surfaces instructions like asking a model to do deep research or think before it solves a problem.

It needs no gradients and labels beyond a score, which makes it the simplest of the six.

But it plateaus on hard tasks, reacts strongly to how the meta-prompt is phrased, and was never built to beat specialized solvers on large problems.

_A meta-prompt is the prompt handed to the optimizer model, not the one being optimized. It holds the task description, the leaderboard of past instructions and their scores, and the request to write a better one._

* * *

2) MIPROv2, from DSPy, tunes two things at once:

  * One is the wording of the instruction.
  * The other is the set of a few-shot examples, the solved cases shown inside the prompt to demonstrate the task.

Those examples are not something a person hand-picks. MIPROv2 generates them by running the program over a batch of labeled data and keeping the runs that reached the correct answer, so the demonstrations come from what already works.

![](https://substackcdn.com/image/fetch/$s_!CRxN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1fc1f35-d662-4326-9570-c22b216a53f6_1396x209.webp)   
---  
  
Alongside that, it writes candidate instructions informed by the data and the program, then runs a Bayesian search, which tries the promising combinations rather than every one, to find which instruction and example set score best together.

Pairing them in one search is a critical improvement, since an instruction written to fit the examples it ships with reads more cohesively than tuning either half alone.

It works well once a few hundred labeled examples are on hand. The catch is that it locks in its pool of candidate instructions and examples up front, so it cannot react to a specific failure the way a trace-reading method can, and running all the scoring trials gets expensive.

* * *

3) TextGrad, from Stanford, borrows backpropagation almost directly.

It turns a system into a graph where each node is a piece of text and each edge is an LLM call, then passes natural-language criticism backward through that graph so every component learns what it specifically got wrong.

![](https://substackcdn.com/image/fetch/$s_!9Crv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f87ec76-ad2b-4151-b5ae-d4f2b470b604_1396x209.gif)   
---  
  
That design lets it optimize whole multi-step pipelines, and even non-text artifacts like candidate drug molecules, through the same loop.

The interface mirrors PyTorch, so anyone who has written a training loop can pick it up. But the feedback grows unstable once the graph runs more than three or four nodes deep, and each step costs several LLM calls, which adds up fast.

* * *

4) [**GEPA**](<https://fff97757.click.kit-mail3.com/v8uqlqw04vhrhvw8lw8ighvz3og4oi9hpqloo/dpheh0hele3o87smh4/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9ob3ctdG8tYmVhdC1ncnBvLXdpdGhvdXQtdG91Y2hpbmctbW9kZWwtd2VpZ2h0cy8=>), from Berkeley, reads the full execution trace of a run instead of collapsing it into a single score.

It diagnoses why the attempt failed, proposes a targeted fix, and keeps a Pareto set of candidates so a variant that is best at one slice of the task survives even when its overall average is worse.

![](https://substackcdn.com/image/fetch/$s_!_lRL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff016e016-dfff-4591-b0dc-eb8732317e08_1396x209.gif)   
---  
  
Reading the trace, rather than a bare reward, lets it reach a working prompt in a fraction of the rollouts that [**reinforcement learning**](<https://fff97757.click.kit-mail3.com/v8uqlqw04vhrhvw8lw8ighvz3og4oi9hpqloo/e0hph7h787xlqkc8h2/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcmwtY291cnNlLXBhcnQtMS8=>) needs, with no weight updates at all.

Keeping the specialists on the frontier also stops a strong but narrow candidate from being averaged away too early. Its main dependency is that the traces have to be rich enough to diagnose, which not every task provides.

[**We covered GEPA in detail here if you want to learn more →**](<https://fff97757.click.kit-mail3.com/v8uqlqw04vhrhvw8lw8ighvz3og4oi9hpqloo/dpheh0hele3o87smh4/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9ob3ctdG8tYmVhdC1ncnBvLXdpdGhvdXQtdG91Y2hpbmctbW9kZWwtd2VpZ2h0cy8=>)

* * *

5) AlphaEvolve, from DeepMind, points the same loop at code.

Two Gemini models, one tuned for breadth and one for depth, propose diffs to a program, automated evaluators score each candidate, and the best survive into a database that seeds the next generation.

![](https://substackcdn.com/image/fetch/$s_!K-4z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1e36373-43ae-4448-9fcf-fa979d888d43_1396x209.gif)   
---  
  
Surprisingly, this has produced results humans had not found, including a way to multiply 4x4 matrices with fewer multiplications than a method that stood for 56 years, and a data center scheduler now running in Google’s production fleet.

It even sped up a kernel used to train the Gemini models behind it. The limit is that every candidate has to be checked by an automatic evaluator, so it only fits problems where correctness can be measured by a machine (like it happened in the matrix multiplication case), and the evolutionary search burns a lot of compute.

* * *

6) AutoResearch, Andrej Karpathy’s method, runs the loop on a machine learning training script and lets it work autonomously.

A coding agent reads the code, edits it, runs a fixed five-minute experiment, commits the change if the metric improved, and reverts it with a git reset if it did not.

![](https://substackcdn.com/image/fetch/$s_!nayP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ef54430-ff81-4637-929d-c9c1952d35c1_1396x209.gif)   
---  
  
Because only improvements are ever committed, the codebase moves in one direction and never regresses, and the git history doubles as a readable log of what worked.

On his own training code, the agent found around 20 improvements in two days, including a bug in the attention implementation he had missed.

The tradeoff is that it cannot step backward to set up a bigger gain later, so it can get stuck in a local optimum, and it only works when experiments are deterministic and comparable.

* * *

The pattern underneath all six is similar. Turn a system into text, define a way to measure it, and let a language model improve it in a loop.

They differ mostly in what they edit and how much feedback they read, and no single one wins everywhere. The choice comes down to what is being optimized and what can be measured cleanly.

👉 Over to you: Have you used automatic optimization methods before?
