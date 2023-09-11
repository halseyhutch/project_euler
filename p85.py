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
