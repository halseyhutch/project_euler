import numpy as np


def sieve(n):
    nums = [True]*n
    nums[0:2] = [False]*2
    p = 2
    while p**2 < n:
        if nums[p]:
            nums[(p**2)::p] = [False]*int(np.ceil((n - p**2)/p))
        p += 1
    return nums