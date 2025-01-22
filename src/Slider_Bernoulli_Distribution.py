import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

num_samples = 100
_lambda = 0.5

def bernoulli(x, _lambda = 0.1):

    y = _lambda ** x * (1 - _lambda) ** (1-x)
    return y

def main():
    global _lambda

    points = np.linspace(0, 1, num_samples)

    y = bernoulli(points, _lambda)

    fig = plt.subplot(1, 1, 1)

    # 下にスライダーを配置したいので、グラフを上に移動する
    plt.subplots_adjust(bottom=0.3)
    
    plt.title('Bernoulli Distribution')
    plt_bernoulli, = plt.plot(points, y)
    plt.ylim(0, 1)

    # Sliderの位置設定
    ax_lambda = plt.axes([0.15, 0.09, 0.75, 0.06])

    # Sliderオブジェクトのインスタンスの作成
    slider_lambda = Slider(ax_lambda, 'lambda', 0.0, 1.0, valinit=_lambda)

    def updatePlot():
        y = bernoulli(points, _lambda)
        plt_bernoulli.set_ydata(y)
        
        label = 'lambda:%.1f' % _lambda

    def update_lambda(slider_val=_lambda):
        global _lambda
        _lambda = slider_val
        updatePlot()

    # Slider値変更時の処理の呼び出し
    slider_lambda.on_changed(update_lambda)

    plt.show()

if __name__ == '__main__':
    main()
