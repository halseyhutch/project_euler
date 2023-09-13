# see https://en.wikipedia.org/wiki/Pythagorean_triple
from math import sqrt, gcd


def p86(limit, M_max):
    counts = [0 for _ in range(M_max + 1)]
    # max perimeter of the triangle
    p_max = (3 + sqrt(5)) * M_max
    # maximum m for pythagorean triples in form (m^2 + n^2, m^2 - n^2, 2 * m * n)
    m_max = int((sqrt(2 * p_max + 1) - 1) / 2)

    # this was improved after browsing other approaches on the forum
    for m in range(2, m_max + 1):
        n_min = 2 if m & 1 else 1
        for n in range(n_min, m, 2):
            if gcd(m, n) == 1:
                x, y = m**2 - n**2, 2 * m * n
                a, b = min(x, y), max(x, y)
                if b <= 2 * a:
                    for x in range(1, M_max // a + 1):
                        counts[x * a] += -(x * b) // 2 + x * a + 1
                for x in range(1, M_max // b + 1):
                    counts[x * b] += (x * a) // 2

    num_sols = 0
    for M, count in enumerate(counts):
        num_sols += count
        if num_sols > limit: return M
    return None


if __name__ == '__main__':
    print(p86(1_000_000, 2000))
