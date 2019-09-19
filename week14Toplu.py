#Soru 1
def pageCount(n, p):
    p_first=[]
    p_last=[]
    p_total=[]
    if n-p == 1 and p % 2 == 0:
        p = 0
        k=1
        p_last.append(p)
        p_first.append(k)
    elif p % 2 == 0:
        p_first.append((((p-1)//2))+1)
        p_last.append(((n-p))//2)
    elif n-p == 1 and p % 2 != 0:
        if n == 2:
            p = 0
            k= 0
            p_last.append(p)
            p_first.append(k)
        else:
            p = 1 #6 ya 5 hata veriyor ikisini de bir yaparrsan 2 ye 1 hata veriyor
            k=1
            p_last.append(p)
            p_first.append(k)
    elif p % 2 !=0:
        p_first.append((((p - 1) // 2)))
        p_last.append(((n - p) ) // 2)
    p_total = (min(p_last, p_first))
    return print(p_total[0])

#soru2

def formingMagicSquare(s):
    matris = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
              [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
              [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
              [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
              [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
              [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
              [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
              [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

    total = []
    for k in matris:
        m = 0
        fark = []
        for i in range(3):
            for j in range(3):
                fark.append(abs(s[i][j] - k[i][j]))
        for i in fark:
            m += i
        total.append(m)
    return min(total)

#soru3

def climbingLeaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse=True)
    # print(scores)
    ranking = []

    for i in alice:
        rank = 1
        for j in scores:
            if i < j:
                rank += 1
            if i == j:
                pass
            if i > j:
                break
        ranking.append(rank)
    for f in ranking:
        print(f)


scores_count = int(input())

scores = list(map(int, input().rstrip().split()))

alice_count = int(input())

alice = list(map(int, input().rstrip().split()))
climbingLeaderboard(scores, alice)
