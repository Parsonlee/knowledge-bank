#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knowledge Bank Raw Folder Restructure Tool (Smart Classification)
将 raw/ 下 the md 文件根据文件名智能分流到 articles/, playbooks/, insights/ 目录，
创建 papers/ 和 transcripts/ 作为空目录备用，
并级联更新整个 Vault 的双向链接与 sources frontmatter 引用。
"""

import os
import sys
import shutil
import subprocess

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

def get_target_subdir(filename):
    # 分类关键字配置
    playbook_keywords = [
        "代码段", "命令", "模板", "Matplotlib", "matplotlib", "Pandas", "pandas",
        "Pytorch", "PyTorch", "pytorch", "FastAPI", "Uvicorn", "Normalization",
        "SVD", "OCR", "数据增强", "一行代码", "手把手", "指令", "技巧", "规则"
    ]
    
    insight_keywords = [
        "创业", "初入投资", "幸福", "初创公司", "独立开发", "投资", "备战与复盘",
        "幸福", "真相", "经验", "全景", "前沿", "认知"
    ]
    
    # 转换为小写进行匹配，但中文不受影响
    fn_lower = filename.lower()
    
    # 检查 playbook 关键字
    for kw in playbook_keywords:
        if kw.lower() in fn_lower:
            return 'playbooks'
            
    # 检查 insight 关键字
    for kw in insight_keywords:
        if kw.lower() in fn_lower:
            return 'insights'
            
    return 'articles'

def main():
    workspace = get_workspace()
    raw_dir = os.path.join(workspace, 'raw')
    
    if not os.path.exists(raw_dir):
        print("❌ 错误：未找到 raw 目录")
        return

    # 1. 定义子目录并创建
    subdirs = ['articles', 'papers', 'transcripts', 'playbooks', 'insights']
    for subdir in subdirs:
        os.makedirs(os.path.join(raw_dir, subdir), exist_ok=True)
    print(f"✅ 已创建/确认子目录：{subdirs}")

    # 2. 扫描 raw/ 根目录下待移动的 markdown 文件
    files_to_move = []
    for f in os.listdir(raw_dir):
        # 排除子目录，仅处理根目录下的 md 文件
        if f.endswith('.md') and os.path.isfile(os.path.join(raw_dir, f)):
            files_to_move.append(f)

    if not files_to_move:
        print("ℹ️ 未在 raw/ 根目录下找到待移动的 markdown 文件，可能已经重构完毕。")
        return

    print(f"📊 发现待移动的原始资料共 {len(files_to_move)} 篇")

    # 3. 搬运文件并记录映射关系
    # 映射字典格式： {文件名: 目标子目录}
    file_dest_map = {}
    moved_count = 0
    
    for f in files_to_move:
        dest_subdir = get_target_subdir(f)
        file_dest_map[f] = dest_subdir
        
        old_path = os.path.join(raw_dir, f)
        new_path = os.path.join(raw_dir, dest_subdir, f)
        
        # 尝试使用 git mv
        res = subprocess.run(['git', 'mv', old_path, new_path], 
                             cwd=workspace, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if res.returncode == 0:
            moved_count += 1
        else:
            # 退回普通的 shutil.move
            shutil.move(old_path, new_path)
            moved_count += 1
            
    print(f"✅ 成功分类搬运 {moved_count} 个物理文献：")
    # 统计各个子目录搬运的文件数
    stats = {s: 0 for s in subdirs}
    for f, dest in file_dest_map.items():
        stats[dest] += 1
    for s, c in stats.items():
        print(f"  - {s}/ : {c} 篇")

    # 4. 全库扫描 md 文件进行链接与引用的替换
    print("🔄 开始全库级联更新链接与引用...")
    all_md_files = []
    for root, _, files in os.walk(workspace):
        # 排除 git, obsidian, tmp 等非文档目录
        if any(p in root for p in ['.git', '.obsidian', 'tmp', '.agents', '.claude']):
            continue
        for f in files:
            if f.endswith('.md'):
                all_md_files.append(os.path.join(root, f))
                
    # 包含根目录下的 AGENTS.md
    agents_md = os.path.join(workspace, 'AGENTS.md')
    if agents_md not in all_md_files and os.path.exists(agents_md):
        all_md_files.append(agents_md)

    # 建立替换映射对
    replacement_pairs = []
    for f, dest_subdir in file_dest_map.items():
        f_no_ext = f[:-3]
        # 精准匹配带 md 后缀的路径
        replacement_pairs.append((f"raw/{f}", f"raw/{dest_subdir}/{f}"))
        # 精准匹配不带 md 后缀的路径 (Obsidian 内部链)
        replacement_pairs.append((f"raw/{f_no_ext}", f"raw/{dest_subdir}/{f_no_ext}"))

    # 执行替换
    updated_files_count = 0
    for md_path in all_md_files:
        content = load_file(md_path)
        original_content = content
        
        for src, dst in replacement_pairs:
            if src in content:
                content = content.replace(src, dst)
                
        if content != original_content:
            save_file(md_path, content)
            updated_files_count += 1

    print(f"✅ 级联更新完成！共修改了 {updated_files_count} 个文件中的链接/引用")

    # 5. 登记维护日志到 wiki/log.md
    log_path = os.path.join(workspace, 'wiki', 'log.md')
    if os.path.exists(log_path):
        log_content = load_file(log_path)
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        
        log_details = f"- **目录分类**：在 `raw/` 下创建子目录 `articles/`、`papers/`、`transcripts/`、`playbooks/`、`insights/`，并将根目录下的 {len(files_to_move)} 篇物理文献智能分流：\n"
        for s, c in stats.items():
            if c > 0:
                log_details += f"  - `raw/{s}/`: {c} 篇\n"
        log_details += f"- **级联更新**：自动检索并更新了全库 {updated_files_count} 个包含 `raw/` 路径引用的 markdown 文件的 YAML sources 字段及正文链接，确保图谱未发生断链。\n"
        
        log_msg = (
            f"## [{today}] chore/restructure-raw | 智能分类重构 raw/ 目录结构\n"
            f"{log_details}"
        )
        if "# Wiki Log\n\n" in log_content:
            new_log = log_content.replace("# Wiki Log\n\n", f"# Wiki Log\n\n{log_msg}\n")
        elif "# 维护日志\n\n" in log_content:
            new_log = log_content.replace("# 维护日志\n\n", f"# 维护日志\n\n{log_msg}\n")
        else:
            new_log = log_content + f"\n\n{log_msg}"
        save_file(log_path, new_log)
        print("✅ 已记录操作流水至 wiki/log.md")

    print("\n🏁 重构搬运动作执行完毕！")

if __name__ == '__main__':
    main()
