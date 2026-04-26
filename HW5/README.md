# Homework 5: Zoeppritz Coefficients

## Problem 1: SV Wave Incidence at Solid-Solid Interface

### 任务概述
计算 SV 波作为入射波，在固体-固体平面界面处产生的反射系数（P波 $R_{sp}$，SV波 $R_{ss}$）和透射系数（P波 $T_{sp}$，SV波 $T_{ss}$）。

### 完成情况
- [x] Cell 1：参数初始化（介质1（浅层地壳）：ρ=2.7 g/cm³, α=5.8 km/s, β=3.2 km/s；介质2（深层地壳）：ρ=3.3 g/cm³, α=7.2 km/s, β=3.9 km/s）
- [x] Cell 2：Zoeppritz 求解函数（Aki & Richards 2002 公式，支持复数角度处理临界角）
- [x] Cell 3：批量计算 0°-90° + 绘图 + 临界角标记

---

## Problem 2: P-Wave Incidence at Core-Mantle Boundary (Solid-Fluid Interface)

### 任务概述
计算 P 波从下地幔（固体）入射到核幔边界（CMB，固体-流体界面）时的位移反射系数（P波 $R_{pp}$，S波 $R_{ps}$）和透射系数（P波 $T_{pp}$，$T_{ps}=0$），并绘制随入射角的变化曲线。

### 完成情况
- [x] Cell 1：参数初始化（下地幔固体：ρ=5.5×10³ kg/m³, vp=13.7 km/s, vs=7.2 km/s；外地核流体：ρ=9.9×10³ kg/m³, vp=8.0 km/s, vs=0）
- [x] Cell 2：固体-流体界面 3×3 Zoeppritz 求解函数（法向位移连续、法向应力连续、切应力为零）
- [x] Cell 3：批量计算 0°-90° + 绘图 + 反射 S 波临界角标记（~31.71°）

### 核心方法

#### 1. Snell 定律
射线参数 $p = \sin i / \alpha_1$

转换波角度：
- 反射 S 波：$\theta_{S1} = \arcsin(p \beta_1)$
- 透射 P 波：$\theta_{P2} = \arcsin(p \alpha_2)$

使用 `numpy.lib.scimath.arcsin` 处理临界角后的复数角度。

#### 2. 固体-流体界面 Zoeppritz 方程组（3×3）
基于法向位移连续、法向应力连续及切向应力为零（流体无法承受剪应力）的边界条件：

$$
\mathbf{M} \cdot \mathbf{x} = \mathbf{b}, \quad \mathbf{x} = [R_{pp}, R_{ps}, T_{pp}]^T
$$

矩阵 $\mathbf{M}$：
- 第 1 行（法向位移）：$\cos\theta_{P1}, \sin\theta_{S1}, \cos\theta_{P2}$
- 第 2 行（法向应力）：$-\rho_1\alpha_1\cos(2\theta_{S1}), \rho_1\beta_1\sin(2\theta_{S1}), \rho_2\alpha_2$
- 第 3 行（切应力为零）：$\frac{\beta_1}{\alpha_1}\sin(2\theta_{P1}), -\cos(2\theta_{S1}), 0$

#### 3. 临界角
- 反射 S 波临界角：$\sin^{-1}(\beta_1 / \alpha_1) \approx 31.71^\circ$
- 透射 P 波：$\alpha_1 > \alpha_2$，无实数临界角

### 数值验证（正常入射 i=0°）
- $R_{pp} = \frac{\rho_2\alpha_2 - \rho_1\alpha_1}{\rho_1\alpha_1 + \rho_2\alpha_2} \approx 0.0249$
- $R_{ps} = 0$
- $T_{pp} = 1 - R_{pp} \approx 0.9751$

---

## 运行方式

```bash
cd ~/GitHub/solid_physics/HW5
mamba run -n solid_physics jupyter notebook HW5_Q1_Zoeppritz.ipynb  # Q1
mamba run -n solid_physics jupyter notebook HW5_Q2_CMB_Zoeppritz.ipynb  # Q2
```

或 VS Code 打开 `.ipynb` 后选 `solid_physics` kernel。

### 依赖
- numpy, matplotlib（通过 `mamba env create -n solid_physics -f requirements.txt` 安装）

## 文件结构

```
HW5/
├── HW5_Q1_Zoeppritz.ipynb      # Q1: SV波固体-固体界面
├── HW5_Q2_CMB_Zoeppritz.ipynb  # Q2: P波核幔边界（固体-流体）
├── HW5_Report.md               # 正式作业报告（含完整推导 + 数值验证）
├── figures/
│   ├── HW5_Q1_Zoeppritz.png    # Q1 生成图件
│   └── HW5_Q2_CMB_Zoeppritz.png # Q2 生成图件
└── README.md                   # 本文件
```

## 注意事项
- 超出临界角后系数变为复数，绘图时取绝对值 `np.abs()`
- Q1（SV波入射）：正常入射（i=0°）时 SV 波 mode conversion 产生非零 P 波
- Q2（P波入射 CMB）：流体介质无 S 波，$T_{ps}=0$ 恒成立；$\alpha_1 > \alpha_2$ 故无透射 P 波临界角
