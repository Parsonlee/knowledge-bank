---
title: "Build production-grade MCP servers"
source: "https://mail.google.com/mail/u/0/#inbox/19c010d600302f25"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-01-27
created: 2026-07-30
description: "介绍如何利用 Postman MCP Generator 无代码快速构建 100% 本地运行的生产级 Model Context Protocol (MCP) 服务端。"
tags:
  - clippings
---

# 构建生产级 MCP 服务端（Build production-grade MCP servers）

构建生产级 **MCP (Model Context Protocol)** 服务端迎来了一种全新高效范式：
* **耗时不到 1 分钟**。
* **零代码编写**。
* **轻松集成 100,000+ API 工具**。

本文将讲解如何利用该工具构建一个 100% 本地运行的 MCP 服务端。

## 1. 传统开发与 Postman MCP Generator 的对比

从零构建带有自定义工具的 MCP 服务器往往需要：
1. 阅读庞大的第三方 API 文档。
2. 编写 MCP 工具逻辑代码。
3. 繁琐的测试与配置调试。

Postman 推出的 **MCP Generator** 将这一过程大幅简化，允许开发者直接从 Postman 的公共 API 网络（包含超过 10 万个 API）中挑选任意工具一键生成代码。

![图 1：Postman MCP Generator 无代码工具构建面板](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F552ad51b-a2b4-45fe-90db-38930593a27a_1080x1080.png)
*说明：图 1：Postman MCP Generator 无代码工具构建面板*

## 2. 操作步骤

1. **选择 API 工具**：在 Postman API Network 中搜索并勾选所需 API（例如 Hacker News 的 `get_story`、`fetch_top_stories`、`fetch_best_stories`、`fetch_new_stories` 等）。
2. **导出代码**：点击 "Generate" 生成并下载完整的服务器代码压缩包。
3. **安装依赖**：解压压缩包后，在终端运行 `npm install`。
4. **配置客户端**：在 Claude Desktop 的 `Settings -> Developer -> Edit Config` 中更新配置文件 JSON，配置 node 执行路径与服务器入口。

![图 2：从 API 网络选择工具并生成服务器代码](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F929f2f8c-c1e3-4ca0-8552-69b849d0cfed_1200x837.png)
*说明：图 2：从 API 网络选择工具并生成服务器代码*

![图 3：Claude Desktop 的 MCP JSON 配置界面](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F664ce951-2860-44dc-8b0f-f02d91508902_1200x829.png)
*说明：图 3：Claude Desktop 的 MCP JSON 配置界面*

![图 4：在 Claude 中流畅交互调用生成的 MCP 工具](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b694401-0631-433d-9a34-7174b9174ca8_1200x640.png)
*说明：图 4：在 Claude 中流畅交互调用生成的 MCP 工具*

![图 5：MCP 构建与部署流程全景复盘](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b0f3b5a-f817-4dd5-9e84-c2c45c0d50d8_1200x829.png)
*说明：图 5：MCP 构建与部署流程全景复盘*
