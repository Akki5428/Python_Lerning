a = float(input("Enter first number :"))
b = float(input("Enter second number :"))
operation = input("Enter +,-,/,* :")

if(operation == "+"):
    print("sum =",a+b)
elif(operation == "-"):
    print("sub =",a-b)
elif(operation == "*"):
    print("mul =",a*b)   
elif(operation == "/"):
    print("div =",a/b)
else:
    print("wrong operation........")     