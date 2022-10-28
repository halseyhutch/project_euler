def p1(limit):
    return sum([x for x in range(limit) if x % 3 == 0 or x % 5 == 0])


print(p1(1000))