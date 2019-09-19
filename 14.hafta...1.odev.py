def pageCount():
    n = int(input())
    p = int(input())
    if n == p:
        print(n - p)
    elif (n - p) >= p :     # starting from the beginning of the book
        if n % 2 == 0 :
            print(int(p / 2))
        else:
            print(int(p / 2))
    elif (n - p) <= p :      # starting from the end of the book
        if n % 2 == 0 :
            print(int(((n - 1) - p) / 2 )+1)
        else:
            print(int((n - p) / 2))
pageCount()
