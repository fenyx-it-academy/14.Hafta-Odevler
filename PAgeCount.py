
def pageCount(n, p):
    tershesap=(n-p)
    if n-p>p or n-p==p:
        if p%2==0:
            return p//2
        else:
            return (p-1)//2
    else:
        if p%2==0:
            return tershesap//2
        else:
            return (tershesap+1)//2


n_book=int(input("kitabin n:"))
p_book=int(input("acilan p:"))
pageCount(n_book,p_book)