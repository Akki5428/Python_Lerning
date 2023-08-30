"""
1.B
"""

"""
2.

A = int(input())
B = int(input())
i = 0
mul = 1
while i < B: 
    mul *= A
    i+=1
print(mul)     

"""

"""
3.Sum of digit

T = int(input())
i = 0
l = []
while i < T:
    N = int(input())
    sum = 0
    while N > 0 :
        n = N % 10
        sum = sum + n
        N //= 10  
    l.append(sum)
    i+=1

while j < T:
    print(l[0])
    j += 1

"""

"""
4.Table


A = int(input())

i = 1
while i <= 10:
    print(f"{A} * {i} = {A*i}")
    i+=1
"""

"""
5.Number of Digit
"""
T = int(input())
i = 0
l = []
while i < T:
    N = int(input())
    sum = 0
    count = 0
    while N > 0 :
        N //= 10 
        count += 1  
    l.append(count)
    i+=1
for x in l:
    print(x)