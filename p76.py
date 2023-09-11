<<<<<<< Updated upstream
from functools import cache
from math import sqrt, floor

# https://en.wikipedia.org/wiki/Partition_(number_theory)
# note that this is slightly different, including just the term as
# one possibility. (we subtract one in the main function to account for this.)
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
    return res


def p76(n):
    return partition(n) - 1


print(p76(100))
=======
# https://en.wikipedia.org/wiki/Partition_function_(number_theory)
from functools import cache

@cache
def p76(n):
    if n == 0: return 1
    k = 1
    p = k*(3*k - 1)//2
    res = 0
    while p <= n:
        res += ((-1)**(k+1))*p76(n - p)
        if k > 0: k = -1*k
        else: k = -1*k + 1
        p = k*(3*k - 1)//2
    return res


if __name__ == '__main__':
    print(p76(100) - 1)
>>>>>>> Stashed changes
