#soru1(Drawing Book)
n = int(input())
p = int(input())
def sayfa(a):
    if a%2==0:
        return a/2
    return (a-1)/2

print(int(min((sayfa(n)-sayfa(p)),sayfa(p))))

#soru(magic square)
#bu sorunun cevabinda belki cok yer kisaltilabilir.simdilik bu sekliyle kalsin

#  a  b  c
#  d  e  f
#  g  h  k

# a c g k cift
cift=[2,4,6,8]
# b d f h tek
tek=[1,3,7,9]
ciftlerdortlu=[]
teklerdortlu=[]
cozum_kumesi=[]
for a in cift:
    for c in cift:
        for g in cift:
            for k in cift:
                if a+k==10 and c+g==10 and a!=k and a!=c and  a!=g and c!=k and c!=g and g!=k:
                    ciftlerdortlu.append([a,c,g,k])

for b in tek:
    for d in tek:
        for f in tek:
            for h in tek:
                if b+h==10 and d+f==10 and b!=d and b!=f and b!=h and d!=f and d!=h and f!=h:
                    teklerdortlu.append([b,d,f,h])

for [a,c,g,k] in ciftlerdortlu:
    for [b,d,f,h] in teklerdortlu:
        if a+d+g==15 and g+h+k==15 and k+f+c==15 and c+b+a==15:
            cozum_kumesi.append([a,b,c,d,5,f,g,h,k])

s = []
for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

tamliste=[s[i][j] for i in range(3) for j in range(3)]
farklar=[]
for i in range(8):
    farklar.append(sum(abs(tamliste[j]-cozum_kumesi[i][j])for j in range(9)))

print(min(farklar))

#soru (leader board)
#iki tip cozum ama ikiside hiz testinden gecemedi
#cozum1
scores_count = int(input())
scores = list(set(map(int, input().rstrip().split())))
scores.sort(reverse=True)
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))

alt_sinir=len(scores)-1
siradki_sayi_ayni=alt_sinir
for i in range(len(alice)):
    if alice[i]==alice[i-1] and i>0:
        print(siradki_sayi_ayni)
    else:
        while True:
            if alice[i] < scores[alt_sinir]:
                print(alt_sinir + 2)
                siradki_sayi_ayni = alt_sinir + 2
                break
            elif alice[i] == scores[alt_sinir]:
                print(alt_sinir + 1)
                siradki_sayi_ayni = alt_sinir + 1
                break
            else:
                alt_sinir -= 1
                if alt_sinir == 0:
                    print("1")
                    break
#cozum2
scores_count = int(input())
scores = list(set(map(int, input().rstrip().split())))
scores.sort(reverse=True)
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))

alt_sinir=len(scores)-1
for alie in alice:
    while True:
        if alie < scores[alt_sinir]:
            print(alt_sinir + 2)
            break
        elif alie == scores[alt_sinir]:
            print(alt_sinir + 1)
            break
        else:
            alt_sinir -= 1
            if alt_sinir == 0:
                print("1")
                break


