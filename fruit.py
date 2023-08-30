"""
fruits = ["apple","kiwi","banana","cherry","grapes","orange"]
check = input("Enter your fruit Name: ")
a=0
flag = 0

while(a<len(fruits)):
    if(fruits[a]==check.lower()):
        print("yes!! given fruit is present")
        flag = 1    
    a = a + 1
if flag == 0 :
    print("No!! given fruit is not present")
"""
fruits = ["apple","kiwi","banana","cherry","grapes","orange"]
a=0
while a<len(fruits):
    if fruits[a] != "cherry" :
        print(fruits[a])
    a = a + 1

