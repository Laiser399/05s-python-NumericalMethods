from math import pow


def solveByTrapezoid(a: float, b: float, func, error: float) -> float:
    n = findSplitsCount(b - a, 2, error)
    step = (b - a) / n

    x, res = a, 0
    for i in range(n):
        res += (func(x) + func(x + step)) * 0.5 * step
        x += step
    return res


def solveBySimpson(a: float, b: float, func, error: float) -> float:
    n = findSplitsCount(b - a, 4, error)
    n = n * 2 if n % 2 != 0 else n
    step = (b - a) / n

    x, res = a, 0
    for i in range(n // 2):
        res += func(x) + 4*func(x + step) + func(x + 2*step)
        x += 2 * step
    return res * step / 3


def findSplitsCount(interval: float, r: int, error: float) -> int:
    res = 1
    error = error * 2**r
    while pow(interval, 2) >= error:
        interval /= 2
        res *= 2
    return res

