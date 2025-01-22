import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.special import gamma

num_samples = 100
alpha = 2
beta = 2

def calc_beta(x, alpha=alpha, beta=beta):
    
    y = gamma(alpha+beta)/(gamma(alpha)*gamma(beta)) * x ** (alpha-1) * (1 - x) ** (beta - 1)
    return y

def main():
    global mu, sigma

    points = np.linspace(0, 1, num_samples)

    y = calc_beta(points, alpha, beta)

    fig = plt.subplot(1, 1, 1)

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
