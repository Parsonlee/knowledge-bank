---
title: "应用于不可验证任务（Application to non-verifiable tasks）"
source: "https://mail.google.com/mail/u/0/#inbox/19dd11ff55feb3f6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-27
created: 2026-07-30
description: "探讨了 RULER 在处理缺乏确定性答案的纯主观任务或混合任务中的优势及应用方式。"
tags:
  - clippings
---

# 应用于不可验证任务（Application to non-verifiable tasks）

RULER 是通用的，适用于任何任务。对于纯确定性任务，二进制验证器成本更低且信号清晰；但对于纯主观任务（如总结质量），RULER 是唯一的自动化选项。对于介于两者之间的任务（例如：代理是否找到了正确答案，并且解释得很好？），你可以结合两者：保留单独定义的确定性验证评分，并在其之上叠加 LLM 裁判的评分，从而不丢失任何维度的信号。
