import bisect
scores = [100,100,100,50,50,50,40,40,20,10]
alice = [5,25,50,120]
scores = sorted(list(set(scores)))
[print(abs(bisect.bisect(scores,i)-(len(scores)+1))) for i in alice]

## Hacker rank daki cozum
# import bisect
# scores_count = int(input())
# scores = list(map(int, input().rstrip().split()))
# alice_count = int(input())
# alice = list(map(int, input().rstrip().split()))
# scores = sorted(list(set(scores)))
# [print(abs(bisect.bisect(scores,i)-(len(scores)+1))) for i in alice]