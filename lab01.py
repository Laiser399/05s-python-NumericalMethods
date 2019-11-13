# найти N для ряда, чтобы погрешность была меньше заданной

from math import pi, cosh, sqrt

error = 10 ** -10


def func(N: int):
    res = 1
    for k in range(1, N + 1):
        res *= 1 + 1 / k**3
    return res


def find_N(error):
    true_value = cosh(pi * sqrt(3) * 0.5) / pi
    val = 1
    k = 0
    while True:
        k += 1
        val *= 1 + 1 / k**3
        if abs(val - true_value) < error:
            return val, true_value, k


if __name__ == "__main__":
    res = find_N(error)
    print("Result:     {}".format("{:.10f}".format(res[0])))
    print("            {}".format(res[0]))
    print("True value: {}".format(res[1]))
    print("Error:      {}".format(error))
    print("K:          {}".format(res[2]))


