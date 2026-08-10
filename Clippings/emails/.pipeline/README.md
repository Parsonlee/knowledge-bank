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
