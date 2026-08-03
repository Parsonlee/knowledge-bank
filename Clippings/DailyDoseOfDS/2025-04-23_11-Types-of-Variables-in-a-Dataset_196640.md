# 11 Types of Variables in a Dataset

- **原邮件主题**: 11 Types of Variables in a Dataset
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Wed, 23 Apr 2025 18:56:17 +0000
- **ID**: 19664020d007efe2

---

## **11 Types of Variables in a Dataset**

In any tabular dataset, we typically categorize the columns as either a feature or a target.

However, there are so many variables that one may find/define in their dataset, as shown below:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74dcd89e-96e0-4a1a-864e-bf4a2abc2539_1204x1072.gif)   
---  
  
Let’s understand today!

# **#1-2) Independent and dependent variables**

Independent variables are the features that are used as input to predict the outcome. They are also referred to as predictors/features/explanatory variables.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1782c63-bd12-4dc3-a78f-29043378288b_1720x696.png)   
---  
  
The dependent variable is the outcome that is being predicted. It is also called the target, response, or output variable.

# **#3-4) Confounding and correlated variables**

Confounding variables are usually found in a cause-and-effect study ([**causal inference**](<https://www.dailydoseofds.com/a-crash-course-on-causality-part-1/>)).

These are not always of primary interest, but can lead to weird associations if not handled correctly.

Say we want to measure the effect of ice cream sales on the sales of air conditioners, both of which are highly correlated:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49e31e3c-d9e9-484a-be90-a20646b289dd_1664x688.png)   
---  
  
However, there’s a confounding variable—**temperature** , which influences both ice cream sales and the sales of air conditioners.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9da17703-973f-4987-b451-92a6e76ed65c_1904x676.png)   
---  
  
To study the actual causal impact, one must consider the confounder (temperature). Otherwise, the study will produce misleading results.

It is due to the confounding variables that we say, “Correlation does not imply causation.”

We did a crash course on Causal inference some time back:

\- [**A Crash Course on Causality – Part 1**](<https://www.dailydoseofds.com/a-crash-course-on-causality-part-1/>)

\- [**A Crash Course on Causality – Part 2**](<https://www.dailydoseofds.com/a-crash-course-on-causality-part-2/>)

# **#5) Control variables**

In the above example, we must ensure that the temperature is controlled to measure the true effect of ice cream sales on AC sales.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee226325-30cb-48ae-84b5-00abe1e9af41_1996x676.png)   
---  
  
Once controlled, temperature becomes a **control variable**.

These variables are not the primary focus of the study, but are crucial to account for. This ensures that the effect we intend to measure is not biased or confounded by other factors.

# **#6) Latent variables**

A variable that is not directly observed but is inferred from other observed variables.

For instance, there is no true label in clustering—it is a latent variable.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6dd05f0-e18f-4cd3-a54a-09a23fabb19f_1700x700.png)   
---  
  
We also learned about Latent variables when we implemented [**Gaussian mixture models**](<https://www.dailydoseofds.com/gaussian-mixture-models-gmm/>) from scratch.

# **#7) Interaction variables**

They measure the interaction effect between two or more variables and are often used in regression analysis.

For instance, if you have two variables:

  * Population density → HIGH, MEDIUM, and LOW (one-hot encoded).
  * Income levels → HIGH, MEDIUM, and LOW (one-hot encoded).

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F030349a9-a413-40d7-a304-36f154c93ec4_1724x676.png)   
---  
  
You can multiply them to get interaction variables, which will produce 9 interaction variables. Studying them will likely produce better insights.

# **#8-9) Stationary and Non-Stationary variables:**

Stationary variables are those whose statistical properties (mean, variance) DO NOT change over time.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cacb56f-4600-4b70-9db4-87a8397b4401_2012x800.png)   
---  
  
If it does, the variable is called a non-stationary variable.

Preserving stationarity is critical in statistical learning because these models assume samples are identically distributed. That is why using direct values of the non-stationary feature (like stock price) is not recommended.

Instead, it is better to define features in terms of relative changes:

# **#10) Lagged variables**

A lagged variable represents previous time points’ values of a given variable:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F443c07c5-da56-4caa-9818-410d989313a4_1852x676.png)   
---  
  
For instance, when predicting next month’s sales figures, we might include the sales figures from the previous month as a lagged variable.

Lagged features may include:

  * 7-day lag on website traffic to predict current website traffic.
  * 30-day lag on stock prices to predict the next month’s closing prices.
  * And so on…

# **#11) Leaky variables**

These variables provide information about the target variable that would not be available during prediction.

This leads to overly optimistic model performance during training but fails to generalize to new data.

For instance, creating forward-lag features leads to a leaky variable:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0d3a730-ede6-416f-83e4-5b33d45f4ffe_1852x676.png)   
---  
  
That’s a wrap!

👉Over to you: Have we missed any variable types?
