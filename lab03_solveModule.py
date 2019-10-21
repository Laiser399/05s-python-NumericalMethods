from math import sqrt


def solve(x0: float, y0: float, error: float, f, g, h: float) -> (float, float, int):
    df_dx = createDerivativeByX(f, h)
    df_dy = createDerivativeByY(f, h)
    dg_dx = createDerivativeByX(g, h)
    dg_dy = createDerivativeByY(g, h)
    return solveWithDerivatives(x0, y0, error, f, g, df_dx, df_dy, dg_dx, dg_dy)


def solveWithDerivatives(x0: float, y0: float, error: float, f, g, df_dx, df_dy, dg_dx, dg_dy) -> (float, float, int):
    x1, y1 = x0, y0
    k = 0
    while not isEndCondition(f, g, error, x0, y0, x1, y1):
        k += 1
        x0, y0 = x1, y1
        fraction1 = calcFirstFraction(f, g, df_dx, df_dy, dg_dx, dg_dy, x0, y0)
        fraction2 = calcSecondFraction(f, g, df_dx, df_dy, dg_dx, dg_dy, x0, y0)
        x1 = x0 - fraction1
        y1 = y0 - fraction2
    return x1, y1, k


def createDerivativeByX(f, h: float):
    def derivative(x: float, y: float) -> float:
        return (f(x + h, y) - f(x, y)) / h
    return derivative


def createDerivativeByY(f, h: float):
    def derivative(x: float, y: float) -> float:
        return (f(x, y + h) - f(x, y)) / h
    return derivative


def isEndCondition(f, g, error: float, x0: float, y0: float, x1: float, y1: float) -> bool:
    return sqrt(pow(f(x1, y1), 2) + pow(g(x1, y1), 2)) < error and \
           sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2)) < error


def calcFirstFraction(f, g, df_dx, df_dy, dg_dx, dg_dy, x: float, y: float) -> float:
    a, b, c, d = calcFunctions(x, y, df_dx, df_dy, dg_dx, dg_dy)
    f_xy, g_xy = calcFunctions(x, y, f, g)
    return (d*f_xy - b*g_xy) / (a*d - b*c)


def calcSecondFraction(f, g, df_dx, df_dy, dg_dx, dg_dy, x: float, y: float) -> float:
    a, b, c, d = calcFunctions(x, y, df_dx, df_dy, dg_dx, dg_dy)
    f_xy, g_xy = calcFunctions(x, y, f, g)
    return (a*g_xy - c*f_xy) / (a * d - b * c)


def calcFunctions(x: float, y: float, *functions) -> []:
    res = []
    for func in functions:
        res.append(func(x, y))
    return res
