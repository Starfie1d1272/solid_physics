import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

# ==========================================
# 0. 基础设置与数据读取
# ==========================================
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体
plt.rcParams['axes.unicode_minus'] = False    # 负号正常显示

file_path = r"C:\Users\starfie1d\Documents\我的文件\行星固体物理\Homework1\query.csv"
df = pd.read_csv(file_path)

# 清洗与筛选 (2010-2020, M>=5.0)
df = df.dropna(subset=['mag', 'latitude', 'longitude', 'depth', 'time'])
df['time'] = pd.to_datetime(df['time'], utc=True)
df_filtered = df[(df['time'].dt.year >= 2010) & (df['time'].dt.year <= 2020)]
df_filtered = df_filtered[df_filtered['mag'] >= 5.0]

# 提取后续需要的变量
mags = df_filtered['mag'].values
years_data = df_filtered['time'].dt.year.values
lons = df_filtered['longitude'].values
lats = df_filtered['latitude'].values
depths = df_filtered['depth'].values

# ==========================================
# 图 A：全球地震空间分布图
# ==========================================

plt.figure(figsize=(12, 6))
ax = plt.gca()

# 1. 使用你找到的 URL 加载全球低分辨率矢量地图数据（完美避开弃用警告！）
print("正在从网络加载地图数据，请稍候...")
world = gpd.read_file('https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip')

# 2. 绘制矢量底图 (陆地填浅灰，边界线白色，zorder=1 放底层)
world.plot(ax=ax, color='lightgrey', edgecolor='white', alpha=0.8, zorder=1)

# 3. 绘制地震散点图 (zorder=2 放上层)
# c=depths (颜色深浅代表深度), s (点的大小代表震级)
scatter = plt.scatter(lons, lats, c=depths, cmap='jet_r', 
                      s=(mags - 4.0)**3, alpha=0.7, edgecolors='none', zorder=2)

# 4. 细节修饰
plt.colorbar(scatter, label='震源深度 (km)')
plt.xlabel('经度 (Longitude)', fontsize=12)
plt.ylabel('纬度 (Latitude)', fontsize=12)
plt.title('图A: 全球地震空间分布与震源深度 (2010-2020, M≥5.0)', fontsize=14)

plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.grid(True, linestyle='--', alpha=0.5, zorder=0)

plt.tight_layout()

# 保存高清大图
plt.savefig(r"C:\Users\starfie1d\Documents\我的文件\行星固体物理\Homework1\Plot_A_Spatial_GeoPandas.png", dpi=300)

# ==========================================
# 图 B：累积型 G-R 定律关系图
# ==========================================
plt.figure(figsize=(9, 6))

max_mag = mags.max()
bins = np.arange(5.0, max_mag + 0.5, 0.5)
counts, edges = np.histogram(mags, bins=bins)

# 计算“累积”地震数：即将 counts 从大到小累加
cum_counts = np.cumsum(counts[::-1])[::-1]

# 累积型的 X 轴通常取区间的下边界（即 M >= 5.0, 5.5, 6.0...）
M_lower = edges[:-1]
N_cum = cum_counts / 11.0  # 计算年均累积发生率

# 过滤掉 0 值并取对数
valid = N_cum > 0
M_cum_valid = M_lower[valid]
log_N_cum = np.log10(N_cum[valid])

# 线性拟合 (lgN = a - bM)
coeff_cum = np.polyfit(M_cum_valid, log_N_cum, 1)
b_cum = -coeff_cum[0]
a_cum = coeff_cum[1]

plt.scatter(M_cum_valid, log_N_cum, color='green', marker='s', s=50, label='累积统计数据 $N(≥M)$')
plt.plot(M_cum_valid, a_cum - b_cum * M_cum_valid, color='darkorange', linewidth=2.5, 
         label=rf'累积拟合: $\lg N = {a_cum:.2f} - {b_cum:.2f}M$')

plt.xlabel('震级 M (下边界值, 表示 ≥M)', fontsize=14)
plt.ylabel(r'$\lg N$ (N 为 ≥M 的年平均总次数)', fontsize=14)
plt.title('图B: 累积型 G-R 定律关系图 (2010-2020)', fontsize=16)

plt.legend(fontsize=13)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# 保存图片
plt.savefig(r"C:\Users\starfie1d\Documents\我的文件\行星固体物理\Homework1\Plot_B_Cumulative_GR.png", dpi=300)

# (如果不想它弹窗卡住，可以在前面加 # 注释掉下面这行)
#plt.show()

# ==========================================
# 图 D：历年地震频次分布柱状图
# ==========================================
plt.figure(figsize=(10, 5))

# 统计每年发生的地震总数
year_counts = df_filtered['time'].dt.year.value_counts().sort_index()

# 找出地震最多的年份，用红色标出，其他的用蓝色
colors = ['red' if y in [2010, 2011] else 'steelblue' for y in year_counts.index]

bars = plt.bar(year_counts.index, year_counts.values, color=colors, alpha=0.8, edgecolor='black')

# 在柱子上标出具体的数字
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 20, int(yval), ha='center', va='bottom', fontsize=11)

plt.xticks(year_counts.index, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('年份', fontsize=14)
plt.ylabel('全球地震发生总次数 (M≥5.0)', fontsize=14)
plt.title('图D: 全球地震历年频次时间序列 (2010-2020)', fontsize=16)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(r"C:\Users\starfie1d\Documents\我的文件\行星固体物理\Homework1\Plot_D_Time_Series.png", dpi=300)
#plt.show()