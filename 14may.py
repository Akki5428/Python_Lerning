"""a = 6
d = 7

def arthmeticprog(n):
    if n == 1:
        return a
    else:
        return arthmeticprog(n-1) + d

print(arthmeticprog(7))    
"""

a = 3
r = 4

def GP(n):
    if n == 1:
        return a
    else:
        return GP(n-1) * r

print(GP(3))