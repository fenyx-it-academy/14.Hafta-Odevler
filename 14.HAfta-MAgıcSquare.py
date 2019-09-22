A = [[8,1,6,3,5,7,4,9,2],
          [8,3,4,1,5,9,6,7,2],
          [4,9,2,3,5,7,8,1,6],
          [4,3,8,9,5,1,2,7,6],
          [6,7,2,1,5,9,8,3,4],
          [6,1,8,7,5,3,2,9,4],
          [2,9,4,7,5,3,6,1,8],
          [2,7,6,9,5,1,4,3,8]]

def formingMagicSquare():
    Q=list(map(int, input().rstrip().split()))
    print(Q)
    All=[]
    for i in range(8):
        dif = 0
        for j in range(9):
            print(Q[j],A[i][j])
            dif+=abs(Q[j]-A[i][j])
        All.append(dif)
    print(All)
    print(min(All))

formingMagicSquare()