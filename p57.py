from math import log10, floor


def p57():
    p = 3
    q = 2
    res = 0
    for _ in range(999):
        p, q = p + 2*q, p + q
        if floor(log10(p)) > floor(log10(q)):
            res += 1
    return res


print(p57())