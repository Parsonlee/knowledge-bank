---
title: "[Hands-on] Build a 3D weather globe with Claude Code."
source: "https://mail.google.com/mail/u/0/#inbox/19e84f32570b4582"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-01
created: 2026-07-30
description: "实战教程：利用 Claude Code 从零构建 3D 交互式全球天气地球仪应用，涵盖后端 Setup 与 Prompt 工程实践。"
tags:
  - clippings
---

# [实战] 使用 Claude Code 构建 3D 天气地球仪（[Hands-on] Build a 3D weather globe with Claude Code.）

本实战演练展示了如何利用 Claude Code 命令行 Agent 从零构建一个全栈 3D 交互式全球天气地球仪。

![3D 天气地球仪成品效果](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F525dc9d7-9514-4e68-8abf-2867611dd54d_1080x1080.png)

---

### 1. 后端构建（Setting up the backend）

通过 Claude Code 的命令行协作能力：
* 快速集成第三方 Open-Meteo 天气数据 API；
* 搭建轻量级 Node.js / Python 路由服务，将天气数据转换为前端 3D 控件所需的经纬度与气象特征流。

---

### 2. 提示词与交互调优（The Prompt）

向 Claude Code 提交结构化的需求 Prompt，指导其完成依赖安装、绑定 Three.js / Globe.gl 渲染库，并自动修正前端跨域与 3D 粒子渲染性能瓶颈。

![Claude Code 提示词交互过程](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F03e4dcb5-99c1-4c1e-9180-e014f857c4f8_1807x1358.png)
