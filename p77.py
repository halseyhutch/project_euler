from misc.primes import sieve_list
from functools import cache

# same solution as p31.
PRIMES = sieve_list(100)


@cache
def ways(n, ci):
    if n < 0: return 0
    if n == 0: return 1
    res = 0
    # need to avoid double counting
    for i in range(ci, len(PRIMES)):
        res += ways(n - PRIMES[i], i)
    return res


def p77(n):
    res = 4
    while ways(res, 0) < n:
        res += 1
    return res


print(p77(5000))