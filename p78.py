# https://en.wikipedia.org/wiki/Partition_function_(number_theory)
# pretty much the same approach as 76. calculate everything mod 1e6.
# use ramanujan's congruences - only check 4 mod 5 candidates.

from functools import cache

@cache
def partition(n):
    if n == 0: return 1
    k = 1
    p = k*(3*k - 1)//2
    res = 0
    while p <= n:
        res += ((-1)**(k+1))*partition(n - p)
        if k > 0: k = -1*k
        else: k = -1*k + 1
        p = k*(3*k - 1)//2
    return res % 1_000_000


def p78():
    n = 4
    while partition(n) != 0:
        n += 5
    return n


if __name__ == '__main__':
    print(p78())
