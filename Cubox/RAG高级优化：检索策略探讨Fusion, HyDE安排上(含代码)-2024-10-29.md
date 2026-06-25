---
id: "7250874518892187132"
cubox_url: https://cubox.pro/web/card/7250874518892187132
url: https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484218&idx=1&sn=656549e48f411b94ebe72ecd61259324&chksm=c31049ccf467c0da37cde363ea3183eb2598c2a1fcdc50e582cbf29271fb13b69cf57df989d8&cur_album_id=3621348003472015367&scene=189
tags:
  - RAG
  - Retrieval

---
# RAG高级优化：检索策略探讨Fusion, HyDE安排上(含代码)

Fusion retrieval、HyDE和RAG-Fusion可以创建一个更健壮和准确的检索系统。本文将具体介绍并给出实现代码。

[Read in Cubox](https://cubox.pro/web/card/7250874518892187132)  
[Read Original](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484218&idx=1&sn=656549e48f411b94ebe72ecd61259324&chksm=c31049ccf467c0da37cde363ea3183eb2598c2a1fcdc50e582cbf29271fb13b69cf57df989d8&cur_album_id=3621348003472015367&scene=189)  

---

## Annotations  

> 倒数秩融合：使用 RRF 算法对检索到的文档进行重新排序，该算法结合了多次检索尝试的排名。  

def rrf_fusion(rankings, k=60):
    """
    互易秩融合算法
    :param rankings: 一个包含多个排序结果的列表，每个排序结果是一个文档ID的列表
    :param k: 平滑常数，默认值为60
    :return: 综合排序结果
    """
    from collections import defaultdict

    scores = defaultdict(float)
    
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking):
            scores[doc_id] += 1 / (k + rank + 1)
    
    # 根据综合评分进行排序
    fused_ranking = sorted(scores.keys(), key=lambda doc_id: scores[doc_id], reverse=True)
    
    return fused_ranking

# 示例用法
rankings = [
    ['doc1', 'doc2', 'doc3'],
    ['doc2', 'doc3', 'doc1'],
    ['doc3', 'doc1', 'doc2']
]

fused_ranking = rrf_fusion(rankings)
print(fused_ranking)

[Link️](https://cubox.pro/web/annotations/cards/7250874518892187132?highlight=7250874519064151717)  

