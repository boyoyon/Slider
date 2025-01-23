import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.special import gamma

num_samples = 100
alpha = 2
beta = 2

slider_alpha = None
slider_beta = None

def on_key(event):
    current_alpha = slider_alpha.val
    current_beta  = slider_beta.val

    if event.key == 'right':
        delta = np.ceil(current_alpha * 10) / 10 - current_alpha
        if delta == 0:
            slider_alpha.set_val(current_alpha + 0.1)
        else:
            slider_alpha.set_val(current_alpha + delta)

    elif event.key == 'left':
        delta = current_alpha - np.floor(current_alpha * 10) / 10
        if delta == 0:
            slider_alpha.set_val(current_alpha - 0.1)
        else:
            slider_alpha.set_val(current_alpha - delta)
    
    elif event.key == 'up':
        delta = np.ceil(current_beta * 10) / 10 - current_beta
        if delta == 0:
            slider_beta.set_val(current_beta + 0.1)
        else:
            slider_beta.set_val(current_beta + delta)
    
    elif event.key == 'down':
        delta = current_beta - np.floor(current_beta * 10) / 10
        if delta == 0:
            slider_beta.set_val(current_beta - 0.1)
        else:
            slider_beta.set_val(current_beta - delta)

def calc_beta(x, alpha=alpha, beta=beta):
    
    y = gamma(alpha+beta)/(gamma(alpha)*gamma(beta)) * x ** (alpha-1) * (1 - x) ** (beta - 1)
    return y

def main():
    global mu, sigma, slider_alpha, slider_beta

    print('Hit q-key to terminate')
    print('Slide the lever or hit arrow-key to change parameter')
    
    points = np.linspace(0, 1, num_samples)

    y = calc_beta(points, alpha, beta)

    fig, ax = plt.subplots()

    fig.canvas.mpl_connect('key_press_event', on_key)

    # 下にスライダーを配置したいので、グラフを上に移動する
    plt.subplots_adjust(bottom=0.3)
    
    plt.title('Beta Distribution')
    plt_beta, = plt.plot(points, y)
    plt.ylim(0, 10)

    # Sliderの位置設定
    ax_alpha = plt.axes([0.15, 0.09, 0.75, 0.06])
    ax_beta = plt.axes([0.15, 0.03, 0.75, 0.06])

    # Sliderオブジェクトのインスタンスの作成
    slider_alpha = Slider(ax_alpha, 'alpha', 1, 10, valinit=alpha)
    slider_beta = Slider(ax_beta, 'beta', 1,10, valinit=beta)

    def updatePlot():
        y = calc_beta(points, alpha, beta)
        plt_beta.set_ydata(y)

        label = 'alpha:%.1f, beta:%.1f' % (alpha, beta)

    def update_alpha(slider_val=alpha):
        global alpha
        alpha = slider_val
        updatePlot()

    def update_beta(slider_val=beta):
        global beta
        beta = slider_val
        updatePlot()

    # Slider値変更時の処理の呼び出し
    slider_alpha.on_changed(update_alpha)
    slider_beta.on_changed(update_beta)

    plt.show()

if __name__ == '__main__':
    main()
