"""1.Class Performance 2

A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())

print((A1+A2)/2 > (B1+B2)/2)
"""

"""
2. Min of two Problem Description Write a program to input two numbers(A & B) from user and print the minimum element among A & B in each line.


A = int(input())
B = int(input())
print(B) if B<A else print(A)
"""

"""
3. B
"""

"""
4.D
"""

"""
5. Guide the coordinate
 
 Problem Description:
   Given the (x, y) coordinates of a point on a 2D plane, write a program that transforms these coordinates according to the conditions given below.
     • If the sum of x and y coordinates is a multiple of 5, then increment both the coordinates by 1 and print.
     • If the x coordinate is even and the y coordinate is odd, then increment y by 1 and print both.
     • If the y coordinate is even and the x coordinate is odd, then increment x by 1 and print both. 
     
     Input Format :
     Two lines containing integer x and y. 
     Output Format :
     Two lines containing transformed integer values of x and y. 
     
     Sample Input :
     15 
     10 
     Sample Output :
     16
     11


x = int(input())
y = int(input())

if (x+y)%5==0:
    x+=1
    y+=1
elif x%2==0 and y%2!=0:
    y+=1
elif x%2!=0 and y%2==0:
    x+=1

print(f"{x}\n{y}")      
"""