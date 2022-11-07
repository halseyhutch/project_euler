# we can't avoid a multiple of three issue in the 8-value family if the
# group is one or two digits. need to consider three, six, nine.. digit groups.
# also know that the last digit cannot be in the group
# otherwise there will be multiples of two or five.
from misc.primes import sieve


def p51():
    start = 56_003  # from problem statement
    primes = sieve(1_000_000)
    for p, b in enumerate(primes[start:], start=start):
        if b:
            p = str(p)
            for d in '012':
                if p.count(d) == 3 and p.find(d) != len(p):
                    violations = 0
                    for rd in '123456789':
                        if not primes[int(p.replace(d, rd))]:
                            violations += 1
                        if violations > 1:
                            break
                    else: return p


print(p51())