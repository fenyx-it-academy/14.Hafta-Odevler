#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 18:50:37 2019

@author: ensarbaltas
"""
liste=[1,2,3,4,5,6,7,8,9]
list=[]
s=list
n=15
def formingMagicSquare(s):
    for k in liste:
        for l in liste:
            for m in liste:
                if k+l+m==n and k!=l!=m:
                    list.append([k,l,m])
    sonliste=[]
    for i in list:
        for ii in i:
            for j in list:
                for jj in j:
                    for t in list:
                        for tt in t:
                            if ii+jj+tt==15:
                                if [ii,jj,tt] not in sonliste and ii!=jj and ii!=tt and jj!=tt:
                                    sonliste+=[[ii,jj,tt]]
    magicnumber=[]
    for x in sonliste:
        for y in sonliste:
            for z in sonliste:
                if x[0]+y[0]+z[0]==15:
                    if x[1]+y[1]+z[1]==15:
                        if x[2]+y[2]+z[2]==15:
                            if x[0]!=y[0] and x[0]!=z[0] and y[0]!=z[0] and x[1]!=y[1] and x[1]!=z[1] and y[1]!=z[1] and x[2]!=y[2] and x[2]!=z[2] and y[2]!=z[2]:
                                if  x[0]!=y[1] and x[0]!=z[1] and y[0]!=z[1] and x[1]!=y[2] and x[1]!=z[2] and y[1]!=z[2] and x[2]!=y[1] and x[2]!=z[1] and y[2]!=z[1]:
                                        magicnumber=[[x[0],y[0],z[0],x[1],y[1],z[1],x[2],y[2],z[2]]]
                                        
                                
    toplam=[]                    
    print(magicnumber)
    for p in magicnumber:
        toplam.append(sum([abs(liste[j]-p[j]) for j in range(9)]))
    print(min(toplam))                       
           
    
formingMagicSquare(s)
