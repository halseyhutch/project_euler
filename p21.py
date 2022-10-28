import numpy as np
# import cProfile


def sum_pds(n):
    if n < 2: return 1
    res = 1
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            res += i
            if n != i**2:
                res += (n//i)
    return res


def p21(limit):
    pd_sums = [sum_pds(i) for i in range(limit)]
    amic_nums = set()
    for i in range(2, limit):
        for j in range(i + 1, limit):
            if pd_sums[i] == j and pd_sums[j] == i:
                amic_nums.add(i)
                amic_nums.add(j)
    return sum(amic_nums)


print(p21(10000))
# cProfile.run("p21(10000)")