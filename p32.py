from itertools import permutations


def p32():
    products = set()
    # probably could make this faster. but it runs well on my pc.
    for digs in permutations('123456789', 9):
        digs = "".join(digs)
        if int(digs[0:1])*int(digs[1:5]) == int(digs[5:9]) or \
        int(digs[0:2])*int(digs[2:5]) == int(digs[5:9]):
            products.add(int(digs[5:9]))
    return sum(products)


print(p32())