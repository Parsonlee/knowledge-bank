title: "在 Claude Code 中将任意网页转化为自定义 API" source: "https://mail.google.com/mail/u/0/#inbox/19edcc2a8ec8a790" author:

"[[DailyDoseOfDS]]" published: "2026-06-18" created: "2026-07-28" description: "结合 Bright Data CLI 与 Scraper Studio，通过自然语言生成定制化爬虫与 API，轻松绕过反爬与验证码提取任意网页数据。" tags:

clippings

# 在 Claude Code 中将任意网页转化为自定义 API

Claude Code 内置的 web_fetch 和 web_search 并非为深度抓取而设计，而普通 curl 容易被反爬屏蔽。

Bright Data CLI 与新推出的 Scraper Studio 彻底改变了这一局面：

内置 40+ 平台提取器：直接支持 Amazon、LinkedIn、Reddit、YouTube 等主流站点。

自然语言生成自定义爬虫：对于未预建提取器的网站（如 Substack），只要提供网页与目标字段，CLI / Scraper Studio 就会自动生成采集器（Collector）并发布为可调用的 API。

自动修复（Auto-repair）：当网站前端页面布局变更导致字段为 undefined 时，可在 Scraper Studio 中用自然语言直接修复爬虫。
