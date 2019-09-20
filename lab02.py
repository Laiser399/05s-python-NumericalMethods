



error = 10 ** -5




def func(x: float):
    return 5*x**3 + 2*x**2 - 15*x - 6

def func_derivative(x: float):
    return 15*x**2 + 4*x - 15

def dichotomy_search(func, a: float, b: float, error: float):
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


def simple_iteration(func, t: float, x_0: float, n: int):
    x = x_0
    for i in range(n):
        x = x + t * func(x)
    return x


res1 = [
    dichotomy_search(func, -2, -1, error),
    dichotomy_search(func, -1, 0, error),
    dichotomy_search(func, 0, 2, error),
]

res2 = [
    simple_iteration(func, -2 / (func_derivative(-2) + func_derivative(-1.5)), -1.9, 20),
    simple_iteration(func, -2 / (func_derivative(-1) + func_derivative(0)), -0.5, 20),
    simple_iteration(func, -2 / (func_derivative(1) + func_derivative(2)), 1.5, 20)
]

print(res1)
print(res2)



