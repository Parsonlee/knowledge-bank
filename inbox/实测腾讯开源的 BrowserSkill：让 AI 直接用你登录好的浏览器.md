---
title: "实测腾讯开源的 BrowserSkill：让 AI 直接用你登录好的浏览器"
source: "https://mp.weixin.qq.com/s/w3JLeJb4_8_uhVUqY7vqCw"
author:
  - "[[翻斗花园二蛋]]"
published:
created: 2026-07-01
description: "一句话：做一个本地桥接层，让 AI Agent 通过 CLI 命令控制你浏览器里的一个专属窗口，共享你的登录态，但不打扰你正常用浏览器。"
tags:
  - "clippings"
---
翻斗花园二蛋 翻斗花园二蛋 *2026年6月30日 19:04*

本文是真上手装了、跑了、读了源码、又跟另外四款方案横评之后写的。优缺点都给硬的，不写软文。

## 一、先说痛点

用 Cursor / Claude Code / Codex 写代码，顺手想让 AI 去浏览器里查个内网文档、在后台系统提个单、验收一下刚写的页面——结果常见三种翻车：

1. **AI 直接摆烂**
	："我无法访问网页。"
2. **上 Playwright / Selenium**
	：能跑，但你的内网后台要登录、SaaS 后台要登录。让 AI 自己走登录流程，要么失败，要么得把账号密码明文塞进 prompt——很不优雅。
3. **headless 自动化**
	：AI 另起一个浏览器实例，跟你 **抢窗口、抢标签页** ，有时候还把你正在测的东西给关了。

我自己最烦的是第 3 点：用 Playwright 每次都要 **等它冷启一个全新的 Chromium** ，而且那是另一个浏览器实例，跟我日常浏览器各玩各的——我正测着别的，它一跑可能就把我的环境搅了。

BrowserSkill 想解决的就是这对矛盾： **AI 想用浏览器，但它不会登录；它会自动化，但不能跟你共存。**

## 二、它是什么

腾讯 2026 年 6 月开源，github.com/Tencent/BrowserSkill <sup>[1]</sup> ， **MIT 协议** ，可商用可二开。

一句话： **做一个本地桥接层，让 AI Agent 通过 CLI 命令控制你浏览器里的一个专属窗口，共享你的登录态，但不打扰你正常用浏览器。**

![BrowserSkill 演示：左边终端里 Agent 跑 bsk 命令，右边橙色高亮的 Agent Window 在浏览网页](https://mmbiz.qpic.cn/sz_mmbiz_gif/GvmyiccCUFbyInbh5RuA0eQhuQJ47SwKTfIvf1l8P18gejjAW78sB4NMhVBIA0q2Mnv8blxuLpD7pgN4BK0h7ibg7nsKXmb5QYSHH76jIqZaw/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

BrowserSkill 演示：左边终端里 Agent 跑 bsk 命令，右边橙色高亮的 Agent Window 在浏览网页

上图是官方仓库的演示（已转 GIF）：左边是 Agent 在终端里发 `bsk` 命令，右边橙色描边的就是 Agent Window——它在动，但不抢你正在用的窗口。

## 三、架构（读源码 + 实测确认）

![BrowserSkill 架构：AI Agent → bsk CLI → bsk Daemon → 浏览器扩展 → Agent Window，全链路走 127.0.0.1 不外联](https://mmbiz.qpic.cn/sz_mmbiz_png/GvmyiccCUFby8va2caCsrZexIicftX01Vz4hXPyZVkZQBVTnXfRgqMThkhhvc76S2MdUmqSUH98so1lErevIDLL5B0iaFbqubLTJ72JEsM8dibc/640?from=appmsg&watermark=1#imgIndex=1)

BrowserSkill 架构：AI Agent → bsk CLI → bsk Daemon → 浏览器扩展 → Agent Window，全链路走 127.0.0.1 不外联

两个关键事实：

- **全链路在本机，不外联**
	。读了 `install.sh` 和扩展隐私声明，确认只走 `127.0.0.1` ，无 telemetry、无凭证上报。
- **对 Agent 来说 `bsk` 就是个普通 shell 命令**
	，跟 `curl` 没区别。所以它天然 agent 中立——实测 `bsk install-skill --list` 能自动检测出本机的 Claude Code、Codex、OpenClaw、CodeBuddy、WorkBuddy 等多个框架，一键写入各自的 skills 目录。

## 四、三步装 + 真实命令样例

**第一步：装 CLI**

```
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.sh | sh
# Windows PowerShell
irm https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.ps1 | iex
bsk --version    # 验证
```

它会把 `bsk` 装进 `~/.local/bin` 并写好 PATH，无 sudo、无 telemetry（脚本我逐行读过）。

**第二步：装浏览器扩展**

到 Chrome Web Store 搜 BrowserSkill 装上。⚠️ **装进你平时用的、已经登录了目标站点的那个浏览器** ——这是它复用登录态的前提。

**第三步：配置 Agent**

```
bsk install-skill          # 空格选框架，回车自动配置
```

**实际用起来的命令（我实测跑通的一套）：**

```
bsk browsers                            # 看连了哪些浏览器，拿 instance id
bsk session start --browser <id>        # 在指定浏览器开一个会话
bsk navigate --session <sid> https://example.com
bsk snapshot --session <sid>            # 输出带 @e1/@e2 编号的无障碍树
bsk click   --session <sid> @e12        # 按编号点
bsk fill    --session <sid> @e8 "hello"
bsk get-html --session <sid>            # snapshot 不够时看原始 DOM
bsk screenshot --session <sid>          # 最后才用截图
bsk request-help --session <sid>        # 遇验证码/登录，暂停交回给你
bsk session stop <sid>                  # 用完必须关，否则留下 Agent Window
```

实测最实用的是 `snapshot` ：它把页面可交互元素整理成带编号的树，AI 直接 `click @e12` ，比把整个 DOM 或截图丢给模型 **又稳又省 token** 。

实测一个细节：在一个登录态站点上，普通隔离浏览器（如全新 Playwright 实例）打开会被踢回登录页；而 BrowserSkill 用你已登录的浏览器打开， **直接就是登录后的页面** 。这就是它最大的卖点，确实成立。

## 五、跟其它四款横评

|  | **BrowserSkill** | **Playwright(MCP)** | **官方 Claude in Chrome** | **OpenClaw Relay** | **BrowserAct** |
| --- | --- | --- | --- | --- | --- |
| 用真实登录态 | ✅ | ❌ 全新实例无登录 | ✅ | ✅ | ✅(chrome 模式) |
| 桥接机制 | daemon+WS+CDP | 直接驱动新实例 | native messaging | CDP relay | CLI+多模式 |
| 读 console/network | ❌ | ✅ | ✅✅(主打调试) | ✅(CDP) | — |
| 截图 / GIF 录制 | 仅单张 PNG， **无 GIF** | 截图+视频 | **截图+会话录制为 GIF** | CDP 可截 | 截图 |
| 是否要你浏览器开着 | **要**  (用你现有浏览器) | 否(自己冷启) | 要 | 要 | 视模式 |
| 抢不抢你窗口 | 不抢(独立 Agent Window) | **会抢/会冷启** | 开新标签 | 点哪控哪 | 隔离 session |
| 扩展权限洁净度 | 中(`debugger` + `<all_urls>`) | 不需扩展 | 高(站点白名单) | **最高(debugger+仅localhost)** | 有确认门控 |
| 是否外联上报 | **否(纯本地)** | 否 | 会上报 URL 做策略 | 否 | — |
| agent 中立 | ✅ 任意 shell agent | ✅(MCP) | ❌ 仅 Claude | ❌ 仅 OpenClaw | ✅ |
| 鉴权要求 | **任意**  (authtoken/第三方API 都行) | 任意 | **必须官方账号登录** | 仅 OpenClaw 体系 | 任意 |
| 反爬/隔离模式 | 单一 | 一般 | — | — | **✅✅ 三模式隔离** |
| 开源 | ✅ MIT | ✅ | ❌ | 可读 | — |

一句话定位： **调试看官方，权限最克制看 OpenClaw，多账号隔离/反爬看 BrowserAct，要 CI/无人值守看 Playwright，登录态+agent 中立+纯本地看 BrowserSkill。**

### 更大的赛道全景：两大阵营

把视野放大，2026 年这波"给 Agent 装浏览器"的项目其实分成两个阵营，选型先看你要哪个：

![两大阵营：阵营 A 复用你已登录的真实浏览器（BrowserSkill/官方 Claude in Chrome/OpenClaw 等），阵营 B 是 Agent 优化的全新浏览器（Playwright MCP/Vercel agent-browser 等）；BrowserSkill 占位 agent 中立+纯本地](https://mmbiz.qpic.cn/sz_mmbiz_png/GvmyiccCUFbzSsq2khyHymXB87VcTibGTpgWo1M1SF3AEDhECTXvz0w5nj4vdnjDfZ3T8cGFqgUfHXlg3ULIdCp12ETdkbPHdauKvvLwR1iad0/640?from=appmsg&watermark=1#imgIndex=2)

两大阵营：阵营 A 复用你已登录的真实浏览器（BrowserSkill/官方 Claude in Chrome/OpenClaw 等），阵营 B 是 Agent 优化的全新浏览器（Playwright MCP/Vercel agent-browser 等）；BrowserSkill 占位 agent 中立+纯本地

**阵营 A：复用你已登录的真实浏览器** （适合内网/SaaS 后台、要登录态、人机协作）

- BrowserSkill（腾讯，本文主角）、官方 Claude in Chrome、OpenClaw Relay、GenericAgent
- BrowserAct 的 `chrome` 模式、Browserbase 的本地模式

**阵营 B：Agent 优化的全新浏览器** （适合无人值守、批量抓取、CI；但默认无登录态）

- Playwright MCP、Chrome DevTools MCP
- **Vercel agent-browser**
	（ `agent-browser.dev` ，上线一周冲到 9K star， `npm i -g` 自带 Chromium，实测首次成功率 ~95%，号称优于 Playwright MCP / Chrome DevTools MCP）
- BrowserAct 的 `stealth` 模式（指纹浏览器+住宅 IP，过 Cloudflare/DataDome/reCAPTCHA）、Browserbase 的云端隐身模式

BrowserSkill 是 **阵营 A 里"agent 中立 + 纯本地"那一格** ——这是它最清晰的占位。

### 一个行业已经收敛的最佳实践：Snapshot + 编号引用

值得单独点出来：BrowserSkill 的 `snapshot @eN` 、Vercel agent-browser 的 **Refs** 、BrowserAct 的 **state 编号树** ，三家不约而同走到了同一个设计—— **把页面可交互元素整理成带编号的快照，让 Agent 直接 `click @e12` ，而不是去猜脆弱的 CSS/XPath** 。这套做法 **更省 token、步骤更少、确定性更高** （agent-browser 实测首次成功率 ~95%，明显高于传统 Playwright MCP）。所以你看 BrowserSkill 把 `snapshot` 列为第一选择、截图垫底，不是随便排的，是这一代 Agent 浏览器工具的共识。

## 六、优点（实测/读源码得出，给硬的）

1. **复用登录态，凭证不离开本机**
	。不用把账密塞 prompt，不用配登录流程。安全模型上比"账密进 prompt"强一个量级。
2. **纯本地、不外联**
	。daemon 只在 `127.0.0.1` ，不像官方 Claude in Chrome 会把你访问的 URL 上报服务器做策略校验—— **内网地址友好** ，这点对在内网环境干活的人很关键。
3. **agent 中立**
	。一套桥接，Cursor / Claude Code / Codex / OpenClaw / CodeBuddy 都能用，对它们来说 `bsk` 就是普通命令，零适配。
4. **不挑鉴权方式（很多人会忽略的一条）**
	。官方 Claude in Chrome 绑死 Anthropic 官方账号登录，鉴权过不去就用不了；而国内大量用户跑 Claude Code 走的是 **authtoken 接中转站** ，或者干脆 **接第三方 API** ——这批人官方浏览器功能直接用不了。BrowserSkill 因为只是个普通 shell 命令， **不关心你用什么模型、什么 key、什么鉴权** ，authtoken / 第三方 API / 别家 agent 照样能用。对"非官方订阅"的大多数人来说，这往往是唯一能用的那个。
5. **不抢你的窗口、无冷启**
	。用你已开的浏览器，独立的橙色 Agent Window，要碰你现有标签得显式 `borrow` 。相比 Playwright 每次冷启新实例还跟你抢焦点，体验上确实清爽。
6. **人在回路**
	。 `request-help` 暂停/恢复，验证码、二次确认、删除弹窗交回给你处理完再继续，适合"该自动的自动、该人来的叫人"的半自动流程。
7. **MIT 开源可审计**
	。 `install.sh` / manifest / SKILL.md 我都读过，无 telemetry、无凭证访问，能自己核。

## 七、缺点（一样给硬的，别被科普文带跑）

1. **不适合无人值守 / CI 的长时间自动化**
	。注意：这里要分清——"需要你的浏览器开着"本身 **不是缺点，是设计前提** ，它就是要用你已开、已登录的浏览器（甚至能用 `bsk tab borrow` 直接借用你当前正开着的标签页来看），对"人在电脑前随手让 AI 看个页面"的场景反而是优点：没有冷启动、就是你那个真实会话。真正的短板在于 **连接不够稳** ：实测 service worker 闲置后、或浏览器重启后， **instance id 会变、连接会掉** （这次 Edge 实例 id 变过、Chrome 掉过线，得重跑 `bsk browsers` 重查）。所以 **没人盯着的长时间任务 / CI 流水线** 用它要额外做保活，不如 Playwright 省心；而你人在跟前时，掉了重连一下没什么影响。
2. **读不了 console / network**
	。命令集里没有专门的控制台/网络抓包命令，找前端 bug 看报错和接口返回只能用 `evaluate` 绕。 **这是相对官方 Claude in Chrome 的硬伤** ——后者专门主打读 console 调试。
3. **不支持 GIF / 会话录制**
	。实测命令集里截图只有一个 `screenshot` （单张 PNG，可裁剪到某元素）， **没有 gif/录屏/会话录制** 。官方 Claude in Chrome 支持"会话录制为 GIF"用来记录或分享操作过程，BrowserSkill 没有，要演示流程得自己外接录屏工具。

「读不了 console/network」这条我没忍住，动手给扩展补了一版——用 CDP 的 `Log` / `Network` / `Runtime` 域旁路抓取，能拿到 `evaluate` 绕法拿不到的 **引擎级报错** 和 **真实状态码** 。已 fork 一份（含实现）并给上游提了 issue：

- Fork：https://github.com/hjxccc/BrowserSkill
- Issue：https://github.com/Tencent/BrowserSkill/issues/2

实现就是照搬它自己监听对话框事件的范式，多开两个 CDP 域 + 把事件 buffer 起来——基础设施它本来就有，所以这缺口补起来很轻。

1. **权限大，且约束是"软"的**
	。扩展要 `debugger` + `<all_urls>` ，技术上能读任意站点的全部内容和 cookie；SKILL.md 里写的"不要提取凭证/cookie"只是 **提示词级别的约束，没有技术强制** 。对比之下 OpenClaw 的 manifest 只要 `debugger` + `localhost` （CDP 挂上标签本就够用，不必 `<all_urls>` ），更克制。
2. **有明显的"被接管"观感**
	。它用 CDP，会触发 Chrome/Edge 顶部那条"BrowserSkill 已开始调试此浏览器"横幅 + 整窗橙色描边 + "Agent 正在控制"浮窗（见实测截图）。安全上是好事（可见性高），但有人会觉得碍眼。
3. **页面内容会进 Agent 上下文 = 进你的 LLM 提供商**
	。对含敏感信息的页面，等于绕过了人工脱敏这一关。五款工具都有这个问题，但它是用任何"真实浏览器 + LLM"方案都要付的代价，得心里有数。
4. **很新**
	。v0.1.5、2026 年 6 月首发、star 还不多，长期稳定性和生态没经过检验；多浏览器连接时要手动 `--browser <id>` 指定，体验还略糙。
5. **session 用完必须 `stop`**
	，否则堆 Agent Window；写自动化脚本时容易忘。

## 八、适合谁 / 不适合谁

**适合** ：

- 让 AI 操作 **需要登录** 的内网后台、知识库、工单系统、SaaS 后台——外部工具触达不到，它靠复用登录态天然能进。
- 让 AI 编程助手在 **你平时那个真实浏览器** 里跑端到端验收，而不是 headless。
- 想跟 AI **半自动协作** ：重复操作交给它，关键决策自己点。
- 在意 **数据不出本机** 、用 **多个不同 agent** 的人。

**不适合** ：

- 要 **无人值守 / CI 流水线** ：它依赖你浏览器开着、还会掉线，不如 Playwright 省心。
- 要 **深挖前端 bug 看 console/network** ：它弱，用官方 Claude in Chrome 或 Playwright。
- 对 **扩展权限洁癖** 到极致： `<all_urls>` 会让你不舒服，可以看 OpenClaw。

## 九、结论

BrowserSkill 最聪明的不是"能打开网页"，而是把 **登录态共享 + 与人共存 + 纯本地 + agent 中立** 这四件事一起做对了。它和 Playwright **不是替代关系，是互补** ：

要登录态、要跟人共存、不要冷启 → BrowserSkill； 要 CI、要无人值守、要读 console、要干净隔离 → Playwright。

如果你已经在让 AI 干网页活儿，又被"登录态"和"抢窗口"折磨过，它值得装来试。但别把它当成全自动魔法—— **它需要你的浏览器开着，它读不了 console，它的权限边界靠自觉** 。认清这三条，再决定用在哪。

### 引用链接

\[1\] https://github.com/Tencent/BrowserSkill

**微信扫一扫赞赏作者**

闪记

复制 LaTeX 公式