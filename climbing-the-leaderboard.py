def climbingLeaderboard(alice,scores):
    alice.sort()
    scores = sorted(set(scores),reverse=True)
    for i in alice:
        sayac = 1
        for x in scores:
            if x>i:
                sayac+=1
            elif x<i:
                break
            else:
                pass
        print(sayac)
scores_count = int(input())
scores = list(map(int, input().rstrip().split()))
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))
result=climbingLeaderboard(alice,scores)