import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

num_samples = 100
shift = 0.0
scale = 1

def gauss(x, a = 1, mu = 0, sigma = 1):
    return a * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))

def main():
    global num_samples, shift, scale

    points = np.linspace(0, 1, num_samples)

    pos = gauss(points, 1, 0.5 + shift, 0.1)
    neg = gauss(points, scale, 0.5 - shift, 0.1)

    fig = plt.subplot(2, 1, 1)

    # 下にスライダーを配置したいので、グラフを上に移動する
    plt.subplots_adjust(bottom=0.3)

    plt_pos, = plt.plot(points, pos, color = 'red', alpha = 0.5, label = 'POS')
    plt_neg, = plt.plot(points, neg, color = 'blue', alpha = 0.5, label = 'NEG')
    plt.legend()

    true_rate = np.zeros((num_samples), np.float32)
    false_rate = np.zeros((num_samples), np.float32)

    for i in reversed(range(num_samples)):
        true_rate[i] = np.sum(pos[i:num_samples]) / np.sum(pos)
        false_rate[i] = np.sum(neg[i:num_samples]) / np.sum(neg)

    plt.subplot(2, 1, 2)
    plt.ylim(0.0, 1.0)
    plt_roc, = plt.plot(false_rate, true_rate, color = 'black', label = 'auc:')
    plt_roc2, = plt.plot(false_rate, true_rate, color = 'black', alpha = 0)
    legend = plt.legend()

    # Sliderの位置設定
    ax_sep = plt.axes([0.15, 0.09, 0.75, 0.06])
    ax_scale = plt.axes([0.15, 0.03, 0.75, 0.06])
    
    # Sliderオブジェクトのインスタンスの作成
    separation_slider = Slider(ax_sep, 'separation', -1, 1, valinit=shift)
    scale_slider = Slider(ax_scale, 'NEG scale', 0.1, 10, valinit=scale)

    def updatePlot():
        global shit, scale
        fig = plt.subplot(2, 1, 1)
        plt.ylim(0,max(1.0, scale))
        pos = gauss(points, 1, 0.5 + shift, 0.1)
        plt_pos.set_ydata(pos)
        neg = gauss(points, scale, 0.5 - shift, 0.1)
        plt_neg.set_ydata(neg)

        for i in reversed(range(num_samples)):
            true_rate[i] = np.sum(pos[i:num_samples]) / np.sum(pos)
            false_rate[i] = np.sum(neg[i:num_samples]) / np.sum(neg)

        auc = 0
        auc2 = 0

        for i in range(1, num_samples):
            auc += (true_rate[i-1] + true_rate[i] ) * (false_rate[i-1] - false_rate[i]) / 2
            auc2 += (false_rate[i-1] + false_rate[i] ) * (true_rate[i-1] - true_rate[i]) / 2

        if shift >= 0:

            plt_roc.set_xdata(false_rate)
            plt_roc.set_ydata(true_rate)
            plt_roc.set_linestyle('-')
            plt_roc2.set_alpha(0)

            label = 'auc:%1.5f' % auc

        else: # sliderの設定がマイナスの場合はPOSとNEGを入れ替えたROCを描画

            plt_roc.set_xdata(false_rate)
            plt_roc.set_ydata(true_rate)
            plt_roc.set_linestyle('-')

            plt_roc2.set_xdata(true_rate)
            plt_roc2.set_ydata(false_rate)
            plt_roc2.set_linestyle('--')
            plt_roc2.set_alpha(1)

            label = 'auc:%1.5f(%1.5f)' % (auc, auc2)

        legend.get_texts()[0].set_text(label)

    def separation_update(slider_val=shift):
        global shift
        shift = slider_val
        updatePlot()

    def scale_update(slider_val=scale):
        global scale
        scale = slider_val
        updatePlot()

    # Slider値変更時の処理の呼び出し
    separation_slider.on_changed(separation_update)
    scale_slider.on_changed(scale_update)

    plt.show()

if __name__ == '__main__':
    main()
