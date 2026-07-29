title: 借助助教模型（Teacher Assistant）改进知识蒸馏 source: https://mail.google.com/mail/u/0/#inbox/19f6ca0f2c928ca3 author:

"[[DailyDoseOfDS]]" published: 2026-07-16 created: 2026-07-28 description: 解决 Teacher 与 Student 模型尺寸差距过大导致蒸馏效果下降的问题，引入尺寸介于两者之间的 Teacher Assistant 进行过渡蒸馏。 tags:

clippings

# 借助助教模型（Teacher Assistant）改进知识蒸馏

在模型压缩中，知识蒸馏（Knowledge Distillation）通过让小模型（Student）学习大模型（Teacher）的输出概率分布来传递知识。

## 传统知识蒸馏的痛点

实验表明：当 Teacher 模型与 Student 模型的尺寸差距过大时，蒸馏效果会大幅下滑。小模型无法直接吸收过于复杂的 Teacher 表达能力。

## 助教（TAKD）解决方案

引入一个尺寸介于两者之间的助教模型（Teacher Assistant）：

步骤 1：助教模型从超大 Teacher 模型中学习；

步骤 2：Student 模型再从助教模型中学习。

该方法（TAKD）在各项实验中表现均显著优于直接蒸馏（BLKD）和无蒸馏直接训练（NOKD），以极小的二次训练成本换取了 Student 模型在生产部署时的最高性价比。
