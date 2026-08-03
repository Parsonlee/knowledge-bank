# RAG vs MetaAI's REFRAG

- **原邮件主题**: How to Build an OS for Your AI Workforce?
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Tue, 24 Mar 2026 21:23:23 +0000
- **ID**: 19d21bb1fc294cac

---

## [**RAG vs MetaAI's REFRAG**](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/x0hph6he2wv5dgs5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==>)

Most of what we retrieve in RAG setups never actually helps the LLM.

In classic RAG, when a query arrives:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/fGhFLCjc94but5UngpEb3/email)   
---  
  
  * You encode it into a vector.
  * Fetch the most similar chunks from your vector DB.
  * Dump all retrieved text into the LLM context.

It works, but at a huge cost:

  * Most chunks contain redundant or irrelevant text.
  * The LLM processes **far more tokens** than it needs.
  * You pay for compute, latency, and context; most of it is wasted.

That’s the exact problem Meta AI’s new method REFRAG solves. It fundamentally rethinks retrieval and this diagram explains how it works:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/wkSXfpLuRr1KXdcXpZ6odb/email)   
---  
  
Instead of feeding the LLM every chunk and every token, REFRAG compresses and filters context at a vector level:

  * Chunk compression: Each chunk is encoded into a single compressed embedding, rather than hundreds of token embeddings.
  * Relevance policy: A lightweight RL-trained policy evaluates these compressed embeddings and keeps only the most relevant chunks.
  * Selective expansion: Only the chunks chosen by the RL policy are expanded back into their full embeddings and passed to the LLM.

This way, the model processes just what matters and ignores the rest.

Here's the step-by-step walkthrough:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/wkSXfpLuRr1KXdcXpZ6odb/email)   
---  
  
  * Step 1-2) Encode documents and store them in a vector DB.
  * Step 3-5) Encode the full user query and find relevant chunks. Also, compute the token-level embeddings for both the query (step 7) and matching chunks.
  * Step 6) Use a relevance policy (trained via reinforcement learning) to select which chunks to keep.
  * Step 8) Concatenate the token-level representations of the input query with the token-level embedding of selected chunks and a compressed single-vector representation of the rejected chunks.
  * Step 9-10) Send that to the LLM for the final response.

The RL step makes REFRAG a more selective and relevance-aware RAG pipeline.

Based on the research paper, this leads to:

  * 30.85x faster time-to-first-token (3.75x better than previous SOTA)
  * 16x larger context windows
  * Outperforms LLaMA on 16 RAG benchmarks while using 2–4x fewer decoder tokens
  * No accuracy loss across RAG, summarization, and multi-turn conversation tasks

That means you can process 16x more context at 30x the speed, with the same accuracy.

The code has not been released yet by Meta. They intend to do that soon, but in the meantime, you can [**read the research paper here →**](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/dpheh0he609lmzam/aHR0cHM6Ly9hcnhpdi5vcmcvcGRmLzI1MDkuMDEwOTI=>)

If you don't know how production-grade RAG systems are built, here's everything we have covered in the RAG crash course:

  * [****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/x0hph6he2wv5dgs5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==>)[**RAG fundamentals**](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/x0hph6he2wv5dgs5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==>)[****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/x0hph6he2wv5dgs5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==>)
  * [****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/e0hph7h7v0382ps8/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0yLXdpdGgtaW1wbGVtZW50YXRpb25zLw==>)[**RAG evaluation**](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/e0hph7h7v0382ps8/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0yLXdpdGgtaW1wbGVtZW50YXRpb25zLw==>)[****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/e0hph7h7v0382ps8/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0yLXdpdGgtaW1wbGVtZW50YXRpb25zLw==>)
  * [****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/7qh7h8h9lo2rm6cz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0zLXdpdGgtaW1wbGVtZW50YXRpb24v>)[**RAG optimization**](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/7qh7h8h9lo2rm6cz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0zLXdpdGgtaW1wbGVtZW50YXRpb24v>)[****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/7qh7h8h9lo2rm6cz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0zLXdpdGgtaW1wbGVtZW50YXRpb24v>)
  * [****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/owhkhqhw9rm27nav/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC01LXdpdGgtaW1wbGVtZW50YXRpb24v>)[**Multimodal RAG**](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/owhkhqhw9rm27nav/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC01LXdpdGgtaW1wbGVtZW50YXRpb24v>)[****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/owhkhqhw9rm27nav/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC01LXdpdGgtaW1wbGVtZW50YXRpb24v>)
  * [****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/z2hghnhe632q8rip/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC03LXdpdGgtaW1wbGVtZW50YXRpb24v>)[**Graph RAG**](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/z2hghnhe632q8rip/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC03LXdpdGgtaW1wbGVtZW50YXRpb24v>)[****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/z2hghnhe632q8rip/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC03LXdpdGgtaW1wbGVtZW50YXRpb24v>)
  * [****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/p8heh9h46zwnllsq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC04LXdpdGgtaW1wbGVtZW50YXRpb24v>)[**Multivector retrieval using ColBERT**](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/p8heh9h46zwnllsq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC04LXdpdGgtaW1wbGVtZW50YXRpb24v>)[****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/p8heh9h46zwnllsq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC04LXdpdGgtaW1wbGVtZW50YXRpb24v>)
  * [****](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/x0hph6he2wv5l7t5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC05LXdpdGgtaW1wbGVtZW50YXRpb24v>)[**RAG over complex real-world docs ft. ColPali**](<https://fff97757.click.kit-mail3.com/75ur9re36qi8h6l7dmpazhwrpz72winh50m33/x0hph6he2wv5l7t5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC05LXdpdGgtaW1wbGVtZW50YXRpb24v>)

