def pageCount(n, p):
    numofpages=[]
    sayac=0
    x=0
    y=0
    for i in range(n+1):
        numofpages+=[i]
    for i in numofpages:
        if i==p:
            x=p/2.0001
    for i in numofpages[::-1]:
        if p==numofpages[-2]:
            x=0
        sayac+=1
        if i==p:
            y=sayac/2.01
    if x > y:
        print(round(y))
    else:
        print(round(x))
while True:
    n = int(input())
    p = int(input())
    if n<1 or n>10**5:
        print('again input n')
        continue
    if p<1 or p>n :
        print('again input p')
        continue
    break
result=pageCount(n,p)
