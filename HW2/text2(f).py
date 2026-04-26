import numpy as np
import pandas as pd

def compute_fault_stresses(t11, t22, t12):
    results = []
    # 按照 10 度为间隔计算 (0 到 170 度)
    for phi_deg in range(0, 180, 10):
        phi = np.radians(phi_deg)
        
        # 应用张量坐标变换推导公式
        sigma_n = (t11 + t22)/2 + ((t11 - t22)/2)*np.cos(2*phi) - t12*np.sin(2*phi)
        tau_s = ((t11 - t22)/2)*np.sin(2*phi) + t12*np.cos(2*phi)
        
        results.append({
            'Azimuth (deg)': phi_deg,
            'Normal Stress (Pa)': round(sigma_n, 1),
            'Shear Stress (Pa)': round(tau_s, 1),
            'Abs Shear Stress': abs(tau_s)
        })
        
    df = pd.DataFrame(results)
    
    # 寻找最大绝对剪应力对应的方位角
    max_idx = df['Abs Shear Stress'].idxmax()
    best_azimuth = df.loc[max_idx, 'Azimuth (deg)']
    
    # 移除辅助列以获得干净的输出表格
    df_clean = df.drop(columns=['Abs Shear Stress'])
    
    return df_clean, best_azimuth

if __name__ == "__main__":
    
    # ==========================================
    # 情景 (b): Landers 地震同震应力变化数据
    # ==========================================
    t11_b = 3294
    t22_b = 81351
    t12_b = -45643.5
    
    df_b, max_az_b = compute_fault_stresses(t11_b, t22_b, t12_b)
    
    print("--------------------------------------------------")
    print(" CASE B: Landers Earthquake Co-seismic Stress")
    print("--------------------------------------------------")
    print(df_b.to_string(index=False))
    print(f"\n>> Maximum absolute shear stress occurs at Azimuth: {max_az_b} degrees.\n")
    
    # 将表格导出为 CSV 文件
    df_b.to_csv("data/case_b_landers_stress.csv", index=False)
    print("-> Table exported to 'data/case_b_landers_stress.csv'")
    
    
    # ==========================================
    # 情景 (d): 1000 年长期累积应力变化数据
    # ==========================================
    t11_d = 9196200
    t22_d = 1192050
    t12_d = 330750
    
    df_d, max_az_d = compute_fault_stresses(t11_d, t22_d, t12_d)
    
    print("\n--------------------------------------------------")
    print(" CASE D: 1000-Year Steady Strain Accumulation")
    print("--------------------------------------------------")
    print(df_d.to_string(index=False))
    print(f"\n>> Maximum absolute shear stress occurs at Azimuth: {max_az_d} degrees.\n")
    
    # 将表格导出为 CSV 文件
    df_d.to_csv("data/case_d_1000yr_stress.csv", index=False)
    print("-> Table exported to 'data/case_d_1000yr_stress.csv'")
    print("--------------------------------------------------")