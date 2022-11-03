def p22():
    with open('data/p22.txt') as f:
        names = sorted(f.read().replace('"', '').split(','))
    res = 0
    for i, name in enumerate(names):
        res += (i + 1)*sum(map(lambda x: ord(x) - 96, name.lower()))
    return res

print(p22())