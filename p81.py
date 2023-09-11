<<<<<<< Updated upstream
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
=======
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
import numpy as np

def p81():
    mat = np.loadtxt('data/p81.txt', delimiter=',')
    visited = np.zeros(mat.shape)
    distances = np.full(mat.shape, np.inf)
    distances[0, 0] = mat[0, 0]
    i = 0
    j = 0
    while visited[-1, -1] == 0:
        # check down
        if i < (mat.shape[0] - 1) and visited[i+1, j] == 0:
            distances[i+1, j] = min(distances[i+1, j], distances[i, j] + mat[i+1, j])
        # check right
        if j < (mat.shape[1] - 1) and visited[i, j+1] == 0:
            distances[i, j+1] = min(distances[i, j+1], distances[i, j] + mat[i, j+1])
        visited[i, j] = 1
        # minimum unvisited distance (use 1e12 to disqualify visited nodes)
        i, j = np.unravel_index(np.argmin(distances + 1e12*visited), mat.shape)
    return distances[-1, -1]


if __name__ == '__main__':
    print(p81())
>>>>>>> Stashed changes
