from collections import defaultdict
from misc.primes import sieve_list


def p49():

    primes = sieve_list(9999)
    # in retrospect, probably should have used dict of lists...
    perms = defaultdict(set)

    for p in primes:
        pkey = "".join(sorted(str(p)))
        if pkey in perms:
            perms[pkey].add(p)
        else:
            perms[pkey] = {p}

    for s in perms.values():
        if len(s) >= 3:
            for low in s:
                if low < 1000 or low == 1487: continue
                for p in s:
                    if p <= low: continue
                    if 2*p - low in s:
                        return str(low) + str(p) + str(2*p - low)


print(p49())