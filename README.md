# Planetary Solid Physics（行星固体物理）课程仓库

本仓库用于整理南京大学《行星固体物理》课程作业，包括代码、数据、图件和报告文档。

## 作业总览

| 作业 | 主题                                  | 目录          | 状态                       |
| ---- | ------------------------------------- | ------------- | -------------------------- |
| HW1  | 地震频度与 Gutenberg-Richter 定律分析 | [HW1](./HW1/) | 已完成                     |
| HW2  | 应力张量分析与库仑破裂应力（CFF）计算 | [HW2](./HW2/) | 已完成                     |
| HW3  | 地震波数据处理与波形可视化            | [HW3](./HW3/) | 已完成                     |
| HW4  | 火星内核射线追踪与震相走时对比        | [HW4](./HW4/) | 已完成                     |
| HW5  | Zoeppritz 方程与SV/P波斜入射系数计算  | [HW5](./HW5/) | 已完成                     |

## HW5 当前说明（2026/05/01）

- 题目一：SV 波斜入射固体-固体平面界面，推导并数值求解 4×4 Zoeppritz 方程组（Aki & Richards 2002）。
- 题目二：P 波斜入射核幔边界（CMB，固体-流体界面），推导并求解 3×3 Zoeppritz 方程组。
- 主要 Notebook：
	- [HW5_Q1_Zoeppritz.ipynb](./HW5/HW5_Q1_Zoeppritz.ipynb) — SV 波固体-固体界面
	- [HW5_Q2_CMB_Zoeppritz.ipynb](./HW5/HW5_Q2_CMB_Zoeppritz.ipynb) — P 波核幔边界（固体-流体）
- 主要文档：
	- [HW5/README.md](./HW5/README.md)
	- [HW5/HW5_Report.md](./HW5/HW5_Report.md)

## 运行环境

- Python 3.x
- NumPy / Pandas / Matplotlib
- ObsPy（含 TauP）
- VS Code + Git

各作业的详细说明请查看对应子目录中的 README。