def climbingLeaderboard(scores, alice):
    yeniscorelist=sorted(list(set(scores)))[::-1]
    for i in alice:
        yeniscorelist.append(i)
        a=sorted(yeniscorelist)[::-1]
        print(a.index(i)+1)

scores_count = int(input())
scores = list(map(int, input().rstrip().split()))
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))
climbingLeaderboard(scores, alice)
