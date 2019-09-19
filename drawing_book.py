n=int(input('sayfa sayisini giriniz :'))
p=int(input('gitmek istediginiz sayfaya giriniz :'))
x1=n//2
k=(n-p)//2
if n<=2:
    print(0)
elif n%2==0 and n-p==1:
    print(1)
elif k<(x1-k):

    print(k)
else:
    print(x1-k)
