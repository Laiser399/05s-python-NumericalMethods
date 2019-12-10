# вычисление системы уравнений методом Ньютона (производные находятся вручную и программно)


if __name__ == "__main__":
    from lab03_data import error, x0, y0
    from lab03_data import f, g, df_dx, df_dy, dg_dx, dg_dy
    from lab03_solveModule import solveWithDerivatives, solve

    x, y, iterations = solveWithDerivatives(x0, y0, error, f, g, df_dx, df_dy, dg_dx, dg_dy)
    print("Analytical solve:")
    print("x = {:.5f}".format(x))
    print("y = {:.5f}".format(y))
    print("Iterations count: {}".format(iterations))

    h = 10**-3
    x, y, iterations = solve(x0, y0, error, f, g, h)
    print("Program solve:")
    print("x = {:.5f}".format(x))
    print("y = {:.5f}".format(y))
    print("Iterations count: {}".format(iterations))

