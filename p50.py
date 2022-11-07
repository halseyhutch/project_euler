from misc.primes import sieve


def p50(n):
    primes = sieve(n)
    plist = [p for p, b in enumerate(primes) if b]
    start_w = 0
    while sum(plist[:start_w]) < n:
        start_w += 1
    for w in range(start_w, 0, -1):
        p = sum(plist[:w])
        if p >= n: continue
        if primes[p]: return p
        for k in range(len(plist) - w):
            p -= plist[k]
            p += plist[w+k]
            if p >= n: break
            if primes[p]: return p
            

print(p50(1_000_000))