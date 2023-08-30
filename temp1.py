from datetime import date

class Products():
    all_products = []
    country = "India"
    today = date.today()

    def __init__(self, name:str, cost_price, mrp, quantity:int):
        assert isinstance(name, str), "Name should be a string..."
        self.name = name

        assert isinstance(cost_price, float) or isinstance(cost_price,int), "Cost Price should be a Float..."
        self.cost_price = cost_price
        assert isinstance(mrp, float) or isinstance(mrp, int), "MRP should be a Float..."
        self.mrp = mrp
        
        assert isinstance(quantity, int) or int(quantity) == quantity, "Qunatity should be integer."
        assert quantity > 0, "Quantity should be greater than 0!"
        self.quantity = quantity
        Products.all_products.append(self)
        self.generateBarcode()

    def generateBarcode(self):
        # Format: YYYYMMCXXXX
        """
        YYYY: Year of purchase in 4 digits (to be fetched from the system date using datetime module)
        MM: Month of purchase in 2 digits (to be fetched from the system date using datetime module)
        C: category_code (E/G/F/T/C)
        XXXX: Index number in the list + 100
        """
        self.brcode = str(self.today.year).zfill(4) + str(self.today.month).zfill(2) + self.category_code + str(Products.all_products.index(self) + 100).zfill(4)
        self.index = int(self.brcode[-4::]) - 100

    @staticmethod
    def showInventory():
        print("SrNo\t\tItem Name")
        for item in Products.all_products:
            print(f"{item.brcode}\t{item.name}")
        barcode = input("Enter barcode no: ")
        index = int(barcode[-4:]) - 100
        return index


    def show_details(self):
        if self != None:   
            print(f"------------- Details of {self.name} -------------")
            print("Category:", self.category)
            print("Cost price:", self.cost_price)
            print("MRP:", self.mrp)
            print("Stock:", self.quantity)
            print("BRcode:", self.brcode)
            print(self.index)

    @staticmethod
    def addNewItem():
        print("Enter the following details:")
        name = input("Name: ")
        cost_price = float(input("Cost Price: "))
        mrp = float(input("MRP: "))
        quantity = int(input("Quantity: "))
        return name, cost_price, mrp, quantity
    
    def editDetails(self):
        print("Enter new details (Press 'Enter' to keep old detail):")
        print("Field\tOld Value\tNew Value".expandtabs(20))
        name = input(f"Name\t{self.name}:\t".expandtabs(20))
        if name != "": self.name = name

        category = input(f"Category\t{self.category}:\t".expandtabs(20))
        if category != "": 
            print("Sorry, cannot change category from here. You need to delete this object and create a new one in that category.")
        
        cost_price = input(f"Cost price\t{self.cost_price}:\t".expandtabs(20))
        if cost_price != "": self.cost_price = float(cost_price)

        mrp = input(f"MRP\t{self.mrp}:\t".expandtabs(20))
        if mrp != "": self.mrp = float(mrp)

        quantity = input(f"Stock\t{self.quantity}:\t".expandtabs(20))
        if quantity != "": self.quantity = int(quantity)

        month = input(f"Month\t{self.brcode[4 : 6]}:\t".expandtabs(20)).zfill(2)
        if month != "":
            self.brcode = self.brcode[ : 4] + month + self.brcode[6 : ]
        year = input(f"Year\t{self.brcode[ : 4]}:\t".expandtabs(20))

        if year != "":
            self.brcode = year + self.brcode[4 : ]


if __name__ == '__main__' :
    # p1 = Products("1234", 35.5, 50.5, 10)
    # p1.show_details()
    # p2 = Products("Sample product 1", 35.5, 50.5, 10)
    # p2.show_details()
    # s1 = 123
    # print(isinstance(s1, str))
    pass