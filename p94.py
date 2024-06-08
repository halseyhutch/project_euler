# pell's equation, see p75

if __name__ == '__main__':
    print(sum([2 * round(0.5 * ((2 - 3 ** 0.5) ** i + (2 + 3 ** 0.5) ** i)) for i in range(2, 16)]))
