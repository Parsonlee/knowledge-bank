#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knowledge Bank Vault Lint & Cascading Pruning Tool
遵循 AGENTS.md 规范的自动化图谱健康检查与级联清理脚本。

用法:
  python3 scripts/vault_lint.py lint             # 执行图谱死链、漏登、张量语法全面诊断
  python3 scripts/vault_lint.py sanitize-raw     # 自动转义 raw/ 目录下正文中非链接的 Tensor/矩阵 伪出链
  python3 scripts/vault_lint.py prune <raw_path> # 预演（Dry-run）单篇原始资料的 4 步级联精简报告
  python3 scripts/vault_lint.py prune <raw_path> --apply # 确认执行单篇级联精简清理
  python3 scripts/vault_lint.py prune-orphans    # 预演批量清理已删 raw 物理文件对应的下游孤立 Source 与 Index
  python3 scripts/vault_lint.py prune-orphans --apply # 确认批量清理下游孤立页面
  python3 scripts/vault_lint.py recover-dates    # 预演为缺失时间的 raw/ 文章自动捞回并溯源创建时间
  python3 scripts/vault_lint.py recover-dates --apply # 确认执行时间捞回与注入
  python3 scripts/vault_lint.py fetch-published  # 预演利用 BrowserSkill 首屏极速提取真实发表时间
  python3 scripts/vault_lint.py fetch-published --apply # 确认启动真实浏览器批量抓取发布时间并注入
  python3 scripts/vault_lint.py fetch-published --apply --zhihu-only # 仅处理知乎文章
"""

import os
import sys
import re
import json
import time
import argparse
import subprocess
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
        print(f"⚠️ 发现 {len(broken_links)} 处潜在死链（引用了被删除或不存在的笔记）：")
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
        raw_files_map = get_all_md_files(workspace, folders=['raw'])
        for rel_p, abs_p in sorted(raw_files_map.items()):
            content = load_file(abs_p)
            body = re.sub(r'^---\n.*?\n---', '', content, flags=re.DOTALL)
            matches = re.findall(r'\[\[\s*[\d\-+.,\s]+\s*\]\]', body)
            if matches:
                bracket_pollution.append((rel_p, len(matches)))

    print(f"\n📊 【检查 3：原始资料正文张量语法净化检查 (Raw Hygiene)】")
    if bracket_pollution:
        print(f"⚠️ 发现 {len(bracket_pollution)} 篇 raw/ 文献正文中存在疑似张量/数字矩阵未转义伪双链：")
        for f_name, count in bracket_pollution[:5]:
            print(f"  - raw/{f_name} ({count} 处 [[矩阵]])")
        print("💡 建议运行: python3 scripts/vault_lint.py sanitize-raw 进行自动转义")
    else:
        print("✅ raw/ 文献正文洁净，无矩阵伪双链干扰图谱！")

    print("\n" + "=" * 60)
    print("🏁 Lint 健康扫描执行完毕。")
    print("=" * 60)

def cmd_sanitize(workspace):
    print("=" * 60)
    print("🧹 [Sanitize Raw] 正在净化 raw/ 目录正文中的张量数组伪双链...")
    print("=" * 60)
    raw_dir = os.path.join(workspace, 'raw')
    if not os.path.exists(raw_dir):
        return

    fixed_count = 0
    raw_files_map = get_all_md_files(workspace, folders=['raw'])
    for rel_p, abs_p in sorted(raw_files_map.items()):
        content = load_file(abs_p)
        m = re.match(r'^(---\n.*?\n---)(.*)', content, re.DOTALL)
        if m:
            fm, body = m.group(1), m.group(2)
        else:
            fm, body = "", content
        new_body = re.sub(r'\[\[(\s*[\d\-+.,\s]+)\]\]', r'\\[\\[\1\\]\\]', body)
        if new_body != body:
            save_file(abs_p, fm + new_body)
            fixed_count += 1
            print(f"  🛠️ 转义矩阵修复: {rel_p}")

    print(f"\n✅ 净化完成！共处理修复 {fixed_count} 篇原始资料。")

def cmd_prune(workspace, target_raw, apply=False):
    print("=" * 60)
    print(f"✂️ [Cascading Prune SOP] 单篇级联精简清理流程")
    print(f"🎯 目标原始文献: {target_raw}")
    print(f"🛡️ 执行模式: {'【直接动刀 (APPLY)】' if apply else '【预演报告 (DRY-RUN)】'}")
    print("=" * 60)

    target_rel = os.path.relpath(os.path.join(workspace, target_raw), workspace)
    target_abs = os.path.join(workspace, target_rel)
    if not os.path.exists(target_abs):
        print(f"❌ 错误：目标文件 {target_rel} 在磁盘上不存在！")
        return

    target_basename = os.path.basename(target_rel)

    sources_dir = os.path.join(workspace, 'wiki', 'sources')
    matched_sources = []
    for f in os.listdir(sources_dir):
        if not f.endswith('.md'):
            continue
        abs_s = os.path.join(sources_dir, f)
        content = load_file(abs_s)
        if target_rel in content or target_basename in content:
            matched_sources.append(f)

    index_path = os.path.join(workspace, 'wiki', 'index.md')
    index_content = load_file(index_path)
    index_lines_to_remove = []
    for s_file in matched_sources:
        s_base = s_file[:-3]
        for line in index_content.split('\n'):
            if s_base in line:
                index_lines_to_remove.append(line)

    all_md_files = get_all_md_files(workspace)
    in_degree = {}
    for rel, abs_p in all_md_files.items():
        if rel.startswith('wiki/concepts/') or rel.startswith('wiki/entities/'):
            in_degree[rel] = 0

    link_regex = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]')
    for rel, abs_p in all_md_files.items():
        if rel.startswith('raw/'):
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

def cmd_prune_orphans(workspace, apply=False):
    print("=" * 60)
    print("✂️ [Cascading Batch Prune] 批量清理已删 raw 物理文件对应的下游孤立 Source 与 Index")
    print(f"🛡️ 执行模式: {'【直接动刀 (APPLY)】' if apply else '【预演报告 (DRY-RUN)】'}")
    print("=" * 60)

    sources_dir = os.path.join(workspace, 'wiki', 'sources')
    raw_dir = os.path.join(workspace, 'raw')
    raw_files = set()
    if os.path.exists(raw_dir):
        for root, _, files in os.walk(raw_dir):
            for file in files:
                if file.endswith('.md'):
                    abs_path = os.path.join(root, file)
                    rel_path_to_raw = os.path.relpath(abs_path, raw_dir)
                    raw_files.add(rel_path_to_raw)

    orphan_sources = []
    for f in sorted(os.listdir(sources_dir)):
        if not f.endswith('.md'): continue
        p = os.path.join(sources_dir, f)
        content = load_file(p)
        matches = re.findall(r'raw/([^\n\"\'\]]+)', content)
        if not matches:
            orphan_sources.append(f)
        else:
            exists = any((m.strip() in raw_files) for m in matches)
            if not exists:
                orphan_sources.append(f)

    index_path = os.path.join(workspace, 'wiki', 'index.md')
    index_content = load_file(index_path)
    index_lines_to_remove = []
    for s_file in orphan_sources:
        s_base = s_file[:-3]
        for line in index_content.split('\n'):
            if s_base in line and line not in index_lines_to_remove:
                index_lines_to_remove.append(line)

    print("\n📑 【批量级联清理影响清单】")
    print(f"1️⃣ 发现物理文献(raw/)已丢失的下游 Source 摘要页 : {len(orphan_sources)} 篇")
    print(f"2️⃣ 需在总索引 wiki/index.md 中剔除的条目数 : {len(index_lines_to_remove)} 行")

    if not apply:
        print("\n" + "-" * 60)
        print("💡 当前为 Dry-run 检查模式，未对文件作实质性修改。")
        print("👉 若确认无误要批量清理，请运行: python3 scripts/vault_lint.py prune-orphans --apply")
        print("-" * 60)
        return

    print("\n⚡ 正式开始清理下游孤立 Source 和 Index...")
    removed_sources = 0
    for s_file in orphan_sources:
        abs_p = os.path.join(sources_dir, s_file)
        if os.path.exists(abs_p):
            os.remove(abs_p)
            removed_sources += 1

    new_index_lines = [l for l in index_content.split('\n') if l not in index_lines_to_remove]
    save_file(index_path, '\n'.join(new_index_lines))

    log_path = os.path.join(workspace, 'wiki', 'log.md')
    log_content = load_file(log_path)
    today = datetime.now().strftime("%Y-%m-%d")
    log_msg = f"## {today} lint/prune | 批量清理物理文件丢失的下游 {removed_sources} 篇 Source 摘要及 Index 目录\n"
    new_log = log_content.replace("# 维护日志\n\n", f"# 维护日志\n\n{log_msg}\n")
    save_file(log_path, new_log)

    print(f"✅ 成功清理 {removed_sources} 篇 Source 摘要及 {len(index_lines_to_remove)} 行 Index 记录！")

def cmd_recover_dates(workspace, apply=False):
    print("=" * 60)
    print("⏳ [Recover Dates] 正在为 raw/ 目录下缺失时间的文章溯源捞回创建时间...")
    print(f"🛡️ 执行模式: {'【直接动刀 (APPLY)】' if apply else '【预演报告 (DRY-RUN)】'}")
    print("=" * 60)

    raw_dir = os.path.join(workspace, 'raw')
    sources_dir = os.path.join(workspace, 'wiki', 'sources')
    if not os.path.exists(raw_dir):
        return

    raw_to_source_date = {}
    if os.path.exists(sources_dir):
        for f in os.listdir(sources_dir):
            if not f.endswith('.md'): continue
            sp = os.path.join(sources_dir, f)
            content = load_file(sp)
            raw_matches = re.findall(r'raw/([^\n\"\'\]]+)', content)
            date_matches = re.findall(r'(?:created|updated):\s*[\'\"]?(\d{4}-\d{2}-\d{2})', content)
            if raw_matches and date_matches:
                for rm in raw_matches:
                    raw_to_source_date[rm.strip()] = date_matches[0]

    raw_files = []
    if os.path.exists(raw_dir):
        for root, _, files in os.walk(raw_dir):
            for file in files:
                if file.endswith('.md'):
                    rel_path_to_raw = os.path.relpath(os.path.join(root, file), raw_dir)
                    raw_files.append(rel_path_to_raw)
    raw_files.sort()
    already_has_date = 0
    recovered_from_source = []
    recovered_from_git = []
    recovered_from_body = []
    failed_files = []

    for f in raw_files:
        abs_p = os.path.join(raw_dir, f)
        content = load_file(abs_p)
        m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if m and any(k in m.group(1) for k in ['created:', 'published:', 'date:', 'updated:']):
            already_has_date += 1
            continue

        if f in raw_to_source_date:
            recovered_from_source.append((f, raw_to_source_date[f]))
            continue

        body_dates = re.findall(r'202[0-9]年\s*[0-1]?[0-9]月\s*[0-3]?[0-9]日|202[0-9]-[0-1][0-9]-[0-3][0-9]', content[:2000])
        if body_dates:
            d_str = re.sub(r'[年月日\s]+', '-', body_dates[0]).strip('-')
            parts = d_str.split('-')
            if len(parts) == 3:
                d_clean = f"{parts[0]}-{int(parts[1]):02d}-{int(parts[2]):02d}"
                recovered_from_body.append((f, d_clean))
                continue

        try:
            git_out = subprocess.check_output(
                ['git', 'log', '--follow', '--reverse', '--format=%cI', '--', f'raw/{f}'],
                cwd=workspace, stderr=subprocess.DEVNULL
            ).decode('utf-8').strip().split('\n')[0]
            if git_out and len(git_out) >= 10:
                recovered_from_git.append((f, git_out[:10]))
                continue
        except Exception:
            pass

        failed_files.append(f)

    total_recovered = len(recovered_from_source) + len(recovered_from_git) + len(recovered_from_body)
    print("\n📑 【时间溯源捞回结果清单】")
    print(f"0️⃣ 已有时间戳的文章 : {already_has_date} 篇")
    print(f"1️⃣ 通过 Source 摘要页成功溯源 : {len(recovered_from_source)} 篇")
    print(f"2️⃣ 通过 Git 提交历史成功溯源 : {len(recovered_from_git)} 篇")
    print(f"3️⃣ 通过正文发表日期成功溯源 : {len(recovered_from_body)} 篇")
    print(f"❌ 无法溯源时间的文章 : {len(failed_files)} 篇")

    if not apply:
        print("\n" + "-" * 60)
        print("💡 当前为 Dry-run 检查模式，未作实质性修改。")
        print(f"👉 共计可为 {total_recovered} 篇无时间文章捞回创建时间！")
        print("👉 若确认注入，请运行: python3 scripts/vault_lint.py recover-dates --apply")
        print("-" * 60)
        return

    print("\n⚡ 正式开始为文章 YAML Header 注入时间戳...")
    injected_count = 0
    all_recovered = recovered_from_source + recovered_from_git + recovered_from_body

    for f_name, date_str in all_recovered:
        abs_p = os.path.join(raw_dir, f_name)
        content = load_file(abs_p)
        m = re.match(r'^(---\n.*?)(\n---)(.*)', content, re.DOTALL)
        if m:
            fm_body, fm_close, rest = m.group(1), m.group(2), m.group(3)
            new_content = f"{fm_body}\ncreated: {date_str}{fm_close}{rest}"
        else:
            title_clean = f_name[:-3]
            new_content = f"---\ntitle: {title_clean}\ncreated: {date_str}\n---\n\n{content}"
        save_file(abs_p, new_content)
        injected_count += 1

    log_path = os.path.join(workspace, 'wiki', 'log.md')
    log_content = load_file(log_path)
    today = datetime.now().strftime("%Y-%m-%d")
    log_msg = f"## {today} lint/recover-dates | 成功为 raw/ 目录下 {injected_count} 篇历史文章溯源捞回并注入创建时间\n"
    new_log = log_content.replace("# 维护日志\n\n", f"# 维护日志\n\n{log_msg}\n")
    save_file(log_path, new_log)

    print(f"✅ 成功为 {injected_count} 篇文章注入 `created: YYYY-MM-DD` 时间戳并记录操作流水！")

def normalize_date(d_str):
    if not d_str:
        return None
    clean = re.sub(r'[年月日/.]+', '-', str(d_str)).strip('-')
    parts = clean.split('-')
    if len(parts) >= 3:
        try:
            y = int(parts[0])
            m = int(parts[1])
            d = int(parts[2][:2])
            if 2000 <= y <= 2030 and 1 <= m <= 12 and 1 <= d <= 31:
                return f"{y:04d}-{m:02d}-{d:02d}"
        except ValueError:
            pass
    return None

def cmd_fetch_published(workspace, apply=False, limit=None, zhihu_only=False):
    print("=" * 60)
    print("🌐 [Fetch Published Dates] 正在利用 BrowserSkill 极速抓取首屏真实发布时间...")
    print(f"🛡️ 执行模式: {'【直接动刀 (APPLY)】' if apply else '【预演报告 (DRY-RUN)】'}")
    print("=" * 60)

    raw_dir = os.path.join(workspace, 'raw')
    if not os.path.exists(raw_dir):
        return

    raw_files = []
    if os.path.exists(raw_dir):
        for root, _, files in os.walk(raw_dir):
            for file in files:
                if file.endswith('.md'):
                    rel_path_to_raw = os.path.relpath(os.path.join(root, file), raw_dir)
                    raw_files.append(rel_path_to_raw)
    raw_files.sort()
    target_files = []
    already_published = 0

    for f in raw_files:
        abs_p = os.path.join(raw_dir, f)
        content = load_file(abs_p)
        m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if m and re.search(r'^published:\s*[\'\"]?202\d-\d{2}-\d{2}', m.group(1), re.MULTILINE):
            already_published += 1
            continue

        # 寻找可提取的外链 URL
        url_m = re.findall(r'^(?:source|url|readmedium|weixin|zhihu|github|cnblogs|juejin|infoq|sspai|qq)\s*:\s*([^\s\'\"\n]+)', content, re.MULTILINE | re.IGNORECASE)
        valid = [u for u in url_m if 'cubox.pro' not in u and ('http://' in u or 'https://' in u)]
        if not valid:
            url_m2 = re.findall(r'\[(?:Read Original|原文|源链接|来源|阅读原文)\]\(([^\)]+)\)', content, re.IGNORECASE)
            valid = [u for u in url_m2 if 'cubox.pro' not in u and ('http://' in u or 'https://' in u)]
        if not valid:
            all_u = re.findall(r'https?://[^\s\'\"\)\>\]]+', content)
            valid = [u for u in all_u if 'cubox.pro' not in u and not u.endswith('.jpg') and not u.endswith('.png') and not u.endswith('.css') and not u.endswith('.js')]

        if valid:
            target_files.append((f, valid[0]))

    zhihu_files = [(f, u) for f, u in target_files if 'zhihu.com' in u or '知乎' in f]
    normal_files = [(f, u) for f, u in target_files if 'zhihu.com' not in u and '知乎' not in f]

    if zhihu_only:
        target_files = zhihu_files
        print(f"\n🎯 当前模式：【仅处理知乎文章】，共筛选出 {len(target_files)} 篇")
    else:
        print(f"\n💡 已自动过滤出 {len(zhihu_files)} 篇知乎文章（因未登录弹窗遮挡，稍后单独处理）。")
        target_files = normal_files

    print(f"\n📑 【首屏发布时间待提取分析】")
    print(f"0️⃣ 已有 `published: YYYY-MM-DD` 真实时间的文章 : {already_published} 篇")
    print(f"1️⃣ 本批次待处理外部 URL 文章 : {len(target_files)} 篇")
    if target_files:
        print("   示例清单 (前 5 篇):")
        for f, u in target_files[:5]:
            print(f"   - raw/{f[:35]}... -> {u[:45]}...")

    if not apply:
        print("\n" + "-" * 60)
        print("💡 当前为 Dry-run 检查模式，未启动真实浏览器及修改文件。")
        print(f"👉 若确认启动浏览器全量提取，请运行: python3 scripts/vault_lint.py fetch-published --apply")
        print("-" * 60)
        return

    if limit and isinstance(limit, int):
        target_files = target_files[:limit]
        print(f"\n⚠️ 已限制本次处理文章数量上限为: {limit} 篇")

    bsk_bin = "/Users/ZHao/.local/bin/bsk"
    if not os.path.exists(bsk_bin):
        bsk_bin = "bsk"

    print("\n⚡ 正在启动 BrowserSkill 自动化浏览器窗口会话...")
    try:
        session_out = subprocess.check_output([bsk_bin, "session", "start"]).decode('utf-8').strip()
        session_id = session_out.split('\n')[-1].strip()
        print(f"  🟢 成功建立会话 Session ID: [{session_id}]")
    except Exception as e:
        print(f"❌ 启动 BrowserSkill 会话失败: {e}")
        return

    js_expr = """(async () => {
        for (let i = 0; i < 25; i++) {
            const isCaptcha = window.location.href.includes('wappoc') || window.location.href.includes('captcha') || (document.title && document.title.includes('安全验证')) || (document.body && document.body.innerText.includes('为了保护你的网络安全')) || (document.body && document.body.innerText.includes('环境异常'));
            if (isCaptcha) return "CAPTCHA_DETECTED";

            const wxEl = document.getElementById('publish_time') || document.querySelector('#publish_time') || document.querySelector('.rich_media_meta_text');
            if (wxEl && wxEl.innerText) {
                const m = wxEl.innerText.match(/202[0-9][-年/.]\\s*[0-1]?[0-9][-月/.]\\s*[0-3]?[0-9]/);
                if (m) return m[0];
            }
            const metas = [
                'meta[property="article:published_time"]',
                'meta[name="date"]',
                'meta[name="pubdate"]',
                'meta[property="og:release_date"]',
                'meta[itemprop="datePublished"]'
            ];
            for (const sel of metas) {
                const mEl = document.querySelector(sel);
                if (mEl && mEl.getAttribute('content')) {
                    const m = mEl.getAttribute('content').match(/202[0-9][-年/.]\\s*[0-1]?[0-9][-月/.]\\s*[0-3]?[0-9]/);
                    if (m) return m[0];
                }
            }
            const timeEls = document.querySelectorAll('time, .time, .date, .post-date, .article-time, .publish-time, .post-meta, .article-meta, .Post-RichText');
            for (const tEl of timeEls) {
                const txt = tEl.getAttribute('datetime') || tEl.innerText || '';
                const m = txt.match(/202[0-9][-年/.]\\s*[0-1]?[0-9][-月/.]\\s*[0-3]?[0-9]/);
                if (m) return m[0];
            }
            const bodyText = document.body ? document.body.innerText.slice(0, 1500) : '';
            const mBody = bodyText.match(/202[0-9][-年/.]\\s*[0-1]?[0-9][-月/.]\\s*[0-3]?[0-9]/);
            if (mBody) return mBody[0];
            
            await new Promise(r => setTimeout(r, 200));
        }
        return null;
    })()"""

    success_count = 0
    fail_count = 0

    try:
        total = len(target_files)
        for idx, (f_name, url) in enumerate(target_files, 1):
            print(f"[{idx}/{total}] 极速首屏提取: raw/{f_name[:35]}...", end="", flush=True)
            try:
                # 默认 load 且不超时阻塞，立刻进入 async 轮询首屏
                subprocess.run([bsk_bin, "navigate", url, "--session", session_id, "--timeout", "12s"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                # 提取首屏时间 (JS 内部重试高达 5 秒)
                eval_out = subprocess.check_output([bsk_bin, "evaluate", "--session", session_id, "--timeout", "10s", "--json", js_expr],
                                                   stderr=subprocess.DEVNULL).decode('utf-8').strip()
                val_obj = json.loads(eval_out)
                val = val_obj.get("value") if isinstance(val_obj, dict) else val_obj

                if val == "CAPTCHA_DETECTED":
                    print("\n  ⚠️ 触发微信/平台安全拦截！正在呼出浏览器干预窗口...", flush=True)
                    time.sleep(3.0) # 缓冲等待重定向页面在浏览器中加载完毕
                    subprocess.run([bsk_bin, "request-help", "--session", session_id,
                                    "--prompt", "检测到安全验证码/滑块验证，请在浏览器中完成验证。验证成功后页面会自动刷新，脚本会即刻继续！",
                                    "--title", "需解除防爬安全验证", "--timeout", "10m"],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                    # 无论 request-help 是否顺利（即使因为页面重定向导致通信通道重置），
                    # 只要还没有提取到真实时间或仍处在 CAPTCHA 页面，就在 Python 层进入最多 90 秒的死循环轮询监听！
                    wait_time = 0
                    while wait_time < 90:
                        try:
                            eval_out = subprocess.check_output([bsk_bin, "evaluate", "--session", session_id, "--timeout", "10s", "--json", js_expr],
                                                               stderr=subprocess.DEVNULL).decode('utf-8').strip()
                            val_obj = json.loads(eval_out)
                            val = val_obj.get("value") if isinstance(val_obj, dict) else val_obj
                            if val != "CAPTCHA_DETECTED" and val is not None:
                                print("  🟢 验证成功解除！正在提取真实时间...", end="", flush=True)
                                break
                        except Exception:
                            pass
                        time.sleep(2.0)
                        wait_time += 2

                norm_date = normalize_date(val)
                if norm_date:
                    print(f" -> ✅ {norm_date}")
                    abs_p = os.path.join(raw_dir, f_name)
                    content = load_file(abs_p)
                    m = re.match(r'^(---\n.*?)(\n---)(.*)', content, re.DOTALL)
                    if m:
                        fm_body, fm_close, rest = m.group(1), m.group(2), m.group(3)
                        if "published:" in fm_body:
                            fm_body = re.sub(r'^published:.*$', f"published: {norm_date}", fm_body, flags=re.MULTILINE)
                            new_content = f"{fm_body}{fm_close}{rest}"
                        else:
                            new_content = f"{fm_body}\npublished: {norm_date}{fm_close}{rest}"
                    else:
                        new_content = f"---\ntitle: {f_name[:-3]}\npublished: {norm_date}\n---\n\n{content}"
                    save_file(abs_p, new_content)
                    success_count += 1
                else:
                    print(" -> ⚠️ 未能提取时间")
                    fail_count += 1
            except Exception as e:
                print(" -> ❌ 抓取或异常")
                fail_count += 1
            time.sleep(0.8) # 保护浏览器和 CPU

    finally:
        print(f"\n🛑 正在关闭 BrowserSkill 会话 [{session_id}]...")
        try:
            subprocess.run([bsk_bin, "session", "stop", session_id], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("  ✅ 自动化浏览器窗口已优雅释放！")
        except Exception:
            pass

    log_path = os.path.join(workspace, 'wiki', 'log.md')
    log_content = load_file(log_path)
    today = datetime.now().strftime("%Y-%m-%d")
    log_msg = f"## {today} lint/fetch-published | 利用 BrowserSkill 自动抓取并注入 {success_count} 篇 raw/ 原始文献的真实 published 发表时间\n"
    new_log = log_content.replace("# 维护日志\n\n", f"# 维护日志\n\n{log_msg}\n")
    save_file(log_path, new_log)

    print(f"\n🎉 首屏批量时间提取完成！成功抓取并写入 {success_count} 篇，失败或无明确时间 {fail_count} 篇。")

def main():
    parser = argparse.ArgumentParser(description="Knowledge Bank Vault Lint & Prune CLI")
    subparsers = parser.add_subparsers(dest="subcommand")

    subparsers.add_parser("lint", help="执行图谱死链、漏登、张量语法全面诊断")
    subparsers.add_parser("check", help="lint 命令别名")
    subparsers.add_parser("sanitize-raw", help="自动转义 raw/ 正文中非链接的矩阵伪出链")

    prune_p = subparsers.add_parser("prune", help="执行单篇文献自上而下四步级联清理流程")
    prune_p.add_argument("path", help="待清理的 raw/ 原始资料相对路径")
    prune_p.add_argument("--apply", action="store_true", help="确认实质动刀删除")

    prune_o = subparsers.add_parser("prune-orphans", help="批量清理已被直接删去物理源文件的下游 Source 及 Index")
    prune_o.add_argument("--apply", action="store_true", help="确认批量实质清理")

    rec_d = subparsers.add_parser("recover-dates", help="为 raw/ 目录下缺失时间的文章溯源捞回并注入创建时间")
    rec_d.add_argument("--apply", action="store_true", help="确认实质注入时间戳")

    f_pub = subparsers.add_parser("fetch-published", help="利用 BrowserSkill 首屏极速提取真实发表时间")
    f_pub.add_argument("--apply", action="store_true", help="确认启动浏览器实质抓取")
    f_pub.add_argument("--limit", type=int, default=None, help="限制处理的最多文章数量")
    f_pub.add_argument("--zhihu-only", action="store_true", help="仅处理知乎文章")

    args = parser.parse_args()
    workspace = get_workspace()

    if args.subcommand in ["lint", "check"]:
        cmd_lint(workspace)
    elif args.subcommand == "sanitize-raw":
        cmd_sanitize(workspace)
    elif args.subcommand == "prune":
        cmd_prune(workspace, args.path, apply=args.apply)
    elif args.subcommand == "prune-orphans":
        cmd_prune_orphans(workspace, apply=args.apply)
    elif args.subcommand == "recover-dates":
        cmd_recover_dates(workspace, apply=args.apply)
    elif args.subcommand == "fetch-published":
        cmd_fetch_published(workspace, apply=args.apply, limit=args.limit, zhihu_only=args.zhihu_only)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
