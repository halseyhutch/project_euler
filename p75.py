from misc.gcd import gcd
from math import sqrt
import numpy as np


def p75(N):
    res = np.zeros(N)
    max_m = int(sqrt(2*N + 1) - 1)//2
    for m in range(2, max_m + 1):
        max_n = (N//(2*m)) - m
        for n in range(1, min(m, max_n + 1)):
            if gcd(m, n) > 1: continue
            if m % 2 == 1 and n % 2 == 1: continue
            L = 2*m**2 + 2*m*n
            res[L::L] += 1
    return np.sum(res == 1)


print(p75(1_500_000))