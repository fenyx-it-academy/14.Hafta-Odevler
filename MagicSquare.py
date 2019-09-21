def magicSquareMaker():
    for a in range(1, 10):
        for b in range(1, 10):
            if set([a, 15 - a - b, b, 5 + b - a, 5, 5 + a - b, 10 - b, a + b - 5, 10 - a]) == set(range(1, 10)):
                magicSquares.append([a, 15 - a - b, b, 5 + b - a, 5, 5 + a - b, 10 - b, a + b - 5, 10 - a])


def minCostCalculator():
    min_cost = 0
    costs = []

    for item in magicSquares:
        k = 0
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - item[j+k])
            k += 3
        costs.append(cost)
        min_cost = min(costs)
    return min_cost


# Complete the formingMagicSquare function below.
def formingMagicSquare():
    magicSquareMaker()
    print(minCostCalculator())


magicSquares = []
s = []


for _ in range(3):
    s.append(list(map(int, input().split())))

# magicSquareMaker()
# minCostCalculator()
formingMagicSquare()
