---
title: "[Hands-on] Build your own 100% local AI second brain."
source: "https://mail.google.com/mail/u/0/#inbox/19e0470d88335c78"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-07
created: 2026-07-30
description: "实战指南：使用开源工具 Rowboat 构建 100% 本地运行的 AI 第二大脑，将 Gmail、日历与会议记录转化为自演进的知识图谱。"
tags:
  - clippings
---

# [实战] 构建 100% 本地的 AI 第二大脑（[Hands-on] Build your own 100% local AI second brain.）

Karpathy 曾提出过利用 LLM 构建个人 Wiki 知识库的模式。本文将介绍如何使用开源项目 **Rowboat** 在本地构建一个 100% 私密、自动演进的 AI 第二大脑。

与传统 Wiki 编译静态概念页面不同，Rowboat 捕捉的是真实工作流中不断演进的人际、项目与决策关联。

---

### 结构与配置

Rowboat 将所有数据以标准 Markdown 格式保存在本地目录 `~/.rowboat/` 中，零格式锁定：

![Rowboat CLI 启动与配置](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6a742ee-e6f1-4a6a-bb03-5119f0d662ca_679x212.png)

你可以随意选择本地模型（如 Ollama、LM Studio）或云端 LLM Provider（OpenAI, Anthropic, OpenRouter）：

![模型 Provider 配置](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b5a8a77-a753-47ab-b057-fb20f6905b01_679x579.png)

![托管 API 配置](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6021554-ff5e-4377-a876-f4a42d0c5bf7_680x571.png)

![UI 设置中的密钥绑定](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6daff8a0-5159-4db8-b90a-98afa7588eda_680x467.png)

连接 Google OAuth 凭据后，系统能安全无缝地同步 Gmail、Calendar 以及 Drive 数据：

![Google OAuth 同步流程](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e072a61-28be-4ff4-a169-85888533eb65_680x635.png)

首次同步完成后，知识图谱开始构建：

![同步完成图谱准备就绪](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59c609d6-420b-445c-a1d7-0623a2c37f11_680x445.png)

---

### 本地 Vault 目录结构

同步后，`~/.rowboat/` 目录正式生效：

![磁盘上的 Vault 结构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbeb31673-1dc4-4299-8cd1-39c041dfae9e_680x419.png)

核心知识沉淀在 `knowledge/` 目录中：

![knowledge 目录架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4db3dce-d50e-4994-8b77-1e1c768cb875_680x419.png)

包含了 `People/`, `Organizations/`, `Projects/`, `Topics/` 等子文件夹：

![实体分类文件夹](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5d4cf07-32e6-4e13-bfc8-40bb8d9e7f89_680x283.png)

**精妙的设计抉择**：Rowboat 不会盲目为垃圾邮件或营销链接创建实体，只有积累了实质信号后才会创建对应的实体 Markdown 文件。

---

### 知识图谱查询与交互

你可以对构建好的图谱进行自然语言查询：

![查询 Sarah 的最新进展与返回简报](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8530385-d0db-4e75-af52-a1acfaeddd6a_680x428.png)

在返回的简报中，所有 `[[entity]]` 均为可点击的双向链接，点击可跳转至底层实体节点：

![点击双向链接查看实体节点细节](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe97f9824-21f1-4c5e-b892-5a4cbf0d4ac7_680x428.png)

询问日程会议上下文：

![查询今日会议背景信息](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff43c9ad2-232a-45ed-9cd9-8225d67aa9bb_680x359.png)

---

### 知识图谱随时间演进

随着新邮件与会议不断涌入，新信号会自动附加到现有实体节点上：

![知识图谱随时间增长不断变密](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c189cd4-baaa-496f-82e6-8b356de31ac0_679x370.png)

当联系人发送最新反馈时，更新会直接追加至原有的实体节点中，而不会生成重复文件：

![实体节点动态追加与演进](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73f5b093-ceef-4175-b293-2bfd6189e112_680x187.png)

Rowboat 完全本地运行、Apache-2.0 开源，所有文件纯 Markdown 存储，保证了极高的隐私防护与自主可控性：

![安全架构与总结](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a28fe2f-0085-4f14-871e-7d15fb7fd47e_680x370.png)

GitHub 开源地址：`github.com/rowboatlabs/rowboat`
