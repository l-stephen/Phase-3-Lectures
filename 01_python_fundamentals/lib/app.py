#!/usr/bin/env python3
import numpy as np
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

#Variables
#Todo 5: Create a variable and assign it to a value

#Global Variables

#Python Data Types
#Todo 6: Create a data type variable

#str

#int

#float

#bool

#None

#Tuple

#Set

#Dictionary

#Type Conversion
#Todo 7: Perform type conversion on a data type

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

#Test if a string is empty

#Test if a number is positive or negative using an else

#Test if a number is positve, negative, or zero, using if, elif, and else

#Test if a number is in between two numbers using the and operator

#Test if a number is positive, even, or both

#Test if a string is empty or not

#Todo 8: Create a condition to check a pet's mood using an if/elif/else and a ternary
pet_name = "tracker"
pet_mood = "Hungry"
#If "pet_mood" is "Hungry!", "Tracker needs to be fed."
#If "pet_mood" is "Whinny ", "Tracker needs a walk"
#In all other cases, "Tracker is all good"

#While Loop

#For Loop and Range

#List Comprehension

#String Interpolation example

#Todo 9: Move conditional logic from Deliverable 1 into a function (pet_status) so that we may 
# use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"

#Todo 10: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

#Todo 11: Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"

#Todo 12: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

#Todo 13: Creating test in python

