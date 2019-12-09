# вычисление неберущихся определенных интегралов методами Симпсона и трапеции


if __name__ == "__main__":
    from lab05_data import a, b, func, error
    from lab05_solveModule import solveBySimpson, solveByTrapezoid

    res = solveByTrapezoid(a, b, func, error)
    print("Trapezoid method: {:.4f}".format(res))

    res = solveBySimpson(a, b, func, error)
    print("Simpson method: {:.4f}".format(res))



