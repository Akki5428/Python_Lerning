"""print("Enter 10 Numbers:")
list  = [input() for i in range (10)]
t = tuple(list)
print(t)

for i in t:
    c  = t.count(i)
    if(c>1):
      rep = i
in1 = t.index(rep)
print(f"2nd index of {rep} is {t.index(i,in1+1)}")"""


student_data = ("akshat",19,"male")

student_name = student_data[0]

student_age = student_data[1]
   
student_gender = student_data[2]

print("student_name:",student_name)    
print("student_age:",student_age)
print("student_gender:",student_gender)