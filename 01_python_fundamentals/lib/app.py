#!/usr/bin/env python3
#The python shebang is used to make a file executable
#To make the file executable run the command chmod +x /path/to/your/script.py
#Lastly, run the file in your terminal as follows: /path/to/your/script.py
#Todo 1: print a simple string and run the file in your terminal using the command python3 <filename> or the executable option

#Python Package Index
#To install packages use 'pip install package_name'
#Todo 2: Find a pip package from the PyPi library, install the package and use the package to perform a simple task
# https://pypi.org/ 


#Debugging using ipdb
#Todo 3: Debugging the following code using ipdb
# add a set_trace() in the code, and when you are in the ipdb terminal print the x and y variables
import ipdb

def multiply(a,b):
    result = a * b
    #ipdb.set_trace()
    return result

x  = '0'
y = 5
num = multiply(x,y)
print(num)

def addition(a,b):
    result = a + b
    #ipdb.set_trace()
    return result

a = 60
b = "hello"


# You can also use the python shell and use print statements to debug code
#Todo 4: Create an error in your code and debug the code using the python shell and print statements

#Variables
#Todo 5: Create a variable and assign it to a value

pet_name = "tracker"


#Global Variables

#Python Data Types
#Todo 6: Create a data type variable

#str
string_var = "hello world"
#int
number = 10
#float
float_number = 10.5
#bool
boolean = True
#None
null = None
#Tuple
tuple_var = ("hello", "world")
#Set
set_var = {"hello", "world"}
#Dictionary
dictionary_var = {"hello": "world"}
#List
list_var = ["hello", "world"]

#Type Conversion
#Todo 7: Perform type conversion on a data type
new_number = str(number)
print(type(new_number))

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
num = 10
if num > 0:
    print("The number is positive")


#Test if a string is empty
string = ""
if string == "":
    print("The string is empty")

#Test if a number is positive or negative using an else
num2 = 20
if num2 > 0:
    print("The number is positive")
else:
    print("The number is negative")

#Test if a number is positve, negative, or zero, using if, elif, and else
num3 = 0
if num3 > 0:
    print("The number is positive")
elif num3 < 0:
    print("The number is negative")
else:
    print("The number is zero")

#Test if a number is in between two numbers using the and operator
num4 = 10
if num4 > 0 and num4 < 20:
    print("The number is in between 0 and 20")
#Test if a number is positive, even, or both using logical operators
num5 = 10
if num5 > 0:
    print("The number is positive")
elif num5 % 2 == 0:
    print("The number is even")
elif num5 > 0 and num5 % 2 == 0:
    print("The number is positive and even")
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
    print("Tracker needs to be fed")
elif pet_mood == "Whinny":
    print("Tracker needs a walk")
else:
    print("Tracker is all good")

#Ternary
print("Tracker needs to be fed") if pet_mood == "Hungry" else print("Tracker needs a walk") if pet_mood == "Whinny" else print("Tracker is all good")
#While Loop
#while condition:
    # body of while loop
i = 1
while i < 6:
    print(i)
    i += 1
#For Loop and Range
#for val in condition:
    #statements
#for val in range(6):
    #statements

#List Comprehension
#newlist = [expression for item in iterable if condition == True]
#create a list comprehension example
newlist = [x for x in range(10) if x < 5]
print(newlist)
#String Interpolation example
#string interpolation example
name = "John"
age = 23
print(f"Hello, my name is {name} and I am {age} years old")

#Todo 9: Move conditional logic from Deliverable 1 into a function (pet_status) so that we may 
# use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
def pet_status():
    if pet_mood == "Hungry":
        print("Tracker needs to be fed")
    elif pet_mood == "Whinny":
        print("Tracker needs a walk")
    else:
        print("Tracker is all good")

#Todo 10: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"
def pet_birthday():
    pet_age = 10
    try:
        print("Happy Birthday! Your pet is now " + str(pet_age + 1))
    except TypeError:
        print("Type Error Occurred")

pet_birthday()
#Todo 11: Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"
def say_hello():
    return "Hello World!"

#Todo 13: Creating test in python
#install pytest
#pip install pytest
#create a testing folder and pytest file
#import modules
#create tests
#run tests

