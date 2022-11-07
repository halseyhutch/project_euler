from misc.primes import sieve
from itertools import permutations


# eight or nine numbers ensures divisibility by nine
# 1..9 = 45, 1..8 = 36.
# try permutations of seven
def p41():
    res = 0
    primes = sieve(8_000_000)
    for n in permutations('1234567', 7):
        if n[6] in [2, 4, 6]:
            continue
        n = int("".join(n))
        if primes[n]:
            res = max(n, res)
    return res


print(p41())