<<<<<<< Updated upstream
def rect_count(m, n):
    res = 0
    # a little misleading. i is height - 1 of the candidate.
    for i in range(m):
        for j in range(n):
            res += (m - i)*(n - j)
    return res


def p85():
    res = 0
    nearest = 999999999999
    # arbitrary starting point. it runs fast anyway.
    for i in range(10, 100):
        over_flag = False
        for j in range(i, 100):
            if over_flag: break
            c = rect_count(i, j)
            if c > 2e6: over_flag = True
            if abs(2e6 - c) < nearest:
                res = i*j
                nearest = abs(2e6 - c)
    return res


print(p85())
=======
if __name__ == '__main__':
    min_distance = 2_000_000
    sol = -1
    for i in range(1, 100):
        for j in range(1, 100):
            num_rects = i*(i+1)*j*(j+1)/4
            if abs(num_rects - 2_000_000) < min_distance:
                min_distance = abs(num_rects - 2_000_000)
                sol = i*j
    print(sol)
>>>>>>> Stashed changes
