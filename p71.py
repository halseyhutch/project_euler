# p/q < 3/7 => 7p < 3q.
# choose 7p = 3q - 1.
# we could probably speed this up by searching downwards, but I couldn't
# think of a good cutoff rule. this runs quickly anyway.

# forum solutions were surprisingly bad! one of the rare cases where I think
# mine is better :)
def p71(n):
    assert n >= 8
    p_best = 2
    q_best = 5
    for q in range(2, n):
        p = (3*q - 1)//7
        if p_best/q_best < p/q:
            p_best, q_best = p, q
    return p_best


print(p71(1_000_000))