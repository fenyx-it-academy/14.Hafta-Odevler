#week14-
#hwk1:
val = []

n = int(input())

p = int(input())
def front(n, p):  # fronttan cevirinceyi hesaplemek icin
    if p%2 ==0:
        val.append(int(p/2))

    elif p !=n and p%2 !=0:
        val.append(int((p-1)/2))

def back(n, p):
    if n % 2 == 0 and n !=p :  #backteni hesaplamak icin.
        if p%2 ==0:
            val.append(int((n - p) / 2))
        else:
            val.append(int((n+1-p)/2))

    else:  #(if n%2 !=  0:)

        if p%2 ==0:
            val.append(int((n - (p+1)) / 2))

        else:
            val.append(int((n -p) / 2))

        # if b < 1:
        #     b = 0
        #     val.append(b)


def pageCount(n, p):
    if p ==1 or n == p:  # 1. ya da son sayfa olma exceptionu
        val.append(0)
    else:
        back(n, p)
        front(n,p)

    print(min(val))


pageCount(n, p)

###
#hwk2:  bu soruyuyu hackerrankte kabul etmedi.



# n x n   sum=n(n**2+1)/2
#Sum in each row & each column & in each diagonal = 3*(3**2+1)/2 = 15

magic_maxr   = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
               [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
               [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
               [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
               [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
               [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
               [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
               [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

s =[]

def formingMagicSquare(s):
    a = list(input('3 say gir'))
    b = list(input('3 say gir'))
    c = list(input('3 say gir'))
    s.extend(a, b, c)
    #soyle olmsi gerekiyor sum(a) == sum(b) == sum(c) == 15

    subt = []


    cost = []
    for x in magic_maxr:
        m = 0
        for i in range(3):
            for j in range(3):
                subt.append(abs(s[i][j] - x[i][j]))
        for i in subt:
            m += i
        cost.append(m)
    return min(cost)




#hwk3

#3u henuz yapamadim




