from misc.sieve import sieve
import numpy as np

def p7(n):
    ln = np.log(n)
    lln = np.log(ln)
    # https://en.wikipedia.org/wiki/Prime_number_theorem
    primes = sieve(int(n*(ln + lln)))
    counter = 0
    for p, b in enumerate(primes):
        if b:
            counter += 1
            if counter == n:
                return p

print(p7(10001))