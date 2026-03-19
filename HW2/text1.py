import numpy as np
import matplotlib.pyplot as plt

# 设置倾角范围 0 到 90 度，间隔为 5 度
theta_deg = np.arange(0, 95, 5)
theta_rad = np.radians(theta_deg)

# 根据推导公式计算正应力和剪应力
sigma_N = -50 - 10 * np.cos(2 * theta_rad) - 10 * np.sin(2 * theta_rad)
tau_S = 10 * np.sin(2 * theta_rad) - 10 * np.cos(2 * theta_rad)

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(theta_deg, sigma_N, marker='o', label='Normal Stress ($\sigma_N$)', color='blue')
plt.plot(theta_deg, tau_S, marker='s', label='Shear Stress ($\\tau_S$)', color='red')

# 设置图表属性
plt.title('Normal and Shear Stresses on Fault Plane vs. Dip Angle', fontsize=14)
plt.xlabel('Dip Angle $\\theta$ (degrees)', fontsize=12)
plt.ylabel('Stress (MPa)', fontsize=12)
plt.xticks(np.arange(0, 95, 5))
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

# 显示图像
plt.show()