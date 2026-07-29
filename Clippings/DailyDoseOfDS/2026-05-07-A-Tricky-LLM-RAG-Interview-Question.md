title: 一道棘手的大模型 RAG 面试题 source: https://mail.google.com/mail/u/0/#inbox/19e0470d88335c78 author:

"[[DailyDoseOfDS]]" published: 2026-05-07 created: 2026-07-28 description: 探讨为什么 RAG 系统在 5k 文档时检索准确率达 90%，扩大到 500k 文档时准确率会暴跌至 50%，并介绍 EnterpriseRAG-Bench 测试集。 tags:

clippings

# 一道棘手的大模型 RAG 面试题

面试题：为什么同一个 Embedding 模型，RAG 系统的检索准确率在 5 千份文档时为 90%，规模扩大到 50万份文档时暴跌至 50%？

## 根因分析

企业文档在 Embedding 空间中的分布存在高邻域密度（Neighborhood Density）。同一项目产生的 Slack 讨论、Jira 单子、Confluence 文档和邮件都在极小区域内聚类。随着文档量级增加，包含真正正确事实的那个 Chunk 很容易被大量主题相似的干扰 Chunk 挤出 Top-K 检索列表。
