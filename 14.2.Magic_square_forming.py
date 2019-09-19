print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def formingMagicSquare():
    s = []
    [s.append(k) for _ in range(3) for k in list(map(int, input().split()))]


    values = []
    [values.append([a, 15 - a - b, b, 5 + b - a, 5, 5 + a - b, 10 - b, a + b - 5, 10 - a]) for a in range(1, 10)
     for b in range(1, 10) if {a, 15 - a - b, b, 5 + b - a, 5, 5 + a - b, 10 - b, a + b - 5, 10 - a}
     == set(range(1, 10))]
    # print(values)

    minimum = 100
    for i in values:
        cost = 0
        for j in range(9):
            cost += abs(i[j] - s[j])
        if cost < minimum:
            minimum = cost
    return print(minimum)


formingMagicSquare()

