<style>
@media print {
    thead {
        display: table-row-group !important;
    }
}
</style>

# Homework2

**231830104 杜鑫宇**

### 第一题

#### (1)求断层面上的正应力和剪应力

已知二维应力张量为：
$$ \boldsymbol{\sigma} = \begin{pmatrix} \sigma_x & \tau_{xy} \\ \tau_{yx} & \sigma_y \end{pmatrix} = \begin{pmatrix} -40 & -10 \\ -10 & -60 \end{pmatrix} \text{ MPa} $$

根据题意图示，设断层面的倾角为 $\theta$。我们先定义断层面上的法向单位向量 $\mathbf{n}$ 和切向单位向量 $\mathbf{\hat{f}}$。
*   断层面的法向量 $\mathbf{n}$ 指向右上方，其与 $x$ 轴正方向的夹角为 $90^\circ - \theta$。因此：
    $$ \mathbf{n} = \begin{pmatrix} \cos(90^\circ - \theta) \\ \sin(90^\circ - \theta) \end{pmatrix} = \begin{pmatrix} \sin\theta \\ \cos\theta \end{pmatrix} $$
*   断层面的切向向量 $\mathbf{\hat{f}}$ 指向右下方，与 $x$ 轴正方向夹角为 $-\theta$。因此：
    $$ \mathbf{\hat{f}} = \begin{pmatrix} \cos(-\theta) \\ \sin(-\theta) \end{pmatrix} = \begin{pmatrix} \cos\theta \\ -\sin\theta \end{pmatrix} $$

##### 方法一：斜截面应力法

首先求出作用在断层面上的面力\mathbf{T}$：
$$ \mathbf{T} = \boldsymbol{\sigma} \mathbf{n} = \begin{pmatrix} -40 & -10 \\ -10 & -60 \end{pmatrix} \begin{pmatrix} \sin\theta \\ \cos\theta \end{pmatrix} = \begin{pmatrix} -40\sin\theta - 10\cos\theta \\ -10\sin\theta - 60\cos\theta \end{pmatrix} $$

正应力 $\sigma_N$ 是面力在法向 $\mathbf{n}$ 上的投影：
$$ \begin{aligned} \sigma_N &= \mathbf{T} \cdot \mathbf{n} = (-40\sin\theta - 10\cos\theta)\sin\theta + (-10\sin\theta - 60\cos\theta)\cos\theta \\ &= -40\sin^2\theta - 10\sin\theta\cos\theta - 10\sin\theta\cos\theta - 60\cos^2\theta \\ &= -40\sin^2\theta - 60\cos^2\theta - 20\sin\theta\cos\theta \end{aligned} $$
化简得：
$$ \sigma_N = -40\left(\frac{1-\cos 2\theta}{2}\right) - 60\left(\frac{1+\cos 2\theta}{2}\right) - 10\sin 2\theta $$
$$ \sigma_N = -50 - 10\cos 2\theta - 10\sin 2\theta \text{ (MPa)} $$

**剪应力 $\tau_S$** 是面力在切向 $\mathbf{\hat{f}}$ 上的投影：
$$ \begin{aligned} \tau_S &= \mathbf{T} \cdot \mathbf{\hat{f}} = (-40\sin\theta - 10\cos\theta)\cos\theta + (-10\sin\theta - 60\cos\theta)(-\sin\theta) \\ &= -40\sin\theta\cos\theta - 10\cos^2\theta + 10\sin^2\theta + 60\sin\theta\cos\theta \\ &= 20\sin\theta\cos\theta + 10(\sin^2\theta - \cos^2\theta) \end{aligned} $$
化简得：
$$ \tau_S = 10\sin 2\theta - 10\cos 2\theta \text{ (MPa)} $$

##### 方法二：坐标变换法

建立新的局部坐标系 $x'y'$，使得 $y'$ 轴与法向 $\mathbf{n}$ 一致，$x'$ 轴与切向 $\mathbf{\hat{f}}$ 一致。
坐标旋转矩阵 $Q$ 为：
$$ Q = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} $$
根据张量坐标变换公式 $\boldsymbol{\sigma}' = Q \boldsymbol{\sigma} Q^T$：
$$ \boldsymbol{\sigma}' = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} -40 & -10 \\ -10 & -60 \end{pmatrix} \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} $$
展开矩阵乘法后，求新坐标系下的正应力 $\sigma_{y'y'}$ 和剪应力 $\tau_{y'x'}$：
$$ \begin{pmatrix} \sigma_{x'x'} & \tau_{x'y'} \\ \tau_{y'x'} & \sigma_{y'y'} \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} -40\cos\theta + 10\sin\theta & -40\sin\theta - 10\cos\theta \\ -10\cos\theta + 60\sin\theta & -10\sin\theta - 60\cos\theta \end{pmatrix} $$
提取出断层面正应力 $\sigma_N = \sigma_{y'y'}$ 和剪应力 $\tau_S = \tau_{y'x'}$：
$$ \begin{aligned} \sigma_N &= \sigma_{y'y'} = \sin\theta(-40\sin\theta - 10\cos\theta) + \cos\theta(-10\sin\theta - 60\cos\theta) \\ &= -40\sin^2\theta - 60\cos^2\theta - 20\sin\theta\cos\theta = -50 - 10\cos 2\theta - 10\sin 2\theta \text{ (MPa)} \end{aligned} $$
$$ \begin{aligned} \tau_S &= \tau_{y'x'} = \sin\theta(-40\cos\theta + 10\sin\theta) + \cos\theta(-10\cos\theta + 60\sin\theta) \\ &= 10\sin^2\theta - 10\cos^2\theta + 20\sin\theta\cos\theta = 10\sin 2\theta - 10\cos 2\theta \text{ (MPa)} \end{aligned} $$

##### 编程画图展示

按照5度为间隔计算并绘制应力随倾角 $\theta$ 变化的图像：

![Figure_1](C:\Users\starfie1d\Documents\我的文件\行星固体物理\Homework2\Figure_1.png)

---

#### (2) 求主应力及其对应方向

主应力 $\lambda$ 满足特征方程：$|\boldsymbol{\sigma} - \lambda \mathbf{I}| = 0$，其中 $\mathbf{I}$ 是单位矩阵。
$$ \begin{vmatrix} -40 - \lambda & -10 \\ -10 & -60 - \lambda \end{vmatrix} = 0 $$

展开行列式，得到特征多项式：
$$ (-40 - \lambda)(-60 - \lambda) - (-10 \times -10) = 0 $$
$$ \lambda^2 + 100\lambda + 2300 = 0 $$

使用求根公式求解 $\lambda$：
$$ \lambda = \frac{-100 \pm \sqrt{100^2 - 4 \times 1 \times 2300}}{2} = \frac{-100 \pm 20\sqrt{2}}{2} = -50 \pm 10\sqrt{2} $$

两个主应力为：
*   **最小主应力：$\sigma_1 = \lambda_1 = -50 + 10\sqrt{2} \approx -35.86 \text{ MPa}$**
*   **最大主应力：$\sigma_2 = \lambda_2 = -50 - 10\sqrt{2} \approx -64.14 \text{ MPa}$**

将求得的特征值代回方程 $(\boldsymbol{\sigma} - \lambda \mathbf{I})\mathbf{v} = 0$，求解对应的特征向量 $\mathbf{v} = \begin{pmatrix} v_x \\ v_y \end{pmatrix}$。

**1. 对应于最小主应力 $\sigma_1 = -50 + 10\sqrt{2}$ 的方向：**
$$ \begin{pmatrix} -40 - (-50 + 10\sqrt{2}) & -10 \\ -10 & -60 - (-50 + 10\sqrt{2}) \end{pmatrix} \begin{pmatrix} v_x \\ v_y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$
$$ \begin{pmatrix} 10 - 10\sqrt{2} & -10 \\ -10 & -10 - 10\sqrt{2} \end{pmatrix} \begin{pmatrix} v_x \\ v_y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

取矩阵的第一行，得到方程：
$$ (10 - 10\sqrt{2})v_x - 10v_y = 0 $$
$$ (1 - \sqrt{2})v_x = v_y $$
所以特征向量可以表示为 $\mathbf{v_1} = \begin{pmatrix} 1 \\ 1-\sqrt{2} \end{pmatrix}$。
该向量与 $x$ 轴的夹角 $\alpha_1$ 为：
$$ \tan\alpha_1 = \frac{v_y}{v_x} = 1 - \sqrt{2} \approx -0.414 $$
$$ \alpha_1 = \arctan(1 - \sqrt{2}) = -22.5^\circ $$
(即 $x$ 轴顺时针旋转 $22.5^\circ$ 的方向)

**2. 对应于最大主应力 $\sigma_2 = -50 - 10\sqrt{2}$ 的方向：**
$$ \begin{pmatrix} -40 - (-50 - 10\sqrt{2}) & -10 \\ -10 & -60 - (-50 - 10\sqrt{2}) \end{pmatrix} \begin{pmatrix} v_x \\ v_y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

$$ \begin{pmatrix} 10 + 10\sqrt{2} & -10 \\ -10 & -10 + 10\sqrt{2} \end{pmatrix} \begin{pmatrix} v_x \\ v_y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$

取第一行方程：
$$ (10 + 10\sqrt{2})v_x - 10v_y = 0 \implies (1 + \sqrt{2})v_x = v_y $$
所以特征向量可以表示为 $\mathbf{v_2} = \begin{pmatrix} 1 \\ 1+\sqrt{2} \end{pmatrix}$。
该向量与 $x$ 轴的夹角 $\alpha_2$ 为：
$$ \tan\alpha_2 = \frac{v_y}{v_x} = 1 + \sqrt{2} \approx 2.414 $$
$$ \alpha_2 = \arctan(1 + \sqrt{2}) = 67.5^\circ $$
(即 $x$ 轴逆时针旋转 $67.5^\circ$ 的方向)

---

#### (3) 求最大剪应力及其对应方向

最大剪应力为主应力差的一半：
$$ \tau_{max} = 10\sqrt{2} \approx 14.14 \text{ MPa} $$

最大剪应力面与主应力面呈 $45^\circ$ 夹角。其方向为：
$$ \alpha_\tau = \alpha_1 \pm 45^\circ = -22.5^\circ \pm 45^\circ $$
得到两个正交的面，角度分别为：
$$ \alpha_{\tau1} = 22.5^\circ, \quad \alpha_{\tau2} = -67.5^\circ $$

------

### 第二题

#### (a)计算拉梅参数

由S波速度公式 $\beta = \sqrt{\frac{\mu}{\rho}}$，两边平方并变形可得：
$$ \mu = \rho \beta^2 $$

代入得：
$$ \mu = (2.7 \times 10^3 \text{ kg/m}^3) \times (3.5 \times 10^3 \text{ m/s})^2 = 3.3075 \times 10^{10} \text{ Pa} $$

由P波速度公式 $\alpha = \sqrt{\frac{\lambda + 2\mu}{\rho}}$，两边平方并变形可得：
$$ \lambda + 2\mu = \rho \alpha^2 $$
$$ \lambda = \rho \alpha^2 - 2\mu $$
其中：

$$ \rho \alpha^2 = (2.7 \times 10^3 \text{ kg/m}^3) \times (6 \times 10^3 \text{ m/s})^2 = 9.72 \times 10^{10} \text{ Pa} $$

代入 $\mu$ 计算 $\lambda$：
$$ \lambda = 9.72 \times 10^{10} \text{ Pa} - 2 \times (33.075 \times 10^9 \text{ Pa}) = 3.105 \times 10^{10} \text{ Pa} $$

------

#### (b)计算应力

由广义胡克定律： $$ \tau_{ij} = \lambda \delta_{ij} e_{kk} + 2\mu e_{ij} $$

其中$$ e_{kk} = e_{11} + e_{22} = (-0.26 \times 10^{-6}) + (0.92 \times 10^{-6}) = 0.66 \times 10^{-6} $$

$$ \lambda e_{kk} = (3.105 \times 10^{10} \text{ Pa}) \times (0.66 \times 10^{-6})   = 2.0493 \times 10^4 \text{ Pa} $$  

$$ 2\mu = 2 \times 3.3075 \times 10^{10} \text{ Pa} = 6.615 \times 10^{10} \text{ Pa} $$

$$ \tau_{11} = \lambda e_{kk} + 2\mu e_{11} = 2.0493 \times 10^4 \text{ Pa} + (6.615 \times 10^{10} \text{ Pa}) \times (-0.26 \times 10^{-6}) = 3294 \text{ Pa} $$

$$ \tau_{22} = \lambda e_{kk} + 2\mu e_{22} = 2.0493 \times 10^4 \text{ Pa} + (6.615 \times 10^{10} \text{ Pa}) \times (0.92 \times 10^{-6}) = 81351 \text{ Pa} $$

$$ \tau_{12} = 2\mu e_{12} = (6.615 \times 10^{10} \text{ Pa}) \times (-0.69 \times 10^{-6}) = -45643.5 \text{ Pa} $$

------

#### (c)计算主应变轴方位角

设主应变轴与正东方向的逆时针夹角为 $\theta$，由剪应变$e'_{12} $为0得极值条件：
$$ \tan(2\theta) = \frac{2e_{12}}{e_{11} - e_{22}} $$

代入已知数据：
$$ 2e_{12} = 2 \times (-0.69 \times 10^{-6}) = -1.38 \times 10^{-6} $$
$$ e_{11} - e_{22} = (-0.26 \times 10^{-6}) - (0.92 \times 10^{-6}) = -1.18 \times 10^{-6} $$
$$ \tan(2\theta) = \frac{-1.38 \times 10^{-6}}{-1.18 \times 10^{-6}} \approx 1.1695 $$

由于分子与分母均为负， $2\theta$ 位于第三象限。由 $\arctan(1.1695) \approx 49.47^\circ$ 可得：
*   对应最小主应变（最大压缩）的角度：$2\theta_2 = 49.47^\circ \implies \theta_2 = 24.73^\circ$
*   对应最大主应变（最大拉伸）的角度：$2\theta_1 = 180^\circ + 49.47^\circ = 229.47^\circ \implies \theta_1 = 114.73^\circ$

转换为方位角：

*   最小主应变（最大压缩）轴方位角：$$ Az_{comp} = 90^\circ - 24.73^\circ = 65.27^\circ $$
*   最大主应变（最大拉伸）轴方位角：$$ Az_{ext} = 90^\circ - 114.73^\circ = -24.73^\circ \quad (\text{即 } 335.27^\circ) $$

------

#### (d)计算长期累积的应力张量

计算 1000 年积累的总应变：
$$ E_{ij} = e_{ij} \times 1000 $$
代入得：
$$ E_{11} = (0.101 \times 10^{-6}) \times 1000 = 101 \times 10^{-6} $$
$$ E_{22} = (-0.02 \times 10^{-6}) \times 1000 = -20 \times 10^{-6} $$
$$ E_{12} = (0.005 \times 10^{-6}) \times 1000 = 5 \times 10^{-6} $$

由广义胡克定律计算总应力变化： $$ \tau_{ij} = \lambda \delta_{ij} E_{kk} + 2\mu E_{ij} $$

其中总平面体应变：
$$ E_{kk} = E_{11} + E_{22} = (101 \times 10^{-6}) + (-20 \times 10^{-6}) = 81 \times 10^{-6} $$

公共项：
$$ \lambda E_{kk} = (3.105 \times 10^{10} \text{ Pa}) \times (81 \times 10^{-6}) = 2.51505 \times 10^6 \text{ Pa} $$  
$$ 2\mu = 6.615 \times 10^{10} \text{ Pa} $$

代入各分量计算最终应力：
$$ \tau_{11} = \lambda E_{kk} + 2\mu E_{11} = 2.51505 \times 10^6 \text{ Pa} + (6.615 \times 10^{10} \text{ Pa}) \times (101 \times 10^{-6}) = 9.1962 \times 10^6 \text{ Pa} $$

$$ \tau_{22} = \lambda E_{kk} + 2\mu E_{22} = 2.51505 \times 10^6 \text{ Pa} + (6.615 \times 10^{10} \text{ Pa}) \times (-20 \times 10^{-6}) = 1.19205 \times 10^6 \text{ Pa} $$

$$ \tau_{12} = 2\mu E_{12} = (6.615 \times 10^{10} \text{ Pa}) \times (5 \times 10^{-6}) = 3.3075 \times 10^5 \text{ Pa} $$

------

#### (e)Bob土地面积的变化

忽略二阶小量，地表土地面积的变化率可以近似等于水平方向正应变之和。面积变化量公式为：
$$ \frac{\Delta A}{A} = e_{11} + e_{22} \implies \Delta A = A(e_{11} + e_{22}) $$

每年长期累积导致的面积变化：
$$ \Delta A_{year} = 10^6 \text{ m}^2 \times (0.101 \times 10^{-6} - 0.02 \times 10^{-6}) = 0.081 \text{ m}^2 $$

 Landers 地震同震导致的面积变化：
$$ \Delta A_{EQ} = 10^6 \text{ m}^2 \times (-0.26 \times 10^{-6} + 0.92 \times 10^{-6}) = 0.66 \text{ m}^2 $$

即由于面应变为正，Bob每年获得的土地面积为 **$0.081 \text{ m}^2$**。

而因为 Landers 地震，Bob获得的土地面积为 $0.66 \text{ m}^2$。

------

#### (f) 计算断层面上的应力并寻找最大剪应力

设垂直断层的走向方位角为 $\phi$，则断层的走向单位向量为 $(\sin\phi, \cos\phi)$，其垂直法向单位向量可表示为 $(\cos\phi, -\sin\phi)$。

此时断层面上的正应力 $\sigma_n$ 和剪应力 $\tau_s$ 随方位角 $\phi$ 的关系式可化简为：
$$ \sigma_n = \frac{\tau_{11} + \tau_{22}}{2} + \frac{\tau_{11} - \tau_{22}}{2}\cos(2\phi) - \tau_{12}\sin(2\phi) $$
$$ \tau_s = \frac{\tau_{11} - \tau_{22}}{2}\sin(2\phi) + \tau_{12}\cos(2\phi) $$

编程得以下数据：

**Landers 地震同震应力变化**

| 断层走向 (deg) | 正应力 (Pa) | 剪应力 (Pa)  |
| :------------: | :---------: | :----------: |
|       0        |   3294.0    |   -45643.5   |
|       10       |   21258.7   |   -56239.4   |
|     **20**     | **41764.0** | **-60052.0** |
|       30       |   62336.7   |   -56621.4   |
|       40       |   80495.3   |   -46361.5   |
|       50       |   94049.8   |   -30509.7   |
|       60       |  101365.0   |   -10977.9   |
|       70       |  101559.0   |    9877.9    |
|       80       |   94608.3   |   29542.3    |
|       90       |   81351.0   |   45643.5    |
|      100       |   63386.3   |   56239.4    |
|    **110**     | **42881.0** | **60052.0**  |
|      120       |   22308.3   |   56621.4    |
|      130       |   4149.7    |   46361.5    |
|      140       |   -9404.8   |   30509.7    |
|      150       |  -16720.2   |   10977.9    |
|      160       |  -16914.1   |   -9877.9    |
|      170       |   -9963.3   |   -29542.3   |

**1000 年长期累积应力变化**

| 断层走向 (deg) |  正应力 (Pa)  |  剪应力 (Pa)   |
| :------------: | :-----------: | :------------: |
|       0        |   9196200.0   |    330750.0    |
|       10       |   8841720.5   |   1679589.6    |
|       20       |   8047285.4   |   2825852.1    |
|       30       |   6908722.0   |   3631267.3    |
|     **40**     | **5563345.8** | **3998705.5**  |
|       50       |   4173453.6   |   3883839.8    |
|       60       |   2906649.3   |   3300517.5    |
|       70       |   1915764.1   |   2319124.9    |
|       80       |   1320283.4   |   1057985.3    |
|       90       |   1192050.0   |   -330750.0    |
|      100       |   1546529.5   |   -1679589.6   |
|      110       |   2340964.6   |   -2825852.1   |
|      120       |   3479528.0   |   -3631267.3   |
|    **130**     | **4824904.2** | **-3998705.5** |
|      140       |   6214796.4   |   -3883839.8   |
|      150       |   7481600.7   |   -3300517.5   |
|      160       |   8472485.9   |   -2319124.9   |
|      170       |   9067966.6   |   -1057985.3   |

基于计算结果，对于 Landers 地震同震应力响应，剪应力绝对值最大出现在断层方位角为 **$20^\circ$** 和 **$110^\circ$** 时。对于1000 年长期累积应力，剪应力绝对值最大出现在断层方位角为 **$40^\circ$** 和 **$130^\circ$** 时。

------

#### (g) 计算CFF的年变化率

从 ( d ) 中，已知 PFO 每年的应变率为：
$$ e_{11\_yr} = 0.101 \times 10^{-6} $$
$$ e_{22\_yr} = -0.02 \times 10^{-6} $$
$$ e_{12\_yr} = 0.005 \times 10^{-6} $$

利用广义胡克定律（同 d），可求得每年积累的应力变化量 $\Delta\tau_{ij\_yr}$ 为：
*   $\Delta\tau_{11\_yr} = 9196.2 \text{ Pa/yr}$
*   $\Delta\tau_{22\_yr} = 1192.05 \text{ Pa/yr}$
*   $\Delta\tau_{12\_yr} = 330.75 \text{ Pa/yr}$

将年应力变化张量，代入 ( f ) 的斜截面应力旋转公式中，即可求出各个断层走向 $\phi$ 上的 $\Delta\tau_n$ 和 $\Delta\tau_s$。

编程计算得到由于长期应变积累导致的各方位角断层面上 $\Delta\text{CFF}$ 的年变化率：

| 走向方位角 (deg) | 年正应力变化 $\Delta\tau_n$ (Pa/yr) | 年剪应力变化 $\Delta\tau_s$ (Pa/yr) | **库仑破裂函数年变化 $\Delta\text{CFF}$ (Pa/yr)** |
| :--------------: | :---------------------------------: | :---------------------------------: | :-----------------------------------------------: |
|        0         |               9196.2                |                330.8                |                    **2170.0**                     |
|        10        |               8841.7                |               1679.6                |                    **3447.9**                     |
|        20        |               8047.3                |               2825.9                |                    **4435.3**                     |
|        30        |               6908.7                |               3631.3                |                    **5013.0**                     |
|      **40**      |               5563.3                |               3998.7                |                    **5111.4**                     |
|        50        |               4173.5                |               3883.8                |                    **4718.5**                     |
|        60        |               2906.6                |               3300.5                |                    **3881.9**                     |
|        70        |               1915.8                |               2319.1                |                    **2702.3**                     |
|        80        |               1320.3                |               1058.0                |                    **1322.0**                     |
|        90        |               1192.1                |               -330.8                |                     **569.2**                     |
|       100        |               1546.5                |               -1679.6               |                    **1988.9**                     |
|       110        |               2341.0                |               -2825.9               |                    **3294.0**                     |
|       120        |               3479.5                |               -3631.3               |                    **4327.2**                     |
|       130        |               4824.9                |               -3998.7               |                    **4963.7**                     |
|     **140**      |               6214.8                |               -3883.8               |                    **5126.8**                     |
|       150        |               7481.6                |               -3300.5               |                    **4796.8**                     |
|       160        |               8472.5                |               -2319.1               |                    **4013.6**                     |
|       170        |               9068.0                |               -1058.0               |                    **2871.6**                     |

从表中可以看出，在长期的应力积累下，方位角为 **$40^\circ$** 和 **$140^\circ$** 附近的断层，其库仑破裂函数 ($\Delta\text{CFF}$) 增加得最快（约为 $5120 \text{ Pa/yr}$）。这说明这些走向的断层面最容易积累足够的能量和滑动趋势，是最容易发生下一次地震破裂的危险面。

---
#### (h) 计算 Landers 地震对下一次地震时间的影响

将 (b) 的同震应力和 (d) 的千年累积应力代入，编程得以下结果：

| 断层方位角 (deg) | $\tau_{s\_1000}$ | $\tau_{s\_L}$ | $\text{CFF}_a$ (Pa/yr) | $\text{CFF}_{1000+L} - \text{CFF}_{1000}$ | **提前/推迟时间 $\Delta t$ (年)** |
| :--------------: | :--------------: | :-----------: | :--------------------: | :---------------------------------------: | :-------------------------------: |
|        0         |     330750.0     |   -45643.5    |         2170.0         |                 -44984.7                  |            **-20.73**             |
|        10        |    1679590.0     |   -56239.4    |         3447.9         |                 -51987.7                  |            **-15.08**             |
|        20        |    2825850.0     |   -60052.0    |         4435.3         |                 -51699.2                  |            **-11.66**             |
|        30        |    3631270.0     |   -56621.4    |         5013.0         |                 -44154.1                  |             **-8.81**             |
|        40        |    3998710.0     |   -46361.5    |         5111.4         |                 -30262.4                  |             **-5.92**             |
|        50        |    3883840.0     |   -30509.7    |         4718.5         |                 -11699.7                  |             **-2.48**             |
|        60        |    3300520.0     |   -10977.9    |         3881.9         |                  9295.1                   |             **+2.39**             |
|        70        |    2319120.0     |    9877.9     |         2702.3         |                  30189.7                  |            **+11.17**             |
|        80        |    1057990.0     |    29542.3    |         1322.0         |                  48464.0                  |            **+36.66**             |
|        90        |    -330750.0     |    45643.5    |         569.2          |                 -29373.3                  |            **-51.61**             |
|       100        |    -1679590.0    |    56239.4    |         1988.9         |                 -43562.1                  |            **-21.90**             |
|       110        |    -2825850.0    |    60052.0    |         3294.1         |                 -51475.8                  |            **-15.63**             |
|       120        |    -3631270.0    |    56621.4    |         4327.2         |                 -52159.8                  |            **-12.05**             |
|       130        |    -3998710.0    |    46361.5    |         4963.7         |                 -45531.5                  |             **-9.17**             |
|       140        |    -3883840.0    |    30509.7    |         5126.8         |                 -32390.6                  |             **-6.32**             |
|       150        |    -3300520.0    |    10977.9    |         4796.8         |                 -14322.0                  |             **-2.99**             |
|       160        |    -2319120.0    |    -9877.9    |         4013.6         |                  6495.1                   |             **+1.62**             |
|       170        |    -1057990.0    |   -29542.3    |         2871.6         |                  27549.7                  |             **+9.59**             |

分析表中结果可得，对于大部分走向的断层$\Delta t$ 为负，使下一次地震推迟；而对于**$60^\circ \sim 80^\circ$** 和 **$160^\circ \sim 170^\circ$** 附近的断层，$\Delta t$ 为正数，使下一次地震提前。

------

#### (i) 实际情况对CFF公式的验证

实际观测中，Landers 地震后 PFO 附近没有观测到地震活动增加，这正符合上一问中我们计算得到的结果，即我们预测此处大部分走向的断层，该地震的应力使下一次地震推迟。该实际观测结果说明该处主要断层走向落在刚刚计算出$\Delta t$ 为负的区间内。