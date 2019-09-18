liste = []
def countRank(scores, i):
    count = 0
    rank = 0
    for j in scores:
        if j not in liste:
            liste.append(j)
            count += 1
            if j == i:
                rank = count
    liste.clear()
    return rank


def climbingLeaderboard(scores, alice):
    total_ranks = []
    for i in alice:
        scores.append(i)
        scores.sort(reverse=True)
        count_of_rank = countRank(scores, i)
        total_ranks.append(str(count_of_rank))
        scores.remove(i)

    total_ranks = '\n'.join(total_ranks)
    return print(total_ranks)


scores_count = int(input('ScoresCount:'))

scores = list(map(int, input('Scores: ').rstrip().split()))

alice_count = int(input('AliceCount: '))

alice = list(map(int, input('AliceScores: ').rstrip().split()))

result = climbingLeaderboard(scores, alice)



