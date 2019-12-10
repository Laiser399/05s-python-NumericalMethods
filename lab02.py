# вычисление f(x)=0 методами дихотомии и простой итерации


if __name__ == "__main__":
    from lab02_data import error, derivative_extreme_points, intervals
    from lab02_data import func, func_derivative
    from lab02_solveModule import dichotomy_search, simple_iteration

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



