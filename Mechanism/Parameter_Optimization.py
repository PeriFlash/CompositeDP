from Mechanism.Mapping import *
from Mechanism.Evaluation import *

def parameter_optimazation(ep, fd, fd2, index):
    e = math.e

    # Work out Sensitivity
    sensitivity = abs(fd - fd2)

    # First round, work out 0.1 accuracy
    step1 = 0.1
    step2 = 0.01
    step3 = 0.001
    k_best = 0
    m_best = 0
    y_best = 0
    reduceRate_best = -1000
    var_best = 10000
    var_lap_pick = 0
    cp_pick = 0
    L_pick = 0
    a_pick = 0

    y_upper = 1
    k_upper = 1
    m_upper = 2

    k_stop = 0
    y_stop = 0

    # y_count = 0.001
    y_count = 0


    while (y_count < y_upper):
        # print("y_count =", y_count)
        k_count = 0
        while (k_count < k_upper):
            m_count = 0
            while (m_count <= m_upper):
                # Work out Cp
                cp_range = cpRange(ep, k_count, m_count, y_count, index)
                if (cp_range == 0):
                    m_count = m_count + step1
                    continue
                C = sensitivity / cp_range
                cp_count = mapping_fromRtoP(fd, fd, fd2, 1 / C)

                # Check Constraint
                if (check_constraint(ep, k_count, m_count, cp_count, y_count, index) == 0):
                    # Work out variance
                    var_tmp = perturbation_fun_var(ep, k_count, m_count, y_count, cp_count, index)
                    if (var_tmp > 0):
                        var_lap = (cp_range / ep) ** 2 * 2
                        reduceRate_tmp = reduceRate(var_lap, var_tmp)

                        if (reduceRate_tmp > reduceRate_best):
                            reduceRate_best = reduceRate_tmp
                            y_best = y_count
                            k_best = k_count
                            m_best = m_count
                            cp_pick = cp_count

                m_count = m_count + step1
            k_count = k_count + step1
        y_count = y_count + step1

    # Second round, work out 0.01 accuracy

    if (y_best == 0):
        y_count = 0
        y_count_end = 0.1
    else:
        y_count = y_best - step1
        y_count_end = y_best + step1
    while (y_count < y_count_end):
        if (k_best == 0):
            k_count = 0
            k_count_end = 0.1
        else:
            k_count = k_best - step1
            k_count_end = k_best + step1
        while (k_count < k_count_end):
            if (m_best == 0):
                m_count = 0
                m_count_end = 0.1
            else:
                m_count = m_best - step1
                m_count_end = m_best + step1
            while (m_count < m_count_end):

                # Work out Cp
                cp_range = cpRange(ep, k_count, m_count, y_count, index)
                if (cp_range == 0):
                    m_count = m_count + step2
                    continue
                C = sensitivity / cp_range
                cp_count = mapping_fromRtoP(fd, fd, fd2, 1 / C)

                # Check Constraint
                if check_constraint(ep, k_count, m_count, cp_count, y_count, index) == 0:
                    # Work out variance
                    var_tmp = perturbation_fun_var(ep, k_count, m_count, y_count, cp_count, index)
                    if (var_tmp > 0):
                        var_lap = (cp_range / ep) ** 2 * 2
                        reduceRate_tmp = reduceRate(var_lap, var_tmp)
                        if (reduceRate_tmp > reduceRate_best):
                            reduceRate_best = reduceRate_tmp
                            y_best = y_count
                            k_best = k_count
                            m_best = m_count
                            cp_pick = cp_count

                m_count = m_count + step2
            k_count = k_count + step2
        y_count = y_count + step2

    # Third round, work out 0.001 accuracy
    if (y_best == 0):
        y_count = 0
        y_count_end = 0.01
    else:
        y_count = y_best - step2
        y_count_end = y_best + step2

    while (y_count < y_count_end):
        if (k_best == 0):
            k_count = 0
            k_count_end = 0.01
        else:
            k_count = k_best - step2
            k_count_end = k_best + step2
        while (k_count < k_count_end):
            if (m_best == 0):
                m_count = 0
                m_count_end = 0.01
            else:
                m_count = m_best - step2
                m_count_end = m_best + step2
            while (m_count < m_count_end):
                # Work out Cp
                cp_range = cpRange(ep, k_count, m_count, y_count, index)
                if (cp_range == 0):
                    m_count = m_count + step3
                    continue
                C = sensitivity / cp_range
                cp_count = mapping_fromRtoP(fd, fd, fd2, 1 / C)

                # Check Constraint
                if check_constraint(ep, k_count, m_count, cp_count, y_count, index) == 0:
                    # Work out variance
                    var_tmp = perturbation_fun_var(ep, k_count, m_count, y_count, cp_count, index)
                    if (var_tmp > 0):
                        var_lap = (cp_range / ep) ** 2 * 2
                        reduceRate_tmp = reduceRate(var_lap, var_tmp)
                        if (reduceRate_tmp > reduceRate_best):
                            reduceRate_best = reduceRate_tmp
                            y_best = y_count
                            k_best = k_count
                            m_best = m_count
                            cp_pick = cp_count

                m_count = m_count + step3
            k_count = k_count + step3
        y_count = y_count + step3

    return k_best, m_best, y_best, cp_pick