# Operators in Python
"""
1. Arithmetic Operators: +, -, *, /, %, ** (exponent), // (floor division/integer division)
2. Comparision/Conditional/Relational Operators/Conditions: <, >, <=, >=, ==, !=
    # these operators will always return either True or False
3. Logical Operators: and, or, not
4. Bitwise Operators: &, |, ~, ^ (xor- exclusive or), <<, >>
    3 : 0 0 1 1
        & & & &
    5 : 0 1 0 1
    -----------
        0 0 0 1 = 1
    3 : 0 0 1 1
        | | | |
    5 : 0 1 0 1
    -----------
        0 1 1 1 = 7
    3 : 0 0 1 1
        ^ ^ ^ ^
    5 : 0 1 0 1
    -----------
        0 1 1 0 = 6
    3 : 0 0 1 1
    ~3: 1 1 0 0 = -4
    23 : 0 0 0 1  0 1 1 1
    << : 0 0 1 0  1 1 1 0 : 46
    << : 0 1 0 1  1 1 0 0 : 92
    << : 1 0 1 1  1 0 0 0 : 184
    100 : 0 1 1 0  0 1 0 0
    >>  : 0 0 1 1  0 0 1 0 : 50
    >>  : 0 0 0 1  1 0 0 1 : 25
    >>  : 0 0 0 0  1 1 0 0 : 12
5. Assignment Operators: 
    =
    a = 5
    shorthand operators:
    a = a + b   : a += b
    a = a - b   : a -= b
    a = a * b   : a *= b
    a = a / b   : a /= b
    a = a % b   : a %= b
    a = a ** b  : a **= b
    a = a // b  : a //= b
    a = a & b   : a &= b
    a = a | b   : a |= b
    a = a ^ b   : a ^= b
    a = a << 3  : a <<= b
    a = a >> 3  : a >>= b
    There is no such thing as i++ or i-- in Python, so we have to write i += 1 or i -= 1.
6. Membership Operators: in, not in
7. Identity Operators: is, is not
"""

# print(10 ** 3)      # 10^3
# print(64 ** (1/2))
# print(64 ** 0.5)
# print(11/4)     # 2.75
# print(11//4)    # 2

# print(10 > 20)
# print(10 <= 20)

# a = 3
# b = 5
# c = 10
# d = 15
# print(a > b or c > b)
# print(a > b and c > b)

# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)

# print(23 << 3)
# print(100 >> 2)

# print("toh" in "Python")
# print("th" in "Python")

# d <<= 3
# print(d)

# print(a is b)
# print(b is not c)

# print(a == b)
# print(b != c)

# myList = [1,2,3,4]
# yourList = myList
# ourList = myList.copy()

# print(myList is yourList)
# print(myList == yourList)

# print(myList == ourList)
# print(myList is ourList)