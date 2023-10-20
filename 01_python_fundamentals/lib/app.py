#!/usr/bin/env python3
import numpy as np
import ipdb

#The python shebang is used to make a file executable
#To make the file executable run the command chmod +x /path/to/your/script.py
#Lastly, run the file in your terminal as follows: /path/to/your/script.py
#Todo 1: print a simple string and run the file in your terminal using the command python3 <filename> or the executable option
print("Hello, World!")

#Pipenv - package and virtual environment tool, uses a pipfile and pipfile.lock, think of node npm
#Use pipenv install to generate a Pipfile and Pipfile.lock
#This will create a virtual environment using the packages in your pipfile and pipfile lock
#Genereate virtual enviroment with 'pipenv shell'
#Exit your virtual environment with 'exit' or 'pipenv --rm'

#Python Package Index
#To install packages to your computer use 'pip install package_name'
#To install packages to your virtual environment use 'pipenv install package_name'
#Todo 2: Find a pip package from the PyPi library, install the package and use the package to perform a simple task
# https://pypi.org/ 

new_array = np.arange(16)
print(new_array)

#Debugging
#To enable ipdb debugging, import ipdb
#ipdb.set_trace() will set a breakpoint
# You can also use the python shell & print statements to debug code
#Todo 4: Create an error in your code and debug the code using the python shell & print statements
#new 
ipdb.set_trace()

#Variables
#Todo 5: Create a variable and assign it to a value
pet_name = "Tracker"
#Global Variables
pet_name2 = "Boba"

#Python Data Types
#Todo 6: Create a data type variable

#str
string_var = "this is a string"
print(string_var)
string_var2 = str("this is created with str function")
print(string_var2)
#int
number = 10
print(number)
number2 = int(20)
print(number2)
#float
floating_num = 10.50
print(floating_num)
#bool
truthy = True
print(truthy)
falsy = False
print(falsy)
#None
null = None
print(null)
#Tuple - Cannot change once it is assigned
my_tuple = (1, "tuple", [10, 20, 30, 40])
print(my_tuple)
#Set - Unordered, unchangeable, does not allow duplicates
fruit_set = {"apple", "banana", "cherry", "apple"}
print(fruit_set)
#Dictionary
my_dict = {
    "make": "Polestar",
    "model": "S",
    "Year": 2022,
    "colors": ["black", "white", "grey"]
}
print(my_dict)
print(my_dict["colors"])

#Type Conversion
#Todo 7: Perform type conversion on a data type
age = 28
str_age = str(age)
print(type(str_age))
#Python Conditionals and Control Flow

#Syntax of Conditionals

#if statement
#if condition:
    #statement if the condition is true

#if/else syntax
#if condition:
#else:

#if/elif/else syntax
#if condition:
#elif:
#elif:
#else:

#Syntax of a ternary
#[option1] if [condition] else [option2]

#Comparison Operators:
# == : Equal to
# != : Not equal to
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to

#Logical Operators
#and, or, not

#Conditionals and Control Flow

#Test if a number is positive
if age > 0:
    print("Positive")
#Test if a string is empty
string = ""
if not string:
    print("Empty")
#Test if a number is positive or negative using an else
if age > 0: 
    print("Positive")
else:
    print("Negative")
#Test if a number is positve, negative, or zero, using if, elif, and else
if age > 0: 
    print("Positive")
elif age < 0:
    print("Negative")
else:
    print("Zero")
#Test if a number is in between two numbers using the and operator
num4 = 10
if num4 > 0 and num4 < 20:
    print("The number is between 10 and 20")
#Test if a number is positive, even, or both
num5 = 10

if num5 > 0 and num5 % 2 == 0:
    print("The number is positive and even")
elif num5 > 0:
    print("The number is positive")
elif num5 % 2 == 0:
    print("The number is even")
else:
    print("The number is negative and odd")

#Test if a string is empty or not
string2 = "hello"

if string2 == "":
    print("The string is empty")
else:
    print("The string is not empty")
#Todo 8: Create a condition to check a pet's mood using an if/elif/else and a ternary
pet_name = "tracker"
pet_mood = "Hungry"
#If "pet_mood" is "Hungry!", "Tracker needs to be fed."
#If "pet_mood" is "Whinny ", "Tracker needs a walk"
#In all other cases, "Tracker is all good"

if pet_mood == "Hungry":
    print('Tracker needs to be fed')
elif pet_mood == "Whinny":
    print("Tracker needs a walk")
else:
    print("Tracker is all good")

print("Trackers need to be fed") if pet_mood == "Hungry" else print("Tracker needs a walk") if pet_mood == "Whinny" else print("Tracker is all good")


#While Loop
i = 1
while i <= 100:
    print(i)
    i += 1

#For Loop and Range
fruits = ['Apple', "Orange", "Mango"]
for fruit in fruits:
    print(fruit)

for num in range(10):
    print("Printing: ", num)
#List Comprehension
newlist = [x for x in range(10) if x < 5]
print(newlist)
#String Interpolation example
name = "programmers"
program = "python"
print(f"Hello {name} this is {program} %s")
#Todo 9: Move conditional logic from Deliverable 1 into a function (pet_status) so that we may 
# use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
def pet_status(pet_moods):
    if pet_moods == "Hungry":
        print('Tracker needs to be fed')
    elif pet_moods == "Whinny":
        print("Tracker needs a walk")
    else:
        print("Tracker is all good")

pet = "Hungry"
ipdb.set_trace()
pet_status("Hungry")
#Todo 10: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

def pet_birthday():
    pet_age = "10"
    try:
        print("Happy Birthday! Your pet is now " + str(pet_age + 1))

    except TypeError:
        print("Type error occured")

pet_birthday("wrong")

