"""
duty比により積分器出力のレベルが変わることを確認する

"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

duty = 15
tau = 50

# 入力パルス
def system_response(y, t):
    global duty, tau
    if t % 100 < duty:
        u = 1.0
    else:
        u = 0.0

    dydt = (-y + u)/tau
    return dydt

# 初期値
y0 = 0

t = np.arange(0, 1000, 0.01)
ut = np.zeros((t.shape), np.float32)
y = odeint(system_response, y0, t)

fig, ax = plt.subplots(figsize=(15, 3))
plt_y, = ax.plot(t, y, label='output', c='red')
plt_ut, = ax.plot(t, ut, label='input', c='blue', alpha = 0.3)

# 下にスライダーを配置したいので、グラフを上に移動する
plt.subplots_adjust(bottom=0.3)

plt_y.axes.set_ylim(0, 1.2)

# Sliderの位置設定
ax_duty = plt.axes([0.15, 0.09, 0.75, 0.06])
ax_tau = plt.axes([0.15, 0.03, 0.75, 0.06])

# Sliderオブジェクトのインスタンスの作成
slider_duty = Slider(ax_duty, 'duty', 1, 100, valinit=15)
slider_tau = Slider(ax_tau, 'tau', 1, 200, valinit=50)

ax.set_xlabel('t')
ax.set_ylabel('input, output')
ax.legend(loc='best')
ax.grid(ls=':')

def updatePlot():
    global duty, tau
    ut = np.zeros((t.shape), np.float32)
    ut[t % 100 < duty] = 1.0
    ut[t % 100 >= duty] = 0.0
    y = odeint(system_response, y0, t)

    plt_y.set_ydata(y)
    plt_ut.set_ydata(ut)

def update_duty(slider_val):
    global duty
    duty = slider_val
    updatePlot()

def update_tau(slider_val):
    global tau
    tau = slider_val
    updatePlot()

# Slider値変更時の処理の呼び出し
slider_duty.on_changed(update_duty)
slider_tau.on_changed(update_tau)

fig.show()
input('Hit any key to terminate')
