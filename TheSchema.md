---
created: 2026-06-26
updated: 2026-06-26
type: guide
tags:
  - schema
  - wiki
  - knowledge-management
---

## 0. 目标与边界

> [!info] 核心目标
> 维护 `wiki/` 目录，将其打造为**可复利的知识层**

- **目标**：你负责维护本仓库中的 `wiki/` 目录，把它变成一个可复利的知识层
- **边界**：
- **边界**：
  - 原始资料（`raw/`、`Clippings/`）是唯一事实来源，**只读不改**
  - 只在 `wiki/` 里创建、修改 Markdown 页面
  - `notes/` 是用户手写笔记，不受 LLM 管理
  - 不要动其它目录

---

## 1. 目录结构约定

### 原始资料层
- `raw/`：主原始资料库（合并了原 Cubox 批注与正文），**只读**
- `Clippings/`：网页剪藏库（由 Obsidian 官方插件自动存入），**只读**
- `workdocs/`：工作项目原始文档，**只读**

### Wiki 维护层
`wiki/` 由你维护，子目录：

| 目录                  | 用途           |
| ------------------- | ------------ |
| `wiki/sources/`     | 单个来源的摘要页     |
| `wiki/entities/`    | 人物、书籍、项目等实体页 |
| `wiki/concepts/`    | 方法、理论、模型等概念页 |
| `wiki/comparisons/` | 比较分析页        |
| `wiki/overview/`    | 总览、综合页       |

### 根目录文件
- `wiki/index.md`：内容索引
- `wiki/log.md`：操作日志

---

## 2. 页面类型与基本格式

所有 wiki 页面使用 Markdown，顶部 frontmatter 示例：

```yaml
---
type: "source|entity|concept|comparison|overview"
tags: ["tag1", "tag2"]
summary: "一句话说明这页的核心内容"
sources: ["raw/xxx.md"]
updated: "2026-07-02"
---
```

### 2.1 Source Summary（来源摘要页）

路径：`wiki/sources/xxx.md`

- 来源信息（标题、作者、时间、链接）
- 核心要点（3–7 条 bullet）
- 关键引文（可选）
- 关联实体/概念链接（`[[entities/xxx]]` / `[[concepts/yyy]]`）

### 2.2 Entity Page（实体页）

路径：`wiki/entities/实体_xxx.md`

- 基本信息
- 行为 / 特征 / 状态
- 相关事件 / 计划 / 实验链接
- 来自哪些来源（列出 `sources`）

### 2.3 Concept Page（概念页）

路径：`wiki/concepts/概念_xxx.md`

- 定义
- 使用场景 / 步骤
- 在本知识库中的应用示例
- 关联实体 / 其它概念

### 2.4 Comparison Page（比较页）

路径：`wiki/comparisons/xxx_vs_yyy.md`

- 比较对象简介
- 相同点
- 不同点（目标、成本、适用场景…）
- 结论 / 选择建议

### 2.5 Overview / Synthesis（总览 / 综合）

路径：`wiki/overview/综述_xxx.md`

- 一句话结论（Summary）
- 当前理解 / 总体框架
- 支撑它的主要来源和页面链接
- 未决问题 / 待验证假设

---

## 3. 工作流：Ingest / Query / Lint

### 3.1 Ingest（导入新资料）

当我说"请基于 `raw/xxx` 进行 Ingest"时：

1. 阅读 `raw/xxx`，提炼要点
2. 在 `wiki/sources/` 新建或更新摘要页
3. 根据内容更新或创建：
   - 相关实体页（`wiki/entities/`）
   - 相关概念页（`wiki/concepts/`）
4. 维护索引 / Log：
   - 在 `wiki/index.md` 补上新页面条目（标题、链接、一句话 summary）
   - 在 `wiki/log.md` 追加记录：
     ```
     ## [2026-07-02] ingest | raw/xxx → wiki/sources/xxx.md (+ affected pages)
     ```

### 3.2 Query（基于 wiki 回答问题）

当我提问时：

1. 通过 `wiki/index.md`、frontmatter 的 `summary` 找到候选页面
2. 读取页面内容，综合回答
3. 如回答有价值（比较 / 分析 / 计划），可建议：
   - 写回为新 wiki 页面（`wiki/comparisons/` 或 `wiki/overview/`）
   - 在 `wiki/log.md` 记录：
     ```
     ## [2026-06-26] query | 新建 wiki/comparisons/xxx_vs_yyy.md
     ```

### 3.3 Lint（健康检查）

当我说"请对 wiki 做一次 Lint"时：

1. 扫描 wiki，找出：
   - 页面间明显矛盾
   - 明显过时的表述（被新资料推翻）
   - 孤立页面（没有入链）
   - 被多次提到但没有独立页的概念
   - 严重缺失 cross-ref 的地方
2. 生成「建议清单」，**不直接大改**：
   - 哪几页建议合并 / 拆分
   - 哪些观点需要确认更新
   - 哪些概念值得单独开页
3. 经我确认后再动手，并记录到 `wiki/log.md`：
   ```
   ## [2026-06-26] lint | merge 概念_X v1→v2
   ```

---

## 4. 约定与风格

> [!tip] 操作原则
> 不确定时，先提议再执行，不做大规模自动改动

- 页面命名：中文 + 下划线，稳定可读（如 `概念_费曼学习法`）
- 内部链接：使用 Obsidian `[[wikilink]]` 语法
- 沿用主库已有的 tag 体系（见 `CLAUDE.md`），不另起一套
- 不确定时：先提议"创建/修改哪些页面"，由我确认后再执行
- 每次 ingest 后建议 git 提交，便于回溯

### 4.1 工具选择

当需要操作 vault 时，**优先使用 MCP 工具（`mcp__obsidian__*`）**：

- `vault_read` / `vault_write`：读写笔记
- `search_query`：按 tag / frontmatter 结构化搜索
- `search_simple`：全文搜索
- `vault_patch`：精准修改 frontmatter 或某个标题下的内容
- `tag_list`：查看全局 tag 分布

> [!note] 为什么用 MCP
> MCP 工具直接访问 Obsidian 的实时元数据和链接结构，比文本搜索更精确高效
