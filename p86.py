from math import sqrt, isqrt, comb


def possible_paths(M):
    res = 0
    for i in range(1, M + 1):
        for j in range(i + i % 2, 2*i + 1):
            if isqrt(i**2 + j**2) == sqrt(i**2 + j**2):
                res += j//2
    return res


print(possible_paths(100))