import random
from Mechanism.Parameter_Optimization import *
import numpy as np

# The Probability Density Function P(x) of the Proposed Mechanism is as follows:
def probability_fun(x, ep, k, m, cp, y, index):
    e = math.e
    y = float3f(y)
    L = float3f(LValue(ep, k, m, y, index))
    a = float3f(aValue(k, m, cp, index))

    k = float3f(k)
    m = float3f(m)
    cp = float3f(cp)

    if (index == 1):
        P = 0
        if ((x >= -L) and (x < a)):
            P = y
        if ((x >= a) and (x < a + m)):
            P = y + k
        if ((x >= a + m) and (x <= L)):
            P = y
        return float2f(P)

    if (index == 2):
        P = 0
        if ((x >= -L) and (x < a)):
            P = y
        if ((x >= a) and (x < a + m / 2)):
            P = y + 2 * k / m * x - 2 * a * k / m
        if ((x >= a + m / 2) and (x < a + m)):
            P = y - 2 * k / m * x + 2 * (a + m) * k / m
        if ((x >= a + m) and (x <= L)):
            P = y
        return float2f(P)

    if (index == 3):
        P = 0
        if ((x >= -L) and (x < a)):
            P = y
        if ((x >= a) and (x < a + m)):
            P = y + k * sin(pi / m * (x - a))
        if ((x >= a + m) and (x <= L)):
            P = y
        return float2f(float(P))

    if (index == 4):
        P = 0
        if (cp >= 0):
            if ((x >= -L) and (x < 0)):
                P = y / L * x + y
            if ((x >= 0) and (x < a)):
                P = -y / L * x + y
            if ((x >= a) and (x <= a + m)):
                P = -y / L * x + y + k
            if ((x >= a + m) and (x <= L)):
                P = -y / L * x + y
        else:
            if ((x >= -L) and (x < a)):
                P = y / L * x + y
            if ((x >= a) and (x < a + m)):
                P = y / L * x + y + k
            if ((x >= a + m) and (x <= 0)):
                P = y / L * x + y
            if ((x >= 0) and (x <= L)):
                P = -y / L * x + y
        return float2f(P)

    if (index == 5):
        P = 0
        if (cp >= 0):
            if ((x >= -L) and (x < 0)):
                P = y / L * x + y
            if ((x >= 0) and (x < a)):
                P = -y / L * x + y
            if ((x >= a) and (x <= a + m / 2)):
                P = -y / L * x + y + 2 * k / m * x - 2 * a * k / m
            if ((x >= a + m / 2) and (x <= a + m)):
                P = -y / L * x + y - 2 * k / m * x + 2 * (a + m) * k / m
            if ((x >= a + m) and (x <= L)):
                P = -y / L * x + y
        else:
            if ((x >= -L) and (x < a)):
                P = y / L * x + y
            if ((x >= a) and (x < a + m / 2)):
                P = y / L * x + y + 2 * k / m * x - 2 * a * k / m
            if ((x >= a + m / 2) and (x < a + m)):
                P = y / L * x + y - 2 * k / m * x + 2 * (a + m) * k / m
            if ((x >= a + m) and (x <= 0)):
                P = y / L * x + y
            if ((x >= 0) and (x <= L)):
                P = -y / L * x + y
        return float2f(P)

    if (index == 6):
        P = 0
        if (cp >= 0):
            if ((x >= -L) and (x < 0)):
                P = y / L * x + y
            if ((x >= 0) and (x < a)):
                P = -y / L * x + y
            if ((x >= a) and (x <= a + m)):
                P = -y / L * x + y + k * sin(pi / m * (x - a))
            if ((x >= a + m) and (x <= L)):
                P = -y / L * x + y
        else:
            if ((x >= -L) and (x < a)):
                P = y / L * x + y
            if ((x >= a) and (x < a + m)):
                P = y / L * x + y + k * sin(pi / m * (x - a))
            if ((x >= a + m) and (x <= 0)):
                P = y / L * x + y
            if ((x >= 0) and (x <= L)):
                P = -y / L * x + y
        return float2f(float(P))

    if (index == 7):
        P = 0
        if ((x >= -L) and (x < a)):
            P = -(y-1/e**ep)/L**4*x**4+y
        if ((x >= a) and (x < a + m)):
            P = -(y-1/e**ep)/L**4*x**4+y + k
        if ((x >= a + m) and (x <= L)):
            P = -(y-1/e**ep)/L**4*x**4+y
        return float2f(P)

    if (index == 8):
        P = 0
        if ((x >= -L) and (x < a)):
            P = -(y-1/e**ep)/L**4*x**4+y
        if ((x >= a) and (x < a + m / 2)):
            P = -(y-1/e**ep)/L**4*x**4+y + 2*k/m*x - 2*a*k/m
        if ((x >= a + m / 2) and (x < a + m)):
            P = -(y-1/e**ep)/L**4*x**4+y - 2*k/m*x + 2*(a+m)*k/m
        if ((x >= a + m) and (x <= L)):
            P = -(y-1/e**ep)/L**4*x**4+y
        return float2f(P)

    if (index == 9):
        P = 0
        if ((x >= -L) and (x < a)):
            P = -(y-1/e**ep)/L**4*x**4+y
        if ((x >= a) and (x < a + m)):
            P = -(y-1/e**ep)/L**4*x**4+y + k*sin(pi/m*(x-a))
        if ((x >= a + m) and (x <= L)):
            P = -(y-1/e**ep)/L**4*x**4+y
        return float2f(float(P))

    if (index == 10):
        P = 0
        if (cp >= 0):
            if ((x >= -L) and (x < 0)):
                P = y / L ** 2 * (x + L) ** 2
            if ((x >= 0) and (x < a)):
                P = y / L ** 2 * (x - L) ** 2
            if ((x >= a) and (x <= a + m)):
                P = y / L ** 2 * (x - L) ** 2 + k
            if ((x >= a + m) and (x <= L)):
                P = y / L ** 2 * (x - L) ** 2
        else:
            if ((x >= -L) and (x < a)):
                P = y / L ** 2 * (x + L) ** 2
            if ((x >= a) and (x < a + m)):
                P = y / L ** 2 * (x + L) ** 2 + k
            if ((x >= a + m) and (x <= 0)):
                P = y / L ** 2 * (x + L) ** 2
            if ((x >= 0) and (x <= L)):
                P = y / L ** 2 * (x - L) ** 2
        return float2f(P)

    if (index == 11):
        P = 0
        if (cp >= 0):
            if ((x >= -L) and (x < 0)):
                P = y / L ** 2 * (x + L) ** 2
            if ((x >= 0) and (x < a)):
                P = y / L ** 2 * (x - L) ** 2
            if ((x >= a) and (x <= a + m / 2)):
                P = y / L ** 2 * (x - L) ** 2 + 2 * k / m * x - 2 * a * k / m
            if ((x >= a + m / 2) and (x <= a + m)):
                P = y / L ** 2 * (x - L) ** 2 - 2 * k / m * x + 2 * (a + m) * k / m
            if ((x >= a + m) and (x <= L)):
                P = y / L ** 2 * (x - L) ** 2
        else:
            if ((x >= -L) and (x < a)):
                P = y / L ** 2 * (x + L) ** 2
            if ((x >= a) and (x < a + m / 2)):
                P = y / L ** 2 * (x + L) ** 2 + 2 * k / m * x - 2 * a * k / m
            if ((x >= a + m / 2) and (x < a + m)):
                P = y / L ** 2 * (x - L) ** 2 - 2 * k / m * x + 2 * (a + m) * k / m
            if ((x >= a + m) and (x <= 0)):
                P = y / L ** 2 * (x + L) ** 2
            if ((x >= 0) and (x <= L)):
                P = y / L ** 2 * (x - L) ** 2
        return float2f(P)

    if (index == 12):
        P = 0
        if (cp >= 0):
            if ((x >= -L) and (x < 0)):
                P = y / L ** 2 * (x + L) ** 2
            if ((x >= 0) and (x < a)):
                P = y / L ** 2 * (x - L) ** 2
            if ((x >= a) and (x <= a + m)):
                P = y / L ** 2 * (x - L) ** 2 + k * sin(pi / m * (x - a))
            if ((x >= a + m) and (x <= L)):
                P = y / L ** 2 * (x - L) ** 2
        else:
            if ((x >= -L) and (x < a)):
                P = y / L ** 2 * (x + L) ** 2
            if ((x >= a) and (x < a + m)):
                P = y / L ** 2 * (x + L) ** 2 + k * sin(pi / m * (x - a))
            if ((x >= a + m) and (x <= 0)):
                P = y / L ** 2 * (x + L) ** 2
            if ((x >= 0) and (x <= L)):
                P = y / L ** 2 * (x - L) ** 2
        return float2f(float(P))

    print("P Value Incorrect")
    return -1

# This "perturbation_fun_generate_perturbed_list" function can generate the perturbed results in a list according to parameter setup and Cp.
def perturbation_fun_generate_perturbed_list(ep, k, m, y, cp, index):
    e = math.e
    k = float3f(k)
    m = float3f(m)
    y = float3f(y)
    cp = float3f(cp)

    # Check the constraint:
    if check_constraint(ep, k, m, cp, y, index) != 0:
        #        print("Constraint Errors")
        return -1
    L = LValue(ep, k, m, y, index)
    divid = 10000

    step = 2 * L / divid
    x_count = -L

    X_axis = []
    P_axis = []
    perturbed_list = []

    while (x_count <= L):
        P_x = probability_fun(x_count, ep, k, m, cp, y, index)
        P_axis.append(P_x)
        X_axis.append(x_count)
        x_count = x_count + step

    for i in range(len(X_axis)):
        rp = P_axis[i]
        rp = int(rp * 100)
        for j in range(rp):
            perturbed_list.append(X_axis[i])

    random.shuffle(perturbed_list)
    return perturbed_list

# The Experimental Variance (which is relevant to parameter k, m, y) of the Proposed Mechanism is as follows:
def perturbation_fun_var_exp(ep, k, m, y, cp, index):
    perturbed_list = perturbation_fun_generate_perturbed_list(ep, k, m, y, cp, index)
    variance = 0
    for i in range(len(perturbed_list)):
        variance = variance + (perturbed_list[i] - cp) ** 2
    variance = variance / (len(perturbed_list))
    return variance

def perturbation_fun_oneCall(ep, fd, fd2, k, m, y, index):
    # Work out Sensitivity
    sensitivity = abs(fd - fd2)

    cp_range = cpRange(ep, k, m, y, index)
    if (cp_range == 0):
        print("Parameter setup Errors")
        return 0
    C = sensitivity / cp_range
    cp = mapping_fromRtoP(fd, fd, fd2, 1/C)
    perturbed_list = perturbation_fun_generate_perturbed_list(ep, k, m, y, cp, index)

    if (perturbed_list == -1 ):
        print("Parameter Constraint Errors")
        return 0
    else:
        mapped_perturbedList = listMapping_fromPtoR(perturbed_list, fd, fd2, C)
        return mapped_perturbedList[0]

def perturbation_fun_multipleCall(ep, fd, fd2, k, m, y, index, repeat_times):
    # Work out Sensitivity
    sensitivity = abs(fd - fd2)

    cp_range = cpRange(ep, k, m, y, index)
    if (cp_range == 0):
        print("Parameter setup Errors")
        return 0
    C = sensitivity / cp_range
    cp = mapping_fromRtoP(fd, fd, fd2, 1/C)
    perturbed_list = perturbation_fun_generate_perturbed_list(ep, k, m, y, cp, index)

    if (perturbed_list == -1 ):
        print("Parameter Constraint Errors")
        return 0
    else:
        mapped_perturbedList = listMapping_fromPtoR(perturbed_list, fd, fd2, C)
        ret_perturbed = []
        for i in range(repeat_times):
            ret_perturbed.append(mapped_perturbedList[i])

        return ret_perturbed


def perturbation_fun_optimized_oneCall(ep, fd, fd2, index):
    # Work out Sensitivity
    sensitivity = abs(fd - fd2)
    k_best, m_best, y_best, cp_pick = parameter_optimazation(ep, fd, fd2, index)

    # Work out perturbed_list
    perturbed_list = perturbation_fun_generate_perturbed_list(ep, k_best, m_best, y_best, cp_pick, index)

    # Map to real space
    cp_range = cpRange(ep, k_best, m_best, y_best, index)
    if (cp_range == 0):
        print("Parameter setup Errors")
        return 0
    C = sensitivity / cp_range
    mapped_perturbedList = listMapping_fromPtoR(perturbed_list, fd, fd2, C)

    return mapped_perturbedList[0]

def perturbation_fun_optimized_multipleCall(ep, fd, fd2, index, repeat_times):
    # Work out Sensitivity
    sensitivity = abs(fd - fd2)
    k_best, m_best, y_best, cp_pick = parameter_optimazation(ep, fd, fd2, index)

    # Work out perturbed_list
    perturbed_list = perturbation_fun_generate_perturbed_list(ep, k_best, m_best, y_best, cp_pick, index)

    # Map to real space
    cp_range = cpRange(ep, k_best, m_best, y_best, index)
    if (cp_range == 0):
        print("Parameter setup Errors")
        return 0
    C = sensitivity / cp_range
    mapped_perturbedList = listMapping_fromPtoR(perturbed_list, fd, fd2, C)

    ret_perturbed = []
    for i in range(repeat_times):
        ret_perturbed.append(mapped_perturbedList[i])

    return ret_perturbed

def Calculate_MSE(input_list, fd):
    MSE = 0
    for i in range(len(input_list)):
        MSE = MSE + (input_list[i] - fd) ** 2
    MSE = MSE / len(input_list)

    return float(MSE)


def Calculate_RE(input_list, fd):
    RE = 0
    for i in range(len(input_list)):
        RE = RE + abs(input_list[i] - fd)
    RE = RE / len(input_list)

    return float(RE)

def Calculate_Bias(input_list, fd):
    Bias = 0
    for i in range(len(input_list)):
        Bias = Bias + (input_list[i] - fd) / fd

    Bias = Bias / len(input_list)
    return abs(Bias)

def Calculate_AL(input_list, fd):
    AL = []
    for i in range(len(input_list)):
        tmp_al = abs((input_list[i]-fd)/fd)
        AL.append(tmp_al)

    return AL

def perturbation_fun_MSE(ep, fd, fd2, index, repeat_times):
    perturbed_list = perturbation_fun_optimized_multipleCall(ep, fd, fd2, index, repeat_times)
    MSE = Calculate_MSE(perturbed_list, fd)
    return MSE

def perturbation_fun_MSE_Log(ep, fd, fd2, index, repeat_times,d):
    perturbed_list = perturbation_fun_optimized_multipleCall(ep, fd, fd2, index, repeat_times)
    MSE = Calculate_MSE(perturbed_list, fd)
    return np.log(MSE+d)


def perturbation_fun_RE(ep, fd, fd2, index, repeat_times):
    perturbed_list = perturbation_fun_optimized_multipleCall(ep, fd, fd2, index, repeat_times)
    RE = Calculate_RE(perturbed_list, fd)
    return RE

def perturbation_fun_AL(ep, fd, fd2, index,repeat_times):
    perturbed_list = perturbation_fun_optimized_multipleCall(ep, fd, fd2, index, repeat_times)
    AL = Calculate_AL(perturbed_list, fd)
    return AL

def perturbation_fun_Bias(ep, fd, fd2, index, repeat_times):
    perturbed_list = perturbation_fun_optimized_multipleCall(ep, fd, fd2, index, repeat_times)
    Bias = Calculate_Bias(perturbed_list, fd)
    return abs(Bias)

def perturbation_fun_Var_and_HRate(ep, fd, fd2, index, k, m, y, repeat_times):
    sensitivity = abs(fd - fd2)
    cp_range = cpRange(ep, k, m, y, index)

    if (cp_range != 0):
        C = sensitivity / cp_range
        cp = mapping_fromRtoP(fd, fd, fd2, 1 / C)
        if (check_constraint(ep, k, m, cp, y, index) == 0):
            perturbed_list = perturbation_fun_generate_perturbed_list(ep, k, m, y, cp, index)
            C = sensitivity / cp_range
            mapped_perturbedList = listMapping_fromPtoR(perturbed_list, fd, fd2, C)

            H1 = H1Rate(ep, k, m, y, index)
            H2 = H2Rate(ep, cp, k, m, y, index)
            ret_perturbed = []
            for i in range(repeat_times):
                ret_perturbed.append(mapped_perturbedList[i])

            Var = Calculate_MSE(ret_perturbed, fd)
            return abs(H1), abs(H2), Var
        else:
            print("Constraint Errors")
            return -1
    else:
        print("Cp_range Errors")
        return -2