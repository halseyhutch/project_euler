from misc.primes import sieve
import numpy as np


def p35(limit):
    primes = sieve(limit)
    res = 0
    for p, b in enumerate(primes):
        if b:
            pt = (p // 10) + (p % 10)*10**int(np.log10(p))
            while pt != p:
                if not primes[pt]: break
                pt = (pt // 10) + (pt % 10)*10**int(np.log10(pt))
            else: res += 1
    return res


print(p35(1_000_000))