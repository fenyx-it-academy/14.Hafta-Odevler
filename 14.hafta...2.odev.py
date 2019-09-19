def formingMagicSquare():
    x = []          # 3 x 3 entered numbers list
    for i in range(3):
        x += (list(map(int, input().rstrip().split())))
    a = 0           # Sum of numbers from 1 to 9
    n = 3           # 3 x 3  formingMagicSquare
    b = []          # List of numbers from 1 to 9
    for i in range(1, n ** 2 + 1):
        a += i
        b.append(i)
    c = []          # list of numbers whose totals are equal to 'a / n'
    for i in b:
        for j in b:
            for k in b:
                if i == j or i == k or k == j:
                    continue
                if i + j + k == a / n:
                    t = [i, j, k]
                    c.append(t)
    s = []        # 3 x 3 magic squares
    for i in c:
        for j in c:
            for k in c:
                if i[0] + i[1] + i[2] == j[0] + j[1] + j[2] == k[0] + k[1] + k[2] == \
                        i[0] + j[0] + k[0] == i[1] + j[1] + k[1] == i[2] + j[2] + k[2] == \
                        i[0] + j[1] + k[2] == i[2] + j[1] + k[0] \
                        and i[0] != j[1] != k[1] \
                        and i[0] != j[2] != k[1] \
                        and i[1] != j[0] != k[2] \
                        and i[2] != j[0] != k[1] \
                        and j[0] != k[0] \
                        and j[2] != k[2]:
                    t = [i[0], i[1], i[2], j[0], j[1], j[2], k[0], k[1], k[2]]
                    s.append(t)
    total_cost = []             # total_cost list
    for i in s:
        t = 0
        for j in range(len(i)):
            if i[j] != x[j]:
                t += abs(i[j] - x[j])
        total_cost.append(t)
    print(min(total_cost))      # minimal total cost choose
formingMagicSquare()