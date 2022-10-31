from math import sqrt


def p45():
    n = 143  # start at the known one
    while True:
        n += 1
        Hn = n*(2*n - 1)
        # no need to check triangular numbers.
        # superset of hexagonal.
        n_p = (sqrt(24*Hn + 1) + 1)/6
        if int(n_p) == n_p:
            return Hn


print(p45())