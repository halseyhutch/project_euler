def p22():
    names = sorted(open('data/p22.txt').read().replace('"', '').split(','))
    res = 0
    for i, name in enumerate(names):
        res += (i + 1)*sum(map(lambda x: ord(x) - 96, name.lower()))
    return res

print(p22())