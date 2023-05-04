class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport
        passport.set_owner(self)


class Passport:
    def __init__(self, number, expiration_date):
        self.number = number
        self.expiration_date = expiration_date
        self.owner = None

    def set_owner(self, person):
        self.owner = person


# Create a Person and a Passport object
p1 = Person("Alice", Passport("123456789", "2025-05-31"))

# Print the name and passport number of the Person
print("Name:", p1.name)
print("Passport number:", p1.passport.number)

# Print the name of the owner of the Passport
print("Passport owner:", p1.passport.owner.name)