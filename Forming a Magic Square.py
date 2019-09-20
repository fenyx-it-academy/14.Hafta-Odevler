a1=[[8,1,6],[3,5,7],[4,9,2]]   #sadece 3x3 luk versiyonunu yapabildim.Bu versiyonun tum hallerini tanimladim
a2=[[8,3,4],[1,5,9],[6,7,2]]   
a3=[[6,1,8],[7,5,3],[2,9,4]]
a4=[[4,3,8],[9,5,1],[2,7,6]]
a5=[[4,9,2],[3,5,7],[8,1,6]]
a6=[[6,7,2],[1,5,9],[8,3,4]]
a7=[[2,9,4],[7,5,3],[6,1,8]]
a8=[[2,7,6],[9,5,1],[4,3,8]]

    

liste=[[4,8,2],[4,5,7],[6,1,6]] #benden istenen karsilastirmasi yapilan matris

 
a1ayni=[]#karsilastirma yapmak icin herbir versiyon icin ortak eleman hangisinde en fazla onu bulup bir listeye atiyorum. 
a1fark=0 #Ardindan da farkli olanlarin farkini bulup bu fark kismina ekliyorum.Boylece toplam buluyorum. 
for i in range(3):
    for k in range(3):
        if a1[i][k]==liste[i][k]:
            a1ayni.append(a1[i][k])
            
        else:
            a1fark+=abs(liste[i][k]-a1[i][k])

a2ayni=[]
a2fark=0
for i in range(3):
    for k in range(3):
        if a2[i][k]==liste[i][k]:
            a2ayni.append(a2[i][k])
            
        else:
            a2fark+=abs(liste[i][k]-a2[i][k])
            

a3ayni=[]
a3fark=0
for i in range(3):
    for k in range(3):
        if a3[i][k]==liste[i][k]:
            a3ayni.append(a3[i][k])
            
        else:
           a3fark+=abs(liste[i][k]-a3[i][k])
            

a4ayni=[]
a4fark=0

for i in range(3):
    for k in range(3):
        if a4[i][k]==liste[i][k]:
            a4ayni.append(a4[i][k])
            
        else:
            a4fark+=abs(liste[i][k]-a4[i][k])

a5ayni=[]
a5fark=0
for i in range(3):
    for k in range(3):
        if a5[i][k]==liste[i][k]:
            a5ayni.append(a5[i][k])
            
        else:
            a5fark+=abs(liste[i][k]-a5[i][k])
        

a6ayni=[]
a6fark=0
for i in range(3):
    for k in range(3):
        if a6[i][k]==liste[i][k]:
            a6ayni.append(a6[i][k])
            
        else:
            a6fark+=abs(liste[i][k]-a6[i][k])

a7ayni=[]
a7fark=0
for i in range(3):
    for k in range(3):
        if a7[i][k]==liste[i][k]:
            a7ayni.append(a7[i][k])
            
        else:
            a7fark+=abs(liste[i][k]-a7[i][k])

a8ayni=[]
a8fark=0
for i in range(3):
    for k in range(3):
        if a8[i][k]==liste[i][k]:
            a8ayni.append(a8[i][k])
            
        else:
            a8fark+=abs(liste[i][k]-a8[i][k])


karsilastirma=[]  #hangi versiyonun uyumlu oldugunu bulmak icin en cok uyum olan matrisi seciyorum.
s1=len(a1ayni)
s2=len(a2ayni)
s3=len(a3ayni)
s4=len(a4ayni)
s5=len(a5ayni)
s6=len(a6ayni)
s7=len(a7ayni)
s8=len(a8ayni)
karsilastirma.append(s1)
karsilastirma.append(s2)
karsilastirma.append(s3)
karsilastirma.append(s4)
karsilastirma.append(s5)
karsilastirma.append(s6)
karsilastirma.append(s7)
karsilastirma.append(s8)

if max(karsilastirma)==s1:   #karsilastirma sonucu en uyumlu matris icin farkli olanlarin farkini bulup topladigim fark toplamini yazdiriyorum.
    print(a1fark)
    
elif max(karsilastirma)==s2:
    print(a2fark)

elif max(karsilastirma)==s3:
    print(a3fark)

elif max(karsilastirma)==s4:
    print(a4fark)

elif max(karsilastirma)==s5:
    print(a5fark)

elif max(karsilastirma)==s6:
    print(a6fark)

elif max(karsilastirma)==s7:
    print(a7fark)

elif max(karsilastirma)==s8:
    print(a8fark)

    


    




            
        
