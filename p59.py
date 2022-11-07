def p59():
    with open('data/p59.txt') as f:
        chars = list(map(int, f.read().split(',')))
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                decrypt = ""
                for i in range(len(chars)):
                    if i % 3 == 0:
                        decrypt += chr(chars[i]^a)
                    elif i % 3 == 1:
                        decrypt += chr(chars[i]^b)
                    else:
                        decrypt += chr(chars[i]^c)
                if 'have ' in decrypt:
                    # print(decrypt)
                    # print(chr(a) + chr(b) + chr(c))
                    return sum([ord(c) for c in decrypt])


print(p59())