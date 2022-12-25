from math import sqrt, floor

# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation
def p80():

    res = 0

    for i in range(2, 100):

        c = i
        p = 0
        x = floor(sqrt(c))
        y = x**2
        r = c - y

        if r == 0: continue
        res += x
        p = 10*p + x

        # find first 100 digits (first one already found)
        for _ in range(99):
            
            # simplified for integer square roots
            c = r*100
            x = 0
            while x*(20*p + x) <= c: x += 1
            x -= 1
            y = x*(20*p + x)
            r = c - y
            res += x
            p = 10*p + x
    
    return res

print(p80())