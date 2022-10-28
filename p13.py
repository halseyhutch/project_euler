import numpy as np


def p13():
    nums = open('data/p13.txt').read().splitlines()
    res = 0
    for n in nums:
        # doesn't generalize to use the first k + eps digits.
        # but it works ok here.
        res += int(n[:12])
    res //= 10**np.floor(np.log10(res) - 9)
    return res


print(p13())