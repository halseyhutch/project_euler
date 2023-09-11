<<<<<<< Updated upstream
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
=======
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation
# or, abuse modern computational power

from math import isqrt

def p80(n):
    result = 0
    for i in range(1, n + 1):
        if isqrt(i)**2 == i: continue
        digits = str(isqrt(i*10**(2*100)))[:100]
        result += sum([int(d) for d in digits])
    return result


if __name__ == '__main__':
    print(p80(100))
>>>>>>> Stashed changes
