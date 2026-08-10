# HANDOFF.md - DailyDoseOfDS Gmail Pipeline 交接

> 最后更新：2026-08-10 by Codex

## Goal

在 Knowledge Bank 中维护一条可重复、可追踪、可自动化的 Daily Dose of DS 邮件管线：

```text
Gmail starred
  -> Clippings/DailyDoseOfDS（发现、拆分、人工审阅）
  -> Knowledge Bank Ingest SOP
  -> raw/articles + wiki/sources + 图谱/索引/日志
```

Pipeline 只负责 Gmail 同步、文章拆分和状态追踪，不得绕过仓库 `AGENTS.md` 的 Ingest SOP 直接写入 `raw/` 或 `wiki/`。

## Current Progress

### 已完成

- Pipeline 已迁移到 `scripts/dailydose_pipeline.py`，使用 PEP 723 声明依赖，通过 `uv run` 执行。
- Pipeline 元数据集中在 `Clippings/DailyDoseOfDS/.pipeline/`，避免根目录中的状态 Markdown 被 Ingest 扫描误认为文章。
- `manifest.json` 是机器事实账本，保存邮件到文章的一对多关系、远程星标状态、错误、拒绝原因和生命周期。
- `SYNC_STATUS.md` 是人类可读状态表；`ARCHIVE_INDEX.md` 索引已进入 `raw/articles/` 的历史文章。
- 新文件统一命名为 `YYYY-MM-DD_<规范化标题>_<Gmail ID 前6位>.md`，不再混用 `_partN`。旧 `raw/` 文件名保持不变，避免破坏既有 Source 链接。
- 当前账本包含 59 封已处理邮件：48 封 `ingested`，11 封 `ignored`。
- 当前文章状态：76 篇 `ingested`、0 篇 `review`、1 篇 `rejected`。
- `Succeed in AI Engineering roles` 已确认是邮件 footer 会员推广，不是文章：
  - `ingest_progress.json` 已从 `true` 修正为 `false`；
  - manifest 记录为 `rejected / footer_ad_parse_bug`；
  - 不存在于 `raw/articles` 是正确状态。
- Kit footer 误拆分 Bug 已修复：
  - 支持解码 `click.kit-mail*.com` 与 ConvertKit 跟踪链接；
  - 使用 URL-safe Base64 还原真实目标；
  - 指向 `/membership` 的 H2 被识别为推广；
  - 有 H2 的邮件始终按有效 H2 分段，全为推广 H2 时返回零篇文章。
- 保留 4 个简单测试，正式命令执行结果为 4/4 通过。

### 当前限制

- `last_discovery_at` 仍为 `null`，59 封邮件的 `remote_starred` 均为未知。
- 2026-08-10 尝试访问 Google Gmail discovery API 时连接超时，因此没有把失败结果伪装成已核对状态。
- knowledge-bank 工作树还有用户原有改动：`.obsidian/plugins/google-drive-mirror/*` 和已删除的 `download.html`。不要恢复、覆盖或混入 Pipeline 清理。
- 本次 Pipeline 文件仍可能处于未提交状态；操作前先运行 `git status --short`。

## What Worked

- 用完整 Gmail message ID 作为邮件主键，用 manifest 明确表达一封邮件对应零到多篇文章。
- 从现有 `ingest_progress.json + raw/articles` 初始化历史状态，不把已 Ingest 的 76 篇文章重新复制回 Clippings。
- 将 Clippings 根目录限定为真正待 Ingest 的文章和 `ingest_progress.json`，其余元数据放入隐藏 `.pipeline/`。
- Gmail `messages.list` 自动跟随 `nextPageToken`，避免只读取第一页。
- 失败邮件记录为 `failed` 并允许下次 `fetch` 重试；取消远程星标不会删除本地文章。
- 依据解码后的目标 URL `/membership` 判断 footer 推广，比按标题硬编码 `Succeed in AI Engineering roles` 更稳健。
- 直接从 Git 历史恢复误拆分文件，确认其正文是会员课程 CTA，而不是凭标题猜测。

## What Didn't Work

- 旧增量脚本依赖历史会话日志和 58 个硬编码 ID，无法可靠区分未同步、已过滤和本地删除。
- 旧拆分器只用静态 H2 文本黑名单；`Succeed in AI Engineering roles` 未命中黑名单，因此被误判成第 5 篇文章。
- 旧链接解码器只识别域名包含 `convertkit`，没有覆盖实际使用的 `click.kit-mail3.com`。
- 旧逻辑只有在有效 H2 数量至少为 2 时才拆分；只有 1 个有效 H2 加 footer 时会回退整封邮件，把 footer 再次带入。
- 将 README、状态表直接放在 Clippings 根目录存在被批量 Ingest 误扫的风险，因此已迁移到 `.pipeline/`。
- `gws schema` 和远程 `discover` 曾因 Google discovery API DNS/连接超时失败。网络失败时不要手动填充 `last_discovery_at`。

## Next Steps

1. 网络恢复后，在 knowledge-bank 根目录执行远程核对：

   ```bash
   uv run scripts/dailydose_pipeline.py discover
   uv run scripts/dailydose_pipeline.py status
   ```

2. 若出现 `discovered` 邮件，下载并拆分到 Clippings：

   ```bash
   uv run scripts/dailydose_pipeline.py fetch
   ```

3. 查看 `Clippings/DailyDoseOfDS/.pipeline/SYNC_STATUS.md` 的待审文章。拒绝文章可执行：

   ```bash
   uv run scripts/dailydose_pipeline.py reject '<完整邮件ID>:<文章序号>' --reason '<原因>'
   ```

4. 对保留文章严格执行 `AGENTS.md` 的 Ingest SOP。批量 Ingest 必须串行，每个 Subagent 最多 2 篇；完成摘要、图谱、索引、日志和事实核查后再移动到 `raw/articles`。

5. Ingest 流程更新 `ingest_progress.json` 后对账：

   ```bash
   uv run scripts/dailydose_pipeline.py reconcile
   ```

6. 日常自动发现与抓取可运行：

   ```bash
   uv run scripts/dailydose_pipeline.py run
   ```

   `run` 不会自动 Ingest，这是刻意保留的质量关卡。

7. 如果以后出现新的 footer 误拆分，优先从链接目标、DOM 位置或推广容器特征扩展过滤规则，不要只追加易误伤的标题关键词。

## Verification

```bash
uv run --with beautifulsoup4 --with html2text python scripts/test_dailydose_pipeline.py
uv run scripts/dailydose_pipeline.py status
git diff --check
```

最近一次测试结果：4 tests passed。

## Key Files

| 路径 | 用途 |
| --- | --- |
| `scripts/dailydose_pipeline.py` | Pipeline 主程序 |
| `scripts/test_dailydose_pipeline.py` | 4 个简单回归测试 |
| `Clippings/DailyDoseOfDS/.pipeline/manifest.json` | 机器事实账本 |
| `Clippings/DailyDoseOfDS/.pipeline/SYNC_STATUS.md` | 人类可读同步状态 |
| `Clippings/DailyDoseOfDS/.pipeline/ARCHIVE_INDEX.md` | DailyDoseOfDS raw 历史索引 |
| `Clippings/DailyDoseOfDS/.pipeline/README.md` | 使用说明 |
| `Clippings/DailyDoseOfDS/ingest_progress.json` | Ingest 完成记录 |
| `AGENTS.md` | Knowledge Bank 分层和 Ingest 权威规范 |
