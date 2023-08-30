# string datatype
"""
a = "my string"
b = 'your string'
c = "c"
print(c, type(c))

length_of_a = len(a)
print("Length of a:", length_of_a)
"""

# concat
"""
print(a + " " + b)
"""

# string: Ordered & Immutable collection of characters

# d = 	"Marry Christmas to all of you and a very very HAPPY NEW YEAR!"
# index: 0123456789..................................................60
# -ve:	 ....................................................987654321

# print(len(d))

# Accessing through index
"""
print(d[8])
print(d[-8])
print(d[0])
"""
# slicing
"""
print(d[2 : 9])

print(d[6 : 60 : 2])
print(d[10 : ])
print(d[ : 50])
print(d[ : ])
print(d[10 : 50 : ])
print(d[ : : ])
print(d[ : : 3])

print(d[-59 : -52])
print(d[-10 : 10 : -1])
print(d[4 : -3])
print(d[ : : -1])
print(d[ : : -3])
print(d[ : : 0])
"""

# functions vs. methods

d = "Hello friends chay pilo"
"""
print(d)
type(d)
len(d)


# methods:

# Case-related methods

# capitalize(string)	wrong
e = d.capitalize()
print(e)
# print(d.upper())
# print(d.lower())
print(d.title())
print(d.swapcase())
print(d.casefold())
"""

# allignment related methods
"""
print(d.center(100))
print(d.center(100, "-"))
print(d.rjust(100))
print(d.rjust(100, "$"))
print(d.ljust(100))
print(d.ljust(100, "."))
"""

# count
"""
print(d.count('a'))
print(d.count('a', 6))
print(d.count('a', 6, 20))

print(d.count('very'))
print(d.count('very', 35))
print(d.count('very', 35, 42))
"""

# print(d.encode('utf-16'))

# Next Class: methods starting from endswith

#s1 = "Happy New Year! Wishing everyone of you a great 2023 ahead!"
"""
print(s1.endswith('!'))
print(s1.endswith('head!'))
print(s1.endswith('head..'))
print(s1.endswith('ear!', 0, 15))
print(s1.endswith('ahead!', 58))

print(s1.startswith('H'))
print(s1.startswith('h'))
print(s1.startswith('Hap'))
print(s1.startswith('Wish', 16))
print(s1.startswith('Wish', 16, 50))
"""
"""
print("Subject\t".expandtabs(30) + "Test1\tTest2\tFinal")
print("Maths\t".expandtabs(30) + "23\t20\t77")
print("Machine Learning\t".expandtabs(30) + "22\t19\t91")
print("C\t".expandtabs(30) + "24\t18\t72")
print("Environment\t".expandtabs(30) + "23\t25\t90")
print("C++\t".expandtabs(30) + "17\t22\t80")
print("Artificial Intelligence I\t".expandtabs(30) + "20\t24\t88")
print("Java\t".expandtabs(30) + "21\t23\t82")
print("Python\t".expandtabs(30) + "25\t25\t95")
"""
"""
print(s1.find('Y'))
print(s1.find('e'))
print(s1.find('e', 8))
print(s1.find('e', 12, 40))
print(s1.find('ing', -40, -4))
print(s1.find('z'))
print(s1.find('year'))
print("------------------")

print(s1.index('Y'))
print(s1.index('e'))
print(s1.index('e', 8))
print(s1.index('e', 12, 40))
print(s1.index('ing', -40, -4))
# print(s1.index('z'))
print("------------------")

print(s1.rfind('Y'))
print(s1.rfind('e'))
print(s1.rfind('e', 8))
print(s1.rfind('e', 12, 40))
print(s1.rfind('ing', -40, -4))
print("------------------")

print(s1.rindex('Y'))
print(s1.rindex('e'))
print(s1.rindex('e', 8))
print(s1.rindex('e', 12, 40))
print(s1.rindex('ing', -40, -4))
"""

# Methods starting from 'is': these will always return True/False
# print(s1.isupper())
# print(s1.islower())
# # print(s1.istitle())

# s1 = "Happy New Year!\nWishing everyone of you a great 2023 ahead! ©Alakh Pandya2023"

# s2 = "RoyalTechnosoft"
# print(s1.isalpha())
# print(s2.isalpha())

# s3 = "9825782290"
# print(s3.isnumeric())

# s4 = "RoyalTechnosoft9825782290"
# print(s4.isalnum())

# print(s2.isalnum())
# print(s3.isalnum())

# print(s3.isnumeric())

# print(s1.isascii())
# s5 = "fortryiselseifwhileelif"
# print(s5.isidentifier())
# print(s1.isprintable())
# s6 = "      \t\t          \t   \n       \n          \t        "
# print(s6.isspace())

s1 = "Happy New Year! Wishing everyone of you a great 2023 ahead!"
# print(s1.split())
# print(s1.split('a'))
# print(s1.split('a', 3))
# print(s1.rsplit('a'))
# print(s1.rsplit('a', 3))
# print(s1.split('everyone'))

# split_list = ['May', 'this', 'year', 'brings', 'you', 'everything', 'you', 'want!']
# s2 = "_".join(split_list)
# s2 = "\t".join(split_list)
# print(s2)

# print(s1.partition('everyone'))
# print(s1.partition('e'))
# print(s1.rpartition('e'))

# s2 = "                Happy New Year!!                                       "
# print(s2)
# print("Length =", len(s2))

# s3 = s2.lstrip()
# print(s3)
# print("Length =", len(s3))

# s4 = s2.rstrip()
# print(s4)
# print("Length =", len(s4))

# s5 = s2.strip()
# print(s5)
# print("Length =", len(s5))

s6 = "$$$$$$$$$$$$$$$$$$$$$Happy$New$Year!$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
# # print(s6.lstrip('$'))
# # print(s6.rstrip('$'))
# print(s6.strip('$'))
"""
"""
# s1 = "Hello"
# s2 = "Python!"
# print(s1 + s2)
# s1.__add__(s2)

# s3 = 5
# s4 = 10
# print(s3 + s4)
# s3.__add__(s4)
# s1 = "Hello friends chay pilo"
# print(s6.replace('$','-',2))
# s2 = s1.splitlines()
# print("Enter your date of birth (dd/mm):")
# dd = input("Date(dd): ")
# mm = input("Month(mm): ")
# print(f"Your next birthday will come on {dd.zfill(2)}/{mm.zfill(2)}/2023")


# Next Class: Lists

# HW: find out the difference between .isnumeric(), .isdigit() & .isdecimal()
# string examples for homework:

"""
1. Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. 
Example:
input: Alakh Janakkumar Pandya
output: A.J.Pandya

name = input("Enter Your Name:-")
n1 = name.title()
n2 = n1.split(" ")

f = n2[0]
n2[0] = f[:1:] 

s = n2[1]
n2[1] = s[:1:]
n3 = ".".join(n2)
print(n3)
"""

"""
2. Write a program to find the number of vowels, consonents and white space characters in a given string.
Example:
input string: Python Programming
output:
vowels: 4
whitel spaces: 1
consonents: 13

str = input("Enter a string:-")
str1 = str.lower()
s1 = int(str1.count('a'))
s2 = int(str1.count('e'))
s3 = int(str1.count('i'))
s4 = int(str1.count('o'))
s5 = int(str1.count('u'))
v = s1+s2+s3+s4+s5
s = str1.count(" ")
c = len(str1) - (v+s)
print(f"Vowels :- {v}")
print(f"whitel spaces :- {s}")
print(f"consonents :- {c}")
"""

"""
3. Write a program to make a new string with the word "the" deleted in the given string.
eg:
input string: This is the lion in the cage.
output: This is lion in cage.

str = input("Enter your string:-")
print("Input String:",str)
str1 = str.split('the ')
str2 = "".join(str1)
print("Output:",str2)
"""

"""
4. Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".
Example:
input string: Keep yourself mute while not speaking.
output: Keep_yourself mute while not#speaking.


str = input("Enter a string:-")
print("Input string:-",str)
str1 = str.split(" ",1)
str2 = "_".join(str1)
str3 = str2.rsplit(" ",1)
str4 = "#".join(str3)
print("Output:-",str4)
"""