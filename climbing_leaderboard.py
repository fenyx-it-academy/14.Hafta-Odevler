def climbingLeaderboard():
    no_of_players = int(input())
    scores = list(map(int, input().split()))
    no_of_games_alice_played = int(input())
    alice = list(map(int, input().split()))
    scores = sorted(list(set(scores)), reverse=True)

    for alices_score in alice:
        rank = len(scores)+1
        for score in scores:
            if alices_score >= score:
                rank -= 1
        print(rank)


climbingLeaderboard()
