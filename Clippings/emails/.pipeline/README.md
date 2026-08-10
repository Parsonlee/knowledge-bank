# 多来源邮件暂存管线

`Clippings/emails/` 是 Gmail 订阅邮件的暂存根目录。共享管线发现所有星标邮件、记录差异并按发件人路由；每个来源的解析器只负责把自己的邮件拆分为待审 Markdown。

```text
Gmail is:starred
  -> sync（发现、元数据、差异账本）
  -> route（已注册来源解析；未知来源仅待路由）
  -> Clippings/emails/<source_key>/*.md（用户人工逐篇 Review）
  -> 用户明确指令后，Agent 执行 AGENTS.md Ingest SOP
  -> raw/articles + wiki/sources + 图谱/索引/日志
```

## 目录与状态

- `manifest.json`：机器事实账本。邮件是容器，`articles` 数组中的文章是状态管理和 Ingest 的原子要素。
- `SYNC_STATUS.md`：自动生成的人工可读状态表，列出待路由邮件和待审文章。
- `ARCHIVE_INDEX.md`：已归档至 `raw/articles/` 的邮件订阅文章索引。
- `../<source_key>/*.md`：来源解析器生成的待审文章；当前已注册来源为 `dailydoseofds`。

未注册发件人仅保存 ID、发件人、主题和日期，并标记为 `unhandled`；不会拉取正文或生成文件。新增解析器后，登记发件人规则并执行 `route` 即可处理。

## 使用方法

```bash
# 同步全部 Gmail 星标邮件，登记元数据与差异
uv run scripts/mail_pipeline.py sync

# 解析已注册来源，生成待审 Markdown；未知来源保持 unhandled
uv run scripts/mail_pipeline.py route

# 日常组合命令：逐篇对账 -> 同步 -> 路由
uv run scripts/mail_pipeline.py run

# 查看共享状态
uv run scripts/mail_pipeline.py status
```

## 筛选与入库约束

一封邮件可拆分为多篇独立文章。`route` 只生成待审 Markdown，**绝不表示同封邮件中的所有文章都应入库**。

1. `sync`、`route` 与 `run` 是可自动执行的**邮件同步阶段**：仅更新账本、读取已支持来源的邮件并生成待审 Markdown，绝不 Ingest。
2. 用户在 `SYNC_STATUS.md` 或来源目录中逐篇完成 Review，决定保留或删除；未选文章继续保持 `review`，或执行 `uv run scripts/mail_pipeline.py reject '<文章 ID>' --reason '<原因>'` 显式拒绝。
3. 即使文章状态为 `review`，Agent 也不得自行判断其应保留或执行 Ingest。只有用户完成 Review 后明确要求 Agent 入库指定文章，才可对该单篇文章执行 `AGENTS.md` 的完整 Ingest SOP。
4. Ingest 完成并将该文章归档至 `raw/articles/` 后，执行 `uv run scripts/mail_pipeline.py reconcile`；该命令只会逐篇回写已存在于 `raw/articles/` 的文章状态。

`run` 不会自动移动、Ingest 或写入 `wiki/`。

## 自动同步到本地

推荐在保存此 Vault 且已完成 `gws` Gmail 授权的本机上，用 macOS `launchd` 定时执行邮件同步。调度器只运行 `run`，因此自动化边界始终停留在「拉取 -> 路由 -> 生成待审 Markdown」；它不会选择文章、删除文章、移动至 `raw/` 或写入 `wiki/`。

```text
Gmail 新邮件或星标变更
  -> launchd 定时唤醒本机任务
  -> uv run scripts/mail_pipeline.py run
  -> Clippings/emails/<source_key>/*.md
  -> 用户在本地逐篇 Review
```

### macOS launchd（推荐）

仓库提供模板 [`scripts/launchd/com.parsonlee.knowledge-bank.mail-sync.plist`](../../../scripts/launchd/com.parsonlee.knowledge-bank.mail-sync.plist)。先用本机的绝对路径替换模板中的以下占位符：

- `__VAULT_PATH__`：本仓库的绝对路径；
- `__UV_PATH__`：执行 `command -v uv` 得到的路径；
- `__GWS_PATH__`：执行 `command -v gws` 得到的路径。

随后将文件复制到 `~/Library/LaunchAgents/`，并加载任务：

```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.parsonlee.knowledge-bank.mail-sync.plist
launchctl kickstart -k gui/$(id -u)/com.parsonlee.knowledge-bank.mail-sync
```

模板默认每 30 分钟运行一次，并在登录后立即补跑一次。日志写入 `.pipeline/logs/`，可用下列命令检查任务和最近输出：

```bash
launchctl print gui/$(id -u)/com.parsonlee.knowledge-bank.mail-sync
tail -n 100 Clippings/emails/.pipeline/logs/mail-sync.err.log
```

修改周期或模板后，先卸载再重新加载：

```bash
launchctl bootout gui/$(id -u)/com.parsonlee.knowledge-bank.mail-sync
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.parsonlee.knowledge-bank.mail-sync.plist
```

> [!warning] 前提与边界
> 电脑休眠或关机时不会即时拉取；下次登录/唤醒后的下一次调度会补拉，`sync` 的差异账本会去重。`launchd` 环境没有交互式 shell 的 `PATH`，所以模板必须使用 `uv` 与 `gws` 的绝对路径。Gmail OAuth 凭据保留在本机，严禁提交到仓库或复制到 GitHub Actions Secret。

### 事件触发的取舍

Gmail API 的 Push Notification 需要 Google Cloud Pub/Sub 端点和持续运行的 Web 服务，并且通知只表示「邮箱有变化」，仍需调用同步接口拉取并去重。对于个人 Vault，这比每 30 分钟轮询的运维成本高，收益很小；当前不建议实现。

若未来需要接近实时的同步，可部署一个仅触发本机 `run` 的受认证 Webhook/队列消费者，或将本机任务频率调整为 5 分钟。无论采用哪一种，处理范围都必须保持在本节的自动同步边界内，Ingest 仍需用户逐篇 Review 后明确指令。

### GitHub Actions 说明

`.github/workflows/sync-clippings.yml` 是旧的 Gemini/Google Drive 管线，指向已移除的 `Clippings/DailyDoseOfDS/`，不能同步本机 Gmail，也不应继续作为邮件同步方案。保留本地 `launchd` 作为唯一自动拉取入口。
