def p3(n):
    # check two
    d = 2
    if n % d == 0: n /= d
    d += 1
    # then we can skip all even d
    while n > 1:
        if n % d == 0: n /= d
        else: d += 2
    return d


print(p3(600851475143))