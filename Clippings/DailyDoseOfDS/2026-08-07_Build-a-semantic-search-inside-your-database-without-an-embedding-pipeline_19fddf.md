#  Build a semantic search inside your database without an embedding pipeline 

- **原邮件主题**: [Hands-on] Build Semantic Search Inside Your Database Without an Embedding Pipeline
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 07 Aug 2026 20:42:13 +0000
- **ID**: 19fddf64edb10546

---

## [**Build a semantic search inside your database without an embedding pipeline**](<https://fandf.co/45Hl0Tm>)

We typed a plain English query against 21,000 movie plots and got back semantically relevant results without writing a single line of embedding code.

![](https://substackcdn.com/image/fetch/$s_!D_AD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1843328d-aac8-46cd-8d4d-a0aed939af4b_3110x1992.png)   
---  
  
The database is [**MongoDB Atlas**](<https://fandf.co/45Hl0Tm>), which added auto-embedding powered by Voyage AI directly into its vector search index configuration.

[**MongoDB Atlas Platform**](<https://fandf.co/45Hl0Tm>)  
---  
  
When you add semantic search to an app, the standard move is to wire up an external embedding service, sync vectors to a separate store, and write glue to keep everything updated as data changes. 

Most teams never question this setup because that’s just how the stack looked when vector search was new.

The real problem shows up later when your data changes, but your pipeline has already run, and search quality starts degrading in ways that are hard to pin down because nothing is explicitly broken. 

![](https://substackcdn.com/image/fetch/$s_!Q5qP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96a7459a-565c-47fe-969c-7963738b636a_3112x1978.png)   
---  
  
MongoDB Atlas handles this with auto-embedding. You point an index at a text field, specify a Voyage AI model, and it generates and maintains the vectors inside the database. 

When a document changes, it re-embeds automatically, so your search stays current.

#### Setting up auto-embedding

Load MongoDB’s sample dataset from your Atlas cluster and navigate to `sample_mflix` → `movies`. Then go to Search & Vector Search → Create Search Index.

On the index creation screen:

  * Select **Vector Search** as the search type
  * Scroll down and select **Automated Embedding** under “How do you want to set up your vector data?”
  * Name your index `autoembed_index`
  * Select `sample_mflix` → `movies` as the database and collection
  * Choose **JSON Editor** as the configuration method

Atlas pre-populates the config. Just replace `<field-name>` with `plot`:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/iTRwztmm4xvX3ytRnrNwnt/email)   
---  
  
Once the index flips to Active, open the Aggregation tab on the movies collection and run:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/uLFD6twXa1zufHLReaNZ7g/email)   
---  
  
The results come back with movies whose plots share none of those exact words with the query, which is the index doing semantic matching rather than keyword lookup.

One index config replaced the embedding service, the vector store, and the sync layer you used to maintain separately.

If you want to go deeper, MongoDB has a full [**AI Skill Badges program**](<https://fandf.co/4fVsOG0>) on MongoDB University covering everything from vector search fundamentals to agentic memory and RAG, and each badge earns a Credly credential you can share on LinkedIn.

[**Explore the AI Skill Badges →**](<https://fandf.co/4fVsOG0>)

[**MongoDB Atlas Platform →**](<https://fandf.co/45Hl0Tm>)

_Thanks to MongoDB for working with us on today’s issue!_
