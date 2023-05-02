#!/usr/bin/env python3
import numpy as np
import ipdb
#The python shebang is used to make a file executable
#To make the file executable run the command chmod +x /path/to/your/script.py
#Lastly, run the file in your terminal as follows: /path/to/your/script.py
#Todo 1: print a simple string and run the file in your terminal using the command python3 <filename> or the executable option
print("Hello, world!")

#Python Package Index
#To install packages use 'pip install package_name'
#Todo 2: Find a pip package from the PyPi library, install the package and use the package to perform a simple task
# https://pypi.org/ 

a =  np.array([1,2,3,4,6,7,8,9,10])
print(a)

#Debugging using ipdb
def addition(a,b):
    result = a + b
    #ipdb.set_trace()
    print(a)
    print(b)
    return result

a = 150
b = 200
sum = addition(a,b)
print(sum)

#Todo 3: Debugging the following code using ipdb
# add a set_trace() in the code, and when you are in the ipdb terminal print the a and b variables
def multiply(a,b):
    result = a * b
    #ipdb.set_trace()
    return result

x  = 10
y = 5
num = multiply(x,y)
print(num)

# You can also use the python shell and use print statements to debug code
#Todo 4: Create an error in your code and debug the code using the python shell and print statements

def divide(a,b):
    result = a / b
    return result

x = 10
y = 1
print(type(y))
division = divide(x,y)
print(division)
#Variables
#Todo 5: Create a variable and assign it to a value
name1 = None

pet_name = "Tracker"

#Global Variables
name2 = "John"

global name3 
name3 = "Sarah"

#Python Data Types
#Todo 6: Create a data type variable
#str
string_var = "Hello World!"
string_var2 = str("Hello")
print(string_var2)
#int
number = 10
number_2 = int(20)
print(number_2)
#float
float_number = 10.5
#bool
boolean = True
#None
null = None
#Tuple
tuple = ("hello", "world")
#Set
set_var = {"Hello", "World"}
#Dictionary
dict_var = {"Hello": "World"}
#list
lists = [1,2,3,4,5,6,7,8,9,10]
letters = ["a","b"]
alphabet = list("abc")
print(alphabet)
#Type Conversion
#Todo 7: Perform type conversion on a data type
new_string = str(number)
print(new_string)
print(type(new_string))

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
    print("the number is positive")

#Test if a string is empty
string = ""

if not string:
    print("The string is empty")

#Test if a number is positive or negative using an else
num2 = 20
if num2 > 0: 
    print("The number is positive")
else: 
    print("The number is negative")


#Test if a number is positve, negative, or zero, using if, elif, and else

num3 =0 
if num3 > 0:
    print("The number is positive")
elif num3 < 0:
    print("The numner is negative")
else:
    print("The number is zero")


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
#while condition:
    #statments
i = 1
while i <= 100:
    print(i)
    i += 1
#For Loop and Range
# for val in condition:
    #statements
fruits = ['Apple', "Orange", "Mango"]
for fruit in fruits:
    print(fruit)

# for val in range(6):
    #statements

for num in range(10):
    print("Printing: ", num)
#List Comprehension
#newlist = [expression for item in iterable if conditon == True]
newlist = [x for x in range(10) if x < 5]
print(newlist)
#String Interpolation example
name = "John"
age = 23
print(f"Hello, my name is {name} and I am {age} years old")
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
pet_status("Hungry")

def divide(a,b):
   # if b == 0:
     #  raise ZeroDivisionError("Cannot divide by zero")
    #return a/b

    try:
        result = a /b
        return result
    
    except ZeroDivisionError as e:
        print(e)

d = divide(10,0)
print(d)
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

pet_birthday()


