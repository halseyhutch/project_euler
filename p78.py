<<<<<<< Updated upstream
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
=======
# https://en.wikipedia.org/wiki/Partition_function_(number_theory)
# pretty much the same approach as 76. calculate everything mod 1e6.
# use ramanujan's congruences - only check 4 mod 5 candidates.

from functools import cache

@cache
def partition(n):
    if n == 0: return 1
    k = 1
    p = k*(3*k - 1)//2
    res = 0
    while p <= n:
        res += ((-1)**(k+1))*partition(n - p)
        if k > 0: k = -1*k
        else: k = -1*k + 1
        p = k*(3*k - 1)//2
    return res % 1_000_000


def p78():
    n = 4
    while partition(n) != 0:
        n += 5
    return n


if __name__ == '__main__':
    print(p78())
>>>>>>> Stashed changes
