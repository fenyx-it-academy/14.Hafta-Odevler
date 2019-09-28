
"""
14.Hafta 3.odev

@author: ensarbaltas
"""
import random
#oyuncu sayisi random.randint ile secildi
oyuncusayisi=random.randint(2,4)
#print('oyuncusayisi ',oyuncusayisi)
scores=[]
count1=0
while count1<oyuncusayisi:
    scores+=[random.randrange(5,120,5)]
    scores.append(random.randrange(5,120,5))
    scores.sort()
    scores.reverse()
    count1+=1  
print('Bu dongude oyuncu puanlari random ile rastgele secildi \n')
n=len(scores)
#print('n ',n)
print('General scores :',scores,'\n')
#oyun sayisi random.randint ile secildi. 
oyunsayisi=random.randint(2,oyuncusayisi) 
#print('oyunsayisi ',oyunsayisi)
#Alice'nin puanlari random.randrange ile secildi
alice=[]
count2=0
while count2<oyunsayisi:
    alice+=[random.randrange(5,120,5)]
    alice.append(random.randrange(5,120,5))
    alice.sort()
    alice.reverse()
    count2+=1
#Bu dongude Alice'nin puanlari rastgele secildi
m=len(alice)
#print('m ',m)
print('Alice scores :',alice,'\n')
#Burada oyuncu siralamasi yapildi
oyuncusirasi=[]
sira1=[]
for i in scores:
    if i not in oyuncusirasi:
        oyuncusirasi+=[i]
        sira1+=[len(oyuncusirasi)]
#print('oyuncusirasi ',oyuncusirasi)
#print('sira1',sira1)
#Burada oyun puanlari ile alice nin puanlari birlestirildi
toplamsira=scores+alice
toplamsira.sort()
toplamsira.reverse()  
tekrarsizliste=[]
sira2=[]
#Asil siralama icin tekrarsiz liste olusturuldu
for i in toplamsira:
    if i not in tekrarsizliste:
        tekrarsizliste+=[i]
        sira2+=[len(tekrarsizliste)]
sira2.reverse()

#print('toplamsira ',toplamsira)
#print('tekrarsizliste ',tekrarsizliste)
#print('sira2',sira2)
#Tekrarsiz listeden hareketle alice nin sirasi tesbit edildi.
sonuc=[]
aliceninsirasi=[]
count3=0
for i in alice:
    if i in tekrarsizliste:
        sonuc+=[tekrarsizliste.index(i)]
for i in sonuc:
    i+=1
    aliceninsirasi+=[i]
aliceninsirasi.reverse()    
print("Alice'in sirasi : \n",*aliceninsirasi, sep='\n')















    
