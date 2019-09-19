def pageCount():
    n = int(input())
    p = int(input())
    if (n - p) < p and n % 2 == 0:      # n double and starting from the end of the book
        print(int(((n - 1) - p) / 2))
    elif (n - p) < p and n % 2 != 0:    # n single and starting from the end of the book
        print(int((n - p) / 2))
    elif (n - p) > p and n % 2 == 0:    # starting from the beginning of the book
        print(int(p / 2))
    elif (n - p) < p and n % 2 != 0:    # starting from the beginning of the book
        print(int(p / 2))
    elif n == p:
        print(int(n - p))
pageCount()