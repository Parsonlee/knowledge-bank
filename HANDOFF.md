# HANDOFF.md - 多来源邮件暂存管线交接

> 最后更新：2026-08-11 by Codex

> [!IMPORTANT] 当前优先实施任务
> `AGENTS.md` 与 Obsidian Second Brain 的优化融合已形成可执行计划：[SECOND_BRAIN_INTEGRATION_PLAN](.agents/SECOND_BRAIN_INTEGRATION_PLAN.md)。后续 Agent 应严格按计划实施并停在验收门槛；本文件以下邮件管线交接继续有效，不得覆盖。

## Goal

维护统一的 Gmail 星标邮件前置流程：发现全部星标邮件、记录差异、按发件人路由至独立解析器，并将生成的文章保留为可逐篇选择的 `Clippings` 暂存资料。该管线绝不绕过 `AGENTS.md` 的 Ingest SOP。

## Current Progress

- 旧 DDoDS 专用目录已迁移至 `Clippings/emails/`；共享账本位于 `Clippings/emails/.pipeline/manifest.json`。
- 当前账本：62 封邮件，50 封含已入库文章、12 封忽略；文章状态为 78 篇 `ingested`、0 篇 `review`、8 篇 `rejected`。其中 7 篇由用户直接删除的待审文章已记录为 `manual_delete`。
- `scripts/mail_pipeline.py` 提供 `sync`、`route`、`run`、`status`、`reconcile` 与逐篇 `reject`。
- `scripts/mail_sources/dailydoseofds.py` 是首个来源解析器，保留了 ConvertKit 链接解码、会员 footer 过滤和 H2 拆分规则。
- 共享层对未知发件人只保存元数据并标记为 `unhandled`，不会下载正文；已注册来源才会在 `route` 阶段下载正文并生成 Markdown。
- `sync`、`route`、`run` 是可自动执行的邮件 Sync 阶段，只更新账本和待审 Markdown，绝不 Ingest。
- 用户必须先完成逐篇 Review；即使文章状态为 `review`，Agent 也必须等待用户明确要求对指定文章执行 Ingest，其他文章保持 `review` 或显式 `rejected`。

## What Worked

- 以 Gmail message ID 标识邮件，以 `<message ID>:<序号>` 标识邮件内文章，清晰区分两层状态。
- `run` 只执行逐篇对账、远程同步和已支持来源解析，不会自动移动文件或写入 Wiki。
- 旧 DDoDS 历史 `raw/articles/` 文件名保持不变，现有 Source 链接不受迁移影响。
- 现有 DDoDS footer 会员推广仍作为 `rejected / footer_ad_parse_bug` 保留在账本中。

## What Didn't Work

- 旧单体脚本将星标发现、DDoDS 解析和进度文件耦合，无法容纳多来源邮件。
- Google API discovery 曾发生网络超时，OAuth 刷新令牌也曾过期；远程同步失败时不得手工更新账本的同步时间。

## Next Steps

1. 未来邮件同步后，用户在 `Clippings/emails/.pipeline/SYNC_STATUS.md` 逐篇审阅待审文章。完成后，等待用户明确指定需要 Agent Ingest 的文章；不得自行开始 Ingest。用户直接删除的文章会在 `reconcile` 中记录为 `manual_delete`。
2. 新邮件来源需在 `scripts/mail_pipeline.py` 的 `SOURCES` 注册发件人地址/域名，并在 `scripts/mail_sources/` 新增专用解析器。
3. 日常运行 `uv run scripts/mail_pipeline.py run`；发现 `unhandled` 邮件后决定是否开发对应解析器。
4. Ingest 后运行 `uv run scripts/mail_pipeline.py reconcile`，逐篇回写账本状态。

## Verification

```bash
uv run --with beautifulsoup4 --with html2text python scripts/test_mail_pipeline.py
uv run scripts/mail_pipeline.py status
git diff --check
```

## Key Files

| 路径 | 用途 |
| --- | --- |
| `scripts/mail_pipeline.py` | 共享 Gmail 同步、路由和对账入口 |
| `scripts/mail_sources/dailydoseofds.py` | Daily Dose of DS 专用解析器 |
| `scripts/test_mail_pipeline.py` | 共享层和 DDoDS 解析回归测试 |
| `Clippings/emails/.pipeline/manifest.json` | 邮件与文章两层状态账本 |
| `Clippings/emails/.pipeline/README.md` | 工作流、目录和逐篇入库约束 |
