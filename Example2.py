#from sympy import symbols, expand, collect, integrate, Eq, solveset

import matplotlib.pyplot as plt

from Traditional_Mechanism import *
from Perturbation_Mechanism import *


def plt_exp_AL_Laplace(ep_list, fd, fd2, repeat_times):
    sensitivity = abs(fd - fd2)

    AL_lap = []
    for i in range(len(ep_list)):
        tmp = Laplace_AL(sensitivity, ep_list[i], fd, repeat_times)
        AL_lap.append(tmp)

    labels = '0.2', '0.3', '0.4', '0.5', '1', '1.2', '1.4', '1.6', '1.8', '2.0'

    plt.rcParams['axes.facecolor'] = 'whitesmoke'
    plt.ticklabel_format(style='plain', scilimits=(0, 0), axis='both')
    plt.boxplot(AL_lap, labels=labels, whis=3, showmeans=True, patch_artist=True,
                boxprops={'color': 'black', 'facecolor': 'skyblue'})
    plt.grid(true)
    plt.grid(color='w', linewidth=1)
    plt.xlabel("Privacy Budget")
    plt.ylabel("Accuracy Loss")
    plt.tight_layout()
    plt.show()


def plt_exp_AL_Gaussian(ep_list, fd, fd2, repeat_times):
    sensitivity = abs(fd - fd2)

    AL_Gau = []
    for i in range(len(ep_list)):
        tmp = Gaussian_AL(sensitivity, ep_list[i], fd, repeat_times)
        AL_Gau.append(tmp)

    labels = '0.2', '0.3', '0.4', '0.5', '1', '1.2', '1.4', '1.6', '1.8', '2.0'

    plt.rcParams['axes.facecolor'] = 'whitesmoke'
    plt.ticklabel_format(style='plain', scilimits=(0, 0), axis='both')
    plt.boxplot(AL_Gau, labels=labels, whis=3, showmeans=True, patch_artist=True,
                boxprops={'color': 'black', 'facecolor': 'skyblue'})
    plt.grid(true)
    plt.grid(color='w', linewidth=1)
    plt.xlabel("Privacy Budget")
    plt.ylabel("Accuracy Loss")
    plt.tight_layout()
    plt.show()


def plt_exp_AL_Perturbation(ep_list, fd, fd2, index, repeat_times):
    sensitivity = abs(fd - fd2)

    AL_M = []
    for i in range(len(ep_list)):
        tmp = perturbation_fun_AL(ep_list[i], fd, fd2, index, repeat_times)
        AL_M.append(tmp)

    labels = '0.2', '0.3', '0.4', '0.5', '1', '1.2', '1.4', '1.6', '1.8', '2.0'

    plt.rcParams['axes.facecolor'] = 'whitesmoke'
    plt.ticklabel_format(style='plain', scilimits=(0, 0), axis='both')
    plt.boxplot(AL_M, labels=labels, whis=3, showmeans=True, patch_artist=True,
                boxprops={'color': 'black', 'facecolor': 'skyblue'})
    plt.grid(true)
    plt.grid(color='w', linewidth=1)
    plt.xlabel("Privacy Budget")
    plt.ylabel("Accuracy Loss")
    plt.tight_layout()
    plt.show()

# Diabetes dataset
# For the counting query
# First Example#
#==============================================#
ep_list = [0.2,0.3,0.4,0.5,1,1.2,1.4,1.6,1.8,2.0]
fd = 768
fd2 = 769
repeat_times = 1000
plt_exp_AL_Laplace(ep_list,fd,fd2,repeat_times)

# Second Example#
#==============================================#
# Diabetes dataset
# ep_list = [0.2,0.3,0.4,0.5,1,1.2,1.4,1.6,1.8,2.0]
# fd = 768
# fd2 = 769
# repeat_times = 1000
# plt_exp_AL_Gaussian(ep_list,fd,fd2,repeat_times)

# Third Example#
#==============================================#
# Diabetes dataset
# ep_list = [0.2,0.3,0.4,0.5,1,1.2,1.4,1.6,1.8,2.0]
# fd = 768
# fd2 = 769
# index = 1
# repeat_times = 1000
# plt_exp_AL_Perturbation(ep_list,fd,fd2,index,repeat_times)