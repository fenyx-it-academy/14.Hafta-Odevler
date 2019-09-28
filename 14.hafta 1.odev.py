#14.hafta 1.odev
import random

def pageCount(n, p):
    if n-p==1 and n % 2 != 0:  #n ile p arasindaki fark 1 ise ve n tek ise hatali sonuc cikmamasi icin n bir azatildi
        n-=1
    if n-p==1 and n % 2 == 0:  #n ile p arasindaki fark 1 ise ve n cift ise hatali sonuc cikmamasi icin n bir azatildi
        n+=1    
    if n>p and n % 2 != 0 and p % 2 == 0: # ayni sekilde hata engellendi
        n -= 1
    #tum hatalar ayiklandiktan sonra sayfa cevirmeye gecildi
    if p<n-p :
        turn=(p//2)
        print('soldan ',turn )
    elif p>n-p:
        turn=((n-p)//2)
        print('sagdan ',turn)
    else:
        turn=(p//2)
        print('soldan ',turn)
    return turn
#n ve p degerlerini random kullanarak rasgele cagirdik
n=random.randint(10,20)  
p=random.randint(1,10)
pageCount(n,p)

