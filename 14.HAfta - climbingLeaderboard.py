def climbingLeaderboard():
    skor_sayısı = int(input())
    skor = list(map(int, input().rstrip().split()))
    alice_sayısı = int(input())
    alice = list(map(int, input().rstrip().split()))
    alice.sort()
    skor = sorted(set(skor), reverse=True)
    n=len(skor)
    for i in alice:
        while (n>0) and (i>=skor[n-1]):
            n-=1
        print(n+1)




sonuc=climbingLeaderboard()