def p67():
    with open('data/p67.txt') as f:
        raw = f.read().split('\n')
    triangle = [list(map(int, x.split())) for x in raw]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(i + 1):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


print(p67())