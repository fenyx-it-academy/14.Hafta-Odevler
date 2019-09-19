def climbingLeaderboard():
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    scores = list(set(scores))  
    scores.sort(reverse=True)
    rankings = []
    for i in alice:
        count = 1
        for j in scores:
            if i > j:
                break
            elif i == j:
                pass
            elif i < j:
                count += 1
        rankings.append(count)
    for i in rankings:
        print(i)
climbingLeaderboard()