from misc.primes import sieve_list, is_prime
from functools import cache
import time


@cache
def p60c(x, y):
    return not is_prime(int(str(x) + str(y)))


# this is the first nontrivial problem. you can kind of luck into the answer
# with the right prime list (e.g., set cap to 10k and return first candidate).
# I tried to avoid this in my solution, still runs well under a minute.
# but 20k is ultimately still an arbitrary size.
def p60():
    res = 999999999
    primes_short = sieve_list(20_000)
    for i1 in range(1, len(primes_short)):
        p1 = primes_short[i1]
        for i2 in range(i1 + 1, len(primes_short)):
            p2 = primes_short[i2]
            if p1 + p2 >= res: break
            if p60c(p1, p2) or p60c(p2, p1): continue
            for i3 in range(i2 + 1, len(primes_short)):
                p3 = primes_short[i3]
                if p1 + p2 + p3 >= res: break
                if (p60c(p1, p3) or p60c(p2, p3)
                    or p60c(p3, p1) or p60c(p3, p2)):
                    continue
                for i4 in range(i3 + 1, len(primes_short)):
                    p4 = primes_short[i4]
                    if p1 + p2 + p3 + p4 >= res: break
                    if (p60c(p1, p4) or p60c(p2, p4) or p60c(p3, p4)
                        or p60c(p4, p1) or p60c(p4, p2) or p60c(p4, p3)):
                        continue
                    for i5 in range(i4 + 1, len(primes_short)):
                        p5 = primes_short[i5]
                        if p1 + p2 + p3 + p4 + p5 >= res: break
                        if (p60c(p1, p5) or p60c(p2, p5) or p60c(p3, p5)
                            or p60c(p4, p5) or p60c(p5, p1) or p60c(p5, p2)
                            or p60c(p5, p3) or p60c(p5, p4)):
                            continue
                        res = min(res, sum([p1, p2, p3, p4, p5]))
    return res


tic = time.time()
print(p60())
print(time.time() - tic)