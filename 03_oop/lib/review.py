#lambda functions are short annoyomous functions
add = lambda a,b: print(a + b)
add(10, 20)
# def add(a,b):
#     print(a+b)
# You can pass a lambda function to a higher order function
def multiply(num):
    return lambda n: num * n

double = multiply(10)
print(double(10))
#raising an error
# val = False
# if val == True:
#     print('Its True')
# else:
#     raise Exception("Not True")
# val = False
# if val == True:
#     print("True")
# else:
#     raise Exception("False")

# try:
#     console.log("")
# except SyntaxError:
#     print("console is not defined")
#everything in python is an object
# when you create something python will allocate memory and assign an id
x = []
y = []
print(x == y)
print(id(type(x)))
print(id(list))

