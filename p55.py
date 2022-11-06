from misc.palindrome import is_palindrome


def is_lychrel(n, d=0):
    if d > 50: return 1
    n += int(str(n)[::-1])
    if is_palindrome(n): return 0
    else: return is_lychrel(n, d+1)


def p55():
    res = 0
    for i in range(1, 10_000):
        res += is_lychrel(i)
    return res


print(p55())