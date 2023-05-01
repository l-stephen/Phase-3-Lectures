from lib.app import say_hello, pet_birthday
class TestHello:
    '''say_hello() in app.py'''
    def test_say_hello(self):
        assert say_hello() == "Hello World!"

class TestPetBirthday:
    '''pet_birthday in app.py'''

    def test_pet_birthday(self):
        '''returns pets age + 1'''
        assert(pet_birthday(10) == "Happy Birthday! Your pet is now 11")
    
