# once again python makes this easy
def p29():
    seen = set()
    for a in range(2, 101):
        for b in range(2, 101):
            seen.add(a**b)
    return len(seen)


print(p29())