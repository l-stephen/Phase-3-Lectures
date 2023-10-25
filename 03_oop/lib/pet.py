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
    def __init__(self,species,name):
        self.name = name
        self.species = species
        self.food = []
        self.toys = 0
        self.dog_names.append(name)
        #append the species to the list, if the species is not in the list
        if species not in self.species_list:
            self.species_list.append(species)
    #Instance Methods
    #create a method to print the name
    def printname(self):
        print(self.name)

    #create a method that will add to the number of toys, only if the type is int and toys is greater than 0
    #if toys is less than 0, raise an error
    #if toys is not a number, raise an error
    def eat_cupcakes(self, num_toys):
        if type(num_toys) is int and num_toys > 0:
            self.toys += num_toys
        elif num_toys < 0:
            raise TypeError("Cannot be 0 or below")
        else:
            raise TypeError("Not a number!")
    #Properties
    # #create a property that will get and set the name
    # def get_name(self):
    #     print('Getting the name')
    #     return self._name
    # def set_name(self,new_name):
    #     print(f'Setting name to {new_name}')
    #     self._name = new_name
    # #To avoid calling get_name and set_name everytime we could use the python decorator property():https://www.programiz.com/python-programming/property 
    # #This will set some code to a attribute of your class
    # name = property(get_name, set_name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    #Class Methods
    #create a class method that will print all the dogs
    @classmethod
    def print_all_dogs(cls):
        print(cls.dog_names)

    @classmethod
    #create a class method that will add a new species to the list
    def add_new_species(cls, species):
        cls.species_list.append(species)

    #__repr__ will run when you print on the class
    def __repr__(self):
        return f'Name: {self.species_list}, species: {self.species}'

if __name__ == "__main__":
    #Todo 2: Instantiate a few dogs
    tracker =  Dog("Golden Retriever", "Tracker")
    franklin = Dog("Toy Yorkie", "Franklin")
    brindle = Dog("Shis Tzu", "Brindle")
    #append a name to the list and print
    tracker.dog_names.append("Scout")
    print(tracker)
    #Todo 3: Creating a Global Variables
    #create a new array of medicine and append a medicine to the list, print the results
    franklin.medicine = []
    franklin.medicine.append("Advil")
    print(franklin.medicine)
    #Todo 4: Create a method and print result
    print(tracker.toys)
    tracker.eat_cupcakes(5)
    print(tracker.toys)
    #Todo 5: Output of the __repr__
    print(tracker)
    #Todo 6: use the property() method, to set and get 
    brindle.name = "Boba"
    print(brindle.name)

    tracker.add_new_species("Labrador")
    print(Dog.species_list)
    print(brindle.species_list)