---
title: 7 Uses of Underscore in Python
source_key: dailydoseofds
email_subject: 7 Uses of Underscore in Python
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Fri, 31 Jan 2025 20:22:52 +0000
email_id: 194be07e12ab82bc
article_id: 194be07e12ab82bc:1
published: '2025-01-31'
tags:
- Skill/python
---

# 7 Uses of Underscore in Python

- **原邮件主题**: 7 Uses of Underscore in Python
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 31 Jan 2025 20:22:52 +0000
- **ID**: 194be07e12ab82bc

---

## **7 Uses of Underscore in Python**

Underscore (`_`) has so many usages in Python.

Today, I want to walk you through 7 of them.

* * *

# **#1) Retrieve the last computed value**

You can retrieve the last computed value, as demonstrated below:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc34bcb49-53f1-4884-85fb-ea1d02e6a94e_1456x695.png)   
---  
  
This works both in a script (`.py`) and an interactive environment like Jupyter Notebook.

* * *

# **#2) Placeholder for loop variable**

Instead of explicitly declaring a loop variable, you can also run loops as follows:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F447dbdfa-0b7b-4da0-b31f-0f9245f4e65a_1456x517.png)   
---  
  
* * *

# **#3) Digit separator**

When declaring large numbers, it can be difficult to interpret them. Underscore simplifies this:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facc2c87d-58d7-417a-a5fc-50966d0f59dd_1456x515.png)   
---  
  
* * *

# **# 4-7) Declaring names**

underscoresWe can also use underscore when naming objects.

  * A single leading underscore is used to declare variables for internal use. Thus, they cannot be imported during wild imports (`from file import *`)

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a19924b-1c57-4b50-843c-542ef3fa6816_1456x585.png)   
---  
  
  * A single trailing underscore is used to avoid conflict with reserved keywords, as depicted below:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3d2b997-2c28-4fc4-ad39-40c9851a3fd3_1456x571.png)   
---  
  
  * Double leading underscores are used to invoke name mangling. This way, one can prevent direct access to private variables outside a class:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fc0d05a-7ba9-4dba-b69a-20365950545f_1456x1395.png)   
---  
  
  * Finally, double leading and trailing underscores, as you may already know, are used to define magic methods:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a4f2b24-ea57-4391-a4bf-2726ea9d7309_1456x595.png)   
---  
  
This is a guide on the 20 most common magic methods in Python:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9550cb8-0231-47d3-9903-60e7e4ac8862_863x1128.png)   
---  
  
Done!

👉 Over to you: Which usage of underscore is your favorite?
