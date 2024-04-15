from functools import cache


@cache
def match_sum_prod(s, p, k):
    if s < k: return False
    if p == 1: return s == k
    if k == 1: return s == p
    for i in range(2, int(p) + 1):
        if (s - i) < (k - 1): return False
        if p % i == 0:
            if match_sum_prod(s - i, p / i, k - 1): return True
    return False


def min_sum_prod(k):
    for i in range(k + 1, 2 * k + 1):
        if match_sum_prod(i, i, k):
            return i


def p88(n):
    minimal_ps_numbers = set()
    for k in range(2, n+1):
        minimal_ps_numbers.add(min_sum_prod(k))
    return sum(minimal_ps_numbers)


if __name__ == '__main__':
    print(p88(12000))
