import math
from math import pi

error = 10 ** -10


def func(N: int):
    res = 1
    for k in range(1, N + 1):
        res *= 1 + 1 / k ** 3
    return res


def find_N(error):
    true_value = math.cosh(pi * math.sqrt(3) * 0.5) / pi
    val = 1
    k = 0
    while True:
        k += 1
        val *= 1 + 1 / k ** 3
        if abs(val - true_value) < error:
            return val, true_value, k


res = find_N(error)
print(res[0])
print(res[1])
print(res[2])


