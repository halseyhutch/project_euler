import numpy as np
from misc.gcd import lcm


def p5(n):
    res = 1
    for i in range(1, n + 1):
        res = lcm(res, i)
    return res


def p5_np(n):
    return np.lcm.reduce(np.arange(1, n + 1))


print(p5(20))
print(p5_np(20))