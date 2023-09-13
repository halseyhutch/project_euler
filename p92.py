from functools import cache

@cache
def chain(n):
    if n == 89: return 1
    if n == 1: return 0
    n = str(n)
    res = 0
    for d in n:
        res += (int(d)*int(d))
    return chain(res)


if __name__ == '__main__':
    sol = 0
    for i in range(1, 10_000_000):
        sol += chain(i)
    print(sol)
