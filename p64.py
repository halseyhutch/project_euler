from math import sqrt


# https://en.wikipedia.org/wiki/Periodic_continued_fraction#Canonical_form_and_repetend
def p64(N):
    res = 0
    for S in range(2, N+1):
        if int(sqrt(S))**2 == S: continue
        i = 0
        m = 0
        d = 1
        a0 = int(sqrt(S))
        a = a0
        seen = dict()
        while (m, d, a) not in seen:
            seen[(m, d, a)] = i
            i += 1
            m = d*a - m
            d = (S - m*m)//d
            a = (a0 + m)//d
        if (i - seen[(m, d, a)]) % 2 == 1:
            res += 1
    return res


print(p64(10_000))