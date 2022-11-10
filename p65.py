from misc.digit_sum import digit_sum


# https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents
def p65(n):
    p = [2, 3, 8]
    q = [1, 1, 3]
    for i in range(1, n-2):
        if i % 3 == 0: a = (i//3 + 1)*2
        else: a = 1
        p[0:2] = p[1:3]
        q[0:2] = q[1:3]
        p[2] = a*p[1] + p[0]
        q[2] = a*q[1] + q[0]
    return digit_sum(p[2])


print(p65(100))