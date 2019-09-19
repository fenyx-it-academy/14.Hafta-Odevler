##def solve(n, p):
##    sayfa_sayisi=p//2
##    gidilecek_sayfa=n//2
##    return min(p//2, n//2 - p//2)
##    return min(sayfa_sayisi, gidilecek_sayfa-sayfa_sayisi)
##n = int(input("kitabin toplam sayfa sayisini giriniz:").strip())
##p = int(input("kitabda gitmek istediginiz sayfa numarasini giriniz:").strip())
##result = solve(n, p)
##print(result)
##




def pageCount(n, p):
    sayfa_sayisi=p//2
    gidilecek_sayfa=n//2
    return min(p//2, n//2 - p//2)
    return min(sayfa_sayisi, gidilecek_sayfa-sayfa_sayisi)
    

n = int(input())
p = int(input())
result = pageCount(n, p)




 
