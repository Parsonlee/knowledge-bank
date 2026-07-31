---
title: "用一个 Python 装饰器部署 AI 应用（开源）"
source: "https://mail.google.com/mail/u/0/#inbox/198e2e9234d8b09f"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-25
created: 2026-07-30
description: "推广开源项目 Beam：它定位为 Modal 的替代方案，声称可通过 Python 装饰器部署无服务器 AI 工作负载。"
tags:
  - clippings
---

# 用一个 Python 装饰器部署 AI 应用（开源）

> [!note] 邮件推广内容
> 本节由 newsletter 作为开源项目推荐发布；以下功能与性能表述均为邮件中的项目主张。

![Beam 部署示意图](https://substack-post-media.s3.amazonaws.com/public/images/d877ecc7-b5a0-499f-a6d4-91c8a8519611_1199x1127.png)

[Beam](https://github.com/beam-cloud/beta9) 是一个开源的 [Modal](https://modal.com/) 替代方案，旨在以零基础设施开销部署无服务器 AI 工作负载。

## 使用步骤

1. 安装客户端：

   ```bash
   uv add beam-client
   ```

2. 构建 AI 工作流。
3. 将调用逻辑封装在一个方法中。
4. 使用 `@endpoint` 装饰器，并指定服务器配置。

## 邮件列出的特性

- 容器启动速度很快；
- 支持分布式卷存储；
- 可从 0 自动扩展至数百个容器；
- 支持 4090、H100，或自带 GPU；
- 可用简单装饰器部署推理端点；
- 可为 LLM 生成的代码启动隔离沙箱。

## 链接

- [Beam GitHub 仓库](https://github.com/beam-cloud/beta9)
