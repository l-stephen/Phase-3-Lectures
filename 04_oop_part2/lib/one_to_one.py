class House:
    def __init__(self, roof_type, sqft, color, price):
        self.roof_type = roof_type
        self.sqft = sqft
        self.color = color
        self.price = price
        self._owner = None

    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, new_owner):
        if isinstance(new_owner, People):
            self._owner = new_owner
        else:
            raise ValueError("Owner must be a People object")
        
    def add_feature(self, feature):
        print(f"Adding {feature} to the house.")

    def is_eligible(self, person):
        try:
            if person.age >= 18:
                print(f"{person.name} is eligible")
        except:
            print(f"{person.name} is not eligible")


class People:
    def __init__(self, name, age):
        self.name = name
        try: 
            if age >= 18:
                self.age = age
        except:
            raise ValueError("Age must be greater than 18")
        self._house = None

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, new_house):
        if isinstance(new_house, House):
            self._house = new_house
            new_house.owner = self
        else:
            raise ValueError("Must select a house")
    
if __name__ == "__main__":
    stephen = People("Stephen", 17)
    house1 = House("Steel", 1000, "Grey", 100000)
    stephen.house = house1
    print(stephen.house.color)
    print(house1.owner.name)
    house1.add_feature("Hot tub")


    
