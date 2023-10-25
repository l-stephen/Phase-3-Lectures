#lambda functions are short annoyomous functions
add = lambda a,b: a + b
print(add(10, 20))
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

#everything in python is an object
# when you create something python will allocate memory and assign an id

x = []
y = []
print(x == y)
print(id(type(x)))
print(id(list))