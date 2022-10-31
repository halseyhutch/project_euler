from itertools import permutations


def p43():
    res = 0
    for n in permutations('0123456789', 10):
        n = "".join(n)
        if int(n[3]) not in [2, 4, 6, 8, 0]: continue
        if int(n[5]) not in [5, 0]: continue
        if int(n[2:5]) % 3 != 0: continue
        if int(n[4:7]) % 7 != 0: continue
        if int(n[5:8]) % 11 != 0: continue
        if int(n[6:9]) % 13 != 0: continue
        if int(n[7:10]) % 17 != 0: continue
        res += int(n)
    return res


print(p43())