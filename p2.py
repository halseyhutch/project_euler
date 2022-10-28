def p2(limit):
    f1 = 1
    f2 = 2
    result = 0
    while f2 < limit:
        if f2 % 2 == 0:
            result += f2
        tmp = f2
        f2 += f1
        f1 = tmp
    return result


print(p2(4e6))