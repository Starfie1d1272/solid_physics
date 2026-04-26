# Homework 5, Problem 1: Zoeppritz Coefficients for Incident SV Wave

## 任务概述

计算 SV 波作为入射波，在固体-固体平面界面处产生的反射系数（P波 $R_{sp}$，SV波 $R_{ss}$）和透射系数（P波 $T_{sp}$，SV波 $T_{ss}$）。

## 完成情况

- [x] Cell 1：参数初始化（介质1（浅层地壳）：ρ=2.7 g/cm³, α=5.8 km/s, β=3.2 km/s；介质2（深层地壳）：ρ=3.3 g/cm³, α=7.2 km/s, β=3.9 km/s）
- [x] Cell 2：Zoeppritz 求解函数（Aki & Richards 2002 公式，支持复数角度处理临界角）
- [x] Cell 3：批量计算 0°-90° + 绘图 + 临界角标记

## 核心方法

### 1. Snell 定律
射线参数 $p = \sin i / \beta_1 = \sin\theta_{P1}/\alpha_1 = \sin\theta_{P2}/\alpha_2 = \sin\theta_{S2}/\beta_2$

使用 `numpy.lib.scimath.arcsin` 处理超出临界角后的复数角度。

### 2. Zoeppritz 矩阵（Aki & Richards 2002, Eq. 5.37）
SV 波入射的 4×4 矩阵方程 $\mathbf{M} \cdot \mathbf{x} = \mathbf{b}$：

- 第 1 行：垂直位移连续性
- 第 2 行：水平位移连续性
- 第 3 行：正应力 $\sigma_{zz}$ 连续性
- 第 4 行：切应力 $\sigma_{xz}$ 连续性

求解向量 $\mathbf{x} = [R_{sp}, R_{ss}, T_{sp}, T_{ss}]^T$

### 3. 临界角
- 反射 P 波临界角：$\sin^{-1}(\beta_1 / \alpha_1) \approx 33.5^\circ$
- 透射 P 波临界角：$\sin^{-1}(\beta_1 / \alpha_2) \approx 26.4^\circ$
- 透射 SV 波临界角：$\sin^{-1}(\beta_1 / \beta_2) \approx 55.1^\circ$

## 运行方式

```bash
cd ~/GitHub/solid_physics/HW5
mamba run -n solid_physics jupyter notebook HW5_Q1_Zoeppritz.ipynb
```

或 VS Code 打开 `.ipynb` 后选 `solid_physics` kernel。

### 依赖
- numpy, matplotlib（通过 `mamba env create -n solid_physics -f requirements.txt` 安装）

## 文件结构

```
HW5/
|├── HW5_Q1_Zoeppritz.ipynb    # 主 notebook
|├── HW5_Report.md             # 正式作业报告（含完整推导 + 数值验证）
|├── figures/
|│   └── HW5_Q1_Zoeppritz.png  # 生成图件
|└── README.md                 # 本文件
```

## 注意事项
- 超出临界角后系数变为复数，绘图时取绝对值 `np.abs()`
- 正常入射（i=0°）时 SV 波 mode conversion 产生非零 P 波，源于阻抗差异
