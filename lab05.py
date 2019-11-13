# вычисление неберущихся определенных интегралов методами Симпсона и трапеции


if __name__ == "__main__":
    from lab05_data import a, b, func
    from lab05_solveModule import solveBySimpson

    res = solveBySimpson(a, b, func)
    print(res)



