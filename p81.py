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
