import numpy as np


def p18():
    triangle = np.loadtxt('data/p18.txt', dtype=int)
    n = triangle.shape[0]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            triangle[i, j] += max(triangle[i + 1, j], triangle[i + 1, j + 1])
    return triangle[0, 0]


print(p18())