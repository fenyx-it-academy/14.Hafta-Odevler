def climbingLeaderboard():
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    s=sorted(set(scores),reverse=True)
    m=len(s)
    liste=[]
    for i in alice:
        while (m > 0) and i >= s[m-1]:
            m-=1
        liste.append(m+1)
    return liste
result = climbingLeaderboard()
print(result)
