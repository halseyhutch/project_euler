# 6*9^5 = 354294.
# so we only need to consider six digit (or less) numbers.
# and most of the six digit nums will be invalid.
def p30(p):
    res = 0
    for i in range(2, 1_000_000):
        tmp = i
        ss = 0
        while tmp > 0:
            ss += (tmp % 10)**p
            if ss > i:
                break
            tmp //= 10
        if i == ss:
            res += i
    return res


print(p30(5))