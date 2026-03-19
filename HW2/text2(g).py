import numpy as np
import pandas as pd

def compute_yearly_cff_table():
    # 1. 已知参数设定
    mu_s = 0.2  # 静摩擦系数
    
    # 2. 从(d)问直接输入每年积累的应力张量 (单位：Pa/yr)
    t11_yr = 9196.20
    t22_yr = 1192.05
    t12_yr = 330.75
    
    results = []
    
    # 3. 按照 10 度间隔遍历方位角
    for phi_deg in range(0, 180, 10):
        phi = np.radians(phi_deg)
        
        # 计算该面上的正应力变化和剪应力变化
        delta_tau_n = (t11_yr + t22_yr)/2 + ((t11_yr - t22_yr)/2)*np.cos(2*phi) - t12_yr*np.sin(2*phi)
        delta_tau_s = ((t11_yr - t22_yr)/2)*np.sin(2*phi) + t12_yr*np.cos(2*phi)
        
        # 计算库仑破裂函数变化: dCFF = d|tau_s| + mu_s * dtau_n
        delta_cff = abs(delta_tau_s) + mu_s * delta_tau_n
        
        results.append({
            'Azimuth (deg)': phi_deg,
            'Delta Normal Stress (Pa/yr)': round(delta_tau_n, 1),
            'Delta Shear Stress (Pa/yr)': round(delta_tau_s, 1),
            'Delta CFF (Pa/yr)': round(delta_cff, 1)
        })
        
    df = pd.DataFrame(results)
    return df

if __name__ == "__main__":
    df_cff = compute_yearly_cff_table()
    print("Yearly change in Coulomb Failure Function (CFF):")
    print(df_cff.to_markdown(index=False))