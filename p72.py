from functools import cache
from math import floor


# https://en.wikipedia.org/wiki/Farey_sequence
@cache
def farey_length(n):
    res = n*(n+3)//2
    for d in range(2, n + 1):
        res -= farey_length(floor(n/d))
    return res


def p72(n):
    # we don't want 0/1 or 1/1 (which are included in this algorithm)
    return farey_length(n) - 2


print(p72(1_000_000))