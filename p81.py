import numpy as np
matrix = np.loadtxt('data/p81.txt', dtype=int, delimiter=',')


def p81(matrix):

    m = matrix.shape[0]
    n = matrix.shape[1]
    D = matrix.copy()

    # can only get to the 0th row and 0th column one way
    D[0, :] = np.cumsum(D[0, :])
    D[:, 0] = np.cumsum(D[:, 0])

    for i in range(1, m):
        for j in range(1, n):
            D[i, j] += min(D[i - 1, j], D[i, j - 1])
        
    return D[m - 1, n - 1]


print(p81(matrix))