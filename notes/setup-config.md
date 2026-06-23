# 知识库配置清单

> 在任意一台桌面端按此配好后，`.obsidian/` 会随 Git 同步到其它设备，无需重复配置。

## 一、推荐插件（Community Plugins）

开启方式：Settings → Community plugins → 关闭 Restricted mode → Browse → 搜索安装 → Enable。

| 插件 | 作用 | 优先级 |
| --- | --- | --- |
| **Obsidian Git** | 自动 commit/push/pull，多端同步核心 | 必装 |
| **Templater** | 笔记模板（日记、会议、读书笔记等） | 高 |
| **Dataview** | 把笔记当数据库查询，自动生成列表/表格 | 高 |
| **Calendar** | 日历视图，配合日记 | 中 |
| **Tag Wrangler** | 批量重命名/管理标签 | 中 |
| **Outliner** | 列表大纲增强（拖拽、折叠） | 中 |
| **Paste image rename** | 粘贴图片时自动重命名归档到 assets/ | 中 |

## 二、Obsidian Git 设置（桌面端）

Settings → Obsidian Git：

- **Auto pull on startup**：✅（开 Obsidian 时自动拉最新）
- **Vault backup interval (minutes)**：`10`（每 10 分钟自动 commit + push）
- **Auto pull interval (minutes)**：`10`
- **Pull updates on every commit**：✅（减少冲突）
- **Commit message**：可设为 `vault backup: {{date}}`

## 三、核心设置建议（Settings → Files & Links）

- **New link format**：`Relative path to file`（相对路径，跨平台更稳）
- **Default location for new attachments**：`In subfolder under current folder` 或固定到 `assets/`
- **Use [[Wikilinks]]**：开启（Obsidian 原生双链）

## 四、附件归档

- 图片统一放 `assets/`，避免散落各处。
- 配合 **Paste image rename** 插件，粘贴即自动命名 + 归档。

## 五、冲突处理

走 Git 多端，偶尔会有冲突文件（如 `note (conflicted copy).md`）。处理原则：
- 打开 Obsidian **先等它 pull 完**再编辑。
- 真出现冲突时，用桌面端 `git status` / `git diff` 手动合并最稳。
