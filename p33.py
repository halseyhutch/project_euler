from misc.gcd import gcd


def p33():
    res = 1
    for d in range(12, 100):
        for n in range(11, d):
            fn = n // 10
            ln = n % 10
            if ln == 0: continue
            fd = d // 10
            ld = d % 10
            if (ln == fd and ld != 0 and n/d == fn/ld):
                # print(f"{n}/{d}")
                g = gcd(d, n)
                res *= d/g
                if res % (n/g) == 0: res /= n/g
    return res


print(p33())