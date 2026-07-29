title: Bright Data CLI & Scraper Studio：将任意网页转化为自定义 API source: https://mail.google.com/mail/u/0/#inbox/19edcc2a8ec8a790 author:


* "[[DailyDoseOfDS]]" published: 2026-06-18 created: 2026-07-28 description: 解决 Claude Code 中 web_fetch 摘要限制与 curl 反爬阻断问题，通过 Scraper Studio 自然语言构建自修复的网页抓取 API。 tags:
* clippings


________________


Bright Data CLI & Scraper Studio：将任意网页转化为自定义 API
在 Claude Code 等 Agent 终端中，内置的 web_fetch 仅返回截断摘要，而 curl 经常触发反爬封禁。


Bright Data Scraper Studio 结合开源 CLI，允许开发者通过自然语言直接定义需抓取的网页与目标字段：


* 自动生成与挂载 API：自动生成应对 CAPTCHA 与动态渲染的 Collector，并发布为标准 REST API。
* 自然语言自修复：当目标网页结构发生变更时，无需重新编写 CSS Selector，直接通过自然语言命令完成抓取逻辑的自愈修复。