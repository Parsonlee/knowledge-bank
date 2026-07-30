---
title: "Turn any website into a custom API."
source: "https://mail.google.com/mail/u/0/#inbox/19edcc2a8ec8a790"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-18
created: 2026-07-30
description: "实战演练：在 Claude Code 中结合 Bright Data CLI 与 Scraper Studio，将任意网页秒级转化为自定义 API。"
tags:
  - clippings
---
# 在 Claude Code 中将任意网站转化为自定义 API（Turn any website into a custom API.）

在智能体协作开发中，Claude Code 默认提供了 `web_fetch` 与 `web_search` 工具，但在复杂数据抓取场景下存在明显局限：
* `web_fetch` 会将网页送入较小模型总结，并对引用长度进行硬性限制（最多 125 字符），无法提取完整规格或长帖子内容；
* `curl` 容易触发 Amazon、LinkedIn 等防爬机制及 CAPTCHA 拦截，且无法渲染 JavaScript 动态页面。

**Bright Data CLI** 与新推出的 **Scraper Studio** 彻底解决了这一难题。

---

## 1. Bright Data 基础设施与技能安装

![Bright Data CLI 工具架构图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e16b25e-8cf6-4791-bbe6-0e8b480f8865_1005x512.png)

可以通过命令行一键安装 Bright Data 技能和 CLI：

```bash
# 安装 Bright Data 核心技能库与 CLI
npx @brightdata/bdata-cli setup
```

该工具支持自动绕过 Bot 拦截、解决验证码，并针对 40+ 主流平台（Amazon, LinkedIn, YouTube, Reddit 等）提供了预置提取器。

---

## 2. 利用 Scraper Studio 自然语言构建 API

![Scraper Studio 操作示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78eaef8c-51df-4e0e-b447-4843335e0b36_1198x639.png)

![生成提取字段与解析配置](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F290b4488-414f-4a29-b77c-ae7c5fefb698_1240x824.png)

在 Scraper Studio 中，只需提供目标 URL 和希望提取的字段名称（例如文章标题、作者、发布日期、正文）：

![在 Claude Code 中自动部署生成 API 端点](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F751c6daf-474e-42e1-805d-e17f508b015e_2090x700.png)

![API 数据流与自动修复机制图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67b2ab6d-bbda-4094-9e58-b4d71b2ec2c5_2078x888.png)

![解析输出对比示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8df489d-ee8f-425f-96de-6b4a2e33a1cd_1456x434.png)

通过自然语言指令，工具会自动分析 HTML 结构、生成抓取规则并发布为标准的 REST API Endpoint。当网页前端布局变更时，系统还会实现自动自愈与修复。
