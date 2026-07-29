title: "分位数回归（Quantile Regression）原理与应用" date: 2026-07-24 author: "Avi Chawla & Akshay Pachaar" source: "https://mail.google.com/mail/u/0/#inbox/19f962933027e3e6" type: clipping
分位数回归（Quantile Regression）原理与应用
传统的回归模型（如 OLS 普通最小二乘法）通常只能给出一个点估计——即特定输入下目标变量的均值（Mean）。但在许多实际场景中（例如薪资预测、风险评估），单一点估计无法反映分布的离散程度。


例如，预测薪资为 $80k 远不如提供以下分位数区间具有指导意义：


* 25 分位数：$65k（25% 的员工薪资低于或等于该值）
* 50 分位数：$80k（中位数）
* 75 分位数：$95k（25% 的员工薪资高于或等于该值）


分位数回归（Quantile Regression）正是为了估计条件分位数而设计的工具。


________________


核心工作原理：Quantile Loss（Pinball Loss）
传统线性回归的均方误差（MSE）对正负误差赋予相同的惩罚权重；而分位数回归通过参数 $w$（权重）重新定义损失函数，使得两侧误差的惩罚不对等：


$$\text{Loss}(y, \hat{y}) = \begin{cases} w \cdot (y - \hat{y}), & \text{if } y \ge \hat{y} \ (1 - w) \cdot (\hat{y} - y), & \text{if } y < \hat{y} \end{cases}$$


* 当 $w = 0.75$ 时：赋予正误差更高权重，拟合曲线向上抬升，得到 75 分位数。
* 当 $w = 0.25$ 时：赋予负误差更高权重，拟合曲线向下压低，得到 25 分位数。
* 当 $w = 0.50$ 时：等价于绝对值损失（MAE），拟合出 50 分位数（中位数）。


________________


工程实现与应用
在 Python 中，可以通过定义 Quantile Loss 并结合 scipy.optimize.minimize 对模型参数求解，也可以直接使用支持分位数损失函数的树模型（如 LightGBM 的 objective='quantile'）。


分位数回归完美拟合了不均匀的数据分布，是构建置信区间与风险控制模型的理想方法。