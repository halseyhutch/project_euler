from misc.gcd import gcd
from math import sqrt


# https://en.wikipedia.org/wiki/Pythagorean_triple
def p9(total):
    max_m = int(sqrt(2*total + 1) - 1)//2
    for m in range(2, max_m + 1):
        max_n = (total//(2*m)) - m
        for n in range(1, min(m, max_n + 1)):
            if gcd(m, n) > 1:
                continue
            if m % 2 == 1 and n % 2 == 1:
                continue
            k = 1
            while 2*k*m**2 + 2*k*m*n <= total:
                if 2*k*m**2 + 2*k*m*n == total:
                    return k**3*(m**2 - n**2)*2*m*n*(m**2 + n**2)
                k += 1


print(p9(1000))