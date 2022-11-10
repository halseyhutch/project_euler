from misc.primes import sieve_list
from math import sqrt


# phi(p) = p - 1. can't be a permutation.
# try n of the form p_1p_2.
def p70():
    res = -1
    min_ratio = 9999999999
    # we only need to check up to sqrt(1e7) on one side,
    # but the other side can be higher if the other side is lower.
    # below, we check higher (primes[i]) up to 10_000.
    primes = sieve_list(10_000)
    for i in range(len(primes)):
        if primes[i] <= int(sqrt(1e7)): continue
        for j in range(i):
            n = primes[i]*primes[j]
            if n > 1e7: break
            phi = (primes[i] - 1)*(primes[j] - 1)
            if sorted(str(n)) == sorted(str(phi)) and n/phi < min_ratio:
                min_ratio, res = n/phi, n
    return res


print(p70())