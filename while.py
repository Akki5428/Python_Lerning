# Loops in Python: for loop, while loop
"""
for(i=1; i<=5; i++)
"""
# while loop

# Multiplicative table of a given integer
"""
n = int(input("n: "))   # 5
i = 1
while i <= 10:
    print(f"{n} X {i} = {n*i}")
    i += 1
Output:
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
"""

# Write a program in Python that takes an integer from user & prints the number of digits it has.

"""
a = int(input("Enter a number:  "))
count = 0
if a == 0:
    count = 1
else:
    while a > 0:
        a = a // 10
        count += 1
print(count)
"""
"""
number = int(input("Enter a number:  "))    # 5379
print(len(str(number)))     # "5379"
"""

# using while loop to iterate through a collection:
"""
fruits = ["apple", "kiwi", "banana", "cherry", "grapes", "orange"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
name = "James Bond"
i = 0
while i < len(name):
    print(name[i])
    i += 1
"""

# Biggest use of while loop in Python: To create infinite loop
"""
a = int(input("Enter two integers:\n"))
b = int(input())
while True:
    operation = input("Enter operation (+, -, *, / or 'x' to quit): ").lower()
    if operation == "+":
        print(f"{a} + {b} = {a + b}")
    elif operation == "-":
        print(f"{a} - {b} = {a - b}")
    elif operation == "*":
        print(f"{a} * {b} = {a * b}")
    elif operation == "/":
        print(f"{a} / {b} = {a / b}")
    # elif operation == "x" or operation == "X":
    elif operation == "x":
        break
    else:
        print("Invalid, please try again...")
"""
# False: False, 0, "", [], set(), (), {}
# True: True, 1 and everything other than above
# print(5 > 3)

# Write a Python program to take a integer from the user and print whether it is a Prime number or not.
"""
n = int(input("n: "))
i = 2
flag = 1
while i < n: # i=2,3,4,5,6,7,...,640
    if n % i == 0:
        print("Not Prime.")
        flag = 0
        break
    i += 1
if flag == 1:
    print("Prime.")
"""

# IMP Homework:
# Write a Python program that takes name of a fruit from user & prints whether it is in the following list or not:
# fruits = ["apple", "kiwi", "banana", "cherry", "grapes", "orange"]


# Additional programs:
"""





9. Write a Python program that prints all the Armstrong numbers between two integers given by user.
"""

"""
1. Write a Python code that takes an integer from user and prints number of digits in that integer.


num = input("Enter your number:-")
print("Digit :-",len(num))
"""

"""
2. Write down a Python code that creates a user defined list

l = []
while True:
    num = input("Enter + for Add x for Exit:-").lower()
    if  num == "+":
        n = input("Enter Any Element:")
        l.append(n)
    elif num == "x":
        break
    else:
        print("Invalid Operation..")

if(len(l) == 0):
    print("\nYour list is Empty...")
else:
    print("\nYour List:",l)    
"""

"""
3. Write a Python code to print each of the elements of a given list in a new line 


l = ["hello","friends","chay","pilo","khana","khalo"]
i = 0
while i < len(l) :
    print(l[i])
    i += 1
"""

"""
4. Write a Python program that prints whether the number given is a prime number or not.

num = int(input("Enter your Number: "))
i = 2
count = 0
while i < num:
    if num % i == 0:
        print(f"{num} is not a Prime number...")
        count = 1
        break   
    i += 1 
if count == 0:
    print(f"{num} is a Prime Number....")
"""



"""
5. Write a Python program that prints whether the number given is a perfect number or not.

num = int(input("Enter your number: "))
i = 1
per = 0

while i < num:
    if num % i == 0:
        per = per + i
    i += 1
if per == num:
    print(num,"is a Perfect number")
else:
    print(num,"is not a Perfrct number")    
"""



"""
6. Write a Python program that prints whether the number given is an Armstrong number or not.

amg = input("Enter Your number:-")
i=0
sum=0
while(i<len(amg)):
    sum += (int(amg[i]) ** len(amg))
    i += 1

if sum == int(amg):
    print("The Number is Armstrong")
else:
    print("The Number isn't Armstrong")        
"""


"""
7. Write a Python program that prints all the prime numbers between two integers given by user.

f = int(input("Enter your First Number: "))
s = int(input("Enter your Second Number: "))

print(f"\nPrime Number between {f} and {s}")
while f <= s:
    i = 2
    count = 0
    while i < f:
        if f % i == 0:
            count = 1
            break   
        i += 1 
    if count == 0:
        print(f)
    f += 1
    """


"""
8. Write a Python program that prints all the perfect numbers between two integers given by user.

f = int(input("Enter your First Number: "))
s = int(input("Enter your Second Number: "))

print(f"perfect numbers between {f} and {s}")
while f < s:
    i = 2
    per = 1

    while i < f:
        if f % i == 0:
            per = per + i
        i += 1
    if per == f:
        print(f)  
    f += 1    
"""    