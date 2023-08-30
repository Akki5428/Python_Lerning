
"""a = int(input("Enter Your First Number:-"))
b = int(input("Enter YOur Second Number:-"))
for n in range(a,b+1):
    if n <= 1:
         continue
    for i in range(2,n):
        if n % 2 == 0 :
            break
    else:
         print(n,"is prime")"""

# a = int(input("Enter A number: "))
# i = 1
# sum = 0
# for i in range(i,(a//2)+1):
#     if a % i == 0:
#         sum = sum + i 
# if sum == a:
#     print(a,"is perfect number...")  
# else:
#     print(a,"isn't perfect number...")    


"""
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print(f"Perfect number between {a} and {b}:")
for n in range(a,b+1):
    i = 1
    sum = 0
    if n < 1:
        continue
    for i in range(i,(n//2)+1):
        if n % i == 0:
            sum = sum + i 
    if sum == n:
        print(n)  
"""



# num = input("Enter any 3 digit Number: ")
# sum = 0
# for i in range(0,len(num)):
#     sum = sum + (int(num[i])**3)
# if int(num) == sum:
#     print(num,"is Armstrong number..")
# else:
#     print(num,"isn't Armstrong number..")




# num = int(input("Enter 3 digit number"))
# sum = 0
# for i in range(0,3):
#     n = num % 10
#     sum = sum + (n**3) 
#     num = num // 10
# if num == sum:
#     print(num,"is Armstrong number..")
# else:
#     print(num,"isn't Armstrong number..")


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print(f"Armstrong number between {a} and {b}")
for num in range (int(a),int(b+1)):  
    num = str(num)
    sum = 0 
    for i in range(0,len(num)):
        sum = sum + (int(num[i])**len(num))
    if int(num) == sum:
        print(num)