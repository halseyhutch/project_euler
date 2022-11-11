from functools import cache
from math import factorial


def digit_fsum(n):
    res = 0
    while n > 0:
        res += factorial(n % 10)
        n //= 10
    return res


@cache
def chain_length(n):

    if n == 169: return 3
    elif n == 363601: return 3
    elif n == 1454: return 3
    elif n == 871: return 2
    elif n == 45361: return 2
    elif n == 872: return 2
    elif n == 45362: return 2
    elif digit_fsum(n) == n: return 1
    else: return 1 + chain_length(digit_fsum(n))


def p74(n):
    res = 0
    for i in range(1, n):
        if chain_length(i) == 60:
            res += 1
    return res


print(p74(1_000_000))