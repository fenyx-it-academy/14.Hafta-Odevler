print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

scores_count = int(input())
scores = list(map(int, input().split()))
alice_count = int(input())
alice = list(map(int, input().split()))

def climbingLeaderboard(scores, alice):
    scores = sorted(set(scores), reverse=True)
    length = len(scores)

    for i in alice:
        while (length > 0) and (i >= scores[length - 1]):
            length -= 1
        print(length + 1)

climbingLeaderboard(scores, alice)
