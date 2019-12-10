# вычисление СЛАУ методами Гаусса, наискорейшего спуска и сопряженных градиентов
from numpy import array, ndarray

float_template = "{:.7f}"


def formatX(arr: ndarray, template: str):
    vector = arr.transpose()[0]
    res = ""
    for val in vector:
        if len(res) != 0:
            res += ", "
        res += template.format(val)
    return res


def formatVector(vector: list) -> str:
    res = ""
    for val in vector:
        if len(res) != 0:
            res += ", "
        res += str(val)
    return res


if __name__ == "__main__":
    from lab04_solveModule import solveByGauss, solveByDescent, solveByConjugateGradient
    from lab04_data import A, f, error, x0

    res = solveByGauss(A, f)
    print("Gauss method")
    print("X=({})\n".format(formatVector(res)))

    res = solveByDescent(A, f, x0, error)
    print("Steepest descent method")
    print("X=({})   n={}".format(formatX(res[0], float_template), res[1]))
    for tuple in res[2]:
        print("E={}   X=({})   n(E)={}".format(float_template.format(tuple[0]),
                                               formatX(tuple[1], float_template), tuple[2]))

    res = solveByConjugateGradient(A, f, x0)
    print("\nConjugate gradient method")
    print("X=({})".format(formatVector(res[0].transpose()[0])))
    for iterData in res[1]:
        print("E={}   X=({})   n(E)={}".format(
            float_template.format(iterData[0]),
            formatX(iterData[1], float_template),
            iterData[2])
        )









