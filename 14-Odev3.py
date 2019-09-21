# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 01:04:24 2019

@author: HP
"""

#Alice bir arcade oyunu oynuyor ve skor tablosunun tepesine tırmanmak istiyor ve sıralamasını izlemek istiyor. 
#Oyun, Yoğun Sıralamayı kullanıyor ve lider tablosu şöyle çalışıyor:

#En yüksek puana sahip olan oyuncu skor tablosunda 1 numaradır.
#Eşit puan alan oyuncular aynı sıralama numarasına sahip olur ve bir sonraki oyuncu hemen sıradaki numarayı alır.
#Örneğin, lider panosundaki dört oyuncunun puanları 100, 90, 90 ve 80'dir. 
#Bu oyuncular sırasıyla 1,2, 2 ve 3 dereceye sahip olacaklar. 
#Alice'in puanı 70, 80 ve 105 ise, her maçtan sonraki sıralaması 4., 3. ve 1..

def climbingLeaderboard(scores, alice):
    alice.sort()    # liste olarak kucukten buyuge dizelim
    scores=list(set(scores)) # Kume yaparak ortak elemanlari cikardik
    scores.sort()      # Kucukten buyuge
    scores.reverse()   # Tersine cevir
    #print(scores)
    
    boyut=len(scores)
    for puan in alice:
        while (boyut>0) and (puan >= scores[boyut-1]):
            boyut-=1
        print(f'{puan} puanina gore sira =',boyut+1)


if __name__ == '__main__':
    scores_count = int(input('Tablodaki kisi sayisi ='))
    scores = list(map(int, input('Skorlari birer bosluk birakarak giriniz ;').rstrip().split()))
    alice_count = int(input('Alice in mac sayisi ='))
    alice = list(map(int, input('Alice in skorlarini birer bosluk birakarak giriniz ;').rstrip().split()))

    climbingLeaderboard(scores, alice)