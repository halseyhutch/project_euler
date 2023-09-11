# https://en.wikipedia.org/wiki/Partition_function_(number_theory)
from functools import cache

@cache
def p76(n):
    if n == 0: return 1
    k = 1
    p = k*(3*k - 1)//2
    res = 0
    while p <= n:
        res += ((-1)**(k+1))*p76(n - p)
        if k > 0: k = -1*k
        else: k = -1*k + 1
        p = k*(3*k - 1)//2
    return res


if __name__ == '__main__':
    print(p76(100) - 1)
