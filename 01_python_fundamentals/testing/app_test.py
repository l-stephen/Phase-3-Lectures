# Import functions from the app
from lib.app import pet_birthday

#create tests that will test the functions
def test_pet_birthday():
     """Returns a string wishing the pet a happy birthday"""
     assert pet_birthday(5) == "Happy Birthday! Your pet is now 6"

# Define a test function with a descriptive name
def test_pet_birthday_increment_age():
    """Test if pet_birthday function increments pet's age correctly"""
    
    # Age increases by 1
    current_age = 5
    expected_age = current_age + 1
    assert pet_birthday(current_age) == f"Happy Birthday! Your pet is now {expected_age}", "Age should increase by 1"
