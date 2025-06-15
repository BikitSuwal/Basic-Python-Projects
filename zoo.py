#zoo management System

class animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Some generic animal sound"

class lion(animal):
    def make_sound(animal):
        return "Roar"

class tiger(animal):
    def make_sound(animal):
        return "Grrr"

class elephant(animal):
    def make_sound(animal):
        return "Trumpet"

class monkey(animal):
    def make_sound(animal):
        return "Ooh Ooh Aah Aah"
    
class zebra(animal):
    def make_sound(animal):
        return "Neigh"
    
class giraffe(animal):
    def make_sound(animal):
        return "Hum"
    
def animal_show(animals):
    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")


zoo = [
    lion("Shiha"),
    tiger("Baagh"),
    elephant("Hati"),
    monkey("Badar"),
    zebra("jbra"),
    giraffe("grafe")
    ]

animal_show(zoo)
    


