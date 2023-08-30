def fun(a):
    return sum (a) / len(a)
n = int(input("Enter how many number you want to sum:"))
li = []
for i in range(n):
    num = int(input("Enter Number:"))
    li.append(num)

print("avg = ",fun(li))   
