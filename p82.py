import numpy as np
matrix = np.loadtxt('data/p82.txt', dtype=int, delimiter=',')


def p82(matrix):

    m = matrix.shape[0]
    n = matrix.shape[1]
    D = matrix.copy()

    # dynamic programming, similar approach to p67.
    # (this particular way relies on no right moves)
    for j in range(1, n):
        
        # left
        for i in range(m):
            D[i, j] = matrix[i, j] + D[i, j - 1]

        # down
        for i in range(1, m):
            D[i, j] = min(D[i, j], D[i - 1, j] + matrix[i, j])
        
        # up
        for i in range(m - 2, -1, -1):
            D[i, j] = min(D[i, j], D[i + 1, j] + matrix[i, j])
        
    return np.min(D[:, n - 1])


print(p82(matrix))