from misc.gcd import gcd


# not great, probably a smarter way.
def p73(n):
    assert n > 4
    res = 0
    for q in range(5, n + 1):
        for p in range(q//3, q//2 + 1):
            if 3*p > q and 2*p < q and gcd(p, q) == 1:
                res += 1
    return res


print(p73(12_000))