---
title: ANN search using inverted file index
source_key: dailydoseofds
email_subject: Another MCP Moment by Anthropic?
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Mon, 27 Oct 2025 20:11:13 +0000
email_id: 19a274be34a3e99c
article_id: 19a274be34a3e99c:1
published: '2025-10-27'
tags:
- RAG/retrieval
---

# ANN search using inverted file index

- **原邮件主题**: Another MCP Moment by Anthropic?
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Mon, 27 Oct 2025 20:11:13 +0000
- **ID**: 19a274be34a3e99c

---

## [**ANN search using inverted file index**](<https://www.dailydoseofds.com/a-beginner-friendly-and-comprehensive-deep-dive-on-vector-databases/>)

kNN performs an exhaustive search, which is inefficient at scale!

![](https://substackcdn.com/image/fetch/$s_!arGl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71e5cfd4-7661-4426-9e57-a6115654b5b3_1140x454.gif)   
---  
  
Approximate nearest neighbor search algorithms solve this.

The core idea is to narrow down the search space using indexing techniques, which improves the run-time performance.

![](https://substackcdn.com/image/fetch/$s_!Elpl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4efa275d-c8ee-4332-8648-f69a70fe6d68_1504x884.png)   
---  
  
Inverted file index (IFV) is one of the simplest and intuitive techniques to do this.

Steps for indexing:

  * Partition the given data using techniques like k-means.

![](https://substackcdn.com/image/fetch/$s_!FTOZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefcd3013-5d0d-4862-a6a5-f487ae34bbce_2184x676.png)   
---  
  
  * Each partition gets a centroid, and each data point gets associated with only one partition.

![](https://substackcdn.com/image/fetch/$s_!dMa8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcbfb865-09ee-41d8-891f-e003ddac6d77_2048x684.png)   
---  
  
  * A map holds all the data points that belong to a centroid’s partition.

![](https://substackcdn.com/image/fetch/$s_!5ovD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1485046c-35b6-434b-8afc-4af53c35e69e_1728x796.png)   
---  
  
Indexing done!

Here’s how we search.

  * First, find the closest centroid to the query:

![](https://substackcdn.com/image/fetch/$s_!n2-4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aa59990-088f-4954-9547-2267c3931230_1700x756.png)   
---  
  
  * Next, find the nearest neighbor among only those data points that belong to the closest centroid’s partition:

![](https://substackcdn.com/image/fetch/$s_!AK0D!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c8b11cc-047f-4103-98f3-c806cb658050_1820x716.png)   
---  
  
This drastically reduces the run-time.

Consider:

  * There are `N` data points.
  * Each data point is `D`-dimensional.
  * We create `K` partitions.
  * Lastly, for simplicity, let’s assume that each partition gets equal data points.

In kNN, the query data point is matched to all `N` data points, which makes the time complexity → `O(ND)`.

In IFV, however, there are two steps:

  1. Match to all centroids → `O(KD)`.
  2. Find the nearest neighbor in the nearest partition → `O(ND/K)`.

The final time complexity comes out to be the following:

![](https://substackcdn.com/image/fetch/$s_!hK5Q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fae4e0e08-91d4-4050-ad96-07a3e6236d1b_325x114.png)   
---  
  
…which is significantly lower than that of kNN.

Assume → `N=10M` and `k=100`:

  * The search complexity of kNN will be proportional to **10M**.
  * With IFV, the search complexity will be proportional to `100 + 100k = 100100`, which is nearly **100 times faster**.

That said, ANN is not always accurate.

If some data points are actually close to the query data point but not in the same partition, they may still get missed:

![](https://substackcdn.com/image/fetch/$s_!nRi5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36119d6b-8644-4f97-b824-8f110e20c749_1808x744.png)   
---  
  
We willingly accept such trade-offs to reduce latency.

In the deep dives on vector databases (open access), we discussed 4 such techniques, along with an entirely beginner-friendly and thorough discussion on Vector Databases.

Check it out here if you haven’t already: [**A Beginner-friendly and Comprehensive Deep Dive on Vector Databases**](<https://www.dailydoseofds.com/a-beginner-friendly-and-comprehensive-deep-dive-on-vector-databases/>).

Thanks for reading!
