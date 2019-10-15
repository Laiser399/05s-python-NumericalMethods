

def func(x: float) -> float:
    return 5*x**3 + 2*x**2 - 15*x - 6


def func_derivative(x: float) -> float:
    return 15*x**2 + 4*x - 15


def dichotomy_search(func, a: float, b: float, error: float) -> float:
    if a >= b or func(a) * func(b) >= 0 or error <= 0:
        raise ValueError

    while abs(b - a) > error:
        center = (b + a) * 0.5
        multi = func(a) * func(center)
        if multi > 0:
            a = center
        elif multi == 0:
            return center
        else:
            b = center
    return (a + b) / 2


def simple_iteration(func, func_derivative, derivative_extreme_points: list, a: float,
                     b: float, n: int) -> float:
    derivative_values = [func_derivative(a), func_derivative(b)]
    for extremum in derivative_extreme_points:
        if contains(a, b, extremum):
            derivative_values.append(func_derivative(extremum))
    m, M = min(*derivative_values), max(*derivative_values)
    tau = -2 / (m + M)
    x = (a + b) * 0.5
    for i in range(n):
        x = x + tau * func(x)
    return x


def contains(a, b, x):
    return a <= x <= b


if __name__ == "__main__":
    error = 10 ** -5
    derivative_extreme_points = [-2 / 15]  # решения f''(x) = 0
    # берем промежутки
    intervals = [
        [-2, -1], [-1, 0], [0, 2]
    ]

    dichotomy_res = []
    for interval in intervals:
        result = dichotomy_search(func, interval[0], interval[1], error)
        dichotomy_res.append(result)

    iteration_res = []
    for interval in intervals:
        result = simple_iteration(func, func_derivative, derivative_extreme_points,
                                  interval[0], interval[1], 30)  # TODO remove n
        iteration_res.append(result)

    print(dichotomy_res)
    print(iteration_res)



