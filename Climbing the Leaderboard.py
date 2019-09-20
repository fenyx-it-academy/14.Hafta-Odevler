
def ilk_siralama(*args): #ilk siralamayi almak icin bir liste tanimliyorum
    global siralama      #Bunu def le almak cok kolay o yuzden bu sekilde aliyorum.
    siralama=list(args)
    siralama.sort(reverse=True)
    

def alice(*args):   #ayni sekilde bu kolayliktan dolayi alice in notlarini da boyle aliyorum
    global siralama2#bu listeleri liste seklinde kullanabilmek icin global tanimliyorum
    siralama2=list(args)
    siralama2.sort() #Kucukten buyuge kullanabilmek icin burada siraliyorum
   

def after_alice():
    ilk_siralama(100,90,90,80,75,60) #istedigim verileri aliyorum
    alice(50,65,77,90,102)
    for i in range(len(siralama2)): #sirasiyla alice in verilerini ilk listeye ekliyorum
        a=siralama2[i]
        siralama.append(a)
        yenisiralama=[]
        for k in siralama:  #siralama yapmak icin yeni bir liste olusturup tekrar eden verileri siliyorum.Boylece siralama yapmam kolaylasiyor.
            if not k in yenisiralama:
                yenisiralama.append(k)
                yenisiralama.sort(reverse=True)
        print(yenisiralama.index(a)+1) #ekledigim verinin index numarasinin bir fazlasi onun siralamasi oluyor
        
        
    

after_alice()


    

    





    
    
    
    
