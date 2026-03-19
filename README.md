# 🌍 Planetary Solid Physics (行星固体物理) @NJU

> 🎓 本仓库记录了南京大学 (Nanjing University) 《行星固体物理》课程的编程作业、数据分析报告与学习记录。

## 📅 作业目录 (Assignments Overview)

| 序号 | 课题 (Topic) | 核心技术/工具 | 截止日期 (Due) | 状态 |
| :---: | :--- | :--- | :---: | :---: |
| **[HW1](./HW1/)** |[**地震频度与 Gutenberg-Richter 定律分析**](./HW1/README.md) <br> *基于 USGS 目录验证 G-R 关系，求解 a, b 值。* | `pandas`, `matplotlib`, 线性拟合 | 2026/03/09 | ✅ 完成 |
| **[HW2](./HW2/)** |[**应力张量分析与库仑破裂应力 (CFF) 建模**](./HW2/README.md) <br> *二维张量计算及 1992 Landers 地震触发效应评估。* | `numpy`, 连续介质力学, 理论推导 | 2026/03/16 | ✅ 完成 |
| **[HW3](./HW3/)** |[**地震波数据处理：汶川地震波形下载、旋转与可视化**](./HW3/README.md) <br> *基于 ObsPy 获取波形，去仪器响应并绘制波形剖面图。* | `obspy`, `taup`, `cartopy`/`basemap` | 2026/03/23 | 🚧 进行中 |

---
*注：各个作业的具体要求、理论背景及代码文件说明，请进入对应的子目录查看具体的 `README.md`。*

## 🛠️ 本地开发环境与技术栈 (Tech Stack)

本项目的所有代码均在标准化、隔离的 Python 环境下开发测试。主要工具包括：
- **核心环境：** `Python 3.11.15` (独立虚拟环境 `solid_physic`)
- **地球物理专属库：** `ObsPy` (地震学处理核心)
- **编辑器与版本控制：** `VS Code` + `Git` / `GitHub`

---
*Created with ❤️ by [Xinyu Du (Starfield)](https://github.com/Starfie1d1272) | 2026*