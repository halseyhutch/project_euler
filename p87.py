from misc.primes import sieve_list
from math import sqrt


def p87(limit):
    primes = sieve_list(int(sqrt(limit)))
    sols = set()
    for i in range(len(primes)):
        if primes[i]**4 > limit:
            break
        for j in range(len(primes)):
            if primes[i]**4 + primes[j]**3 > limit:
                break
            for k in range(len(primes)):
                if primes[i]**4 + primes[j]**3 + primes[k]**2 < limit:
                    sols.add(primes[i]**4 + primes[j]**3 + primes[k]**2)
                else:
                    break
    return len(sols)


if __name__ == '__main__':
    print(p87(50_000_000))