# 个人知识库 (Personal KB)

基于 Obsidian 的个人知识库，通过 Git + GitHub 实现跨平台多端同步。
## 同步方案

- **桌面端 (Mac/Linux/Windows)**：Obsidian + [Obsidian Git](https://github.com/Vinzent03/obsidian-git) 插件，定时自动 commit & push/pull。
- **移动端 (iPhone/iPad)**：Obsidian 移动版 + Obsidian Git 插件（或 Working Copy 配合）。

> `.obsidian/` 里的配置会随仓库同步，因此插件和主题在各端保持一致；`workspace.json` 等设备相关缓存已在 `.gitignore` 中排除。
