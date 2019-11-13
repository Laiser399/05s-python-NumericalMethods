

def solveBySimpson(a: float, b: float, func) -> float:
    return (b - a) / 6 * (func(a) + 4 * func((a + b) / 2) + func(b))



