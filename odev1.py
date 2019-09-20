#page count#

def pageCount():
    n = int(input("length of book:   "))
    p = int(input("page nubmber:  "))
    if n%2==0:
        print(min(p//2,(n+1-p)//2))
    else:
        print(min(p//2,(n-p)//2))
pageCount() 
