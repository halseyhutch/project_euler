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


def sieve_set(n, frozen=True):
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


# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Miller_test
def is_prime(n):

    assert n < 4_759_123_141
    if n in [2, 7, 61]: return True

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for a in [2, 7, 61]:
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n-1: break
        else: return False
    
    return True