class Animal:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
        self.age = 0

    def petAnimal(self):
        print(f"Petting {self.name}")

class Friend():
    def __init__(self, name, status, duration):
        self.name = name
        self._status = status
        self.duration = duration

    @property
    def get_status(self):
        return self._status
    @get_status.setter
    def set_status(self, new_status):
        self._status = new_status

class Bird(Animal,Friend):
    def __init__(self, size, species, color, habitat, name, status, duration):
        # super().__init__(name)
        Friend.__init__(name, status, duration)
        Animal.__init__(name, color, size)
        self._species = species
        self.habitat = habitat

class Dog(Animal):
    def __init__(self, breed, name, color, age, size):
        super().__init__(name, color, size)
        self.breed = breed
        self.age = age

    def petAnimal(self):
        super().petAnimal()
        print(f"{self.name} is happy!")



pigeon=Bird("Small", "Pigeon", "Grey", "City", "Pie")
pigeon.petAnimal()
print(pigeon.size)
tracker = Dog("Golden", "Tracker", "Brown", 5, "large")
tracker.petAnimal()
print(tracker.size)
print(tracker.breed)