#Drawing Book
#https://www.hackerrank.com/challenges/drawing-book/problem
def pageCount(n, p):
    sayfalar_bastan=[i for i in range(1,p,2)]

    sayfalar_sondan=[]
    if n % 2== 0:
        sayfalar_sondan=[i  for i in range(n,p,-2) ]
    else:
        sayfalar_sondan = [i for i in range(n-1, p, -2)]

    if len(sayfalar_bastan)>len(sayfalar_sondan):
        return len(sayfalar_sondan)
    else:
        return len(sayfalar_bastan)


n = int(input())
p = int(input())
result = pageCount(n, p)
print(result)