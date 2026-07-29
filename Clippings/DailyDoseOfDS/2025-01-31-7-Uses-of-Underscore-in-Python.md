---
title: 7 Uses of Underscore in Python
source: https://mail.google.com/mail/u/0/#inbox/194be07e12ab82bc
author:
  - "[[DailyDoseOfDS]]"
published: 2025-01-31
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 7 Uses of Underscore in Python 的原理剖析与工程实践。
tags:
  - clippings
---

# 7 Uses of Underscore in Python

## 1. 核心要点解析

本期内容重点涵盖：
- **7 Uses of Underscore in Python**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/lmu9m96v3wcmhn0ed8li6h8lo4v00bg/3ohphkh7w2rxvear/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Bright Data: Collect public web data in real-time at scale
* 7 Uses of Underscore in Python

Reading time: 3 minutes.

TODAY'S ISSUE

Together with bright data
-------------------------

-----------------------------------------------------------------
​Bright Data: Collect public web data in real-time at scale (
https://click.convertkit-mail2.com/lmu9m96v3wcmhn0ed8li6h8lo4v00bg/48hvhehrop9wk7fx/aHR0cHM6Ly9icmlnaHRkYXRhLmNvbS8_cHJvbW89ZGFpbHlkb3Nlb2ZkcyZ1dG1fY2FtcGFpZ249YnJuZC1ta3RfcGFydG5lcl9kYWlseWRvc2VvZmRzX05MMSZ1dG1fc291cmNlPWJyYW5k
)​
-----------------------------------------------------------------

(
https://click.convertkit-mail2.com/lmu9m96v3wcmhn0ed8li6h8lo4v00bg/48hvhehrop9wk7fx/aHR0cHM6Ly9icmlnaHRkYXRhLmNvbS8_cHJvbW89ZGFpbHlkb3Nlb2ZkcyZ1dG1fY2FtcGFpZ249YnJuZC1ta3RfcGFydG5lcl9kYWlseWRvc2VvZmRzX05MMSZ1dG1fc291cmNlPWJyYW5k
)​
Building AI apps capable of interacting with real-time web data
can feel impossible. Here are the challenges:

* You must simulate human-like interactions.
* You must overcome site blocks and captchas.
* You must scrape accurate and clean data at scale.
* You must ensure compliance with all legal standards.

​Bright Data (
https://click.convertkit-mail2.com/lmu9m96v3wcmhn0ed8li6h8lo4v00bg/48hvhehrop9wk7fx/aHR0cHM6Ly9icmlnaHRkYXRhLmNvbS8_cHJvbW89ZGFpbHlkb3Nlb2ZkcyZ1dG1fY2FtcGFpZ249YnJuZC1ta3RfcGFydG5lcl9kYWlseWRvc2VvZmRzX05MMSZ1dG1fc291cmNlPWJyYW5k
) provides the complete infrastructure to handle data extraction,
user simulation, and real-time interactions for your AI apps
across the web.

With Bright Data (
https://click.convertkit-mail2.com/lmu9m96v3wcmhn0ed8li6h8lo4v00bg/48hvhehrop9wk7fx/aHR0cHM6Ly9icmlnaHRkYXRhLmNvbS8_cHJvbW89ZGFpbHlkb3Nlb2ZkcyZ1dG1fY2FtcGFpZ249YnJuZC1ta3RfcGFydG5lcl9kYWlseWRvc2VvZmRzX05MMSZ1dG1fc291cmNlPWJyYW5k
), you can:

* Access clean data from any public website with ease.
* Simulate user behaviors at scale using advanced browser-based
tools.
* Enable AI models to retrieve real-time insights with a seamless
Search API.

​Bright Data (
https://click.convertkit-mail2.com/lmu9m96v3wcmhn0ed8li6h8lo4v00bg/48hvhehrop9wk7fx/aHR0cHM6Ly9icmlnaHRkYXRhLmNvbS8_cHJvbW89ZGFpbHlkb3Nlb2ZkcyZ1dG1fY2FtcGFpZ249YnJuZC1ta3RfcGFydG5lcl9kYWlseWRvc2VvZmRzX05MMSZ1dG1fc291cmNlPWJyYW5k
) is the fastest way to take your AI apps to the next level.

-->Start collecting data today (
https://click.convertkit-mail2.com/lmu9m96v3wcmhn0ed8li6h8lo4v00bg/48hvhehrop9wk7fx/aHR0cHM6Ly9icmlnaHRkYXRhLmNvbS8_cHJvbW89ZGFpbHlkb3Nlb2ZkcyZ1dG1fY2FtcGFpZ249YnJuZC1ta3RfcGFydG5lcl9kYWlseWRvc2VvZmRzX05MMSZ1dG1fc291cmNlPWJyYW5k
)
Start collecting data today (
https://brightdata.com/?utm_source=brand&utm_campaign=brnd-mkt_partner_dailydoseofds_NL1&promo=dailydoseofds
)Thanks to Bright Data (
https://click.convertkit-mail2.com/lmu9m96v3wcmhn0ed8li6h8lo4v00bg/48hvhehrop9wk7fx/aHR0cHM6Ly9icmlnaHRkYXRhLmNvbS8_cHJvbW89ZGFpbHlkb3Nlb2ZkcyZ1dG1fY2FtcGFpZ249YnJuZC1ta3RfcGFydG5lcl9kYWlseWRvc2VvZmRzX05MMSZ1dG1fc291cmNlPWJyYW5k
) for partnering today.

Today's daily dose of data science
----------------------------------

------------------------------
7 Uses of Underscore in Python
------------------------------

Underscore (_) has so many usages in Python.

Today, I want to walk you through 7 of them.

************************************
#1) Retrieve the last computed value
************************************

You can retrieve the last computed value, as demonstrated below:

​
This works both in a script (.py) and an interactive environment
like Jupyter Notebook.

*********************************
#2) Placeholder for loop variable
*********************************

Instead of explicitly declaring a loop variable, you can also run
loops as follows:

​

*******************
#3) Digit separator
*******************

When declaring large numbers, it can be difficult to interpret
them. Underscore simplifies this:

​

*********************
#4-7) Declaring names
*********************

underscoresWe can also use underscore when naming objects.

* A single leading underscore is used to declare variables for
internal use. Thus, they cannot be imported during wild imports
(from file import *)

​
* A single trailing underscore is used to avoid conflict with
reserved keywords, as depicted below:

​
* Double leading underscores are used to invoke name mangling.
This way, one can prevent direct access to private variables
outside a class:

​
* Finally, double leading and trailing underscores, as you may
already know, are used to define magic methods:

​
This is a guide on the 20 most common magic methods in Python:

​
Done!

👉 Over to you: Which usage of underscore is your favorite?

THAT'S A WRAP

NO-FLUFF DS/ML RESOURCES TO...
------------------------------

-----------------------------------------------------------------
​Succeed in DS/ML roles (
https://click.convertkit-mail2.com/lmu9m96v3wcmhn0ed8li6h8lo4v00bg/wnh2hghwzk4m8dt7/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcA==
)​
-----------------------------------------------------------------

​
All businesses care about impact. That’s it!

* Can you reduce costs?
* Drive revenue?
* Can you scale ML models?
* Predict trends before they happen?

We have discussed several other topics (with implementations) in
the past that align with such topics.

-->Develop Industry ML skills (
https://click.convertkit-mail2.com/lmu9m96v3wcmhn0ed8li6h8lo4v00bg/wnh2hghwzk4m8dt7/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcA==
)
Develop Industry ML skills (
https://www.dailydoseofds.com/membership )Here are some of them:

* Learn how to build real-world RAG app

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。
