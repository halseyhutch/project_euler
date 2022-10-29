from misc.gcd import gcd
import numpy as np


def p39():
    sols = [0]*1001
    # upper bound ~= sqrt(500)
    for m in range(2, 22):
        for n in range(1, m):
            p = 2*m**2 + 2*m*n
            if p > 1000:
                break
            if gcd(m, n) == 1 and not (m % 2 == 1 and n % 2 == 1):
                sols[p::p] = [x+1 for x in sols[p::p]]
    return np.argmax(sols)


print(p39())