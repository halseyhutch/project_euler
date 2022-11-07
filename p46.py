from math import sqrt
from misc.primes import sieve


def p46():
    primes = sieve(10_000)
    for n, b1 in enumerate(primes):
        if n < 9: continue
        if not b1 and n % 2 == 1:
            for p, b2 in enumerate(primes[:n]):
                if b2:
                    rem = (n - p)/2
                    if int(sqrt(rem))**2 == rem:
                        break
            else:
                return n


print(p46())