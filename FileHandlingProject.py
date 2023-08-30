while True:
    print("\n1..for add Student detail")
    print("2..for read Student detail")
    print("3..for delete Student detail")
    print("4..for edit Student detail")
    print("5..for exit")
    
    choice = int(input("\nEnter Choice: "))
    if choice == 1:
        f = open("Student.csv","r+")
        data = f.readlines()
        name = input("Enter Name: ")
        role = input("Enter Role: ")
        f.write(f"\n{len(data)},{name},{role}")
        f.close
    
    if choice == 2:
        f = open("Student.csv","r")
        data = f.readlines()
        print(data)
        for i in data:
            student_info = i.strip().split(',')
            rollno , name, role = student_info
            print(f"{rollno}\t{name}\t{role}")
        f.close
    
    if choice == 3:
        f = open("Student.csv","r")
        data = f.readlines()
        f.close
        for i in data:
            student_info = i.strip().split(',')
            rollno , name, role = student_info
            print(f"{rollno}\t{name}\t{role}")
        num = int(input("Enter number you want to delete: "))
        data.pop(num)
        f = open("Student.csv","w")
        f.writelines(data)
        f.close 
        
    if choice == 4:
        f = open("Student.csv","r")
        data = f.readlines()
        f.close
        for i in data:
            student_info = i.strip().split(',')
            rollno , name, role = student_info
            print(f"{rollno}\t{name}\t{role}")
        no = int(input("Enter your roll no:"))
        student_info = data[no].strip().split(',')
        rollno , name, role = student_info
        newname = input(f"Enter your new name(old:{name})")
        newrole = input(f"Enter your new role(old:{role})") 
        data[no] = f"{no},{newname},{newrole}\n"
        print(data)
        f = open("Student.csv","w")
        f.writelines(data)
        f.close
        
    if choice == 5:
        break

