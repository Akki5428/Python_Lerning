class Car:
    seating_capacity = 5        # class variable
    allCars = []

    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel
        Car.allCars.append(self)

    # creating a method
    def displayDetails(self):
        print(f"---------- Details of {self.name} ----------")
        print("Model Name:", self.name)
        print("Price:", (self.price))
        print("Fuel:", self.fuel)
        print("Seating Capacity:", self.seating_capacity)
        print()

    def changeDetails(self):
        print("Enter new details (just press Enter if you want to keep that detail same):")
        n = self.name
        p = self.price
        f = self.fuel
        self.name = input("Name: ")
        if self.name == "":
            self.name = n
        self.price = input("Price: ")
        if self.price == "":
            self.price = p
        self.fuel = input("Fuel: ")
        if self.fuel == "":
            self.fuel = f


    # static methods
    @staticmethod
    def showAllCars():
        print("Sr.No.\tName")
        for i in range(len(Car.allCars)):
            print(f"{i}\t{Car.allCars[i].name}")


    # class method:
    @classmethod
    def addNewCar(cls):
        print("Enter the following details:")
        name = input("Name: ")
        price = int(input("Price: "))
        fuel = input("Fuel: ")
        return cls(name, price, fuel)

c1 = Car("Elantra", 2500000, "Petrol")

c2 = Car("Verna", 1200000, "Petrol")

c3 = Car("Fortuner", 3500000, "Diesel")




while True:
    print("Press:")
    print("1 to add new car")
    print("2 to display details of an exisiting car")
    print("3 to change details of an exisiting car")
    print("4 to delete an exisiting car")
    print("5 to exit")
    op = int(input())
    if op == 1:
        Car.addNewCar()

    elif op == 2:
        Car.showAllCars()
        c = int(input("Sr.No:"))
        Car.allCars[c].displayDetails()

    elif op == 3:
        Car.showAllCars()
        c = int(input("Sr.No:"))
        Car.allCars[c].changeDetails()

    elif op == 4:
        Car.showAllCars()
        c = int(input("Sr.No:"))
        Car.allCars.pop(c)
        pass

