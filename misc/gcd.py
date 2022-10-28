def gcd(x, y):
    if x >= y: a, b = x, y
    else: a, b = y, x
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


def lcm(x, y):
    return int(x*y/gcd(x, y))