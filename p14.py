import functools


@functools.cache
def collatz(n):
    if n == 1: return 1
    elif n % 2 == 0: return collatz(n/2) + 1
    # speed up this case, we know it will be even after the first step.
    else: return collatz((3*n + 1)/2) + 2


def p14(limit):
    res = 0
    max_len = 0
    for i in range(1, limit):
        cl = collatz(i)
        if cl > max_len:
            max_len = cl
            res = i
    return res


print(p14(1000000))