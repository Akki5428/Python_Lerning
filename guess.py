import random

value = random.randrange(101)

while True:
    num = int(input("\nChalo number nakho: "))
    if value > num:
        print("\nkhoto chhe moto nakh")
    elif value < num:
        print("\nkhoto chhe nano nakh")
    else:
        print("\nWahh Dhokla Tu jiti gyo")
        break


