from sympy import *
import math

def float3f(num):
    return float(format(num, '.3f'))

def float2f(num):
    return float(format(num, '.2f'))

def LValue(ep, k, m, y, index):
    e = math.e

    if (index == 1):
        L = (1 - k * m) / (2 * y)
        return L

    if (index == 2):
        L = (-k * m + 2) / (4 * y)
        return L

    if (index == 3):
        L = (-k * m + pi / 2) / (pi * y)
        return float(L)

    if (index == 4):
        L = (1 - k * m) / y
        return L

    if (index == 5):
        L = (2 - k * m) / (2 * y)
        return L

    if (index == 6):
        L = (-2 * k * m + pi) / (pi * y)
        return float(L)

    if (index == 7):
        L = 5 * e ** ep * (-k * m + 1) / (2 * (4 * e ** ep * y + 1))
        return L

    if (index == 8):
        L = 5 * e ** ep * (-k * m + 2) / (4 * (4 * e ** ep * y + 1))
        return L

    if (index == 9):
        L = 5 * e ** ep * (-2 * k * m + pi) / (2 * pi * (4 * e ** ep * y + 1))
        return float(L)

    if (index == 10):
        L = -3 * (k * m - 1) / (2 * y)
        return float(L)

    if (index == 11):
        L = -3 * (k * m - 2) / (4 * y)
        return float(L)

    if (index == 12):
        L = 3 * (-2 * k * m + pi) / (2 * pi * y)
        return float(L)

    print("L Value Incorrect, Index =", index)
    return -1


def aValue(k, m, cp, index):
    e = math.e

    if ((k == 0) or (m == 0)):
        return 0

    if (index == 1):
        a = -(-2 * cp + k * m ** 2) / (2 * k * m)
        return a

    if (index == 2):
        a = -(-4 * cp + k * m ** 2) / (2 * k * m)
        return a

    if (index == 3):
        a = -(-pi * cp + k * m ** 2) / (2 * k * m)
        return float(a)

    if (index == 4):
        a = -(-2 * cp + k * m ** 2) / (2 * k * m)
        return a

    if (index == 5):
        a = -(-4 * cp + k * m ** 2) / (2 * k * m)
        return a

    if (index == 6):
        a = -(-pi * cp + k * m ** 2) / (2 * k * m)
        return float(a)

    if (index == 7):
        a = -(-2 * cp + k * m ** 2) / (2 * k * m)
        return float(a)

    if (index == 8):
        a = 2 * cp / (k * m) - m / 2
        return float(a)

    if (index == 9):
        a = pi * cp / (2 * k * m) - m / 2
        return float(a)

    if (index == 10):
        a = -(-2 * cp + k * m ** 2) / (2 * k * m)
        return float(a)

    if (index == 11):
        a = -(-4 * cp + k * m ** 2) / (2 * k * m)
        return float(a)

    if (index == 12):
        a = -(-pi * cp + k * m ** 2) / (2 * k * m)
        return float(a)

    print("a Value Incorrect, Index =", index)
    return -1

def check_constraint(ep, k, m, cp, y, index):
    e = math.e

    k = float3f(k)
    m = float3f(m)
    y = float3f(y)
    cp = float3f(cp)
    a = float3f(aValue(k, m, cp, index))

    if (k <=0):
        return -5
    if (m <=0):
        return -6
    if (y <= 0):
        return -7

    if (cp>=0):
        if a < cp:
            return -8
    else:
        if a+m > cp:
            return -8

    if (index == 1):
        if k * m >= 1:
            return -1
        limit1 = k * m * (-k * m - m * y + 1) / (2 * y)
        limit2 = -k * m * (-k * m - m * y + 1) / (2 * y)
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2
        if k > 1 - y:
            return -3
        if k > y * (e ** ep - 1):
            return -4

    if (index == 2):
        if k * m / 2 >= 1:
            return -1
        limit1 = k * m * (-k * m - 2 * m * y + 2) / (8 * y)
        limit2 = k * m * (k * m + 2 * m * y - 2) / (8 * y)
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2
        if k > 1 - y:
            return -3
        if k > y * (e ** ep - 1):
            return -4

    if (index == 3):
        if float(2 * k * m / pi) >= 1:
            return -1
        limit1 = k * m * (-2 * k * m - pi * m * y + pi) / (pi ** 2 * y)
        limit2 = k * m * (2 * k * m + pi * m * y - pi) / (pi ** 2 * y)
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2
        if k > 1 - y:
            return -3
        if k > y * (e ** ep - 1):
            return -4

    if (index == 4):
        if k * m >= 1:
            return -1
        limit1 = k * m * (-2 * k * m - m * y + 2) / (2 * y)
        limit2 = k * m * (2 * k * m + m * y - 2) / (2 * y)
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2
        limit3 = (-k * m + 1) * (e ** ep * y - k - y) / (y ** 2 * (e ** ep - 1))
        limit4 = (k * m - 1) * (e ** ep * y - k - y) / (y ** 2 * (e ** ep - 1))
        if (cp > float3f(float(limit3))) or (cp < float3f(float(limit4))):
            return -3
        if k > 1 - y:
            return -4
        if k > y * (e ** ep - 1):
            return -5

    if (index == 5):
        if k * m / 2 >= 1:
            return -1
        limit1 = k * m * (-k * m - m * y + 2) / (4 * y)
        limit2 = k * m * (k * m + m * y - 2) / (4 * y)
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2
        limit3 = (-k * m + 2) * (e ** ep * y - k - y) / (2 * y ** 2 * (e ** ep - 1))
        limit4 = (k * m - 2) * (e ** ep * y - k - y) / (2 * y ** 2 * (e ** ep - 1))
        if (cp > float3f(float(limit3))) or (cp < float3f(float(limit4))):
            return -3
        if k > 1 - y:
            return -4
        if k > y * (e ** ep - 1):
            return -5

    if (index == 6):
        if 2 * k * m / pi >= 1:
            return -1
        limit1 = k * m * (-4 * k * m - pi * m * y + 2 * pi) / (pi ** 2 * y)
        limit2 = k * m * (4 * k * m + pi * m * y - 2 * pi) / (pi ** 2 * y)
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2
        limit3 = (-2 * k * m + pi) * (e ** ep * y - k - y) / (pi * y ** 2 * (e ** ep - 1))
        limit4 = (2 * k * m - pi) * (e ** ep * y - k - y) / (pi * y ** 2 * (e ** ep - 1))
        if (cp > float3f(float(limit3))) or (cp < float3f(float(limit4))):
            return -3
        if k > 1 - y:
            return -4
        if k > y * (e ** ep - 1):
            return -5

    if (index == 7):
        if k * m >= 1:
            return -1
        limit1 = k * m * (e ** ep * (-5 * k * m + 5) - m * (4 * e ** ep * y + 1)) / (2 * (4 * e ** ep * y + 1))
        limit2 = k * m * (5 * e ** ep * (k * m - 1) + m * (4 * e ** ep * y + 1)) / (2 * (4 * e ** ep * y + 1))
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2
        if k > 1 - y:
            return -3
        if k > y * (e ** ep - 1):
            return -4

    if (index == 8):
        if k * m / 2 >= 1:
            return -1
        limit1 = -k * m * (5 * e ** ep * (k * m - 2) + 2 * m * (4 * e ** ep * y + 1)) / (32 * e ** ep * y + 8)
        limit2 = k * m * (5 * e ** ep * (k * m - 2) + 2 * m * (4 * e ** ep * y + 1)) / (8 * (4 * e ** ep * y + 1))
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2
        if k > 1 - y:
            return -3
        if k > y * (e ** ep - 1):
            return -4

    if (index == 9):
        if k * m / 2 >= 1:
            return -1
        limit1 = -k * m * (5 * e ** ep * (2 * k * m - pi) + pi * m * (4 * e ** ep * y + 1)) / (
                    pi ** 2 * (4 * e ** ep * y + 1))
        limit2 = k * m * (5 * e ** ep * (2 * k * m - pi) + pi * m * (4 * e ** ep * y + 1)) / (
                    pi ** 2 * (4 * e ** ep * y + 1))
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2
        if k > 1 - y:
            return -3
        if k > y * (e ** ep - 1):
            return -4

    if (index == 10):
        if k * m >= 1:
            return -1
        limit1 = k * m * (-3 * k * m - m * y + 3) / (2 * y)
        limit2 = k * m * (3 * k * m + m * y - 3) / (2 * y)
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2

        if -(k * (e ** ep - 1) * (k * m - 1) / y) < 0:
            return -3

        limit3 = (-2 * sqrt(6) * y ** 3 * sqrt(-k * (e ** ep - 1) * (k * m - 1) / y) + 9 * (1 - e ** ep) * (
                    -k * m + 1) ** 2) / (6 * y * (e ** ep - 1) * (k * m - 1))
        limit4 = - (-2 * sqrt(6) * y ** 3 * sqrt(-k * (e ** ep - 1) * (k * m - 1) / y) + 9 * (1 - e ** ep) * (
                    -k * m + 1) ** 2) / (6 * y * (e ** ep - 1) * (k * m - 1))
        if (cp > float3f(float(limit3))) or (cp < float3f(float(limit4))):
            return -3
        if k > 1 - y:
            return -4
        if k > y * (e ** ep - 1):
            return -5

    if (index == 11):
        if k * m / 2 >= 1:
            return -1
        limit1 = k * m * (-3 * k * m - 2 * m * y + 6) / (8 * y)
        limit2 = k * m * (3 * k * m + 2 * m * y - 6) / (8 * y)
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2

        if -(k * (e ** ep - 1) * (k * m - 2) / y) < 0:
            return -3

        limit3 = (-8 * sqrt(3) * y ** 3 * sqrt(-k * (e ** ep - 1) * (k * m - 2) / y) + 9 * (1 - e ** ep) * (
                    -k * m + 2) ** 2) / (12 * y * (e ** ep - 1) * (k * m - 2))
        limit4 = - (-8 * sqrt(3) * y ** 3 * sqrt(-k * (e ** ep - 1) * (k * m - 2) / y) + 9 * (1 - e ** ep) * (
                    -k * m + 2) ** 2) / (12 * y * (e ** ep - 1) * (k * m - 2))
        if (cp > float3f(float(limit3))) or (cp < float3f(float(limit4))):
            return -3
        if k > 1 - y:
            return -4
        if k > y * (e ** ep - 1):
            return -5

    if (index == 12):
        if 2 * k * m / pi >= 1:
            return -1
        limit1 = k * m * (-6 * k * m - pi * m * y + 3 * pi) / (pi ** 2 * y)
        limit2 = k * m * (6 * k * m + pi * m * y - 3 * pi) / (pi ** 2 * y)
        if (cp > float3f(float(limit1))) or (cp < float3f(float(limit2))):
            return -2

        if -(k * (e ** ep - 1) * (2 * k * m - pi) / y) < 0:
            return -3

        limit3 = (-2 * sqrt(6) * pi ** (3 / 2) * y ** 3 * sqrt(-k * (e ** ep - 1) * (2 * k * m - pi) / y) + 9 * (
                    1 - e ** ep) * (-2 * k * m + pi) ** 2) / (6 * pi * y * (e ** ep - 1) * (2 * k * m - pi))
        limit4 = -limit3
        if (cp > float3f(float(limit3))) or (cp < float3f(float(limit4))):
            return -3
        if k > 1 - y:
            return -4
        if k > y * (e ** ep - 1):
            return -5

    return 0

