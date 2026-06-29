# 批量 Ingest 执行计划

## 基本参数

| 参数 | 值 |
|------|-----|
| 总文章数 | 205 篇全文 |
| 分批策略 | 按 tag 集群，每批 5 篇 |
| 并发 | 串行（一批完成再下一批）|
| 验收 | 每个集群完成后，独立 opus subagent 审核 |
| 失败处理 | 跳过 + 记入 wiki/fail.md |

## 执行顺序

| Phase | 集群 | 文章数 | 批次(5篇/批) |
|-------|------|--------|------|
| 1 | Infra + CV + DeepLearning | ~22 | 4-5 批 |
| 2 | RAG | ~45 | 9 批 |
| 3 | LLM | ~66 | 13 批 |
| 4 | AI-Agent | ~45 | 9 批 |
| 5 | Skill + AIGC | ~32 | 6-7 批 |
| 6 | 创业 + 面试 + Life + 其它 | ~22 | 4-5 批 |

## Subagent 指令规范

每个 ingest subagent 的职责：

### 输入
- 5 篇全文路径（`tmp/Cubox-批量导出.../xxx.md`）
- 对应 Cubox highlight 路径（`Cubox/xxx.md`）
- 当前 `wiki/index.md`（确认已有概念）

### 正常流程
1. 逐篇读全文 + highlight
2. 创建 `wiki/sources/xxx.md`（source summary，highlight 内容优先/加权）
3. 提取概念 → 检查 index.md 是否已存在：
   - 已存在 → 用 Edit 追加新来源信息
   - 不存在 → 创建新 `wiki/concepts/概念_xxx.md`
4. 提取实体 → 同上逻辑
5. 更新 `wiki/index.md` + `wiki/log.md`
6. 所有页面用 `[[wikilink]]` 互链

### 异常处理（严格要求）
如遇以下情况，**跳过该文章**并记录到 `wiki/fail.md`：
- 全文文件为空 / <500 字符
- 内容为乱码（非人类可读的 HTML 残留/编码错误）
- 全文只有标题没有正文实质内容

fail.md 记录格式：
```
| 标题 | URL | 失败原因 | 日期 |
|------|-----|----------|------|
| xxx  | url | 全文为空/乱码/无实质内容 | 2026-06-29 |
```

### 质量规则
- confidence 如实标注：`high`（全文有明确依据）/ `medium`（提及但不详细）
- 不用模型知识补全全文没有的内容
- 用户高亮覆盖的内容标 `[重点/高亮]` 置顶
- 超大文章(>80KB)单独 1 篇/批

## 验收 Subagent 指令规范

每个集群完成后，独立 opus subagent 验收：

1. 读该集群所有新建的 wiki 页面
2. 抽查 3-5 个 source 页：对比全文原文，确认核心要点是否真实存在于原文
3. 检查概念页：是否有超出原文的编造内容
4. 检查 [[wikilink]]：是否有死链（指向不存在的页面）
5. 检查 fail.md：失败原因是否合理
6. 输出验收报告（pass/问题清单）

## 预期产出

- ~180-200 个 source summary 页（扣除失败的）
- ~100-150 个 concept 页
- ~30-50 个 entity 页
- 少量 comparison 页
- 全部通过 [[wikilink]] 互联
- 1 个 fail.md 记录失败文章
