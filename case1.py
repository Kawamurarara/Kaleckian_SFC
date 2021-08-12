#大野隆、西洋 著(2011)「カレツキアン・モデルの新しい展開––––ストック・フロー・コンシステント・モデル」、季刊経済理論、第47巻第4号、p.6-18をモデル化した
##パラメータ
#利潤分配率に関するパラメータ
α = 0.2
#稼働率に関するパラメータ
β = 0.1
#税率
θ = 0.25
#企業の資本蓄積率における定数項
g_0 = 0.02
#貸出利子率に関するパラメータ
θ_1 = 0.2
#実質資本ストックに対する政府支出の割合
γ = 0.22
#保有資産のうち株式として保有する割合
δ = 0.3
#利潤分配率
π = 0.28
#利潤の配当割合
μ = 0.75
#総資産の消費割合
a = 0.03
#貸出利子率
i_l = 4/300
#国債利子率
i_b = 0.01
#マークアップ率
τ_b = 1/3

##長期均衡値
#成長率
g_t = [0.1600]
#稼働率
u_t = [0.8667]
#実質資本ストックに対する国債の割合
b_t = [0.0222]
#実質資本ストックに対する家計の保有資産の割合
v_t = [0.6223]

import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語を有効化するモジュールをインポート
plt.rcParams['xtick.direction'] = 'in' #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in' #y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.major.width'] = 1 #x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1 #y軸主目盛り線の線幅
plt.rcParams['font.size'] = 10.5 #フォントの大きさ
plt.rcParams['axes.linewidth'] = 1 # 軸の線幅edge linewidth。囲みの太さ

def model(α, β, θ, g_0, θ_1, γ, δ, π, a, i_l, i_b, τ_b, t):
    
    φ = 1/(1 - (1 - π) * (1 - θ) - β)
    ut = φ * (g_0 - θ_1 * i_l + α * π + γ) + φ * a * v_t[-1]
    u_t.append(ut)
    
    gt = g_0 + α * π + β * ut - θ_1 * i_l
    g_t.append(gt)
    
    bt = (b_t[-1] + i_b * b_t[-1] + γ - θ * u_t[-1])/(1 + g_t[-1])
    b_t.append(bt)
    
    vt = 1/(1 + g_t[-1] - δ) * ((1 - δ) * i_b * (1 - τ_b) * (1 - μ) - a + 1 - δ) * v_t[-1] + ((1 - (1 + τ_b) * (1 - μ)) * i_b * bt + μ * (1 - θ) * π * ut)
    v_t.append(vt)

Time = [i for i in range(0, 16)]
for t in range(1,16):
    if t < 5:
        model(α, β, θ, g_0, θ_1, γ, δ, π, a, i_l, i_b, τ_b, t)
    else:
        π = 0.3
        model(α, β, θ, g_0, θ_1, γ, δ, π, a, i_l, i_b, τ_b, t)

fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1,1,1)
ax2 = ax1.twinx()
line1 = ax1.plot(Time, g_t, 'C0', label = "成長率")
line2 = ax2.plot(Time, u_t, 'C1', linestyle="dashed", label = "稼働率")

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()

ax1.set_title("利潤配分率の上昇")
ax1.set_xlabel("期")
ax1.set_ylabel("成\n長\n率", rotation=0, va='center')
ax2.set_ylabel("稼\n働\n率", rotation=0, va='center')
ax1.set_xlim(0,16)
ax1.legend(h1+h2, l1+l2, loc='lower right')
plt.show()

