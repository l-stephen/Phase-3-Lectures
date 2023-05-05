# Create a class
class Dog:
    #global variable
    doglist = []
    #initialize properties
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.doglist.append(name)

    # Create a method
    def bark(self):
        print("Woof")
    
    def get_name(self):
        print("Getting name")
        return self._name
    def set_name(self, new_name):
        if type(new_name) is str:
            self._name = new_name

        else:
            raise Exception(f"{new_name} is not a valid name")
    name = property(get_name, set_name)

    @classmethod
    def printalldogs(cls):
        print(cls.doglist)
        

tracker = Dog("Tracker", "Retriever", 4)
print(tracker.bark())
print(tracker.get_name())
tracker.printalldogs()

from datetime import datetime

def log_date(func):
    def display():
        print(f'Current Time: {datetime.today()}')
        func()
    
    return display

@log_date
def display_date():
    print("This is the date")

display_date()

#Environment setup
#pyenv is a virtual environment manager for python, that allows you to install different versions of python and switch between them
#How to Install: https://github.com/pyenv/pyenv#installation 
#run pyenv versions to see the versions of python you have installed
#pyenv versions

#pyenv install -l to see diffent versions of python you can install

#to install a specific version use pyenv install 3.9.2
#to set globally pyenv global 3.9.2

#pipenv
# tool that provides all necessary means to create a virtual environment for your Python project. 
# It automatically manages project packages through the Pipfile file as you install or uninstall packages.

#create a virtual environment
#pipenv --python 3.8.13

#Pipfile is a file that contains the information about your project dependencies
#Pipfile.lock is a file that contains the information about your project dependencies and their versions

#install a library into the virtual environment
#pipenv install requests
#pipenv install requests==2.26.0 to use a specific version
#pipenv --venv to see the path to the virtual environment

#pipenv allows you to install dependecies, modules that are not needed in production, but are useful to develop and test your code
#pipenv install pytest --dev

#pipenv shell to activate the virtual environment
#you can also import packages into your virtual environment and use them to test your code

#pipenv --rm to remove the virtual environment

#pipenv install to create a new virtual environment

#pipenv run python <filename> to run a file in the virtual environment
