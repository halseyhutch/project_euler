def p42():

    res = 0

    # probably a smarter way to do this. but it works and is fast.
    tri_nums = set()
    for n in range(1, 100):
        tri_nums.add(n*(n+1)//2)

    with open('data/p42.txt') as f:
        words = f.read().replace('"', '').split(',')
    for word in words:
        score = sum(map(lambda x: ord(x) - 96, word.lower()))
        if score in tri_nums:
            # print(score)
            res += 1
    return res


print(p42())