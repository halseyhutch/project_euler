from misc.primes import sieve


def p10(limit):
    primes = sieve(limit)
    res = 0
    for p, b in enumerate(primes):
        if b:
            res += p
    return res


print(p10(int(2e6)))