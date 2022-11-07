from misc.primes import sieve_set


def p37():
    res = 0
    # iterated on this size until 11 primes were in the final set
    primes = sieve_set(1_000_000, frozen=True)
    for p in primes:
        p = str(p)
        for i in range(len(p)):
            if int(p[i:]) not in primes or int(p[:(i+1)]) not in primes:
                break
        else: res += int(p)
    return res - 17  # remove 2, 3, 5, 7


print(p37())