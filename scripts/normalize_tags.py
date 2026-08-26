#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knowledge Bank Tag Normalization & Cleanup Tool
遵循 AGENTS.md §5 规范的全局 Tag 规范化、去噪与 Frontmatter 清洗工具。

用法:
  uv run --with pyyaml python scripts/normalize_tags.py           # 默认 Dry-run 预演
  uv run --with pyyaml python scripts/normalize_tags.py --dry-run # 显式 Dry-run 预演
  uv run --with pyyaml python scripts/normalize_tags.py --apply   # 确认执行全库清洗与落盘
"""

import os
import sys
import re
import argparse
import yaml
from pathlib import Path
from collections import defaultdict, Counter

# 同步 vault_lint.py 单一事实来源，消除两套定义不同步的风险
try:
    from vault_lint import STANDARD_TOP_LEVEL_TAGS, STANDARD_TAG_BRANCHES, validate_tag
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from vault_lint import STANDARD_TOP_LEVEL_TAGS, STANDARD_TAG_BRANCHES, validate_tag

# 动态组装全量合规标签集合（单向同步自 vault_lint）
APPROVED_TAGS = set(STANDARD_TOP_LEVEL_TAGS)
for branch, leaves in STANDARD_TAG_BRANCHES.items():
    for leaf in leaves:
        APPROVED_TAGS.add(f"{branch}/{leaf}")

# 常见合规三级细分叶子
APPROVED_MULTI_LEVEL_TAGS = {
    "LLM/arch/Mamba", "LLM/arch/MoE", "LLM/arch/attention",
    "LLM/training/RL", "LLM/training/post-train", "LLM/training/pre-train",
}
APPROVED_TAGS.update(APPROVED_MULTI_LEVEL_TAGS)

TAG_MAP = {
    # Top-level umbrella terms -> leaf mapping
    "RAG": "RAG/retrieval",
    "LLM": "LLM/arch",
    "llm": "LLM/arch",
    "CV": "CV/detection",
    "AI-Agent": "AI-Agent/coding",
    "AI-Agents": "AI-Agent/coding",
    "Agent": "AI-Agent/coding",
    "agent": "AI-Agent/coding",
    "Deep-Learning": "DeepLearning",
    "deep-learning": "DeepLearning",
    "MachineLearning": "Skill/data-analysis",
    "Machine-Learning": "Skill/data-analysis",
    "machine-learning": "Skill/data-analysis",
    "python": "Skill/python",
    "pytorch": "Skill/python",
    "Skill/python/pytorch": "Skill/python",
    "Claude-Code": "Skill/claude-code",
    "claude-code": "Skill/claude-code",
    "clippings": None,
    "Overview": None,

    # AI-Agent variations & unapproved branches
    "AI-Agent/harness": "AI-Agent/coding",
    "Agent-Harness": "AI-Agent/coding",
    "agent-harness": "AI-Agent/coding",
    "loop-engineering": "AI-Agent/coding",
    "AI-Agent/loop-engineering": "AI-Agent/coding",
    "harness-engineering": "AI-Agent/coding",
    "AI-Agent/eval": "AI-Agent/coding",
    "AI-Agent/evaluation": "AI-Agent/coding",
    "AI-Agent/infra": "Infra/AI",
    "AI-Agent/infrastructure": "Infra/AI",
    "AI-Agent/Infra": "Infra/AI",
    "AI-Agent/MCP": "AI-Agent/tool-calling",
    "AI-Agent/recursive-language-models": "AI-Agent/context-engineering",
    "Multi-Agent": "AI-Agent/multi-agent",
    "multi-agent": "AI-Agent/multi-agent",
    "sub-agents": "AI-Agent/multi-agent",
    "agent-teams": "AI-Agent/multi-agent",
    "maker-checker": "AI-Agent/multi-agent",
    "Skill/knowledge-bank": "AI-Agent/skill",
    "AI-Tools": "AI-Agent/tool-calling",
    "agent-framework": "AI-Agent/coding",
    "System-Architecture": "AI-Agent/coding",
    "Orchestration": "AI-Agent/coding",
    "Dynamic-Workflows": "AI-Agent/coding",
    "dynamic-workflows": "AI-Agent/coding",
    "visual-programming": "AI-Agent/UI",
    "state-management": "AI-Agent/memory",
    "memory-system": "AI-Agent/memory",
    "context-rot": "AI-Agent/context-engineering",
    "context-engineering": "AI-Agent/context-engineering",
    "AI-Engineering": "AI-Agent/coding",

    # LLM variations
    "LLM/Multimodal": "LLM/arch",
    "LLM/inference/kv-cache": "LLM/inference",
    "KV-Cache": "LLM/inference",
    "LLM-Serving": "LLM/inference",
    "decoding-strategies": "LLM/inference",
    "generation-parameters": "LLM/inference",
    "quantization": "LLM/inference",
    "model-compression": "LLM/inference",
    "Inference-Optimization": "LLM/inference",
    "Diffusion-LLM": "LLM/arch",
    "Autoregressive": "LLM/arch",
    "Kimi-K3": "LLM/arch",
    "Attention-Mechanism": "LLM/arch/attention",
    "attention-mechanism": "LLM/arch/attention",
    "flash-attention": "LLM/arch/attention",
    "sparse-attention": "LLM/arch/attention",
    "large-language-models": "LLM/arch",
    "prompt-engineering": "AI-Agent/prompt-engineering",
    "prompt-tuning": "LLM/training/post-train",
    "parameter-efficient-fine-tuning": "LLM/training/post-train",
    "peft": "LLM/training/post-train",
    "lora": "LLM/training/post-train",
    "qlora": "LLM/training/post-train",
    "fine-tuning": "LLM/training/post-train",
    "distillation": "LLM/training/post-train",
    "knowledge-transfer": "LLM/training/post-train",
    "rl": "LLM/training/RL",
    "grpo": "LLM/training/RL",
    "GRPO": "LLM/training/RL",
    "Reinforcement-Learning": "LLM/training/RL",
    "gepa": "AI-Agent/prompt-engineering",
    "auto-prompt": "AI-Agent/prompt-engineering",
    "dspy": "AI-Agent/prompt-engineering",
    "LLM-Evaluation": "LLM/reasoning",
    "training": "LLM/training",
    "training-techniques": "LLM/training",
    "Unsloth": "LLM/training",
    "NeMo-Gym": "LLM/training/RL",

    # RAG variations
    "colbert": "RAG/embedding",
    "sentence-similarity": "RAG/embedding",
    "bi-encoder": "RAG/embedding",
    "cross-encoder": "RAG/embedding",
    "embedding": "RAG/embedding",
    "representation-learning": "RAG/embedding",
    "vector-space": "RAG/embedding",
    "vector-database": "RAG/retrieval",
    "vector-search": "RAG/retrieval",
    "approximate-nearest-neighbor": "RAG/retrieval",
    "indexing": "RAG/retrieval",
    "search": "RAG/retrieval",
    "BM25": "RAG/retrieval",
    "sparse-retrieval": "RAG/retrieval",
    "chunking": "RAG/chunking",
    "text-splitting": "RAG/chunking",
    "REFRAG": "RAG/retrieval",
    "InformationRetrieval": "RAG/retrieval",

    # Data Science / ML variations
    "data-science": "Skill/data-analysis",
    "Data-Science": "Skill/data-analysis",
    "statistics": "Skill/data-analysis",
    "mathematics": "Skill/data-analysis",
    "linear-algebra": "Skill/data-analysis",
    "feature-engineering": "Skill/data-analysis",
    "data-preprocessing": "Skill/data-analysis",
    "categorical-encoding": "Skill/data-analysis",
    "variable-types": "Skill/data-analysis",
    "cyclical-features": "Skill/data-analysis",
    "data-deduplication": "Skill/data-analysis",
    "fuzzy-matching": "Skill/data-analysis",
    "blocking-technique": "Skill/data-analysis",
    "data-visualization": "Skill/data-analysis",
    "clustering": "Skill/data-analysis",
    "Clustering": "Skill/data-analysis",
    "KMeans": "Skill/data-analysis",
    "BreathingKMeans": "Skill/data-analysis",
    "knn": "Skill/data-analysis",
    "t-SNE": "Skill/data-analysis",
    "dimensionality-reduction": "Skill/data-analysis",
    "ML/dimension-reduction": "Skill/data-analysis",
    "unsupervised-learning": "Skill/data-analysis",
    "supervised-learning": "Skill/data-analysis",
    "classification": "Skill/data-analysis",
    "classification-models": "Skill/data-analysis",
    "Regression": "Skill/data-analysis",
    "regression": "Skill/data-analysis",
    "gbdt": "Skill/data-analysis",
    "ensemble-learning": "Skill/data-analysis",
    "bagging": "Skill/data-analysis",
    "random-patches": "Skill/data-analysis",
    "imbalanced-data": "Skill/data-analysis",
    "model-calibration": "Skill/data-analysis",
    "probability-estimation": "Skill/data-analysis",
    "model-testing": "Skill/data-analysis",
    "model-diagnostics": "Skill/data-analysis",
    "learning-curve": "Skill/data-analysis",
    "Model-Evaluation": "Skill/data-analysis",
    "Model-Interpretability": "Skill/data-analysis",
    "business-ml": "Skill/data-analysis",
    "machine-learning/evaluation": "Skill/data-analysis",
    "machine-learning/methodology": "Skill/data-analysis",
    "evaluation": "Skill/data-analysis",
    "algorithm": "Skill/data-analysis",
    "big-data": "Skill/data-analysis",
    "data-collection": "Skill/data-analysis",
    "Data-Version-Control": "Skill/data-analysis",
    "DVC": "Skill/data-analysis",
    "Reproducibility": "Skill/data-analysis",
    "optimization": "Skill/data-analysis",

    # DeepLearning theory
    "neural-network": "DeepLearning",
    "neural-networks": "DeepLearning",
    "activation-functions": "DeepLearning",
    "relu": "DeepLearning",
    "loss-function": "DeepLearning",
    "Loss-Function": "DeepLearning",
    "Double-Descent": "DeepLearning",
    "Generalization": "DeepLearning",
    "Over-parameterization": "DeepLearning",
    "nlp": "DeepLearning",
    "natural-language-processing": "DeepLearning",
    "modernbert": "DeepLearning",

    # Python & Programming
    "python/syntax": "Skill/python",
    "descriptor": "Skill/python",
    "oop": "Skill/python",
    "module-and-package": "Skill/python",
    "concurrency": "Skill/python",
    "parallelism": "Skill/python",
    "gil": "Skill/python",
    "multithreading": "Skill/python",
    "multiprocessing": "Skill/python",
    "coroutines": "Skill/python",
    "subinterpreters": "Skill/python",
    "engineering-practices": "Skill/python",
    "Software-Engineering": "Skill/python",
    "Software-Engineering/Observability": "AI-Agent/coding",
    "system-design": "AI-Agent/coding",
    "Architecture": "AI-Agent/coding",
    "architecture": "AI-Agent/coding",
    "Graph-Engineering": "AI-Agent/coding",
    "software-evolution": "Skill/python",
    "programming": "Skill/python",
    "computer-science": "Skill/python",
    "open-source": "Skill/python",
    "MetaAI": "AI-Agent/coding",
    "Configuration": "Skill/claude-code",
    "Config-Architecture": "Skill/claude-code",

    # Infra & GPU
    "MLOps": "Infra/AI",
    "LLMOps": "Infra/AI",
    "AI-Infra": "Infra/AI",
    "Infrastructure": "Infra/AI",
    "gpu": "Infra/gpu",
    "GPU/parallelism": "Infra/gpu",
    "GPU/acceleration": "Infra/gpu",
    "data-transfer": "Infra/AI",
    "AI-Hardware/Accelerator": "Infra/AI",
    "Computer-Architecture/Processor": "Infra/AI",
    "dataloader": "Infra/AI",
    "memory-pinning": "Infra/AI",
    "memory-management": "Infra/AI",
    "performance-tuning": "Infra/AI",
    "performance-optimization": "Infra/AI",
    "auto-tuning": "AI-Agent/prompt-engineering",
    "model-deployment": "Infra/AI",
    "ONNX": "Infra/AI",
    "ONNX-Runtime": "Infra/AI",
    "scale": "Infra/AI",
    "efficiency": "Infra/AI"
}

FORBIDDEN_FIELDS = {"confidence", "created", "ai-first"}

def normalize_tag_list(tags, ptype="source", content=""):
    if not isinstance(tags, list):
        if isinstance(tags, str):
            tags = [tags]
        else:
            tags = []
    
    normalized = []
    for t in tags:
        if not t:
            continue
        t_str = str(t).strip()
        
        # 针对 Overview 页面的顶层标签特殊保留
        if ptype == "overview" and t_str in STANDARD_TAG_BRANCHES:
            if t_str not in normalized:
                normalized.append(t_str)
            continue
        
        # 优先使用权威门禁校验器进行校验
        is_valid, _ = validate_tag(t_str, ptype)
        if is_valid:
            if t_str not in normalized:
                normalized.append(t_str)
            continue
        
        # 查表映射
        if t_str in TAG_MAP:
            target = TAG_MAP[t_str]
            if target:
                target_valid, _ = validate_tag(target, ptype)
                if target_valid and target not in normalized:
                    normalized.append(target)
            continue
        
        # 尝试大小写不敏感匹配合法标签
        matched = False
        for app in APPROVED_TAGS:
            if t_str.lower() == app.lower():
                is_valid, _ = validate_tag(app, ptype)
                if is_valid and app not in normalized:
                    normalized.append(app)
                matched = True
                break
        if matched:
            continue
        
        print(f"  ⚠️ 未知 Tag 无法映射: {t_str}")

    # Fallback 策略改造：严禁基于正文关键词猜测分类，若原始 Tags 全被清除则置为 [] 并打印警告待人工介入
    if not normalized and tags:
        print(f"  ⚠️ 原始 Tags {tags} 经清理/去噪后为空，无法自动推断合法 Tag，置为 [] (待人工复核)")

    return normalized

def process_file(file_path, workspace, apply=False):
    rel_path = os.path.relpath(file_path, workspace)
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        return False, None, None, f"读取失败: {e}"

    m = re.match(r"^---\n(.*?)\n---(.*)", content, re.DOTALL)
    if not m:
        return False, None, None, None

    fm_str = m.group(1)
    body = m.group(2)

    try:
        data = yaml.safe_load(fm_str)
        if not isinstance(data, dict):
            return False, None, None, None
    except Exception as e:
        return False, None, None, f"YAML 解析失败: {e}"

    original_data = dict(data)
    modified = False
    diffs = []

    # 1. 移除违规非标字段 (仅针对 wiki/ 文件)
    if rel_path.startswith("wiki/"):
        for ff in FORBIDDEN_FIELDS:
            if ff in data:
                del data[ff]
                modified = True
                diffs.append(f"移除禁止字段 '{ff}'")

    # 2. 规范化 tags
    ptype = data.get("type", "source" if rel_path.startswith("wiki/sources") else "concept")
    orig_tags = data.get("tags", [])
    if orig_tags is None:
        orig_tags = []
    new_tags = normalize_tag_list(orig_tags, ptype=ptype, content=content)

    if orig_tags != new_tags:
        data["tags"] = new_tags
        modified = True
        diffs.append(f"Tags 变更: {orig_tags} -> {new_tags}")

    if not modified:
        return False, original_data, data, None

    # 重构 Frontmatter
    if rel_path.startswith("wiki/"):
        field_order = ["type", "tags", "summary", "sources", "updated", "timeline"]
        reconstructed_fm = {}
        for key in field_order:
            if key in data:
                reconstructed_fm[key] = data[key]
        for key in data:
            if key not in reconstructed_fm:
                reconstructed_fm[key] = data[key]
    else:
        # raw/articles
        reconstructed_fm = data

    new_fm_str = yaml.dump(reconstructed_fm, allow_unicode=True, sort_keys=False, default_flow_style=False).strip()
    new_full_content = f"---\n{new_fm_str}\n---{body}"

    if apply:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_full_content)

    return True, original_data, reconstructed_fm, "; ".join(diffs)

def main():
    parser = argparse.ArgumentParser(description="Knowledge Bank Tag Normalizer")
    parser.add_argument("--dry-run", action="store_true", help="预演模式（不修改文件）")
    parser.add_argument("--apply", action="store_true", help="正式落盘应用更改")
    args = parser.parse_args()

    apply = args.apply
    if not apply:
        print("=" * 60)
        print("🔍 [Tag Normalizer] 正在以 Dry-Run 预演模式运行（不会修改任何文件）...")
        print("=" * 60)
    else:
        print("=" * 60)
        print("🚀 [Tag Normalizer] 正在执行全库 Tag 规范化与清洗落盘...")
        print("=" * 60)

    workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    target_dirs = [
        os.path.join(workspace, "wiki/sources"),
        os.path.join(workspace, "wiki/concepts"),
        os.path.join(workspace, "wiki/entities"),
        os.path.join(workspace, "wiki/comparisons"),
        os.path.join(workspace, "wiki/overview"),
        os.path.join(workspace, "raw/articles"),
        os.path.join(workspace, "raw/insights"),
        os.path.join(workspace, "Clippings")
    ]

    total_scanned = 0
    modified_files = []
    stats_by_dir = defaultdict(int)

    for tdir in target_dirs:
        if not os.path.exists(tdir):
            continue
        for root, _, files in os.walk(tdir):
            for file in sorted(files):
                if file.endswith(".md"):
                    total_scanned += 1
                    full_p = os.path.join(root, file)
                    rel_p = os.path.relpath(full_p, workspace)
                    mod, orig, new_fm, diff_summary = process_file(full_p, workspace, apply=apply)
                    if mod:
                        modified_files.append((rel_p, orig, new_fm, diff_summary))
                        top_dir = "/".join(rel_p.split("/")[:2])
                        stats_by_dir[top_dir] += 1

    print(f"\n📊 扫描完成！共扫描文件 {total_scanned} 篇，拟修改文件 {len(modified_files)} 篇。")
    print("-" * 60)
    for sdir, count in sorted(stats_by_dir.items()):
        print(f"  📁 {sdir:20}: {count} 篇文件变更")
    print("-" * 60)

    print(f"\n📝 详细变更清单（共 {len(modified_files)} 篇）:")
    for rel_p, orig, new_fm, diff_summary in modified_files:
        print(f"  📄 [{rel_p}]")
        print(f"     ↳ {diff_summary}")

    if not apply:
        print("\n" + "=" * 60)
        print("✅ Dry-run 预演完成！若确认无误，请运行以下命令正式执行落盘:")
        print("   uv run --with pyyaml python scripts/normalize_tags.py --apply")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print(f"✅ 全库清洗完成！已成功将变更落盘至 {len(modified_files)} 篇文件。")
        print("=" * 60)

if __name__ == "__main__":
    main()
