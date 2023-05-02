from lib.app import pet_birthday
from lib.review import say_hello
class TestHelloWorld:
    '''say_hello() in review.py'''

    def test_say_hello(self):
        '''returns hello world'''
        assert(say_hello() == "Hello, world!")

class TestPetBirthday:
    '''pet_birthday in app.py'''

    def test_pet_birthday(self):
        '''returns pets age + 1'''
        assert(pet_birthday(10) == "Happy Birthday! Your pet is now 11")