import numpy as np


def is_palindrome(n):
    other_half = 0
    n_len = np.floor(np.log10(n)) + 1
    for i in range(int(n_len/2)):
        other_half = other_half*10 + (n % 10)
        n //= 10
    if n_len % 2 == 1:
        n //= 10
    return n == other_half



def p4(digits):
    res = 0
    for i in range(1, 10**digits):
        for j in range(i, 10**digits):
            if is_palindrome(i*j):
                res = max(res, i*j)
    return res


print(p4(3))