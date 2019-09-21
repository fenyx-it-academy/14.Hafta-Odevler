n = int(input())
p = int(input())

a = 0
b = 0
for i in range(2, p + 1, 2):
    a += 1
    if p == 1:
        a = 0
for i in range(n, p + 1, -2):
    b += 1
if n % 2 == 0 and n - 1 == p:
    b = 1
    
print(min(a, b))
