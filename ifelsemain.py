# if-else / Decision Making

"""
if (condition){
    code 1
    code 2
    code 3
}
code 4
if condition :
    code 1
    code 2
code 3
code 4
"""
"""
a = int(input("a: "))
count = 0
if a % 2 == 0:
    print("Even")
    count += 1
else:
    print("Odd")
print("End of the program.")
"""
"""
a = float(input("a: "))
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")
print("End of the world.")
"""
# shorthand if can only be used if code inside each if/else block is only of one line.
# shorthand if:
"""
age = int(input("Your age: "))
if age >= 18: print("Please vote.")
print("Have a nice day, good bye!")
"""
# shorthand if-else:
"""
a = int(input("a: "))
print("Even") if a % 2 == 0 else print("Odd")
print("End of the program.")
"""
# shorthand for if-elif-else does not exist.

# There is no switch case in Python.
"""
Ask two numbers from user. Also ask for operation (+,-,* or /). Print answer accordingly.
a = float(input("a: "))
b = float(input("b: "))
operation = input("Operation (+, -, * or /): ")
"""

# Printing the score of golf game:
"""
PAR: 10
Strokes         Score
10              PAR
9 (PAR - 1)     BIRDIE
8 (PAR - 2)     EAGLE
7 (PAR - 3)     DOUBLE EAGLE
2 TO 6          TRIPLE EAGLE
(2 to PAR - 4)
1               HOLE IN ONE
11 (PAR + 1)    BOGEY
12 or 13        DOUBLE BOGEY
(PAR + 2 OR PAR + 3)
14 OR MORE      GO HOME
(PAR + 4 OR MORE)
Write a Python program that takes PAR & Strokes from user & prints the score accordingly.


par = int(input("Enter your par:-"))
stroke = int(input("Enter your stroke:-"))

if stroke==par:
    print("You hit PAR...")
elif stroke == (par - 1) :     
    print("You hit BIRDIE...")
elif stroke == (par - 2) :     
    print("You hit EAGLE...")
elif stroke == (par - 3) :     
    print("You hit DOUBLE EAGLE...")    
elif stroke == (par - 1) :     
    print("You hit BIRDIE...")
elif stroke == (par - 1) :     
    print("You hit BIRDIE...")
# HW Examples:
"""



"""
1. A school has following grading system. Write a Python code that takes percentage of a student and display his/her grade.
below 35%       :   F
from 35 to 44   :   E
from 45 to 54   :   D
from 55 to 64   :   C
from 65 to 74   :   B
75 or more      :   A


per = int(input("Enter your percentage:-"))

if 0 <= per < 35 :
    print("Your grade is F")
elif 35 <= per <= 44 :
    print("Youe grade is E")   
elif 45 <= per <= 54 :
    print("Youe grade is D")
elif 55 <= per <= 64 :
    print("Youe grade is C")
elif 65 <= per <= 74 :
    print("Youe grade is B")
elif 75 <= per <= 100 :
    print("Youe grade is A") 
else:
    print("Please Enter percentage bitween 0 to 100")   
"""

"""
2. Write a Python program to find whether a given year is a leap year or not. 
Test Data : 2016
Expected Output :
2016 is a leap year.

year = int(input("Enter year:-"))

print("Your year :",year)
if year % 4 == 0 :
    print("It's leap year")
else :
    print("It's not leap year")    
"""

"""
3. Write a Python program to find the largest of three numbers. 
Test Data : 12 25 52
Expected Execution:
1st Number = 12
2nd Number = 25
3rd Number = 52
52 is the largest number.

code 1:-
l1 = []
a = int(input("Enter your first number:-"))
b = int(input("Enter your second number:-"))
c = int(input("Enter your third number:-"))

l1.append(a)
l1.append(b)
l1.append(c)
print(f"{max(l1)} is the largest number.")

code 2:-

a = int(input("Enter your first number:-"))
b = int(input("Enter your second number:-"))
c = int(input("Enter your third number:-"))

if a<=b and a<=c:
    print(c,"is the largest number.")
elif a<=b and c<=b:
    print(b,"is the largest number.")    
else:
    print(a,"is the largest number.")        
"""

"""
4. Write a Python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies. 
Test Data : 
x-coordinate: 7
y-coordinate: 9
Expected Output :
The coordinate point (7,9) lies in the First quadrant.


x = int(input("x-coordinate: "))
y = int(input("y-coordinate: "))

if x>=0 and y>=0:
    print(f"The coordinate point ({x},{y}) lies in the First quadrant.")
elif x<0 and y>0:
    print(f"The coordinate point ({x},{y}) lies in the Second quadrant.")
elif x<0 and y<0:
    print(f"The coordinate point ({x},{y}) lies in the Third quadrant.")        
elif x>0 and y<0:
    print(f"The coordinate point ({x},{y}) lies in the Forth quadrant.")    
"""    


"""
5. Write a Python program to find the eligibility of admission for a professional course based on the following criteria: 
Eligibility Criteria : 
Marks in Maths must be atleast 65,
Marks in Phy must be atleast 55,
Marks in Chem must be atleast 50 and 
Total marks all three subject must be atleast 190 or Total in Maths and Physics >=140
Input the marks obtained in Mathematics :72 
Input the marks obtained in Physics :65 
Input the marks obtained in Chemistry :51 
Total marks of Maths, Physics and Chemistry : 188 
Total marks of Maths and Physics : 137 
The candidate is not eligible.


math = int(input("Input the marks obtained in Mathematics :"))
phy = int(input("Input the marks obtained in Physics :"))
chem = int(input("Input the marks obtained in Chemistry :"))
tol = int(math+phy+chem)
tolmp = int(math+phy)
print("Total marks of Maths, Physics and Chemistry :",tol)
print("Total marks of Maths and Physics :",tolmp)

if math >= 65 and phy >= 55 and chem >= 50 and tol >= 190 and tolmp >= 140 :
    print("The candidate is eligible.")
else:
    print("The candidate is not eligible.")
"""

"""
6. Take values of length and breadth of a rectangle from user and check if it is square or not.



l = int(input("Enter length of rectangle:-"))
b = int(input("Enter breadth of rectangle:-"))

if l == b:
    print("The rectangle is square...")
else :
    print("The rectangle isn't square...")   
"""     

"""
7. A shop gives discount of 10% if the cost of purchased quantity is more than Rs.1000.
Ask user for quantity
Assume each item costs 100.
Calculate and print total amount to be paid by user.

print("New Offer :- If your net value is Rs.1000+ then you get instant 10% Discount..")
item = int(input("Enter Quantity:-"))
val = int(item*100)

if val>1000:
    print("CONGO!!You got 10% discount..")
    print("Your net value",val-(val*0.1))
else:
    print("sorry you can't get any discount..")
    print("Your net value",val)    
"""

"""
8. In above program, ask user for his/her name, mobile number, quantity and price of each item, then decide whether he/she is eligible for discount and based on that print the invoice in the following format:
case 1- when customer is not eligible for discount:
------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              50          3               150
item-2              100         4               400
item-3              40          5               200
                                                ---------
                                Final Amount:   750
----------------Thanks for shopping with us!---------------
case 2- when customer is eligible for discount:
------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              90          3               270
item-2              100         4               400
item-3              40          10              400
                                                ---------
                                Grand Total:    1070
                                Discount:        107
                                                ---------
                                Final Amount:    963
----------------Thanks for shopping with us!---------------

code:-

print("\n","New Offer :- If your net value is Rs.1000+ then you get instant 10% Discount..","\n")
  

name = input("Enter Your Name:-")
num = int(input("Enter your number:-"))
q1 = int(input("Item-1 Quantity:-"))
p1 = int(input("Item-1 Price:-"))
q2 = int(input("Item-2 Quantity:-"))
p2 = int(input("Item-2 Price:-"))
q3 = int(input("Item-3 Quantity:-"))
p3 = int(input("Item-3 Price:-"))
tol1 = int((q1*p1))
tol2 = int((q2*p2))
tol3 = int((q3*p3))
tol = int((q1*p1)+(q2*p2)+(q3*p3))


print("Retail Invoice".center(60,"-"))
print("Customer Name: ",name)
print("Contact Number: ",num)
print("Date of Invoice: 09-01-2022")
print("".center(60,"-"))
print("Items\t".expandtabs(20)+"Price\tQuantity\t"+"Total")
print("items-1\t".expandtabs(20)+f"{p1}\t\t{q1}\t\t{tol1}")
print("items-1\t".expandtabs(20)+f"{p2}\t\t{q2}\t\t{tol2}")
print("items-1\t".expandtabs(20)+f"{p3}\t\t{q3}\t\t{tol3}")
print("\t".expandtabs(48)+"---------")
print("\t".expandtabs(32)+f"Grand Total:\t{tol}")
if tol>1000:
    print("\t".expandtabs(32)+"Discount:\t"+f"{int(tol*0.1)}".rjust(len(str(tol))," "))
    print("\t".expandtabs(48)+"---------")
    print("\t".expandtabs(32)+"Final Amount:\t"+f"{int(tol-(tol*0.1))}".rjust(len(str(tol))," "))
else:
    print("\t".expandtabs(48)+"---------")
    print("\t".expandtabs(32)+"Final Amount:\t"+f"{tol}".rjust(len(str(tol))," "))

print("Thanks for shopping with us!".center(60,"-"))
"""


"""
9. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and years of service and print the final salary.
"""
sal = int(input("Enter Your Salary:-"))
ser = int(input("Enter Your years of service:-"))

if ser > 5:
    print("Because Your year of service more than 5 years Our company decided to give you BONUS..and it's 5% of your salary","\n")
    print("Your Final Salary: ",sal+(sal*.05))
else:
    print("Sorry you are not eligbale for Bonus because your year of service less than 5 year","\n")
    print("Your Final Salary: ",sal)    

