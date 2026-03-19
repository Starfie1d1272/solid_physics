# Homework 2: 应力张量分析与库仑破裂应力 (CFF) 建模

> **Due Date:** 2026/03/16

## 📝 任务概述 (Assignment Objective)
本作业分为理论计算与编程实操两部分，核心旨在掌握连续介质力学中的二维应力/应变张量分析，并利用应变观测数据，评估真实地震（1992 Landers Earthquake）对周边断层的库仑破裂应力（Coulomb Failure Function, CFF）影响及地震触发效应。

---

### Part 1: 二维应力张量基础分析
已知二维应力张量为：
$$ \sigma = \begin{pmatrix} -40 & -10 \\ -10 & -60 \end{pmatrix} \text{ MPa} $$
1. **断层面应力解析：** 分别使用**斜截面法** (Cauchy's Theorem) 和**坐标变换法**求取任意倾角 $\theta$ 断层面上的正应力 ($\sigma_n$) 和剪应力 ($\tau$)。
2. **可视化编程：** 以 5° 为间隔，编程计算并绘制该应力状态下的正应力与剪应力随倾角 $\theta$ 变化的分布图。
3. **主应力与最大剪应力：** 解析求解该状态下的主应力大小/方向，以及最大剪应力及其作用面方位。

---

### Part 2: 1992 Landers 地震综合分析案例
* **数据背景：** 1992 年加州南部 Landers 地震 ($M_s=7.3$) 发生后，Piñon Flat Observatory (PFO) 记录到了显著的应变静态变化。
* **题目来源：** Peter Shearer, *Introduction to Seismology* (P35, Problem 12)

本部分包含详细的理论推导与 Python 编程数值计算，具体分为以下阶段：

#### 📝 阶段一：理论与弹性参数推导 (Parts a - e)
* **(a) Lamé 参数反演：** 基于 P 波波速 ($\alpha=6\text{ km/s}$)、S 波波速 ($\beta=3.5\text{ km/s}$) 及密度 ($\rho=2.7\text{ Mg/m}^3$) 计算地层拉梅参数 $\lambda$ 和 $\mu$。
* **(b) 静态应力变化 ($\Delta\sigma$)：** 利用广义 Hooke 定律，将 Landers 地震引起的同震水平应变张量转换为深度 5km 处的应力变化张量 ($\tau_{11}, \tau_{22}, \tau_{12}$)。
* **(c)-(d) 主应变轴与长期应力积累：** 计算主应变轴方位角；并基于长期的地壳应变率 ($e_{11}, e_{22}, e_{12}$)，计算 1000 年积累的长期应力张量。
* **(e) 面积应变 (Areal Strain)：** 物理情景应用（Farmer Bob's land），计算每年及同震的土地面积绝对变化量。

#### 💻 阶段二：计算模型与编程实现 (Parts f - i)
*(本部分对应本目录下的 Python 脚本程序)*
* **(f) 任意方位角断层应力遍历：** 编写程序计算方位角 $0^\circ \sim 170^\circ$（10° 间隔）垂直断层上的正应力与剪应力。
* **(g) 库仑破裂应力变化 ($\Delta\text{CFF}$)：** 引入静摩擦系数 $\mu_s=0.2$，编程计算各个方位角断层上的同震 $\Delta\text{CFF}$，以及由长期应变引起的年均 $\Delta\text{CFF}$：
  $$ \Delta\text{CFF} = \Delta|\tau_s| + \mu_s \Delta\tau_n $$
* **(h) 地震触发机制 (Clock Advance/Retardation)：** 建立临界阈值模型，计算 Landers 地震对周边各个方位角断层的“时钟提前/延迟”效应 ($\Delta t$)。
* **(i) 物理意义探讨：** 结合 PFO 附近震后实际微震活动并未增加的观测事实，讨论 CFF 阈值模型的局限性与有效性。

## 📁 文件结构 (File Structure)

* `text1.py`: Part 1 针对基础应力张量计算与可视化的主程序。
* `text2_f.py`: Part 2(f) 断层应力方位角遍历计算程序。
* `text2_g.py`: Part 2(g) 库仑破裂应力 ($\Delta\text{CFF}$) 建模与计算程序。
* `text2_h.py`: Part 2(h) 地震触发时间延迟/提前 ($\Delta t$) 计算程序。
* `figures/`: 存放所有脚本输出的 PNG 关系曲线与可视化图表。
* 📄 **`HW2_report.md`**: 包含所有子题目的推导过程、矩阵演算、代码结果表格及论述的完整报告。