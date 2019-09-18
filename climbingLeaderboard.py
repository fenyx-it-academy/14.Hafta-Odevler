def climbingLeaderboard():
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    alice.sort()
    scores = sorted(set(scores), reverse=True)
    n=len(scores)
    for i in alice:
        while (n>0) and (i>=scores[n-1]):
            n-=1
        print(n+1)




result=climbingLeaderboard()