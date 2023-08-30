"""
Option = {"Python" : "Nice choice!",
        "Java" : "Nice choice!",
        "Golang" : "You're a cool person I see...",
        "JavaScript" : "Okay so you are our web developer!",
        "C++" : "Too old school..."
        }
Anything else
I don't know that language

lang = input()
print(Option["he"])


lang = input()
if lang == "Python":
    print("Nice choice!")
elif lang == "Java":
    print("Nice choice!")   
elif lang == "Golang":
    print("You're a cool person I see...")    
elif lang == "JavaScript":
    print("Okay so you are our web developer!")
elif lang == "C++":
    print("Too old school...")
else:
    print("I don't know that language")
"""

"""
2.Leap Year doubt
"""
A = int(input())
print(int(A%400==0 or (A%4==0 and A%100!=0 )))


"""
3.D
"""

"""
4. Categorise the number -
 Nested if-else Problem Description Given the number N,
 Categorise the number according to following condition : 
 1. Odd-Positive
 2. Odd-Negative
 3. Even-Positive
 4. Even-Negative

N = int(input())
if N%2!=0 and N>0:
    print("Odd-Positive") 
elif N%2!=0 and N<0:
    print("Odd-Negative")     
elif N%2==0 and N>0:
    print("Even-Positive")  
else :
    print("Even-Negative")       
"""


"""
5. Fizz Buzz Problem Description Write a program that takes in a number N as input and does the following: 
• if N is a multiple of 3, print Fizz 
• if N is a multiple of 5, print Buzz 
• if N is a multiple of both 3 and 5, print FizzBuzz 
Problem Constraints:
 1 <= N <= 1000 
Input Format :
 There is only 1 single line in the input, which is the integer N.
Output Format :
Print Fizz / Buzz / FizzBuzz depending on the value N.
Example Input 
Input 1:- 9 
Input 2:- 15 
Example Output
Output 1:-Fizz 
Output 2:- FizzBuzz


N = int(input())
if N % 3 == 0 and N % 5 == 0 :
    print("FizzBuzz")
elif N % 3 == 0:
    print("Fizz") 
elif N % 5 == 0:
    print("Buzz")      
"""

"""
6.B
"""

"""
7.B
"""

"""
8.A,D    doubt


a= 2
b=2
c=3

if (a==b and a==c) and b==c: 
    print("equilateral") 
elif a==b or b==c or c==a:
    print("isosceles")
else:
    print('scalene')
"""