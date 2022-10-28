def p28(n):
    res = 1
    cell = 1
    d = 2
    while (d + 1) <= n:
        res += 4*cell + 10*d
        cell += 4*d
        d += 2
    return res


print(p28(1001))