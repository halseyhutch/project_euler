from misc.sieve import sieve_set


def p37():
    res = 0
    # just a guess on size.
    primes = sieve_set(1_000_000, frozen=True)
    for p in primes:
        p = str(p)
        violation = False
        for i in range(len(p)):
            if int(p[i:]) not in primes or int(p[:(i+1)]) not in primes:
                violation = True
                break
        if not violation:
            # print(p)
            res += int(p)
    return res - 17  # remove 2, 3, 5, 7


print(p37())