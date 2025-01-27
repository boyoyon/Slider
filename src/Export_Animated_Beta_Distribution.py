import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
import matplotlib.animation as animation
import os

STEP = 0.01

fig = plt.figure()
plots = []

no = 1

plt.yticks(color='None')

plt.tight_layout()
plt.ylim(0, 16)

folder_no = 1
folder_name = '%d' % folder_no
while os.path.exists(folder_name):
    folder_no += 1
    folder_name = '%d' % folder_no

os.mkdir(folder_name)

for alpha in np.arange(0.6, 10, 0.6):

    #beta = alpha
    beta = 10 - alpha

    x = np.arange(STEP, 1, STEP)
    y = gamma(alpha+beta)/(gamma(alpha)*gamma(beta)) * x ** (alpha-1) * (1 - x) ** (beta - 1)

    #label = 'alpha:%.1f, beta:%.1f' % (alpha, beta)
    plt.plot(x, y, color = 'blue')
    plt.fill_between(x, 0, y, alpha = 0.2, color = 'blue')

    dst_path = os.path.join(folder_name, '%04d.png' % no)
    plt.savefig(dst_path)
    print('save %s' % dst_path)
    no += 1

    plt.clf()
    plt.tight_layout()
    plt.ylim(0, 16)
    plt.yticks(color='None')

for alpha in np.arange(10 - 0.6, 0.6, -0.6):

    #beta = alpha
    beta = 10 - alpha

    x = np.arange(STEP, 1, STEP)
    y = gamma(alpha+beta)/(gamma(alpha)*gamma(beta)) * x ** (alpha-1) * (1 - x) ** (beta - 1)

    #label = 'alpha:%.1f, beta:%.1f' % (alpha, beta)
    plt.plot(x, y, color = 'blue')
    plt.fill_between(x, 0, y, alpha = 0.2, color = 'blue')

    dst_path = os.path.join(folder_name, '%04d.png' % no)

    plt.savefig(dst_path)
    print('save %s' % dst_path)
    no += 1

    plt.clf()
    plt.tight_layout()
    plt.ylim(0, 16)
    plt.yticks(color='None')

