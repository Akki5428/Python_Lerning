"""
party = {
    "Vivek" : "Pizza",
    "Ayush" : 23,
    "Jay" : ["Soup", "Main Course", "Gulab Jamun"],
    "Rishi" : ("Dosa", "Pepsi"),
    "Alakh" : {"Dosa", "Pepsi"},
    "Dhiraj" : frozenset({"Rotlo", "Gud", "Buttermilk"}),
    "Marlin" : {"BF" : "Sandwich", "Lunch" : "Punjabi", "Dinner" : "Pau Bhaji"}
}

name = input("Enter Name:")
print(f"\n{name} : {party[name]}")

name = input("Enter Name:")
name1 = name.capitalize()
print(f"\n{name} : {party[name1]}")

name = input("Enter Name:").capitalize()
i = 0
if name != "Vivek" and name != "Ayush" and name != "Marlin":
    for i in party[name]:
         print(i)
elif name == "Marlin":
    time = input("Enter your Time (BF,Lunch,Dinner):")
    print(party[name][time])         
else:
     print(party[name])

"""

consumers = ["Darshan", "Nishkal", "Vidhi", "Devanshi", "Harsh"]
new = dict.fromkeys(consumers,1000)
print(new)
