# modified sieve algorithm
def p47():
    factors = [0]*1_000_000
    # use this to check for sequential nums
    check = 0
    for i in range(2, len(factors)):
        if factors[i] == 0:
            check = 0
            factors[i::i] = [x+1 for x in factors[i::i]]
        elif factors[i] == 4:
            check += 1
            if check == 4: return i-3
        else: check = 0
        

print(p47())