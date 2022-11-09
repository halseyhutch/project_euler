from math import log10, floor


def p63():
    res = 1 # include 1^1
    for x in range(2, 10):
        p = 1
        while x**p > 10**(p-2):
            if floor(log10(x**p)) == p - 1:
                res += 1
            p += 1
    return res


print(p63())