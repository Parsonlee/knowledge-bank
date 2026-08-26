---
title: Categorization of clustering algorithms
source_key: dailydoseofds
email_subject: '[Hands-on] Build a 3D Weather Globe with Claude Code'
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Mon, 01 Jun 2026 20:49:47 +0000
email_id: 19e84f32570b4582
article_id: 19e84f32570b4582:1
published: '2026-06-01'
tags:
- Skill/data-analysis
---

# Categorization of clustering algorithms

- **原邮件主题**: [Hands-on] Build a 3D Weather Globe with Claude Code
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Mon, 01 Jun 2026 20:49:47 +0000
- **ID**: 19e84f32570b4582

---

## [**Categorization of clustering algorithms**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/n2hohvhvpezwovi6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZ2F1c3NpYW4tbWl4dHVyZS1tb2RlbHMtZ21tLw==>)

There’s a whole world of clustering algorithms beyond KMeans, which a data scientist must be familiar with.

In the following visual, we have summarized 6 different types of clustering algorithms:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/kBcUzeRfgu9suBiQmaGz4m/email)   
---  
  
**1) Centroid-based:** Cluster data points based on proximity to centroids.

**2) Connectivity-based:** Cluster points based on proximity between clusters.

**3) Density-based:** Cluster points based on their density. It is more robust to clusters with varying densities and shapes than centroid-based clustering.

  * DBSCAN is a popular algorithm here, but it has high run-time.
  * [****](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/48hvhehmek4z26ix/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGJzY2FuLXRoZS1mYXN0ZXItYW5kLXNjYWxhYmxlLWFsdGVybmF0aXZlLXRvLWRic2Nhbi1jbHVzdGVyaW5nLw==>)[**DBSCAN++**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/48hvhehmek4z26ix/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGJzY2FuLXRoZS1mYXN0ZXItYW5kLXNjYWxhYmxlLWFsdGVybmF0aXZlLXRvLWRic2Nhbi1jbHVzdGVyaW5nLw==>)[](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/48hvhehmek4z26ix/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGJzY2FuLXRoZS1mYXN0ZXItYW5kLXNjYWxhYmxlLWFsdGVybmF0aXZlLXRvLWRic2Nhbi1jbHVzdGVyaW5nLw==>) solves this.
  * It is a faster and more scalable alternative to DBSCAN.
  * We covered both DBSCAN and DBSCAN++ in detail [**here**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/48hvhehmek4z26ix/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZGJzY2FuLXRoZS1mYXN0ZXItYW5kLXNjYWxhYmxlLWFsdGVybmF0aXZlLXRvLWRic2Nhbi1jbHVzdGVyaW5nLw==>).

**4) Graph-based:** Cluster points based on graph distance.

**5) Distribution-based:** Cluster points based on their likelihood of belonging to the same distribution.

  * [****](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/n2hohvhvpezwovi6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZ2F1c3NpYW4tbWl4dHVyZS1tb2RlbHMtZ21tLw==>)[**Gaussian Mixture Models**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/n2hohvhvpezwovi6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZ2F1c3NpYW4tbWl4dHVyZS1tb2RlbHMtZ21tLw==>) is one example.
  * We discussed it in detail and implemented it from scratch (only NumPy) here: [****](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/n2hohvhvpezwovi6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZ2F1c3NpYW4tbWl4dHVyZS1tb2RlbHMtZ21tLw==>)[**Gaussian Mixture Models**](<https://fff97757.click.kit-mail3.com/27uprpxd03foh8po0gzi3hg9nleqpaghgmk33/n2hohvhvpezwovi6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vZ2F1c3NpYW4tbWl4dHVyZS1tb2RlbHMtZ21tLw==>)**.**

**6) Compression-based:** Transform data to a lower-dimensional space and then perform clustering.

👉 Over to you: What other clustering algorithms will you include here?
