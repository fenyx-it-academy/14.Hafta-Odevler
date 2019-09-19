print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

n = int(input())
p = int(input())


def pageCount(n, p):
    pages = min(p // 2, n // 2 - p // 2)
    return print(pages)


pageCount(n, p)
