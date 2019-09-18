squars = [[8,1,6,3,5,7,4,9,2],
          [8,3,4,1,5,9,6,7,2],
          [4,9,2,3,5,7,8,1,6],
          [4,3,8,9,5,1,2,7,6],
          [6,7,2,1,5,9,8,3,4],
          [6,1,8,7,5,3,2,9,4],
          [2,9,4,7,5,3,6,1,8],
          [2,7,6,9,5,1,4,3,8]]

def formingMagicSquare():
    s=list(map(int, input().rstrip().split()))
    print(s)
    all_dif=[]
    for i in range(8):
        dif = 0
        for j in range(9):
            print(s[j],squars[i][j])
            dif+=abs(s[j]-squars[i][j])
        all_dif.append(dif)
    print(all_dif)
    print(min(all_dif))

formingMagicSquare()

# from itertools import *
#
# X = []
# X.extend(list(map(int,input().split())))
# X.extend(list(map(int,input().split())))
# X.extend(list(map(int,input().split())))
#
# Ans = 81
# for P in permutations(range(1,10)):
#     print(P)
#     if sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and P[0] + P[4] + P[8] == 15 and (P[2] + P[4] + P[6] == 15):
#         Ans = min(Ans, sum(abs(P[i] - X[i]) for i in range(0,9)))
# print(Ans)
#
