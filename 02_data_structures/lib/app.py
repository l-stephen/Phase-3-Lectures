#!/usr/bin/env python3
# Sequence Types

# Creating Lists
#1. ✅ Create a list of 10 pet names
def demo_lists():
    pet_names = ["Tracker", "Boba", "Willow", "Winry", "Ziggy", "Leo", "Lucy", "Abe", "Quinn", "Ruby"]
# Reading Information from Lists
# 2. ✅ Return the first pet name
    print("First pets name is ", pet_names[0])
# 3. ✅ Return all pet names beginning from the 3rd index
    print("Pet names from third index", pet_names[3:len(pet_names)-1])
#4. ✅ Return all pet names before the 3rd index
    print(f"Pet's before third index {pet_names[:3]}")
#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th]
    print("Pets from 3rd to 7th index", pet_names[3:7])
#6. ✅ Find the index of a given element
    print("Find index of pet ", pet_names.index("Leo"))
#7. ✅ Reverse the original list
    pet_names.reverse()
    print("Reversed List ", pet_names)
#8. ✅ Return the frequency of a given element 
    print("Number times this pet exists", pet_names.count("Boba"))
# Updating Lists
#9. ✅ Change the first element to all uppercase 
    print(pet_names[0].upper())
# Adding items to list
#10. ✅ Append a new name to the list
    pet_names.append("Franklin")
    pet_names.append("Blue")
    print(pet_names)
    new_pets_list = pet_names + ["Mini", "Lea"]
    print(new_pets_list)
    pet_names = pet_names[1:]
#11. ✅ Add a new name at a specific index

#12. ✅ Add two lists together 

# Removing 
#13. ✅ Remove the final element from the list
    print(pet_names.pop())
    print(pet_names.pop(1))

    print(pet_names)
    franklin = pet_names.pop()
    print(franklin)
    print(franklin.upper())
#14. ✅ Remove element by specific index

#15. ✅ Remove a specific element 
    print(pet_names.remove("Ziggy"))
    print(pet_names)
#16. ✅ Remove all pet names from the list
    # pet_names.clear()
    # print(pet_names)
    pet_names = pet_names[1:]
    print(pet_names)
demo_lists()
#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable
def demo_tuples():
#17. ✅ Create a Tuple of pet 10 ages 
    pet_ages = (2,3,4,5,6,7,8,9,10,51)
    print(pet_ages)
#18. ✅ Print the first pet age
    print(pet_ages[6])
    
# Testing Changeability 
#19. ✅ Attempt to remove an element with .pop (should error)
# -> AttributeError: 'tuple' object has no attribute 'pop'
    # print(pet_ages.pop())

#20. ✅ Attempt to change the first element (should error)
# -> TypeError: 'tuple' object does not support item assignment
    # pet_ages[0] = 6
    # print(pet_ages)

# Tuple Methods
#21. ✅ Return the frequency of a given element
    print(pet_ages.count(6))

#22. ✅ Return the index of a given element 
    print(pet_ages.index(51))
    # print(pet_ages.__contains__(10))
#23. ✅ Create a range 
#Note Ranges are primarily used in loops
    range1 = range(100)
    print(range1)
    range2 = range(90, 100, 2)
    print(range2)
# Demo Sets (stretch goal)
#24. ✅ Create a set of 3 pet foods
    pet_foods = {"Purina", "Open Farm", "Puppy Chow", "Purina"}
    
    print(pet_foods)

# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys name, age and breed
def demo_dict():
    pet_info_tracker = {"name": "Tracker", "age": 5, "breed": "Golden Lab"}
    print(pet_info_tracker)
    #26. ✅  Use dict to create a dictionary of pet information with the keys name, age and breed
    print(pet_info_tracker["age"])
    print(pet_info_tracker.get("breed"))
    print(pet_info_tracker.keys())
    print(pet_info_tracker.values())

# Reading
#27. ✅ Print the pet attribute of name using bracket notation 

#28. ✅ Print the pet attribute of age using .get
#Note: get is preferred over bracket notation in most cases because it will return none instead of an error

# Updating 
#29. ✅ Update the pets age to 12
    pet_info_tracker["age"] = 6
    print(pet_info_tracker)
    pet_info_tracker.update({"age": 7})
    print(pet_info_tracker)

#30. ✅ Update the other pets age to 26
    del pet_info_tracker['age']
    print(pet_info_tracker)
    pet_info_tracker.pop("breed")
    print(pet_info_tracker)
    pet_info_tracker.popitem()
    print(pet_info_tracker)

# Deleting
#30. ✅ Delete a pets age using the del keyword 
#31. ✅ Delete the other pets age using the .pop 
#32. ✅ Delete the last item in the pet dictionary using popitem()
def demo_loops():
# Demo Loops 
    
    pet_names = ["Tracker", "Boba", "Willow", "Winry", "Ziggy", "Leo", "Lucy", "Abe", "Quinn", "Ruby"]
    pet_info = [
        {
            'name':'rose',
            'age':11,
            'breed': 'domestic long-haired',
        }, 
        {
            'name':'spot',
            'age':25,
            'breed': 'boxer',
        },
        {
            'name':'Meow Meow Beans',
            'age':2,
            'breed': 'domestic long-haired',
        }
        ]
#33. ✅ loop through a range of 10 and print every number within the range
    for _ in range(100):
        print(_)

    for num in range(100):
        print(num)

    for num in range(50, 100, 2):
        print(num)

    for pet in pet_info:
        print(pet)


#34. ✅ loop through a range between 50 and 60 that iterates by 2 and print every number


#35. ✅ Loop through the pet_info list and print every dictionary  


#36. ✅ Create a function that takes a list as an argument. 
    # The function should use a for loop to loop through the list and print every item in the list 
    # Invoke the function and pass it pet_names as an argument
    def print_pets(list):
        for item in list:
            print(item)
    print_pets(pet_names)



#37. ✅ Create a function that takes a list as an argument.(simple example) 
    # The function should define a counter and set it to 0
    # Create a while loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # return the counter 
    def count(list):
        counter = 0
        while(counter < len(list)):
            counter += 1
            # counter = counter + 1
        return counter
    print(count(pet_info))
        


#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of dicts, name and age as parameters 
        # Create a index variable and set it to 0
        # Create a while loop. 
            # The loop will continue so long as the list does not contain a name matching the name param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found update the items age with the new age 
        # else return 'pet not found'
    def update_age(dict, name, age):
        index = 0
        while(dict[index].get("name") != name and index < len(dict)-1):
            index +=1
        
        if dict[index].get("name")  == name:
            dict[index]["age"] = age
            return dict[index]
        else:
            return "Pet Not Found"
    print(update_age(pet_info, "Buster", 1))
    print(pet_info)

# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from pet_info changed to uppercase
    pet_name_upper = [pet.get('name').upper() for pet in pet_info]
    print(pet_name_upper)
    pet_name_upper = [pet["name"].upper() for pet in pet_info]
    print(pet_name_upper)
# find like
#40. ✅ Use list comprehension to find a pet named spot
    find_pet = [pet for pet in pet_info if pet["name"] == "spot"]
    print(find_pet)

# filter like
# 41. ✅ Use list comprehension to find all of the pets under 3 years old
    young_pets = [pet for pet in pet_info if pet["age"] < 3]
    print(young_pets)
# 43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension.
    young_pets_generator = (pet for pet in pet_info if pet.get("age") > 2)
    print(young_pets_generator)
demo_tuples()
demo_dict()
demo_loops()

def uppercase_decorator(func):

    def return_name(name):
        result = func(name)
        return result.upper()
    
    return return_name

def reverse_decorator(func):
    def reverse(name):
        result = func(name)
        return result.lower()
    return reverse
    
@reverse_decorator
def greeting(name):
    return f"Hello, {name}!"

print(greeting("Stephen"))


