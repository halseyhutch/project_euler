from misc.primes import sieve_list


# we can get the lowest value by multiplying the primes in order.
def p69():
    primes = sieve_list(100)
    res = 1
    i = 0
    while res <= 1_000_000:
        res *= primes[i]
        i += 1
    # a bit sloppy, but the problem is easy.
    return res//primes[i-1]


print(p69())