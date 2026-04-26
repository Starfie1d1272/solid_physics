import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# 第一步：设置中文字体（已为跨平台兼容进行简化）
# ==========================================
# SimHei 是 Windows 专有字体，此处已注释；
# 如果中文标签显示为方框，请安装中文字体（如 SimHei 或 Noto Sans CJK）并取消注释下一行：
# plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决图表中负号 '-' 显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 第二步：读取 USGS 下载的 CSV 数据
# ==========================================
# 使用 pathlib 构建跨平台数据路径
data_dir = Path(__file__).parent / "data"
file_path = str(data_dir / "query.csv")
print("正在读取数据...")
df = pd.read_csv(file_path)

# ==========================================
# 第三步：数据清洗与筛选
# ==========================================
# USGS 数据的震级列名称通常为 'mag'，时间列为 'time'
# 1. 剔除震级列中的缺失值 (NaN)
df = df.dropna(subset=['mag'])

# 2. 确保只截取 2010年 到 2020年 的数据
# 将 time 列转换为 Pandas 的时间格式，方便提取年份
df['time'] = pd.to_datetime(df['time'], utc=True)
# 筛选出年份在 2010 到 2020 之间的数据
df_filtered = df[(df['time'].dt.year >= 2010) & (df['time'].dt.year <= 2020)]

# 3. 筛选出震级 >= 5.0 的地震
mags = df_filtered[df_filtered['mag'] >= 5.0]['mag']
print(f"筛选完毕，共提取到 {len(mags)} 次 M>=5.0 的地震数据。")

# ==========================================
# 第四步：数据分箱（统计每 0.5 级区间的地震个数）
# ==========================================
# 获取最大的震级，用于确定统计区间的上限
max_mag = mags.max()

# 设定统计区间（bins）。
# np.arange 的三个参数分别是：起始值, 终止值(不包含), 步长
# 为了包含最大的地震，我们将终止值加上 0.5
bins = np.arange(5.0, max_mag + 0.5, 0.5)

# np.histogram 用于统计数据在各个区间内的频数
# counts 是每个区间内的地震次数，edges 是区间的边界 (如 5.0, 5.5, 6.0...)
counts, edges = np.histogram(mags, bins=bins)

# 寻找震级区间的中心值（例如[5.0, 5.5) 区间的中心值是 5.25）
# edges[:-1] 是每个区间的左边界，加上 0.25 即为中心值 M
M = edges[:-1] + 0.25

# ==========================================
# 第五步：计算年均地震发生率 N 及 lgN
# ==========================================
# 2010年~2020年共包含了 11 个完整的自然年
years = 11

# 计算每个震级区间的“每年平均地震次数” N
N = counts / years

# 剔除掉没有地震发生的震级区间（因为如果 N=0，lg(0) 在数学上无意义，代码会报错）
valid_indices = (N > 0)
M_valid = M[valid_indices]     # 过滤后的震级中心值
N_valid = N[valid_indices]     # 过滤后的年平均次数

# 计算以 10 为底的对数 lgN
log_N = np.log10(N_valid)

# ==========================================
# 第六步：线性拟合 (利用最小二乘法计算 G-R 定律的 a 和 b)
# ==========================================
# G-R 定律公式: lgN = a - bM
# 利用 np.polyfit 对 M 和 log_N 进行一次多项式（直线）拟合
# 返回的 coefficients 包含了直线的 [斜率, 截距]
coefficients = np.polyfit(M_valid, log_N, 1)

slope = coefficients[0]     # 斜率对应公式里的 -b
intercept = coefficients[1] # 截距对应公式里的 a

b = -slope
a = intercept

print(f"拟合完成！得到 G-R 定律参数: a = {a:.4f}, b = {b:.4f}")

# 生成一条拟合直线的 Y 值，用于在图上画出这条线
log_N_fit = a - b * M_valid

# ==========================================
# 第七步：使用 Matplotlib 绘制关系图
# ==========================================
plt.figure(figsize=(9, 6)) # 设置画布大小

# 1. 绘制实际数据的散点图
plt.scatter(M_valid, log_N, color='red', marker='o', s=60, label='实际统计数据', zorder=5)

# 2. 绘制拟合出来的直线
fit_equation = r'$\lg N = {:.2f} - {:.2f} M$'.format(a, b)
plt.plot(M_valid, log_N_fit, color='blue', linewidth=2.5, linestyle='-', label=f'拟合直线: {fit_equation}')

# 3. 图表排版与美化
plt.xlabel('震级 M (区间中心值)', fontsize=14)
plt.ylabel(r'$\lg N$ (N 为年平均发生次数)', fontsize=14)
plt.title('全球地震震级-频度关系 G-R定律 (2010-2020, M≥5.0)', fontsize=16)

# 设置刻度标签的大小
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# 显示图例
plt.legend(fontsize=13, loc='upper right')

# 添加网格线，使图表更加专业易读
plt.grid(True, which='major', linestyle='--', alpha=0.7)

# 自动紧凑布局
plt.tight_layout()

# 将生成的图片保存到和 csv 相同的文件夹下
save_path = data_dir / "GR_Law_Plot.png"
plt.savefig(save_path, dpi=300)
print(f"图表已保存至: {save_path}")

# 显示图表
plt.show()