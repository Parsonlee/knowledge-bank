---
title: Simplify Python imports with explicit packaging
source_key: dailydoseofds
email_subject: Data and Pipeline Engineering for ML Systems (With Implementation)
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Sat, 30 Aug 2025 19:20:34 +0000
email_id: 198fc6ca70584770
article_id: 198fc6ca70584770:1
published: '2025-08-30'
tags:
- Skill/python
---

# Simplify Python imports with explicit packaging

- **原邮件主题**: Data and Pipeline Engineering for ML Systems (With Implementation)
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Sat, 30 Aug 2025 19:20:34 +0000
- **ID**: 198fc6ca70584770

---

## **Simplify Python imports with explicit packaging**

Python lets us package a project by adding an `__init__.py` file inside a directory.

If you have ever been confused about the internal details of the `__init__.py` file, today’s issue with help.

Let’s understand!

* * *

# **Packaging in Python**

Simply put, if a project is packaged, you can import stuff from it.

While Python 3.3+ provides **Implicit Namespace Packages** , which means a directory with modules is considered a package by default, it is still advised to create an explicit `__init__.py` file.

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/5yHkqwZgoPD7T3rEouKiSQ/email)   
---  
  
A couple of major benefits of doing this are that it helps in:

  * Explicitly specifying which classes/functions can be imported from the package.
  * Avoiding redundant imports.

* * *

Some terminology before proceeding ahead:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/7aLjgqn4cYzmMeHC2CyeN1/email)   
---  
  
  * Module: A Python file.
  * Package: A collection of Python files in a directory.
  * Library: A collection of Packages.

* * *

Consider this is our directory structure (and we are using Python 3.3+):

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/cf7E4HwpcKDjeygYKynvsq/email)   
---  
  
  * `train.py` has a `Training` class.
  * `test.py` has a `Testing` class.

As we are using Python 3.3+, we can directly import the `Training` and `Testing` class in `pipeline.py` as follows:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/mf2sDVsNayYwN1jo3myWLk/email)   
---  
  
While this will work as expected, the problem is that we have to explicitly import the specific class from each of the modules.

This creates redundant imports.

Defining the `__init__.py` file can simplify this.

Let’s see how.

![](https://substackcdn.com/image/fetch/$s_!6ReI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcca20f5e-ff1a-4af4-a960-ccb30cdd5cc6_3040x1244.png)   
---  
  
As depicted above:

  * We first explicitly package the directory by creating an `__init__.py` file.
  * Next, we specify the imports directly in this file.

Now, instead of writing redundant imports, you can directly import the intended classes from the “**model** ” package, as shown below:

![](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/9EVjEkeusVqSaS45NYo5Ci/email)   
---  
  
In other words, specifying the `__init__.py` file lets you treat your package like a module.

This simplifies your imports.

Also, as discussed earlier, an `__init__.py` file lets you explicitly specify which classes/functions can be imported from the package, which, otherwise, will not be evident.

This simplifies things for other users of your project.

Isn’t that cool?

👉 Over to you: What are some other Python project development insights you are aware of?

Thanks for reaching!
