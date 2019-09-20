def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)),reverse=True)
    list1 = []
    x= len(scores) - 1
    for i in alice:
        while x >= 0:
            if i >= scores[x]:
                x -= 1
            else:
                list1.append(x + 2)
                break
        if x< 0:
            list1.append(1)
    return list1



scores =  list(map(int, "100 100 50 40 40 20 10".rstrip().split()))#scores of other players#
alice = list(map(int, "5 25 50 120".rstrip().split()))#alices scores#
results= climbingLeaderboard(scores, alice)
for i in results:
    print(i)#ranks of alice in each situation#
