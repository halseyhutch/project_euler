from math import sqrt


# https://en.wikipedia.org/wiki/Pell%27s_equation
def p66(n):
    res = -1
    max_x = -1
    for D in range(2, n):
        if int(sqrt(D))**2 == D: continue
        m = 0
        d = 1
        a0 = int(sqrt(D))
        a = a0
        p = [0, 1, a0]
        q = [1, 0, 1]
        while True:
            m = d*a - m
            d = (D - m*m)//d
            a = (a0 + m)//d
            p[0:2] = p[1:3]
            q[0:2] = q[1:3]
            p[2] = a*p[1] + p[0]
            q[2] = a*q[1] + q[0]
            if p[2]*p[2] - D*q[2]*q[2] == 1: break
        if p[2] > max_x:
            max_x = p[2]
            res = D
    return res


print(p66(1000))