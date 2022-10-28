def p3(n):
    d = 2
    while n > 1:
        if n % d == 0:
            n /= d
        else:
            d += 1
    return d


print(p3(600851475143))