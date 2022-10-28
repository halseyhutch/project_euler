from math import comb


def p15(n):
    return comb(2*n, n)


print(p15(20))