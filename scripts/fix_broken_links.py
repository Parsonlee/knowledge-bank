import os
import re
from collections import defaultdict

def get_all_md_files(workspace):
    folders = ['wiki']
    files_map = {}
    for folder in folders:
        folder_path = os.path.join(workspace, folder)
        if not os.path.exists(folder_path): continue
        for root, _, files in os.walk(folder_path):
            if '.git' in root or '.obsidian' in root: continue
            for f in files:
                if f.endswith('.md'):
                    abs_path = os.path.join(root, f)
                    rel_path = os.path.relpath(abs_path, workspace)
                    files_map[rel_path] = abs_path
    return files_map

workspace = "/Users/ZHao/WorkSpace/knowledge-bank"
all_md_files = get_all_md_files(workspace)

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
    with open(abs_p, 'r') as f:
        content = f.read()
    for target in link_regex.findall(content):
        t_clean = target.strip()
        if t_clean.startswith('http'):
            continue
        t_name = os.path.basename(t_clean)
        if t_clean.endswith('.md'):
            t_name = t_name[:-3]
        
        if t_clean not in known_nodes and t_name not in known_nodes:
            broken_links.append((rel, t_clean, target))

freq = defaultdict(int)
for rel, t_clean, target in broken_links:
    if t_clean.startswith('概念_') or t_clean.startswith('实体_'):
        freq[t_clean] += 1

to_downgrade = set([k for k, v in freq.items() if v <= 2])
high_freq = {k: v for k, v in freq.items() if v >= 3}

print("=== High Frequency Broken Links (Recommend to Create) ===")
for k, v in sorted(high_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{k}: {v} times")

print("\n=== Low Frequency Broken Links (<=2) to Downgrade ===")
print(f"Total to downgrade: {len(to_downgrade)} nodes.")

fixed_count = 0
for rel, abs_p in all_md_files.items():
    if rel.startswith('raw/') or 'verify-' in rel or rel == 'wiki/log.md':
        continue
    with open(abs_p, 'r') as f:
        content = f.read()
    
    new_content = content
    def repl(m):
        full_link = m.group(0)
        target = m.group(1).strip()
        if target in to_downgrade:
            if '|' in full_link:
                alias = full_link.split('|')[1].strip(']')
                return alias
            else:
                if target.startswith('概念_'):
                    return target[3:]
                elif target.startswith('实体_'):
                    return target[3:]
                else:
                    return target
        return full_link

    new_content = re.sub(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]', repl, new_content)
    if new_content != content:
        with open(abs_p, 'w') as f:
            f.write(new_content)
        fixed_count += 1

print(f"\nDowngraded low-frequency broken links in {fixed_count} files.")
