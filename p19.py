from datetime import datetime


def p19():
    res = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            if datetime(y, m, 1).weekday() == 6:
                res += 1
    return res


print(p19())