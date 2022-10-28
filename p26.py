import numpy as np
from misc.sieve import sieve


# https://en.wikipedia.org/wiki/Repeating_decimal
def p26(lim):
    primes = sieve(lim)
    max_len = 0
    res = 0
    for p, b in enumerate(primes):
        if b:
            # this part is borrowed from grimbal's solution.
            # assume that the longest cycle must be p-1 length.
            # get the remainder at that time, then go forward another
            # p iterations and see how long the cycle is.
            rem = 1
            for i in range(p): rem = (rem*10) % p
            r0 = rem
            rem = (rem*10) % p
            rem_len = 1
            while rem != r0:
                rem = (rem*10) % p
                rem_len += 1
            if rem_len > max_len:
                res = p
                max_len = rem_len
    return res


print(p26(1000))