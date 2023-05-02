from Mechanism.Constraints import *

def mapping_inverse_fromPtoR(x, fd, fd2, C):
    map_inverse_x = C * x + (fd + fd2) / 2
    return map_inverse_x

def mapping_fromRtoP(x, fd, fd2, C):
    map_x = (x - (fd + fd2) / 2) * C
    return map_x

def listMapping_fromPtoR(perturbed_list, fd, fd2, C):
    length = len(perturbed_list)
    mapped_perturbedList = []
    for i in range(length):
        tmp_value = mapping_inverse_fromPtoR(perturbed_list[i], fd, fd2, C)
        mapped_perturbedList.append(tmp_value)

    return mapped_perturbedList

def cpRange(ep, k, m, y, index):
    e = math.e

    k = float3f(k)
    m = float3f(m)
    y = float3f(y)

    if (y == 0):
        y = 1000000

    if (index == 1):
        cp_range = k * m * (-k * m - m * y + 1) / (2 * y)
        cp_range = float3f(cp_range * 2)
        return cp_range

    if (index == 2):
        cp_range = k * m * (-k * m - 2 * m * y + 2) / (8 * y)
        cp_range = float3f(cp_range * 2)
        return cp_range

    if (index == 3):
        cp_range = k * m * (-2 * k * m - pi * m * y + pi) / (pi ** 2 * y)
        cp_range = float3f(float(cp_range * 2))
        return cp_range

    if (index == 4):
        cp_range1 = k * m * (-2 * k * m - m * y + 2) / (2 * y)
        cp_range1 = float3f(cp_range1 * 2)

        cp_range2 = (-k * m + 1) * (e ** ep * y - k - y) / (y ** 2 * (e ** ep - 1))
        cp_range2 = float3f(cp_range2 * 2)

        if (cp_range1 <= cp_range2):
            return cp_range1
        else:
            return cp_range2

    if (index == 5):
        cp_range1 = k * m * (-k * m - m * y + 2) / (4 * y)
        cp_range1 = float3f(cp_range1 * 2)

        cp_range2 = (-k * m + 2) * (e ** ep * y - k - y) / (2 * y ** 2 * (e ** ep - 1))
        cp_range2 = float3f(cp_range2 * 2)

        if (cp_range1 <= cp_range2):
            return cp_range1
        else:
            return cp_range2

    if (index == 6):
        cp_range1 = k * m * (-4 * k * m - pi * m * y + 2 * pi) / (pi ** 2 * y)
        cp_range1 = float3f(float(cp_range1 * 2))

        cp_range2 = (-2 * k * m + pi) * (e ** ep * y - k - y) / (pi * y ** 2 * (e ** ep - 1))
        cp_range2 = float3f(float(cp_range2 * 2))

        if (cp_range1 <= cp_range2):
            return cp_range1
        else:
            return cp_range2

    if (index == 7):
        cp_range = k * m * (e ** ep * (-5 * k * m + 5) - m * (4 * e ** ep * y + 1)) / (2 * (4 * e ** ep * y + 1))
        cp_range = float3f(cp_range * 2)
        return cp_range

    if (index == 8):
        cp_range = -k * m * (5 * e ** ep * (k * m - 2) + 2 * m * (4 * e ** ep * y + 1)) / (32 * e ** ep * y + 8)
        cp_range = float3f(cp_range * 2)
        return cp_range

    if (index == 9):
        cp_range = -k * m * (5 * e ** ep * (2 * k * m - pi) + pi * m * (4 * e ** ep * y + 1)) / (
                    pi ** 2 * (4 * e ** ep * y + 1))
        cp_range = float3f(float(cp_range * 2))
        return cp_range

    if (index == 10):
        cp_range1 = k * m * (-3 * k * m - m * y + 3) / (2 * y)
        cp_range1 = float3f(float(cp_range1 * 2))

        if -(k * (e ** ep - 1) * (k * m - 1) / y) < 0:
            return 0

        cp_range2 = (-2 * sqrt(6) * y ** 3 * sqrt(-k * (e ** ep - 1) * (k * m - 1) / y) + 9 * (1 - e ** ep) * (
                    -k * m + 1) ** 2) / (6 * y * (e ** ep - 1) * (k * m - 1))
        # print ("cp_range2 =", cp_range2)
        cp_range2 = float3f(float(cp_range2 * 2))

        if (cp_range1 <= cp_range2):
            return cp_range1
        else:
            return cp_range2

    if (index == 11):
        cp_range1 = k * m * (-3 * k * m - 2 * m * y + 6) / (8 * y)
        cp_range1 = float3f(float(cp_range1 * 2))

        if -(k * (e ** ep - 1) * (k * m - 2) / y) < 0:
            return 0

        cp_range2 = (-8 * sqrt(3) * y ** 3 * sqrt(-k * (e ** ep - 1) * (k * m - 2) / y) + 9 * (1 - e ** ep) * (
                    -k * m + 2) ** 2) / (12 * y * (e ** ep - 1) * (k * m - 2))
        # print ("cp_range2 =", cp_range2)
        cp_range2 = float3f(float(cp_range2 * 2))

        if (cp_range1 <= cp_range2):
            return cp_range1
        else:
            return cp_range2

    if (index == 12):
        cp_range1 = k * m * (-6 * k * m - pi * m * y + 3 * pi) / (pi ** 2 * y)
        cp_range1 = float3f(float(cp_range1 * 2))

        if -(k * (e ** ep - 1) * (2 * k * m - pi) / y) < 0:
            return 0

        cp_range2 = (-2 * sqrt(6) * pi ** (3 / 2) * y ** 3 * sqrt(-k * (e ** ep - 1) * (2 * k * m - pi) / y) + 9 * (
                    1 - e ** ep) * (-2 * k * m + pi) ** 2) / (6 * pi * y * (e ** ep - 1) * (2 * k * m - pi))
        # print ("cp_range2 =", cp_range2)
        cp_range2 = float3f(float(cp_range2 * 2))

        if (cp_range1 <= cp_range2):
            return cp_range1
        else:
            return cp_range2

    print("CP Range Value Incorrect, Index=", index)
    return -1