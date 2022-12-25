import time


with open('data/p81.txt') as f:
    matrix = f.read().split()
matrix = [list(map(int, x.split(','))) for x in matrix]

# assume: matrix is a square list of lists.
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
def p81(matrix):

    m = len(matrix[0]) - 1
    n = len(matrix) - 1
    visited = [[False]*(m + 1) for _ in range(n + 1)]
    limit = sum([sum(x) for x in matrix])
    distances = [[limit]*(m + 1) for _ in range(n + 1)]
    
    i = 0
    j = 0
    distances[i][j] = matrix[i][j]

    while not visited[m][n]:

        # check down
        if i < m and not visited[i + 1][j]:
            distances[i + 1][j] = min(
                distances[i + 1][j],
                distances[i][j] + matrix[i + 1][j]
            )
        
        # check right
        if j < n and not visited[i][j + 1]:
            distances[i][j + 1] = min(
                distances[i][j + 1],
                distances[i][j] + matrix[i][j + 1]
            )

        # mark current node as visited
        visited[i][j] = True

        # find minimum unvisited node
        # we default to the end node as the non-minimum case.
        i = m
        j = n
        for k in range(m + 1):
            for l in range(n + 1):
                if not visited[k][l]:
                    if distances[k][l] < distances[i][j]:
                        i, j = k, l

    return distances[m][n]


start_time = time.time()
print(p81(matrix))
print(time.time() - start_time)