import numpy as np
import pandas as pd

def compute_delta_t_table():
    mu_s = 0.2
    
    # 1. 输入原始数据
    # (d)问：每年积累应变率对应的应力率 (Pa/yr)
    t11_yr = 9196.20
    t22_yr = 1192.05
    t12_yr = 330.75
    
    # (b)问：Landers 同震应力变化 (Pa)
    t11_L = 3294
    t22_L = 81351
    t12_L = -45643.5
    
    # 计算 1000 年积累的总应力张量
    t11_1000 = t11_yr * 1000
    t22_1000 = t22_yr * 1000
    t12_1000 = t12_yr * 1000
    
    # 计算 1000年 + Landers 叠加后的总应力张量
    t11_total = t11_1000 + t11_L
    t22_total = t22_1000 + t22_L
    t12_total = t12_1000 + t12_L
    
    results = []
    
    for phi_deg in range(0, 180, 10):
        phi = np.radians(phi_deg)
        
        # --- 步骤 A: 计算长期年累积 CFF_a ---
        tau_n_a = (t11_yr + t22_yr)/2 + ((t11_yr - t22_yr)/2)*np.cos(2*phi) - t12_yr*np.sin(2*phi)
        tau_s_a = ((t11_yr - t22_yr)/2)*np.sin(2*phi) + t12_yr*np.cos(2*phi)
        cff_a = abs(tau_s_a) + mu_s * tau_n_a
        
        # --- 步骤 B: 计算千年底态 CFF_1000 ---
        tau_n_1000 = (t11_1000 + t22_1000)/2 + ((t11_1000 - t22_1000)/2)*np.cos(2*phi) - t12_1000*np.sin(2*phi)
        tau_s_1000 = ((t11_1000 - t22_1000)/2)*np.sin(2*phi) + t12_1000*np.cos(2*phi)
        cff_1000 = abs(tau_s_1000) + mu_s * tau_n_1000
        
        # 顺便算出单纯的 Landers 剪应力，用于验证符号规律
        tau_s_L = ((t11_L - t22_L)/2)*np.sin(2*phi) + t12_L*np.cos(2*phi)
        
        # --- 步骤 C: 计算叠加后的终态 CFF_1000+L (注意绝对值的非线性!) ---
        tau_n_total = (t11_total + t22_total)/2 + ((t11_total - t22_total)/2)*np.cos(2*phi) - t12_total*np.sin(2*phi)
        tau_s_total = ((t11_total - t22_total)/2)*np.sin(2*phi) + t12_total*np.cos(2*phi)
        cff_1000_L = abs(tau_s_total) + mu_s * tau_n_total
        
        # --- 步骤 D: 计算最终的时间提前/推迟 Delta t ---
        delta_cff_jump = cff_1000_L - cff_1000
        delta_t = delta_cff_jump / cff_a
        
        # 判断符号是否一致
        sign_match = "Yes" if (np.sign(tau_s_1000) == np.sign(tau_s_L)) else "No"
        
        results.append({
            'Azimuth (deg)': phi_deg,
            'tau_s_1000 (Pa)': round(tau_s_1000, 1),
            'tau_s_L (Pa)': round(tau_s_L, 1),
            'Sign Match': sign_match,
            'CFF_a (Pa/yr)': round(cff_a, 1),
            'CFF_jump (Pa)': round(delta_cff_jump, 1),
            'Delta t (years)': round(delta_t, 2)
        })
        
    df = pd.DataFrame(results)
    return df

if __name__ == "__main__":
    df_time = compute_delta_t_table()

    print("----------------------------------------------------------------------------------")
    print(df_time.to_string(index=False))