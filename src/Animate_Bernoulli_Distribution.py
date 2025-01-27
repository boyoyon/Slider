""" 
Bernoulli Distribution を表示する

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

STEP = 0.1

fig = plt.figure()
plots = []

for _lambda in np.arange(0.1, 1.0, 0.01):

    x = np.arange(0, 1+STEP, STEP)
    y = _lambda ** x * (1 - _lambda) ** (1-x)

    #label = 'lambda=%.2f' % lambda_list[i]
    plots.append(plt.plot(x, y, color = 'blue'))


ani = animation.ArtistAnimation(fig, plots, interval=100)
#plt.legend()
plt.show() 
