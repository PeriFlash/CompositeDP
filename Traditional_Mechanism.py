import numpy as np

# Comparative mechanisms
def Laplace_fun(sensitivity, epsilon):
    noise = np.random.laplace(0, sensitivity / epsilon)
    return noise
def Gaussian_fun(sensitivity, epsilon):
    delta = 1e-6
    sigma = np.sqrt(2 * np.log(1.25 / delta)) * sensitivity / epsilon
    noise = np.random.normal(loc=0, scale=sigma)
    return noise

def Laplace_MSE(sensitivity, epsilon, repeat_times):
    MSE = 0
    for i in range(repeat_times):
        tmp = Laplace_fun(sensitivity, epsilon)
        MSE = MSE + tmp ** 2

    MSE = MSE / repeat_times
    return MSE

def Laplace_MSE_Log(sensitivity, epsilon, repeat_times,d):
    MSE = 0
    for i in range(repeat_times):
        tmp = Laplace_fun(sensitivity, epsilon)
        MSE = MSE + tmp ** 2

    MSE = MSE / repeat_times
    return np.log(MSE+d)

def Gaussian_MSE(sensitivity, epsilon, repeat_times):
    MSE = 0
    for i in range(repeat_times):
        tmp = Gaussian_fun(sensitivity, epsilon)
        MSE = MSE + tmp ** 2

    MSE = MSE / repeat_times
    return MSE


def Gaussian_MSE_Log(sensitivity, epsilon, repeat_times,d):
    MSE = 0
    for i in range(repeat_times):
        tmp = Gaussian_fun(sensitivity, epsilon)
        MSE = MSE + tmp ** 2

    MSE = MSE / repeat_times
    return np.log(MSE+d)


def Laplace_RE(sensitivity, epsilon, repeat_times):
    RE = 0
    for i in range(repeat_times):
        tmp = Laplace_fun(sensitivity, epsilon)
        RE = RE + abs(tmp)

    RE = RE / repeat_times
    return RE

def Gaussian_RE(sensitivity, epsilon, repeat_times):
    RE = 0
    for i in range(repeat_times):
        tmp = Gaussian_fun(sensitivity, epsilon)
        RE = RE + abs(tmp)

    RE = RE / repeat_times
    return RE

def Laplace_Bias(sensitivity, epsilon, fd, repeat_times):
    Bias = 0
    for i in range(repeat_times):
        tmp = Laplace_fun(sensitivity, epsilon)
        Bias = Bias + tmp / fd

    Bias = Bias / repeat_times
    return abs(Bias)

def Gaussian_Bias(sensitivity, epsilon, fd, repeat_times):
    Bias = 0
    for i in range(repeat_times):
        tmp = Gaussian_fun(sensitivity, epsilon)
        Bias = Bias + tmp / fd

    Bias = Bias / repeat_times
    return abs(Bias)

def Laplace_AL(sensitivity, epsilon, fd, repeat_times):
    AL = []
    for i in range(repeat_times):
        tmp = Laplace_fun(sensitivity, epsilon)
        tmp_al = abs(tmp/fd)
        AL.append(tmp_al)
    return AL

def Gaussian_AL(sensitivity, epsilon, fd, repeat_times):
    AL = []
    for i in range(repeat_times):
        tmp = Gaussian_fun(sensitivity, epsilon)
        tmp_al = abs(tmp/fd)
        AL.append(tmp_al)
    return AL