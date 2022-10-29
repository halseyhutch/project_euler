import numpy as np


# old version
def is_palindrome(n):
    other_half = 0
    n_len = np.floor(np.log10(n)) + 1
    for i in range(int(n_len/2)):
        other_half = other_half*10 + (n % 10)
        n //= 10
    if n_len % 2 == 1:
        n //= 10
    return n == other_half


# this version is way faster
def is_p2(n):
    return str(n) == str(n)[::-1]


def p36(limit):
    res = 0
    # even numbers won't work (invalid binary palindrome)
    for i in range(1, limit, 2):
        if is_p2(i) and is_p2(int(bin(i)[2:])):
                res += i
    return res


print(p36(1_000_000))