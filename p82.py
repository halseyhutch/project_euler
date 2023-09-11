# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# kind of slow
import numpy as np

def p82():
    mat = np.loadtxt('data/p82.txt', delimiter=',')
    candidates = []
    for i_initial in range(0, mat.shape[0]):
        visited = np.zeros(mat.shape)
        distances = np.full(mat.shape, np.inf)
        i = i_initial
        j = 0
        distances[i, j] = mat[i, j]
        while np.sum(visited[:, -1]) == 0:
            # check up
            if i > 0 and visited[i-1, j] == 0:
                distances[i-1, j] = min(distances[i-1, j], distances[i, j] + mat[i-1, j])
            # check down
            if i < (mat.shape[0] - 1) and visited[i+1, j] == 0:
                distances[i+1, j] = min(distances[i+1, j], distances[i, j] + mat[i+1, j])
            # check right
            if j < (mat.shape[1] - 1) and visited[i, j+1] == 0:
                distances[i, j+1] = min(distances[i, j+1], distances[i, j] + mat[i, j+1])
            visited[i, j] = 1
            # minimum unvisited distance (use 1e12 to disqualify visited nodes)
            i, j = np.unravel_index(np.argmin(distances + 1e12*visited), mat.shape)
        # only the visited node will have a non-zero value
        candidates.append(distances[visited[:, -1] == 1, -1][0])
    return min(candidates)


if __name__ == '__main__':
    print(p82())
