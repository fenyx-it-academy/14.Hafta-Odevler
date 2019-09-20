a1=[[8,1,6],[3,5,7],[4,9,2]]   #sadece 3x3 luk versiyonunu yapabildim.Bu versiyonun tum hallerini tanimladim
a2=[[8,3,4],[1,5,9],[6,7,2]]   
a3=[[6,1,8],[7,5,3],[2,9,4]]
a4=[[4,3,8],[9,5,1],[2,7,6]]
a5=[[4,9,2],[3,5,7],[8,1,6]]
a6=[[6,7,2],[1,5,9],[8,3,4]]
a7=[[2,9,4],[7,5,3],[6,1,8]]
a8=[[2,7,6],[9,5,1],[4,3,8]]

liste=[[0,0,0],[0,0,0],[0,0,0]]
liste[0][0]=int(input())
liste[0][1]=int(input())
liste[0][2]=int(input())
liste[1][0]=int(input())
liste[1][1]=int(input())
liste[1][2]=int(input())
liste[2][0]=int(input())
liste[2][1]=int(input())
liste[2][2]=int(input())
print(liste) #benden istenen karsilastirmasi yapilan matris

 



#Ardindan da farkli olanlarin farkini bulup,mutlak degerini alip, bu fark kismina ekliyorum.Boylece toplam buluyorum. 
a1fark=0
for i in range(3):
    for k in range(3):
        a1fark+=abs(liste[i][k]-a1[i][k])

a2fark=0
for i in range(3):
    for k in range(3):
        a2fark+=abs(liste[i][k]-a2[i][k])

a3fark=0
for i in range(3):
    for k in range(3):
        a3fark+=abs(liste[i][k]-a3[i][k])

a4fark=0
for i in range(3):
    for k in range(3):
        a4fark+=abs(liste[i][k]-a4[i][k])

a5fark=0
for i in range(3):
    for k in range(3):
        a5fark+=abs(liste[i][k]-a5[i][k])
        
a6fark=0
for i in range(3):
    for k in range(3):
        a6fark+=abs(liste[i][k]-a6[i][k])
        
a7fark=0
for i in range(3):
    for k in range(3):
        a7fark+=abs(liste[i][k]-a7[i][k])
        
a8fark=0
for i in range(3):
    for k in range(3):
        a8fark+=abs(liste[i][k]-a8[i][k])

karsilastirma=[]   #farklari bir listeye atiyorum
karsilastirma.extend([a1fark,a2fark,a3fark,a4fark,a5fark,a6fark,a7fark,a8fark])
en_kucuk_fark=min(karsilastirma) #liste icinden en kucuk farki cekiyorum.

print(en_kucuk_fark)


        
        
