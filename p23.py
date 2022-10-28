import numpy as np


def sum_pds(n):
    if n < 2: return 1
    res = 1
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            res += i
            if n != i**2:
                res += (n//i)
    return res


def p23():
    abund_nums = [i for i in range(1, 28123) if sum_pds(i) > i]
    abund_sums = set()
    for i in range(len(abund_nums)):
        for j in range(i, len(abund_nums)):
            x = abund_nums[i] + abund_nums[j]
            if x <= 28123: abund_sums.add(x)
    # calculating this via the complement
    return int(28123*28124/2) - sum(abund_sums)


print(p23())