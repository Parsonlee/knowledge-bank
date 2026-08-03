# Claude Code dynamic workflows, explained!

- **原邮件主题**: [Hands-on] Build a 3D Weather Globe with Claude Code
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Mon, 01 Jun 2026 20:49:47 +0000
- **ID**: 19e84f32570b4582

---

## [**Claude Code dynamic workflows, explained!**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/3ohphkh3lve6d7br/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9jbGF1ZGUtc3ViYWdlbnRzLXZzLWFnZW50LXRlYW1zLw==>)

Anthropic recently release Opus 4.8, and everyone is talking about the benchmarks, the honesty improvements, and the cheaper fast mode.

But the feature that shipped alongside it might matter more for how we actually build: Dynamic Workflows in Claude Code.

Here’s what they are, how they differ from subagents and agent teams (which already existed), and why they change the game for large-scale agentic coding.

![](https://substackcdn.com/image/fetch/$s_!sGB0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0274fe54-fda1-4ffe-be74-bc19107013f8_2412x1426.png)   
---  
  
#### What are dynamic workflows?

Claude Code already had two multi-agent primitives before this release.

![](https://substackcdn.com/image/fetch/$s_!N-0b!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74e64a66-02af-490f-9371-55286fa09cf0_1566x788.png)   
---  
  
  * Subagents are lightweight workers spawned from a main session. They do a focused task and report back. But they can’t talk to each other, and the main agent still acts as the bottleneck for orchestration. Every result routes through one context window.
  * Agent Teams (shipped with Opus 4.6) removed that constraint. Multiple Claude instances coordinate through a shared task list and message each other directly. But they top out at 3-5 teammates practically, sessions don’t survive interruptions (if Claude crashes mid-task, the team is gone), and you still need to design the orchestration upfront.

[**We published an article on both of the above. You can read it here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/3ohphkh3lve6d7br/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9jbGF1ZGUtc3ViYWdlbnRzLXZzLWFnZW50LXRlYW1zLw==>)

Dynamic Workflows sit above both.

Instead of Claude holding the plan in its context window, it writes a JavaScript orchestration script. That script becomes the plan. A JS runtime executes it, fanning work across tens to hundreds of parallel subagents automatically.

![](https://substackcdn.com/image/fetch/$s_!PHoD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea0dbf24-dec6-468f-bf36-8f4470cfeeec_965x562.png)   
---  
  
You describe the task. Claude decides how to split it, how many agents to spawn, how to verify results, and what to report back. The orchestration logic moves from the LLM’s memory into executable code.

Claude’s context window only ever sees the final converged answer. Not the intermediate results of hundreds of steps.

This is helpful because of several reasons:

  * Scale → You can run up to 16 concurrent agents and 1,000 total per workflow, while Subagents max out at a handful and Agent Teams get messy past 5.
  * Adversarial verification → This allows agents to tackle a problem from independent angles, other agents try to refute their findings, and the system iterates until answers converge. Compare this to subagents which just report back and Agent Teams collaborate but don’t adversarially verify.
  * Resumability → You can save progress saves continuously. So interrupted jobs pick up where they left off while Agent Teams die with the session.
  * Zero orchestration burden → You just describe the goal and Claude decides how to split work, how many agents to spawn, and how to verify results.

These are some best practices:

→ Start with a scoped task to calibrate token usage before going full-scale. Workflows consume significantly more tokens than a typical session.

→ Enable auto mode so Claude decides when a workflow is appropriate vs. when a simpler approach works.

→ Use the `ultracode` setting (effort menu) to let Claude auto-trigger workflows. This also sets reasoning to `xhigh`.

→ Review the execution plan on first trigger. A poorly scoped prompt will fan out agents unnecessarily.

→ Enterprise plans have workflows off by default. An admin needs to enable them.

As further reading, [**we published an article on Agent Teams and Subagents recently. You can read it here →**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/3ohphkh3lve6d7br/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9jbGF1ZGUtc3ViYWdlbnRzLXZzLWFnZW50LXRlYW1zLw==>)
