# вычисление неберущихся определенных интегралов методами Симпсона и трапеции


if __name__ == "__main__":
    from lab05_data import a, b, func, error
    from lab05_solveModule import solveBySimpson, solveByTrapezoid

    res, n = solveByTrapezoid(a, b, func, error)
    print("Trapezoid method: {:.5f}".format(res))
    print("Intervals count: {}\n".format(n))

    res, n = solveBySimpson(a, b, func, error)
    print("Simpson method: {:.5f}".format(res))
    print("Intervals count: {}\n".format(n))
