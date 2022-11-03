import numpy as np


def p13():
    with open('data/p13.txt') as f:
        nums = f.read().splitlines()
    res = 0
    for n in nums:
        # doesn't generalize to use the first k + eps digits.
        # but it works ok here.
        res += int(n[:12])
    res //= 10**np.floor(np.log10(res) - 9)
    return res


print(p13())