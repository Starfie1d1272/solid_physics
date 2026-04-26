# Homework 5: 固体-固体界面 Zoeppritz 方程与 SV 波斜入射问题

> **姓名:** 杜鑫宇  
> **学号:** 231830104  
> **日期:** 2026/04/27  
> **课程:** 行星固体物理

---

## 第一题：SV 波斜入射固体-固体平面界面的 Zoeppritz 系数

### 问题重述

考虑一个固体-固体平坦界面（设界面为 $z=0$ 平面），上下两半空间均为各向同性均匀弹性介质。一道 SV 波（横波，质点振动方向在入射面内）以角度 $i$ 从介质 1 斜入射至界面上。在界面上，SV 波会发生波型转换，产生以下四类次级波：

- **反射 P 波**（mode-converted），振幅记为 $R_{sp}$
- **反射 SV 波**（同模式反射），振幅记为 $R_{ss}$
- **透射 P 波**（mode-converted），振幅记为 $T_{sp}$
- **透射 SV 波**（同模式透射），振幅记为 $T_{ss}$

请根据弹性波动理论，推导出上述四个系数的求解方程（Zoeppritz 方程组）。

---

### 第一步：Snell 定律与射线参数

设入射 SV 波角度为 $i$（即 $\theta_{S1}$）。由于界面两侧介质的水平慢度必须连续，定义射线参数 $p$ 如下：

$$ p = \frac{\sin i}{\beta_1} = \frac{\sin \theta_{P1}}{\alpha_1} = \frac{\sin \theta_{P2}}{\alpha_2} = \frac{\sin \theta_{S2}}{\beta_2} $$

其中：
- $\alpha_1, \beta_1$ — 介质 1 的 P 波与 S 波速度
- $\alpha_2, \beta_2$ — 介质 2 的 P 波与 S 波速度
- $\theta_{P1}$ — 反射 P 波角度
- $\theta_{P2}$ — 透射 P 波角度
- $\theta_{S2}$ — 透射 SV 波角度

由上式可显式表示出各次级波的角度：

$$ \theta_{P1} = \arcsin\!\left(\frac{\alpha_1}{\beta_1} \sin i\right), \quad
\theta_{P2} = \arcsin\!\left(\frac{\alpha_2}{\beta_1} \sin i\right), \quad
\theta_{S2} = \arcsin\!\left(\frac{\beta_2}{\beta_1} \sin i\right) $$

当入射角 $i$ 超过某类波的临界角时，对应角度成为复数，反射/透射系数变为复数（表示全反射与相位偏移）。

---

### 第二步：物理边界条件

在固体-固体理想接触界面（$z=0$）上，必须满足以下四个连续性条件：

1. **法向位移连续**（$w_1 = w_2$）：上下介质在垂直于界面方向不能脱开
2. **切向位移连续**（$u_1 = u_2$）：上下介质在平行于界面方向不能滑动
3. **法向应力连续**（$\sigma_{zz1} = \sigma_{zz2}$）：垂直方向的挤压/拉伸力平衡
4. **切向应力连续**（$\sigma_{xz1} = \sigma_{xz2}$）：水平方向的剪切力平衡

---

### 第三步：Zoeppritz 方程组的建立

将入射 SV 波、反射 P 波、反射 SV 波、透射 P 波、透射 SV 波的位移场和应力场表达式分别代入上述四个边界条件，整理后得到一个 $4 \times 4$ 线性方程组 $\mathbf{M} \mathbf{x} = \mathbf{b}$。

未知数向量为：

$$ \mathbf{x} = \begin{bmatrix} R_{sp} \\ R_{ss} \\ T_{sp} \\ T_{ss} \end{bmatrix} $$

按照 Aki & Richards (2002) 的经典形式，系数矩阵 $\mathbf{M}$ 与右端项 $\mathbf{b}$ 的具体表达式如下：

#### 位移连续条件

**法向位移（第 1 行）：**

$$ -\sin\theta_{P1} \cdot R_{sp} - \cos i \cdot R_{ss} - \sin\theta_{P2} \cdot T_{sp} + \cos\theta_{S2} \cdot T_{ss} = \sin i $$

**切向位移（第 2 行）：**

$$ \cos\theta_{P1} \cdot R_{sp} - \sin i \cdot R_{ss} + \cos\theta_{P2} \cdot T_{sp} + \sin\theta_{S2} \cdot T_{ss} = \cos i $$

#### 应力连续条件

**法向应力 $\sigma_{zz}$（第 3 行）：**

$$ 2\rho_1\beta_1^2 p\cos\theta_{P1} \cdot R_{sp} + \rho_1\beta_1(1-2\beta_1^2 p^2) \cdot R_{ss} + 2\rho_2\beta_2^2 p\cos\theta_{P2} \cdot T_{sp} - \rho_2\beta_2(1-2\beta_2^2 p^2) \cdot T_{ss} = -\rho_1\beta_1(1-2\beta_1^2 p^2) $$

**切向应力 $\sigma_{xz}$（第 4 行）：**

$$ -\rho_1\alpha_1(1-2\beta_1^2 p^2) \cdot R_{sp} + 2\rho_1\beta_1^2 p\cos i \cdot R_{ss} + \rho_2\alpha_2(1-2\beta_2^2 p^2) \cdot T_{sp} + 2\rho_2\beta_2^2 p\cos\theta_{S2} \cdot T_{ss} = 2\rho_1\beta_1^2 p\cos i $$

> 注：上述方程中 $p$ 为第一步定义的射线参数，$\rho_1, \rho_2$ 分别为介质 1、2 的密度。此形式严格遵循 Aki & Richards (2002) 的约定，与常见的 P 波入射形式在符号和项的组合上存在差异。

---

### 第四步：求解方法

将上述四个方程写成矩阵形式 $\mathbf{M}\mathbf{x} = \mathbf{b}$ 后，可通过以下方法求解：

1. **克莱姆法则（Cramer's Rule）**：获得各系数的解析表达式（代数式较为冗长）
2. **矩阵求逆**：$\mathbf{x} = \mathbf{M}^{-1}\mathbf{b}$，适用于数值计算
3. **数值线性代数求解**：如高斯消元、LU 分解等

在实际应用中，当给定具体的介质参数和入射角度后，可直接采用数值方法求解。若需要对系数行为进行快速定性分析，也可使用 Zoeppritz 方程的近似形式（如 Aki-Richards 近似、Shuey 近似等）进行简化。

---

### 第五步：数值模拟验证

为了直观展示 Zoeppritz 系数的角度依赖特征，选取一组具有地球物理意义的参数进行数值求解：

| 参数 | 介质 1（浅层地壳） | 介质 2（深层地壳） |
| :-- | :--: | :--: |
| 密度 $\rho$ (g/cm³) | 2.7 | 3.3 |
| P 波速度 $\alpha$ (km/s) | 5.8 | 7.2 |
| S 波速度 $\beta$ (km/s) | 3.2 | 3.9 |

计算入射角范围 $0^\circ$ 到 $90^\circ$，步长 $0.5^\circ$，得到四个 Zoeppritz 系数的振幅随入射角的变化曲线（图 1）。

![Zoeppritz Coefficients for Incident SV Wave](./figures/HW5_Q1_Zoeppritz.png)
*(图 1：SV 波入射时四个 Zoeppritz 系数的振幅—角度关系曲线。垂直虚线标示三类临界角位置。)*

#### 临界角分析

由 Snell 定律可确定三个临界角：

- **反射 P 波临界角**：$i_c^{P1} = \arcsin(\beta_1/\alpha_1) \approx 33.5^\circ$
- **透射 P 波临界角**：$i_c^{P2} = \arcsin(\beta_1/\alpha_2) \approx 26.4^\circ$
- **透射 SV 波临界角**：$i_c^{S2} = \arcsin(\beta_1/\beta_2) \approx 55.1^\circ$

#### 结果讨论

从图 1 中可以观察到以下物理特征：

1. **小角度区域（$0^\circ < i < 26.4^\circ$）**：所有系数均为实数，波型转换正常发生。透射 P 波系数 $|T_{sp}|$ 在 $i \to 0^\circ$ 时趋于一个有限小值，这与 SV 波在垂直入射（$i=0^\circ$）时纵波激发效率较低的特征相符。

2. **第一临界角（$i = 26.4^\circ$）**：透射 P 波（$T_{sp}$）率先超临界，振幅出现剧烈跳变。此处 $T_{sp}$ 变为复数，$|T_{sp}|$ 迅速衰减，而能量重新分配到反射波和透射 SV 波中。

3. **第二临界角（$i = 33.5^\circ$）**：反射 P 波（$R_{sp}$）达到临界，其振幅同样呈现复杂弯曲。

4. **大角度区域（$i > 55.1^\circ$）**：所有转换波均处于超临界状态，$|R_{ss}|$ 逐渐趋于 1（全反射），$|T_{ss}|$ 稳定在非零但较小的水平。能量主要以反射 SV 波形式回到介质 1 中。

5. **反射 SV 波 $|R_{ss}|$** 在大部分角度范围内占主导地位，体现了 SV 波入射时同模式反射为主要能量通道的基本物理图像。

---

### 总结

本题目完成了以下工作：

1. **理论推导**：从 Snell 定律出发，建立 SV 波斜入射固体-固体界面的四个物理边界条件，严格导出了 Zoeppritz 方程组的 Aki & Richards (2002) 标准矩阵形式。该形式适用于任意入射角（包括超临界后的复数域计算）。

2. **数值验证**：采用数值矩阵求解方法，在典型地壳参数下计算了 $0^\circ$ 至 $90^\circ$ 范围内四个 Zoeppritz 系数的振幅特征，清晰识别了三类临界角及其对各系数的物理影响。

3. **物理图像**：结果明确了 SV 波入射与 P 波入射的关键差异——SV 波在近垂直入射时 P 波转换效率较低，且存在三个临界角而非两个，反映了横波入射时更丰富的波型转换机制。

---

## 附录

### A1. 代码运行说明

- 核心计算位于 `HW5_Q1_Zoeppritz.ipynb`，按单元顺序执行即可
- Cell 1：导入依赖与参数定义
- Cell 2：Zoeppritz 求解函数（支持复数角度，基于 `numpy.lib.scimath`）
- Cell 3：批量计算与可视化绘图

### A2. 依赖环境

```bash
cd ~/GitHub/solid_physics
mamba run -n solid_physics jupyter notebook HW5/HW5_Q1_Zoeppritz.ipynb
```

所需依赖：`numpy`, `matplotlib`
