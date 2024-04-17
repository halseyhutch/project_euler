def p91(limit):
    # preemptively handle all cases where right angle is at the origin
    result = limit**2
    for x0 in range(limit + 1):
        for y0 in range(limit + 1):
            for x1 in range(limit + 1):
                for y1 in range(limit + 1):
                    # exclude cases where the "triangle" is a line
                    if x0*y1 - x1*y0 == 0:
                        continue
                    # dot product (check for right angle at (x0, y0))
                    if (0 - x0)*(x1 - x0) + (0 - y0)*(y1 - y0) == 0:
                        result += 1
    return result


if __name__ == '__main__':
    print(p91(50))
