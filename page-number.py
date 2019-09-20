#
# Complete the pageCount function below.
#
class Page:
    def __init__(self, left, right):
        self.leftPage = left
        self.rightPage = right

class Book:
    def __init__(self, pageNumber):
        self.pages = []
        if pageNumber > 0:
            firstPage = Page(0, 1)
            self.pages.append(firstPage)
            for i in range(2, pageNumber + 1, 2):
                if (i < pageNumber):
                    self.pages.append(Page(i, i + 1))
                else:
                    self.pages.append(Page(i, -1))



def pageCount(n, p):
    book = Book(n)
    frontCount = 0 # onden cevirdigimizde kac adim attik
    backCount = 0 # arkadan cevirdigimizde kac adim attik
    for page in book.pages: #onden baslarsak
        if page.leftPage == p or page.rightPage == p:
            break
        frontCount += 1
    book.pages.reverse()
    for page in book.pages:
        if page.leftPage == p or page.rightPage == p:
            break
        backCount += 1
    return min(frontCount, backCount)

print(pageCount(83246, 78132))