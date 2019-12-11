error = 10 ** -5
derivative_extreme_points = [-2 / 15]  # решения f''(x) = 0
intervals = [
    [-2, -1], [-1, 0], [1.7, 1.8]
]


def func(x: float) -> float:
    return 5*x**3 + 2*x**2 - 15*x - 6


def func_derivative(x: float) -> float:
    return 15*x**2 + 4*x - 15
