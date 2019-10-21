

if __name__ == "__main__":
    from lab03_func import f, g, df_dx, df_dy, dg_dx, dg_dy
    from lab03_solveModule import solveWithDerivatives, solve

    error = 10**-5
    x0, y0 = -1, 1
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

