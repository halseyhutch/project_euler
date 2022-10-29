from math import factorial
import time


# https://mathworld.wolfram.com/Factorion.html
def p34():
    res = 0
    for i in range(3, 50_000):
        fs = 0
        tmp = i
        while tmp > 0:
            fs += factorial(tmp % 10)
            tmp //= 10
        if fs == i:
            res += i
    return res


print(p34())