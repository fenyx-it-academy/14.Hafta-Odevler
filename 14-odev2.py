# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 01:04:58 2019

@author: HP
"""
#Sihirli kareyi 1'den n ^ 2'ye kadar farklı pozitif tamsayı dizisi olarak tanımlarız; burada toplam veya 
#herhangi bir satır, sütun veya çapraz veya uzunluk n, her zaman aynı sayıya eşittir: sihirli sabiti.

#Size dahil olan aralıkta 3x3'lük bir matris veya tamsayılar verilecektir [1,9]. 
#Herhangi bir rakamı [1,9] aralığında herhangi bir b basamağına | a-b | . 
#Verildiğinde, minimum maliyetle sihirli bir kareye dönüştürün. Bu maliyeti yeni bir satıra yazdırın.

#Örneğin, şu matris s ile başlıyoruz:
#  5 3 4
#  1 5 8
#  6 4 2
#Bunu aşağıdaki sihirli kareye dönüştürebiliriz:
#  8 3 4
#  1 5 9
#  6 7 2
# Bu bir |5-8|+|8-9|+|4-7|=7 pahasına üç yedek aldı.
matris = [[8,1,6,3,5,7,4,9,2],
          [8,3,4,1,5,9,6,7,2],
          [4,9,2,3,5,7,8,1,6],
          [4,3,8,9,5,1,2,7,6],
          [6,7,2,1,5,9,8,3,4],
          [6,1,8,7,5,3,2,9,4],
          [2,9,4,7,5,3,6,1,8],
          [2,7,6,9,5,1,4,3,8]]

def formingMagicSquare(s):
    print(s)
    s2=[s[i][j] for i in range(3) for j in range(3)]
    print(s2)
    minumum_liste=[]
    
    for i in range(8):  # 8 satir
        satir_top=0
        for j in range(9): # 9 sutun
            fark=abs(s2[j]-matris[i][j])
            satir_top+=fark
        minumum_liste.append(satir_top)
    
    print(min(minumum_liste))


if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input('Matris elemanlarini giriniz ;').rstrip().split())))

    formingMagicSquare(s)