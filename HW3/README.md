# Homework 3: 汶川地震波形数据下载、预处理与可视化

> **Due Date:** 2026/03/23

## 📝 任务概述 (Assignment Objective)
本作业旨在掌握实际地震学研究中最核心的数据处理流程。获取 2008 年汶川大地震的真实地震波形数据，利用 Python 的 **ObsPy** 库独立完成数据预处理、去仪器响应、坐标系旋转，并进行科学可视化（绘制台站分布地图与多台站波形剖面图）。

### 具体要求 (Specific Requirements)：

#### 1. 数据筛选与获取 (Data Query)
*   **地震事件：** 2008年5月12日汶川大地震。
*   **台站条件：**
    *   震中距 ($ \Delta $) 范围：30° ~ 90°
    *   台站分布：在方位角和震中距上尽量**均匀分布**，数量在 10 个以上。
    *   数据质量：包含完整三分量数据，且 P 波初动尽可能清晰。
*   **时间窗设定：** 利用 1D 速度模型（`iasp91`）计算走时，截取时间段为：**理论 P 波初动前 300s，至理论 S 波初动后 600s**。

#### 2. 数据预处理 (Data Processing)
针对下载的各台站三分量 (Z-N-E) 数据，进行以下处理：
*   **基础清洗：** 去趋势 (`detrend`)、去均值、合并数据 (`merge`)。
*   **去仪器响应 (Remove Response)：** 结合台站元数据 (Inventory)，将数字信号转换为真实的物理速度 (`output='VEL'`)，并应用 `pre_filt=(1.0/180, 1.0/150, 4, 5)` 进行频段滤波。
*   **坐标系旋转 (Rotation)：** 根据震中到台站的反方位角，将水平分量 N (North)、E (East) 旋转至断层坐标系 R (Radial，径向) 和 T (Transverse，切向)。

#### 3. 科学可视化 (Plotting)
生成并提交 4 张图件：
1.  **台站与震源分布图:** 包含地形/海岸线背景，震源使用红色五角星标记，台站使用蓝色三角形标记。
2.  **Z, R, T 分量波形剖面图 (Record Section):** 共 3 张。纵坐标为震中距，横坐标为发震后的绝对走时，需在波形上标注直达 P 波和 S 波的理论到时曲线。

---

## 📁 文件结构 (File Structure)

*   `data/`: 存放使用 PyWEED (GUI) 预先下载并经过人工质控的 13 个台站的三分量原始波形数据 (`.sac` 格式)。
*   `hw3.ipynb`: 核心工作区 (Jupyter Notebook)。包含本地数据读取、FDSN 仪器响应动态获取、波形预处理、坐标系旋转以及 4 张图件的生成代码。
*   `figures/`: 包含脚本自动输出的 4 张结果图件。
    *   `Figure1_Station_Map.png`: 3D 正射投影的台站与震源分布图。
    *   `Figure2_Section_Z.png`: Z 分量波形剖面图。
    *   `Figure3_Section_R.png`: R 分量波形剖面图。
    *   `Figure4_Section_T.png`: T 分量波形剖面图。
*   📄 **`HW3_Report.md`**: 本次作业的完整数据处理报告，包含参数设定依据及对 P/S 波震相物理特征的详细分析。

## 💡 核心 API 参考 (References)
*   **波形读取与处理:** `obspy.read`, `obspy.core.stream.Stream.remove_response`, `obspy.core.stream.Stream.rotate`
*   **元数据获取:** `obspy.clients.fdsn.Client("EARTHSCOPE")` 
*   **理论到时计算:** `obspy.taup.TauPyModel("iasp91")`
*   **空间几何计算:** `obspy.geodetics.base.gps2dist_azimuth`
*   **地图可视化:** `cartopy.crs`, `cartopy.feature`