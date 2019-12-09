# вычисление f(x)=0 методами дихотомии и простой итерации


def func(x: float) -> float:
    return 5*x**3 + 2*x**2 - 15*x - 6


def func_derivative(x: float) -> float:
    return 15*x**2 + 4*x - 15


def dichotomy_search(func, a: float, b: float, error: float) -> (float, int):
    k = 0
    while b - a > error:
        k += 1
        center = (b + a) * 0.5
        multi = func(a) * func(center)
        if multi > 0:
            a = center
        elif multi == 0:
            return center
        else:
            b = center
    return (a + b) / 2, k


def simple_iteration(func, func_derivative, derivative_extreme_points: list,
                     a: float, b: float, error: float) -> (float, int):
    derivative_values = [func_derivative(a), func_derivative(b)]
    for extremum in derivative_extreme_points:
        if contains(a, b, extremum):
            derivative_values.append(func_derivative(extremum))
    m, M = min(*derivative_values), max(*derivative_values)
    tau = -2 / (m + M)

    x0 = (a + b) * 0.5
    x1 = x0
    k = 0
    while abs(func(x1)) >= error or abs(x1 - x0) >= error:
        x0 = x1
        x1 = x0 + tau * func(x0)
        k += 1
    return x1, k


def contains(a, b, x):
    return a <= x <= b


if __name__ == "__main__":
    error = 10 ** -5
    derivative_extreme_points = [-2 / 15]  # решения f''(x) = 0
    # берем промежутки
    intervals = [
        [-2, -1], [-1, 0], [1, 2]
    ]

    dichotomy_res = []
    for interval in intervals:
        result = dichotomy_search(func, interval[0], interval[1], error)
        dichotomy_res.append(result)

    iteration_res = []
    for interval in intervals:
        result = simple_iteration(func, func_derivative, derivative_extreme_points,
                                  interval[0], interval[1], error)
        iteration_res.append(result)

    print("Dichotomy search")
    for res in dichotomy_res:
        print("{}: {:.5f}".format(res[1], res[0]))
    print("Simple iteration")
    for res in iteration_res:
        print("{}: {:.5f}".format(res[1], res[0]))



