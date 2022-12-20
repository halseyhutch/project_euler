from functools import cache
from math import sqrt, floor

# https://en.wikipedia.org/wiki/Partition_(number_theory)
# change the function a bit from p76 so we don't have huge numbers.
@cache
def partition(n):
    if n == 0: return 1
    elif n < 0: return 0
    res = 0
    lb = floor((sqrt(24*n + 1) - 1)/-6)
    ub = floor((sqrt(24*n + 1) + 1)/6)
    for i in range(lb, ub + 1):
        if i == 0: continue
        res += ((-1)**(i + 1))*partition(n - i*(3*i - 1)//2)
        res %= 1e6
    return res


def p78():
    i = 2
    while partition(i) != 0:
        i += 1
    return i


print(p78())