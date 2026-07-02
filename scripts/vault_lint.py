#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knowledge Bank Vault Lint & Cascading Pruning Tool
遵循 AGENTS.md 规范的自动化图谱健康检查与级联清理脚本。

用法:
  python3 scripts/vault_lint.py lint             # 执行图谱死链、漏登、语法污染全面审查
  python3 scripts/vault_lint.py sanitize-raw     # 自动转义 raw/ 目录下未规范化的行内伪 Tag 和 Tensor 伪出链
  python3 scripts/vault_lint.py prune <raw_path> # 预演（Dry-run）删除原始资料所触发的自上而下 4 步级联精简报告
  python3 scripts/vault_lint.py prune <raw_path> --apply # 确认执行级联精简清理
"""

import os
import sys
import re
import argparse
from datetime import datetime

def get_workspace():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(script_dir)

def load_file(path):
    if not os.path.exists(path):
        return ""
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def save_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def get_all_md_files(workspace, folders=None):
    if folders is None:
        folders = ['wiki', 'raw', 'notes']
    files_map = {}
    for folder in folders:
        folder_path = os.path.join(workspace, folder)
        if not os.path.exists(folder_path):
            continue
        for root, _, files in os.walk(folder_path):
            if '.git' in root or '.obsidian' in root:
                continue
            for f in files:
                if f.endswith('.md'):
                    abs_path = os.path.join(root, f)
                    rel_path = os.path.relpath(abs_path, workspace)
                    files_map[rel_path] = abs_path
    return files_map

def cmd_lint(workspace):
    print("=" * 60)
    print("🔍 [Vault Lint] 正在执行知识库全量图谱健康扫描...")
    print("=" * 60)

    all_md_files = get_all_md_files(workspace)
    
    # 1. 漏登审计 (Index Registration Audit)
    index_path = os.path.join(workspace, 'wiki', 'index.md')
    index_content = load_file(index_path)
    
    unindexed = []
    for folder in ['wiki/sources', 'wiki/concepts', 'wiki/entities']:
        folder_path = os.path.join(workspace, folder)
        if not os.path.exists(folder_path):
            continue
        for f in sorted(os.listdir(folder_path)):
            if not f.endswith('.md'):
                continue
            basename = f[:-3]
            if basename not in index_content and f not in index_content:
                unindexed.append(f"{folder}/{f}")

    print(f"\n📊 【检查 1：总索引挂载审计 (Index Registration)】")
    if unindexed:
        print(f"⚠️ 发现 {len(unindexed)} 个漏登 index.md 的孤立页面：")
        for u in unindexed[:10]:
            print(f"  - {u}")
        if len(unindexed) > 10:
            print(f"  ...等共 {len(unindexed)} 个")
    else:
        print("✅ 所有 Sources / Concepts / Entities 均已 100% 注册至 wiki/index.md！")

    # 2. 死链审计 (Broken Link Audit)
    known_nodes = set()
    for rel in all_md_files:
        known_nodes.add(rel)
        known_nodes.add(rel[:-3])
        known_nodes.add(os.path.basename(rel)[:-3])

    broken_links = []
    link_regex = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]')
    
    for rel, abs_p in all_md_files.items():
        if rel.startswith('raw/') or 'verify-' in rel or rel == 'wiki/log.md':
            continue
        content = load_file(abs_p)
        for target in link_regex.findall(content):
            t_clean = target.strip()
            if t_clean.startswith('http'):
                continue
            t_name = os.path.basename(t_clean)
            if t_clean.endswith('.md'):
                t_name = t_name[:-3]
            
            if t_clean not in known_nodes and t_name not in known_nodes:
                broken_links.append((rel, target))

    print(f"\n📊 【检查 2：维基图谱死链审计 (Broken Link Audit)】")
    if broken_links:
        print(f"⚠️ 发现 {len(broken_links)} 处潜在死链（引用了不存在的笔记）：")
        for source_doc, target_link in broken_links[:10]:
            print(f"  - [{source_doc}] -> [[{target_link}]]")
        if len(broken_links) > 10:
            print(f"  ...等共 {len(broken_links)} 处")
    else:
        print("✅ 维基层未发现任何死链引用！")

    # 3. 语法污染检查 (Raw Syntax Pollution Check)
    raw_dir = os.path.join(workspace, 'raw')
    bracket_pollution = []
    if os.path.exists(raw_dir):
        for f in sorted(os.listdir(raw_dir)):
            if not f.endswith('.md'):
                continue
            abs_p = os.path.join(raw_dir, f)
            content = load_file(abs_p)
            matches = re.findall(r'\[\[(.*?)\]\]', content)
            if matches:
                bracket_pollution.append((f, len(matches)))

    print(f"\n📊 【检查 3：原始资料语法净化检查 (Raw Hygiene)】")
    if bracket_pollution:
        print(f"⚠️ 发现 {len(bracket_pollution)} 篇 raw/ 文献中存在疑似矩阵/张量或未转义的伪双链：")
        for f_name, count in bracket_pollution[:5]:
            print(f"  - raw/{f_name} ({count} 处 [[...]])")
        print("💡 建议运行: python3 scripts/vault_lint.py sanitize-raw 进行自动修复")
    else:
        print("✅ raw/ 文献语法洁净，无伪双链干扰图谱！")

    print("\n" + "=" * 60)
    print("🏁 Lint 健康扫描执行完毕。")
    print("=" * 60)

def cmd_sanitize(workspace):
    print("=" * 60)
    print("🧹 [Sanitize Raw] 正在净化 raw/ 目录下的语法冲突...")
    print("=" * 60)
    raw_dir = os.path.join(workspace, 'raw')
    if not os.path.exists(raw_dir):
        print("毫无待处理的文件。")
        return

    fixed_count = 0
    for f in sorted(os.listdir(raw_dir)):
        if not f.endswith('.md'):
            continue
        abs_p = os.path.join(raw_dir, f)
        content = load_file(abs_p)
        new_content = content.replace('[[', '\\[\\[')
        if new_content != content:
            save_file(abs_p, new_content)
            fixed_count += 1
            print(f"  🛠️ 转义修复: raw/{f}")

    print(f"\n✅ 净化完成！共处理修复 {fixed_count} 篇原始资料。")

def cmd_prune(workspace, target_raw, apply=False):
    print("=" * 60)
    print(f"✂️ [Cascading Prune SOP] 级联精简清理流程")
    print(f"🎯 目标原始文献: {target_raw}")
    print(f"🛡️ 执行模式: {'【直接动刀 (APPLY)】' if apply else '【预演报告 (DRY-RUN)】'}")
    print("=" * 60)

    target_rel = os.path.relpath(os.path.join(workspace, target_raw), workspace)
    target_abs = os.path.join(workspace, target_rel)
    if not os.path.exists(target_abs):
        print(f"❌ 错误：目标文件 {target_rel} 在磁盘上不存在！")
        return

    target_basename = os.path.basename(target_rel)

    # 第一步：查找绑定的 Source 摘要页
    sources_dir = os.path.join(workspace, 'wiki', 'sources')
    matched_sources = []
    for f in os.listdir(sources_dir):
        if not f.endswith('.md'):
            continue
        abs_s = os.path.join(sources_dir, f)
        content = load_file(abs_s)
        if target_rel in content or target_basename in content:
            matched_sources.append(f)

    # 第二步：排查总索引受影响条目
    index_path = os.path.join(workspace, 'wiki', 'index.md')
    index_content = load_file(index_path)
    index_lines_to_remove = []
    for s_file in matched_sources:
        s_base = s_file[:-3]
        for line in index_content.split('\n'):
            if s_base in line:
                index_lines_to_remove.append(line)

    # 第三步：入度审计与概念 GC 预测
    all_md_files = get_all_md_files(workspace)
    in_degree = {}
    for rel, abs_p in all_md_files.items():
        if rel.startswith('wiki/concepts/') or rel.startswith('wiki/entities/'):
            in_degree[rel] = 0

    link_regex = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]')
    for rel, abs_p in all_md_files.items():
        if rel.startswith('raw/') or 'verify-' in rel or rel == 'wiki/log.md':
            continue
        if os.path.basename(rel) in matched_sources:
            continue
        content = load_file(abs_p)
        for target in link_regex.findall(content):
            t_clean = target.strip()
            for cand in in_degree.keys():
                cand_base = os.path.basename(cand)[:-3]
                if t_clean == cand or t_clean == cand_base:
                    in_degree[cand] += 1

    gc_candidates = []
    for s_file in matched_sources:
        abs_s = os.path.join(sources_dir, s_file)
        content = load_file(abs_s)
        for target in link_regex.findall(content):
            t_clean = target.strip()
            for cand, deg in in_degree.items():
                cand_base = os.path.basename(cand)[:-3]
                if (t_clean == cand or t_clean == cand_base) and deg == 0:
                    gc_candidates.append(cand)

    gc_candidates = sorted(list(set(gc_candidates)))

    print("\n📑 【自上而下四步级联影响分析清单】")
    print(f"1️⃣ 目标物理源文件 : {target_rel}")
    print(f"2️⃣ 连带清理摘要页 : {len(matched_sources)} 篇 -> {matched_sources}")
    print(f"3️⃣ 剔除总索引条目 : {len(index_lines_to_remove)} 行")
    for l in index_lines_to_remove:
        print(f"    - {l.strip()}")
    print(f"4️⃣ 触发垃圾回收(GC): {len(gc_candidates)} 个孤立概念/实体页 (剩余引用度为0)")
    for gc in gc_candidates:
        print(f"    - 🗑️ GC 清理: {gc}")

    if not apply:
        print("\n" + "-" * 60)
        print("💡 当前为 Dry-run 检查模式，未对文件作实质性修改。")
        print(f"👉 若确认无误要执行删除，请运行: python3 scripts/vault_lint.py prune \"{target_raw}\" --apply")
        print("-" * 60)
        return

    print("\n⚡ 正在正式执行级联清理...")
    
    os.remove(target_abs)
    print(f"  ✅ 已删物理源文件: {target_rel}")

    for s_file in matched_sources:
        abs_s = os.path.join(sources_dir, s_file)
        if os.path.exists(abs_s):
            os.remove(abs_s)
            print(f"  ✅ 已删 Source 摘要页: wiki/sources/{s_file}")

    new_index_lines = [l for l in index_content.split('\n') if l not in index_lines_to_remove]
    save_file(index_path, '\n'.join(new_index_lines))
    print("  ✅ 已精准剔除 wiki/index.md 中的相关索引条目")

    for gc in gc_candidates:
        abs_gc = os.path.join(workspace, gc)
        if os.path.exists(abs_gc):
            os.remove(abs_gc)
            print(f"  🗑️ 已垃圾回收孤立节点: {gc}")

    log_path = os.path.join(workspace, 'wiki', 'log.md')
    log_content = load_file(log_path)
    today = datetime.now().strftime("%Y-%m-%d")
    log_msg = f"## {today} lint/prune | prune {target_rel} (+ Cascading cleanup sources, index & gc {len(gc_candidates)} entities/concepts)\n"
    new_log = log_content.replace("# 维护日志\n\n", f"# 维护日志\n\n{log_msg}\n")
    save_file(log_path, new_log)
    print("  ✅ 已记录操作流水至 wiki/log.md")

    print("\n🏁 级联清理动刀闭环执行完毕！")

def main():
    parser = argparse.ArgumentParser(description="Knowledge Bank Vault Lint & Prune CLI")
    subparsers = parser.add_subparsers(dest="subcommand")

    subparsers.add_parser("lint", help="执行图谱死链、漏登、语法污染全面健康诊断")
    subparsers.add_parser("check", help="lint 命令别名")
    subparsers.add_parser("sanitize-raw", help="自动修复 raw/ 目录下未规范化的括号与伪标签")

    prune_p = subparsers.add_parser("prune", help="执行自上而下四步级联精简清理流程")
    prune_p.add_argument("path", help="待清理的 raw/ 原始资料相对路径")
    prune_p.add_argument("--apply", action="store_true", help="确认实质动刀删除（不加此参数则仅干跑输出报告）")

    args = parser.parse_args()
    workspace = get_workspace()

    if args.subcommand in ["lint", "check"]:
        cmd_lint(workspace)
    elif args.subcommand == "sanitize-raw":
        cmd_sanitize(workspace)
    elif args.subcommand == "prune":
        cmd_prune(workspace, args.path, apply=args.apply)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
