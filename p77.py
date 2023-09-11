# this is the same problem as #31
import functools
from misc.primes import sieve_list
PRIMES = sieve_list(100)


@functools.cache
def ways(n, ci):
    if n < 0: return 0
    if n == 0: return 1
    res = 0
    # need to avoid double counting
    for i in range(ci, len(PRIMES)):
        res += ways(n - PRIMES[i], i)
    return res


def p77(limit):
    n = 1
    while ways(n, 0) < limit:
        n += 1
    return n


if __name__ == '__main__':
    print(p77(5_000))
