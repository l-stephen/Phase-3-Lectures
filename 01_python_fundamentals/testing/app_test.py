# Import functions from the app
from lib.app import pet_birthday


#create tests that will test the functions
def test_pet_birthday():
     """Returns a string wishing the pet a happy birthday"""
     assert pet_birthday(5) == "Happy Birthday! Your pet is now 6"