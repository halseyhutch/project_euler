def p52():
    i = 0
    while True:
        i += 1
        digits = sorted(str(i))
        # lazy eval automatically speeds things up
        if sorted(str(2*i)) != digits or \
            sorted(str(3*i)) != digits or \
            sorted(str(4*i)) != digits or \
            sorted(str(5*i)) != digits or \
            sorted(str(6*i)) != digits:
            continue
        return i


print(p52())