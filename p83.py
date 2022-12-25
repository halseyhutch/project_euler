import numpy as np
import time
matrix = np.loadtxt('data/p83.txt', dtype=int, delimiter=',')

# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
def p83(matrix):

    m = matrix.shape[0] - 1
    n = matrix.shape[1] - 1
    limit = np.sum(matrix)

    visited = np.full(matrix.shape, False)
    distances = np.full(matrix.shape, limit)
    
    i = 0
    j = 0
    distances[i, j] = matrix[i, j]

    while not visited[m, n]:

        # check down
        if i < m and not visited[i + 1, j]:
            distances[i + 1, j] = min(
                distances[i + 1, j],
                distances[i, j] + matrix[i + 1, j]
            )
        
        # check right
        if j < n and not visited[i, j + 1]:
            distances[i, j + 1] = min(
                distances[i, j + 1],
                distances[i, j] + matrix[i, j + 1]
            )
        
        # check up
        if i > 0 and not visited[i - 1, j]:
            distances[i - 1, j] = min(
                distances[i - 1, j],
                distances[i, j] + matrix[i - 1, j]
            )
        
        # check left
        if j > 0 and not visited[i, j - 1]:
            distances[i, j - 1] = min(
                distances[i, j - 1],
                distances[i, j] + matrix[i, j - 1]
            )

        # mark current node as visited
        visited[i, j] = True

        # find minimum unvisited node
        # we default to the end node as the non-minimum case.
        i = m
        j = n
        for k in range(m + 1):
            for l in range(n + 1):
                if not visited[k, l]:
                    if distances[k, l] < distances[i, j]:
                        i, j = k, l
    
    return distances[m, n]


# the base Python implementation was 4x faster on p81.
# not a great numpy application with this method.
start_time = time.time()
print(p83(matrix))
print(time.time() - start_time)