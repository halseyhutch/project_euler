<<<<<<< Updated upstream
from misc.primes import sieve_list
from functools import cache

# same solution as p31.
PRIMES = sieve_list(100)


@cache
=======
# this is the same problem as #31
import functools
from misc.primes import sieve_list
PRIMES = sieve_list(100)


@functools.cache
>>>>>>> Stashed changes
def ways(n, ci):
    if n < 0: return 0
    if n == 0: return 1
    res = 0
    # need to avoid double counting
    for i in range(ci, len(PRIMES)):
        res += ways(n - PRIMES[i], i)
    return res


<<<<<<< Updated upstream
def p77(n):
    res = 4
    while ways(res, 0) < n:
        res += 1
    return res


print(p77(5000))
=======
def p77(limit):
    n = 1
    while ways(n, 0) < limit:
        n += 1
    return n


if __name__ == '__main__':
    print(p77(5_000))
>>>>>>> Stashed changes
