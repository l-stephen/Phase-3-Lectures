class House:
    def __init__(self, roof_type, sqft, color):
        self.roof_type = roof_type
        self.sqft = sqft
        self.color = color
        self._owner = None
    
class People:
    def __init__(self, name, age):
        self.name = name
        if age >= 18:
            self.age = age
        self._house = None

    @property
    def get_house(self):
        return self._house
    
    @get_house.setter
    def set_house(self, new_house):
        if isinstance(new_house, House):
            self._house = new_house
            new_house.owner = self
        else:
            raise Exception("Not a house")

if __name__ == "__main__":
    stephen = People("Stephen", 28)

    stephens_house = House("Steel", 1000, "Grey")
    stephen.house = stephens_house
    print(stephen.house.color)
    stephens_house.owner = stephen
    print(stephens_house.owner.name)

        