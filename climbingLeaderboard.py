# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)), reverse=True)
    liste = []
    t = len(scores) - 1
    for i in alice:
        while t >= 0:
            if i >= scores[t]:
                t -= 1
            else:
                liste.append(t + 2)
                break
        if t < 0:
            liste.append(1)
    return liste


scores_count = 7 # int(input())
scores =  list(map(int, "100 100 50 40 40 20 10".rstrip().split()))
alice_count = 4
alice = list(map(int, "5 25 50 120".rstrip().split()))
result = climbingLeaderboard(scores, alice)
for i in result:
    print(i)


