import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
import matplotlib.animation as animation

STEP = 0.01

fig = plt.figure()
plots = []

for alpha in np.arange(0.3, 10, 0.3):

    #beta = alpha
    beta = 10 - alpha

    x = np.arange(STEP, 1, STEP)
    y = gamma(alpha+beta)/(gamma(alpha)*gamma(beta)) * x ** (alpha-1) * (1 - x) ** (beta - 1)

    #label = 'alpha:%.1f, beta:%.1f' % (alpha, beta)
    plots.append(plt.plot(x, y, color = 'blue'))

ani = animation.ArtistAnimation(fig, plots, interval=100)
#plt.legend()
plt.show() 
