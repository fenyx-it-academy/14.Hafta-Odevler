import random
scores=[100,90,90,80,75,60]
alice=[50,65,77,90,102]
x=set(scores)
y=list(x)
random.shuffle(alice)
print(alice)
y.sort()
sonuc=[]
def climbingLeaderboard(scores, alice):
    x=set(scores)
    y=list(x)
    y.sort()
    result=[]
    for i in alice:
        if i in y:
            result.append(len(y)-y.index(i))
            continue
        else:
            y.append(i)
            y.sort()
            a=y.index(i)
            y.remove(i)
            result.append(len(y)-(a-1))
            continue
    return print(result)



climbingLeaderboard(scores,alice)