n=int(input()) #istenen inputlari aliyorum. 
p=int(input())
if n-p>p:      #sayfa sayilarinin farkinin buyuk oldugu yeri belirliyorum.
    if p%2==0: #bu ihtimale giriyorsa bastan cevirmeye basliyorum. 
        answer=p/2  #fonksiyonlastirdigimda bu verilere ulastim. 
        print(int(answer)) #sayfa sayisinin tek ve ya cift olmasi islemi degistiriyor
    else:                  #bu yuzden her ikisinde de ayri tanimlandi.ilk kisimda tek if else blogu olmasinin nedeni 1 den basladiginin bilinmesi ve 1 in tek olmasi. 
        answer=(p-1)/2
        print(int(answer))

else:
    if n%2==0:       
        if p%2==0:    
            answer=((n-p)/2)-1
            print(int(answer))
        else:
            answer=(((n-p)+1)/2)-1
            print(int(answer))
    else:
        if p%2==0:
            answer=((n-p)-1)/2
            print(int(answer))
        else:
            answer=(n-p)/2
            print(int(answer))
        
