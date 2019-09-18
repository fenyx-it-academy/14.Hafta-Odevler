scores=[100 , 90 , 90, 80, 75 , 60]
alice=[50, 65, 77, 90, 102]
scores = sorted( set( scores ) , reverse = True )
k = len( scores )
for i in alice:
    while k > 0 and i >= scores[k - 1]:
        k-= 1
    print (k+1)
    
# for i in alice:
#     scores.append ( i )
#     scores = sorted(list ( set(scores) ))
#     scores.sort(reverse = True)
#     print( scores.index( i ) + 1 )
#     scores.remove( i )
# ****************************************
# s=0
# while s<len(alice):
#     kutu = []
#     scores.append(alice[s])
#     scores.sort(reverse = True)
#     sayi=1
#     for i in range(len(scores)):
#         if scores[i]==scores[i-1]:
#
#             kutu+=[sayi]
#         else:
#
#             kutu+=[sayi]
#             sayi += 1
#     # print(kutu)
#     print(kutu[scores.index(alice[s])])
#     # print ( scores )
#     scores.remove(alice[s])
#     # print(sayi)
#     # print(scores)
#     s += 1
#     continue
#**************************************

