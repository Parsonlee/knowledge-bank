# Technical LLM interview question!

- **原邮件主题**: Serverless vs. On-prem vs. Edge Deployment
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Tue, 28 Jul 2026 21:23:05 +0000
- **ID**: 19faa9c1ec5cf9ba

---

## [**Technical LLM interview question!**](<https://fff97757.click.kit-mail3.com/4zuwmw6lz0hehpxmvm3txh63p02rzf5h6ng99/vqh3hrhoznl205bghl/aHR0cHM6Ly9hcnhpdi5vcmcvcGRmLzI2MDQuMDAzNTY=>)

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/rebNqDFnniHnJpNUpKsorU/email)   
---  
  
You have 80,000 agent trajectories from production. You need to find top 100 worth reviewing to improve your agent.

No LLM allowed to evaluate trajectories. How will you do this?

Let’s look at some approaches.

The simplest solution one could start with is random sampling. Pick 100 random trajectories and review.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/krBWhu2kjr6CKDi15JRfPp/email)   
---  
  
But most production agents handle routine requests just fine, so you end up wasting a big chunk of your annotation budget.

Another approach can filter for longer conversations since 10+ user messages means more complexity.

But longer conversations skew heavily toward outright failures. You’ll surface obvious breakdowns but miss subtle issues hiding in conversations where the agent technically succeeded.

A [**recent paper from DigitalOcean**](<https://fff97757.click.kit-mail3.com/4zuwmw6lz0hehpxmvm3txh63p02rzf5h6ng99/vqh3hrhoznl205bghl/aHR0cHM6Ly9hcnhpdi5vcmcvcGRmLzI2MDQuMDAzNTY=>) takes a new approach. 

![](https://substackcdn.com/image/fetch/$s_!RO6D!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F348b55cc-2e33-45b0-8a80-f31681a7ce21_1061x1015.png)   
---  
  
It computes lightweight behavioral signals directly from the trajectory data using deterministic rules.

The signals fall into three groups:

![](https://substackcdn.com/image/fetch/$s_!7pYl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1908fc0-67d9-4c76-9b4a-ad7f2f9d6019_1108x552.png)   
---  
  
1) Interaction signals:

  * If a user rephrases the request or corrects the agent, that’s misalignment.
  * Agent repeating itself is stagnation.
  * User abandoning the agent is disengagement.
  * User confirming something worked is satisfaction.

All are detected through normalized phrase matching and similarity checks.

2) Execution signals:

  * A tool call that doesn’t advance the task is a failure signal.
  * Repeated calls with identical or drifting inputs indicate a loop.

These are straightforward to extract from execution logs.

3) Environment signals, like rate limits, context overflow, and API errors.

  * Useful to diagnose but not for training since they reflect system constraints, not agent decisions.

Each trajectory gets scored based on which signals fire, and you sample the highest-signal ones for review.

On τ-bench, they compared all three approaches on 100 trajectories:

![](https://substackcdn.com/image/fetch/$s_!3a47!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe193608f-e5a1-4416-b1b4-c77bed82d7c6_1246x385.png)   
---  
  
  * Random sampling hit a 54% informativeness rate.
  * The length-based heuristic reached 74%.
  * Signal-based sampling reached 82%.

This means roughly 4 out of every 5 trajectories are genuinely useful to improve the agent.

In fact, among conversations where the agent completed the task correctly, signal sampling still identified useful patterns in 66.7% of cases vs. 41.3% for random.

These are the subtle issues like policy violations, inefficient tool use, and unnecessary steps that don’t break the task but still matter for optimization.

The whole framework runs without any LLM overhead and can sit always-on in a production pipeline.

If you want to see this in practice, this signal-based approach is already integrated into [**Plano**](<https://fff97757.click.kit-mail3.com/4zuwmw6lz0hehpxmvm3txh63p02rzf5h6ng99/l2hehmhl8oe575h6h0/aHR0cHM6Ly9naXRodWIuY29tL2thdGFuZW1vL3BsYW5v>), an open-source AI-native proxy that handles routing, orchestration, guardrails, and observability in one place.

[![](https://substackcdn.com/image/fetch/$s_!b9Bw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97164b14-e9ff-4676-9b9a-31e325a91d6e_1456x902.png)](<https://fff97757.click.kit-mail3.com/4zuwmw6lz0hehpxmvm3txh63p02rzf5h6ng99/m2h7h5h3dovkzgamhq/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIWI5QnchLGZfYXV0byxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRjk3MTY0YjE0LWU5ZmYtNDY3Ni05YjlhLTMxZTMyNWE5MWQ2ZV8xNDU2eDkwMi5wbmc=>)  
---  
  
[**Here’s the Plano GitHub repo →**](<https://fff97757.click.kit-mail3.com/4zuwmw6lz0hehpxmvm3txh63p02rzf5h6ng99/l2hehmhl8oe575h6h0/aHR0cHM6Ly9naXRodWIuY29tL2thdGFuZW1vL3BsYW5v>)

[**Here’s the paper on arxiv →**](<https://fff97757.click.kit-mail3.com/4zuwmw6lz0hehpxmvm3txh63p02rzf5h6ng99/vqh3hrhoznl205bghl/aHR0cHM6Ly9hcnhpdi5vcmcvcGRmLzI2MDQuMDAzNTY=>)

👉 Over to you: What is your approach to solve this? 
