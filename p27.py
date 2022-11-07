from misc.primes import sieve_set


def p27():
    # this is a little risky. 
    primes = sieve_set(1000, frozen=True)
    max_p = 0
    res = 0
    for a in range(-999, 1000):
        # n = 0 ensures that b must be prime.
        for b in primes:
            cnt = 1
            check = 1 + a + b
            while check in primes:
                cnt += 1
                check = cnt**2 + a*cnt + b
            if cnt > max_p:
                max_p = cnt
                res = a*b
    return res


print(p27())