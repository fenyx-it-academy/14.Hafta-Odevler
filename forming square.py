s=[[4,5,8],[2,4,1],[1,9,7]]

cozum_1=[[8, 1, 6], [3, 5, 7], [4, 9, 2]]
cozum_2=[[6, 1, 8], [7, 5, 3], [2, 9, 4]]
cozum_3=[[4, 9, 2], [3, 5, 7], [8, 1, 6]]
cozum_4=[[2, 9, 4], [7, 5, 3], [6, 1, 8]]
cozum_5=[[4, 3, 8], [9, 5, 1], [2, 7, 6]]
cozum_6=[[8, 3, 4], [1, 5, 9], [6, 7, 2]]
cozum_7=[[6, 7, 2], [1, 5, 9], [8, 3, 4]]
cozum_8=[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
coz1=[abs(i-j) for x,y in zip(cozum_1,s) for i,j in zip(x,y)]
coz2=[abs(i-j) for x,y in zip(cozum_2,s) for i,j in zip(x,y)]
coz3=[abs(i-j) for x,y in zip(cozum_3,s) for i,j in zip(x,y)]
coz4=[abs(i-j) for x,y in zip(cozum_4,s) for i,j in zip(x,y)]
coz5=[abs(i-j) for x,y in zip(cozum_5,s) for i,j in zip(x,y)]
coz6=[abs(i-j) for x,y in zip(cozum_6,s) for i,j in zip(x,y)]
coz7=[abs(i-j) for x,y in zip(cozum_7,s) for i,j in zip(x,y)]
coz8=[abs(i-j) for x,y in zip(cozum_8,s) for i,j in zip(x,y)]


print(min(sum(coz1),sum(coz2),sum(coz3),sum(coz4),sum(coz5),sum(coz6),sum(coz7),sum(coz8)))
