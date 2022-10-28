from math import factorial


def p24(n, d):
    # this makes n more intuitive
    # and still work with zero indexing
    n -= 1
    res = 0
    digits = list(range(d))
    while len(digits) > 0:
        di = n // factorial(len(digits)- 1)
        res = res*10 + digits[di]
        n %= factorial(len(digits) - 1)
        digits.pop(di)
    return res


print(p24(1_000_000, 10))