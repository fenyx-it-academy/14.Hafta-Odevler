from itertools import permutations
kar=[]
kar.extend(map(int, input().rstrip().split()))
kar.extend(map(int, input().rstrip().split()))
kar.extend(map(int, input().rstrip().split()))

liste = [x for x in range(1,10)]
ihtimal = list(permutations(liste))
matris = []
for i in ihtimal:
    yeni=[]
    for b in range(3):
        yeni+=[sum([i[a] for a in range(b,9,3)])==15]
        yeni+=[sum([i[d] for d in range(b*3,3+b*3)])==15]
    yeni+=[sum([i[z] for z in range(0,9,4)])==15]
    yeni+=[sum([i[f] for f in range(2, 7, 2)])==15]
    if False not in yeni:
        matris += [i]

sonuc=[sum(abs(a-b) for a,b in zip(kar,i)) for i in matris]
print(min(sonuc))

