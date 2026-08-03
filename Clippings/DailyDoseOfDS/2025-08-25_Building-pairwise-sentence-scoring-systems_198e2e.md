# Building pairwise sentence scoring systems

- **原邮件主题**: 4 Layers of Agentic AI Systems
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Mon, 25 Aug 2025 20:26:25 +0000
- **ID**: 198e2e9234d8b09f

---

## [**Building pairwise sentence scoring systems**](<https://www.dailydoseofds.com/bi-encoders-and-cross-encoders-for-sentence-pair-similarity-scoring-part-1/>)

So real-world NLP systems implicitly or explicitly depend on context similarities:

  * A RAG system heavily relies on pairwise sentence scoring (_this could be at varying levels of granularity based on how you chunk the data_) to retrieve relevant context, which is then fed to the LLM for generation. That is why RAG is considered 80% retrieval and 20% generation. In other words, most of it boils down to how well you retrieve the relevant context.

![](https://substackcdn.com/image/fetch/$s_!DpHM!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6878b8fa-5e74-45a1-9a89-5aab92889126_2366x990.gif)   
---  
  
  * Several question-answering systems implicitly evaluate the similarity between questions and potential answers.
  * Several information retrieval (IR) systems depend on scoring query-document pairs to rank the most suitable documents for a given query.
  * Duplicate detection engines assess whether two sentences or questions convey the same meaning. This is especially observed in community-driven platforms (Stackoverflow, Medium, Quora, etc.). For instance, Quora shows you questions related to the question you are reading answers for.

This list of tasks that depend on pairwise sentence scoring can go on and on.

But the point is that pairwise sentence (paragraphs, documents, etc.) scoring is a fundamental building block in several NLP applications.

If you intend to build such systems, you need those skills and understand SOTA approaches.

We did a 2-part series that covers the entire background in a beginner-friendly way, the challenges with traditional approaches, optimal approaches, and implementations.

Read part 1 here: [**Bi-encoders and Cross-encoders for Sentence Pair Similarity Scoring Part 1**](<https://www.dailydoseofds.com/bi-encoders-and-cross-encoders-for-sentence-pair-similarity-scoring-part-1/>).

Read part 2 here: [**AugSBERT: Bi-encoders + Cross-encoders for Sentence Pair Similarity Scoring Part 2**](<https://www.dailydoseofds.com/augsbert-bi-encoders-cross-encoders-for-sentence-pair-similarity-scoring-part-2/>).

If you have never heard about such systems, don’t worry, since that is what we intend to cover today with proper context, like we always do.
