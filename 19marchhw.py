"""
1. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.
for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']
"""

"""

2. Create a Python program to generate user-defined set. ask uThen ser to eneter any value & check if the given value is present in a set or not.


new = set()
num = int(input("How many number you want to print:"))
i=0
for i in range(num):
    n =input("Enter any value:")
    new.add(n)
print(new)

check = input("Enter any value to check:-")

for i in new:
    if check == i:
        print("Value is present in set")
        break
else:
    print("Value is not present in set")

    """



"""
3. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.


l = []
for i in range(10):
    num = int(input(f"Enter {i+1} number"))
    l.append(num)
print("Normal list:",l)

rl = l[-1 :  :-1]
print("Reverse list:",rl)
"""



"""
4. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.


anto = {
    "right" : "left",
    "up" : "dowm",
    "create" : "destroy",
    "new" : "old"
}

anto1 = {
    "left" : "right",
    "down" : "up",
    "destroy" : "create",
    "old" : "new"
}

print(anto)
word = input("Enter any word from dictnory:")
new =anto.get(word)
if new != None:
    print(f"antonym of word {word} is {new}")
else:
    print(f"antonym of word {word} is {anto1[word]}")
"""



"""
5. Ask user to give name and marks of 10 different students. Store them in dictionary.
"""
# d = dict()
# i = 0
# for i in range(3):
#     name = input(f"Enter Name of student {i+1}:")
#     mark = int(input(f"Enter Marks of student {i+1}:"))
#     d.update({name : mark})

# print(d)


"""
6. Sort the above dictionary by the names of students.
"""

anto = {
    "right" : "left",
    "up" : "dowm",
    "create" : "destroy",
    "new" : "old"
}
print(anto.fromkeys())


"""
7. Sort the dictionary in ex-5 by the marks.
"""