from pet import Dog

tracker = Dog()

pet_info = [
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

pet_info_2 = [
    {
        'name':'Bud',
        'age':5,
        'breed': 'golden retriever',
    }, 
    {
        'name':'Princess Grace',
        'age':9,
        'breed': 'persian',
    },
    {
        'name':'WiFi',
        'age':4,
        'breed': 'wolf',
    }
]

# List Comprehensions => []
#Shorter syntax to create a new list based on the values of an existing list
# map like 
#Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
pet_names = [pet.get("name").upper() for pet in pet_info]
print(pet_names)
# find like
#Use list comprehension to find a pet named spot
spot = [pet for pet in pet_info if pet.get("name") == "Spot"]
print(spot)
# filter like
#Use list comprehension to find all of the pets under 3 years old
young_pets = [pet for pet in pet_info if pet.get("age") < 3]
print(young_pets)
# Generator Expression => (expression for item in iterable)
# A function that returns an iterator that produces a sequence of values when iterated over
# We can make a generator expression by putting list comprehension in parenthesis
# Or create a generator object with the yield keyword
# Main Benefit => Less Memory Intensive

#Create a generator expression and generator matching the filter above
def my_gen():
    for pet in pet_info:
        if pet.get("age") < 3:
            #produce the current value
            yield pet

gen = my_gen()
print(next(gen))

gen = (pet for pet in pet_info if pet.get("age") < 3)

for i in gen:
    print(i)



