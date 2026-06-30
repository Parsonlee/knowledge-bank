---
tags:
  - schema
created: 2026-06-29
---

# Obsidian Tag 列表被内联 #xxx 污染问题

## 现象

Tag 面板出现大量无意义 tag，如：`output`, `outputtensor`, `This`, `Let`, `Create`, `Causal`, `Multi-Headed`, `instag`, `写一份好的`, `E1F5FE），并在` 等。

## 根因

Obsidian 会索引 vault 内**所有** `.md` 文件正文中的 `#word` 模式，不区分是否在代码块（部分情况下）或普通文本里。`tmp/` 目录存放 Cubox 批量导出的文章，这些文章正文包含大量内联 `#xxx`（Python 代码变量名、英文段首词等），全部被识别为 tag。

确认受影响文件（均在 `tmp/`）：
- `tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/手把手教你，从零开始实现一个稀疏混合专家架构语言模型（MoE）.md`
- `tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/北京大学发布LLMs（预训练+微调）数据管理全流程综述.md`
- `tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/写好 CLAUDE.md _ HumanLayer 博客.md`
- （可能还有更多）

## 修复方案

### 方案一（推荐）：Excluded Files 设置

> Settings → Files and links → Excluded files → Add → 输入 `tmp` → 回车

立即生效，tag 面板自动清洁，不影响文件内容。

### 方案二：清空 tmp/

如果 `tmp/` 文件已无用，直接删除：

```
rm -rf tmp/*
```

## 状态

- [x] 确认 tmp/ 外是否还有污染源（tmp/ 是唯一来源）
- [x] 选择并执行修复方案（方案一：已在 `.obsidian/app.json` 写入 `userIgnoreFilters: ["tmp"]`）
