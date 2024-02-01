class Cocktails:
    all_bars = []
    def __init__(self, spirit, oz, name):
        self.spirit = spirit
        self.name = name
        self.oz = oz
        self.bars = []
        Cocktails.all_bars.append(self)
    
class Bar:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cocktails = []

    def build_menu(self, menu_arr):
        for item in menu_arr:
            if type(item) is Cocktails:
                self.cocktails.append(item)
                item.bars.append(self)


pony_up = Bar("Pony Up", "Blake St")
beacon = Bar("Beacon", "Rino")

rum_and_coke = Cocktails("Rum", 5, "rum & coke")
tequila_shot = Cocktails("Tequila", 3, "Shot")
pony_up.build_menu([rum_and_coke, tequila_shot])
print(pony_up.cocktails)
for c in pony_up.cocktails:
    print(f"We offer {c.name}")
print(rum_and_coke.bars)
for b in rum_and_coke.bars:
    print(f"find here {b.name}")
