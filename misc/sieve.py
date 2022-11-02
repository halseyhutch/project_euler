import numpy as np


def sieve(n):
    nums = [True]*n
    nums[0:2] = [False]*2
    p = 2
    while p**2 < n:
        if nums[p]:
            nums[(p**2)::p] = [False]*int(np.ceil((n - p**2)/p))
        p += 1
    return nums


def sieve_set(n, frozen=False):
    primes_bool = sieve(n)
    pset = set()
    for p, b in enumerate(primes_bool):
        if b:
            pset.add(p)
    if frozen: return frozenset(pset)
    else: return pset


def sieve_list(n):
    primes_bool = sieve(n)
    return [p for p, b in enumerate(primes_bool) if b]
