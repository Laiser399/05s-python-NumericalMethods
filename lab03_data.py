from math import sqrt, asin

error = 10**-5
x0, y0 = -1, 1


def f(x: float, y: float) -> float:
    return x + 2*y + asin(x*y + 1)


def g(x: float, y: float) -> float:
    return x*x - y*y - 1


def df_dx(x: float, y: float) -> float:
    xy = x*y
    return y / sqrt(-xy*xy - 2*xy) + 1


def df_dy(x: float, y: float) -> float:
    xy = x*y
    return x / sqrt(-xy*xy - 2*xy) + 2


def dg_dx(x: float, y: float) -> float:
    return 2*x


def dg_dy(x: float, y: float) -> float:
    return -2*y
