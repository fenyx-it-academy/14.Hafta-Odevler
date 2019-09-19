# input istende ve split ile listeye donusturldu.
liste=(input("Lutfen karenizi olusturucak 1-9 a 9 rakami arada 1 bosluk birakarak giriniz.")).split()
# listedeki elemanlar matematiksel islem goreceginden int cevrildi.
yeni = [int(liste[i]) for i in range(9)]
# tum magic square olusturan degerleri bir liste yaptik.(kaynak google)
sihirlikareler= [[8,1,6,3,5,7,4,9,2], [6,1,8,7,5,3,2,9,4], [4,9,2,3,5,7,8,1,6], [2,9,4,7,5,3,6,1,8],
                 [8,3,4,1,5,9,6,7,2], [4,3,8,9,5,1,2,7,6], [6,7,2,1,5,9,8,3,4], [2,7,6,9,5,1,4,3,8]]
toplam = []
# bu dongude verilen listeyi tum sihirlikareler degerleriyle karsilastiriyoruz.
# her bir karsilastirma icin ayni konumdaki degerlerin farkini alip listede tutuyoruz.
# sonra bu degerleri toplayip onlarida toplam listesine ekliyoruz.
for i in sihirlikareler:
    toplam.append(sum([abs(yeni[j]-i[j]) for j in range(9)]))
print(min(toplam))
