# last solution on p1 was very similar to mine, so I took what I perceived
# as the best of both solutions.
def step(figs, x, res):
    if len(figs) == 1 and x[2:4]+x[:2] in figs[0]:
        print(sum([int(x) for x in res + [x[2:4]+x[:2]]]))
    for i in range(len(figs)):
        for n in figs[i]:
            if x[2:4] == n[:2]:
                figsc = figs.copy()
                step(figsc[:i]+figsc[i+1:], x[:2]+n[2:4], res + [n])



def p61():
    # did some work in wolfram to find bounds
    tri = [str(n*(n+1)//2) for n in range(45, 141)]
    sq = [str(n*n) for n in range(32, 100)]
    pent = [str(n*(3*n-1)//2) for n in range(26, 82)]
    hex = [str(n*(2*n-1)) for n in range(23, 71)]
    hept = [str(n*(5*n-3)//2) for n in range(21, 64)]
    oct = [str(n*(3*n-2)) for n in range(19, 59)]

    for n in oct:
        step([tri, sq, pent, hex, hept], n, [n])


p61()