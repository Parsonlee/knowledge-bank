# 概念_Binary_Embedding

> tags: RAG, RAG/embedding
> confidence: high

## 定义

Binary Embedding（极致 0/1 压缩）将浮点向量二值化为 0/1 表示，实现极致存储压缩与超快计算。

## 特点

- 编码方式：对 float 向量做 sign() 或 ITQ 旋转二值化
- 存储：1bit × dim，比 float32 省 32×
- 效果：计算改 XOR + popcount，CPU 单核可过 1 亿次/秒
- 痛点：汉明距离只能排序，无法得到真实相似度分值；精度平均下降 5~15%

## 适用场景

- 设备端、离线、大基数、只关心快的检索首选
- 案例：安卓相册重复照片清理，256 维 CNN 向量二值化后在 3 万张照片找相似耗时 80ms，耗电 <1%

## 关联

- 相关概念：[[概念_Quantized_Embedding]]、[[概念_Dense_Embedding]]
- 来源：[[从BM25到Multi-Vector_6种Embedding演进路线]]
