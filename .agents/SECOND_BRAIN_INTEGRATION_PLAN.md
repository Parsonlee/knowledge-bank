---
title: AGENTS.md 与 Obsidian Second Brain 重构记录
date: 2026-08-11
updated: 2026-08-11
status: accepted
tags:
  - AI-Agent/governance
  - AI-Agent/skill
  - knowledge-base/maintenance
aliases:
  - Second Brain 融合重构记录
---

# AGENTS.md 与 Obsidian Second Brain 重构记录

> [!success] 最终结论
> 本次重构已经完成并通过验收。`AGENTS.md` 继续作为本仓库唯一治理权威；`obsidian-second-brain` 保留，但被收敛为受控适配层与只读工具路由。没有引入 Typed Edge 或 `relations:`，没有恢复用户人工删除的 Skill / Obsidian 插件，也没有执行自动 Git 写操作。

## 1. 背景与目标

重构前，仓库治理规则、Second Brain 上游规则和 `vault_lint.py` 的实际行为存在多处不一致：

1. `AGENTS.md` 一方面要求删除与 Prune 必须经过 L3 Dry-run，另一方面又写有“无源页面直接物理清除”，形成权限冲突。
2. 活动 Second Brain Skill 曾把末端页面错误地描述为直接溯源 `raw/`，破坏 `raw -> wiki/sources -> 末端页面` 的单向推导链。
3. Git 自动操作与 Vault L3 审批边界不清，容易被误读为用户可用 L3 解禁 `stash`、`reset` 或 `commit`。
4. 上游构建默认在活动 `.agents/skills/` 树内生成 `dist/`，其中包含大量嵌套 `SKILL.md`，可能被 Agent 发现器当成活动技能加载。
5. `vault_lint.py` 对 Frontmatter、来源链和 Prune 的部分判断依赖正则，不能稳定处理重复 YAML 键、类型错误及结构化 `timeline`。
6. 旧 Sanitizer 可接受 `raw/../AGENTS.md`，并把仓库治理文件派生为 Sanitized View，证明存在真实路径穿越漏洞。
7. 启用严格 Schema 后发现 26 个 Concept 和 1 个 Entity 缺少 `summary`，需要受控数据迁移。

本次目标是统一治理、收紧能力边界、修复确定性工具、隔离上游构建，并在不扩展页面正文的前提下补齐 27 个缺失摘要。

## 2. 明确排除项

以下事项从方案阶段起即明确不做，最终 diff 也未出现相关实现：

- 不引入 Typed Edge、`relations:` 或其他平行关系字段。
- 不采用上游 AI-First Preamble、`ai-first`、`confidence` 或平行可信度 Schema。
- 不恢复用户人工删除的 Skill、Obsidian 插件或配置。
- 不改变邮件 Sync、人工 Review 或 Ingest 管线；工作区中的邮件管线改动属于用户既有变更。
- 不允许自动 Git `commit`、`stash`、`checkout`、`reset` 或 `push`。
- 不以“让上游旧测试全绿”为理由恢复自动 Synthesis、后台 Agent、Daily Note 写入或完整上游命令路由。

## 3. 最终架构

### 3.1 治理优先级

最终规则层级为：

1. 根目录 `AGENTS.md`：唯一治理权威，决定知识分层、来源链、权限和审批。
2. 仓库任务说明与 `scripts/`：实现确定性流程，但必须服从 `AGENTS.md`。
3. Agent Skills / 外部工作流：只能提供能力、路由和工具，不能自行扩大授权。
4. Agent 自身知识：只能作为明确标注的补充，不得冒充库内事实。

Second Brain 的活动 `SKILL.md` 不再复制一套完整治理规则，而是保留最小路由、白名单、禁用能力和上游归档说明。

### 3.2 来源链

```text
raw/ 或 Clippings/
        |
        v
wiki/sources/              每页必须且只能有一个真实 raw 上游
        |
        v
entities / concepts /      sources 必须为非空 wiki/sources 字符串数组
comparisons / overview
```

- Source 不允许零上游、多上游、非字符串上游或不存在的 raw 路径。
- 末端页面禁止绕过 Source 直接指向 `raw/`。
- 无源、低频和过期信号只产生 error、warning 或 Dry-run 候选，不自动赋予删除权限。

### 3.3 权限与 Git 边界

- L0：只读诊断。
- L1：确定性修复，需显式启用。
- L2：语义写入，执行前预览。
- L3：删除、Merge、Prune、批量迁移等 Vault 高危操作，必须先 Dry-run 并获得明确批准。
- Git 自动写操作不属于上述分级，永久禁止，不存在 L3 例外。

## 4. 文件级实施记录

### 4.1 `AGENTS.md`

完成以下治理修订：

- 将“无源页面直接物理清除”改为强制报错和 L3 Dry-run 候选。
- 明确 Source 与四类末端页面的严格来源结构。
- 明确 Sanitized View 只生成临时读取副本，不修改 `raw/` 或 `Clippings/` 原始字节。
- 统一仓库脚本命令为 `uv run --with pyyaml python ...`。
- 将 Git 写操作定义为无例外永久红线。

### 4.2 `.agents/skills/obsidian-second-brain/SKILL.md`

活动 Skill 保留并收敛为仓库适配器：

- 第一原则指向根 `AGENTS.md`，冲突时无条件服从根规则。
- 末端来源方向修正为 `wiki/sources/`。
- 白名单只保留已审计命令：仓库 Lint、`vault_health.py`、带 `--print-only` 或 `--json` 的 `vault_stats.py`。
- `vault_scan.py` 等未证明安全的脚本不因名称看似只读而进入白名单。
- `bootstrap_vault.py`、`heal_links.py --apply` 等能力保持 L3 禁用。
- Git 写入、自动 Ingest、自动 Synthesis、后台写入、PostCompact、AI-First Validator 和无人值守冲突裁决永久禁用。
- `UPSTREAM_SKILL.md` 只作为离线参考与审计归档，其 SHA-256 保持：
  `67325d177d51e7eb331d05e1944d23f8c2206f128d9a000cf26aee6fd4cb2d9d`。

### 4.3 Second Brain 构建隔离

`.agents/skills/obsidian-second-brain/scripts/build.sh` 增加安全输出协议：

- 支持 `--output-dir <path>`，并拒绝参数缺值。
- 当源码位于活动 `.agents/skills/` 树时，默认输出到仓库 `tmp/obsidian-second-brain-dist/`。
- 拒绝输出到文件系统根目录或任意活动 `.agents/skills/` 树。
- 对路径做词法规范化，并解析最近存在父目录的物理路径，阻止 `..` 和 symlink 绕过。
- 构建后的 bytecode 清理锚定到实际 `OUTPUT_DIR`。
- Adapter 测试会在临时活动 Skill 树中执行真实构建，并确认活动树没有新增嵌套 `SKILL.md`。

### 4.4 `scripts/vault_lint.py`

Lint 与治理命令完成结构化重构：

- 使用 PyYAML SafeLoader，并通过自定义 Loader 拒绝重复键。
- 解析失败、非映射 Frontmatter 和字段类型错误均稳定报告，不再静默退化。
- 校验 `type`、`tags`、`summary`、`sources`、`updated` 的存在性与类型。
- 修正 `overview` 对应 `wiki/overview/` 的目录映射。
- Entity `timeline` 校验结构、字段、字符串值、有效日期、`null` 及 `wiki/sources/` 来源。
- Prune、orphan、recover 和 raw 引用提取改用同一套结构化 Frontmatter 解析，不再从正文正则猜测 `sources`。
- 强制错误返回非零；低频 warning 不触发删除。

### 4.5 Sanitized View 安全

`sanitize-view` 的最终安全属性包括：

- 输入只允许仓库相对的 `raw/` 或 `Clippings/` 路径。
- 拒绝绝对路径、`..` 穿越、输入 symlink 逃逸和输出 symlink 逃逸。
- SHA-256 基于原始 bytes，而非解码后的字符串。
- 输出固定在 `tmp/sanitized/`，同步生成包含原路径、解析路径、原始哈希、转换动作、生成时间和版本的 JSON sidecar。
- 使用目录文件描述符、`O_EXCL`、`O_NOFOLLOW` 和 `0600` 权限创建文件。
- 不覆盖既有普通文件、symlink 或元数据文件。
- `sanitize-raw` 明确失败，不能修改原始资料。

旧实现曾成功生成 `tmp/sanitized/AGENTS_ace9d445.md`，其来源路径显示为 `raw/../AGENTS.md`。该文件成为路径穿越缺陷的直接证据；修复后的单测要求同一输入失败且不产生输出。

### 4.6 自动测试

新增两组隔离测试：

- `scripts/test_vault_lint.py`：22 项，覆盖 YAML、五类页面、来源链、timeline、Sanitizer 路径与并发写安全、结构化 Prune 及 warning 不删除。
- `.agents/skills/obsidian-second-brain/tests/test_knowledge_bank_adapter.py`：12 项，覆盖治理入口、上游哈希、来源方向、Git 红线、CLI 白名单、禁用能力、独立 uv 环境、活动 Skill 发现边界和构建输出隔离。

所有 fixture 使用临时目录，不写真实 Vault 正文。

## 5. 27 页 Summary 数据迁移

严格 Schema 首次在真实 Vault 运行时发现 26 个 Concept 与 1 个 Entity 缺少 `summary`。最终修复遵循：

1. 每个 Writer 批次最多 2 页。
2. 每页只修改 Frontmatter 的 `summary` 一行。
3. Writer 沿 `wiki/sources/` 回查 raw；独立 Auditor 再次对照物理原文。
4. 每批通过后运行真实 Vault Lint，当前批失败不得推进。
5. 不顺手修正文、标签或创建新页面。

最终 27 个目标为：

| 类型 | 页面 |
| --- | --- |
| Concept | `概念_Agentic_RL环境与GRPO` |
| Concept | `概念_LoRA与QLoRA微调` |
| Concept | `概念_数据集变量分类` |
| Concept | `概念_稀疏注意力` |
| Concept | `概念_机器学习损失函数` |
| Concept | `概念_分位数回归与Pinball_Loss` |
| Concept | `概念_Agent内存与状态管理` |
| Concept | `概念_Claude_Code核心配置与原语` |
| Concept | `概念_Python并发与并行机制` |
| Concept | `概念_数据版本控制与DVC` |
| Concept | `概念_LLM文本生成解码参数` |
| Concept | `概念_不平衡数据的kNN优化` |
| Concept | `概念_固定内存_Memory_Pinning` |
| Concept | `概念_分块阻断技术_Blocking` |
| Concept | `概念_LLM系统自动优化方法论` |
| Concept | `概念_梯度提升决策树_GBDT` |
| Concept | `概念_Python模块与包管理` |
| Concept | `概念_分类模型校准` |
| Concept | `概念_主成分分析_PCA` |
| Concept | `概念_类别特征编码技术` |
| Concept | `概念_Graph_Engineering图工程` |
| Concept | `概念_机器学习双下降现象` |
| Concept | `概念_扩散大语言模型_dLLMs` |
| Concept | `概念_ReLU激活函数非线性拟合本质` |
| Concept | `概念_周期性特征编码` |
| Concept | `概念_跨模型嵌入对比局限` |
| Entity | `实体_Sim_AI工作流框架` |

最终 `git diff --numstat -- wiki/concepts wiki/entities` 对每页均显示 `1 0`，即只增加一行，没有正文删改。

## 6. 实施事故与纠正

### 6.1 第一版摘要修复失败

第一版实施脚本从正文截取前约 50 个字符并拼接 `...`，生成了 27 条残句。这些摘要虽然能满足“非空字符串”的结构检查，但不具备可接受的语义质量。

纠正措施：

- 立即拒绝该轮验收。
- 删除错误实施脚本，不把脚本通过视为事实性通过。
- 按每批最多 2 页重新派发 Writer。
- 由独立 Auditor 回查 Source 与 raw。
- PCA 摘要中曾出现“当前两个主成分”的笔误，退回 Writer 修正为“前两个主成分”后再复审。
- 最终扫描未发现以 `...` 或 `…` 结尾的摘要。

### 6.2 上游完整测试的适配冲突

上游完整测试在保持 `.agents/skills/obsidian-second-brain/` 真实目录形态的 `/private/tmp` 副本中运行，结果为：

```text
534 passed, 28 failed, 7 skipped
```

28 项失败的分类如下：

| 数量 | 原因 | 处理结论 |
| ---: | --- | --- |
| 18 | 上游测试硬编码旧 `dist/` 输出，而活动 Skill 构建已按要求输出到 Vault `tmp/` | 旧构建契约不适用于本仓库，不恢复活动树内 `dist/` |
| 5 | 要求活动 `SKILL.md` 暴露全部上游命令或旧触发路由 | 与受控适配层目标冲突，不恢复 |
| 2 | 依赖旧英文字符串或过窄命令正则 | 适配层命令已由本仓库契约测试覆盖，不修改活动规则迎合字符串 |
| 3 | 测试调用 `git ls-files`，而隔离副本没有 Git 元数据 | 环境依赖，非脚本功能回归 |

新增 Adapter 12 项在同一真实目录形态下全部通过，因此没有用 Adapter 测试冒充“上游全量通过”。

## 7. 最终验收结果

| 验收项 | 结果 |
| --- | --- |
| `uv run --with pyyaml python -m unittest scripts/test_vault_lint.py` | 22 passed |
| `uv run --with pyyaml python scripts/vault_lint.py lint` | 退出码 0；全部强制检查通过，33 个低频实体仅作为候选 warning |
| `uv run --directory .agents/skills/obsidian-second-brain python -m pytest tests/test_knowledge_bank_adapter.py` | 12 passed |
| Skill Creator `quick_validate.py` | `Skill is valid!` |
| `bash -n .../scripts/build.sh` | 通过 |
| `git diff --check` | 通过 |
| 活动树 `find ... -name SKILL.md` | 仅根 `.agents/skills/obsidian-second-brain/SKILL.md` |
| 截断摘要扫描 | 无匹配 |
| 上游归档 SHA-256 | 与基线一致 |

## 8. 清理与保留

已经清理的本轮产物：

- 根目录一次性实施脚本 `patch_agents.py`、`update_vault_lint.py`。
- 活动 Skill 树内旧 `dist/`，共 937 个生成文件，约 6.1 MiB。
- 第一版错误摘要实现使用的三个 `scratch/` 脚本。
- `/private/tmp` 中的完整测试副本。

经 L3 Dry-run 与用户明确批准，最终清理以下阶段性材料，共 5 个文件、74,109 字节：

- `FIX_PLAN.md`
- `dry_run_summary_fix.md`
- `dry_run_cleanup.md`
- 本轮生成的两个 `tmp/sanitized/*.md` 临时视图
- 已清空的 `scratch/` 目录

上述未跟踪或忽略文件已物理删除，不能通过 Git 恢复；其中需要长期保留的架构、验收与事故信息均已汇总在本文。

以下文件虽然也具有临时或备份性质，但早于本次重构，因此明确不在本次清理范围：

- `tmp/fix_index.py`
- `wiki/index.md.bak`（Git 已跟踪）

## 9. 遗留风险与后续建议

> [!warning] 本次事实性验收的边界
> 27 页验收只覆盖新增 `summary`，不代表这些页面既有正文已经通过全文事实核查。

Auditor 在抽查中发现部分既有 Concept 正文含有超出当前 Source 明示范围的扩写，例如 LoRA 页中的初始化、`alpha/r`、vLLM/S-LoRA、LRU 与加载延迟，以及数据集变量、稀疏注意力、损失函数、DVC 等页面中的额外机制陈述。

这些内容没有在本轮被自动删除或顺手改写。建议未来建立独立的“末端页面正文事实性审计”项目，按页面输出主张、Source 证据、raw 位置和处理建议，并继续遵守 Writer / Auditor 分离。

## 10. 后续维护约束

1. 修改治理规则时只更新 `AGENTS.md`，活动 Skill 只保留必要路由，避免形成第二套宪法。
2. 升级 Second Brain 上游时先复制到 `tmp/` 或 `/private/tmp` 做差异审计，禁止用上游更新器覆盖活动适配层。
3. 构建测试必须保留 `.agents/skills/obsidian-second-brain/` 目录形态，否则 Adapter 测试无法正确发现 Vault 根目录。
4. 新增 Lint 规则时同时补充临时目录 fixture，不使用真实 Wiki 页面制造失败样本。
5. Schema 通过只能证明结构合法，语义写入仍必须由独立 Auditor 对照 raw。
6. 删除、Merge、Prune 和批量迁移继续执行 L3 Dry-run；Git 自动写操作继续永久禁止。
