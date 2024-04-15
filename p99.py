from math import log

def p99():
    with open('data/p99.txt') as f:
        content = f.read().splitlines()
        bases = [int(x.split(',')[0]) for x in content]
        exps = [int(x.split(',')[1]) for x in content]

    base = bases[0]
    candidate = exps[0]
    result = 0

    # x^y > a^b
    # y > b*log_x(a)
    for i in range(1, len(bases)):
        if exps[i]*log(bases[i], base) > candidate:
            candidate = exps[i]*log(bases[i], base)
            result = i
    
    return result + 1

if __name__ == "__main__":
    print(p99())
