import numpy as np


def sieve(n):
    nums = [True]*n
    nums[0:2] = [False]*2
    p = 2
    while p**2 < n:
        nums[(p**2)::p] = [False]*int(np.ceil((n - p**2)/p))
        p = next((i for i, j in enumerate(nums[(p+1):]) if j)) + p + 1
    return nums