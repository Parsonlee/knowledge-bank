# 概念_Quantized_Embedding

> tags: RAG, RAG/embedding
> confidence: high

## 定义

Quantized Embedding（压缩版稠密向量）通过量化把高精度浮点向量压缩为低位宽整数，降低存储和内存占用。

## 特点

- 压缩手段：float32 → int8 / uint8
- 压缩率：75% 体积下降，召回下降 <1%（实验值）
- 效果：内存×4↓，磁盘×4↓，向量检索 QPS×2↑
- 适合一次性加载进内存的 ANN 引擎（FAISS-IVF、Milvus）
- 痛点：必须重新训练或做 Post-Training Quantization；极低比特（4bit）会出现明显"值域截断"误差

## 适用场景

- 内存/磁盘告急时首选
- 案例：电商 2 亿商品向量 2.4TB → 600GB，P99 延迟 18ms → 9ms
- 实践建议：量化前务必在业务数据上测"召回@K 下降"曲线，别只看压缩率

## 关联

- 相关概念：[[概念_Dense_Embedding]]、[[概念_Binary_Embedding]]
- 来源：[[从BM25到Multi-Vector_6种Embedding演进路线]]
