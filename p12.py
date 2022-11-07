from misc.primes import sieve
import numpy as np
# import cProfile


def divisor_count(n, primes):
    total = 1
    for p, b in enumerate(primes):
        if b:
            counter = 0
            if n % p == 0:
                n_t = n
                while n_t % p == 0:
                    n_t = n_t/p
                    counter += 1
                total = total*(counter + 1)
    return total


def p12(limit):
    primes = sieve(10000)
    # find a lower bound to speed up the main part
    # multiplying n primes gives a number with 2^n divisors
    lb = 1
    count = 0
    clim = int(np.log2(limit))
    for p, b in enumerate(primes):
        if b:
            lb *= p
            count += 1
            if count == clim: break
    # begin the actual work
    div_count = 0
    n = int(np.ceil(0.5*np.sqrt(8*lb + 1) - 0.5)) - 1
    tn = int(0.5*n*(n+1))
    while div_count <= limit:
        n += 1
        tn += n
        div_count = divisor_count(tn, primes)
    return tn


print(p12(500))
# cProfile.run("p12(500)")