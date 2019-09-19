def formingMagicSquare(s):
    n = [s[i][j] for i in range(3) for j in range(3)]
    all_n = [[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4],[4,9,2,3,5,7,8,1,6],[2,9,4,7,5,3,6,1,8],[8,3,4,1,5,9,6,7,2],[4,3,8,9,5,1,2,7,6],[6,7,2,1,5,9,8,3,4],[2,7,6,9,5,1,4,3,8]]

    total_sum = []
    for l in all_n:
        total_sum.append(sum( [abs(n[i]-l[i])for i in range(9)]))
        total_sum.sort()
    return total_sum[0]

s = []
for _ in range(3):
    s.append(list(map(int, input(":").rstrip().split())))

result = formingMagicSquare(s)
print(result)


"""2. Soruyu şöyle bir çevirmiştik
sihirli kare olarak tanımlanan bir matris varmış, Öyle ki 
- Bu karenin her elemanı birbirinden farklı olacak ve elemanlar 1’den n^2’ye kadar değer alabilecek.
- Seçilen herhangi bir satır, sütun ve köşegendeki sayıların toplamı hep aynı sayıyı verecek (sihirli sabit-magic constant)
—Bizim durumda, 3 x 3’lük bir matris verilecek, elemanlar 1’den 9’a kadar olacak. Bizden rastgele verilen Matrisi, en az masrafla, sihirli kareye çevirmemiz isteniyor. a sayısını, b şahısına çevirmenin masrafı mutlak a-b.

Tam çevirisi değil, açıklamalı ama iş görür heralde"""
