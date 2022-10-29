def p38():
    res = 0
    for i in range(9, 10_000):
        n = 2
        pd = "".join([str(k*i) for k in range(1, n+1)])
        if sorted(pd) == list('123456789'):
            res = max(res, int(pd))
    return res


print(p38())