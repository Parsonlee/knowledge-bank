# Daily Dose of DS Gmail Pipeline

上级目录是 Daily Dose of DS 邮件进入 Knowledge Bank 的暂存区。本 `.pipeline/` 目录集中保存同步元数据，避免被 Ingest 扫描误判为文章。同步脚本遵守 Vault 的分层规则：新文章只写入 `Clippings/DailyDoseOfDS/`，后续仍需通过仓库 `AGENTS.md` 规定的 Ingest SOP 移动到 `raw/articles/` 并生成 `wiki/sources/`。

## 文件职责

- `manifest.json`：邮件与文章的一对多追踪账本，是同步状态的机器事实来源。
- `SYNC_STATUS.md`：自动生成的人类可读状态表。
- `../ingest_progress.json`：知识库现有 Ingest 流程维护的完成记录。
- `../*.md`：新抓取且尚未 Ingest 的文章。
- `ARCHIVE_INDEX.md`：自动生成的 `raw/articles/` Daily Dose of DS 历史索引。
- `README.md`：本 Pipeline 使用说明。

历史文件沿用原有名称；新文件统一使用 `YYYY-MM-DD_<标题>_<Gmail ID 前6位>.md`，不再生成 `_partN`。同一邮件拆出的多篇文章依靠标题区分，完整对应关系保存在 `manifest.json`。

历史上的 `Succeed in AI Engineering roles` 是拆分器误识别的 footer 广告，账本将其记录为 `rejected / footer_ad_parse_bug`，不会进入 `raw/articles/`。

## 筛选与入库约束

一封邮件可拆分为多篇独立文章。`fetch` 仅负责拉取、拆分和暂存，**绝不意味着该邮件中的所有文章都应入库**。

1. 先在 `SYNC_STATUS.md` 查看每篇待审文章，逐篇阅读并判断是否有保留价值。
2. 仅对明确选中的单篇文章执行仓库 `AGENTS.md` 规定的完整 Ingest SOP：提炼、生成 `wiki/sources/`、按需联动图谱、更新索引与日志、完成事实核查后，才移动到 `raw/articles/`。
3. 未选中的文章不得因同封邮件中其他文章已入库而一并 Ingest；可继续保留在待审区，或使用 `reject '<完整邮件ID>:<文章序号>' --reason '<原因>'` 显式拒绝。
4. 只有完成上述单篇 Ingest 且更新 `ingest_progress.json` 后，才运行 `reconcile` 回写该文章的账本状态。

## 使用方法

在 Knowledge Bank 仓库根目录执行：

```bash
# 首次迁移或修复账本
uv run scripts/dailydose_pipeline.py bootstrap

# 分页读取 Gmail 星标清单
uv run scripts/dailydose_pipeline.py discover

# 下载并拆分新增邮件到当前 Clippings 目录
uv run scripts/dailydose_pipeline.py fetch

# 查看同步状态
uv run scripts/dailydose_pipeline.py status
```

对每篇选中的文章分别完成 `AGENTS.md` 的 Ingest SOP，并更新 `ingest_progress.json` 后执行：

```bash
uv run scripts/dailydose_pipeline.py reconcile
```

日常自动任务可以运行：

```bash
uv run scripts/dailydose_pipeline.py run
```

`run` 会先对账，再发现并抓取新邮件，但不会自动把文章移动到 `raw/`，以免绕过摘要、图谱、索引和事实核查流程。

简单测试：

```bash
uv run --with beautifulsoup4 --with html2text python scripts/test_dailydose_pipeline.py
```
