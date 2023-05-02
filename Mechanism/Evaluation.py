from Mechanism.Constraints import *

# The Theoretical Variance (which is relevant to parameter k, m, y) of the Proposed Mechanism is as follows:
def perturbation_fun_var(ep, k, m, y, cp, index):
    e = math.e
    k = float3f(k)
    m = float3f(m)
    y = float3f(y)
    cp = float3f(cp)

    if check_constraint(ep, k, m, cp, y, index) != 0:
        #        print("Constraint Errors")
        return -1

    if (index == 1):
        variance = -cp ** 2 + cp ** 2 / (k * m) - k ** 3 * m ** 3 / (12 * y ** 2) + k ** 2 * m ** 2 / (
                    4 * y ** 2) + k * m ** 3 / 12 - k * m / (4 * y ** 2) + 1 / (12 * y ** 2)
        return variance
    if (index == 2):
        variance = -cp ** 2 + 2 * cp ** 2 / (k * m) - k ** 3 * m ** 3 / (96 * y ** 2) + k ** 2 * m ** 2 / (
                    16 * y ** 2) + k * m ** 3 / 48 - k * m / (8 * y ** 2) + 1 / (12 * y ** 2)
        return variance
    if (index == 3):
        variance = -cp ** 2 - 4 * k * m ** 3 / pi ** 3 - (2 * k * m - pi) ** 3 / (12 * pi ** 3 * y ** 2) + (
                    pi * cp - k * m ** 2) ** 2 / (4 * pi * k * m) + (pi * cp + k * m ** 2) ** 2 / (4 * pi * k * m)
        return float(variance)
    if (index == 4):
        variance = 0
        if (cp >= 0):
            variance = -cp ** 2 + cp ** 2 / (k * m) - k ** 3 * m ** 3 / (6 * y ** 2) + k ** 2 * m ** 2 / (
                        2 * y ** 2) + k * m ** 3 / 12 - k * m / (2 * y ** 2) + 1 / (6 * y ** 2)
        else:
            variance = -cp ** 2 + cp ** 2 / (k * m) - k ** 3 * m ** 3 / (6 * y ** 2) + k ** 2 * m ** 2 / (
                        2 * y ** 2) + k * m ** 3 / 12 - k * m / (2 * y ** 2) + 1 / (6 * y ** 2)

        return float(variance)

    if (index == 5):
        variance = 0
        if (cp >= 0):
            variance = -cp ** 2 + 2 * cp ** 2 / (k * m) - k ** 3 * m ** 3 / (48 * y ** 2) + k ** 2 * m ** 2 / (
                        8 * y ** 2) + k * m ** 3 / 48 - k * m / (4 * y ** 2) + 1 / (6 * y ** 2)
        else:
            variance = -cp ** 2 + 2 * cp ** 2 / (k * m) - k ** 3 * m ** 3 / (48 * y ** 2) + k ** 2 * m ** 2 / (
                        8 * y ** 2) + k * m ** 3 / 48 - k * m / (4 * y ** 2) + 1 / (6 * y ** 2)

        return float(variance)

    if (index == 6):
        variance = 0
        if (cp >= 0):
            variance = -cp ** 2 + pi * cp ** 2 / (2 * k * m) - 4 * k ** 3 * m ** 3 / (
                        3 * pi ** 3 * y ** 2) + 2 * k ** 2 * m ** 2 / (
                                   pi ** 2 * y ** 2) - 4 * k * m ** 3 / pi ** 3 + k * m ** 3 / (2 * pi) - k * m / (
                                   pi * y ** 2) + 1 / (6 * y ** 2)
        else:
            variance = -cp ** 2 + pi * cp ** 2 / (2 * k * m) - 4 * k ** 3 * m ** 3 / (
                        3 * pi ** 3 * y ** 2) + 2 * k ** 2 * m ** 2 / (
                                   pi ** 2 * y ** 2) - 4 * k * m ** 3 / pi ** 3 + k * m ** 3 / (2 * pi) - k * m / (
                                   pi * y ** 2) + 1 / (6 * y ** 2)
        return float(variance)

    if (index == 7):
        variance = -cp ** 2 - 125 * e ** (3 * ep) * y * (k * m - 1) ** 3 / (
                    21 * (4 * e ** ep * y + 1) ** 3) - 125 * e ** (2 * ep) * (k * m - 1) ** 3 / (
                               28 * (4 * e ** ep * y + 1) ** 3) - (2 * cp - k * m ** 2) ** 3 / (
                               24 * k ** 2 * m ** 3) + (2 * cp + k * m ** 2) ** 3 / (24 * k ** 2 * m ** 3)
        return variance

    if (index == 8):
        variance = -16 * cp ** 4 / (3 * k ** 3 * m ** 5) - cp ** 2 + cp * (4 * cp - k * m ** 2) ** 3 / (
                    6 * k ** 3 * m ** 5) + cp * (4 * cp + k * m ** 2) ** 3 / (6 * k ** 3 * m ** 5) - 125 * e ** (
                               3 * ep) * y * (k * m - 2) ** 3 / (168 * (4 * e ** ep * y + 1) ** 3) - 125 * e ** (
                               2 * ep) * (k * m - 2) ** 3 / (224 * (4 * e ** ep * y + 1) ** 3) - (
                               4 * cp - k * m ** 2) ** 3 / (24 * k ** 2 * m ** 3) + (4 * cp + k * m ** 2) ** 3 / (
                               24 * k ** 2 * m ** 3) - (4 * cp - k * m ** 2) ** 4 / (32 * k ** 3 * m ** 5) - (
                               4 * cp + k * m ** 2) ** 4 / (32 * k ** 3 * m ** 5)
        return variance

    if (index == 9):
        variance = (-5376 * pi ** 3 * cp ** 2 * e ** (3 * ep) * k * m * y ** 3 + 2688 * pi ** 4 * cp ** 2 * e ** (
                    3 * ep) * y ** 3 - 4032 * pi ** 3 * cp ** 2 * e ** (
                                2 * ep) * k * m * y ** 2 + 2016 * pi ** 4 * cp ** 2 * e ** (
                                2 * ep) * y ** 2 - 1008 * pi ** 3 * cp ** 2 * e ** ep * k * m * y + 504 * pi ** 4 * cp ** 2 * e ** ep * y - 84 * pi ** 3 * cp ** 2 * k * m + 42 * pi ** 4 * cp ** 2 - 4000 * e ** (
                                3 * ep) * k ** 4 * m ** 4 * y + 6000 * pi * e ** (
                                3 * ep) * k ** 3 * m ** 3 * y - 21504 * e ** (
                                3 * ep) * k ** 2 * m ** 4 * y ** 3 + 2688 * pi ** 2 * e ** (
                                3 * ep) * k ** 2 * m ** 4 * y ** 3 - 3000 * pi ** 2 * e ** (
                                3 * ep) * k ** 2 * m ** 2 * y + 500 * pi ** 3 * e ** (
                                3 * ep) * k * m * y - 3000 * e ** (2 * ep) * k ** 4 * m ** 4 + 4500 * pi * e ** (
                                2 * ep) * k ** 3 * m ** 3 - 16128 * e ** (
                                2 * ep) * k ** 2 * m ** 4 * y ** 2 + 2016 * pi ** 2 * e ** (
                                2 * ep) * k ** 2 * m ** 4 * y ** 2 - 2250 * pi ** 2 * e ** (
                                2 * ep) * k ** 2 * m ** 2 + 375 * pi ** 3 * e ** (
                                2 * ep) * k * m - 4032 * e ** ep * k ** 2 * m ** 4 * y + 504 * pi ** 2 * e ** ep * k ** 2 * m ** 4 * y - 336 * k ** 2 * m ** 4 + 42 * pi ** 2 * k ** 2 * m ** 4) / (
                               84 * pi ** 3 * k * m * (
                                   64 * e ** (3 * ep) * y ** 3 + 48 * e ** (2 * ep) * y ** 2 + 12 * e ** ep * y + 1))
        return float(variance)

    if (index == 10):
        variance = 0
        if (cp >= 0):
            variance = -cp ** 2 + cp ** 2 / (k * m) - 9 * k ** 3 * m ** 3 / (40 * y ** 2) + 27 * k ** 2 * m ** 2 / (
                        40 * y ** 2) + k * m ** 3 / 12 - 27 * k * m / (40 * y ** 2) + 9 / (40 * y ** 2)
        else:
            variance = -cp ** 2 + cp ** 2 / (k * m) - 9 * k ** 3 * m ** 3 / (40 * y ** 2) + 27 * k ** 2 * m ** 2 / (
                        40 * y ** 2) + k * m ** 3 / 12 - 27 * k * m / (40 * y ** 2) + 9 / (40 * y ** 2)

        return float(variance)

    if (index == 11):
        variance = 0
        if (cp >= 0):
            variance = -cp ** 2 + 2 * cp ** 2 / (k * m) - 9 * k ** 3 * m ** 3 / (
                        320 * y ** 2) + 27 * k ** 2 * m ** 2 / (160 * y ** 2) + k * m ** 3 / 48 - 27 * k * m / (
                                   80 * y ** 2) + 9 / (40 * y ** 2)
        else:
            variance = -cp ** 2 + 2 * cp ** 2 / (k * m) - 9 * k ** 3 * m ** 3 / (
                        320 * y ** 2) + 27 * k ** 2 * m ** 2 / (160 * y ** 2) + k * m ** 3 / 48 - 27 * k * m / (
                                   80 * y ** 2) + 9 / (40 * y ** 2)

        return float(variance)

    if (index == 12):
        variance = 0
        if (cp >= 0):
            variance = -cp ** 2 + pi * cp ** 2 / (2 * k * m) - 9 * k ** 3 * m ** 3 / (
                        5 * pi ** 3 * y ** 2) + 27 * k ** 2 * m ** 2 / (
                                   10 * pi ** 2 * y ** 2) - 4 * k * m ** 3 / pi ** 3 + k * m ** 3 / (
                                   2 * pi) - 27 * k * m / (20 * pi * y ** 2) + 9 / (40 * y ** 2)
        else:
            variance = -cp ** 2 + pi * cp ** 2 / (2 * k * m) - 9 * k ** 3 * m ** 3 / (
                        5 * pi ** 3 * y ** 2) + 27 * k ** 2 * m ** 2 / (
                                   10 * pi ** 2 * y ** 2) - 4 * k * m ** 3 / pi ** 3 + k * m ** 3 / (
                                   2 * pi) - 27 * k * m / (20 * pi * y ** 2) + 9 / (40 * y ** 2)
        return float(variance)

    print("Index Errors")
    return -2

def H1Rate(ep, k, m, y, index):
    e = math.e
    k = float3f(k)
    m = float3f(m)
    y = float3f(y)
    L = LValue(ep, k, m, y, index)

    if (k < 0 or m < 0):
        print("H1_Rate Incorrect")
        return -1

    # R1 = s1/s2

    if (index == 1):
        s1 = k * m
        s2 = 2 * y * L
        R1 = s2 / s1
        return float(R1)

    if (index == 2):
        s1 = k * m / 2
        s2 = 2 * y * L
        R1 = s2 / s1
        return float(R1)

    if (index == 3):
        s1 = 2 * k * m / pi
        s2 = 2 * y * L
        R1 = s2 / s1
        return float(R1)

    if (index == 4):
        s1 = k * m
        s2 = y * L
        R1 = s2 / s1
        return float(R1)

    if (index == 5):
        s1 = k * m / 2
        s2 = y * L
        R1 = s2 / s1
        return float(R1)

    if (index == 6):
        s1 = 2 * k * m / pi
        s2 = y * L
        R1 = s2 / s1
        return float(R1)

    if (index == 7):
        s1 = k * m
        s2 = L * (8 * y + 2 * e ** (-ep)) / 5
        R1 = s2 / s1
        return float(R1)

    if (index == 8):
        s1 = k * m / 2
        s2 = L * (8 * y + 2 * e ** (-ep)) / 5
        R1 = s2 / s1
        return float(R1)

    if (index == 9):
        s1 = 2 * k * m / pi
        s2 = L * (8 * y + 2 * e ** (-ep)) / 5
        R1 = s2 / s1
        return float(R1)

    if (index == 10):
        s1 = k * m
        s2 = 2 * L * y / 3
        R1 = s2 / s1
        return float(R1)

    if (index == 11):
        s1 = k * m / 2
        s2 = 2 * L * y / 3
        R1 = s2 / s1
        return float(R1)

    if (index == 12):
        s1 = 2 * k * m / pi
        s2 = 2 * L * y / 3
        R1 = s2 / s1
        return float(R1)

    print("H1_Rate Incorrect")
    return -1

def H2Rate(ep, cp, k, m, y, index):
    if (k <= 0 or m <= 0):
        print("H2_Rate Incorrect")
        return -1

    e = math.e
    k = float3f(k)
    m = float3f(m)
    y = float3f(y)
    L = LValue(ep, k, m, y, index)

    if (index == 1):
        return 1

    if (index == 2):
        return 1

    if (index == 3):
        return 1

    if (index == 4):
        if cp>=0:
            if (3*cp-L)/4 > 0:
                h2_rate = 3*(9*L**2 + 2*L*cp - 7*cp**2)/(15*L**2 + 30*L*cp - 17*cp**2)
                return float(h2_rate)
            else:
                h2_rate = 3*(7*L**2 + 14*L*cp - 25*cp**2)/(15*L**2 + 30*L*cp - 17*cp**2)
                return float(h2_rate)
        else:
            if (3*cp+L)/4 < 0:
                h2_rate = 3*(9*L**2 - 2*L*cp - 7*cp**2)/(15*L**2 - 30*L*cp - 17*cp**2)
                return float(h2_rate)
            else:
                h2_rate = 3*(7*L**2 - 14*L*cp - 25*cp**2)/(15*L**2 - 30*L*cp - 17*cp**2)
                return float(h2_rate)

    if (index == 5):
        if cp>=0:
            if (3*cp-L)/4 > 0:
                h2_rate = 3*(9*L**2 + 2*L*cp - 7*cp**2)/(15*L**2 + 30*L*cp - 17*cp**2)
                return float(h2_rate)
            else:
                h2_rate = 3*(7*L**2 + 14*L*cp - 25*cp**2)/(15*L**2 + 30*L*cp - 17*cp**2)
                return float(h2_rate)
        else:
            if (3*cp+L)/4 < 0:
                h2_rate = 3*(9*L**2 - 2*L*cp - 7*cp**2)/(15*L**2 - 30*L*cp - 17*cp**2)
                return float(h2_rate)
            else:
                h2_rate = 3*(7*L**2 - 14*L*cp - 25*cp**2)/(15*L**2 - 30*L*cp - 17*cp**2)
                return float(h2_rate)

    if (index == 6):
        if cp>=0:
            if (3*cp-L)/4 > 0:
                h2_rate = 3*(9*L**2 + 2*L*cp - 7*cp**2)/(15*L**2 + 30*L*cp - 17*cp**2)
                return float(h2_rate)
            else:
                h2_rate = 3*(7*L**2 + 14*L*cp - 25*cp**2)/(15*L**2 + 30*L*cp - 17*cp**2)
                return float(h2_rate)
        else:
            if (3*cp+L)/4 < 0:
                h2_rate = 3*(9*L**2 - 2*L*cp - 7*cp**2)/(15*L**2 - 30*L*cp - 17*cp**2)
                return float(h2_rate)
            else:
                h2_rate = 3*(7*L**2 - 14*L*cp - 25*cp**2)/(15*L**2 - 30*L*cp - 17*cp**2)
                return float(h2_rate)

    if (index == 7):
        if cp>=0:
            h2_rate = 3*(1280*L**4*e**ep*y*(L + cp) + 1024*cp**5*(-e**ep*y + 1) + (L - 3*cp)**5*(-e**ep*y + 1))/(3840*L**4*e**ep*y*(L + cp) - 1024*cp**5*(e**ep*y - 1) - (3*L - cp)**5*(e**ep*y - 1))
            return float(h2_rate)
        else:
            h2_rate = 3*(1280*L**4*e**ep*y*(-L + cp) + 1024*cp**5*(-e**ep*y + 1) + (L + 3*cp)**5*(e**ep*y - 1))/(3840*L**4*e**ep*y*(-L + cp) - 1024*cp**5*(e**ep*y - 1) + (3*L + cp)**5*(e**ep*y - 1))
            return float(h2_rate)

    if (index == 8):
        if cp>=0:
            h2_rate = 3*(1280*L**4*e**ep*y*(L + cp) + 1024*cp**5*(-e**ep*y + 1) + (L - 3*cp)**5*(-e**ep*y + 1))/(3840*L**4*e**ep*y*(L + cp) - 1024*cp**5*(e**ep*y - 1) - (3*L - cp)**5*(e**ep*y - 1))
            return float(h2_rate)
        else:
            h2_rate = 3*(1280*L**4*e**ep*y*(-L + cp) + 1024*cp**5*(-e**ep*y + 1) + (L + 3*cp)**5*(e**ep*y - 1))/(3840*L**4*e**ep*y*(-L + cp) - 1024*cp**5*(e**ep*y - 1) + (3*L + cp)**5*(e**ep*y - 1))
            return float(h2_rate)

    if (index == 9):
        if cp>=0:
            h2_rate = 3*(1280*L**4*e**ep*y*(L + cp) + 1024*cp**5*(-e**ep*y + 1) + (L - 3*cp)**5*(-e**ep*y + 1))/(3840*L**4*e**ep*y*(L + cp) - 1024*cp**5*(e**ep*y - 1) - (3*L - cp)**5*(e**ep*y - 1))
            return float(h2_rate)
        else:
            h2_rate = 3*(1280*L**4*e**ep*y*(-L + cp) + 1024*cp**5*(-e**ep*y + 1) + (L + 3*cp)**5*(e**ep*y - 1))/(3840*L**4*e**ep*y*(-L + cp) - 1024*cp**5*(e**ep*y - 1) + (3*L + cp)**5*(e**ep*y - 1))
            return float(h2_rate)

    if (index == 10):
        if cp>=0:
            if (3*cp-L)/4 > 0:
                h2_rate = (61*L**3 - 33*L**2*cp - 57*L*cp**2 + 37*cp**3)/(21*L**3 + 63*L**2*cp - 65*L*cp**2 + 21*cp**3)
                return float(h2_rate)
            else:
                h2_rate = (37*L**3 + 111*L**2*cp - 273*L*cp**2 + 37*cp**3)/(21*L**3 + 63*L**2*cp - 65*L*cp**2 + 21*cp**3)
                return float(h2_rate)
        else:
            if (3*cp+L)/4 < 0:
                h2_rate = (61*L**3 + 33*L**2*cp - 57*L*cp**2 - 37*cp**3)/(21*L**3 - 63*L**2*cp - 65*L*cp**2 - 21*cp**3)
                return float(h2_rate)
            else:
                h2_rate = (37*L**3 - 111*L**2*cp - 273*L*cp**2 - 37*cp**3)/(21*L**3 - 63*L**2*cp - 65*L*cp**2 - 21*cp**3)
                return float(h2_rate)

    if (index == 11):
        if cp>=0:
            if (3*cp-L)/4 > 0:
                h2_rate = (61*L**3 - 33*L**2*cp - 57*L*cp**2 + 37*cp**3)/(21*L**3 + 63*L**2*cp - 65*L*cp**2 + 21*cp**3)
                return float(h2_rate)
            else:
                h2_rate = (37*L**3 + 111*L**2*cp - 273*L*cp**2 + 37*cp**3)/(21*L**3 + 63*L**2*cp - 65*L*cp**2 + 21*cp**3)
                return float(h2_rate)
        else:
            if (3*cp+L)/4 < 0:
                h2_rate = (61*L**3 + 33*L**2*cp - 57*L*cp**2 - 37*cp**3)/(21*L**3 - 63*L**2*cp - 65*L*cp**2 - 21*cp**3)
                return float(h2_rate)
            else:
                h2_rate = (37*L**3 - 111*L**2*cp - 273*L*cp**2 - 37*cp**3)/(21*L**3 - 63*L**2*cp - 65*L*cp**2 - 21*cp**3)
                return float(h2_rate)

    if (index == 12):
        if cp>=0:
            if (3*cp-L)/4 > 0:
                h2_rate = (61*L**3 - 33*L**2*cp - 57*L*cp**2 + 37*cp**3)/(21*L**3 + 63*L**2*cp - 65*L*cp**2 + 21*cp**3)
                return float(h2_rate)
            else:
                h2_rate = (37*L**3 + 111*L**2*cp - 273*L*cp**2 + 37*cp**3)/(21*L**3 + 63*L**2*cp - 65*L*cp**2 + 21*cp**3)
                return float(h2_rate)
        else:
            if (3*cp+L)/4 < 0:
                h2_rate = (61*L**3 + 33*L**2*cp - 57*L*cp**2 - 37*cp**3)/(21*L**3 - 63*L**2*cp - 65*L*cp**2 - 21*cp**3)
                return float(h2_rate)
            else:
                h2_rate = (37*L**3 - 111*L**2*cp - 273*L*cp**2 - 37*cp**3)/(21*L**3 - 63*L**2*cp - 65*L*cp**2 - 21*cp**3)
                return float(h2_rate)

    print("H2_Rate Incorrect")
    return -1

def reduceRate(var1,var2):
    rate = (var1 - var2)/var1
    return float(rate)