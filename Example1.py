#from sympy import symbols, expand, collect, integrate, Eq, solveset

import matplotlib.pyplot as plt

from Traditional_Mechanism import *
from Perturbation_Mechanism import *


def plt_exp_MSE_RE01(ep_list, fd, fd2, repeat_times, d):
    sensitivity = abs(fd - fd2)

    Lap_MSE = []
    Gau_MSE = []

    MX_11_MSE = []
    MX_22_MSE = []
    MX_33_MSE = []
    # =====================================================================#

    Lap_RE = []
    Gau_RE = []

    MX_11_RE = []
    MX_22_RE = []
    MX_33_RE = []

    for i in range(len(ep_list)):
        Lap_MSE.append(Laplace_MSE_Log(sensitivity, ep_list[i], repeat_times, d))
        Gau_MSE.append(Gaussian_MSE_Log(sensitivity, ep_list[i], repeat_times, d))

        MX_11_MSE.append(perturbation_fun_MSE_Log(ep_list[i], fd, fd2, 1, repeat_times, d))
        MX_22_MSE.append(perturbation_fun_MSE_Log(ep_list[i], fd, fd2, 5, repeat_times, d))
        MX_33_MSE.append(perturbation_fun_MSE_Log(ep_list[i], fd, fd2, 9, repeat_times, d))

        Lap_RE.append(Laplace_RE(sensitivity, ep_list[i], repeat_times))
        Gau_RE.append(Gaussian_RE(sensitivity, ep_list[i], repeat_times))

        MX_11_RE.append(perturbation_fun_RE(ep_list[i], fd, fd2, 1, repeat_times))
        MX_22_RE.append(perturbation_fun_RE(ep_list[i], fd, fd2, 5, repeat_times))
        MX_33_RE.append(perturbation_fun_RE(ep_list[i], fd, fd2, 9, repeat_times))

    X_labels = []
    for i in range(len(ep_list)):
        X_labels.append(str(ep_list[i]))

    X_axis = np.arange(len(X_labels))

    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()

    bar_width = 0.15
    space = 0.05
    diff = bar_width + space
    ax1.bar(X_axis - diff * 2, Gau_RE, color="white", ec="green", width=bar_width, label="Gaussian", ls="-",
            hatch="///")
    ax1.bar(X_axis - diff, Lap_RE, color="white", ec="blue", width=bar_width, label="Laplace", ls="-", hatch="///")
    ax1.bar(X_axis, MX_11_RE, color="white", ec="orange", width=bar_width, label="Act1-Base1", ls="-", hatch="///")
    ax1.bar(X_axis + diff, MX_22_RE, color="white", ec="red", width=bar_width, label="Act2-Base2", ls="-", hatch="///")
    ax1.bar(X_axis + diff * 2, MX_33_RE, color="white", ec="slategray", width=bar_width, label="Act3-Base3", ls="-",
            hatch="///")

    ax1.set_ylabel("RE")
    ax2.plot(X_axis, Gau_MSE, color="green", linewidth=2.0, marker='D', linestyle="-.", label="Gaussian")
    ax2.plot(X_axis, Lap_MSE, color="blue", linewidth=2.0, marker='D', linestyle="--", label="Laplace")
    ax2.plot(X_axis, MX_11_MSE, color="orange", linewidth=2.0, marker='o', linestyle="-", label="Act1-Base1")
    ax2.plot(X_axis, MX_22_MSE, color="red", linewidth=2.0, marker='<', linestyle="-", label="Act2-Base2")
    ax2.plot(X_axis, MX_33_MSE, color="slategray", linewidth=2.0, marker='H', linestyle="-", label="Act3-Base3")

    ax2.set_ylabel("log(MSE+1)")
    ax1.set_xlabel("Privacy Budget")

    plt.legend(loc='upper right')
    plt.xlabel("Privacy Budget")
    plt.xticks(X_axis, X_labels)
    plt.tight_layout()
    plt.show()


def plt_exp_MSE_RE02(ep_list, fd, fd2, repeat_times, d):
    sensitivity = abs(fd - fd2)

    Lap_MSE = []
    Gau_MSE = []

    MX_12_MSE = []
    MX_23_MSE = []
    MX_34_MSE = []

    # =====================================================================#

    Lap_RE = []
    Gau_RE = []

    MX_12_RE = []
    MX_23_RE = []
    MX_34_RE = []

    for i in range(len(ep_list)):
        Lap_MSE.append(Laplace_MSE_Log(sensitivity, ep_list[i], repeat_times, d))
        Gau_MSE.append(Gaussian_MSE_Log(sensitivity, ep_list[i], repeat_times, d))

        MX_12_MSE.append(perturbation_fun_MSE_Log(ep_list[i], fd, fd2, 4, repeat_times, d))
        MX_23_MSE.append(perturbation_fun_MSE_Log(ep_list[i], fd, fd2, 8, repeat_times, d))
        MX_34_MSE.append(perturbation_fun_MSE_Log(ep_list[i], fd, fd2, 12, repeat_times, d))

        Lap_RE.append(Laplace_RE(sensitivity, ep_list[i], repeat_times))
        Gau_RE.append(Gaussian_RE(sensitivity, ep_list[i], repeat_times))

        MX_12_RE.append(perturbation_fun_RE(ep_list[i], fd, fd2, 4, repeat_times))
        MX_23_RE.append(perturbation_fun_RE(ep_list[i], fd, fd2, 8, repeat_times))
        MX_34_RE.append(perturbation_fun_RE(ep_list[i], fd, fd2, 12, repeat_times))

    X_labels = []
    for i in range(len(ep_list)):
        X_labels.append(str(ep_list[i]))

    X_axis = np.arange(len(X_labels))

    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()

    bar_width = 0.15
    space = 0.05

    diff = bar_width + space

    ax1.bar(X_axis - diff * 2, Gau_RE, color="white", ec="green", width=bar_width, label="Gaussian", ls="-",
            hatch="///")
    ax1.bar(X_axis - diff, Lap_RE, color="white", ec="blue", width=bar_width, label="Laplace", ls="-", hatch="///")
    ax1.bar(X_axis, MX_12_RE, color="white", ec="brown", width=bar_width, label="Act1-Base2", ls="-", hatch="///")
    ax1.bar(X_axis + diff, MX_23_RE, color="white", ec="coral", width=bar_width, label="Act2-Base3", ls="-",
            hatch="///")
    ax1.bar(X_axis + diff * 2, MX_34_RE, color="white", ec="blueviolet", width=bar_width, label="Act3-Base4", ls="-",
            hatch="///")

    ax1.set_ylabel("RE")

    ax2.plot(X_axis, Gau_MSE, color="green", linewidth=2.0, marker='D', linestyle="-.", label="Gaussian")
    ax2.plot(X_axis, Lap_MSE, color="blue", linewidth=2.0, marker='D', linestyle="--", label="Laplace")
    ax2.plot(X_axis, MX_12_MSE, color="brown", linewidth=2.0, marker='o', linestyle="-", label="Act1-Base2")
    ax2.plot(X_axis, MX_23_MSE, color="coral", linewidth=2.0, marker='<', linestyle="-", label="Act2-Base3")
    ax2.plot(X_axis, MX_34_MSE, color="blueviolet", linewidth=2.0, marker='H', linestyle="-", label="Act3-Base4")

    ax2.set_ylabel("log(MSE+1)")
    ax1.set_xlabel("Privacy Budget")

    plt.legend(loc='upper right')
    plt.xlabel("Privacy Budget")
    plt.xticks(X_axis, X_labels)
    plt.tight_layout()
    plt.show()


# # For Mod Value
# Dataset:Diabetes, data attributes:BMI
# ###===========================###
# mod_raw = 32.0
# mod_nei = 31.2
# sensitivity_mod = 0.8000000000000007
# ###===========================###
#
# Dataset:Diabetes, data attributes:Glucose
# ###===========================###
# mod_raw = 99
# mod_nei = 100
# sensitivity_mod = 1
# ###===========================###
#
# Dataset:Runging_and_HR, data attributes:time_elapsed
# ###===========================###
# mod_raw = 472.0
# mod_nei = 448.0
# sensitivity_mod = 24.0
# ###===========================###
#
# Dataset:Runging_and_HR, data attributes:max_speed
# ###===========================###
# mod_raw = 13.9752
# mod_nei = 14.2092
# sensitivity_mod = 0.23399999999999999
# ###===========================###


# First Example#
#==============================================#
mod_raw = 32.0
mod_nei = 31.2
sensitivity_mod = 0.8000000000000007
ep_list = [0.2,0.3,0.5,1,2,5]
fd = mod_raw
fd2 = mod_nei
repeat_times = 10000
d = 1
plt_exp_MSE_RE01(ep_list,fd,fd2,repeat_times,d)

# Second Example#
#==============================================#
# mod_raw = 32.0
# mod_nei = 31.2
# sensitivity_mod = 0.8000000000000007
# ep_list = [0.2,0.3,0.5,1,2,5]
# fd = mod_raw
# fd2 = mod_nei
# repeat_times = 10000
# d = 1
# plt_exp_MSE_RE02(ep_list,fd,fd2,repeat_times,d)
