# Homework 3: 汶川地震波形数据下载、预处理与可视化

> **Due Date:** 2026/03/23

## 📝 任务概述 (Assignment Objective)
本作业旨在掌握实际地震学研究中最核心的数据处理流程。利用 Python 的 **ObsPy** 库，获取 2008 年汶川大地震的真实地震波形数据，并独立完成数据筛选、去仪器响应、坐标系旋转以及最终的科学可视化（绘制台站分布图与地震波剖面图）。

### 具体要求 (Specific Requirements)：

#### 1. 数据筛选与下载 (Data Query & Download)
*   **地震事件：** 2008年5月12日汶川大地震。
*   **台站条件：**
    *   震中距 ($ \Delta $) 范围：30° ~ 90°
    *   台站分布：在方位角和震中距上尽量**均匀分布**，数量在 10 个以上。
    *   数据质量：P 波初动尽可能清晰（可结合 GUI 软件如 PyWEED 辅助挑选）。
*   **时间窗设定：** 利用 1D 速度模型（如 `iasp91` 或 `ak135`）计算走时，截取时间段为：**理论 P 波初动前 300s，至理论 S 波初动后 600s**。

#### 2. 数据预处理 (Data Processing)
针对下载的各台站三分量 (Z-N-E) 数据，需进行以下处理：
*   **基础清理：** 去趋势 (`detrend`)、去均值、合并断片 (`merge`)。
*   **去仪器响应 (Remove Response)：** 将数字信号转换为真实的物理速度 (`output='VEL'`)，并应用 `pre_filt` 频段滤波 (例如 `1.0/180, 1.0/150, 4, 5`)。
*   **坐标系旋转 (Rotation)：** 根据震中到台站的方位角/反方位角，将水平分量 N (North)、E (East) 旋转至断层坐标系 R (Radial，径向) 和 T (Transverse，切向)。

#### 3. 科学可视化 (Plotting)
需生成并提交 **4 张** 高质量图件：
1.  **台站与震源分布图 (Station Map):** 包含海岸线或地形背景，震源使用**红色五角星**标记，台站使用**三角形**标记。
2.  **Z 分量波形剖面图 (Z-Component Record Section):** 纵坐标为震中距，横坐标为走时。需在波形上标注直达 P 波和 S 波的理论到时曲线/标记。
3.  **R 分量波形剖面图 (R-Component Record Section):** 同上，展示去响应及旋转后的径向分量。
4.  **T 分量波形剖面图 (T-Component Record Section):** 同上，展示去响应及旋转后的切向分量。

---

## 📁 文件结构 (File Structure)

*(建议的目录结构)*
*   `data/`: 存放使用 FDSNWS 或 PyWEED 下载的原始波形数据 (如 `.sac` 或 `.mseed`) 及仪器响应文件 (`.xml`)。
*   `hw3_download.py`: (可选) 利用 `obspy.clients.fdsn` 批量请求台站信息与波形数据的脚本。
*   `hw3_process_and_plot.py`: 核心数据处理脚本，包含去仪器响应、`NE->RT` 旋转计算，以及 4 张图件的绘制代码。
*   `figures/`:
    *   `station_map.png`: 包含海岸线的台站震中分布地图。
    *   `section_Z.png`: Z 分量波形剖面图。
    *   `section_R.png`: R 分量波形剖面图。
    *   `section_T.png`: T 分量波形剖面图。
*   📄 **`HW3_Report.pdf`** (若需要): 包含处理流程说明、图件展示及可能的数据质量分析简述。

## 💡 核心 API 参考 (References)
*   **数据下载:** `obspy.clients.fdsn.Client("IRIS")` 
*   **去仪器响应与旋转:** `obspy.core.stream.Stream.remove_response`, `obspy.core.stream.Stream.rotate`
*   **理论到时计算:** `obspy.taup.TauPyModel("iasp91")`
*   **方位角计算:** `obspy.geodetics.base.gps2dist_azimuth`