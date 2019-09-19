



error = 10 ** -5




def func(x: float):
    return 5*x**3 + 2*x**2 - 15*x - 6

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

print(dichotomy_search(func, -2, -1, error))
print(dichotomy_search(func, -1, 0, error))
print(dichotomy_search(func, 0, 2, error))


