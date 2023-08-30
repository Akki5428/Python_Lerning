"""
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

numbers = [2,3,4,5,6,7,8,9]

factorials = []

for ele in numbers:
    factorials.append(factorial(ele))

print(factorials)


# use the above function and create another list named 'factorials' that contains factorials of all the members of list 'numbers'
# Write your code here
"""





"""
1.what is the result of following expression i python ?
    print("54"+"23")
    a)77
    b)5423   Right
    c)54
    d)23
2.what is the result of following expression  python ?
    print(true==1)
    a)True
    b)False
    c)Error  Right
3.what is the result of following expression  python ?
    print("1" == 1)
    a)True
    b)False  Right
    c)Error
4.what is output of following statements ?
    x=55/11
    print(x)
    a)5   
    b)5.0  Right
    c)6.0
5.Print the result of the following expression:
    (3+4)//2+6

    9
6. Set the value of variable a, b and c such that the following condition evaluates to true:
    a = 5 # change this
    b = 3 # change this
    c = 4 # change this
    # DO NOT CHANGE THE FOLLOWING:
    x = a < b + c
    print(x) # this should be True
    Note: You need to write the code from scratch in the code editor.


"""

"""
DOUBT   7. Problem Description:
    Given total bills amount and amount of a single bill. Print number of bills.
    Note: The total amount is equally splitted in all bills. The number of bills should be an integer value.
    Input Format:
    The first line contains a real number N denoting the total budget. The second line contains an integer M denoting the value of a single bil11
    Output Format:
    Print in a single line denoting the total number of bills that can fit in the total budget.
    Problem Constraints:
    1 < N Cx 10000 1 C# M xx 100
    Examples
    Input:
    126.3
    5
    Output: 
    25

tamt = float(input("Enter Your Total Amount: "))
samt = int(input("Enter Single Bill Amount: "))

print(f"\n\nNumber of Bills : {int(tamt//samt)}")
"""

"""
8. Problem Description:
    A group of spammers is troubling Varun by calling on his mobile phone repeatedly. After a while, Varun observed a pattern that the mobile number from which the spammers call him is always lesser than his mobile number when compared on the number line. The mobile number of Varun is 1234880990. Given a mobile number as an input print True if the number belongs to the spammers else False.
    Input Format:
    The input will be a single integer representing a mobile number.
    Output Format:
    The output would be True if the condition holds else False
    Sample Input:
    9999999999
    Sample Output:
    False
    Note: All the mobile numbers in this problem are hypothetical


num = int(input("Enter Mobile Number: "))

print(num<1234880990)
  """  



# HW - 2
"""
Doubt : 1. Numerical Derivative
    Problem Description:
    The derivative of a function is a value that tells us how much the output of a mathematical function would change, if we were to make a very, very tiny change in its input. In mathmetical terms, the limit definition of a derivative is defined as: limo Where x and hare both inputs to the h
    function f. You can safely ignore the lim part in the expression.
    Given the values of x and your task is to evaluate the expression for the function f(x) = 3x² + 2 and print the value obtained.
    Input Format:
    The input will contain two numbers.
    The first line will be the x value.
    The second line will be the h value.
    Output Format:
    The output would be a single line float value of the expression in problem description.
    
    Input:
    1
    1
    Output:
    9.0
    Note: The value of hwill always be more than for this problem.


x = int(input("Enter X value: "))
h = int(input("Enter H value: "))

ans = 6*x + 3*h
print(float(ans))
"""



"""

9.Raised to the power
    What do you think would be the output when we run the piece of code given below?
    print(3 ** 2 ** 0)
    a.	Error  
    b.	0
    c.	3   Right
    d.	1
10.	What would be the output of the following piece of code?
    print("abcd" < "abce")
    a.	Error
    b.	True   Right
    c.	False  
"""


"""
2.Is the third one greater?
    Problem Description:
    Given three integer values as input, your task is to print True if the third number is greater than the first two else False.
    Input Format:
    Input will contain three lines denoting three integer values.
    Output Format:
    The output would be True if the condition holds else False.
    Input:
    1
    2
    3
    Output:
    True
    Explanation:
    Here 3 is greater than 1 and 3 is also greater than 2 and hence the output is True.

a = int(input("Enter Your 1 Number : "))
b = int(input("Enter Your 2 Number : "))
c = int(input("Enter Your 3 Number : "))

print(a<c and b<c)
"""


"""
3.	Floors and Ceilings
    Problem Description:
    The floor function floor(x) is defined as the greatest integer less than or equal to the given number.
    For example, floor(7.64)=7.
    Likewise, the ceiling function ceil(x) is defined as the smallest integer greater than or equal to the given number.
    For example, ceil(7.64)=8.
    Given a number x as input, output its floor(x) and ceil(x) values.
    Note: Assume that the input will never be an integer.
    Input Format:
    One line float value
    Output Format:
    Print two integers, first one denoting the floor value and second one the ceiling value of the given number.
    
    Input:
    7.64
    Output:
    7
    8
    Example Explanation:
    The greatest integer that is less than or equal to 7.64 is clearly 7.
    The smallest integer that is greater than or equal to 7.64 is clearly 8.\
        
import math

num = float(input("Enter a number: "))
print(f"\nfloor = {math.floor(num)}\nceil = {math.ceil(num)}")
"""


"""
4. Multiply Chain
    Problem Description:
    Given a number n as input, multiply it with the number (n-1) and (n-2) and print the resultant output.
    Input Format:
    A single line containing an integer.
    Output Format:
    A single line output according to the problem description.
    Input:
    10
    Output:
    720


A = 10
print(A*(A-1)*(A-2))
"""


"""
5.Module Trouble
    Problem Description:
    Shikha is trying to solve a hard math problem in which she is required to take the mod of a number x with y quite frequently. Given two numbers x and y write a program that helps Shikha do this easily. Assume that the value of y is always greater than 0.
    Input Format:
    Two lined inputs. The first line denotes the x value and the second one the y value.
    Output Format:
    Single number which is the mod of x with y.
    Input:
    100
    11
    Output:
    1

x = 100
y = 99

print(f"\n{x % y}")
"""


"""
6.Four average
    Problem Description:
    Given four numbers as input print their average value as output.
    Input Format:
    Four lines denoting four numbers.
    Output Format:
    Single number denoting the average value.
    Input:
    1
    2
    3
    4
    Output:
    2.5


a = float(input("Enter 1 number: ")) 
b = float(input("Enter 2 number: "))
c = float(input("Enter 3 number: "))
d = float(input("Enter 4 number: "))
print(f"Avg = {(a+b+c+d)/4}")

"""


"""

7.Odd/Even - without 'if' statements
    Problem Description
    Given an integer n as input, print True if it is odd and False if it is even. Solve this question with the concepts taught in the Lecture on Operators. DO NOT USE IF/ELSE.
    Input Format:
    A single line input containing the integer.
    Output Format:
    A single-line boolean value.
    Input:
    2
    Output:
    False
    Example Explanation
    The output is False because 2 is even.


n = int(input("Enter Your Number: "))
print(n%2!=0)
"""



"""
8.Are the weights balanced?
    Problem Description:
    A weighing machine has two arms, a left arm, and a right arm. On both sides of the weighting machine we can put in weights and if both of those weights are equal, the arms of the machine will hang equally in the air, with none of them hanging below the other. This is hard to observe visually hence you are asked to write a program that takes in two weight values as input and outputs True if they will leave the machine balanced and False if they will leave the machine unbalanced.
    Input Format:
    The input will contain two lines denoting the weight values on the left and right arms of the machine
    Output Format:
    True if the machine is balanced. False if the machine is unbalanced.
    Input:
    64.0
    63.0
    Output:
    False

a=float(input("Enter Left Arm Weight: "))
b=float(input("Enter Right Arm Weight: "))
print(a==b)
"""


