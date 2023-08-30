"""Write a program to ask name & marks of a subject. Add them in the following dictionary if the subject doesn't exist in it and print "Success". If the subject already exists, show user the old marks of that subject and ask whether they want to overwrite the marks or not. If user chooses 'no', print "Aborted" or if user chooses 'yes' then, update the marks of that subject in the dictionary. In all cases, print the final dictionary at last."""

result = {"Physics" : 83, "Maths": 91, "Python" : 100, "Chemistry": 90, "java": 99, "SQL":10}

name = input("Enter name of subject: ")
marks = int(input("Enter marks: "))

n = result.get(name)
m =result.setdefault(name,marks)  

if m !=  n:
    print("Success")
else:
    print("Subject already exists")
    print(f"The old mark of {name} is {m}")
    ans = input("You want to enter new marks (yes/no): ")
    if(ans=="yes"):
        new = int(input("Enter your new marks: "))   
        result[name] = new
    else:
        print("Aborted")     
print("Final Dictonary:-")
print(result)