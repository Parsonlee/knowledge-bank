title: 使用 Claude Code 实战构建 3D 天气地球仪 source: https://mail.google.com/mail/u/0/#inbox/19e84f32570b4582 author:


* "[[DailyDoseOfDS]]" published: 2026-06-01 created: 2026-07-28 description: 展示如何通过单条 Prompt 引导 Claude Code 利用 Tiger Cloud (TimescaleDB) 与 Three.js 快速搭建包含昼夜交替与 10 天预报的 3D 全栈天气仪表盘。 tags:
* clippings


________________


使用 Claude Code 实战构建 3D 天气地球仪
只需给出一条精准的 Prompt，Claude Code 就能在单次会话中独立完成从数据库初始化、表结构设计、2.5 万条气象数据灌入，到基于 Next.js 与 Three.js 构建 3D 可视化前端的全栈开发。
核心亮点
* 3D 交互地球仪：使用 NASA 卫星图像模拟昼夜交替与夜间城市灯光，气象图标根据当地时间自动切换日月形态。
* 时间滑块（Time Travel Slider）：支持滑动检索过去 10 天及未来 3 天的预报数据。
* 后端支撑：运行于 Tiger Cloud (托管于 Postgres 之上的 TimescaleDB)，通过时间戳自动对数据进行 Hypertable 分区与连续聚合（Continuous Aggregates），确保高频滑动查询依然保持毫秒级响应。