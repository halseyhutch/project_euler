# doesn't really make sense to check every a and b. start high
def p56():
    res = -1
    for a in range(90, 100):
        for b in range(90, 100):
            res = max(res, sum(map(int, list(str(a**b)))))
    return res


print(p56())