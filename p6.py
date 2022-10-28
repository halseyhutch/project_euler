def p6(n):
    # https://www.wolframalpha.com/input?i=%28n%28n%2B1%29%2F2%29%5E2+-+n%28n%2B1%29%282n%2B1%29%2F6
    return n*(n+1)*(3*n+2)*(n-1)//12


print(p6(100))