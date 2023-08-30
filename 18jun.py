class Car:
    seating_capacity = 5   # class variable
    allcars = [] 
    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel
        Car.allcars.append(self)

    # creating a method
    def displayDetails(self):
        print("---------- Details of c1 ----------")
        print("Model Name:", self.name)
        print("Price:", self.price)
        print("Fuel:", self.fuel)
        print("Seating Capacity:", self.seating_capacity)
        print()

    def changeDetails(self):
        print("Enter new details:")
        self.name = input("Name: ")
        self.price = int(input("Price: "))
        self.fuel = input("Fuel: ")

    # def displayDetails(self, something):
    #     print("Something is -", something)

c1 = Car("Elantra", 2500000, "Petrol")
# c1.displayDetails("Nothing")

c2 = Car("Verna", 1200000, "Petrol")
# c1.changeDetails()
# c1.displayDetails()
c3 = Car("Fortuner", 3500000, "Diesel")
"""
Press 1 - to add a new car
2 - display details of an existing car
3 - change details of an existing car
4 - delete a car
5 - exit
"""
# Your code goes here
while(1):
    print("0 - display Srno. with name of car.")
    print("1 - to add new Car.")
    print("2 - display details of an existing car")
    print("3 - change details of an existing car")
    print("4 - delete a car")
    print("5 - for exit")
    choice = int(input("Enter a choice: "))

    if choice == 0 :
        print("Sr no.\tName")
        for c in range(len(Car.allcars)):
            print(f"{c}\t{Car.allcars[c].name}")
            
    elif choice == 1:
        pass 
    elif choice == 2:
        n = input("Enter car name:")
        if n == c1.name:
            c1.displayDetails()
        if n == c2.name:
            c2.displayDetails()
        if n == c3.name:
            c3.displayDetails()
        else:
            print("There is no car exist.")
    elif choice == 3 :
        n = input("Enter car name:")
        if n == c1.name:
            c1.changeDetails()
        if n == c2.name:
            c2.changeDetails()
        if n == c3.name:
            c3.changeDetails()
        else:
            print("There is no car exist.")
    elif choice == 4:
        pass
    elif choice == 5:
        break
    else :
        print("Invalid choice...")