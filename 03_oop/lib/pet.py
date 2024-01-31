#OOP is a programming paradigm based on the concepts of objects or dictionaries
#For example an object can represent a person and have properties like name, address
#Behavior or methods like walking, or running

#Benefits
#Code resuse, modualarity, readable, problem solving, inheritance

#Principles
# Single Responsibility Principle: 
    #classes in oop should have one responsibility, and methods should be aligned with that responsibility
# Separation of concern: 
    #The idea that the various responsibilities, or concerns, of a computer program should be separated
# Domain Modeling: 
    # A method to describe and model entities and the relationships between them
# Abstraction: 
    #representing complex real-world problems in a simplified manner by focusing on the most relevant aspects and ignoring the rest.
# Encapsulation: 
    #the idea of keeping the internal workings of an object hidden from the outside world.
# Inheritance: 
    #the ability for objects to inherit properties and behaviors from other objects.
# Polymorphism: the ability for objects to take on multiple forms

#Todo 1: Create a dog class, first use pass, and create an instance of the class
#Then use the __init__ to set attributes, and create an instance of the class
class Dog:
    #Global Variables
    dog_names = []
    species_list = []
    #__init__ will set the state when the class is created
    def __init__(self, species, name):
        self.name = name
        self.species = species
        self.food = []
        self.treats = 0
        self.dog_names.append(name)
# tracker = Dog("Tracker", "Golden")
# #instance
# print(tracker.species)
# #class
# print(Dog.dog_names)
        #append the species to the list, if the species is not in the list
        if species not in self.species_list:
            self.species_list.append(species)
       
    #Instance Methods
    #create a method to print the name
    def print_name(self):
        print(f"Hi , {self.name}\n")
   

    #create a method that will add to the number of cupcakes, only if the type is int and cupcakes is greater than 0
    #if cupcakes is less than 0, raise an error
    #if cupcakes is not a number, raise an error
    def eat_treats(self, num_treats):
        # if type(num_treats) is int and num_treats > 0:
        if isinstance(num_treats, int) and num_treats > 0:
            self.treats += num_treats
            # self.treats = self.treats + num_treats
        elif num_treats < 0:
            raise ValueError("Cannot be a negative number")
        else:
            raise TypeError("Not a number")
 
    #Properties
    #create a property that will get and set the name
    # def get_name(self):
    #     print("Getting the name")
    #     return self._name
    # def set_name(self, new_name):
    #     print(f"Setting the name to {new_name}")
    #     self._name = new_name
    #     return new_name
    # name = property(get_name, set_name)
    #To avoid calling get_name and set_name everytime we could use the python decorator property():https://www.programiz.com/python-programming/property 
    #This will set some code to a attribute of your class
    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, new_name):
    #     self._name = new_name

    #Class Methods
    #create a class method that will print all the dogs
    @classmethod
    def print_all_dogs(cls):
        print(cls.dog_names)

    @classmethod
    def add_new_species(cls, new_species):
        cls.species_list.append(new_species)
    #create a class method that will add a new species to the list
    
    #__repr__ will run when you print on the class
    def __repr__(self):
        return f"Name: {self.name}, Species: {self.species}"
    
if __name__ == "__main__":
#Todo 2: Instantiate a few dogs
    tracker = Dog("Golden Lab", "Tracker")
    boba = Dog("Golden Retriever", "Boba")
    boba.dog_names.append("Boba")
    print(boba)
    print(Dog.dog_names)
    tracker.medicine = []
    tracker.medicine.append("Advil")
    print(tracker.medicine)
    print(tracker)
    print(tracker.print_name())
    # print(tracker.eat_treats(-1))
    # print(tracker.eat_treats("s"))
    tracker.eat_treats(10)
    print(tracker.treats)
    # boba.name = "Buster"
    # print(boba)
    # print(boba.get_name())
    # boba.set_name("Buster")
    # print(boba)
    boba.name = "Buster"
    print(boba.name)
    Dog.print_all_dogs()
    Dog.add_new_species("Lab")
    print(Dog.species_list)
    tracker.add_new_species("Terrier")
    print(Dog.species_list)

#append a name to the list and print

#Todo 3: Creating a Global Variables
#create a new array of medicine and append a medicine to the list, print the results

#Todo 4: Create a method and print result

#Todo 5: Output of the __repr__

#Todo 6: use the property() method, to set and get 

#Todo 7: Decorators and CLS (@classmethod)








