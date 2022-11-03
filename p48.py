from functools import reduce


def last_digits_add(x, y, n):
    return (x % 10**n + y % 10**n) % 10**n


def last_digits_power(x, p, n):
    res = 1
    for i in range(p):
        res = (res * x) % 10**n
    return res


def p48(n, d):
    return reduce(
        lambda x, y: last_digits_add(x, y, d),
        [last_digits_power(x, x, d) for x in range(1, n)]
    )


print(p48(1000, 10))