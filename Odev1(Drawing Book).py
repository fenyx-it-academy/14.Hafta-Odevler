def pageCount(n, p):
    if n%2==0 and p==(n-1):
        if n<3:
            print("0")
        else:
            print("1")
    elif n-p>p:
        print(p // 2)
    else:
        print((n-p)//2)

n = int(input("Kitabiniz kac sayfa olsun:"))
p = int(input("Kacinci sayfayi acmak istersiniz:"))
result = pageCount(n, p)