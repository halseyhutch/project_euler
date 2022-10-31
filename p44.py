def p44():
    res = 987654321
    pent_nums = set()
    for n in range(1, 10_001):
        pent_nums.add(n*(3*n-1)//2)
    for pj in pent_nums:
        for pk in pent_nums:
            if pj + pk in pent_nums and pj - pk in pent_nums:
                res = min(res, pj - pk)
    return res


print(p44())