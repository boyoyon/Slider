import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

num_samples = 100
mu = 0.0
sigma = 1.0
slider_mu = None
slider_sigma = None

def on_key(event):
    current_mu = slider_mu.val
    current_sigma  = slider_sigma.val

    if event.key == 'right':
        delta = np.ceil(current_mu * 10) / 10 - current_mu
        if delta == 0:
            slider_mu.set_val(current_mu + 0.1)
        else:
            slider_mu.set_val(current_mu + delta)

    elif event.key == 'left':
        delta = current_mu - np.floor(current_mu * 10) / 10
        if delta == 0:
            slider_mu.set_val(current_mu - 0.1)
        else:
            slider_mu.set_val(current_mu - delta)
    
    elif event.key == 'up':
        delta = np.ceil(current_sigma * 10) / 10 - current_sigma
        if delta == 0:
            slider_sigma.set_val(current_sigma + 0.1)
        else:
            slider_sigma.set_val(current_sigma + delta)
    
    elif event.key == 'down':
        delta = current_sigma - np.floor(current_sigma * 10) / 10
        if delta == 0:
            slider_sigma.set_val(current_sigma - 0.1)
        else:
            slider_sigma.set_val(current_sigma - delta)

def calc_coeff(mu, sigma):

    a =  1 / (np.sqrt(2 * np.pi) * sigma)
    b = -1 / (2 * sigma ** 2)

    return a, b

def normal(x, mu=0, sigma=1):
    a, b = calc_coeff(mu, sigma)
    y = a * np.exp(b * (x - mu)**2)
    return y

def main():
    global mu, sigma, slider_mu, slider_sigma

    print('Hit q-key to terminate')
    print('Slide the lever or hit arrow-key to change parameter')

    points = np.linspace(-5, 5, num_samples)

    y = normal(points, mu, sigma)

    fig, ax = plt.subplots()

    fig.canvas.mpl_connect('key_press_event', on_key)
    
    # 下にスライダーを配置したいので、グラフを上に移動する
    plt.subplots_adjust(bottom=0.3)
    
    plt.title('Normal Distribution')
    plt_normal, = plt.plot(points, y)
    plt.ylim(0, 1.0)

    # Sliderの位置設定
    ax_mu = plt.axes([0.15, 0.09, 0.75, 0.06])
    ax_sigma = plt.axes([0.15, 0.03, 0.75, 0.06])

    # Sliderオブジェクトのインスタンスの作成
    slider_mu = Slider(ax_mu, 'mu', -5.0, 5.0, valinit=0.0)
    slider_sigma = Slider(ax_sigma, 'sigma', 0.1, 10, valinit=1)

    def updatePlot():
        global mu, sigma
        y = normal(points, mu, sigma)
        plt_normal.set_ydata(y)

    def update_mu(slider_val):
        global mu
        mu = slider_val
        updatePlot()

    def update_sigma(slider_val):
        global sigma
        sigma = slider_val
        updatePlot()

    # Slider値変更時の処理の呼び出し
    slider_mu.on_changed(update_mu)
    slider_sigma.on_changed(update_sigma)

    plt.show()

if __name__ == '__main__':
    main()
