---
title: An intuitive guide to non-linearity of ReLU
source_key: dailydoseofds
email_subject: Your Agent Harness Should Repair Itself
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Mon, 08 Jun 2026 21:15:47 +0000
email_id: 19ea91777352c092
article_id: 19ea91777352c092:1
published: '2026-06-08'
tags:
- DeepLearning
---

# An intuitive guide to non-linearity of ReLU

- **原邮件主题**: Your Agent Harness Should Repair Itself
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Mon, 08 Jun 2026 21:15:47 +0000
- **ID**: 19ea91777352c092

---

## **An intuitive guide to non-linearity of ReLU**

Many ML engineers struggle to intuitively understand how ReLU adds non-linearity to a neural network because, with its seemingly linear shape, calling it a non-linear activation function isn’t that intuitive.

Today, let’s discuss an intuitive explanation of this!

* * *

This is the mathematical expression of the ReLU activation function:

![](https://substackcdn.com/image/fetch/$s_!viLi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbe940-eb44-42f0-8509-ceb5e581522e_522x82.png)   
---  
  
The above definition can be rewritten with a parameter `h` as follows:

![](https://substackcdn.com/image/fetch/$s_!Qy2n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3de8b850-a1bf-44ae-b089-392c4e567c42_1704x988.gif)   
---  
  
Effectively, it’s the same ReLU function but shifted `h` units to the right:

![](https://substackcdn.com/image/fetch/$s_!ajNC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51fd87ae-5184-4335-9234-b9f5089c2670_641x122.png)   
---  
  
Keep this in mind as we’ll return to it shortly.

* * *

# **Breaking down a neuron’s output**

Consider the operations carried out in a neuron:

![](https://substackcdn.com/image/fetch/$s_!MZqx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fa9de50-4dfa-43a9-9806-f87c9a519746_1000x488.png)   
---  
  
  * First, we have input from the previous layer (x₁, x₂, …, xₙ).
  * This is multiplied element-wise by the weights (w₁, w₂, …, wₙ).
  * Next, the bias term (`b`) is added, and every neuron has its own bias term.
  * The above output is passed through ReLU activation function to get its output activation.

This final output activation of a neuron is analogous to the `ReLU(x−h)` function discussed above.

![](https://substackcdn.com/image/fetch/$s_!Ba47!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffb448d8-0027-47bb-be66-cede15deec50_1000x346.png)   
---  
  
Now, consider all neurons in the last hidden layer:

![](https://substackcdn.com/image/fetch/$s_!-CmP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6f0e22a-8434-49c1-b5ab-9283a2bad9bc_1000x391.png)   
---  
  
The final output of the whole network will be a weighted sum of differently shifted ReLU activations computed in the last hidden layer.

![](https://substackcdn.com/image/fetch/$s_!D0nO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa323bb08-0368-49d7-bb19-59d2b73633e4_579x290.png)   
---  
  
* * *

# **Plotting dummy ReLU units**

Now, let’s plot the weighted sum of some differently shifted ReLU functions to see what this plot looks like.

Starting with two terms, we notice a change in slope at a point:

![](https://substackcdn.com/image/fetch/$s_!S1Zr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F141beb46-2264-41ba-b178-8a1b14acdbfc_1020x500.png)   
---  
  
Adding more ReLU terms to this results in more bends:

![](https://substackcdn.com/image/fetch/$s_!4FQ9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ce4378b-7574-4443-8371-c7462c3c5aa7_888x395.png)   
---  
  
And adding one more produces one more bend:

![](https://substackcdn.com/image/fetch/$s_!uTJt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdb31bf3-dbe5-4701-9981-fdeefaa75165_1020x527.png)   
---  
  
This indicates we can add more and more ReLU terms, each shifted and multiplied by some constant, to estimate any function, linear or non-linear:

![](https://substackcdn.com/image/fetch/$s_!lQc7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f80a189-6cd7-407c-a83f-adf1463dca80_731x249.png)   
---  
  
The task is to find those specific weights (w₁, w₂, …, wₙ) which closely estimate the function `f(x)`.

Theoretically, the precision of approximation will be perfect if we add a `ReLU` term for each possible value of `x`.

* * *

# **X-squared demo**

Let’s say we want to approximate `y=x^2` for all `x ∈ [0,2]`.

Approximating with just one `ReLU` term → `ReLU(x)`, we get:

![](https://substackcdn.com/image/fetch/$s_!s2Kt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe728d665-103c-4dcb-a27d-db4c752fb570_1000x447.png)   
---  
  
Next, we add another ReLU term and plot `ReLU(x) + ReLU(x−1)`, which produces the green line below and it is a better approximation:

![](https://substackcdn.com/image/fetch/$s_!TN7L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc57784a9-d4e7-489c-aafd-4cb67e041bae_1000x505.png)   
---  
  
Next, by adjusting the weights, we get the blue line, which approximates this even more precisely:

![](https://substackcdn.com/image/fetch/$s_!0WaK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefcd20fb-ea9a-4d6a-a5ce-761a41d208f1_1000x505.png)   
---  
  
* * *

This is exactly how ReLU induces non-linearity in a neural network.

That said, ReLU NEVER adds perfect non-linearity to a neural network. Instead, it’s the piecewise linearity of ReLU that gives us a perception of a non-linear curve.

Also, as we saw above, the strength of ReLU lies not in itself but in an entire army of ReLUs embedded in the network.

This is why having a few ReLU units in a network may not yield satisfactory results.

This is also evident from the image below, where as the number of ReLU units increases, the approximation also becomes better and at 100 ReLU units, the approximation appears entirely non-linear:

![](https://substackcdn.com/image/fetch/$s_!dgOC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36c5cfb7-8465-415c-bf64-fc46bc2c9895_1456x1229.png)   
---  
  
And this is precisely why ReLU is called a non-linear activation function.

That said, KANs are another popular neural network paradigm that challenges the traditional neural network design and offers an exciting new approach to design and train them:

![](https://substackcdn.com/image/fetch/$s_!SOIk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9bff9550-28cd-468d-8cd8-5864d9dfcd3f_1456x548.png)   
---  
  
We did a detailed breakdown and implemented them from scratch here: [**Implementing KANs From Scratch Using PyTorch**](<https://fff97757.click.kit-mail3.com/gkukxk8wqdf5hl8x95ourh8olx6pzfmho2n00/wnh2hghqp29xezt7hx/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vaW1wbGVtZW50aW5nLWthbnMtZnJvbS1zY3JhdGNoLXVzaW5nLXB5dG9yY2gv>).
