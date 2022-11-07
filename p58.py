from misc.primes import is_prime


def p58():
    p = 0
    q = 0
    side_length = 1
    while q == 0 or p/q > 0.1:
        side_length += 2
        for offset in range(1, 4):
            if is_prime(side_length*side_length - offset*(side_length - 1)):
                p += 1
            q += 1
        # include the bottom right diag (always square)
        q += 1
    return side_length


print(p58())