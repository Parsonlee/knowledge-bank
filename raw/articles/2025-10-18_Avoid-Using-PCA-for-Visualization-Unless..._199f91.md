---
title: Avoid Using PCA for Visualization Unless...
source_key: dailydoseofds
email_subject: Avoid Using PCA for Visualization Unless...
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Sat, 18 Oct 2025 20:59:57 +0000
email_id: 199f91f3eaa6509e
article_id: 199f91f3eaa6509e:1
published: '2025-10-18'
tags:
- Skill/data-analysis
---

# Avoid Using PCA for Visualization Unless...

- **原邮件主题**: Avoid Using PCA for Visualization Unless...
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Sat, 18 Oct 2025 20:59:57 +0000
- **ID**: 199f91f3eaa6509e

---

## [**Avoid Using PCA for Visualization Unless...**](<https://www.dailydoseofds.com/formulating-the-principal-component-analysis-algorithm-from-scratch/>)

[**PCA**](<https://www.dailydoseofds.com/formulating-the-principal-component-analysis-algorithm-from-scratch/>), by its very nature, is a dimensionality reduction technique.

Yet, at times, it is used to visualize high-dimensional datasets by projecting the data into two dimensions.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/iqc5YCYR8ZZkd5Ck9ypZXs/email)   
---  
  
Here's the problem with it.

After applying PCA, each new feature (PC1, PC2, ..., PC-N) captures a fraction of the original data variance:

  * PC1 may capture 40%.
  * PC2 may capture 25%.
  * And so on.

Thus, using PCA for visualization by projecting the data to 2-dimensions only makes sense if the first two principal components collectively capture most of the original data variance.

This is rarely true in practice.

But it is possible to verify if PCA's visualization is useful by creating a **cumulative explained variance (CEV)** plot.

It plots the cumulative variance explained by principal components.

In sklearn, the explained variance fraction is available in the `explained_variance_ratio_` attribute:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/gsRttUdcyutEe5Qwb36jY5/email)   
---  
  
Create a cumulative plot of explained variance and check whether the first two components explain the majority of variance.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/naLCbohgQZTgA4s3iDoYL7/email)   
---  
  
If the plot looks the following, your PCA visualizations are misleading since the first two components only explain 55% of the variance:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/kgAKGCyjKou2mT4cXeEZSb/email)   
---  
  
But if the plot looks like the following, it is safe to use PCA:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/nCANandQLfKiLjySpHaSNo/email)   
---  
  
As a takeaway, use PCA for 2D visualization only when the above plot suggests so.

That said, use the CEV plot only for dimensionality reduction to determine how many dimensions to project the data to when using PCA.

For instance, in the following plot, projecting to 5 dimensions could be good (depending on how much information loss you can tolerate):

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/kgAKGCyjKou2mT4cXeEZSb/email)   
---  
  
For visualization, however, use techniques specifically designed for it, like t-SNE, UMAP, etc.

[**We formulated and implemented (in NumPy) t-SNE from scratch here**](<https://www.dailydoseofds.com/formulating-and-implementing-the-t-sne-algorithm-from-scratch/>).

[**We discussed the mathematical details of PCA and derived it from scratch here**](<https://www.dailydoseofds.com/formulating-the-principal-component-analysis-algorithm-from-scratch/>).

👉 Over to you: What are some other problems with using PCA for visualization?
