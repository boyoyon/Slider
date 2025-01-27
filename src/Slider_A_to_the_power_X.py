import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

div = 1000      # -1～1の範囲の分割数
step = 2 / div # -1～1の範囲を1000分割
a = 2              # 底のデフォルト値

def updateY(x):
    global a
    y = a ** x
    return y

def updateDy(y):
    global step
    numPoints = len(y)
    dy = np.zeros((numPoints), np.float32)
    for i in range(1, numPoints - 1):
        dy[i] = (y[i+1] - y[i-1]) / (2 * step) 
    
    dy[0] = dy[1]
    dy[-1] = dy[-2]
    return dy

def main():
    global div
    plt.axes([0.1, 0.1, 0.8, 0.8])
 
    x = np.linspace(-1, 1, div)
    
    y = updateY(x)
    plt_y, = plt.plot(x, y, color = 'blue', label='y = a ** x')
    dy = updateDy(y)
    plt_dy, = plt.plot(x, dy, color='red', label='dy/dx')
    plt.title('a ** x')
    plt.legend()

    # Sliderの位置設定
    ax_a = plt.axes([0.1, 0.01, 0.8, 0.03])

    # Sliderオブジェクトのインスタンスの作成
    slider_a = Slider(ax_a, 'a', 0.01, 4, 2)

    def update_a(slider_val):
        global a
        a = slider_val
        y = updateY(x)
        dy = updateDy(y)
        plt_y.set_ydata(y)
        plt_dy.set_ydata(dy)

    # Slider値変更時の処理の呼び出し
    slider_a.on_changed(update_a)

    plt.show()
 
if __name__ == '__main__':
    main()