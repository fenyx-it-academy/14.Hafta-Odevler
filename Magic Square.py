# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    li=[[8, 1, 6,3, 5, 7, 4, 9, 2],
    [6, 1, 8,7, 5, 3, 2, 9, 4],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [2, 7, 6, 9, 5, 1, 4, 3, 8]]
    bos=[]
    for i in s:
        for j in i:
            bos.append(j)
    diff=[]
    for i in li:
        fark = 0
        for j in range(9):
            if bos[j]==i[j]:
                pass
            else:
                fark+=abs(bos[j]-i[j])
        diff.append(fark)
    return(min(diff))
formingMagicSquare()