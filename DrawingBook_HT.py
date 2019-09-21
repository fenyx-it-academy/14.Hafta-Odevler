# n number of pages of the book, p the page to turn to.
def pageCount(n, p):
    return int((min(p/2, (n/2-p/2+1 if n%2 == 0 else n/2-p/2) if n - p == 1 else n/2-p/2)))


n = int(input('\nEnter n: '))
p = int(input('\nEnter p: '))
print(pageCount(n, p))
