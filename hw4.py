'''
1.
A = int(input())
if A == 1 : print("January")
elif A == 2 : print("February")
elif A == 3 : print("March")
elif A == 4 : print("April")
elif A == 5 : print("May")
elif A == 6 : print("June")
elif A == 7 : print("July")
elif A == 8 : print("August")
elif A == 9 : print("September")
elif A == 10 : print("October")
elif A == 11 : print("November")
elif A == 12 : print("December")
'''


'''
2.
pp = int(input())
tg = int(input())

if pp == 0 and tg == 1:
    print("1")
else:
    print("0")
'''

'''
3.

A = int(input())
if A == 1 or A == 3 or A == 5 or A == 7 or A == 8 or A == 10 or A == 12:
    print("31")
elif A == 2:
    print("28")
else:
    print("30")
'''

'''
4.MAX

A = int(input())
B = int(input())
C = int(input())

if A >= B and A >= C :
    print(A)
elif B >= C and B >= A:
    print(B)
else :
    print(C)
'''

'''
5.MIN

A = int(input())
B = int(input())
C = int(input())

if A <= B and A <= C :
    print(A)
elif B <= C and B <= A:
    print(B)
else :
    print(C)
'''

"""
6.
"""
sold = int(input())

if sold >= 500000 and sold < 1000000:
    print("gold")
elif sold >= 1000000 and sold < 10000000:
    print("platinum")
elif sold >= 10000000:
    print("diamond")
else:
    print("None")







