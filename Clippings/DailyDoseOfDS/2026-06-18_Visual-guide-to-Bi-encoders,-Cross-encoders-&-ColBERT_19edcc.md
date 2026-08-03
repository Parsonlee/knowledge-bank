# Visual guide to Bi-encoders, Cross-encoders & ColBERT

- **原邮件主题**: Turn Any Website Into a Custom API in Claude Code
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Thu, 18 Jun 2026 22:03:23 +0000
- **ID**: 19edcc2a8ec8a790

---

## [**Visual guide to Bi-encoders, Cross-encoders & ColBERT**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3dzv6i8h85wqmzoilhvzgnn/58hvh7hgdv35r0t6h4/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYmktZW5jb2RlcnMtYW5kLWNyb3NzLWVuY29kZXJzLWZvci1zZW50ZW5jZS1wYWlyLXNpbWlsYXJpdHktc2NvcmluZy1wYXJ0LTEv>)

So many real-world NLP systems, implicitly or explicitly, rely on [**pairwise sentence (or context) scoring**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3dzv6i8h85wqmzoilhvzgnn/58hvh7hgdv35r0t6h4/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYmktZW5jb2RlcnMtYW5kLWNyb3NzLWVuY29kZXJzLWZvci1zZW50ZW5jZS1wYWlyLXNpbWlsYXJpdHktc2NvcmluZy1wYXJ0LTEv>) in one form or another.

  * [**RAG systems**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3dzv6i8h85wqmzoilhvzgnn/25h2hoh3pvl7k0u3h4/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==>)
  * QA systems
  * Duplicate text detection systems, etc.

The visual depicts three popular approaches used in the industry to handle this:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94b1deaa-33c4-4030-9323-2f6051e040f8_934x1084.gif)   
---  
  
Let’s understand them one by one!

We covered them with implementation here:

1) [**Bi-encoders and Cross-encoders for sentence pair similarity scoring**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3dzv6i8h85wqmzoilhvzgnn/58hvh7hgdv35r0t6h4/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYmktZW5jb2RlcnMtYW5kLWNyb3NzLWVuY29kZXJzLWZvci1zZW50ZW5jZS1wYWlyLXNpbWlsYXJpdHktc2NvcmluZy1wYXJ0LTEv>)**.**

2) [**AugSBERT for sentence pair similarity scoring**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3dzv6i8h85wqmzoilhvzgnn/qvh8h7hdm7e890blhk/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYXVnc2JlcnQtYmktZW5jb2RlcnMtY3Jvc3MtZW5jb2RlcnMtZm9yLXNlbnRlbmNlLXBhaXItc2ltaWxhcml0eS1zY29yaW5nLXBhcnQtMi8=>)**.**

3) [**A deep dive into ColBERT and ColBERTv2 for improving RAG systems (with implementation).**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3dzv6i8h85wqmzoilhvzgnn/g3hnh5hm8dge4zbrh9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC04LXdpdGgtaW1wbGVtZW50YXRpb24v>)

# **1) Cross-encoders**

These are conceptually one of the most powerful approaches.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f5ba20b-725d-44ad-9902-b0cb88d05f78_933x333.gif)   
---  
  
  * Concatenate the query text and the document text.
  * Encode it using a BERT-like encoder model.
  * Apply a transformation (a dense layer) to the `[CLS]` token representations to get a similarity score.

Since the model attends to both contexts, this produces an incredibly semantically expressive representation.

But it does not scale because if you have 1B documents, you must do 1B forward passes to determine the most relevant documents to a query.

# **2) Bi-encoders**

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa564dd5e-a21f-4b30-9090-52e25ec18f77_933x342.gif)   
---  
  
  * Encode the query and the documents separately.
  * Compute the cosine similarity between the `[CLS]` token of the query and the document.

This is highly scalable since the document embeddings can be computed offline.

But we lose all the interaction and simply “hope” that the entire information about the query and the document is well summarized in the `[CLS]` token.

# **3) ColBERT**

This brings together the power of cross-encoders and the scalability of bi-encoders.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfff0681-bc0f-416e-89b7-436e21f8c52e_933x348.gif)   
---  
  
  * Encode the query and the documents separately.
  * Compute a late interaction matrix, which contains similarity scores (dot product) between all query tokens and all document tokens.
  * For every token, determine the max score across all document tokens.
  * Sum these max scores to get a matching score.

Advantages:

  * Like bi-encoders, it is highly scalable since document embeddings can be computed offline.
  * Like cross-encoders, it maintains cross-interactions between the query and the document tokens (called late interaction).

We covered them with implementation here:

  * [**Bi-encoders and Cross-encoders for Sentence Pair Similarity Scoring**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3dzv6i8h85wqmzoilhvzgnn/58hvh7hgdv35r0t6h4/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYmktZW5jb2RlcnMtYW5kLWNyb3NzLWVuY29kZXJzLWZvci1zZW50ZW5jZS1wYWlyLXNpbWlsYXJpdHktc2NvcmluZy1wYXJ0LTEv>)**.**
  * [**AugSBERT for Sentence Pair Similarity Scoring**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3dzv6i8h85wqmzoilhvzgnn/qvh8h7hdm7e890blhk/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYXVnc2JlcnQtYmktZW5jb2RlcnMtY3Jvc3MtZW5jb2RlcnMtZm9yLXNlbnRlbmNlLXBhaXItc2ltaWxhcml0eS1zY29yaW5nLXBhcnQtMi8=>)**.**
  * [**A deep dive into ColBERT and ColBERTv2 for improving RAG systems (with implementation).**](<https://fff97757.click.kit-mail3.com/e5unmnq5evf7hl3dzv6i8h85wqmzoilhvzgnn/g3hnh5hm8dge4zbrh9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC04LXdpdGgtaW1wbGVtZW50YXRpb24v>)

Over to you: What are some other advantages of ColBERT?
