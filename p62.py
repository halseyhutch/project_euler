from collections import defaultdict


# this doesn't guarantee the lowest min, just the lowest max.
# but it works for this problem.
def p62():
    res = defaultdict(set)
    for i in range(10000):
        c = i*i*i
        pkey = "".join(sorted(str(c)))
        if pkey in res:
            res[pkey].add(c)
            if len(res[pkey]) == 5:
                return min(res[pkey])
        else:
            res[pkey] = {c}


print(p62())