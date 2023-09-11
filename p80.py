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
