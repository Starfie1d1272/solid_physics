# Planetary Solid Physics（行星固体物理）课程仓库

本仓库用于整理南京大学《行星固体物理》课程作业，包括代码、数据、图件和报告文档。

## 作业总览

| 作业 | 主题                                  | 目录          | 状态                       |
| ---- | ------------------------------------- | ------------- | -------------------------- |
| HW1  | 地震频度与 Gutenberg-Richter 定律分析 | [HW1](./HW1/) | 已完成                     |
| HW2  | 应力张量分析与库仑破裂应力（CFF）计算 | [HW2](./HW2/) | 已完成                     |
| HW3  | 地震波数据处理与波形可视化            | [HW3](./HW3/) | 已完成                     |
| HW4  | 火星内核射线追踪与震相走时对比        | [HW4](./HW4/) | 已完成                     |

## HW4 当前说明（2026/04/10）

- 题目一：利用 ObsPy TauP 构建火星 1D 模型（有/无固态内核），对比 27° 震相走时与射线路径。
- 题目二：从零实现射线追踪，对比直角坐标/球坐标/展平变换三种方法的走时与路径差异。
- 主要 Notebook：
	- [HW4_text1.ipynb](./HW4/HW4_text1.ipynb) — 火星内核 TauP 射线追踪
	- [HW4_text2.ipynb](./HW4/HW4_text2.ipynb) — 地球展平变换与自实现射线追踪
- 主要文档：
	- [HW4/README.md](./HW4/README.md)
	- [HW4/HW4_Report.md](./HW4/HW4_Report.md)
	- [HW4/HW4_Report_Submit.md](./HW4/HW4_Report_Submit.md)

## 运行环境

- Python 3.x
- NumPy / Pandas / Matplotlib
- ObsPy（含 TauP）
- VS Code + Git

各作业的详细说明请查看对应子目录中的 README。