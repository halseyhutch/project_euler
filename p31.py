import functools
COINS = [1, 2, 5, 10, 20, 50, 100, 200]


@functools.cache
def uk_ways(n, ci):
    if n < 0: return 0
    if n == 0: return 1
    res = 0
    # need to avoid double counting
    for i in range(ci, len(COINS)):
        res += uk_ways(n - COINS[i], i)
    return res


def p31(n):
    return uk_ways(n, 0)


print(p31(200))