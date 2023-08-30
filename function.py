"""
1. Ask two integers from user, add their factroials. Now ask two more integers from user and add their factorials too. calculate average of the factorials you computed. Now finally ask one last integer from user and add its factorial to the average.


def fact(a):
    sum = 1
    i = 1
    while(i<=a):
        sum = sum * i
        i = i + 1
    return sum  


def add(p,q):
    return p+q

def avg(x,y,z,w):
    return (x+y+z+w)/4

n1 = int(input("Enter Your 1st number:"))
n2 = int(input("Enter Your 2nd number:"))

f1 = fact(n1)
f2 = fact(n2)
s1 = add(f1,f2)
print(f"{n1} and {n2} factorial are {f1} and {f2} and sum of factorial = {s1}")

n3 = int(input("Enter Your 3rd number:"))
n4 = int(input("Enter Your 4th number:"))

f3 = fact(n3)
f4 = fact(n4)
s2 = add(f3,f4)
print(f"{n3} and {n4} factorial are {f3} and {f4} and sum of factorial = {s2}")

allavg = avg(f1,f2,f3,f4)
print(f"Avg = {allavg}")

n5 = int(input("Enter last number:"))

last = add(allavg,n5)

print(f"sum of avg and last number = {last}")
"""



"""
2. Write a function that prints whether the number passed in its argument is prime or not. Using a main program pass the number given by the user to that function.

def prime(num):
    i = 2
    while(i<num):
        if(num%i == 0):
            print(f"{num} is not a Prime number...")
            break
        i = i + 1
    else:
        print(f"{num} is Prime number...")    


num = int(input("Enter Number : "))
prime(num)
"""


"""
3. Write a function to find average of 5 given numbers and a main program that takes 5 integers from user, uses the factorial function to find factorial of each one of them and using average function prints the average of factorials of them.


def fact(a):
    sum = 1
    i = 1
    while(i<=a):
        sum = sum * i
        i = i + 1
    return sum  

def avg(a,b,c,d,e):
    return (a+b+c+d+e)/5

n1 = int(input("Enter 1st number = "))
n2 = int(input("Enter 2nd number = "))
n3 = int(input("Enter 3rd number = "))
n4 = int(input("Enter 4th number = "))
n5 = int(input("Enter 5th number = "))

f1 = fact(n1)
f2 = fact(n2)
f3 = fact(n3)
f4 = fact(n4)
f5 = fact(n5)

s1 = avg(n1,n2,n3,n4,n5)
s2 = avg(f1,f2,f3,f4,f5)

print("Sum of Number:",s1)
print("Sum of factorial",s2)
"""


"""
4. Make a program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
    ap:
    first term = a = 5
    difference = d = 4
    ap = 5, 9, 13, 17, 21, 25,...
    nth term = a + (n-1)d
   

def ap(a,d,n):
    num = a + (n-1)*d
    print(f"nth term = {num}")

a = int(input("Enter First term of series: "))
d = int(input("Enter Difference of series: "))
n = int(input("Enter n term you need:"))

ap(a,d,n)
 """

"""
5. Develop a program that uses a function to find nth term of an geometric progression whose first term is 'a' & common ratio is 'r'.

def gp(a,r,n):
    num = a * (r**(n-1))
    print(f"nth term = {num}")

a = int(input("Enter First term of series: "))
r = int(input("Enter ratio of series: "))
n = int(input("Enter n term you need:"))

gp(a,r,n)
"""


""" 
6. Make a function that checks whether the given number is a perfect number or not. Make a program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.


def perfect(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum = sum + i
    if(sum == n):
        print(f"{n} is Perfect number")
    else:
        print(f"{n} is non Perfect num")  


def perfect1(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum = sum + i
    if(sum == n):
        print(f"{n} is Perfect number")        

def perbtn(a,b):
    for i in range(a,b+1):
        perfect1(i)


num = int(input("Enter Number: "))
a= int(input("Enter 1st num:"))
b = int(input("Enter 2nd num:"))
perbtn(a,b)
"""


"""
7. Write a function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and print all the Prime numbers between those two integers using that function.


def prime(num):
    i = 2
    while(i<num):
        if(num%i == 0):
            print(f"{num} is not a Prime number...")
            break
        i = i + 1
    else:
        print(f"{num} is Prime number...")    

def prime1(num):
    i = 2
    while(i<num):
        if(num%i == 0):
            break
        i = i + 1
    else:
        print(f"{num}",end=",")         

def primebtn(a,b):
    print(f"Prime Number between {a} and {b}:")
    for i in range(a,b+1):
        prime1(i)
           

num = int(input("Enter Number : "))
prime(num)

a = int(input("Enter 1st number = "))
b = int(input("Enter 2nd number = "))
primebtn(a,b)
"""

"""
8. Write a function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.
"""

# def arm(n):
#     sum = 0
#     p = len(n)
#     for i in range(p):
#          sum = sum + int(n[i])**(p)
#          print(sum)
#     if int(n) == sum:
#          print(f"{n} is armstrong number...")
#     else:
#          print(f"{n} is not an armstrong number...")     
        

# num = input("Enter Any Number = ")
# arm(num)

def arm1(n):
    sum = 0
    p = len(n)
    for i in range(p):
         sum = sum + int(n[i])**(p)
    if int(n) == sum:
         print(f"{n} is armstrong number...")

def armbtn(a,b):
     for i in range(a,b):
          arm1(str(i))         

a = int(input("Enter Your First number ="))
b = int(input("Enter Your Second number ="))
armbtn(a,b)