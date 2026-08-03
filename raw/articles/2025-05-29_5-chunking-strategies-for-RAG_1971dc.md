# 5 chunking strategies for RAG

- **原邮件主题**: 5 Chunking Strategies For RAG
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Thu, 29 May 2025 20:47:19 +0000
- **ID**: 1971dcca96aa74c3

---

## [**5 chunking strategies for RAG**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-1-with-implementations/>)  
  
Here’s the typical workflow of RAG:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feed92d2a-dde5-4755-b30f-366a7ad6d606_1240x514.gif)   
---  
  
Since the additional document(s) can be large, step 1 also involves chunking, wherein a large document is divided into smaller/manageable pieces.

This step is crucial since it ensures the text fits the input size of the embedding model.

Here are five chunking strategies for RAG:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92c70184-ba0f-4877-9a55-e4add0e311ad_870x1116.gif)   
---  
  
Let’s understand them today!

If you want to dive into building LLM apps, our full RAG crash course discusses RAG from basics to beyond:

\- [**RAG fundamentals**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-1-with-implementations/>)

\- [**RAG evaluation**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-2-with-implementations/>)

\- [**RAG optimization**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-3-with-implementation/>)

\- [**Multimodal RAG**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-5-with-implementation/>)

\- [**Graph RAG**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-7-with-implementation/>)

\- [**Multivector retrieval using ColBERT**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-8-with-implementation/>)

\- [**RAG over complex real-world docs ft. ColPali**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-9-with-implementation/>)

* * *

# **1) Fixed-size chunking**

Split the text into uniform segments based on a pre-defined number of characters, words, or tokens.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98c422a0-f0e2-457c-a256-4476a56a601f_943x232.png)   
---  
  
Since a direct split can disrupt the semantic flow, it is recommended to maintain some overlap between two consecutive chunks (the blue part above).

This is simple to implement. Also, since all chunks are of equal size, it simplifies batch processing.

But this usually breaks sentences (or ideas) in between. Thus, important information will likely get distributed between chunks.

* * *

# **2) Semantic chunking**

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6ad83a6-2879-4c77-9e49-393f16577aef_1066x288.gif)   
---  
  
  * Segment the document based on meaningful units like sentences, paragraphs, or thematic sections.
  * Next, create embeddings for each segment.
  * Let’s say we start with the first segment and its embedding.
    * If the first segment’s embedding has a high cosine similarity with that of the second segment, both segments form a chunk.
    * This continues until cosine similarity drops significantly.
    * The moment it does, we start a new chunk and repeat.

Here’s what the output could look like:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74037e11-362d-4ea2-8ee2-ee85ab013523_963x231.png)   
---  
  
Unlike fixed-size chunks, this maintains the natural flow of language and preserves complete ideas.

Since each chunk is richer, it improves the retrieval accuracy, which, in turn, produces more coherent and relevant responses by the LLM.

A minor problem is that it depends on a threshold to determine if cosine similarity has dropped significantly, which can vary from document to document.

* * *

# **3) Recursive chunking**

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4009caa-34fc-48d6-8102-3d0f6f2c1386_1066x316.gif)   
---  
  
First, chunk based on inherent separators like paragraphs, or sections.

Next, split each chunk into smaller chunks if the size exceeds a pre-defined chunk size limit. If, however, the chunk fits the chunk-size limit, no further splitting is done.

Here’s what the output could look like:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0e40cc1-996f-48f4-9306-781b112536e4_984x428.png)   
---  
  
As shown above:

  * First, we define two chunks (the two paragraphs in purple).
  * Next, paragraph 1 is further split into smaller chunks.

Unlike fixed-size chunks, this approach also maintains the natural flow of language and preserves complete ideas.

However, there is some extra overhead in terms of implementation and computational complexity.

* * *

# **4) Document structure-based chunking**

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8febecd-ee68-42ff-ab06-41a0a3a43cd3_1102x306.gif)   
---  
  
It utilizes the inherent structure of documents, like headings, sections, or paragraphs, to define chunk boundaries. This way, it maintains structural integrity by aligning with the document’s logical sections.

Here’s what the output could look like:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40bdaf3b-601d-4357-bc7f-89b47f812097_1025x663.png)   
---  
  
That said, this approach assumes that the document has a clear structure, which may not be true.

Also, chunks may vary in length, possibly exceeding model token limits. You can try merging it with recursive splitting.

* * *

# **5) LLM-based chunking**

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d1b6d60-8956-4030-8525-d899ee61a9d5_1140x198.gif)   
---  
  
Prompt the LLM to generate semantically isolated and meaningful chunks.

This method ensures high semantic accuracy since the LLM can understand context and meaning beyond simple heuristics (used in the above four approaches).

But this is the most computationally demanding chunking technique of all five techniques discussed here.

Also, since LLMs typically have a limited context window, that is something to be taken care of.

* * *

Each technique has its own advantages and trade-offs.

We have observed that semantic chunking works pretty well in many cases, but again, you need to test.

The choice will depend on the nature of your content, the capabilities of the embedding model, computational resources, etc.

If you want to dive into building LLM apps, our full RAG crash course discusses RAG from basics to beyond:

  * [**RAG fundamentals**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-1-with-implementations/>)
  * [**RAG evaluation**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-2-with-implementations/>)
  * [**RAG optimization**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-3-with-implementation/>)
  * [**Multimodal RAG**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-5-with-implementation/>)
  * [**Graph RAG**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-7-with-implementation/>)
  * [**Multivector retrieval using ColBERT**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-8-with-implementation/>)
  * [**RAG over complex real-world docs ft. ColPali**](<https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-9-with-implementation/>)

👉 Over to you: What other chunking strategies do you know?
