# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 01:05:00 2019

@author: HP
"""
# Brie’s Drawing teacher asks her class to open their books to a page number. Brie can either start turning pages 
# from the front of the book or from the back of the book. She always turns pages one at a time. 
# When she opens the book, page  is always on the right side. find and print the minimum number of pages 
#Brie must turn in order to arrive at page .

def pageCount(n, p):
    print('Bastan ;', p//2, 'yaprak cevirmeli')
    print('Sondan ;', (n//2)-(p//2),'yaprak cevirmeli')
    print(min(p//2, (n//2)-(p//2)))

if __name__ == '__main__':
    n = int(input('Kitabin sayfa sayisi ='))
    p = int(input('Istenilen sayfa numarasi giriniz ='))
    pageCount(n, p)
