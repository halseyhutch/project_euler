from math import comb

def p53():
    res = 0
    for n in range(23, 101):
        r = 0
        while r <= n:
            if comb(n, r) > 1_000_000:
                res += n - 2*r + 1
                break
            r += 1
    return res


print(p53())