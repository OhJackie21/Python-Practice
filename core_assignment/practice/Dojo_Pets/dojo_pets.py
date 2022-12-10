
class Ninja:
    #implement 
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        	
    
# implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print("Pet is walking")

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print("Pet is eating")
    
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print("Pet is takinG a bath")

class Pet(Ninja):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0


    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        pass
    # eat() - increases the pet's energy by 5 & health by 10
    def eat():
        pass
    # play() - increases the pet's health by 5
    def play():
        pass
    # noise() - prints out the pet's sound
    def noise():
        pass


    