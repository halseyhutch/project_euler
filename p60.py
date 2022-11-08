from misc.primes import sieve_list, is_prime
from itertools import permutations
from operator import itemgetter
import time


def p60():
    primes_short = sieve_list(30_000)
    for i in range(28, len(primes_short)):
        for j in range(i + 1, len(primes_short)):
            pt = (3,7,109) + itemgetter(i, j)(primes_short)
            pc = permutations(pt, 2)
            for p in pc:
                p = int("".join(map(str, p)))
                if not is_prime(p):
                    break
            else: return pt


tic = time.time()
print(p60())
print(time.time() - tic)