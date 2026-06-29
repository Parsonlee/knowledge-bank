# 概念：早停（EarlyStopping）

> confidence: high

## 定义

训练中监控验证集 loss，当其连续多次不再下降时提前停止训练，避免过拟合并保存最优模型。

## 要点（全文实现）

- 关键参数：patience（容忍次数）、delta（最小改善量）、verbose
- 监控 val_loss：score = -val_loss
- 逻辑：
  - 若 score 优于 best_score：更新 best_score，保存 checkpoint，counter 归零
  - 若不优于：counter += 1，达到 patience 则 early_stop = True
- save_checkpoint：当验证 loss 下降时用 `torch.save(model.state_dict(), path)` 保存模型
- 训练循环中每个 epoch 结束调用，early_stop 为真则 break

## 来源

- [[PyTorch训练代码模板]]
