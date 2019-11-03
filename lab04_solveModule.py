from numpy.linalg import norm
from numpy import ndarray, array
import numpy


def solveByGauss(A: ndarray, f: ndarray):
    def firstNotNullIndex(matrix: ndarray, startRow: int, column: int):
        for i in range(startRow, len(matrix)):
            if matrix[i][column] != 0:
                return i
        return -1

    def swapRows(matrix: ndarray, index1: int, index2: int):
        if index1 == index2:
            return
        row1 = matrix[index1]
        matrix[index1] = matrix[index2]
        matrix[index2] = row1

    A = numpy.column_stack((A, f))
    # прямой ход
    for i in range(len(A)):
        index = firstNotNullIndex(A, i, i)
        swapRows(A, i, index)
        A[i] /= A[i][i]
        currentRow = A[i]
        for j in range(i + 1, len(A)):
            A[j] -= currentRow / currentRow[i] * A[j][i]
    # обратный ход
    for i in reversed(range(len(A))):
        for j in range(i):
            A[j] -= A[i] * A[j][i]
    return A[:, len(A)]


def solveByDescent(A: ndarray, f: ndarray, x0: ndarray, error: float) -> (ndarray, int, []):
    def isEndCondition(x0: ndarray, x1: ndarray, r1: ndarray, error: float) -> bool:
        return norm(x1 - x0, ord=2) < error and norm(r1, ord=2) < error

    A_transposed = A.transpose()
    A_norm = A_transposed.dot(A)
    f_norm = A_transposed.dot(f)

    x1 = x0
    r0 = A_norm.dot(x0) - f_norm
    r1 = r0

    iter_error = 10 ** -2
    k = 0
    intermediate_data = []
    while True:
        if isEndCondition(x0, x1, r1, iter_error):
            intermediate_data.append((iter_error, x1, k))
            iter_error *= 0.1
            if iter_error <= error:
                return x1, k, intermediate_data

        k += 1
        tau = (r0*r0).sum() / (A_norm.dot(r0) * r0).sum()
        x0, r0 = x1, r1
        x1 = x0 - tau * r0
        r1 = A_norm.dot(x1) - f_norm




