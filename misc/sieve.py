from math import ceil


def sieve(n):
    nums = [True]*n
    nums[0:2] = [False]*2
    p = 2
    while p**2 < n:
        if nums[p]:
            nums[(p**2)::p] = [False]*int(ceil((n - p**2)/p))
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


def sieve_list(n, start=0):
    primes_bool = sieve(n)
    return [p for p, b in enumerate(primes_bool[start:]) if b]
